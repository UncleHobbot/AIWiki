#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild index.md from all wiki entries."""
import re
import sys
from pathlib import Path

sys.stdout = __import__('io').TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = __import__('io').TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def read_text(path):
    return Path(path).read_text(encoding='utf-8')

wiki_dir = Path('wiki')
entries = []
for f in sorted(wiki_dir.rglob('*.md')):
    rel = f.relative_to(wiki_dir)
    slug = rel.with_suffix('').as_posix()
    text = read_text(f)
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not m:
        continue
    fm = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip().strip('"').strip("'")
    title = fm.get('title', slug.split('/')[-1])
    cat = fm.get('category', 'concepts')
    date = fm.get('date', '')
    sum_m = re.search(r'## Summary\s*\n(.+?)(?:\n##|\n---)', text, re.DOTALL)
    summary = ''
    if sum_m:
        summary = sum_m.group(1).strip().replace('\n', ' ')[:120]
    entries.append({'slug': slug, 'title': title, 'cat': cat, 'date': date, 'summary': summary})

cats = {}
for e in entries:
    cats.setdefault(e['cat'], []).append(e)

total = len(entries)
lines = [f'# LLM Wiki Index', f'**{total} entries** across {len(cats)} categories.', '']

EMOJIS = {
    'concepts': '[concepts]', 'tools': '[tools]', 'agents': '[agents]',
    'models': '[models]', 'news': '[news]', 'tips': '[tips]',
    'people': '[people]', 'research': '[research]'
}
NAMES = {
    'concepts': 'Concepts', 'tools': 'Tools', 'agents': 'Agents',
    'models': 'Models', 'news': 'News', 'tips': 'Tips',
    'people': 'People', 'research': 'Research'
}
ORDER = ['concepts', 'tools', 'agents', 'models', 'news', 'tips', 'people', 'research']

for cat in ORDER:
    if cat not in cats:
        continue
    items = cats[cat]
    if cat == 'news':
        items.sort(key=lambda x: x['date'], reverse=True)
    else:
        items.sort(key=lambda x: x['slug'])
    name = NAMES.get(cat, cat.capitalize())
    lines.append(f'## {EMOJIS.get(cat, "[?]")} {name} ({len(items)})')
    for e in items:
        desc = e['summary']
        prefix = f' {desc}' if desc else ''
        if cat == 'news' and e['date']:
            prefix = f' -- {e["date"]}' + prefix
        sp = e['slug']
        pp = sp.replace('/', '\\\\')
        lines.append(f'- [[{sp}]] [{e["title"]}](wiki\\{pp}.md){prefix}')
    lines.append('')

Path('index.md').write_text('\n'.join(lines), encoding='utf-8')
print(f'Index rebuilt: {total} entries')
