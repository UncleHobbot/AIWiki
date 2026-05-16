---
title: "LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap"
title_ru: "LLM-вики в академических исследованиях: обзор и дорожная карта"
category: concepts
tags: [llm-wiki, knowledge-management, rag, knowledge-graph, survey, academic, personal-wiki, karpathy]
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://arxiv.org/abs/2502.06472
  - https://arxiv.org/abs/2508.14317
  - https://arxiv.org/abs/2410.05779
  - https://arxiv.org/abs/2605.05258
  - https://arxiv.org/abs/2501.04306
---

## Summary
The academic landscape around LLM-maintained knowledge bases splits into two clusters — automated knowledge-graph construction from literature, and end-to-end autonomous research assistants — and both converge on the same unsolved problem: knowledge that does not persist across sessions. Personal wikis built on Karpathy's pattern are already ahead of the research frontier on bilinguality, human-readable storage, and source-tier awareness; the remaining gaps are cross-entry relational reasoning, contradiction detection, and digest coherence.

## Key Ideas
- Academic systems (KARMA, PARNESS, LightRAG) repeatedly fail because they do not accumulate knowledge across runs — the core problem Karpathy's "compile, don't retrieve" pattern solves by design.
- PARNESS (2026) explicitly classifies retrieval scenarios as *similar*, *contradictory*, *cross-domain*, and *counter-intuitive* — treating contradiction as a first-class query type, not an error.
- LightRAG's dual-level graph (entity-level + concept-level) over existing text enables relational queries ("which tools use RAG?") that flat full-text search misses, without requiring a vector database.
- SurveyGen-I's cross-section terminology memory — injecting a "do not re-explain these terms" store into each writing pass — is a direct fix for the digest coherence problem.
- The LLM4SR taxonomy defines the natural evolution path: Level 1 = LLM as Tool (record what sources say); Level 2 = LLM as Analyst (evaluate new content against existing knowledge, flag gaps and contradictions).

## Details

### The Two Academic Clusters

Research in LLM-powered knowledge management as of mid-2026 organises into two tracks.

**Track 1 — Knowledge graph construction.** Systems like KARMA (NeurIPS 2025) and LightRAG (EMNLP 2025) focus on extracting structured knowledge from large corpora. KARMA deploys nine collaborative agents — entity discovery, relation extraction, schema alignment, conflict resolution — across unstructured scientific documents, achieving 83.1% correctness on 38,230 extracted entities and reducing conflicting edges by 18.6% via multi-layer consensus. LightRAG embeds a dual-level graph (entity-level facts + concept-level relationships) directly into the text-indexing layer, with an incremental update algorithm so new documents integrate without reprocessing the full corpus.

**Track 2 — Autonomous research assistants.** Systems like PARNESS (May 2026) and SurveyGen-I (IJCNLP-AIJLP 2025) attempt to automate the full research lifecycle. PARNESS — the closest academic counterpart to the Karpathy wiki pattern — builds a cross-run knowledge graph indexed by retrieval scenario (similar / contradictory / cross-domain / counter-intuitive) and exposes it to Claude Code and OpenCode as the coding agent. SurveyGen-I generates long-form scientific surveys via a coarse-to-fine retrieval loop with a memory mechanism that stores previously written terminology and prevents within-document re-explanation.

Both tracks hit the same wall: without persistent, curated, human-readable storage across sessions, neither can accumulate compounding knowledge. The Karpathy pattern — treating the wiki as compiled knowledge rather than a retrieval index — addresses this directly.

### Where a Personal Wiki Leads the Research

Three dimensions where a well-maintained personal wiki (this one included) is already ahead of what academia has built:

1. **Bilinguality.** No surveyed system tackles multilingual personal knowledge bases. Maintaining entries in both English and Russian doubles the audience for every piece of knowledge without doubling the curation effort.
2. **Human-readable storage.** Academic graph systems store knowledge in opaque databases (Neo4j, SPARQL endpoints). Markdown files are readable without tooling, version-controllable with git, and editable without domain expertise.
3. **Source-tier awareness.** The wiki's four-tier reliability system (primary sources → reputable → community → unknown) is a form of epistemic hygiene that none of the surveyed systems implement.

### Three Open Gaps and How to Close Them

**Gap 1: Contradiction detection.** Contradictions between entries are currently only caught manually. KARMA's approach — extract core claims from each new entry and compare against existing same-category entries — is implementable as `scripts/check_conflicts.py` using structured Claude calls over the existing markdown files. When a conflict is found, auto-populate the existing `## Debate` section in both the new and the conflicting entry.

**Gap 2: Relational retrieval.** The current `/wiki-search` is full-text ripgrep, which misses queries about relationships ("which entries describe tools that use RAG?"). LightRAG's approach applied to the markdown corpus: after each entry is created or updated, run a single relation-extraction Claude call and write the result to `.state/relations/<slug>.json`. Extend `/wiki-search` to query this JSON layer for relational lookups — no vector database or graph DB required.

**Gap 3: Digest coherence across weeks.** The weekly digest currently re-explains concepts (RAG, agents, MCP) that were defined in previous weeks. SurveyGen-I's fix: write `digests/memory.json` after each digest run containing all defined terms and one-line summaries. Inject this as a "do not re-explain" constraint before generating the next week's digest.

## Notable Quotes
> "No existing AI-scientist tool persists knowledge retrievably across runs — they begin from scratch each session." — PARNESS authors, arXiv:2605.05258

> "The bottleneck is no longer generating text. It is knowing what the system already knows." — LLM4SR survey, arXiv:2501.04306

## Related Entries
- [[llm-wiki-pattern]]
- [[llm4sr-survey]]
- [[lightrag-graph-rag]]
- [[karma-knowledge-graph-enrichment]]
- [[surveygen-i-scientific-survey]]
- [[parness-automated-scientific-research]]
- [[omegawiki-research-platform]]
- [[self-guided-self-play]]

---
<!-- RU -->

## Краткое описание
Академический ландшафт в области LLM-поддерживаемых баз знаний разделяется на два кластера — автоматическое построение графов знаний из литературы и автономные системы научных исследований — и оба упираются в одну нерешённую проблему: знания не накапливаются между сессиями. Личные вики на основе паттерна Карпатого уже опережают академический фронтир по трём параметрам: двуязычность, хранение в человекочитаемом формате и учёт достоверности источников. Оставшиеся пробелы — реляционный поиск между записями, выявление противоречий и согласованность дайджестов.

## Ключевые идеи
- Академические системы (KARMA, PARNESS, LightRAG) раз за разом терпят неудачу, потому что не накапливают знания между запусками — именно ту проблему, которую паттерн «компилировать, а не извлекать» решает по своей природе.
- PARNESS (2026) классифицирует сценарии поиска как *похожее*, *противоречащее*, *кросс-доменное* и *контринтуитивное* — рассматривая противоречие как полноценный тип запроса, а не как ошибку.
- Двухуровневый граф LightRAG (уровень сущностей + уровень концепций) поверх существующего текста позволяет задавать реляционные запросы («какие инструменты используют RAG?») без векторной базы данных.
- Механизм памяти терминов SurveyGen-I — внедрение списка «уже объяснённых понятий» в каждый новый проход генерации — непосредственно решает проблему повторяющихся объяснений в еженедельных дайджестах.
- Таксономия LLM4SR определяет естественный путь эволюции: Уровень 1 = LLM как инструмент (фиксировать, что говорят источники); Уровень 2 = LLM как аналитик (оценивать новый контент относительно имеющихся знаний, отмечать пробелы и противоречия).

## Подробнее

### Два академических кластера

Исследования в области LLM-поддерживаемого управления знаниями к середине 2026 года делятся на два направления.

**Направление 1 — Построение графов знаний.** Системы KARMA (NeurIPS 2025) и LightRAG (EMNLP 2025) извлекают структурированные знания из больших корпусов. KARMA задействует девять коллаборативных агентов (обнаружение сущностей, извлечение отношений, выравнивание схем, разрешение конфликтов) и достигает 83,1% корректности на 38 230 извлечённых сущностях, сокращая конфликтующие рёбра на 18,6%. LightRAG встраивает двухуровневый граф (факты на уровне сущностей + отношения на уровне концепций) непосредственно в слой индексации текста с инкрементальным алгоритмом обновления.

**Направление 2 — Автономные исследовательские ассистенты.** PARNESS (май 2026) и SurveyGen-I (IJCNLP-AIJLP 2025) пытаются автоматизировать полный цикл исследований. PARNESS — ближайший академический аналог паттерна Карпатого — строит граф знаний, индексируемый по сценарию поиска (похожее / противоречащее / кросс-доменное / контринтуитивное) и предоставляет его Claude Code и OpenCode. SurveyGen-I генерирует длинные научные обзоры через механизм памяти терминов, предотвращающий повторные объяснения.

Оба направления упираются в одну стену: без постоянного, курируемого, человекочитаемого хранилища знания не накапливаются. Паттерн Карпатого решает это напрямую, рассматривая вики как скомпилированные знания, а не как индекс для поиска.

### Где личная вики опережает исследования

Три параметра, по которым хорошо поддерживаемая личная вики уже опережает академические разработки:

1. **Двуязычность.** Ни одна из рассмотренных систем не решает задачу многоязычных личных баз знаний.
2. **Человекочитаемое хранение.** Академические граф-системы используют непрозрачные БД (Neo4j, SPARQL). Markdown-файлы доступны без инструментария, версионируются через git и редактируются без специальных знаний.
3. **Учёт достоверности источников.** Четырёхуровневая система надёжности вики — это форма эпистемической гигиены, которую ни одна из рассмотренных систем не реализует.

### Три открытых пробела и способы их устранить

**Пробел 1: Выявление противоречий.** Сейчас противоречия между записями замечаются только вручную. Подход KARMA — извлечь ключевые утверждения из каждой новой записи и сравнить с существующими записями той же категории — реализуется как `scripts/check_conflicts.py` через структурированные вызовы Claude. При обнаружении конфликта автоматически заполняется раздел `## Debate` в обеих записях.

**Пробел 2: Реляционный поиск.** Текущий `/wiki-search` основан на полнотекстовом ripgrep и не поддерживает запросы о связях. Применяя подход LightRAG: после создания/обновления записи запускается один вызов Claude для извлечения отношений, результат записывается в `.state/relations/<slug>.json`. `/wiki-search` расширяется для реляционных запросов — без векторной БД.

**Пробел 3: Согласованность дайджестов.** Еженедельный дайджест повторно объясняет понятия из предыдущих недель. Исправление по образцу SurveyGen-I: после каждого дайджеста записывать `digests/memory.json` со всеми определёнными терминами и кратким описанием, вводить этот список как ограничение «не объяснять повторно» при генерации следующего дайджеста.

## Примечательные цитаты
> «Ни один из существующих инструментов AI-учёного не сохраняет знания между запусками доступным образом — каждый раз они начинают с нуля.» — авторы PARNESS, arXiv:2605.05258

> «Узкое место больше не в генерации текста. Оно в том, чтобы знать, что система уже знает.» — обзор LLM4SR, arXiv:2501.04306

## Связанные записи
- [[llm-wiki-pattern]]
- [[llm4sr-survey]]
- [[lightrag-graph-rag]]
- [[karma-knowledge-graph-enrichment]]
- [[surveygen-i-scientific-survey]]
- [[parness-automated-scientific-research]]
- [[omegawiki-research-platform]]
- [[self-guided-self-play]]
