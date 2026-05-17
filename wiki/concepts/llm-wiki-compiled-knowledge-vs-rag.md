---
title: "LLM Wiki vs RAG: Compiled Knowledge Architecture"
title_ru: "LLM Wiki vs RAG: архитектура скомпилированных знаний"
category: concepts
tags: [llm-wiki, rag, compiled-knowledge, karpathy, hybrid-architecture, knowledge-base, retrieval]
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://particula.tech/blog/karpathy-llm-wiki-compiled-knowledge-vs-rag
  - https://pasqualepillitteri.it/en/news/1496/rag-llm-wiki-agentic-search-differences-costs-2026
---

## Summary

Two independent analyses comparing LLM Wiki (compiled knowledge) vs RAG (interpreted retrieval) vs Agentic Search. Particula presents the compiler analogy: RAG re-derives knowledge per query (interpreted), while LLM Wiki pre-compiles sources into cross-referenced pages (compiled). Pasquale Pillitteri adds dollar figures: at 50M monthly queries, enterprise RAG costs ~$43,750/month in extended context alone, while 75% of enterprise apps will use hybrid architectures by end of 2026.

## Key Ideas
- **Compiler analogy (Particula):** RAG = interpreted execution (re-parse source code every query). LLM Wiki = compiled execution (pre-compiled artifacts, fast queries, cross-source analysis at ingest time)
- **Three-layer architecture:** raw/ (immutable sources) → wiki/ (compiled markdown pages + index.md + log.md) → CLAUDE.md (schema/operational rules)
- **When LLM Wiki beats RAG:** Stable knowledge base (<400K words / ~100 articles), need for answer consistency, traceability requirements (healthcare, legal, financial), personal knowledge management
- **When RAG wins:** High-velocity corpora (>100K documents), real-time data, frequent updates
- **Hybrid is the answer (both sources):** Compiled wiki for core stable knowledge + RAG for volatile data. 75% of enterprise apps will use hybrid by end of 2026
- **Three core operations:** Ingest (compile once, ~$0.15-0.30 per source), Query (navigate wiki via index — no vector search), Lint (maintenance — contradiction detection, orphan pages, stale info)
- **Cost comparison (Pasquale):** At 50M queries/month, RAG extended context overhead alone = ~$43,750/month. LLM Wiki pays compilation cost once, queries are cheap navigation
- **Agentic Search as third paradigm:** LLM as autonomous researcher — plans searches, iterates, evaluates quality, uses tools. Not mutually exclusive with RAG or LLM Wiki
- **RAG fundamental limitations:** Chunking breaks context, vector search confuses similar documents, hallucinations persist on top of retrieved material, costs grow linearly with query volume

## Details

Particula's analysis is the most technically precise comparison available. The compiler analogy maps directly: just as a compiler transforms source code into optimized machine code ahead of runtime, the LLM Wiki transforms raw sources into structured, cross-referenced wiki pages ahead of query time. The key insight is that the expensive work (reading, synthesizing, cross-referencing, flagging contradictions) should happen once, not per query.

Pasquale Pillitteri's analysis complements this with concrete cost data and introduces Agentic Search as a third paradigm. The article traces the evolution from RAG (2020) through Agentic Search (2025) to LLM Wiki (2026), noting that 75% of enterprise applications will use hybrid architectures combining all three by end of 2026.

Both sources agree on the scale ceiling: LLM Wiki is optimal for ~20-400K words of stable knowledge, while RAG remains necessary for millions of volatile documents. The hybrid pattern — compiled wiki for core knowledge plus RAG for volatile data — is what most teams should implement.

## Related Entries
- [[llm-wiki-pattern]]
- [[gnosis-mcp-vs-llm-wiki-pattern]]
- [[llm-wiki-implementations-landscape]]
- [[rags-evolution-agentic-ai]]
- [[rag-explained-embeddings-vector-db]]

---
<!-- RU -->

## Краткое описание

Два независимых анализа, сравнивающих LLM Wiki (скомпилированные знания) с RAG (поиск с извлечением) и Agentic Search. Particula представляет аналогию компилятора: RAG повторно извлекает знания при каждом запросе (интерпретация), а LLM Wiki предкомпилирует источники в структурированные страницы (компиляция). Pasquale Pillitteri добавляет конкретные цифры затрат: при 50 млн запросов в месяц RAG стоит ~$43,750/месяц только на расширенный контекст, тогда как 75% корпоративных приложений будут использовать гибридные архитектуры к концу 2026 года.

## Ключевые идеи
- **Аналогия компилятора:** RAG = интерпретируемое выполнение (повторный разбор при каждом запросе). LLM Wiki = скомпилированное выполнение (предкомпилированные артефакты)
- **Трёхуровневая архитектура:** raw/ (неизменные источники) → wiki/ (скомпилированные markdown-страницы) → CLAUDE.md (схема)
- **Когда LLM Wiki побеждает RAG:** Стабильная база знаний (<400K слов), потребность в согласованности ответов, требования трассировки
- **Когда RAG выигрывает:** Высокоскоростные корпуса (>100K документов), данные реального времени
- **Гибрид — ответ:** Скомпилированная вики для стабильных знаний + RAG для изменчивых данных. 75% enterprise приложений будут гибридными к концу 2026
- **Три основные операции:** Ingest (компиляция однажды, ~$0.15-0.30 за источник), Query (навигация по вики без векторного поиска), Lint (обслуживание — обнаружение противоречий, потерянные страницы)
- **Сравнение затрат:** При 50 млн запросов/месяц RAG = ~$43,750/месяц на расширенный контекст. LLM Wiki платит за компиляцию один раз
- **Agentic Search как третья парадигма:** LLM как автономный исследователь — планирует поиск, итерирует, оценивает качество

## Связанные записи
- [[llm-wiki-pattern]]
- [[gnosis-mcp-vs-llm-wiki-pattern]]
- [[llm-wiki-implementations-landscape]]
- [[rags-evolution-agentic-ai]]
- [[rag-explained-embeddings-vector-db]]
