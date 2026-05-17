---
title: "TencentDB Agent Memory: Local Long-Term Memory for AI Agents"
title_ru: "TencentDB Agent Memory: локальная долгосрочная память для AI-агентов"
category: tools
tags: [agent-memory, long-term-memory, tencent, local, token-efficiency, openclaw, mcp]
updated: 2026-05-17
sources:
  - https://github.com/Tencent/TencentDB-Agent-Memory
---

## Summary
TencentDB Agent Memory is a fully local, zero-API-key long-term memory system for AI coding agents that uses a 4-tier progressive pipeline combining symbolic short-term memory and layered long-term memory — cutting token usage by up to 61% and improving task pass rate by 51% in benchmarks with OpenClaw.

## Key Ideas
- **Symbolic short-term memory** compresses heavy tool logs and execution traces into compact Mermaid diagram symbols instead of storing them verbatim, dramatically reducing context window consumption.
- **Layered long-term memory** distills fragmented conversation history into structured personas and scene graphs rather than flat vector piles — preserving semantic relationships between interactions.
- 4-tier progressive pipeline: working memory → episodic memory → semantic memory → procedural memory, with each tier distilling from the one below.
- Zero external API dependencies — all memory operations run locally with no cloud service calls, unlike RAG systems that require a vector DB API or embedding service.
- Benchmarked with OpenClaw: 61.38% token reduction, 51.52% pass rate improvement (relative).

## Details
Most agent memory systems face a fundamental tension: storing enough context to maintain coherence across sessions vs. keeping the active context window small enough for the model to focus. Flat vector stores dump everything into embedding space and retrieve k-nearest neighbors, which works for factual lookup but loses temporal structure and task context.

TencentDB Agent Memory addresses this with a hierarchical approach. The Mermaid-symbol compression in the short-term layer is particularly novel: instead of including raw tool call logs (which can be hundreds of tokens each), the system converts them into compact graph notation that a model can parse in far fewer tokens while preserving the causal relationships between tool calls and their outcomes.

The long-term layer maintains structured "personas" (what the agent has learned about a user's preferences and patterns) and "scenes" (what task context looked like at different points), rather than treating all memories as equally-weighted embedding vectors. This enables retrieval that respects task boundaries and user context.

**Compatibility**: designed to integrate with any MCP-compatible coding agent. The primary benchmark target is OpenClaw (open-source), but the MCP interface makes it compatible with Claude Code, Cursor, Codex CLI, and OpenCode.

## Related Entries
- [[shokunin-memory-system]]
- [[claude-code-memory]]
- [[gnosis-mcp]]
- [[claude-code-extensions-overview]]

---
<!-- RU -->

## Краткое описание
TencentDB Agent Memory — полностью локальная система долгосрочной памяти для AI-агентов без зависимостей от внешних API: 4-уровневый прогрессивный конвейер сочетает символическую краткосрочную и слоистую долгосрочную память, сокращая использование токенов до 61% и улучшая показатель прохождения задач на 51% в бенчмарках с OpenClaw.

## Ключевые идеи
- **Символическая краткосрочная память** сжимает тяжёлые журналы инструментов и трассировки выполнения в компактные символы диаграмм Mermaid вместо дословного хранения — резко сокращая потребление контекстного окна.
- **Слоистая долгосрочная память** дистиллирует фрагментарную историю разговоров в структурированные персоны и граф сцен, а не в плоские векторные кучи — сохраняя семантические связи между взаимодействиями.
- 4-уровневый прогрессивный конвейер: рабочая память → эпизодическая память → семантическая память → процедурная память, каждый уровень дистиллирует из нижележащего.
- Нулевые зависимости от внешних API — все операции памяти выполняются локально, без обращений к облачным сервисам.
- Бенчмарки с OpenClaw: -61,38% токенов, +51,52% к показателю прохождения задач (относительное).

## Подробнее
Плоские векторные хранилища теряют временну́ю структуру и контекст задач. TencentDB Agent Memory решает это через иерархический подход. Компрессия символами Mermaid в краткосрочном слое особенно нова: вместо дословных журналов вызовов инструментов (сотни токенов каждый) система конвертирует их в компактную нотацию графа, которую модель разбирает за значительно меньшее число токенов, сохраняя при этом причинно-следственные связи.

Долгосрочный слой поддерживает структурированные «персоны» (что агент узнал о предпочтениях пользователя) и «сцены» (каким был контекст задачи в разные моменты) — вместо равновзвешенных векторных эмбеддингов. Это обеспечивает поиск, уважающий границы задач и контекст пользователя.

## Связанные записи
- [[shokunin-memory-system]]
- [[claude-code-memory]]
- [[gnosis-mcp]]
- [[claude-code-extensions-overview]]
