Regenerate index.md from all entries currently in wiki/.

Steps:
1. Recursively list all .md files in wiki/
2. For each file, read its front matter and extract: title, title_ru, category, tags, updated, date (if present)
3. Extract the first sentence of the "## Summary" section as the one-line description
4. Group entries by category
5. Write index.md with this structure:

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

6. Report: index.md updated, N total entries indexed
