---
title: "Kindle Highlights Recovery — A Claude Code Skill for Export-Blocked Annotations"
title_ru: "Восстановление Kindle-выписок — скилл Claude Code для заблокированных экспортом аннотаций"
category: tools
tags: [claude-code, skill, kindle, ocr, sqlite, automation]
aliases: [kindle highlights skill, l3a0 claude plugins, kindle export limits]
confidence: medium
updated: 2026-09-01
sources:
  - https://news.ycombinator.com/item?id=49424758
  - https://github.com/l3a0/claude-plugins
---

## Summary
A Claude Code skill (developer l3a0, part of `l3a0/claude-plugins`) that recovers Kindle highlights Amazon blocks from export via undocumented export limits — 815 of 2,432 recovered highlights were previously hidden. The technique combines the local Kindle SQLite database, on-device OCR of Cloud Reader pages, and positional arithmetic; no DRM circumvention involved.

## Key Ideas
- **The problem:** in one book, Amazon's export returned 283 truncated and 180 location-number-only highlights out of 1,211, citing "export limits."
- **Technique 1 — local database:** the Mac Kindle app syncs a SQLite DB with character-precise start/end positions for every highlight, with no export limit applied.
- **Technique 2 — on-device OCR:** Kindle Cloud Reader renders pages as images; captured via canvas and OCR'd locally with Apple Vision (free).
- **Technique 3 — positional arithmetic:** with positions known, recovery is "find the known prefix, cut to the known length" — landing within 0–2 characters of verbatim.
- **Results:** 2,432 highlights across four books → per-book Markdown files, 815 previously blocked.
- **HN discussion themes:** prior art, fragility (depends on model behavior and Amazon's export paths — some newer books aren't in Cloud Reader at all), and an accusation of AI-generated comments violating HN rules.

## Details
A good example of the "agent as personal-glue engineer" genre: the skill exists because a platform added friction to exporting *your own annotations*, and a local model plus local data could route around it without touching DRM. It's also a fragility case study — the author and commenters note it can break if Anthropic changes model behavior or Amazon closes the Cloud Reader path.

## Related Entries
- [[claude-code]] ([Claude Code](claude-code.md))
- [[mattpocock-skills-repo]] ([Matt Pocock Skills Repo](mattpocock-skills-repo.md))
- [[ship-skills-claude-code-pipeline]] ([Ship Skills](ship-skills-claude-code-pipeline.md))

---
<!-- RU -->

## Краткое описание
Скилл для Claude Code (разработчик l3a0, в репо `l3a0/claude-plugins`), восстанавливающий Kindle-выписки, которые Amazon блокирует при экспорте недокументированными лимитами, — 815 из 2432 восстановленных были ранее скрыты. Техника комбинирует локальную SQLite-базу Kindle, локальный OCR страниц Cloud Reader и позиционную арифметику; обхода DRM нет.

## Ключевые идеи
- **Проблема:** в одной книге экспорт Amazon вернул 283 обрезанных и 180 выписок в виде номеров локаций из 1211, ссылаясь на «лимиты экспорта».
- **Техника 1 — локальная база:** Mac-приложение Kindle синхронизирует SQLite с точными позициями начала/конца каждой выписки, без лимитов экспорта.
- **Техника 2 — локальный OCR:** Cloud Reader рендерит страницы картинками; захват через canvas и OCR локально через Apple Vision (бесплатно).
- **Техника 3 — позиционная арифметика:** зная позиции, восстановление — «найти известный префикс, отрезать известную длину» — с точностью 0–2 символа.
- **Результат:** 2432 выписки по четырём книгам → Markdown-файлы, 815 ранее заблокированных.
- **Темы HN:** prior art, хрупкость (зависит от поведения модели и путей экспорта Amazon), обвинение в AI-комментариях на HN.

## Подробнее
Хороший пример жанра «агент как персональный клеевой инженер»: скилл появился, потому что платформа добавила трение в экспорт *ваших же* аннотаций, а локальная модель плюс локальные данные обошли это без касания DRM. Это и кейс о хрупкости: ломается при изменении поведения модели или закрытии Cloud Reader.

## Связанные записи
- [[claude-code]] ([Claude Code](claude-code.md))
- [[mattpocock-skills-repo]] ([Matt Pocock Skills Repo](mattpocock-skills-repo.md))
- [[ship-skills-claude-code-pipeline]] ([Ship Skills](ship-skills-claude-code-pipeline.md))
