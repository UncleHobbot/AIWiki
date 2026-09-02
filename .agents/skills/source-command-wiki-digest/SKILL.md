---
name: "source-command-wiki-digest"
description: "Migrated source command `wiki-digest`"
---

# source-command-wiki-digest

Use this skill when the user asks to run the migrated source command `wiki-digest`.

## Command Template

Generate a weekly digest of all wiki entries created or updated in the last 7 days.

Steps:
1. Determine the current ISO week number (YYYY-WNN format)

2. Load the terminology memory from digests/memory.json if it exists.
   This is the list of terms already explained in previous digests.
   Keep it in context for Step 5.

3. Check if digests/YYYY-WNN.md already exists — if so, regenerate it from scratch

4. Scan all .md files in wiki/ and filter to those with an "updated:" date within
   the last 7 days. Group by category.

5. Write digests/YYYY-WNN.md with the following bilingual structure.

   IMPORTANT: check every technical term against memory.json["terms"].
   If the term appears there, do NOT re-explain it — just use it directly.
   Only define a term inline if it is NOT already in memory.json.

---
title: "LLM Wiki Digest — Week NN, YYYY"
period: YYYY-MM-DD to YYYY-MM-DD
entries_created: N
entries_updated: M
---

## 🔥 Top News
[3-5 most significant news entries from wiki/news/]

## 🛠️ New Tools & Releases
[New or updated entries from wiki/tools/ and wiki/models/]

## 💡 Tips & Techniques
[New or updated entries from wiki/tips/]

## 📚 Concepts Learned
[New or updated entries from wiki/concepts/ and wiki/agents/]

## 🔗 Worth Reading
[Top 5 source URLs from this week's processed entries]

---
<!-- RU -->

## 🔥 Главные новости
[Translation of Top News section]

## 🛠️ Новые инструменты и релизы
[Translation of Tools & Releases section]

## 💡 Советы и техники
[Translation of Tips section]

## 📚 Изученные концепции
[Translation of Concepts section]

## 🔗 Стоит прочитать
[Same 5 URLs — no translation needed for URLs themselves]

6. After writing the digest, update digests/memory.json:
   a. For every technical term, acronym, tool name, or model name that was
      DEFINED or EXPLAINED in this digest, add it to memory.json["terms"]
      with a one-line definition.
   b. Merge with existing memory (do not overwrite terms already present).
   c. Update memory.json["last_updated"] to the current ISO week.

   memory.json schema:
   {
     "last_updated": "YYYY-WNN",
     "terms": {
       "RAG": "Retrieval-Augmented Generation: combining LLM generation with retrieval from an external knowledge store",
       "MCP": "Model Context Protocol: open standard for connecting LLMs to external tools and data sources",
       "...": "..."
     }
   }

7. Report: digest saved to digests/YYYY-WNN.md, N terms added to memory.json
8. **Write to log.md** (required — do not skip):
   python scripts/log_run.py "/wiki-digest" "<YYYY-WNN digest generated, N entries covered, M terms added to memory.json.>"
