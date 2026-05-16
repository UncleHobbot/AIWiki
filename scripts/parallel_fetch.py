#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/parallel_fetch.py
=========================
Fetch all inbox items in parallel using ThreadPoolExecutor — one thread per
item, bounded by --workers.  Results are cached in .state/fetch_cache/ so
re-runs are instant for already-fetched content.

Architecture
------------
  Coordinator (inbox_coordinator.py) -> manifest (.state/inbox_manifest.json)
                                             |
              ┌──────────────────────────────┴──────────────────────────────┐
              │         ThreadPoolExecutor(max_workers=N)                    │
              │   Worker-link  Worker-youtube  Worker-twitter  Worker-paper  │
              │        │             │               │               │       │
              └──────────────────────────────────────────────────────────────┘
                       ↓             ↓               ↓               ↓
              .state/fetch_cache/<type>/<hash>.json  (one file per item)
                                             |
                              Merge step: .state/fetch_results.json

Usage:
    python scripts/parallel_fetch.py [--manifest .state/inbox_manifest.json]
                                     [--workers 8]
                                     [--types link,youtube,twitter,clipping,paper,post,reddit]
                                     [--no-cache]
                                     [--dry-run]
"""

import io
import json
import sys
import subprocess
import hashlib
import datetime
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_json(path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data, indent: int = 2) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
        f.write("\n")


def log(msg: str, level: str = "INFO") -> None:
    safe = msg.encode("ascii", errors="replace").decode("ascii")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {level}: {safe}", file=sys.stderr)


CACHE_DIR = Path(".state/fetch_cache")


def _cache_key(item: dict) -> str:
    """Stable 12-char hash key for an inbox item."""
    seed = item.get("url") or item.get("subreddit") or item.get("text", "")
    return hashlib.md5(seed.encode("utf-8")).hexdigest()[:12]


def _cache_path(item_type: str, key: str) -> Path:
    return CACHE_DIR / item_type / f"{key}.json"


def _is_cached(item_type: str, key: str) -> bool:
    return _cache_path(item_type, key).exists()


def _load_cache(item_type: str, key: str) -> dict:
    return read_json(str(_cache_path(item_type, key)))


def _save_cache(item_type: str, key: str, data: dict) -> None:
    write_json(str(_cache_path(item_type, key)), data)


# ---------------------------------------------------------------------------
# Type-specific fetch workers
# ---------------------------------------------------------------------------

def _run(cmd: list, timeout: int = 60) -> tuple:
    """Run a subprocess, return (returncode, stdout, stderr)."""
    try:
        r = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return 1, "", f"timeout after {timeout}s"
    except Exception as exc:
        return 1, "", str(exc)


def fetch_link(item: dict) -> dict:
    rc, out, err = _run([sys.executable, "scripts/fetch_url.py", item["url"]], timeout=30)
    return {
        "url": item["url"],
        "type": "link",
        "content": out,
        "success": rc == 0 and bool(out.strip()),
        "error": err.strip() or None,
    }


def fetch_paper(item: dict) -> dict:
    result = fetch_link(item)
    result["type"] = "paper"
    return result


def fetch_youtube(item: dict) -> dict:
    rc, out, err = _run([sys.executable, "scripts/fetch_youtube.py", item["url"]], timeout=120)
    data: dict = {}
    if rc == 0 and out.strip():
        try:
            data = json.loads(out)
        except json.JSONDecodeError:
            data = {"raw": out}
    return {
        "url": item["url"],
        "type": "youtube",
        "content": data,
        "success": rc == 0,
        "error": err.strip() or None,
    }


def fetch_twitter(item: dict) -> dict:
    rc, out, err = _run([sys.executable, "scripts/fetch_twitter.py", item["url"]], timeout=30)
    data: dict = {}
    if rc == 0 and out.strip():
        try:
            data = json.loads(out)
        except json.JSONDecodeError:
            data = {"raw": out}
    return {
        "url": item["url"],
        "type": "twitter",
        "content": data,
        "success": rc == 0,
        "error": err.strip() or None,
    }


def fetch_clipping(item: dict) -> dict:
    file_path = item.get("file", "")
    try:
        content = Path(file_path).read_text(encoding="utf-8")
        return {
            "url": item.get("url", file_path),
            "type": "clipping",
            "file": file_path,
            "content": content,
            "success": True,
            "error": None,
        }
    except Exception as exc:
        return {
            "url": item.get("url", file_path),
            "type": "clipping",
            "file": file_path,
            "content": "",
            "success": False,
            "error": str(exc),
        }


def fetch_post(item: dict) -> dict:
    return {
        "type": "post",
        "content": item.get("text", ""),
        "source_file": item.get("source_file", ""),
        "success": True,
        "error": None,
    }


def fetch_reddit(item: dict) -> dict:
    subreddit = item["subreddit"]
    rc, out, err = _run(
        [sys.executable, "scripts/fetch_reddit.py", subreddit,
         "--use-cursor", "--with-comments", "--limit", "25"],
        timeout=60,
    )
    posts: list = []
    if rc == 0 and out.strip():
        try:
            posts = json.loads(out)
        except json.JSONDecodeError:
            pass
    return {
        "subreddit": subreddit,
        "type": "reddit",
        "posts": posts,
        "success": rc == 0,
        "error": err.strip() or None,
    }


FETCH_FN = {
    "link":     fetch_link,
    "paper":    fetch_paper,
    "youtube":  fetch_youtube,
    "twitter":  fetch_twitter,
    "clipping": fetch_clipping,
    "post":     fetch_post,
    "reddit":   fetch_reddit,
}


# ---------------------------------------------------------------------------
# Cache-aware dispatcher
# ---------------------------------------------------------------------------

def process_item(item: dict, use_cache: bool = True) -> dict:
    item_type = item["type"]
    key = _cache_key(item)

    if use_cache and _is_cached(item_type, key):
        result = _load_cache(item_type, key)
        result["from_cache"] = True
        return result

    fn = FETCH_FN.get(item_type)
    if fn is None:
        return {"type": item_type, "success": False, "error": f"unknown type: {item_type}"}

    t0 = time.monotonic()
    result = fn(item)
    result["fetch_time_s"] = round(time.monotonic() - t0, 2)
    result["cache_key"] = key
    result["from_cache"] = False

    if result.get("success"):
        _save_cache(item_type, key, result)

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(
        description="Fetch all inbox items in parallel; cache results to .state/fetch_cache/"
    )
    parser.add_argument("--manifest", default=".state/inbox_manifest.json",
                        help="Path to manifest produced by inbox_coordinator.py")
    parser.add_argument("--workers", type=int, default=8,
                        help="Max concurrent fetch threads (default: 8)")
    parser.add_argument("--types",
                        default="link,paper,youtube,twitter,clipping,post,reddit",
                        help="Comma-separated list of source types to process")
    parser.add_argument("--no-cache", action="store_true",
                        help="Bypass cache and re-fetch everything")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be fetched without fetching")
    args = parser.parse_args()

    if not Path(args.manifest).exists():
        log(f"Manifest not found: {args.manifest} — run inbox_coordinator.py first", "ERROR")
        return 1

    manifest = read_json(args.manifest)
    types_requested = [t.strip() for t in args.types.split(",")]
    use_cache = not args.no_cache

    # Build flat work queue respecting requested types
    all_items: list = []
    for t in types_requested:
        items = manifest["groups"].get(t, [])
        all_items.extend(items)
        if items:
            log(f"Queued {len(items):3d} x {t}")

    if not all_items:
        log("Nothing to fetch — inbox is empty or all items already processed.")
        return 0

    log(f"Total: {len(all_items)} items | workers: {args.workers} | cache: {use_cache}")

    if args.dry_run:
        plan = [
            {"type": i["type"], "key": _cache_key(i),
             "url": i.get("url", i.get("subreddit", "<post>"))}
            for i in all_items
        ]
        print(json.dumps({"planned": plan}, ensure_ascii=False, indent=2))
        return 0

    # --- Parallel fetch ---
    wall_t0 = time.monotonic()
    results: list = []
    errors: list = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_map = {pool.submit(process_item, item, use_cache): item for item in all_items}
        for future in as_completed(future_map):
            item = future_map[future]
            label = item.get("url", item.get("subreddit", "<post>"))[:70]
            try:
                result = future.result()
                results.append(result)
                cached_tag = " [cached]" if result.get("from_cache") else ""
                status = "OK" if result.get("success") else "FAIL"
                log(f"[{status}]{cached_tag} {item['type']:10s} {label} "
                    f"({result.get('fetch_time_s', 0):.1f}s)")
                if not result.get("success") and result.get("error"):
                    errors.append({"item": item, "error": result["error"]})
            except Exception as exc:
                log(f"[EXCEPTION] {label}: {exc}", "ERROR")
                errors.append({"item": item, "error": str(exc)})

    wall_elapsed = time.monotonic() - wall_t0

    # --- Summary ---
    successful = [r for r in results if r.get("success")]
    from_cache = [r for r in results if r.get("from_cache")]

    summary = {
        "completed_at": datetime.datetime.utcnow().isoformat() + "Z",
        "wall_time_s": round(wall_elapsed, 2),
        "workers": args.workers,
        "total": len(all_items),
        "successful": len(successful),
        "from_cache": len(from_cache),
        "failed": len(errors),
        "types": types_requested,
        "results": results,
        "errors": errors,
    }
    write_json(".state/fetch_results.json", summary)

    log(f"Finished: {len(successful)}/{len(all_items)} OK "
        f"({len(from_cache)} cached) in {wall_elapsed:.1f}s wall time")
    log("Results: .state/fetch_results.json")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
