---
title: "LightRAG: Graph-Enhanced Retrieval-Augmented Generation"
title_ru: "LightRAG: графовое улучшение Retrieval-Augmented Generation"
category: tools
tags: [lightrag, rag, knowledge-graph, retrieval, embedding, graphrag, nlp]
aliases: [LightRAG, GraphRAG alternative, graph RAG, dual-level retrieval]
confidence: high
date: 2026-05-16
updated: 2026-05-16
sources:
  - https://lightrag.github.io/
  - https://arxiv.org/abs/2410.05779
---

## Summary
LightRAG is a graph-enhanced RAG system that integrates knowledge graph structures into text indexing and retrieval, achieving significantly lower cost and faster performance than Microsoft GraphRAG while supporting incremental updates.

## Key Ideas
- Dual-level retrieval paradigm: low-level retrieval handles specific entity-based queries, high-level retrieval addresses abstract and thematic questions
- Entity and relationship extraction from document chunks via LLM, with profiling that generates key-value pairs for each entity and relationship
- Deduplication function merges identical entities and relations discovered across different text segments, keeping the graph clean
- Incremental update algorithm processes new documents without rebuilding the entire knowledge graph from scratch
- Achieves approximately 10x token reduction and 65–80% lower ingestion cost compared to Microsoft GraphRAG
- Evaluated on four dimensions — Comprehensiveness, Diversity, Empowerment, and Overall — outperforming GraphRAG and other baselines across multiple datasets
- Ablation study confirms both low-level and high-level retrieval are necessary for optimal results

## Details
LightRAG was developed by researchers at the University of Hong Kong and Beijing University of Posts and Telecommunications (Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, Chao Huang). The core architecture follows a pipeline: extract entities and relations from document chunks using an LLM, build a knowledge graph from those extractions, generate key-value pair profiles for each entity and relationship, and then perform dual-level retrieval to support both specific and abstract queries before final LLM answer generation.

The dual-level retrieval paradigm is the central innovation. Low-level retrieval targets queries about specific entities and their direct relationships, pulling relevant subgraphs from the knowledge graph. High-level retrieval covers broader, thematic questions by aggregating across many entities and relationships. This two-track approach ensures that both fine-grained factual queries and broad summarisation queries receive appropriately scoped context.

A key practical advantage is the incremental update algorithm. Unlike systems that require full graph reconstruction when new documents arrive, LightRAG can insert new entities and relationships into the existing graph, deduplicating as it goes. This makes it feasible to maintain and grow a knowledge base over time without the compounding cost of full rebuilds. Combined with the significant reduction in token usage and ingestion cost, LightRAG presents a more scalable path to graph-based RAG than earlier approaches.

## Related Entries
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[karma-knowledge-graph-enrichment]] ([KARMA: Multi-Agent LLMs for Automated Knowledge Graph Enrichment](../concepts/karma-knowledge-graph-enrichment.md))
- [[parness-automated-scientific-research]] ([PARNESS: End-to-End Automated Scientific Research with Cross-Run Knowledge](../tools/parness-automated-scientific-research.md))

---
<!-- RU -->

## Краткое описание
LightRAG — система RAG с графовым улучшением, которая интегрирует структуры графов знаний в индексирование и поиск текстов, обеспечивая существенно меньшую стоимость и более высокую скорость по сравнению с Microsoft GraphRAG, а также поддержку инкрементальных обновлений.

## Ключевые идеи
- Парадигма двухуровневого поиска: поиск нижнего уровня обрабатывает конкретные запросы по сущностям, поиск верхнего уровня — абстрактные и тематические вопросы
- Извлечение сущностей и отношений из фрагментов документов с помощью LLM с профилированием, генерирующим пары «ключ-значение» для каждой сущности и отношения
- Функция дедупликации объединяет идентичные сущности и отношения, обнаруженные в различных текстовых фрагментах, поддерживая чистоту графа
- Алгоритм инкрементального обновления обрабатывает новые документы без полной перестройки графа знаний с нуля
- Достигает примерно 10-кратного сокращения token usage и на 65–80% меньшей стоимости интеграции по сравнению с Microsoft GraphRAG
- Оценка проводится по четырём измерениям — полнота (Comprehensiveness), разнообразие (Diversity), информативность (Empowerment) и общая оценка (Overall) — система превосходит GraphRAG и другие базовые методы на нескольких наборах данных
- Исследование абляции подтверждает, что оба уровня поиска необходимы для оптимальных результатов

## Подробнее
LightRAG разработан исследователями из Университета Гонконга и Пекинского университета почты и телекоммуникаций (Цзыжуй Го, Лянхао Ся, Яньхуа Юй, Ту Ао, Чжао Хуан). Основная архитектура следует конвейеру: извлечение сущностей и отношений из фрагментов документов с помощью LLM, построение графа знаний из этих извлечений, генерация профилей в виде пар «ключ-значение» для каждой сущности и отношения, а затем выполнение двухуровневого поиска для поддержки как конкретных, так и абстрактных запросов перед финальной генерацией ответа LLM.

Парадигма двухуровневого поиска является центральной инновацией. Поиск нижнего уровня ориентирован на запросы о конкретных сущностях и их прямых связях, извлекая релевантные подграфы из графа знаний. Поиск верхнего уровня охватывает более широкие тематические вопросы путём агрегации по множеству сущностей и отношений. Такой двухтрековый подход гарантирует, что как точечные фактологические запросы, так и широкие запросы на обобщение получают контекст соответствующего охвата.

Ключевое практическое преимущество — алгоритм инкрементального обновления. В отличие от систем, требующих полной реконструкции графа при поступлении новых документов, LightRAG может вставлять новые сущности и отношения в существующий граф с дедупликацией на лету. Это делает возможным поддержание и развитие базы знаний с течением времени без нарастающих затрат на полные перестроения. В сочетании со значительным сокращением использования токенов и стоимости интеграции, LightRAG представляет более масштабируемый подход к графовому RAG по сравнению с более ранними методами.

## Связанные записи
- [[llm-wiki-scientific-research]] ([LLM Wiki for Scientific Research and Academic Writing](../tips/llm-wiki-scientific-research.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-academic-applications]] ([LLM-Powered Personal Wikis: Academic Landscape and Feature Roadmap](../concepts/llm-wiki-academic-applications.md))
- [[karma-knowledge-graph-enrichment]] ([KARMA: Multi-Agent LLMs for Automated Knowledge Graph Enrichment](../concepts/karma-knowledge-graph-enrichment.md))
- [[parness-automated-scientific-research]] ([PARNESS: End-to-End Automated Scientific Research with Cross-Run Knowledge](../tools/parness-automated-scientific-research.md))
