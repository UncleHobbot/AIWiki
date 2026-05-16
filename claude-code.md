---
title: "Claude Code — Coding Agent by Anthropic"
title_ru: "Claude Code — Агент для кодинга от Anthropic"
category: tools
tags: [claude-code, coding-agent, cli, anthropic, agentic-coding]
updated: 2025-05-15
sources:
  - https://docs.anthropic.com/en/docs/claude-code/overview
  - https://www.anthropic.com/news/claude-code
---

## Summary
Claude Code is a command-line coding agent by Anthropic that runs in your terminal, reads your codebase, and autonomously completes multi-step programming tasks.

## Key Ideas
- Operates directly in the terminal; no separate IDE or browser required
- Reads and edits files, runs tests, searches the codebase, and executes shell commands
- Uses a `CLAUDE.md` file in the project root as a persistent instruction set for the agent
- Supports Model Context Protocol (MCP) for connecting to external tools and services
- Billed per token through the Anthropic API; no fixed subscription required for API users
- Available as a global npm package: `npm install -g @anthropic-ai/claude-code`

## Details
Claude Code is Anthropic's answer to autonomous coding workflows. Unlike chat-based coding assistants, it is designed to work inside a real terminal session with full access to the local filesystem. The agent can navigate a codebase, understand context across many files, write new code, fix bugs, run tests, and interpret their output — looping until the task is complete.

The `CLAUDE.md` file is the key configuration mechanism: developers place it at the project root (or globally in `~/.claude/CLAUDE.md`) to define coding standards, available commands, project architecture, and any custom instructions the agent should always follow.

MCP integration allows Claude Code to connect to external systems — databases, APIs, custom tools — making it extensible beyond pure file editing.

## Related Entries
- [[mcp-model-context-protocol]]
- [[agentic-coding-workflow]]
- [[claude-md-configuration]]

---
<!-- RU -->

## Краткое описание
Claude Code — агент для разработки от Anthropic, работающий в терминале. Он читает кодовую базу и автономно выполняет многошаговые задачи программирования.

## Ключевые идеи
- Работает напрямую в терминале — без отдельной IDE или браузера
- Читает и редактирует файлы, запускает тесты, ищет по кодовой базе, выполняет shell-команды
- Использует файл `CLAUDE.md` в корне проекта как постоянный набор инструкций для агента
- Поддерживает Model Context Protocol (MCP) для подключения к внешним инструментам и сервисам
- Оплата по токенам через Anthropic API; фиксированная подписка для пользователей API не требуется
- Устанавливается как глобальный npm-пакет: `npm install -g @anthropic-ai/claude-code`

## Подробнее
Claude Code — ответ Anthropic на запрос об автономных рабочих процессах разработки. В отличие от чат-ассистентов для кодинга, он работает внутри реальной сессии терминала с полным доступом к локальной файловой системе. Агент умеет ориентироваться в кодовой базе, понимать контекст множества файлов, писать новый код, исправлять баги, запускать тесты и анализировать их результаты — повторяя цикл до завершения задачи.

Файл `CLAUDE.md` — ключевой механизм конфигурации: разработчики помещают его в корень проекта (или глобально в `~/.claude/CLAUDE.md`), чтобы задать стандарты кода, доступные команды, архитектуру проекта и любые кастомные инструкции, которым агент должен всегда следовать.

Интеграция с MCP позволяет Claude Code подключаться к внешним системам — базам данных, API, кастомным инструментам, — делая его расширяемым далеко за пределы простого редактирования файлов.

## Связанные записи
- [[mcp-model-context-protocol]]
- [[agentic-coding-workflow]]
- [[claude-md-configuration]]
