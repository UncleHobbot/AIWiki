---
title: "AtomicMemory"
title_ru: "AtomicMemory"
category: tools
tags: [memory, agent-memory, semantic-memory, mcp, sdk, langchain, vercel-ai]
aliases: [AtomicMemory, atomicmemory, atomic memory]
confidence: high
updated: 2026-06-06
sources:
  - https://github.com/atomicstrata/atomicmemory
---

## Summary

AtomicMemory is an open-source, inspectable semantic memory system for AI agents and applications. Built by AtomicStrata, it captures conversational context, grounds future generations in prior interactions, and carries knowledge across sessions — all while remaining SDK-agnostic and auditable.

## Key Ideas

- **SDK-agnostic architecture**: built on a single core SDK; framework adapters (Vercel AI SDK, OpenAI Agents SDK, LangChain, LangGraph, Mastra) are thin convenience layers, not gatekeepers
- **Correction-aware memory**: supports supersession, clarification, deletion, lineage tracking, and trust-sensitive revision — memories can evolve rather than accumulate stale facts
- **Leading benchmark performance**: top results on BEAM-100K (0.7375), BEAM-1M (0.6625), BEAM-10M (0.4875), and LoCoMo10 (0.8396) — competitive on both accuracy and cost
- **Local-first and self-hostable**: Docker-deployable with Postgres/pgvector; no vendor lock-in, fully auditable memory store
- **Broad integration surface**: published packages for core, SDK, CLI, and MCP server; host plugins for Claude Code, OpenClaw, and Hermes (Codex and Cursor coming soon)
- **Solves the "black box problem"**: positions itself as the antithesis of opaque agent memory — open source, self-hostable, every memory operation is inspectable

## Details

AtomicMemory addresses a fundamental gap in agentic AI: agents forget everything between sessions, and when they do remember, the memory is opaque and uncorrectable. The system stores memories as structured, versioned objects with full lineage — you can trace why a memory exists, what it superseded, and whether it's still trusted.

The architecture separates the core memory engine from framework adapters. This means swapping from LangChain to Vercel AI SDK doesn't change how memories are stored or retrieved. Adapters are published as separate npm packages (`@atomicmemory/core`, `sdk`, `cli`, `mcp-server`) and framework-specific wrappers.

Benchmark results place it ahead of alternatives on the BEAM suite (testing retrieval accuracy at 100K, 1M, and 10M memory scales) and LoCoMo10 (long-context memory), making it a strong choice for production deployments where memory accuracy matters.

The MCP server integration is notable: any MCP-compatible host can connect to AtomicMemory without a custom adapter, which covers Claude Code, OpenClaw, Hermes, and future hosts automatically.

## Related Entries

- [[agentmemory]] ([AgentMemory](../tools/agentmemory.md))
- [[tencent-db-agent-memory]] ([Tencent DB Agent Memory](../tools/tencent-db-agent-memory.md))
- [[shokunin-memory-system]] ([Shokunin Memory System](../tools/shokunin-memory-system.md))
- [[ilnamiqui-session-memory]] ([Ilnamiqui Session Memory](../tips/ilnamiqui-session-memory.md))

---
<!-- RU -->

## Краткое описание

AtomicMemory — open-source система семантической памяти для AI-агентов и приложений с возможностью полной инспекции. Разработана AtomicStrata: захватывает контекст разговоров, использует прошлые взаимодействия для генераций и переносит знания между сессиями, оставаясь независимой от SDK и полностью аудируемой.

## Ключевые идеи

- **Архитектура, независимая от SDK**: построена на едином ядре; адаптеры для фреймворков (Vercel AI SDK, OpenAI Agents SDK, LangChain, LangGraph, Mastra) — тонкие удобные обёртки, а не обязательные зависимости
- **Память с поддержкой корректировок**: поддерживает замену, уточнение, удаление, отслеживание происхождения и ревизию с учётом доверия — воспоминания эволюционируют, а не накапливают устаревшие факты
- **Лидирующие результаты бенчмарков**: лучшие показатели на BEAM-100K (0.7375), BEAM-1M (0.6625), BEAM-10M (0.4875) и LoCoMo10 (0.8396) — конкурентно и по точности, и по стоимости
- **Локальное развёртывание и self-hosting**: деплой через Docker с Postgres/pgvector; без привязки к вендору, полностью аудируемое хранилище памяти
- **Широкая интеграция**: опубликованные пакеты для core, SDK, CLI и MCP-сервера; плагины для Claude Code, OpenClaw и Hermes (Codex и Cursor — в разработке)
- **Решение проблемы «чёрного ящика»**: противоположность непрозрачной памяти агентов — open source, self-hosted, каждая операция с памятью инспектируема

## Подробнее

AtomicMemory решает фундаментальную проблему агентного AI: агенты забывают всё между сессиями, а когда помнят — их память непрозрачна и не поддаётся корректировке. Система хранит воспоминания как структурированные, версионированные объекты с полным отслеживанием происхождения — можно проследить, почему существует воспоминание, что оно заменило и актуально ли оно.

Архитектура разделяет ядро памяти и адаптеры фреймворков. Смена LangChain на Vercel AI SDK не меняет способ хранения или извлечения воспоминаний. Адаптеры публикуются как отдельные npm-пакеты (`@atomicmemory/core`, `sdk`, `cli`, `mcp-server`) и обёртки под конкретные фреймворки.

Результаты бенчмарков ставят систему впереди альтернатив на наборе BEAM (точность извлечения при 100K, 1M и 10M воспоминаний) и LoCoMo10 (длинноконтекстная память), что делает её надёжным выбором для продакшена, где важна точность памяти.

Интеграция через MCP-сервер заслуживает внимания: любой MCP-совместимый хост подключается к AtomicMemory без кастомного адаптера — это покрывает Claude Code, OpenClaw, Hermes и будущие хосты автоматически.

## Связанные записи

- [[agentmemory]] ([AgentMemory](../tools/agentmemory.md))
- [[tencent-db-agent-memory]] ([Tencent DB Agent Memory](../tools/tencent-db-agent-memory.md))
- [[shokunin-memory-system]] ([Shokunin Memory System](../tools/shokunin-memory-system.md))
- [[ilnamiqui-session-memory]] ([Ilnamiqui Session Memory](../tips/ilnamiqui-session-memory.md))
