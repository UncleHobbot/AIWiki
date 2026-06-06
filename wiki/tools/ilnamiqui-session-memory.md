---
title: "ilnamiqui"
title_ru: "ilnamiqui"
category: tools
tags: [memory, opencode, claude-code, sqlite, mcp, session-persistence]
aliases: [ilnamiqui, session memory, persistent memory opencode]
confidence: high
date: 2026-06-06
updated: 2026-06-06
sources:
  - https://github.com/beabys/ilnamiqui
---

## Summary

ilnamiqui (from Nahuatl "to remember or recall") is a persistent session memory tool for OpenCode and Claude Code that stores context in a local SQLite database with zero network calls, no telemetry, and no accounts required.

## Key Ideas

- Per-project isolation via `.ilnamiqui/` directory containing a local SQLite database — all data stays on the machine
- Automatic lifecycle hooks: loads past memories on session start, captures the last 20 messages and saves a summary on `/exit`, runs before/after hooks during context compaction
- MCP server provides 9 tools over stdio for Claude Code integration
- TypeScript plugin for OpenCode with automatic lifecycle hooks built in
- CLI with full control: `init`, `save`, `load`, `search`, `prune`, `delete`, `session`, `keys`
- Dual support for both OpenCode and Claude Code with separate installer paths

## Details

ilnamiqui solves the session amnesia problem in coding agents. When you close a Claude Code or OpenCode session, all context is lost — ilnamiqui intercepts session lifecycle events and persists the important bits to a local SQLite database. On the next session start, those memories are automatically loaded back, giving the agent continuity across sessions.

The architecture is deliberately local-first: no network calls, no telemetry servers, no user accounts. Each project gets its own `.ilnamiqui/` directory with an isolated SQLite database. For Claude Code, it runs as an MCP server exposing 9 tools over stdio. For OpenCode, it installs as a TypeScript plugin that hooks into the session lifecycle automatically.

The CLI provides manual control over memory: search past sessions, prune old entries, delete specific memories, and manage per-project keys. The tool is MIT-licensed.

## Related Entries

- [[agentmemory]] ([AgentMemory](../tools/agentmemory.md))
- [[tencent-db-agent-memory]] ([Tencent DB Agent Memory](../tools/tencent-db-agent-memory.md))
- [[shokunin-memory-system]] ([Shokunin Memory System](../tools/shokunin-memory-system.md))
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin Claude Code](../tools/superpowers-plugin-claude-code.md))

---
<!-- RU -->

## Краткое описание

ilnamiqui (из языка науатль — «вспоминать») — инструмент постоянной памяти сессий для OpenCode и Claude Code, сохраняющий контекст в локальной базе SQLite без сетевых запросов, телеметрии и необходимости регистрации.

## Ключевые идеи

- Изоляция по проектам через директорию `.ilnamiqui/` с локальной базой SQLite — все данные остаются на машине
- Автоматические хуки жизненного цикла: загрузка прошлых воспоминаний при старте сессии, захват последних 20 сообщений и сохранение сводки при `/exit`, хуки до/после компрессии контекста
- MCP-сервер предоставляет 9 инструментов через stdio для интеграции с Claude Code
- Плагин на TypeScript для OpenCode со встроенными автоматическими хуками
- CLI с полным управлением: `init`, `save`, `load`, `search`, `prune`, `delete`, `session`, `keys`
- Поддержка как OpenCode, так и Claude Code с отдельными установщиками

## Подробнее

ilnamiqui решает проблему амнезии сессий в кодинговых агентах. При закрытии сессии Claude Code или OpenCode весь контекст теряется — ilnamiqui перехватывает события жизненного цикла и сохраняет важную информацию в локальную базу SQLite. При следующем запуске сессии воспоминания автоматически загружаются, обеспечивая преемственность между сессиями.

Архитектура изначально ориентирована на локальность: никаких сетевых запросов, серверов телеметрии, пользовательских аккаунтов. Каждый проект получает собственную директорию `.ilnamiqui/` с изолированной базой SQLite. Для Claude Code инструмент работает как MCP-сервер, предоставляя 9 инструментов через stdio. Для OpenCode устанавливается как плагин на TypeScript, автоматически интегрирующийся в жизненный цикл сессии.

CLI позволяет вручную управлять памятью: искать по прошлым сессиям, очищать старые записи, удалять конкретные воспоминания и управлять ключами проектов. Инструмент распространяется под лицензией MIT.

## Связанные записи

- [[agentmemory]] ([AgentMemory](../tools/agentmemory.md))
- [[tencent-db-agent-memory]] ([Tencent DB Agent Memory](../tools/tencent-db-agent-memory.md))
- [[shokunin-memory-system]] ([Shokunin Memory System](../tools/shokunin-memory-system.md))
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin Claude Code](../tools/superpowers-plugin-claude-code.md))
