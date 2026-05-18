---
title: "Karpathy's 3-Strategy System: LLM Wiki, Auto-Research, Context Engineering"
title_ru: "Система Карпатского: LLM-вики, авторесёрч, контекст-инжиниринг"
category: tips
tags: [karpathy, llm-knowledge-base, wiki, auto-research, context-engineering, claude-md, claude-code, self-improvement]
aliases: [Karpathy LLM knowledge base, auto research loop, Karpathy wiki method, context engineering Karpathy]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.youtube.com/watch?v=yfeHoOkn2TI
---

## Summary

Andrej Karpathy's three-strategy system for 10x productivity with Claude Code: (1) maintain an LLM-managed knowledge base (wiki) that compounds over time, (2) create self-improving auto-research loops where AI proposes and validates changes, and (3) practice context engineering — feeding the right information to the model for each task. The system is self-sustaining because "LLMs don't get bored."

## Key Ideas

- **LLM knowledge base has three layers**: raw resources (read-only data dump), wiki (organized summaries maintained by Claude), schema (instruction file telling Claude how to structure and maintain the wiki)
- **Auto-research loop**: propose change → test → evaluate → keep or discard → repeat; Karpathy found 20 improvements stacking to 11% gain; Shopify CEO ran similar loop for 19% improvement while sleeping
- **Context engineering**: the CLAUDE.md file is the critical lever — tells Claude project structure, conventions, and common mistakes to avoid, kept under ~50 lines
- **Hooks enable automation**: a hook can remind you to run the knowledge-base improvement cycle when you start a new Claude Code session
- **Key Karpathy insight**: "LLMs don't get bored" — unlike humans who abandon wikis, AI can maintain them indefinitely

## Details

**Strategy 1 — LLM Knowledge Base**: Most people use AI as a search engine that starts from scratch each session. Karpathy's fix: have Claude build and maintain a personal encyclopedia. Layer 1 is raw data (articles, transcripts, PDFs) that Claude reads but never modifies. Layer 2 is the wiki where Claude creates summaries, concept breakdowns, cross-references. Layer 3 is a schema/instruction file telling Claude what format to use, what conventions to follow, and what to do when a new source is added (including running a "health check" to find contradictions and stale info).

**Strategy 2 — Auto-Research**: An agentic loop that finds improvements without human intervention. For measurable outcomes (code performance) this is direct: agent proposes change, runs tests, compares metrics, keeps improvement. For non-measurable things (copywriting quality), use chat history as a proxy: if you went back-and-forth to get the output right, that conversation history signals quality and the system can learn from it. Claude Code's `loop` and `schedule` features support automated improvement cycles; hooks can trigger it per-session.

**Strategy 3 — Context Engineering**: Karpathy: "context engineering is the delicate art and science of filling the context window with just the right information for the next step." Two practical applications: (a) CLAUDE.md file (prompt: "Create a CLAUDE.md for this project. Include what this project is, folder structure, what I'm currently building, and common mistakes to avoid. Keep it under 50 lines."); (b) scoping context to the task — don't load the entire codebase when only the relevant scripts and examples are needed. Skills can auto-load expert frameworks for specific question types.

## Video Notes

- [0:24] Strategy 1: LLM knowledge bases — the problem of "rediscovering from scratch every session"
- [2:42] Strategy 2: Auto-research — Karpathy's open-source project and 11% gain
- [6:50] Strategy 3: Context engineering — Karpathy: "it's a skill issue" when AI doesn't work
- [7:27] How to properly context engineer: CLAUDE.md + scoped context

## Related Entries

- [[karpathy-claude-code-guidelines]] ([Karpathy Claude Code Guidelines](../tips/karpathy-claude-code-guidelines.md))
- [[karpathy-killed-rag-obsidian]] ([Karpathy on Knowledge Management](../tips/karpathy-killed-rag-obsidian.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[context-engineering-ai-agents-pipeline]] ([Context Engineering](../tips/context-engineering-ai-agents-pipeline.md))
- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))

---
<!-- RU -->

## Краткое описание

Трёхстратегийная система Андрея Карпатского для 10-кратного роста продуктивности с Claude Code: (1) LLM-вики с накоплением знаний, (2) авторесёрч-петли для самоулучшения, (3) контекст-инжиниринг. Система самодостаточна — "LLM не устают обслуживать вики, в отличие от людей."

## Ключевые идеи

- **LLM-вики состоит из трёх слоёв**: сырые ресурсы (неизменяемый датадамп), вики (организованные выжимки, поддерживаемые Claude), схема (инструкции Claude по структуре)
- **Петля авторесёрча**: предложить изменение → тестировать → оценить → оставить или выбросить → повторить; Карпатский нашёл 20 улучшений с суммарным эффектом 11%; CEO Shopify — 19% за ночь
- **Контекст-инжиниринг**: файл CLAUDE.md — ключевой рычаг; описывает проект, структуру папок, соглашения и типичные ошибки, до ~50 строк
- **Хуки автоматизируют**: хук напоминает запустить цикл улучшения вики при старте сессии
- **Инсайт Карпатского**: "LLM не устают" — в отличие от людей, AI может поддерживать вики бесконечно

## Подробнее

Стратегия 1: Claude строит и поддерживает персональную энциклопедию. Сырые данные — только для чтения. Вики — живой документ, который Claude обновляет. Схема — инструкция Claude о формате и конвенциях, включая периодический "аудит здоровья" для поиска противоречий.

Стратегия 2: для неизмеримых вещей (качество текста) используется история переписки как прокси качества — если много итераций, значит результат сложно получить, и система должна учиться на этих итерациях.

Стратегия 3: "Контекст-инжиниринг — это тонкое искусство наполнить контекстное окно именно той информацией, которая нужна для следующего шага." CLAUDE.md + скоупинг контекста к конкретной задаче.

## Заметки по видео

- [0:24] Стратегия 1: проблема "заново открывать знания с нуля при каждой сессии"
- [2:42] Стратегия 2: авторесёрч и 11% прирост
- [6:50] Стратегия 3: "это вопрос навыка" — Карпатский о проблемах с AI

## Связанные записи

- [[karpathy-claude-code-guidelines]] ([Karpathy Claude Code Guidelines](../tips/karpathy-claude-code-guidelines.md))
- [[karpathy-killed-rag-obsidian]] ([Karpathy on Knowledge Management](../tips/karpathy-killed-rag-obsidian.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[context-engineering-ai-agents-pipeline]] ([Context Engineering](../tips/context-engineering-ai-agents-pipeline.md))
- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))
