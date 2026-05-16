Search all wiki entries for the query passed as arguments to this command.

The search query is: $ARGUMENTS

## Two search modes

### 1. Relational search (tag/category filter)

If the query contains a known category name (concepts, tools, agents, models,
news, tips, people) OR a tag-like keyword, use the relation index first:

```
# Load the index
.state/relations/_index.json

# Match against by_tag and by_category
```

Relational query patterns to detect:
- "tools using RAG"   → category=tools AND tag=rag
- "concepts about self-play" → category=concepts AND tag contains "self-play"
- "entries tagged knowledge-graph" → tag=knowledge-graph
- "all tips"          → category=tips
- "what links to <slug>" → load .state/relations/<slug>.json → linked_from field

For each matching slug, load .state/relations/<slug>.json to get the title,
then show a one-line result: `[[slug]] (category) — title`.

### 2. Full-text search (fallback)

For all other queries — prose phrases, proper nouns, exact strings — search
across all .md files in wiki/ for $ARGUMENTS:
- Exact title match (highest relevance)
- Tag match in front matter
- Match in the English section body (before <!-- RU -->)

## Output format

Return results sorted by relevance (relational matches first, then text
matches), showing for each:
- `[[slug]]` (category) — one-line title
- Matching tags or the 1–2 sentence excerpt containing the match

Limit to 10 results. If more exist, say how many were omitted.
If no results: suggest the closest tag names from _index.json by_tag keys.

## Relation index location

- `.state/relations/_index.json` — fast lookup by tag and category
- `.state/relations/<slug>.json` — per-entry record with links_to, linked_from, tags

If the index is missing or stale, run:
```
python scripts/build_relations.py
```
