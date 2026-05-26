---
title: "LLM Wiki"
title_ru: "LLM Wiki"
category: concepts
tags: [llm-wiki, karpathy, knowledge-base, compiled-knowledge, personal-wiki]
aliases: [LLM Wiki, Karpathy Wiki, LLM knowledge base]
updated: 2026-05-26
sources:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
---

## Summary
The LLM Wiki is a pattern proposed by Andrej Karpathy where an LLM agent incrementally builds and maintains a persistent, structured wiki of knowledge. Rather than retrieving from raw documents at query time (RAG), knowledge is pre-compiled into clean markdown entries that live in the agent's context window.

## Core Concepts
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md)) — The original pattern and three-layer architecture
- [[llm-wiki-compiled-knowledge-vs-rag]] ([Compiled Knowledge vs RAG](../concepts/llm-wiki-compiled-knowledge-vs-rag.md)) — Key architectural distinction
- [[llm-wiki-implementations-landscape]] ([Implementations Landscape](../concepts/llm-wiki-implementations-landscape.md)) — State of the ecosystem (May 2026)
- [[llm-wiki-academic-applications]] ([Academic Applications](../concepts/llm-wiki-academic-applications.md)) — Academic landscape and feature roadmap

## Implementations
- [[llm-wiki-ecosystem]] ([Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md)) — Curated map of open-source implementations
- [[llmwiki-open-source]] ([llmwiki (Open-Source)](../tools/llmwiki-open-source.md)) — Open-source implementation with local API
- [[graphify-llm-wiki]] ([Graphify](../tools/graphify-llm-wiki-graph-builder.md)) — Knowledge graph builder for codebases
- [[omegawiki-research-platform]] ([OmegaWiki](../tools/omegawiki-research-platform.md)) — Wiki-centric AI research platform
- [[wiki-os]] ([Wiki OS](../tools/wiki-os.md)) — Browser UI for LLM Wiki vaults

## Enterprise and Agent Integration
- [[llm-wiki-enterprise-patterns]] ([Enterprise Patterns](../agents/llm-wiki-enterprise-patterns.md)) — Scaling from personal to production
- [[hermes-agent-llm-wiki-integration]] ([Hermes + LLM Wiki](../agents/hermes-agent-llm-wiki-integration.md)) — Built-in LLM Wiki skill

## Setup Guides
- [[llm-wiki-setup-guide]] ([Practical Setup Guide](../tips/llm-wiki-setup-guide.md)) — Step-by-step from scratch
- [[llm-wiki-obsidian-build-guide]] ([Obsidian Build Guide](../tips/llm-wiki-obsidian-build-guide.md)) — Building in Obsidian
- [[llm-wiki-obsidian-codex-workflow]] ([Obsidian + Codex Workflow](../tips/llm-wiki-obsidian-codex-workflow.md)) — Obsidian and Codex second brain
- [[llm-wiki-scientific-research]] ([Scientific Research](../tips/llm-wiki-scientific-research.md)) — Academic writing use case

## Related Research
- [[lightrag-graph-rag]] ([LightRAG](../tools/lightrag-graph-rag.md)) — Graph-enhanced RAG (complementary approach)
- [[gnosis-mcp-vs-llm-wiki-pattern]] ([Gnosis MCP vs LLM Wiki](../concepts/gnosis-mcp-vs-llm-wiki-pattern.md)) — When to use which
- [[karma-knowledge-graph-enrichment]] ([KARMA](../concepts/karma-knowledge-graph-enrichment.md)) — Automated KG enrichment

---
<!-- RU -->

## Краткое описание
LLM Wiki — паттерн, предложенный Андреем Карпатым, в котором LLM-агент инкрементально строит и поддерживает постоянную структурированную вики знаний. Вместо извлечения из сырых документов во время запроса (RAG), знания предкомпилируются в чистые markdown-записи, находящиеся в контекстном окне агента.

## Основные концепции
- [[llm-wiki-pattern]] — Оригинальный паттерн и трёхуровневая архитектура
- [[llm-wiki-compiled-knowledge-vs-rag]] — Ключевое архитектурное различие
- [[llm-wiki-implementations-landscape]] — Состояние экосистемы (май 2026)
- [[llm-wiki-academic-applications]] — Академический ландшафт и дорожная карта

## Реализации
- [[llm-wiki-ecosystem]] — Кураторская карта open-source реализаций
- [[llmwiki-open-source]] — Open-source реализация с локальным API
- [[graphify-llm-wiki]] — Построитель графов знаний для кодовых баз
- [[omegawiki-research-platform]] — Вики-центрированная платформа AI-исследований
- [[wiki-os]] — Браузерный UI для хранилищ LLM Wiki

## Интеграция с Enterprise и агентами
- [[llm-wiki-enterprise-patterns]] — Масштабирование от личного до продакшена
- [[hermes-agent-llm-wiki-integration]] — Встроенный навык LLM Wiki

## Руководства по настройке
- [[llm-wiki-setup-guide]] — Пошаговое руководство с нуля
- [[llm-wiki-obsidian-build-guide]] — Создание в Obsidian
- [[llm-wiki-obsidian-codex-workflow]] — Obsidian + Codex: второе сознание
- [[llm-wiki-scientific-research]] — Использование в научных исследованиях

## Связанные исследования
- [[lightrag-graph-rag]] — Графовый RAG (комплементарный подход)
- [[gnosis-mcp-vs-llm-wiki-pattern]] — Когда использовать Gnosis MCP, а когда LLM Wiki
- [[karma-knowledge-graph-enrichment]] — Автоматическое обогащение KG
