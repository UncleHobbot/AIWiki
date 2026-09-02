---
title: "RAG Is Simpler Than You Think: Full-Text Search Before Embeddings"
title_ru: "RAG проще, чем кажется: полнотекстовый поиск вместо эмбеддингов"
category: concepts
tags: [rag, full-text-search, bm25, embeddings, vector-database, retrieval, architecture, cost-optimization]
aliases: [RAG is simpler, BM25 vs embeddings, full-text RAG, RAG over-engineering]
confidence: high
date: 2026-08-30
updated: 2026-08-30
sources:
  - https://www.lighthousenewsletter.com/p/rag-is-simpler-than-you-think
  - https://news.ycombinator.com/item?id=49445727
---

## Summary
A widely-discussed argument (513 points, 216 comments on Hacker News) that most teams over-engineer RAG by reaching for embeddings and vector databases first, when BM25 full-text search plus LLM query rewriting would serve roughly 60% of systems at zero API cost and sub-10ms latency.

## Key Ideas
- **The 60/25/10/5 split**: the author's claim is that 60% of RAG systems should stop at full-text + query rewriting, 25% need hybrid with on-the-fly or hot/cold embedding, 10% need full pre-embedding, and 5% need custom solutions.
- **BM25 doesn't get deprecated**: embedding models do. When your embedding model is retired you must re-embed the entire corpus — a 10M-document re-index. Full-text indexes have no such model-lifecycle risk.
- **Chunking is a cost you avoid**: full-text search requires no decisions about chunk size, overlap strategy, or semantic vs. fixed-size chunking — a whole class of tuning work that never has to happen.
- **Latency and explainability**: FTS is sub-10ms with transparent matching logic; on-the-fly embedding adds 200–500ms and produces results you cannot easily explain to a user or debug.
- **Proprietary terminology favors FTS**: general-purpose embedding models have not seen your internal product names, error codes, or domain jargon — exact-match search handles these better than semantic similarity.

## Details

### The Decision Hierarchy
The article proposes escalating only when the simpler tier demonstrably fails:

1. **MVP — full-text only**: keyword-heavy queries, proprietary terminology
2. **Query rewriting**: LLM-based query optimization at ~$0.001/query, *before* touching embeddings
3. **Hybrid search**: BM25 candidate generation + embedding reranking
4. **On-the-fly embedding**: for high-churn data (>10% daily updates)
5. **Hot/cold tiers**: pre-embed frequent docs, embed rare ones dynamically
6. **Full pre-embedding**: only at scale (10K+ queries/day) with a stable corpus

### Community Reception
The HN thread largely corroborated the thesis from production experience. A practitioner who built large-scale RAG systems wrote that people "vastly underestimate full text search and vastly overestimate embeddings" — noting FTS is easy, portable, scalable, and the 80/20 rule applies. Another framing that recurred: RAG is classic information retrieval with an LLM doing the querying, and treating vector search as "magic pixie dust" adds cost and complexity without necessarily improving results.

A dissenting thread criticized the article as LLM-generated, which drew agreement about the growing fatigue of reading AI-written text about AI — a meta-critique worth noting when weighing the source.

### Relevance to the LLM Wiki Pattern
This argument reinforces the compiled-knowledge case: if retrieval quality is the bottleneck and embeddings are frequently overkill, then a curated, human-readable wiki that the model reads directly sidesteps the entire retrieval-tuning problem for corpora that fit in context.

## Notable Quotes
> "When your embedding model gets deprecated... you now need to re-embed all 10 million documents." — Lighthouse Newsletter

## Related Entries
- [[rag-retrieval-augmented-generation]] ([RAG: Retrieval-Augmented Generation](../concepts/rag-retrieval-augmented-generation.md))
- [[rag-explained-embeddings-vector-db]] ([RAG Explained: Embeddings and Vector DBs](../concepts/rag-explained-embeddings-vector-db.md))
- [[llm-wiki-compiled-knowledge-vs-rag]] ([LLM Wiki: Compiled Knowledge vs RAG](../concepts/llm-wiki-compiled-knowledge-vs-rag.md))
- [[rags-evolution-agentic-ai]] ([RAG's Evolution to Agentic AI](../concepts/rags-evolution-agentic-ai.md))

---
- [[ai-engineer-notebooks]] ([AI Engineer Notebooks](../tools/ai-engineer-notebooks.md))
- [[shardflow-distributed-inference]] ([Shardflow Distributed Inference](../research/shardflow-distributed-inference.md))
<!-- RU -->

## Краткое описание
Широко обсуждавшийся аргумент (513 баллов, 216 комментариев на Hacker News): большинство команд переусложняют RAG, сразу хватаясь за эмбеддинги и векторные базы, тогда как BM25-полнотекстовый поиск плюс переписывание запроса через LLM закрывает примерно 60% систем при нулевой стоимости API и задержке менее 10 мс.

## Ключевые идеи
- **Разделение 60/25/10/5**: 60% RAG-систем должны остановиться на полнотекстовом поиске с переписыванием запросов, 25% нуждаются в гибриде, 10% — в полном пре-эмбеддинге, 5% — в кастомных решениях.
- **BM25 не устаревает**: модели эмбеддингов устаревают. При выводе модели из эксплуатации приходится переиндексировать весь корпус — переэмбеддинг 10 млн документов.
- **Чанкинг — это издержки, которых можно избежать**: полнотекстовый поиск не требует решений о размере чанков, стратегии перекрытия и семантическом vs фиксированном разбиении.
- **Задержка и объяснимость**: FTS работает менее 10 мс с прозрачной логикой совпадений; эмбеддинг «на лету» добавляет 200–500 мс и даёт результаты, которые трудно объяснить и отладить.
- **Проприетарная терминология в пользу FTS**: универсальные модели эмбеддингов не видели ваших внутренних названий продуктов, кодов ошибок и жаргона предметной области.

## Подробнее

**Иерархия решений** — переходить на следующий уровень только когда предыдущий доказанно не справляется: полнотекстовый поиск → переписывание запроса через LLM (~$0.001/запрос) → гибридный поиск (BM25 + реранкинг эмбеддингами) → эмбеддинг «на лету» → горячие/холодные уровни → полный пре-эмбеддинг.

**Реакция сообщества**: практик, строивший крупные RAG-системы, написал, что люди «сильно недооценивают полнотекстовый поиск и сильно переоценивают эмбеддинги». Другая повторяющаяся формулировка: RAG — это классический информационный поиск, где запросы формирует LLM, а отношение к векторному поиску как к «волшебной пыльце» добавляет стоимость и сложность без гарантии улучшения.

**Связь с паттерном LLM Wiki**: если качество поиска — узкое место, а эмбеддинги часто избыточны, то курируемая вики, читаемая моделью напрямую, полностью обходит проблему настройки retrieval для корпусов, помещающихся в контекст.

## Связанные записи
- [[rag-retrieval-augmented-generation]] ([RAG: Retrieval-Augmented Generation](../concepts/rag-retrieval-augmented-generation.md))
- [[rag-explained-embeddings-vector-db]] ([RAG Explained: Embeddings and Vector DBs](../concepts/rag-explained-embeddings-vector-db.md))
- [[llm-wiki-compiled-knowledge-vs-rag]] ([LLM Wiki: Compiled Knowledge vs RAG](../concepts/llm-wiki-compiled-knowledge-vs-rag.md))
- [[rags-evolution-agentic-ai]] ([RAG's Evolution to Agentic AI](../concepts/rags-evolution-agentic-ai.md))
