---
title: "Expensive Model ≠ Smart Agent: Anatomy of the AI Agent Brain"
title_ru: "Дорогая модель ≠ умный агент: анатомия мозга AI-агента"
category: agents
tags: [ai-agent, smart-routing, rag, agent-memory, coala, model-routing, cost-optimization, claude-code-architecture]
date: 2026-04-16
updated: 2026-05-17
transcript: unavailable
sources:
  - https://www.youtube.com/watch?v=vjMxeQ3aIGM
---

## Summary

Why an expensive frontier model doesn't make a smart agent. Covers smart model routing (10x cost savings via query classifier and RouteLLM), RAG vs long context decision framework, four types of agent memory from the CoALA framework (procedural, semantic, episodic, working), and a deep dive into Claude Code's memory architecture with 11 subsystems and file-based storage without vector DB.

## Key Ideas
- **Smart routing saves 10x:** RouteLLM + query classifier routes simple queries to cheap models, complex ones to frontier — reducing cost by up to 10x without quality loss
- **RAG vs long context decision framework:** When to retrieve vs when to stuff the context window — it depends on data freshness, query complexity, and latency requirements
- **Four types of agent memory (CoALA framework):** Procedural (skills/capabilities), Semantic (knowledge/facts), Episodic (past experiences), Working (current context)
- **Claude Code memory architecture deep dive:** 11 subsystems, file-based storage (no vector DB!), background agents for memory maintenance. Uses CLAUDE.md, .claude/ directory, and conversation-level memory
- **Prompt caching and thinking mode:** How to leverage caching for cost reduction and when thinking/reasoning mode is worth the extra tokens
- **Frontier model won't save bad architecture:** The quality of an agent is determined by its memory, routing, and context management — not the underlying model

## Video Notes

| Timestamp | Key Point |
|---|---|
| [0:00] | Why expensive model ≠ smart agent |
| [~5:00] | Smart routing: RouteLLM, query classifier, 10x savings |
| [~10:00] | RAG vs long context decision framework |
| [~15:00] | Four memory types from CoALA: procedural, semantic, episodic, working |
| [~25:00] | Claude Code memory architecture: 11 subsystems, no vector DB |
| [~35:00] | Prompt caching and thinking mode optimization |

## Details

This is the second video in Bereznitsky's "System Design AI Agent — Inside Out" series. The core thesis challenges the common assumption that using a better/faster/more expensive model will improve agent quality. In reality, the bottlenecks are in the surrounding architecture: how you route queries, manage memory, handle context windows, and structure retrieval.

The Claude Code architecture breakdown is particularly valuable — it reveals that Claude Code uses 11 memory subsystems with purely file-based storage (no vector database). This is consistent with Karpathy's LLM Wiki pattern: structured markdown files with a schema layer for context injection, rather than traditional RAG infrastructure.

## Related Entries
- [[claude-code-memory]] ([Claude Code Memory: CLAUDE.md and Auto Memory](../agents/claude-code-memory.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent: Pipeline, Loop, Tools, and Traps](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[ai-agents-arr-framework-ooda-loop]] ([AI Agents: ARR Framework, OODA Loop](../concepts/ai-agents-arr-framework-ooda-loop.md))
---
<!-- RU -->

## Краткое описание

Почему дорогая frontier-модель не делает агента умным. Smart routing (экономия 10x через RouteLLM), RAG vs длинный контекст, четыре типа памяти агента по CoALA (процедурная, семантическая, эпизодическая, рабочая), и глубокий разбор архитектуры памяти Claude Code — 11 подсистем, file-based storage без векторной БД.

## Ключевые идеи
- **Smart routing экономит 10x:** RouteLLM + классификатор запросов направляет простые запросы к дешёвым моделям, сложные — к frontier
- **RAG vs длинный контекст:** Фреймворк выбора — зависит от свежести данных, сложности запроса и требований к задержке
- **Четыре типа памяти (CoALA):** Процедурная (навыки), Семантическая (знания), Эпизодическая (опыт), Рабочая (текущий контекст)
- **Архитектура памяти Claude Code:** 11 подсистем, хранение на файлах (без векторной БД!), фоновые агенты для обслуживания памяти
- **Prompt caching и thinking mode:** Как использовать кэширование для снижения затрат
- **Frontier-модель не спасёт плохую архитектуру:** Качество агента определяется памятью, роутингом и управлением контекстом

## Заметки по видео

| Таймкод | Ключевой момент |
|---|---|
| [~5:00] | Smart routing: RouteLLM, классификатор, экономия 10x |
| [~10:00] | RAG vs длинный контекст |
| [~15:00] | Четыре типа памяти CoALA |
| [~25:00] | Архитектура памяти Claude Code: 11 подсистем, без векторной БД |
| [~35:00] | Prompt caching и thinking mode |

## Связанные записи
- [[claude-code-memory]] ([Claude Code Memory: CLAUDE.md and Auto Memory](../agents/claude-code-memory.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent: Pipeline, Loop, Tools, and Traps](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[ai-agents-arr-framework-ooda-loop]] ([AI Agents: ARR Framework, OODA Loop](../concepts/ai-agents-arr-framework-ooda-loop.md))
