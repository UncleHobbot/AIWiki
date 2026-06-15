---
title: "turbo-graph — Graph Memory for RAG"
title_ru: "turbo-graph — графовая память для RAG"
category: tools
tags: [rag, graph-memory, knowledge-graph, retrieval, turbovec]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://github.com/bigmacfive/turbo-graph/
---

## Summary
GraphMemoryIndex implementation on turbovec that adds graph-based memory to RAG systems. Enables relational retrieval where entities and their connections are stored as a graph, allowing multi-hop reasoning over knowledge. Alternative to flat vector similarity search.

## Key Ideas
- Builds a GraphMemoryIndex on top of the turbovec library
- Stores entities and their relationships as a graph, not just flat embeddings
- Enables multi-hop reasoning — queries can traverse connections between entities
- Alternative to standard vector similarity search in RAG pipelines
- Targets the well-known limitation of flat retrieval losing relational context

## Details
Standard RAG systems retrieve chunks by vector similarity, which works well for factual lookup but struggles with relational questions like "which tools use the same approach as X?" or "what is the chain of dependencies from A to B?" Turbo-graph addresses this by maintaining a graph structure alongside embeddings.

The graph stores entities as nodes and their relationships as edges. During retrieval, the system can traverse multiple hops to find connected information that a flat similarity search would miss. This is particularly valuable for knowledge bases with rich interconnections.

Built on turbovec, the implementation aims for performance while keeping the API simple enough to integrate into existing RAG pipelines.

## Related Entries
- [[lightrag-graph-rag]] ([LightRAG](../tools/lightrag-graph-rag.md))
- [[rag-retrieval-augmented-generation]] ([RAG](../concepts/rag-retrieval-augmented-generation.md))

---
<!-- RU -->

## Краткое описание
Реализация GraphMemoryIndex на базе turbovec, добавляющая графовую память в RAG-системы. Обеспечивает реляционный поиск, где сущности и их связи хранятся в виде графа, позволяя многошаговый вывод по знаниям. Альтернатива плоскому векторному поиску по сходству.

## Ключевые идеи
- Строит GraphMemoryIndex поверх библиотеки turbovec
- Хранит сущности и их отношения в виде графа, а не только плоских эмбеддингов
- Обеспечивает многошаговый вывод — запросы могут traversировать связи между сущностями
- Альтернатива стандартному поиску по векторному сходству в RAG-конвейерах
- Направлено на решение известной проблемы плоского поиска — потери реляционного контекста

## Подробнее
Стандартные RAG-системы извлекают фрагменты по векторному сходству, что хорошо работает для поиска фактов, но затрудняет ответ на реляционные вопросы вроде «какие инструменты используют тот же подход, что и X?» или «каковы зависимости от A до B?». Turbo-graph решает это, поддерживая графовую структуру наряду с эмбеддингами.

Граф хранит сущности как узлы и их отношения как рёбра. При поиске система может traversировать несколько шагов для нахождения связанной информации, которую плоский поиск по сходству пропустил бы. Это особенно ценно для баз знаний с богатыми взаимосвязями.

Построенный на turbovec, инструмент стремится к производительности, сохраняя при этом достаточно простой API для интеграции в существующие RAG-конвейеры.

## Связанные записи
- [[lightrag-graph-rag]] ([LightRAG](../tools/lightrag-graph-rag.md))
- [[rag-retrieval-augmented-generation]] ([RAG](../concepts/rag-retrieval-augmented-generation.md))
