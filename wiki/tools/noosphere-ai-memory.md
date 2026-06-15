---
title: "Noosphere: Auditable Human-AI Shared Memory Layer"
title_ru: "Noosphere: проверяемый общий слой памяти для людей и AI"
category: tools
tags: [memory, knowledge-base, agents, opencode, hermes, obsidian, postgresql, confidence-scoring, wiki, self-hosted]
aliases: [Noosphere, noosphere memory, SweetSophia/noosphere, auditable AI memory]
confidence: medium
updated: 2026-06-05
sources:
  - https://github.com/SweetSophia/noosphere
  - https://www.reddit.com/r/opencode/comments/1ttlf3h/i_built_noosphere_auditable_ai_memory/
---

## Summary
Noosphere is a self-hosted memory and knowledge layer for AI agents and humans — a PostgreSQL-backed wiki with confidence scoring, revision history, and scoped API keys that lets agents recall structured context while humans browse and curate the same data through a Markdown interface.

## Key Ideas
- **Structured over semantic**: stores knowledge as human-readable wiki articles with explicit metadata, status lifecycles (draft → reviewed → published), and confidence scores (low/medium/high) — not as opaque embedding vectors.
- **Multi-agent first**: integrates with OpenClaw, Hermes Agent, Opencode, and Kilo Code via standardized REST API; scoped API keys restrict which agent sees which content by topic tags.
- **Revision history and auditability**: every article has soft deletes and full revision history — humans can see exactly what agents wrote, when, and reverse any change.
- **Token-budgeted recall**: multi-provider recall orchestration includes token budgeting for prompt-safe context windows, deduplication, and conflict detection across memory providers.
- **Obsidian-compatible**: export/import in Obsidian format for users who want a human-readable vault alongside the database.

## Details
Noosphere addresses a specific gap in agent memory: most systems store memories as embeddings (invisible to humans, hard to audit, impossible to edit cleanly) or as flat Markdown files (no schema, no conflict detection, no confidence tracking). Noosphere puts a PostgreSQL database at the core with Redis caching, but surfaces the content as a Markdown wiki so humans and agents share the same view.

The confidence scoring system (low/medium/high) lets agents and humans mark how certain they are about a stored fact, enabling downstream filtering — agents can choose to only rely on `high` confidence facts for critical decisions, while using `medium` confidence facts for drafting.

The multi-provider recall orchestration supports Noosphere articles alongside Hindsight (another memory system), giving agents a unified recall interface even when memory is distributed across providers.

**Status lifecycle**: `draft` → `reviewed` → `published`. Agents write drafts; humans can review and promote or reject them before they enter the agent's active context.

## Related Entries
- [[agentmemory]] ([AgentMemory: Persistent Memory for AI Coding Agents](../tools/agentmemory.md))
- [[anthropic-agent-memory-dreaming]] ([Anthropic Agent Memory & Dreaming](../agents/anthropic-agent-memory-dreaming.md))
- [[shokunin-memory-system]] ([Shokunin Memory System](../tools/shokunin-memory-system.md))
- [[agent-lifespan-agingbench]] ([Agent Lifespan Engineering: AgingBench](../concepts/agent-lifespan-agingbench.md))
- [[atomicmemory-semantic-memory]] ([AtomicMemory](../tools/atomicmemory-semantic-memory.md))
- [[turbo-graph-rag-memory]] ([turbo-graph — Graph Memory for RAG](../tools/turbo-graph-rag-memory.md))

---
<!-- RU -->

## Краткое описание
Noosphere — self-hosted слой памяти и знаний для AI-агентов и людей: вики на базе PostgreSQL с оценкой достоверности, историей ревизий и ключами API с ограниченным доступом, позволяющая агентам извлекать структурированный контекст, а людям — просматривать и курировать те же данные через интерфейс Markdown.

## Ключевые идеи
- **Структурированное хранение вместо семантического**: wiki-статьи, читаемые людьми, с явными метаданными, жизненным циклом статусов (черновик → проверено → опубликовано) и оценками достоверности.
- **Мульти-агентная интеграция**: OpenClaw, Hermes Agent, Opencode, Kilo Code через REST API; ключи API с ограниченным доступом по тегам тем.
- **История ревизий и проверяемость**: полная история изменений каждой статьи, мягкие удаления — люди видят, что именно записал агент и когда.
- **Recall с ограничением токенов**: оркестрация recall от нескольких провайдеров с бюджетированием токенов, дедупликацией и обнаружением конфликтов.
- **Совместимость с Obsidian**: экспорт/импорт в формате Obsidian.

## Подробнее
Noosphere решает конкретный пробел в памяти агентов: большинство систем хранят воспоминания как embeddings (невидимые для людей, трудно проверяемые) или как плоские Markdown-файлы (без схемы, без обнаружения конфликтов, без отслеживания достоверности). Noosphere помещает PostgreSQL в центр с Redis-кешированием, но отображает контент как Markdown-вики, чтобы люди и агенты видели одно и то же.

**Жизненный цикл статусов**: `draft` → `reviewed` → `published`. Агенты пишут черновики; люди могут проверять и продвигать или отклонять их до попадания в активный контекст агента.

## Связанные записи
- [[agentmemory]] ([AgentMemory: Persistent Memory for AI Coding Agents](../tools/agentmemory.md))
- [[anthropic-agent-memory-dreaming]] ([Anthropic Agent Memory & Dreaming](../agents/anthropic-agent-memory-dreaming.md))
- [[shokunin-memory-system]] ([Shokunin Memory System](../tools/shokunin-memory-system.md))
- [[agent-lifespan-agingbench]] ([Agent Lifespan Engineering: AgingBench](../concepts/agent-lifespan-agingbench.md))
- [[atomicmemory-semantic-memory]] ([AtomicMemory](../tools/atomicmemory-semantic-memory.md))
- [[turbo-graph-rag-memory]] ([turbo-graph — графовая память для RAG](../tools/turbo-graph-rag-memory.md))
