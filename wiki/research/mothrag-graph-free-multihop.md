---
title: "MOTHRAG — Graph-Free Multi-Hop Retrieval via Query-Time Orchestration"
title_ru: "MOTHRAG — многоскачковый поиск без графа через оркестровку в момент запроса"
category: research
tags: [rag, multi-hop, retrieval, hotpotqa, knowledge-graph, graph-free]
aliases: [MOTHRAG, Moth-Retrieval, moth rag]
confidence: medium
updated: 2026-07-01
sources:
  - https://www.reddit.com/r/MachineLearning/comments/1ukotww/p_mothretrieval_graphfree_multihop_retrieval_via/
---

## Summary
MOTHRAG is an open-sourced multi-hop RAG framework that drops the offline knowledge graph entirely. Instead it uses a graph-free dense index plus query-time orchestration to beat GraphRAG, HippoRAG, and RAPTOR on standard multi-hop benchmarks — while avoiding the brutal re-indexing cost that graph-based systems pay whenever the corpus changes.

## Key Ideas
- **Problem:** the most accurate multi-hop RAG systems (GraphRAG, HippoRAG, RAPTOR) lean on a knowledge graph built offline; every corpus update forces a heavy LLM re-index pass.
- **Approach:** graph-free dense index with query-time orchestration; every component behind a commodity API, no GPU required.
- **Reported results** (Accuracy / F1):
  - HotpotQA: MOTHRAG 78.1 vs GraphRAG 68.6 / HippoRAG 75.5 / RAPTOR 69.5
  - 2WikiMultiHopQA: 76.3 vs 58.6 / 71.0 / 52.1
  - (MuSiQue figures reported in source.)
- **Trade target:** corpora that update frequently (prices, filings, support tickets, news) where graph re-indexing is prohibitively expensive.

## Details
Multi-hop QA requires stitching facts across documents. Graph-based systems pre-compute that stitch offline, which is accurate but brittle under changing data. MOTHRAG defers the orchestration to query time, trading a little per-query compute for eliminating the offline indexing pipeline — a favorable trade for live, mutable corpora.

## Related Entries
- [[lightrag-graph-rag]] ([LightRAG Graph RAG](../tools/lightrag-graph-rag.md))
- [[graphify-llm-wiki]] ([Graphify LLM Wiki](../tools/graphify-llm-wiki.md))
- [[turbo-graph-rag-memory]] ([Turbo Graph RAG Memory](../tools/turbo-graph-rag-memory.md))

---
<!-- RU -->

## Краткое описание
MOTHRAG — открытый фреймворк multi-hop RAG, полностью отказавшийся от оффлайн-графа знаний. Вместо него используется плотный индекс без графа и оркестровка в момент запроса, что обходит GraphRAG, HippoRAG и RAPTOR на стандартных бенчмарках — и избегает дорогого реиндексирования, которым платят графовые системы при каждом изменении корпуса.

## Ключевые идеи
- **Проблема:** самые точные multi-hop RAG-системы опираются на оффлайн-граф; каждое обновление корпуса требует тяжёлого LLM-реиндекса.
- **Подход:** плотный индекс без графа + оркестровка во время запроса; все компоненты за commodity-API, GPU не нужен.
- **Заявленные результаты** (Accuracy / F1):
  - HotpotQA: MOTHRAG 78.1 против GraphRAG 68.6 / HippoRAG 75.5 / RAPTOR 69.5
  - 2WikiMultiHopQA: 76.3 против 58.6 / 71.0 / 52.1
- **Целевой сценарий:** часто обновляемые корпуса (цены, отчётность, тикеты, новости), где реиндекс графа неприемлемо дорог.

## Подробнее
Multi-hop QA требует сшивки фактов между документами. Графовые системы предвычисляют её оффлайн — точно, но хрупко при меняющихся данных. MOTHRAG переносит оркестровку на время запроса, обменивая немного per-query вычислений на устранение оффлайн-индексации — выгодный обмен для живых, изменяемых корпусов.

## Связанные записи
- [[lightrag-graph-rag]] ([LightRAG Graph RAG](../tools/lightrag-graph-rag.md))
- [[graphify-llm-wiki]] ([Graphify LLM Wiki](../tools/graphify-llm-wiki.md))
- [[turbo-graph-rag-memory]] ([Turbo Graph RAG Memory](../tools/turbo-graph-rag-memory.md))
