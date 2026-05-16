---
title: "PARNESS: End-to-End Automated Scientific Research with Cross-Run Knowledge"
title_ru: "PARNESS: сквозная автоматизация научных исследований с накоплением знаний"
category: tools
tags: [autonomous-research, knowledge-graph, dag, llm, scientific-research, claude-code, opencode, pdf-parsing]
date: 2026-05-06
updated: 2026-05-17
sources:
  - https://arxiv.org/abs/2605.05258
authors: [Yuchen Wang, Zhongzhi Luan]
venue: "arXiv:2605.05258 (May 2026)"
---

## Summary
PARNESS is an open-source framework for end-to-end autonomous scientific research that solves the core failure of all prior AI-scientist systems — knowledge does not persist across runs — via a knowledge-graph index with scenario-typed retrieval, a DAG workflow kernel editable as YAML, full-text PDF and code-repository indexing, and native integration with Claude Code, Cursor, Copilot, and OpenCode.

## Key Ideas
- The root cause of prior system failures (AI-Scientist, PaperOrchestra, AutoSOTA): all fix their control-flow shape at the framework level (linear pipeline, state machine, single-agent loop) — PARNESS decouples scheduling from domain semantics via a thin DAG kernel with a four-field Agent contract, making any discipline's loop expressible as user-editable YAML.
- Knowledge-graph index with **scenario-typed retrieval**: surfaces knowledge slices classified as *similar*, *contradictory*, *cross-domain*, or *counter-intuitive* — the first system to make contradiction a first-class query type, not an error state.
- Full-text PDF and code-repository indexing: paper bodies, figures, and tables are indexed as typed objects (not just abstracts); the paper-to-code link is maintained as a first-class relationship.
- Cross-run knowledge accumulation: the knowledge graph persists across sessions — each run adds to it rather than starting from scratch. This is the most direct academic parallel to Karpathy's "compile, don't retrieve" wiki pattern.
- Native coding-agent integration: any module can be added or replaced by Claude Code, Cursor, GitHub Copilot, or OpenCode — the framework is explicitly designed as a coding-agent extension, not a standalone tool.

## Details
PARNESS identifies five root causes why prior autonomous research systems fail at scale: (1) workflows are dynamic and discipline-specific — lab work, surveys, simulations, and theory all loop differently; (2) ideation is bounded by LLM context, and cross-domain ideation needs knowledge no single context can hold; (3) summary-only views miss the paper body, yet full-text access is uneven; (4) the paper-to-code link — often the only complete specification of an experimental scheme — is neglected; (5) no tool persists cross-run knowledge retrievably into a finite LLM context.

The DAG kernel addresses (1): a four-field Agent contract (name, inputs, outputs, compute) decouples the agent's domain logic from the scheduler. Any research workflow becomes a YAML-editable graph of such agents, allowing domain experts to modify pipeline topology without touching code.

The scenario-typed retrieval index addresses (2) and (5). The knowledge graph does not just store facts — it classifies retrieval scenarios. When a new paper is being analysed, the system can retrieve:
- *Similar* prior work (standard similarity search)
- *Contradictory* findings (surface disagreements proactively)
- *Cross-domain* analogies (ideas from other fields that share structural similarity)
- *Counter-intuitive* results (findings that violate the current model's priors)

This four-way classification is the most sophisticated retrieval taxonomy in any open-source research system to date.

Full-text and code indexing addresses (3) and (4): figures, tables, and methodology sections are indexed as typed objects, not just abstract text. The code repository linked from a paper is indexed as the canonical specification of the experimental scheme.

**Relation to the personal wiki pattern:** PARNESS is the closest academic system to Karpathy's LLM Wiki concept. It independently converged on the same insight — persistent, curated knowledge is more valuable than re-deriving knowledge per session — and built production infrastructure around it. The scenario-typed retrieval is a concrete upgrade path for the wiki's `/wiki-search`, which currently only does flat text matching.

## Related Entries
- [[llm-wiki-academic-applications]]
- [[llm-wiki-pattern]]
- [[llm4sr-survey]]
- [[karma-knowledge-graph-enrichment]]
- [[lightrag-graph-rag]]

---
<!-- RU -->

## Краткое описание
PARNESS — open-source фреймворк для сквозной автономной научной работы, решающий ключевую проблему всех предыдущих AI-scientist систем — знания не накапливаются между запусками — через граф знаний со сценарно-типизированным поиском, DAG-ядро с YAML-редактируемыми рабочими процессами, полнотекстовую индексацию PDF и репозиториев, и нативную интеграцию с Claude Code, Cursor, Copilot и OpenCode.

## Ключевые идеи
- Корневая причина отказов предыдущих систем (AI-Scientist, PaperOrchestra, AutoSOTA): все они фиксируют форму потока управления на уровне фреймворка. PARNESS отделяет планирование от доменной семантики через тонкое DAG-ядро с четырёхпольным агентным контрактом — любой исследовательский цикл выражается в пользовательски редактируемом YAML.
- Граф знаний со **сценарно-типизированным поиском**: выдаёт срезы знаний, классифицированные как *похожие*, *противоречащие*, *кросс-доменные* или *контринтуитивные* — первая система, где противоречие является первоклассным типом запроса, а не состоянием ошибки.
- Полнотекстовая индексация PDF и репозиториев: тела статей, рисунки и таблицы индексируются как типизированные объекты; связь статья-код поддерживается как первоклассное отношение.
- Накопление знаний между запусками: граф знаний сохраняется между сессиями — каждый запуск добавляет в него, а не начинает с нуля. Это наиболее прямой академический аналог паттерна «компилировать, а не извлекать» Карпатого.
- Нативная интеграция с агентами кодирования: любой модуль можно добавить или заменить через Claude Code, Cursor, GitHub Copilot или OpenCode — фреймворк проектировался как расширение для coding agents.

## Подробнее
PARNESS выявляет пять корневых причин, почему предыдущие автономные исследовательские системы не масштабируются: (1) рабочие процессы динамичны и предметно-специфичны; (2) порождение идей ограничено контекстом LLM; (3) резюме-только представления упускают тело статьи; (4) связь статья-код игнорируется; (5) ни один инструмент не сохраняет кросс-запусковые знания доступно в конечном контексте LLM.

DAG-ядро решает проблему (1): четырёхпольный агентный контракт (имя, входы, выходы, вычисления) отделяет доменную логику агента от планировщика. Любой исследовательский рабочий процесс превращается в YAML-редактируемый граф таких агентов.

Сценарно-типизированный поисковый индекс решает проблемы (2) и (5). При анализе новой статьи система может извлекать: *похожие* предшествующие работы, *противоречащие* результаты (проактивное выявление несогласий), *кросс-доменные* аналогии (идеи из других областей со структурным сходством), *контринтуитивные* результаты (находки, нарушающие текущие приоры модели).

Полнотекстовая индексация решает проблемы (3) и (4): рисунки, таблицы и разделы методологии индексируются как типизированные объекты; репозиторий кода, на который ссылается статья, индексируется как каноническая спецификация экспериментальной схемы.

**Связь с паттерном личной вики:** PARNESS — ближайшая академическая система к концепции LLM Wiki Карпатого. Она независимо пришла к тому же выводу — постоянные, курируемые знания ценнее повторного извлечения в каждой сессии — и построила вокруг этого производственную инфраструктуру.

## Связанные записи
- [[llm-wiki-academic-applications]]
- [[llm-wiki-pattern]]
- [[llm4sr-survey]]
- [[karma-knowledge-graph-enrichment]]
- [[lightrag-graph-rag]]
