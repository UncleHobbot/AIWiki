---
title: "Hermes Agent + LLM Wiki: Compounding Knowledge Base"
title_ru: "Hermes Agent + LLM Wiki: накопительная база знаний"
category: agents
tags: [hermes-agent, llm-wiki, nous-research, knowledge-base, skill-system, compounding-knowledge, karpathy, open-source, second-brain]
aliases: [Hermes LLM Wiki, Hermes wiki skill, Nous Research LLM Wiki, hermes llmwiki]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.youtube.com/watch?v=YUz2CLLmdjA
  - https://github.com/NousResearch/hermes-agent
---

## Summary
Hermes Agent (by Nous Research) integrated Karpathy's LLM Wiki as a built-in skill, creating a self-hosted agent that builds persistent, compounding knowledge bases from research sessions — and improves its own skill library over time through a learning loop.

## Key Ideas
- **Hermes has a built-in learning loop:** it creates skills from experience, improves them as you use it, and builds a deeper model of the user across sessions — unlike most agents that reset each run.
- **LLM Wiki as a native Hermes skill:** after `hermes update`, the `/llmwiki <topic>` command starts building a structured wiki from any research topic — reading source docs, creating entity/concept pages, updating cross-references.
- **Three-layer LLM Wiki architecture inside Hermes:** (1) Raw sources — immutable; (2) Wiki — AI-owned markdown files; (3) Schema — the configuration AGENTS.md that turns the agent into a disciplined wiki maintainer.
- **Ingest: one source updates 10–15 wiki pages** — concepts, entities, summaries, cross-references all update in a single pass; this compounding effect is the core value proposition.
- **Lint operation keeps the wiki healthy:** finds contradictions, stale information, orphan pages, and missing connections; also suggests new questions to investigate.
- **Runs on a $5 VPS or GPU cluster, supports 200+ models via OpenRouter** — no vendor lock-in, switch models with one command.

## Details
Hermes Agent (github.com/NousResearch/hermes-agent, 26,000+ GitHub stars) is an open-source self-hosted agent from Nous Research. Its differentiating feature compared to most AI agents is a persistent skill system: procedures the agent learns and improves over repeated use, stored as structured files that persist between sessions.

The May 2026 update added LLM Wiki as a built-in skill. When activated with `/llmwiki <topic>`, Hermes:
1. Accepts raw source files (documents, articles, code, research papers)
2. Reads each source and extracts key information
3. Writes/updates structured wiki pages (summaries, entity pages, concept pages, comparison pages)
4. Maintains cross-references between all pages
5. Notes when new information contradicts existing claims
6. Updates the `index.md` catalog and `log.md` chronological record

The Nous Research team demonstrated this by feeding Hermes their own GitHub projects, web sources, code, and research papers — producing a complete structured knowledge base of all their active work in a session that would have taken weeks manually.

**Comparison with pure RAG:**
- RAG: upload documents → query → AI finds relevant chunks → answer; resets each session
- LLM Wiki in Hermes: sources compiled once → wiki grows persistently → queries answered from pre-compiled pages → wiki continuously improves

**Why humans abandon wikis (and why Hermes does not):** The maintenance burden (updating cross-references, keeping summaries current) grows faster than the value for humans. An AI agent does not get bored, never forgets a cross-reference, and can update 15 files in one pass.

**Access channels:** Telegram, Discord, Slack, WhatsApp, Signal — users can interact with their wiki through any messaging platform.

## Video Notes
- [0:30] The problem: AI sessions start from scratch every time — all research, all insights lost
- [1:30] LLM Wiki concept: compile-once instead of retrieve-every-time
- [2:30] Karpathy published April 4, 2026 — 5,000+ GitHub stars in under 48 hours
- [3:30] Hermes' built-in learning loop: skills created from experience, improving over time
- [4:30] LLM Wiki is now a built-in Hermes skill — `hermes update` then `/llmwiki <topic>`
- [5:30] Three operations: Ingest, Query, Lint
- [7:00] Lint: health-check for contradictions, stale info, orphan pages
- [8:00] Installation: one command on Linux, macOS, or WSL 2
- [9:00] Viewing results in Obsidian graph view — hubs, orphans, connection density visible

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[autonomous-personal-agents-openclaw-hermes-zeroclaw]] ([Autonomous Personal AI Agents: OpenClaw, Hermes, ZeroClaw](../agents/autonomous-personal-agents-openclaw-hermes-zeroclaw.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem](../tools/llm-wiki-ecosystem.md))
- [[awesome-agent-skills]] ([Awesome Agent Skills](../tools/awesome-agent-skills.md))

---
<!-- RU -->

## Краткое описание
Hermes Agent от Nous Research интегрировал LLM Wiki Karpathy как встроенный навык, создав самохостируемого агента, который строит персистентные накопительные базы знаний из исследовательских сессий и улучшает собственный набор навыков через цикл обучения.

## Ключевые идеи
- **Встроенный цикл обучения Hermes:** создаёт навыки из опыта, улучшает их в процессе использования и строит модель пользователя между сессиями.
- **LLM Wiki как нативный навык Hermes:** после `hermes update` команда `/llmwiki <тема>` начинает строить структурированную вики на любую тему.
- **Трёхуровневая архитектура LLM Wiki внутри Hermes:** (1) исходные документы — неизменяемые; (2) вики — markdown-файлы, управляемые агентом; (3) схема — конфигурационный AGENTS.md.
- **Ingest: один источник обновляет 10–15 страниц вики** — концепты, сущности, резюме, перекрёстные ссылки — всё за один проход.
- **Операция Lint поддерживает вики в порядке:** находит противоречия, устаревший контент, изолированные страницы и недостающие связи.
- **Работает на VPS за $5, поддерживает 200+ моделей через OpenRouter** — без привязки к провайдеру.

## Подробнее
Hermes Agent (26 000+ звёзд на GitHub) — это open-source самохостируемый агент от Nous Research. Его ключевое отличие — персистентная система навыков: процедуры, которые агент учится и улучшает в процессе использования, хранящиеся как структурированные файлы между сессиями.

Обновление мая 2026 добавило LLM Wiki как встроенный навык. При активации через `/llmwiki <тема>` Hermes принимает источники, читает каждый, создаёт/обновляет структурированные страницы вики, поддерживает перекрёстные ссылки и отмечает противоречия с существующими утверждениями.

**Почему люди бросают вики, а Hermes — нет:** поддержка перекрёстных ссылок и актуальности резюме — это рутинная работа, которая растёт быстрее, чем ценность вики для человека. Агент не устаёт, никогда не забывает перекрёстную ссылку и может обновить 15 файлов за один проход.

**Каналы доступа:** Telegram, Discord, Slack, WhatsApp, Signal.

## Заметки по видео
- [0:30] Проблема: каждая сессия начинается с нуля — всё исследование и инсайты теряются
- [1:30] Концепция LLM Wiki: компиляция один раз вместо извлечения при каждом запросе
- [2:30] Karpathy опубликовал 4 апреля 2026 — 5000+ звёзд на GitHub за 48 часов
- [4:30] LLM Wiki — встроенный навык Hermes: `hermes update`, затем `/llmwiki <тема>`
- [5:30] Три операции: Ingest, Query, Lint
- [8:00] Установка: одна команда в Linux, macOS или WSL 2
- [9:00] Просмотр результатов в Obsidian graph view

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[autonomous-personal-agents-openclaw-hermes-zeroclaw]] ([Autonomous Personal AI Agents: OpenClaw, Hermes, ZeroClaw](../agents/autonomous-personal-agents-openclaw-hermes-zeroclaw.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem](../tools/llm-wiki-ecosystem.md))
- [[awesome-agent-skills]] ([Awesome Agent Skills](../tools/awesome-agent-skills.md))
