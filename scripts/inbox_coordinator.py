#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/inbox_coordinator.py
============================
Read all inbox sources and group items by source type into a processing manifest.

Scans inbox/links.md, inbox/youtube.md, inbox/twitter.md, inbox/posts.md,
and inbox/clippings/ — skipping URLs already in .state/processed_urls.json.
Writes the manifest to .state/inbox_manifest.json for downstream consumers
(parallel_fetch.py, wiki-inbox-parallel command).

Usage:
    python scripts/inbox_coordinator.py [--dry-run] [--json]
"""

import io
import json
import sys
import re
import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Helpers (from _template.py)
# ---------------------------------------------------------------------------

def read_text(path) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def write_json(path, data, indent: int = 2) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
        f.write("\n")


def log(msg: str, level: str = "INFO") -> None:
    safe = msg.encode("ascii", errors="replace").decode("ascii")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {level}: {safe}", file=sys.stderr)


# ---------------------------------------------------------------------------
# State helpers
# ---------------------------------------------------------------------------

URL_RE = re.compile(r'https?://\S+')

SUBREDDITS = [
    "GithubCopilot", "opencodeCLI", "opencode", "ClaudeCode", "ZaiGLM",
    "kimi", "AI_Agents", "LocalLLaMA", "MachineLearning", "singularity",
    "ChatGPT", "ChatGPTCoding", "ollama", "vibecoding", "DeepSeek", "Qwen_AI",
]

ACADEMIC_DOMAINS = [
    "arxiv.org", "semanticscholar.org", "papers.nips.cc",
    "openreview.net", "aclanthology.org", "proceedings.mlr.press",
]


def load_processed_urls() -> set:
    p = Path(".state/processed_urls.json")
    if p.exists():
        data = json.loads(p.read_text(encoding="utf-8"))
        # Support both plain-list format (legacy) and {"urls": [...]} dict format
        if isinstance(data, list):
            return set(data)
        return set(data.get("urls", []))
    return set()


def _clean_url(raw: str) -> str:
    """Strip trailing punctuation artifacts from regex captures."""
    return raw.rstrip(").,\"'>")


def _in_done_section(line: str, flag: bool) -> bool:
    """Return updated in-done flag given the current line."""
    return flag or bool(re.match(r"^#+\s*Done", line.strip(), re.IGNORECASE))


# ---------------------------------------------------------------------------
# Per-source scanners
# ---------------------------------------------------------------------------

def scan_links(path: str, processed: set) -> list:
    p = Path(path)
    if not p.exists():
        return []
    items = []
    in_done = False
    for line in p.read_text(encoding="utf-8").splitlines():
        in_done = _in_done_section(line, in_done)
        if in_done:
            continue
        m = URL_RE.search(line)
        if not m:
            continue
        url = _clean_url(m.group(0))
        if url in processed:
            continue
        is_academic = any(d in url for d in ACADEMIC_DOMAINS)
        items.append({
            "type": "paper" if is_academic else "link",
            "url": url,
            "source_file": path,
        })
    return items


def scan_youtube(path: str, processed: set) -> list:
    p = Path(path)
    if not p.exists():
        return []
    items = []
    in_done = False
    for line in p.read_text(encoding="utf-8").splitlines():
        in_done = _in_done_section(line, in_done)
        if in_done:
            continue
        m = URL_RE.search(line)
        if not m:
            continue
        url = _clean_url(m.group(0))
        if ("youtube.com" in url or "youtu.be" in url) and url not in processed:
            items.append({"type": "youtube", "url": url, "source_file": path})
    return items


def scan_twitter(path: str, processed: set) -> list:
    p = Path(path)
    if not p.exists():
        return []
    items = []
    in_done = False
    for line in p.read_text(encoding="utf-8").splitlines():
        in_done = _in_done_section(line, in_done)
        if in_done:
            continue
        m = URL_RE.search(line)
        if not m:
            continue
        url = _clean_url(m.group(0))
        if ("twitter.com" in url or "x.com" in url) and url not in processed:
            items.append({"type": "twitter", "url": url, "source_file": path})
    return items


def scan_clippings(directory: str, processed: set) -> list:
    p = Path(directory)
    if not p.exists():
        return []
    items = []
    for f in sorted(p.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        # Prefer front-matter url: field; fall back to first URL in body
        fm_match = re.search(r"^url:\s*(.+)$", text, re.MULTILINE)
        url = fm_match.group(1).strip() if fm_match else ""
        if not url:
            m = URL_RE.search(text)
            url = _clean_url(m.group(0)) if m else str(f)
        if url in processed:
            continue
        is_academic = any(d in url for d in ACADEMIC_DOMAINS)
        items.append({
            "type": "paper" if is_academic else "clipping",
            "url": url,
            "file": str(f),
            "source_file": str(f),
        })
    return items


def scan_posts(path: str) -> list:
    p = Path(path)
    if not p.exists():
        return []
    text = p.read_text(encoding="utf-8")
    # Drop everything from ## Done onward
    done_match = re.search(r"^#+\s*Done", text, re.MULTILINE | re.IGNORECASE)
    if done_match:
        text = text[:done_match.start()]
    # Remove the ## To Process heading
    text = re.sub(r"^#+\s*To Process\s*$", "", text, flags=re.MULTILINE)
    blocks = [b.strip() for b in text.split("---") if b.strip()]
    return [
        {"type": "post", "text": block, "source_file": path}
        for block in blocks
        # Skip template header text and trivially short blocks
        if len(block) >= 50 and not block.startswith("#")
    ]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(
        description="Group inbox items by source type into .state/inbox_manifest.json"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Print manifest without writing to disk")
    parser.add_argument("--json", action="store_true",
                        help="Emit manifest JSON to stdout")
    args = parser.parse_args()

    processed = load_processed_urls()
    log(f"Loaded {len(processed)} processed URLs from state")

    groups: dict = {
        "link":     scan_links("inbox/links.md", processed),
        "youtube":  scan_youtube("inbox/youtube.md", processed),
        "twitter":  scan_twitter("inbox/twitter.md", processed),
        "clipping": [],
        "paper":    [],
        "post":     scan_posts("inbox/posts.md"),
        "reddit":   [{"type": "reddit", "subreddit": r} for r in SUBREDDITS],
    }

    # Clippings may contain either clipping or paper entries
    for item in scan_clippings("inbox/clippings", processed):
        groups[item["type"]].append(item)

    totals = {k: len(v) for k, v in groups.items()}
    manifest = {
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "groups": groups,
        "totals": totals,
        "total_items": sum(totals.values()),
    }

    log("Inbox manifest:")
    for group, count in totals.items():
        if count > 0:
            log(f"  {group:10s}: {count} item(s)")
    log(f"  {'TOTAL':10s}: {manifest['total_items']}")

    if not args.dry_run:
        write_json(".state/inbox_manifest.json", manifest)
        log("Manifest written to .state/inbox_manifest.json")

    if args.json or args.dry_run:
        print(json.dumps(manifest, ensure_ascii=False, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
