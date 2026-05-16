---
title: "llmwiki (Open-Source Implementation)"
title_ru: "llmwiki (реализация с открытым кодом)"
category: tools
tags: [karpathy, llm-wiki, knowledge-base, mcp, claude, obsidian, sqlite, open-source]
updated: 2026-05-15
sources:
  - https://github.com/lucasastorian/llmwiki
---

## Summary
An open-source implementation of Karpathy's LLM Wiki pattern: point it at a folder of research files, start the local app, and connect Claude via MCP — Claude then reads sources, writes wiki pages, and maintains cross-references and citations automatically.

## Key Ideas
- **Local-first, MCP-powered:** Runs entirely on your machine (no cloud required); a FastAPI backend + Next.js frontend + stdio MCP server let Claude read and write your wiki via native tools.
- **Filesystem as source of truth:** Wiki pages are ordinary markdown files under `wiki/`; the SQLite index is derived and fully rebuildable — edit pages in any editor, they're picked up by a file watcher.
- **Formats supported:** PDFs (pdf-oxide for text, optional Mistral OCR for tables), Markdown/plain text, Excel/CSV, HTML, images; Word/PowerPoint via optional LibreOffice.
- **Claude's MCP tools:** `guide`, `search` (list or full-text), `read` (PDFs with page ranges, glob batch), `write` (create, str_replace, append), `delete` — all writes go to disk first, then update the search index.
- **Workspace scoping:** One workspace = one MCP server entry; multiple research folders each get their own entry in `claude_desktop_config.json` or `.claude/settings.json`.
- **Hosted option:** `llmwiki.app` runs the multi-tenant version with Postgres/Supabase auth and S3, PGroonga for ranked search, and optional Mistral OCR.

## Details
`llmwiki` is built by Lucas Astorian. Setup is: `git clone`, Python venv + `pip install`, `npm install`, then `./llmwiki init <folder>` to scaffold and index, `./llmwiki serve <folder>` to start the local app. `./llmwiki open <folder>` does all three in one command.

The architecture is: Next.js → FastAPI → SQLite (local), with the MCP server running as a stdio process that Claude connects to. Source files are never moved or modified. The `.llmwiki/` hidden directory holds the index and cache — delete it anytime and run `llmwiki reindex` to rebuild.

Search uses SQLite FTS5 with porter stemming — good for keyword queries, no semantic/embedding search in local mode. The hosted version at `llmwiki.app` uses PGroonga for ranked search. For richer PDF extraction (especially tables and financial documents), setting `MISTRAL_API_KEY` enables Mistral OCR over the default pdf-oxide.

**Key limitation:** PDF table extraction with the default pdf-oxide is rough — tables come through as messy text. For data-heavy PDFs, Mistral OCR is significantly better. Also, one workspace = one MCP server entry by design (intentional scoping of context and file access).

Licensed under Apache 2.0.

## Related Entries
- [[llm-wiki-pattern]]
- [[github-copilot-cli]]

---
<!-- RU -->

## Краткое описание
Реализация паттерна LLM-вики Карпатого с открытым исходным кодом: укажите на папку с исследовательскими файлами, запустите локальное приложение и подключите Claude через MCP — Claude сам будет читать источники, писать страницы вики и поддерживать перекрёстные ссылки и цитаты.

## Ключевые идеи
- **Локальная работа через MCP:** Работает полностью на вашей машине (без облака); FastAPI-бэкенд + Next.js-фронтенд + stdio MCP-сервер позволяют Claude читать и писать вики через нативные инструменты.
- **Файловая система как источник истины:** Страницы вики — обычные markdown-файлы в `wiki/`; SQLite-индекс является производным и полностью восстанавливаемым — редактируйте страницы в любом редакторе, файловый watcher подхватит изменения.
- **Поддерживаемые форматы:** PDF (pdf-oxide для текста, опциональный Mistral OCR для таблиц), Markdown/plain text, Excel/CSV, HTML, изображения; Word/PowerPoint — через опциональный LibreOffice.
- **MCP-инструменты Claude:** `guide`, `search` (список или полнотекстовый поиск), `read` (PDF с указанием страниц, glob-пакетное чтение), `write` (создание, str_replace, дополнение), `delete` — все записи сначала идут на диск, затем обновляется индекс.
- **Изоляция рабочего пространства:** Одно рабочее пространство = одна запись MCP-сервера; несколько исследовательских папок получают собственные записи в `claude_desktop_config.json` или `.claude/settings.json`.
- **Хостируемая версия:** `llmwiki.app` — мультитенантная версия с Postgres/Supabase-аутентификацией, S3, PGroonga для ранжированного поиска и опциональным Mistral OCR.

## Подробнее
`llmwiki` создан Лукасом Астерианом. Установка: `git clone`, Python venv + `pip install`, `npm install`, затем `./llmwiki init <папка>` для инициализации и индексирования, `./llmwiki serve <папка>` для запуска локального приложения. `./llmwiki open <папка>` выполняет всё три команды сразу.

Архитектура: Next.js → FastAPI → SQLite (локально), MCP-сервер работает как stdio-процесс, к которому подключается Claude. Исходные файлы никогда не перемещаются и не изменяются. Скрытая папка `.llmwiki/` содержит индекс и кэш — удалите её в любой момент и запустите `llmwiki reindex` для восстановления.

Поиск использует SQLite FTS5 со стеммингом Porter — хорошо для поиска по ключевым словам, без семантического/эмбеддинг-поиска в локальном режиме. Хостируемая версия использует PGroonga для ранжированного поиска. Для более качественного извлечения из PDF (особенно таблиц и финансовых документов) переменная `MISTRAL_API_KEY` включает Mistral OCR вместо pdf-oxide по умолчанию.

**Ключевое ограничение:** Извлечение таблиц из PDF стандартным pdf-oxide работает грубо — таблицы преобразуются в неструктурированный текст. Для PDF с насыщенными данными Mistral OCR значительно лучше. Также одно рабочее пространство = одна запись MCP-сервера — намеренное проектное решение для изоляции контекста и доступа к файлам.

Лицензия: Apache 2.0.

## Связанные записи
- [[llm-wiki-pattern]]
- [[github-copilot-cli]]
