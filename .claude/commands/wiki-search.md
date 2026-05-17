Search all wiki entries for the query passed as arguments to this command.

The search query is: $ARGUMENTS

## Three search modes (checked in order)

### 0. Alias / title lookup (highest priority)

**Before anything else**, check `_index.json["by_alias"]` for a case-insensitive
exact match of the full query against known aliases and entry titles.

Examples:
- "RAG" → finds lightrag-graph-rag via alias
- "Karpathy" → finds karpathy-deep-dive-llms via alias
- "grill me" → finds matt-pocock-aihero via alias

If a match is found, immediately return that single entry with its title,
confidence level, and aliases, plus links_to/linked_from from the slug JSON.

### 1. Relational search (tag/category filter)

If the query contains a category name (concepts, tools, agents, models,
news, tips, people) OR a tag-like keyword, use the relation index:

```
# Load the index
.state/relations/_index.json

# Match against by_tag and by_category
```

Relational query patterns to detect:
- "tools using RAG"             → category=tools AND tag=rag
- "concepts about self-play"    → category=concepts AND tag contains "self-play"
- "entries tagged knowledge-graph" → tag=knowledge-graph
- "all tips"                    → category=tips
- "high confidence tools"       → category=tools AND confidence=high (filter slug JSONs)
- "what links to <slug>"        → load .state/relations/<slug>.json → linked_from field

For each matching slug, load .state/relations/<slug>.json to get the title,
then show a one-line result: `[[slug]] (category) [confidence] — title`.

### 2. Full-text search (fallback)

For all other queries — prose phrases, proper nouns, exact strings — search
across all .md files in wiki/:
- Alias match in frontmatter (highest relevance, after step 0)
- Exact title match
- Tag match in front matter
- Match in the English section body (before <!-- RU -->)

## Output format

Return results sorted by relevance (alias match → relational → text), showing:
- `[[slug]]` (category) [confidence: high|medium|low] — one-line title
- Matching aliases, tags, or 1–2 sentence excerpt

Limit to 10 results. If more exist, say how many were omitted.
If no results: suggest closest alias or tag names from `_index.json`.

## Relation index location

- `.state/relations/_index.json` — fast lookup by tag, category, and alias
- `.state/relations/<slug>.json` — per-entry record (links_to, linked_from, tags, aliases, confidence)

If the index is missing or stale, run:
```
python scripts/build_relations.py
```
