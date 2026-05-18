Regenerate index.md from all entries currently in wiki/.

Steps:
1. Run: python scripts/obs.py orphans
   Collect the list of entries with no incoming backlinks — these get an (orphan) marker in the index.
2. Recursively list all .md files in wiki/
3. For each file, read its front matter and extract: title, title_ru, category, tags, updated, date (if present)
4. Extract the first sentence of the "## Summary" section as the one-line description
5. Group entries by category
6. Write index.md with this structure:

# LLM Wiki Index
_Last updated: YYYY-MM-DD | Total entries: N_

## 🧠 Concepts (N)
- [[slug]] — One-line English summary
...

## 🛠️ Tools (N)
...

## 🤖 Agents (N)
...

## 🔬 Models (N)
...

## 📰 News (N, sorted by date descending)
- YYYY-MM-DD [[slug]] — One-line summary
...

## 💡 Tips (N)
...

## 👤 People (N)
...

## 📅 Digests
- [[YYYY-WNN]] — Week NN, YYYY (N entries)
...

7. Generate per-topic indexes in topics/ directory.
   Read topics.md to get the 4 priority topics and their keywords + wiki categories.
   For each topic, create topics/<topic-slug>-index.md listing entries whose tags
   or category match that topic's keywords:

   topics/ai-agents-index.md
   topics/agentic-coding-index.md
   topics/llm-wiki-index.md
   topics/llm-models-index.md

   Format for each topic index:
   # <Topic Name> — Index
   _Entries: N | Updated: YYYY-MM-DD_

   - [[slug]] [Title](../wiki/category/slug.md) — one-line summary

8. Add a "## 🔬 Research (N)" section to index.md for wiki/research/ entries.

9. Report: index.md updated, N total entries indexed, K orphans flagged, 4 topic indexes rebuilt
10. **Write to log.md** (required — do not skip):
    python scripts/log_run.py "/wiki-index" "<index.md rebuilt, N entries, K orphans flagged, topic indexes updated.>"
