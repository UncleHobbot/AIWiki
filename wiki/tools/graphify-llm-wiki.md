---
title: "Graphify: Knowledge Graph Builder for Codebases"
title_ru: "Graphify: построитель графов знаний для кодовых баз"
category: tools
tags: [knowledge-graph, codebase, llm-wiki, coding-agent, claude-code, cursor, open-source]
updated: 2026-05-15
sources:
  - https://www.youtube.com/watch?v=orTRCgjlLKo
---

## Summary
Graphify is an AI coding assistant skill (21k+ GitHub stars) that applies Karpathy's LLM Wiki pattern to codebases — it reads your source files, builds a structured knowledge graph, and surfaces relationships and structures you didn't know were there.

## Key Ideas
- **LLM Wiki applied to code:** Rather than building a wiki from articles and PDFs, Graphify ingests a codebase and builds a structured, interlinked knowledge graph of the code's architecture, patterns, and components.
- **21k+ GitHub stars** (as of April 2026) — among the fastest-growing LLM Wiki implementations.
- **Coding agent skill:** Works as a skill/plugin within Claude Code, OpenAI Codex, Cursor, OpenCode, and similar coding agents — not a standalone tool.
- **"Understands codebase faster":** Reduces the ramp-up time for agents working in a new or large codebase by pre-building a navigable knowledge structure.
- **Reveals hidden structure:** Surfaces relationships and patterns in the code that are not obvious from reading files sequentially.
- **Created by Safi Shamsi** on GitHub.

## Details
Graphify is cited as one of the first implementations of Karpathy's LLM Wiki pattern for a specific domain (code) rather than general knowledge. By April 2026 it had 21k GitHub stars, suggesting strong community uptake.

The key insight is that codebases benefit from the same compilation approach as general knowledge bases: instead of an agent reading individual files on demand during each task, Graphify pre-processes the codebase into a structured knowledge graph. The agent then navigates this graph rather than raw files — faster, with better cross-reference awareness, and with pre-built context about how components relate.

This makes Graphify particularly useful for:
- Large or unfamiliar codebases where agent exploration is slow
- Multi-file refactoring where understanding cross-file relationships is critical
- Onboarding agents to existing projects with complex architecture

## Video Notes
- "Andrej Karpathy's LLM Wiki Codes : Graphify" by Data Science in your pocket (Apr 11, 2026)
- Demonstrates Graphify as the first real code implementation of the LLM Wiki pattern
- Shows the GitHub repo (Safi Shamsi), 21k stars

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide to the Top 36](../tips/claude-code-plugins-guide.md))
- [[gitnexus-codebase-knowledge-graph]] ([GitNexus: Codebase Knowledge Graph for Coding Agents](../tools/gitnexus-codebase-knowledge-graph.md))

---
<!-- RU -->

## Краткое описание
Graphify — навык для AI-помощника по кодированию (21k+ звёзд на GitHub), применяющий паттерн LLM-вики к кодовым базам: читает исходные файлы, строит структурированный граф знаний и выявляет связи и структуры, которые не очевидны при последовательном чтении.

## Ключевые идеи
- **LLM-вики применённый к коду:** Вместо вики из статей и PDF, Graphify загружает кодовую базу и строит структурированный граф архитектуры, паттернов и компонентов.
- **21k+ звёзд на GitHub** (по состоянию на апрель 2026) — среди самых быстрорастущих реализаций LLM-вики.
- **Навык для coding-агента:** Работает как навык/плагин внутри Claude Code, OpenAI Codex, Cursor, OpenCode и аналогичных агентов.
- **«Понимает кодовую базу быстрее»:** Сокращает время разгона агентов в новой или большой кодовой базе, предварительно строя навигируемую структуру знаний.
- **Раскрывает скрытую структуру:** Выявляет связи и паттерны в коде, не очевидные при последовательном чтении файлов.
- **Создан Safi Shamsi** на GitHub.

## Подробнее
Graphify рассматривается как одна из первых реализаций паттерна LLM-вики Карпатого для конкретного домена (код), а не для общих знаний. К апрелю 2026 года — 21k звёзд на GitHub.

Ключевая идея: кодовые базы выигрывают от того же подхода компиляции, что и общие базы знаний. Вместо чтения отдельных файлов при каждой задаче, Graphify предварительно обрабатывает кодовую базу в граф знаний. Агент навигирует по этому графу, а не по сырым файлам — быстрее, с лучшей осведомлённостью о перекрёстных ссылках.

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide to the Top 36](../tips/claude-code-plugins-guide.md))
- [[gitnexus-codebase-knowledge-graph]] ([GitNexus: Codebase Knowledge Graph for Coding Agents](../tools/gitnexus-codebase-knowledge-graph.md))
