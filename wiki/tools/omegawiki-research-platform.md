---
title: "OmegaWiki: Wiki-Centric AI Research Platform"
title_ru: "OmegaWiki: вики-центрированная платформа для научных исследований"
category: tools
tags: [omegawiki, research, knowledge-graph, claude-code, paper-writing, citation, academic, karpathy]
date: 2026-05-16
updated: 2026-05-16
sources:
  - https://github.com/skyllwt/OmegaWiki
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
---

## Summary
OmegaWiki is an open-source, wiki-centric full-lifecycle AI research platform by DAIR Lab at Peking University, powered by 24 Claude Code skills that cover everything from paper ingestion to peer review response. It replaces flat RAG retrieval with a typed knowledge graph of 9 entity types and semantic edge labels, enabling knowledge that compiles once and compounds over time.

## Key Ideas
- 24 slash commands spanning the entire research lifecycle: paper ingestion, knowledge graph construction, gap detection, idea generation, experiment design, paper writing, and peer review response
- 9 typed entity types (Paper, Concept, Topic, Person, Idea, Experiment, Method, Summary, Foundation) connected by semantic edges like builds_on, improves_on, challenges, contradicts, and same_problem_as
- Wiki-centric approach outperforms RAG because knowledge compiles once and compounds; RAG re-derives context from scratch on every query
- Cross-model adversarial review using any OpenAI-compatible API as a second reviewer to strengthen papers before submission
- Bilingual support (English + Chinese) and compatibility with third-party Anthropic-compatible APIs (DeepSeek, Kimi, MiMo, GLM/Z.AI)
- Daily arXiv recommendations via GitHub Actions and knowledge graph visualization through web UI or Obsidian

## Details
OmegaWiki (skyllwt/OmegaWiki, 669+ stars, MIT license) rethinks how AI-assisted research tools should work. Instead of treating a corpus of papers as a flat vector store for retrieval-augmented generation, it builds a structured knowledge graph where every entity has a type and every relationship has a semantic label. This means the system understands that one paper *builds_on* another, or that a new method *challenges* an existing one — relationships that RAG simply cannot capture.

The platform provides 24 Claude Code slash commands organized into research phases. `/discover` can scan specific venues (ICLR, NeurIPS, ICML) for relevant work. The knowledge graph is stored as `edges.jsonl` and `citations.jsonl`, enabling both programmatic queries and visual exploration. Methods are first-class entities, making it possible to track how techniques evolve across papers.

A key design principle is anti-repetition memory: failed experiments are recorded in the graph so the system (and the researcher) avoids repeating dead ends. The cross-model adversarial review feature allows routing a draft to a different LLM via any OpenAI-compatible API, providing an independent critical perspective before submission. The project is built by the DAIR Lab team at Peking University: Weitong Qian, Beicheng Xu, Zhongao Xie, Bowen Fan, Guozheng Tang, Xinzhe Wu, Jiale Chen, and Mingtian Yang.

## Notable Quotes
> "knowledge compiles once and compounds; RAG re-derives from scratch every query" — OmegaWiki design philosophy

> "Failed experiments become anti-repetition memory" — OmegaWiki README

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[mathwiki-llm-research-automation]] ([LLM-Powered Math Research: Ideas to Steal for Your MathWiki](../research/mathwiki-llm-research-automation.md))
---
<!-- RU -->

## Краткое описание
OmegaWiki — открытая вики-центрированная платформа полного цикла научных исследований от лаборатории DAIR Пекинского университета, работающая на базе 24 навыков Claude Code и охватывающая всё — от загрузки статей до ответов на рецензии. Заменяет плоский RAG-поиск типизированным графом знаний из 9 типов сущностей и семантическими связями, позволяя знаниям накапливаться и усиливаться со временем.

## Ключевые идеи
- 24 команды (slash commands) покрывают весь жизненный цикл исследования: загрузка статей, построение графа знаний, обнаружение пробелов, генерация идей, планирование экспериментов, написание статей и ответы на рецензии
- 9 типизированных сущностей (Paper, Concept, Topic, Person, Idea, Experiment, Method, Summary, Foundation) связаны семантическими рёбрами: builds_on, improves_on, challenges, contradicts, same_problem_as
- Вики-центрированный подход превосходит RAG, поскольку знания компилируются один раз и накапливаются; RAG каждый раз заново извлекает контекст с нуля
- Перекрёстная состязательная рецензия с использованием любой OpenAI-совместимой модели в качестве второго рецензента для усиления статьи перед подачей
- Двуязычная поддержка (английский + китайский) и совместимость с Anthropic-совместимыми API: DeepSeek, Kimi, MiMo, GLM/Z.AI
- Ежедневные рекомендации arXiv через GitHub Actions и визуализация графа знаний через веб-интерфейс или Obsidian

## Подробнее
OmegaWiki (skyllwt/OmegaWiki, 669+ звёзд, лицензия MIT) переосмысливает подход к инструментам исследований с помощью ИИ. Вместо того чтобы рассматривать корпус статей как плоское векторное хранилище для RAG, платформа строит структурированный граф знаний, где каждая сущность имеет тип, а каждая связь — семантическую метку. Система понимает, что одна статья *builds_on* (строится на) другой, или что новый метод *challenges* (бросает вызов) существующему — отношения, которые RAG просто не способен уловить.

Платформа предоставляет 24 команды Claude Code, организованные по фазам исследования. Команда `/discover` сканирует конкретные конференции (ICLR, NeurIPS, ICML) на предмет релевантных работ. Граф знаний хранится в форматах `edges.jsonl` и `citations.jsonl`, что обеспечивает как программные запросы, так и визуальное исследование. Методы являются сущностями первого класса, что позволяет отслеживать эволюцию техник между статьями.

Ключевой принцип дизайна — память антиповторения: неудачные эксперименты записываются в граф, чтобы система (и исследователь) избегали повторения тупиковых путей. Функция перекрёстной состязательной рецензии позволяет направить черновик другой LLM через любой OpenAI-совместимый API, обеспечивая независимую критическую перспективу перед подачей. Проект разработан командой лаборатории DAIR Пекинского университета: Weitong Qian, Beicheng Xu, Zhongao Xie, Bowen Fan, Guozheng Tang, Xinzhe Wu, Jiale Chen и Mingtian Yang.

## Примечательные цитаты
> "knowledge compiles once and compounds; RAG re-derives from scratch every query" — философия дизайна OmegaWiki

> "Failed experiments become anti-repetition memory" — README OmegaWiki

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[llm-wiki-ecosystem]] ([LLM Wiki Ecosystem: Implementations and Variants](../tools/llm-wiki-ecosystem.md))
- [[mathwiki-llm-research-automation]] ([LLM-Powered Math Research: Ideas to Steal for Your MathWiki](../research/mathwiki-llm-research-automation.md))
