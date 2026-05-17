---
title: "RAG's Evolution: From Simple Retrieval to Agentic AI"
title_ru: "Эволюция RAG: от простого поиска до агентного ИИ"
category: concepts
tags: [rag, retrieval-augmented-generation, semantic-search, hybrid-retrieval, agentic-ai, agents, vector-database, embeddings]
date: 2026-05-05
updated: 2026-05-17
sources:
  - https://www.youtube.com/watch?v=JB2P5Gk23VI
---

## Summary

IBM Technology traces the full evolution of information retrieval from keyword search (TF-IDF/BM25) through semantic search (embeddings), traditional RAG, advanced RAG (rerankers, query expansion), to agentic RAG — where retrieval becomes a tool invoked as part of reasoning, not a fixed pipeline.

## Key Ideas
- **Keyword search (inverted indices):** Maps keywords to documents using TF-IDF/BM25 ranking. Still powers most of the internet but doesn't understand language — treats words as symbols, not meaning
- **Semantic search (embeddings):** Represents text as high-dimensional vectors learned by neural networks. Similar concepts cluster together regardless of exact words (e.g., coffee ≈ espresso, both far from house)
- **Hybrid retrieval:** Combines keyword precision with semantic recall. Doesn't replace keyword search — complements it
- **Traditional RAG (linear pipeline):** Embed documents → vector DB → retrieve at query time → augment LLM prompt → generate. Simple but effective, significantly reduced hallucinations
- **Advanced RAG:** Adds rerankers, query rewriting/expansion, hybrid retrieval. More accurate but still fundamentally static — pipeline is predetermined
- **Agentic RAG (current frontier):** Agent decides whether retrieval is needed, where to search, what to ask, when enough info is obtained. Can compare sources, validate claims, iterate, invoke APIs, pull from multiple knowledge bases
- **The hardest part of AI isn't generation — it's deciding what to look at**

## Video Notes

| Timestamp | Key Point |
|---|---|
| [0:00] | Early search = inverted indices mapping keywords to documents |
| [1:30] | TF-IDF/BM25 for ranking, but no language understanding (Python = coding or pet snake?) |
| [2:15] | Semantic search: vectors/embeddings learned by neural networks from context |
| [3:00] | Hybrid systems bridge keyword precision with semantic recall |
| [3:45] | LLMs predict next token from training patterns — don't retrieve facts, don't know current info |
| [4:30] | RAG born: search external knowledge → augment prompt → generate. External memory for LLMs |
| [5:30] | Advanced RAG: rerankers, query rewriting, hybrid retrieval — still static pipeline |
| [6:15] | Agentic RAG: agent decides retrieval strategy, validates, iterates, uses tools |
| [7:00] | "The hardest part of AI isn't generation. It's deciding what to look at." |

## Details

The video presents a clean 5-stage evolutionary model:

1. **Keyword search** (TF-IDF, BM25) — exact matching, no semantic understanding
2. **Semantic search** (embeddings) — meaning-based retrieval via learned vector representations
3. **Hybrid search** — combines (1) and (2) for precision + recall
4. **Traditional RAG** — search results augment LLM prompts, giving LLMs external memory
5. **Agentic RAG** — LLM-based agents use retrieval as one tool among many, with autonomous planning and multi-step reasoning

The critical insight: each evolution doesn't replace the previous stage — it builds on it. Keyword search is still the backbone. Semantic search adds understanding. RAG adds generation. Agents add reasoning. The current frontier is systems that know *how to find answers*, not just how to generate them.

## Related Entries
- [[llm-wiki-pattern]]
- [[gnosis-mcp-vs-llm-wiki-pattern]]
- [[llm-wiki-implementations-landscape]]

---
<!-- RU -->

## Краткое описание

IBM Technology прослеживает полную эволюцию информационного поиска — от ключевого поиска (TF-IDF/BM25) через семантический поиск (эмбеддинги), традиционный RAG, продвинутый RAG (реранкеры, расширение запросов) до агентного RAG, где поиск становится инструментом, вызываемым в процессе рассуждения, а не фиксированным конвейером.

## Ключевые идеи
- **Ключевой поиск (инвертированные индексы):** Отображает ключевые слова на документы с ранжированием TF-IDF/BM25. Не понимает язык — treats слова как символы, а не смысл
- **Семантический поиск (эмбеддинги):** Представляет текст как многомерные векторы. Похожие концепции кластеризуются вместе независимо от точных слов
- **Гибридный поиск:** Сочетает точность ключевого поиска с семантическим отзывом. Не заменяет ключевой поиск — дополняет его
- **Традиционный RAG (линейный конвейер):** Эмбеддинги документов → векторная БД → поиск при запросе → дополнение промпта LLM → генерация
- **Продвинутый RAG:** Добавляет реранкеры, перезапись запросов, гибридный поиск. Более точный, но принципиально статичный
- **Агентный RAG (текущий рубеж):** Агент решает, нужен ли поиск, где искать, что спросить, когда информации достаточно. Может сравнивать источники, валидировать утверждения, итерировать
- **Самая сложная часть ИИ — не генерация, а решение, на что смотреть**

## Заметки по видео

| Таймкод | Ключевой момент |
|---|---|
| [0:00] | Ранний поиск = инвертированные индексы |
| [1:30] | TF-IDF/BM25 для ранжирования, но без понимания языка |
| [2:15] | Семантический поиск: векторы/эмбеддинги |
| [3:00] | Гибридные системы: точность ключевого + семантический отзыв |
| [4:30] | RAG: поиск во внешней БЗ → дополнение промпта → генерация |
| [5:30] | Продвинутый RAG: реранкеры, перезапись — но статичный конвейер |
| [6:15] | Агентный RAG: агент решает стратегию поиска, валидирует, итерирует |
| [7:00] | «Самая сложная часть ИИ — не генерация. Это решение, на что смотреть» |

## Подробнее

Видео представляет чистую 5-ступенчатую модель эволюции: ключевой поиск → семантический поиск → гибридный поиск → традиционный RAG → агентный RAG. Ключевое наблюдение: каждая эволюция не заменяет предыдущую стадию — она строится поверх неё.

## Связанные записи
- [[llm-wiki-pattern]]
- [[gnosis-mcp-vs-llm-wiki-pattern]]
- [[llm-wiki-implementations-landscape]]
