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

7. Report: index.md updated, N total entries indexed, K orphans flagged
