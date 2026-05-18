---
title: "Building an LLM Wiki in Obsidian: Step-by-Step Guide"
title_ru: "Создание LLM-вики в Obsidian: пошаговое руководство"
category: tips
tags: [llm-wiki, obsidian, knowledge-base, build-guide, local-llm, agentic-firewall, karpathy, second-brain, mcp]
aliases: [LLM Wiki Obsidian setup, Obsidian LLM Wiki, Wanderloots LLM Wiki, building personal wiki AI]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.youtube.com/watch?v=QbjAQFJJyt0
---

## Summary
A practical walkthrough for building a personal LLM Wiki in Obsidian — including folder structure, the AGENTS.md schema, ingest/query/lint workflows, optional agentic firewalls between vaults, and local model integration for fully private operation.

## Key Ideas
- **Obsidian is the viewer; the LLM agent is the programmer; the wiki is the codebase** — this framing anchors the entire setup.
- **The AGENTS.md / CLAUDE.md schema is the most important file** — it defines all conventions and tells the agent exactly what to do on ingest, query, and lint operations.
- **Folder structure matters:** `raw/` inbox for unprocessed clippings → `wiki/` for processed entries → `sources/` for cached originals.
- **Agentic firewalls** can separate a "private" vault (personal notes, diary) from a "knowledge" vault (curated wiki) — the agent reads both but cannot write to the private vault.
- **Local model support:** Ollama models (Llama 3.3, Qwen3, etc.) can run the entire wiki pipeline without any cloud API calls — fully private.
- **The Obsidian Web Clipper browser extension** is the primary ingestion tool — one click saves any article or YouTube transcript as a markdown file into the `raw/` folder.

## Details
The Wanderloots guide (published May 2026) is one of the most complete build walkthroughs for the LLM Wiki pattern. The setup has four main phases:

**Phase 1 — Vault structure.** Create an Obsidian vault with: `raw/` (inbox for clippings), `wiki/concepts/`, `wiki/topics/`, `wiki/entities/`, `sources/`, and `index.md` at root. The index is a table of contents generated and maintained by the agent.

**Phase 2 — The schema file.** Paste Karpathy's `llm-wiki.md` gist (or a custom version) as `AGENTS.md` or `CLAUDE.md` in the vault root. This file defines: how new sources are processed (ingest), how queries are answered (query), and how the wiki is health-checked (lint). The better the schema, the better the wiki — invest time here.

**Phase 3 — Connect an IDE/agent.** Point Claude Code, Codex, or any agent with file access at the Obsidian vault folder. Tell it: "process all files in raw/". The agent reads AGENTS.md, processes each file, creates/updates wiki pages, and moves processed files to `sources/`.

**Phase 4 — Advanced options:**
- *Agentic firewalls:* Use separate Obsidian vaults — one "personal" (diary, private notes, read-only for the agent) and one "knowledge" (the public-ish wiki, writable). The agent ingests from the personal vault for context but only writes to the knowledge vault.
- *Local model:* Configure Ollama in the IDE settings. Qwen3 32B or Llama 3.3 70B are recommended for their large context windows needed for wiki-scale synthesis.
- *Scheduled automation:* Set up a cron job or IDE scheduled task to process `raw/` at midnight nightly — the wiki grows while you sleep.

**Practical insight from the stream:** Concepts extracted from a single source can update 10–15 different wiki pages. This cross-linking is where compounding value actually emerges, and it's what makes the pattern fundamentally different from a flat note-taking system.

## Video Notes
- [1:30] Overview of the system: shared memory layer for AI and self
- [4:00] Folder structure walkthrough: raw/ → wiki/ → sources/
- [8:00] AGENTS.md as the schema/rulebook — the most important file in the vault
- [12:00] Obsidian Web Clipper extension demo: one-click article and YouTube transcript ingestion
- [18:00] Running Claude Code against the vault: "process all files in raw/"
- [24:00] Live demo: watching concepts get extracted and cross-linked in real time
- [30:00] Agentic firewalls: separating private diary vault from knowledge wiki vault
- [38:00] Connecting a local Ollama model for fully private operation

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem](../tools/llm-wiki-ecosystem.md))
- [[llm-wiki-obsidian-codex-workflow]] ([LLM Wiki: Obsidian + Codex Second Brain](../tips/llm-wiki-obsidian-codex-workflow.md))
- [[local-rag-obsidian-zotero]] ([Local RAG with Obsidian and Zotero](../tools/local-rag-obsidian-zotero.md))

---
<!-- RU -->

## Краткое описание
Практическое руководство по созданию персональной LLM-вики в Obsidian — структура папок, файл-схема AGENTS.md, рабочие процессы ingest/query/lint, агентские файрволы между хранилищами и интеграция локальных моделей для полностью приватной работы.

## Ключевые идеи
- **Obsidian — просмотрщик; LLM-агент — программист; вики — кодовая база** — эта формулировка задаёт весь подход.
- **AGENTS.md / CLAUDE.md — самый важный файл** — он определяет все соглашения и точно указывает агенту, что делать при ingest, query и lint.
- **Структура папок важна:** `raw/` (входящие) → `wiki/` (обработанные записи) → `sources/` (кэшированные оригиналы).
- **Агентские файрволы** могут разделять «приватное» хранилище (личные заметки, дневник) и «знаниевое» (курируемая вики) — агент читает оба, но пишет только в знаниевое.
- **Поддержка локальных моделей:** Ollama (Llama 3.3, Qwen3 и др.) позволяет запускать весь конвейер без облачных API — полностью приватно.
- **Расширение Obsidian Web Clipper** — основной инструмент для захвата контента: одним кликом сохраняет статьи и транскрипты YouTube в папку `raw/`.

## Подробнее
Руководство Wanderloots (опубликовано в мае 2026) — одно из наиболее полных практических описаний паттерна LLM Wiki. Настройка состоит из четырёх этапов.

**Этап 1 — Структура хранилища.** Создать Obsidian vault с папками: `raw/` (входящие), `wiki/concepts/`, `wiki/topics/`, `wiki/entities/`, `sources/` и `index.md` в корне.

**Этап 2 — Файл схемы.** Вставить gist Karpathy (`llm-wiki.md`) или кастомную версию как `AGENTS.md` / `CLAUDE.md` в корень хранилища. Файл определяет правила ingest, query и lint. Чем лучше схема, тем лучше вики.

**Этап 3 — Подключение агента.** Указать Claude Code, Codex или любой другой агент с доступом к файлам на папку Obsidian vault. Дать команду: «обработай все файлы в raw/». Агент читает AGENTS.md, обрабатывает каждый файл, создаёт/обновляет страницы вики.

**Этап 4 — Дополнительные возможности:** агентские файрволы (раздельные хранилища), локальные модели через Ollama, ночная автоматизация через cron.

**Практическое наблюдение:** концепты из одного источника могут обновить 10–15 разных страниц вики. Именно в этом перекрёстном связывании и заключается накопительная ценность паттерна.

## Заметки по видео
- [1:30] Обзор системы: общий слой памяти для AI и для себя
- [4:00] Структура папок: raw/ → wiki/ → sources/
- [8:00] AGENTS.md как схема-правило — главный файл хранилища
- [12:00] Расширение Obsidian Web Clipper: захват статей и транскриптов YouTube одним кликом
- [18:00] Запуск Claude Code против хранилища: «обработай все файлы в raw/»
- [30:00] Агентские файрволы: разделение приватного дневника и знаниевой вики
- [38:00] Подключение локальной модели Ollama для полностью приватной работы

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem](../tools/llm-wiki-ecosystem.md))
- [[llm-wiki-obsidian-codex-workflow]] ([LLM Wiki: Obsidian + Codex Second Brain](../tips/llm-wiki-obsidian-codex-workflow.md))
- [[local-rag-obsidian-zotero]] ([Local RAG with Obsidian and Zotero](../tools/local-rag-obsidian-zotero.md))
