#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild topics/*.md per-topic indexes from topics.md keyword definitions."""
import re
import sys
from datetime import date
from pathlib import Path

sys.stdout = __import__('io').TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = __import__('io').TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


def read_text(path):
    return Path(path).read_text(encoding='utf-8')


wiki_dir = Path('wiki')
entries = []
for f in sorted(wiki_dir.rglob('*.md')):
    cat_dir = f.relative_to(wiki_dir).parts[0]
    slug = f.stem
    text = read_text(f)
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not m:
        continue
    fm = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip().strip('"').strip("'")
    tags_m = re.search(r'tags:\s*\[(.*?)\]', m.group(1))
    tags = [t.strip().strip('"').strip("'") for t in tags_m.group(1).split(',')] if tags_m else []
    title = fm.get('title', slug)
    cat = fm.get('category', cat_dir)
    sum_m = re.search(r'## Summary\s*\n(.+?)(?:\n##|\n---)', text, re.DOTALL)
    summary = ''
    if sum_m:
        para = ' '.join(sum_m.group(1).strip().split())
        first = re.match(r'(.*?[.!?])(\s|$)', para)
        summary = first.group(1) if first else para
    entries.append({'slug': slug, 'title': title, 'cat': cat, 'tags': tags,
                     'path': f'wiki/{cat_dir}/{f.name}', 'summary': summary})

topics_text = read_text('topics.md')
blocks = re.findall(
    r'### \d+\.\s*(.+?)\n.*?\*\*Keywords:\*\*\s*(.*?)\n(?:\s*Subreddits)?.*?\*\*Wiki categories:\*\*\s*(.*?)\n',
    topics_text, re.S
)

topic_map = {
    'AI Agents & Agentic Workflows': 'ai-agents-index.md',
    'Agentic Coding Tools': 'agentic-coding-index.md',
    'LLM Knowledge Bases & Wiki Pattern': 'llm-wiki-index.md',
    'LLM Models & Benchmarks': 'llm-models-index.md',
}

topics_dir = Path('topics')
topics_dir.mkdir(exist_ok=True)

for name, keywords_raw, cats_raw in blocks:
    name = name.strip()
    out_file = topic_map.get(name)
    if not out_file:
        continue
    keywords = [k.strip().lower() for k in re.split(r'[,\n]', keywords_raw) if k.strip()]
    cats = [c.strip().lower() for c in cats_raw.split(',')]

    matched = []
    for e in entries:
        if e['cat'] not in cats:
            continue
        haystack = ' '.join([e['title'].lower(), e['slug'].lower(), e['summary'].lower()] + [t.lower() for t in e['tags']])
        if any(kw in haystack for kw in keywords):
            matched.append(e)

    matched.sort(key=lambda e: e['slug'])
    out_lines = [f'# {name} — Index', f'_Entries: {len(matched)} | Updated: {date.today().isoformat()}_', '']
    for e in matched:
        out_lines.append(f'- [[{e["slug"]}]] [{e["title"]}](../{e["path"]}) — {e["summary"]}')

    (topics_dir / out_file).write_text('\n'.join(out_lines).rstrip() + '\n', encoding='utf-8')
    print(f'{out_file}: {len(matched)} entries')
