---
title: "RAG (Retrieval-Augmented Generation)"
title_ru: "RAG (генерация, дополненная поиском)"
category: concepts
tags: [rag, retrieval, augmented-generation, concepts]
aliases: [RAG, Retrieval Augmented Generation, retrieval-augmented]
confidence: high
updated: 2026-06-14
sources:
  - https://research.ibm.com/blog/retrieval-augmented-generation-RAG
  - https://arxiv.org/abs/2005.11401
---

## Summary

Retrieval-Augmented Generation (RAG) is a technique where a language model's prompt is enriched at query time with relevant passages retrieved from an external knowledge store. Instead of relying solely on knowledge baked into the model's weights, RAG fetches fresh, source-grounded context for each query, improving factual accuracy and reducing hallucination.

## Key Ideas

- **Two-step pattern:** (1) retrieve relevant chunks from a knowledge base (vector DB, BM25 index, graph), then (2) feed them into the LLM prompt to ground the answer in source text.
- **Grounding & freshness:** knowledge can be updated by editing the index rather than retraining the model, so answers stay current without weight changes.
- **Citations:** because each answer is tied to specific retrieved passages, RAG can cite sources and trace claims — useful for trust and auditing.
- **vs. compiled knowledge (LLM Wiki):** RAG re-derives context per query; a compiled/wiki approach synthesizes once and queries the synthesis. RAG scales better to huge, fast-changing corpora; synthesis is better for bounded curated sets.
- **Variants:** naive RAG (vector similarity), graph RAG (entity/relation retrieval), and hybrid BM25+vector approaches.

## Details

RAG addresses a core limitation of LLMs: parametric knowledge is static, expensive to update, and prone to hallucination. By separating the knowledge store (a searchable index) from the reasoning engine (the LLM), RAG lets a single model answer questions over arbitrary, evolving corpora. The retrieval step typically embeds both the query and document chunks into a shared vector space and returns the nearest neighbors, though keyword (BM25) and graph-based retrieval remain competitive or complementary.

The main trade-offs are retrieval quality (the model can only use what the retriever finds) and latency/cost of the extra retrieval step. Advanced variants like GraphRAG retrieve over an entity-relationship graph to answer multi-hop questions, while compiled-knowledge approaches (e.g., the LLM Wiki pattern) pre-synthesize sources into a curated knowledge layer to avoid re-deriving answers each time.

## Notable Quotes

> "RAG combines an information retrieval system with a text generation model to ground responses in external knowledge." — Lewis et al., 2020 (RAG paper)

## Related Entries

- [[turbo-graph-rag-memory]] ([Turbo Graph RAG Memory](../tools/turbo-graph-rag-memory.md))
- [[opencoderag-rag-plugin]] ([OpenCodeRAG RAG Plugin](../tools/opencoderag-rag-plugin.md))
- [[lightrag-graph-rag]] ([LightRAG: Graph-Enhanced RAG](../tools/lightrag-graph-rag.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](llm-wiki-pattern.md))

---
<!-- RU -->

## Краткое описание

Retrieval-Augmented Generation (RAG) — техника, при которой промпт языковой модели обогащается в момент запроса релевантными фрагментами, извлечёнными из внешнего хранилища знаний. Вместо того чтобы опираться только на знания, «зашитые» в веса модели, RAG извлекает свежий, обоснованный источниками контекст для каждого запроса, повышая фактическую точность и снижая галлюцинации.

## Ключевые идеи

- **Двухшаговый паттерн:** (1) извлечь релевантные фрагменты из базы знаний (векторная БД, BM25-индекс, граф), затем (2) подать их в промпт LLM, чтобы обосновать ответ текстом источника.
- **Обоснование и свежесть:** знания можно обновлять, редактируя индекс, а не переобучая модель — ответы остаются актуальными без изменения весов.
- **Цитирование:** поскольку каждый ответ привязан к конкретным извлечённым фрагментам, RAG может цитировать источники и отслеживать утверждения — полезно для доверия и аудита.
- **RAG vs. скомпилированные знания (LLM Wiki):** RAG заново извлекает контекст на каждый запрос; подход compile/wiki синтезирует знания один раз и запрашивает уже синтез. RAG лучше масштабируется на огромные, быстро меняющиеся корпуса; синтез — на ограниченные кураторские наборы.
- **Варианты:** наивный RAG (векторная близость), GraphRAG (извлечение по сущностям/отношениям) и гибридные подходы BM25+вектор.

## Подробнее

RAG решает фундаментальное ограничение LLM: параметрические знания статичны, дороги в обновлении и склонны к галлюцинациям. Разделяя хранилище знаний (поисковый индекс) и движок рассуждений (LLM), RAG позволяет одной модели отвечать на вопросы по произвольным, эволюционирующим корпусам. Шаг поиска обычно embed-ит и запрос, и фрагменты документов в общее векторное пространство и возвращает ближайших соседей, хотя ключевое (BM25) и графовое извлечение остаются конкурентоспособными или дополнительными.

Главные компромиссы — качество поиска (модель может использовать лишь то, что нашёл retriever) и задержка/стоимость дополнительного шага поиска. Продвинутые варианты вроде GraphRAG извлекают по графу сущность-отношение для ответа на multi-hop-вопросы, тогда как подходы со скомпилированными знаниями (например, паттерн LLM Wiki) заранее синтезируют источники в курируемый слой знаний, чтобы не выводить ответы заново каждый раз.

## Примечательные цитаты

> «RAG объединяет систему информационного поиска с моделью генерации текста, чтобы обосновывать ответы внешними знаниями.» — Lewis et al., 2020 (статья о RAG)

## Связанные записи

- [[turbo-graph-rag-memory]] ([Turbo Graph RAG Memory](../tools/turbo-graph-rag-memory.md))
- [[opencoderag-rag-plugin]] ([OpenCodeRAG RAG Plugin](../tools/opencoderag-rag-plugin.md))
- [[lightrag-graph-rag]] ([LightRAG: Graph-Enhanced RAG](../tools/lightrag-graph-rag.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](llm-wiki-pattern.md))
