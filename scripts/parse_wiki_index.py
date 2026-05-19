#!/usr/bin/env python3
"""Parse all wiki entries and print JSON summary for index generation."""
import io, os, re, json, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

wiki_dir = "wiki"
entries = []

for root, dirs, files in os.walk(wiki_dir):
    dirs.sort()
    for f in sorted(files):
        if not f.endswith(".md"):
            continue
        path = os.path.join(root, f)
        with open(path, encoding="utf-8") as _fh:
            text = _fh.read()

        fm_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not fm_match:
            continue
        fm = fm_match.group(1)

        def get_field(key):
            m = re.search(r"^" + key + r":\s*[\"']?(.*?)[\"']?\s*$", fm, re.MULTILINE)
            return m.group(1).strip().strip("\"'") if m else ""

        title = get_field("title")
        category = get_field("category")
        date = get_field("date")
        updated = get_field("updated")

        sm = re.search(r"## Summary\n(.*?)(?:\n\n|\n##)", text, re.DOTALL)
        if sm:
            first = re.split(r"(?<=[.!?])\s", sm.group(1).strip())[0]
        else:
            first = ""

        slug = f[:-3]
        entries.append({
            "slug": slug,
            "category": category,
            "date": date,
            "updated": updated,
            "title": title,
            "summary": first,
        })

print(json.dumps(entries, indent=2, ensure_ascii=False))
