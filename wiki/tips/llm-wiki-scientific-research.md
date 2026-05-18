---
title: "LLM Wiki for Scientific Research and Academic Writing"
title_ru: "LLM Wiki в научных исследованиях и академическом письме"
category: tips
tags: [llm-wiki, academic, research, knowledge-graph, arxiv, grobid, graphrag, citation, obsidian, spaced-repetition, mathwiki]
updated: 2026-05-16
sources:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - https://github.com/skyllwt/OmegaWiki
  - https://arxiv.org/abs/2501.04306
  - https://arxiv.org/abs/2503.08549
  - https://arxiv.org/abs/2505.13406
  - https://arxiv.org/abs/2404.10774
  - https://grobid.readthedocs.io/en/latest/Introduction/
  - https://lightrag.github.io/
---

## Summary
The LLM Wiki pattern — pre-compiling knowledge from raw sources into a persistent, LLM-maintained markdown wiki — is especially high-value in scientific research, where synthesizing hundreds of papers is normally months of human work. Applied to math and science, it requires specialized tools for PDF parsing, formula-aware search, citation chaining, and mathematical accuracy verification.

## Key Ideas
- **Compounding advantage over RAG:** A wiki that grows with every new paper creates cumulative synthesis — contradictions are logged, gaps are tracked, cross-paper patterns emerge over time. RAG re-derives from scratch on every query and never accumulates insight.
- **OmegaWiki is the state-of-the-art academic implementation:** Built by DAIR Lab (Peking University), it covers the full research lifecycle — paper ingestion → concept extraction → idea generation → experiment tracking → survey generation → paper draft → submission rebuttal — using 24 typed Claude Code skills and 9 entity types with semantic edge labels (`builds_on`, `improves_on`, `challenges`, `same_problem_as`, `contradicts`).
- **GROBID is the right PDF parser:** Production-used by Semantic Scholar, ResearchGate, CERN, and Internet Archive Scholar. Achieves >90% accuracy on metadata + structure extraction, processes PDFs in 2–5 sec/page, outputs structured TEI XML. Prefers arXiv HTML/LaTeX source when available — formula recovery is far superior to PDF.
- **LightRAG over the wiki corpus replaces keyword search:** Builds a graph from your own wiki entries (entities + relations extracted by LLM), enabling dual-level retrieval: specific entity queries AND thematic/conceptual queries. 10× token reduction vs Microsoft GraphRAG; 65–80% lower ingestion cost.
- **Math semantic search requires formula-aware embeddings:** Standard embeddings miss that `∫f(x)dx = F(b)-F(a)` and "fundamental theorem of calculus" are equivalent. Use SPECTER2 (from Semantic Scholar API, free) for paper-level embeddings + `latex2sympy` normalization for formula fields + hybrid keyword+vector search.
- **MiniCheck for factuality verification:** `Bespoke-MiniCheck-7B` (HuggingFace) fact-checks each wiki claim against its source document at 400× lower cost than GPT-4 for equivalent quality. Claims scoring < 0.7 are flagged for human review. Critical for math content where one wrong condition changes the theorem.
- **Automated paper discovery stack:** Semantic Scholar Graph API (225M+ papers, SPECTER2 embeddings, free), OpenAlex (271M works, fully open), arXiv OAI-PMH RSS (daily per-category feed). The `arxiv-mcp-server` MCP server exposes these directly to Claude Code sessions via `search_papers`, `watch_topic`, `citation_graph` tools.
- **Citation snowballing for auto-linking:** For each new paper, fetch its full reference list via Semantic Scholar API, check which DOIs/arXiv IDs already exist in `.state/processed_urls.json`, and auto-insert `[[slug]]` backlinks. Forward snowballing (papers citing your seed corpus) drives automated discovery of new relevant work.
- **Spaced repetition from wiki entries:** Obsidian's `obsidian-spaced-repetition` + `Flashcards LLM` plugin auto-generate FSRS flashcards from `## Key Ideas` sections. A `PostToolUse` hook in Claude Code can generate the `## Flashcards` section on every new entry write.

## Details

### The Academic Stack

The practitioner consensus (from PhD-level users) stacks: **arXiv/Semantic Scholar** (discovery) → **GROBID** (structured extraction from PDFs) → **Zotero + ZotLit** (citation management synced into Obsidian) → **LLM Wiki** (distillation and synthesis) → **AutoSurvey/LitLLM** (related work generation) → writing tools. The LLM Wiki sits at the center of this stack as the persistent synthesis layer — the only component that accumulates knowledge across time.

### Knowledge Extraction from Math Papers

The AutoMathKG pipeline (2025) defines best practice for LaTeX-heavy papers: rule-based regex extraction of typed LaTeX environments (`\begin{theorem}`, `\begin{definition}`, `\begin{lemma}`, `\begin{proof}`, `\begin{algorithm}`) → LLM augmentation with 12 in-context-learning templates to fill attributes (prerequisites, field, related concepts) → 9 typed relation labels between nodes (`premise`, `assumption`, `lemma`, `definition`, `conclusion`, `generalization`, `specialization`, `contradiction`, `exemplifies`). This produces a per-paper knowledge graph that can be merged into a domain-wide graph.

For mathematical wiki entries specifically, each entry should carry explicit fields for:
- **Conditions/hypotheses** (what must hold for the theorem to apply)
- **Related concepts** (prerequisites from other entries)
- **Counterexamples** (boundary cases, when the claim fails)
- **Confidence** (high / medium / low, with reason for low-confidence entries)

### Multi-Agent Verification for Math Accuracy

The MALT framework (ICML 2025) demonstrates that a planner–extractor–verifier loop catches 40–60% of errors introduced during extraction. For a wiki: the extractor agent reads the source and writes the entry; a separate verifier agent receives both the source and the entry and answers: "Does each claim in this entry follow from the source? Are the conditions/hypotheses stated correctly? Is the mathematical notation consistent?" External grounding (the source paper as context) is critical — LLMs cannot self-correct from memory alone (ICLR 2024 result).

### Tools Compared to PaperQA2 / WikiCrow

FutureHouse's WikiCrow (closest prior art at scale) generated Wikipedia articles for all 20,000 human genes from 1 million papers — expert-rated more accurate than actual Wikipedia (~9% error rate). But WikiCrow is query-time RAG, not a persistent wiki. ContraCrow found an average of 2.34 contradicted statements per biology paper. A true LLM Wiki differs by being persistent, owned locally, customizable via schema, and accumulating synthesis rather than regenerating it.

### What a Math/Science Wiki Should Add Beyond the Base Pattern

1. **Typed atomic notes** (theorem / definition / lemma / algorithm / conjecture) with explicit prerequisite links — following the Zettelkasten graph structure of `Yaro2709/MathWiki`.
2. **`qa_status` front-matter field** (`unreviewed` / `auto-verified` / `human-reviewed`) populated by MiniCheck score.
3. **LaTeX environment extraction** as a pre-processing step before LLM summarization, not after.
4. **FSRS flashcard section** auto-generated in every entry for spaced repetition integration.
5. **`sources/papers/` directory** (parallel to `sources/transcripts/`) for GROBID-processed TEI XML.
6. **`arxiv-mcp-server` + `semantic-scholar-mcp`** installed globally for Claude Code to call during wiki sessions.

## Notable Quotes
> "Synthesizing 200 papers into a coherent understanding is a massive human effort. Literature reviews take months. The wiki pattern provides a continuously updating meta-review where the LLM reads every new paper, updates the synthesis, and flags contradictions." — Andrej Karpathy, LLM Wiki Gist

> "LLMs generate more novel but slightly less valid hypotheses than human researchers." — LLM4SR Survey, arXiv:2501.04306

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[karpathy-claude-code-guidelines]] ([Karpathy-Inspired Claude Code Guidelines](../tips/karpathy-claude-code-guidelines.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[mathwiki-llm-research-automation]] ([LLM-Powered Math Research: Ideas to Steal for Your MathWiki](../research/mathwiki-llm-research-automation.md))
- [[mathwiki-smith-maps-research]] ([AntonIliashenko/MathWiki: Smith Map Research Wiki](../research/mathwiki-smith-maps-research.md))
---
<!-- RU -->

## Краткое описание
Паттерн LLM Wiki — непрерывная компиляция знаний из сырых источников в персистентную, поддерживаемую LLM вики — особенно ценен в научных исследованиях, где синтез сотен статей обычно занимает месяцы. Применительно к математике и естественным наукам он требует специализированных инструментов: парсинга PDF, формульного поиска, анализа цитирований и верификации математической точности.

## Ключевые идеи
- **Накопительное преимущество перед RAG:** Вики, растущая с каждой новой статьёй, накапливает синтез — противоречия фиксируются, пробелы отслеживаются, межстатейные паттерны проявляются со временем. RAG каждый раз выводит знание заново и ничего не накапливает.
- **OmegaWiki — лучшая академическая реализация:** Создана в DAIR Lab (Пекинский университет), покрывает полный исследовательский цикл — загрузка статей → извлечение понятий → генерация идей → отслеживание экспериментов → написание обзоров → черновик статьи → ответ рецензентам — с помощью 24 типизированных навыков Claude Code и 9 типов сущностей с семантическими метками рёбер (`builds_on`, `improves_on`, `challenges`, `contradicts`).
- **GROBID — лучший парсер PDF:** Используется в Semantic Scholar, ResearchGate, CERN и Internet Archive Scholar. Точность > 90% по метаданным и структуре, 2–5 сек/страница, вывод в TEI XML. При наличии исходников LaTeX на arXiv предпочтительнее HTML/LaTeX — качество восстановления формул несравнимо выше.
- **LightRAG поверх корпуса вики заменяет ключевой поиск:** Строит граф из ваших записей (LLM извлекает сущности и связи), обеспечивая двухуровневый поиск: конкретные сущности и тематические/концептуальные запросы. В 10 раз меньше токенов, чем у Microsoft GraphRAG; стоимость индексации ниже на 65–80%.
- **Формульный семантический поиск требует специальных эмбеддингов:** Стандартные эмбеддинги не улавливают, что `∫f(x)dx = F(b)-F(a)` и «основная теорема математического анализа» — одно и то же. Используйте SPECTER2 (от Semantic Scholar API, бесплатно) для уровня статей + нормализацию через `latex2sympy` + гибридный поиск.
- **MiniCheck для верификации достоверности:** `Bespoke-MiniCheck-7B` (HuggingFace) проверяет каждое утверждение вики по исходному документу в 400 раз дешевле GPT-4 при аналогичном качестве. Утверждения с оценкой < 0,7 помечаются для проверки человеком.
- **Стек автоматического обнаружения статей:** Semantic Scholar API (225M+ статей, эмбеддинги SPECTER2, бесплатно), OpenAlex (271M работ, полностью открытый), arXiv OAI-PMH RSS (ежедневная лента по категориям). MCP-сервер `arxiv-mcp-server` предоставляет эти инструменты прямо в сессии Claude Code через `search_papers`, `watch_topic`, `citation_graph`.
- **«Снежный ком» цитирований для автоматической перелинковки:** Для каждой новой статьи получаем полный список ссылок через Semantic Scholar API, проверяем, какие DOI/arXiv ID уже есть в `.state/processed_urls.json`, и автоматически вставляем обратные ссылки `[[slug]]`.
- **Интервальные повторения из записей вики:** Плагины Obsidian `obsidian-spaced-repetition` + `Flashcards LLM` автоматически генерируют FSRS-карточки из разделов `## Ключевые идеи`. Хук `PostToolUse` в Claude Code может создавать раздел `## Flashcards` при каждой записи новой статьи.

## Подробнее

### Академический стек

Типовой практический стек (по опыту PhD-исследователей): **arXiv/Semantic Scholar** (поиск) → **GROBID** (структурное извлечение из PDF) → **Zotero + ZotLit** (управление цитированиями, синхронизация с Obsidian) → **LLM Wiki** (дистилляция и синтез) → **AutoSurvey/LitLLM** (генерация раздела «Related Work») → инструменты для написания. LLM Wiki находится в центре как персистентный слой синтеза — единственный компонент, накапливающий знания во времени.

### Извлечение знаний из математических статей

Пайплайн AutoMathKG (2025): регулярное извлечение типизированных LaTeX-окружений (`\begin{theorem}`, `\begin{definition}`, `\begin{lemma}`, `\begin{proof}`, `\begin{algorithm}`) → обогащение LLM с помощью 12 шаблонов in-context-learning → разметка 9 типами рёбер между узлами (`premise`, `assumption`, `definition`, `conclusion`, `generalization`, `specialization`, `contradiction`). Результат — граф знаний отдельной статьи, объединяемый в общедоменный граф.

### Многоагентная верификация математической точности

Фреймворк MALT (ICML 2025): цикл «планировщик → извлекатель → верификатор» ловит 40–60% ошибок, допущенных при извлечении. Для вики: агент-извлекатель читает источник и пишет запись; отдельный агент-верификатор получает и источник, и запись, отвечая: «Следует ли каждое утверждение из источника? Корректно ли сформулированы условия?». Внешняя контекстная привязка обязательна — LLM не способны самостоятельно исправлять ошибки без грунтового документа (результат ICLR 2024).

### Что добавить к базовому паттерну для математической вики

1. **Типизированные атомарные записи** (теорема / определение / лемма / алгоритм / гипотеза) с явными ссылками на пресуппозиции.
2. **Поле `qa_status`** в метаданных (`unreviewed` / `auto-verified` / `human-reviewed`), заполняемое по оценке MiniCheck.
3. **Извлечение LaTeX-окружений** как препроцессинговый шаг перед суммаризацией LLM.
4. **Раздел FSRS-карточек** в каждой записи для интеграции с интервальными повторениями.
5. **Директория `sources/papers/`** (параллельно `sources/transcripts/`) для TEI XML от GROBID.
6. **`arxiv-mcp-server` + `semantic-scholar-mcp`** в глобальной конфигурации Claude Code.

## Примечательные цитаты
> «Синтез 200 статей в связное понимание — это огромный человеческий труд. Обзоры литературы занимают месяцы. Паттерн вики обеспечивает непрерывно обновляемый мета-обзор: LLM читает каждую новую статью, обновляет синтез и фиксирует противоречия.» — Андрей Карпати, LLM Wiki Gist

> «LLM генерируют более новаторские, но немного менее валидные гипотезы, чем исследователи-люди.» — Обзор LLM4SR, arXiv:2501.04306

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[karpathy-claude-code-guidelines]] ([Karpathy-Inspired Claude Code Guidelines](../tips/karpathy-claude-code-guidelines.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[mathwiki-llm-research-automation]] ([LLM-Powered Math Research: Ideas to Steal for Your MathWiki](../research/mathwiki-llm-research-automation.md))
- [[mathwiki-smith-maps-research]] ([AntonIliashenko/MathWiki: Smith Map Research Wiki](../research/mathwiki-smith-maps-research.md))
