---
title: "React Doctor: AI-Generated React Code Linter"
title_ru: "React Doctor: линтер для React-кода, написанного ИИ"
category: tools
tags: [react, debugging, linting, agents, next-js, react-native, vite]
updated: 2026-05-15
sources:
  - https://x.com/aidenybai/status/2052780632510775469
---

## Summary
React Doctor v2 is a zero-config CLI tool that catches bad React code written by AI coding agents — works with Next.js, Vite, and React Native and runs as a single `npx` command.

## Key Ideas
- **Built for the agent era:** Specifically designed to catch the class of bugs that AI agents reliably produce when writing React code — patterns that look plausible but break at runtime or cause performance issues.
- **Zero-config install:** `npx react-doctor@latest` — no setup, runs against your existing project.
- **Framework coverage:** Next.js, Vite, and React Native all supported out of the box.
- **Run after agent sessions:** The intended workflow is to run react-doctor after an AI agent writes or refactors React code, before code review or deployment.
- **v2 release:** Released by @aidenybai (Aiden Bai) in May 2026 with 765k+ views on the announcement tweet, indicating high community interest.

## Details
Created by Aiden Bai (@aidenybai), who is known in the React ecosystem. React Doctor is a diagnostic tool rather than a linter in the traditional sense — it's specifically tuned to detect patterns that are common failure modes when AI agents generate React code, not just general style violations.

The tool addresses a real pain point: AI coding agents produce syntactically valid React code that often contains subtle semantic errors — incorrect hook dependencies, anti-patterns, or misused APIs. React Doctor catches these before they reach production.

As AI agents write increasingly more frontend code, tooling designed to verify AI output (rather than human output) becomes a distinct category.

## Related Entries
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide to the Top 36](../tips/claude-code-plugins-guide.md))
- [[llm-wiki-enterprise-patterns]] ([LLM Wiki for Enterprise and Agents](../agents/llm-wiki-enterprise-patterns.md))

---
<!-- RU -->

## Краткое описание
React Doctor v2 — CLI-инструмент без конфигурации для обнаружения плохого React-кода, написанного AI-агентами. Работает с Next.js, Vite и React Native, запускается одной командой `npx`.

## Ключевые идеи
- **Создан для эпохи агентов:** Специально разработан для обнаружения класса ошибок, которые AI-агенты надёжно воспроизводят при написании React-кода — паттерны, выглядящие правдоподобно, но ломающиеся в рантайме или вызывающие проблемы производительности.
- **Установка без конфигурации:** `npx react-doctor@latest` — без настройки, запускается для существующего проекта.
- **Поддержка фреймворков:** Next.js, Vite и React Native поддерживаются из коробки.
- **Запускайте после агентских сессий:** Предполагаемый процесс — запускать react-doctor после того, как AI-агент написал или отрефакторил React-код, до код-ревью или деплоя.
- **Релиз v2:** Выпущен @aidenybai в мае 2026 года с 765k+ просмотрами на твите анонса.

## Подробнее
React Doctor создан Эйденом Бай (@aidenybai), известным в экосистеме React. Это диагностический инструмент, а не традиционный линтер — он настроен на выявление паттернов, характерных для сбоев при генерации React-кода AI-агентами, а не просто нарушений стиля.

Инструмент решает реальную проблему: AI-агенты производят синтаксически корректный React-код, который часто содержит тонкие семантические ошибки — неверные зависимости хуков, антипаттерны или некорректно используемые API.

## Связанные записи
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide to the Top 36](../tips/claude-code-plugins-guide.md))
- [[llm-wiki-enterprise-patterns]] ([LLM Wiki for Enterprise and Agents](../agents/llm-wiki-enterprise-patterns.md))
