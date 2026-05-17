#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_relations.py
==========================
Build the incremental relation index under .state/relations/.

For every wiki entry produces:
    .state/relations/<slug>.json   — per-entry record
    .state/relations/_index.json   — aggregated tag/category lookup table

Run after any ingestion batch, or pass --slug to update a single entry:
    python scripts/build_relations.py              # rebuild all
    python scripts/build_relations.py --slug lightrag-graph-rag
"""

import io
import sys
import json
import re
import pathlib
import argparse
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

WIKI_DIR   = pathlib.Path(__file__).parent.parent / "wiki"
STATE_DIR  = pathlib.Path(__file__).parent.parent / ".state" / "relations"
INDEX_FILE = STATE_DIR / "_index.json"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def write_json(path, data):
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def parse_frontmatter(text):
    """Return dict of front-matter fields from a wiki .md file."""
    fm = {}
    m = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
    if not m:
        return fm
    block = m.group(1)

    # scalar fields
    for key in ("title", "title_ru", "category", "updated", "date", "confidence"):
        km = re.search(rf'^{key}:\s*"?(.+?)"?\s*$', block, re.MULTILINE)
        if km:
            fm[key] = km.group(1).strip().strip('"')

    # tags list  — inline form: [a, b, c]
    tm = re.search(r'^tags:\s*\[(.+?)\]', block, re.MULTILINE)
    if tm:
        fm["tags"] = [t.strip().strip('"') for t in tm.group(1).split(",") if t.strip()]
    else:
        fm["tags"] = []

    # aliases list — inline form: [a, b, c]
    am = re.search(r'^aliases:\s*\[(.+?)\]', block, re.MULTILINE)
    if am:
        fm["aliases"] = [a.strip().strip('"') for a in am.group(1).split(",") if a.strip()]
    else:
        fm["aliases"] = []

    return fm


def extract_wikilinks(text):
    """Return deduplicated list of [[slug]] targets from the EN section only."""
    # Only scan before the RU divider
    en_section = text.split("---\n<!-- RU -->")[0]
    return list(dict.fromkeys(re.findall(r"\[\[([^\]|#]+)\]\]", en_section)))


# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------

def build_entry(md_file: pathlib.Path, backlinks_map: dict) -> dict:
    slug = md_file.stem
    text = read_text(md_file)
    fm   = parse_frontmatter(text)

    return {
        "slug":        slug,
        "title":       fm.get("title", slug),
        "title_ru":    fm.get("title_ru", ""),
        "category":    fm.get("category", "uncategorized"),
        "tags":        fm.get("tags", []),
        "aliases":     fm.get("aliases", []),
        "confidence":  fm.get("confidence", ""),   # high | medium | low | ""
        "updated":     fm.get("updated", fm.get("date", "")),
        "links_to":    extract_wikilinks(text),
        "linked_from": sorted(backlinks_map.get(slug, [])),
    }


def build_backlinks_map(all_files: list) -> dict:
    """
    For each slug, collect which other slugs link to it via [[slug]].
    Cheaper to do once across all files than per-entry.
    """
    bmap = {}
    for f in all_files:
        src  = f.stem
        text = read_text(f)
        for target in extract_wikilinks(text):
            bmap.setdefault(target, set()).add(src)
    return {k: sorted(v) for k, v in bmap.items()}


def build_index(records: list) -> dict:
    """Aggregate records into fast-lookup dicts by tag, category, and alias."""
    by_tag      = {}
    by_category = {}
    by_alias    = {}   # alias (lowercased) → slug

    for r in records:
        cat = r["category"]
        by_category.setdefault(cat, []).append(r["slug"])
        for tag in r["tags"]:
            by_tag.setdefault(tag, []).append(r["slug"])
        for alias in r.get("aliases", []):
            by_alias[alias.lower()] = r["slug"]
        # Also index the title and title_ru as aliases
        if r.get("title"):
            by_alias[r["title"].lower()] = r["slug"]

    return {
        "updated":     datetime.date.today().isoformat(),
        "total":       len(records),
        "by_tag":      {k: sorted(v) for k, v in sorted(by_tag.items())},
        "by_category": {k: sorted(v) for k, v in sorted(by_category.items())},
        "by_alias":    dict(sorted(by_alias.items())),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Build wiki relation index.")
    parser.add_argument("--slug", help="Update a single entry instead of all")
    args = parser.parse_args()

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    all_files = sorted(WIKI_DIR.rglob("*.md"))

    if args.slug:
        # Single-entry update: rebuild only this slug, patch index
        target = next((f for f in all_files if f.stem == args.slug), None)
        if not target:
            print(f"Slug not found: {args.slug}", file=sys.stderr)
            return 1

        bmap = build_backlinks_map(all_files)
        rec  = build_entry(target, bmap)
        write_json(STATE_DIR / f"{args.slug}.json", rec)
        print(f"Updated: .state/relations/{args.slug}.json")

        # Patch the index
        idx = read_json(INDEX_FILE) if INDEX_FILE.exists() else {"by_tag": {}, "by_category": {}, "by_alias": {}}
        idx.setdefault("by_alias", {})
        # Remove old slug entries from tags and category
        for tag_list in idx["by_tag"].values():
            if args.slug in tag_list:
                tag_list.remove(args.slug)
        for cat_list in idx["by_category"].values():
            if args.slug in cat_list:
                cat_list.remove(args.slug)
        # Remove old alias entries for this slug
        idx["by_alias"] = {k: v for k, v in idx["by_alias"].items() if v != args.slug}
        # Re-add
        for tag in rec["tags"]:
            idx["by_tag"].setdefault(tag, [])
            if args.slug not in idx["by_tag"][tag]:
                idx["by_tag"][tag].append(args.slug)
                idx["by_tag"][tag].sort()
        idx["by_category"].setdefault(rec["category"], [])
        if args.slug not in idx["by_category"][rec["category"]]:
            idx["by_category"][rec["category"]].append(args.slug)
            idx["by_category"][rec["category"]].sort()
        for alias in rec.get("aliases", []):
            idx["by_alias"][alias.lower()] = args.slug
        if rec.get("title"):
            idx["by_alias"][rec["title"].lower()] = args.slug
        idx["updated"] = datetime.date.today().isoformat()
        write_json(INDEX_FILE, idx)
        print(f"Patched:  .state/relations/_index.json")
        return 0

    # Full rebuild
    print(f"Building relation index for {len(all_files)} entries...")
    bmap    = build_backlinks_map(all_files)
    records = []
    for f in all_files:
        rec = build_entry(f, bmap)
        write_json(STATE_DIR / f"{rec['slug']}.json", rec)
        records.append(rec)

    idx = build_index(records)
    write_json(INDEX_FILE, idx)

    print(f"Done. {len(records)} entries indexed.")
    print(f"  Tags:       {len(idx['by_tag'])} unique")
    print(f"  Categories: {list(idx['by_category'].keys())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
