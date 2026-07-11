---
title: "PackMind — Local Second Brain for Claude Code"
title_ru: "PackMind — локальный second brain для Claude Code"
category: tools
tags: [claude-code, memory, second-brain, embeddings, mcp, hooks, local-first]
aliases: [PackMind, packmind claude code]
confidence: medium
updated: 2026-07-11
sources:
  - https://github.com/mchl-schrdng/packmind
  - https://www.reddit.com/r/ClaudeCode/comments/1utg7yx/i_built_packmind_a_local_second_brain_for_claude/
---

## Summary
**PackMind** is a free, open-source (Apache-2.0) local second brain for Claude Code. It adds persistent project memory, local semantic recall, a project map, session-aware activity tracking, and guardrails via Claude Code hooks and MCP. Memory and embeddings stay local by default.

## Key Ideas
- **Persistent project memory:** solves the problem of useful context, decisions, and previous fixes disappearing between Claude Code sessions.
- **Local semantic recall:** embeddings stored locally by default — no cloud dependency for memory.
- **Project map + session-aware activity tracking:** gives the agent a structural view of the repo and its own prior actions.
- **Guardrails via Claude Code hooks and MCP:** integrates through the native extension surfaces, not a separate app.
- Free and open source (Apache-2.0); normal Claude Code usage costs still apply.

## Details
PackMind targets the inter-session amnesia problem common to coding agents: each session starts fresh and re-derives what prior sessions learned. By keeping a local embedding store and a project map, it lets the agent recall relevant past decisions without bloating the context window with everything. The hooks + MCP integration means it plugs into the agent loop rather than requiring a separate workflow.

## Related Entries
- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))
- [[shokunin-memory-system]] ([Shokunin Memory System](shokunin-memory-system.md))
- [[claude-code]] ([Claude Code](claude-code.md))

---
<!-- RU -->

## Краткое описание
**PackMind** — бесплатный, открытый (Apache-2.0) локальный second brain для Claude Code. Добавляет устойчивую память проекта, локальный семантический recall, карту проекта, session-aware отслеживание активности и ограждения через хуки и MCP Claude Code. Память и эмбеддинги по умолчанию хранятся локально.

## Ключевые идеи
- **Устойчивая память проекта:** решает проблему исчезновения полезного контекста, решений и прошлых фиксов между сессиями Claude Code.
- **Локальный семантический recall:** эмбеддинги хранятся локально — без облачной зависимости.
- **Карта проекта + session-aware трекинг:** агент получает структурный вид репозитория и собственных прошлых действий.
- **Ограждения через хуки и MCP:** интеграция через нативные поверхности расширения.
- Бесплатно и открыто (Apache-2.0); обычные расходы Claude Code сохраняются.

## Подробнее
PackMind решает проблему межсессионной амнезии кодинг-агентов: каждая сессия стартует с нуля и заново выводит то, что нашли предыдущие. Локальный store эмбеддингов и карта проекта позволяют агенту вспоминать релевантные прошлые решения, не раздувая контекстное окно.

## Связанные записи
- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))
- [[shokunin-memory-system]] ([Shokunin Memory System](shokunin-memory-system.md))
- [[claude-code]] ([Claude Code](claude-code.md))
