---
title: "OpenSddRag: MCP Server with Persistent Rules Harness for Coding Agents"
title_ru: "OpenSddRag: MCP-сервер с постоянным движком правил для coding-агентов"
category: tools
tags: [mcp, claude-code, spec-driven-development, agent-memory, open-source]
aliases: [OpenSddRag, spec-driven RAG harness]
confidence: low
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/ollama/comments/1u4ywpq/opensddrag_v012_added_a_harness_rules_engine_to/
---

## Summary
OpenSddRag is an open-source MCP server giving coding agents like Claude Code persistent semantic memory plus a structured spec-driven workflow (propose → spec → design → tasks → apply → verify → archive); v0.1.2 adds a "Harness" rules engine to enforce project-level constraints across sessions.

## Key Ideas
- Solves agent "amnesia" — without a rules engine, constraints like "never touch the auth layer without a spec" or "always run migrations in a separate task" get lost once the context window resets.
- Rules are defined with a name, severity, and a phase trigger: `always`, `on_apply`, `on_verify`, `on_spec`, `on_archive`.
- Rules tagged `trigger="always"` are automatically injected into every agent session via `get_working_context` — no extra tool call required.
- Phase-specific rules surface as checklists inside workflow commands (e.g. `/opsr:apply`, `/opsr:spec`) before the corresponding gate executes.
- Built around an existing seven-stage spec-driven workflow (propose, spec, design, tasks, apply, verify, archive).

## Details
OpenSddRag positions itself as a memory and governance layer for agentic coding tools. The base product already implements a structured spec-driven development loop and persistent semantic memory via MCP. The v0.1.2 release's main addition, the "Harness" rules engine, addresses a specific pain point: agents forget project-level guardrails between sessions because context resets wipe out anything not explicitly re-stated. By persisting rules outside the context window and auto-injecting the "always" ones, and surfacing phase-specific checklists at the relevant workflow gate, the tool aims to make constraints durable without requiring the user to repeat them every session.

This is a small community open-source project (Reddit-sourced, low confidence) and the release notes are self-reported by the maintainer. It is conceptually adjacent to the broader "spec-driven development" trend (cf. GitHub Spec-Kit) but focused specifically on rule persistence and enforcement rather than the spec-to-code pipeline itself.

## Related Entries
- [[github-spec-kit]] ([GitHub Spec-Kit: Spec-Driven Development Toolkit](../tools/github-spec-kit.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development in the Real World](../tips/spec-driven-development-bmad.md))

---
<!-- RU -->

## Краткое описание
OpenSddRag — это open-source MCP-сервер, дающий coding-агентам (например, Claude Code) постоянную семантическую память и структурированный spec-driven workflow (propose → spec → design → tasks → apply → verify → archive); версия v0.1.2 добавляет движок правил "Harness" для соблюдения ограничений проекта между сессиями.

## Ключевые идеи
- Решает проблему "амнезии" агента — без движка правил ограничения вроде "не трогать слой авторизации без спеки" или "всегда выполнять миграции отдельной задачей" теряются при сбросе контекста.
- Правила определяются по имени, уровню серьёзности и триггеру фазы: `always`, `on_apply`, `on_verify`, `on_spec`, `on_archive`.
- Правила с `trigger="always"` автоматически вставляются в каждую сессию агента через `get_working_context` — без дополнительного вызова инструмента.
- Правила для конкретных фаз появляются как чек-листы внутри команд workflow (например, `/opsr:apply`, `/opsr:spec`) перед выполнением соответствующего гейта.
- Построен вокруг существующего семиэтапного spec-driven workflow (propose, spec, design, tasks, apply, verify, archive).

## Подробнее
OpenSddRag позиционируется как слой памяти и управления для агентных coding-инструментов. Базовый продукт уже реализует структурированный цикл spec-driven разработки и постоянную семантическую память через MCP. Главное добавление в релизе v0.1.2 — движок правил "Harness" — решает конкретную проблему: агенты забывают проектные ограничения между сессиями, потому что сброс контекста стирает всё, что не было явно повторено. Сохраняя правила за пределами контекстного окна и автоматически вставляя правила "always", а также показывая чек-листы для конкретных фаз на соответствующих гейтах workflow, инструмент делает ограничения постоянными без необходимости повторять их каждую сессию.

Это небольшой open-source проект сообщества (источник — Reddit, низкая достоверность), и заметки о релизе предоставлены самим автором. Концептуально он близок к более широкому тренду "spec-driven development" (см. GitHub Spec-Kit), но фокусируется именно на сохранении и применении правил, а не на самом пайплайне spec-to-code.

## Связанные записи
- [[github-spec-kit]] ([GitHub Spec-Kit: Spec-Driven Development Toolkit](../tools/github-spec-kit.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development in the Real World](../tips/spec-driven-development-bmad.md))
