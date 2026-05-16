Generate a weekly digest of all wiki entries created or updated in the last 7 days.

Steps:
1. Determine the current ISO week number (YYYY-WNN format)
2. Check if digests/YYYY-WNN.md already exists — if so, regenerate it from scratch
3. Scan all .md files in wiki/ and filter to those with an "updated:" date within the last 7 days
4. Group the qualifying entries by category
5. Write digests/YYYY-WNN.md with the following bilingual structure:

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

6. Report: digest saved to digests/YYYY-WNN.md
