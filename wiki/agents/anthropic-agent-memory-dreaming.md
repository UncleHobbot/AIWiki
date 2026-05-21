---
title: "Anthropic Agent Memory and Dreaming: Cross-Session Learning for Claude Agents"
title_ru: "Память и «сновидения» агентов Anthropic: межсессионное обучение для агентов Claude"
category: agents
tags: [anthropic, claude, memory, dreaming, agent-memory, managed-agents, cross-session, self-learning, multi-agent]
aliases: [Claude agent memory, Anthropic dreaming, agent dreaming, claude managed agents memory]
confidence: high
date: 2026-05-21
updated: 2026-05-21
sources:
  - https://www.youtube.com/watch?v=IGo225tfF2I
---

## Summary

Anthropic has launched **Memory** and **Dreaming** as building blocks for Claude managed agents — enabling agents to learn from previous tasks, accumulate shared knowledge across agent swarms, and continuously improve without resetting to a blank slate each session.

## Key Ideas

- **Memory = cross-session learning.** Agents can carry forward learnings from previous tasks rather than starting from scratch. Performance improves from task to task, not just within a session.
- **File-system model.** Memory is implemented as a file system that Claude navigates. Because Opus 4.7 is already strong at file-system-based memory (navigating, reading, updating files), Anthropic chose to lean on this capability rather than build a specialised vector store.
- **Multi-agent shared memory.** Memory is designed to work *across* agents, not just within a single agent. Agent swarms can contribute to and draw from a shared organisational memory layer — "swarms of agents contributing to and maintaining a shared understanding of the organisation they work in."
- **Dreaming = background memory optimisation.** Dreaming is a process *decoupled from the agent loop* that globally optimises and reconciles memory across agents. It runs after task completion, not during, adding zero latency to active agents.
- **Dreaming raises the floor.** Shared memory raises the baseline performance for every agent; dreaming raises it further by continuously curating and improving the quality of stored memories.
- **Proven results:** Racketin saw a **97% decrease in first-pass errors** in production agents; Wise Docs reduced common issues in their document verification pipeline using cross-session memory.

## Details

### The Problem Memory Solves

Without memory, each agent instance starts from the same blank slate. In a fleet of agents handling repeated or related tasks, every agent independently re-learns the same patterns, makes the same mistakes, and cannot benefit from what other agents discovered. The goal is for performance to improve not just within a task (via context) but *from task to task* and *across the entire agent fleet*.

### How Memory Works

Memory is modelled as a file system to which agents can read and write. The design philosophy is "get out of Claude's way" — Opus 4.7 is state-of-the-art at file-system navigation and increasingly capable of discerning which context is most important to save for its future self. Rather than a rigid specialised memory API, the memory primitive is intentionally flexible, letting the model decide what to record, how to structure it, and how to retrieve it.

Memory supports:
- **Common strategies and previous mistakes** accumulated across tasks
- **Codebase-specific knowledge** — tools, file locations, conventions
- **Cross-agent transfer** — learning from what other agents in the fleet discovered

### Dreaming: Background Memory Curation

Dreaming is Anthropic's "frontier memory feature" — a process that runs independently of the main agent loop and globally optimises memory:

- **Decoupled from the agent loop:** no risk of an agent trading off task completion against memory quality
- **Cross-session, cross-agent analysis:** dreaming looks at transcripts from multiple agents and sessions to identify patterns a single agent in isolation might miss
- **Zero hot-path latency:** runs entirely asynchronously after tasks complete
- **Analogy to test-time compute:** just as letting models "spend tokens to explore a problem" produces better outcomes, dreaming lets agents spend work upfront to curate higher-quality memory — paying dividends for all downstream agent performance

### Timeline of Anthropic Agent Capabilities

| Year | Feature |
|---|---|
| 2024 | Model Context Protocol (MCP) — external tools and data access |
| 2025 (early) | Claude Code + Agent SDK — lowered barrier to building agents |
| 2025 (later) | Skills — generic abstraction for bolting on new capabilities |
| 2026 (April) | Claude Managed Agents — platform for reliably running long-horizon agents |
| 2026 (May) | **Memory + Dreaming** — cross-session learning and background memory optimisation |

### Metr Research Context

In 2025, Metr released a study showing the length of tasks that agents can complete is **doubling every seven months**. Managing context over long-horizon tasks is the key challenge that memory directly addresses.

## Related Entries

- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[shokunin-memory-system]] ([Shokunin Memory System](../tools/shokunin-memory-system.md))
- [[memory-skills-unified-harness]] ([Memory and Skills as a Unified Harness](../concepts/memory-skills-unified-harness.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))

---
<!-- RU -->

## Краткое описание

Anthropic запустила **Memory** (Память) и **Dreaming** (Сновидения) как строительные блоки для управляемых агентов Claude — позволяющие агентам учиться на предыдущих задачах, накапливать общие знания в роях агентов и непрерывно улучшаться, не сбрасываясь к нулю при каждой новой сессии.

## Ключевые идеи

- **Память = межсессионное обучение.** Агенты сохраняют знания из предыдущих задач. Производительность растёт от задачи к задаче, а не только внутри сессии.
- **Модель файловой системы.** Память реализована как файловая система, которую Claude обходит. Поскольку Opus 4.7 силён в навигации по файловым системам, Anthropic предпочла опираться на эту возможность.
- **Общая память мультиагентов.** Память работает *между* агентами, а не только внутри одного. Рои агентов вносят вклад и используют общий организационный слой памяти.
- **Dreaming = фоновая оптимизация памяти.** Dreaming — процесс, *отделённый от цикла агента*, который глобально оптимизирует и согласовывает память между агентами. Работает после завершения задач, добавляя нулевую задержку активным агентам.
- **Доказанные результаты:** Racketin — **97% снижение ошибок первого прохода** в production-агентах; Wise Docs сократила частые проблемы в конвейере верификации документов.

## Подробнее

### Проблема, которую решает память

Без памяти каждый экземпляр агента начинает с чистого листа. В парке агентов, выполняющих повторяющиеся задачи, каждый агент независимо заново учится тем же паттернам. Цель — чтобы производительность росла не только внутри задачи (через контекст), но и *от задачи к задаче* и *по всему парку агентов*.

### Как работает Dreaming

Dreaming — «граничная функция памяти» Anthropic — процесс, независимый от основного цикла агента: анализирует транскрипты нескольких агентов и сессий, находит паттерны, которые одиночный агент пропустил бы. Запускается асинхронно после завершения задач, без задержек для активных агентов. Аналогия с test-time compute: как выделение токенов на исследование проблемы улучшает результаты, dreaming позволяет агентам инвестировать усилия в качество памяти — это приносит дивиденды для всей последующей производительности агентов.

### Хронология возможностей агентов Anthropic

| Год | Функция |
|---|---|
| 2024 | MCP — доступ к внешним инструментам и данным |
| 2025 (начало) | Claude Code + Agent SDK |
| 2025 (позже) | Skills — абстракция для новых возможностей |
| 2026 (апрель) | Claude Managed Agents |
| 2026 (май) | **Memory + Dreaming** |

## Связанные записи

- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[shokunin-memory-system]] ([Shokunin Memory System](../tools/shokunin-memory-system.md))
- [[memory-skills-unified-harness]] ([Memory and Skills as a Unified Harness](../concepts/memory-skills-unified-harness.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
