---
title: "OpenCodeRAG — RAG Plugin for OpenCode"
title_ru: "OpenCodeRAG — RAG-плагин для OpenCode"
category: tools
tags: [opencode, rag, embedding, semantic-search, local-models, ollama]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://github.com/MrDoe/OpenCodeRAG
  - https://www.reddit.com/r/opencodeCLI/comments/1u2w3kc/opencoderag_rag_for_opencode_via_locally_hosted/
---

## Summary

RAG plugin for OpenCode that adds semantic code search powered by locally-hosted embedding models via Ollama or OpenAI API, replacing expensive file-read tool calls with targeted vector-similarity retrieval.

## Key Ideas

- Hybrid search combining TF-IDF keyword index with vector similarity for accurate code retrieval
- Suggests related files after each user message and auto-injects relevant code chunks into context
- Supports locally-hosted embedding models through Ollama, keeping code private
- Primary goal: save tokens from tool calls and speed up file search in large repositories
- Drop-in plugin — installs via OpenCode plugin registry, no manual wiring needed

## Details

OpenCodeRAG addresses a core bottleneck in agentic coding: the agent spends too many tokens reading entire files to find relevant code. Instead of relying on the file-read tool, the plugin builds a vector index of the repository and retrieves only the chunks that matter for the current task.

The hybrid search strategy is notable — pure vector search misses exact identifier matches, while pure keyword search misses semantic relationships. Fusing both via TF-IDF + cosine similarity gives the best of both worlds. The plugin runs embedding inference locally via Ollama, so no code leaves the machine.

After each user message, OpenCodeRAG suggests a ranked list of related files and optionally injects the top-K chunks directly into the prompt context window. This reduces the number of tool round-trips and lets the agent reason over larger codebases without hitting context limits.

## Related Entries

- [[ollama]] ([Ollama](../tools/ollama.md))
- [[lightrag-graph-rag]] ([LightRAG](../tools/lightrag-graph-rag.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))

---
<!-- RU -->

## Краткое описание

RAG-плагин для OpenCode, добавляющий семантический поиск по коду на основе локальных embedding-моделей через Ollama или OpenAI API, заменяющий дорогостоящие вызовы file-read на целевой векторный поиск.

## Ключевые идеи

- Гибридный поиск, объединяющий TF-IDF индекс ключевых слов с векторной схожестью для точного поиска кода
- Предлагает связанные файлы после каждого сообщения пользователя и автоматически внедряет релевантные фрагменты кода в контекст
- Поддержка локальных embedding-моделей через Ollama — код не покидает машину
- Главная цель: экономия токенов на вызовах инструментов и ускорение поиска файлов в больших репозиториях
- Плагин «из коробки» — устанавливается через реестр плагинов OpenCode

## Подробнее

OpenCodeRAG решает ключевую проблему агентного кодирования: агент тратит слишком много токенов на чтение целых файлов для поиска нужного кода. Вместо использования инструмента file-read плагин строит векторный индекс репозитория и извлекает только релевантные фрагменты.

Стратегия гибридного поиска заслуживает внимания — чистый векторный поиск пропускает точные совпадения идентификаторов, а чистый поиск по ключевым словам упускает семантические связи. Объединение TF-IDF + косинусная схожесть даёт лучшее из обоих подходов. Плагин выполняет embedding-инференс локально через Ollama, поэтому код не покидает компьютер.

После каждого сообщения пользователя OpenCodeRAG предлагает ранжированный список связанных файлов и опционально внедряет top-K фрагментов напрямую в контекстное окно промпта. Это уменьшает количество round-trip вызовов инструментов и позволяет агенту работать с большими кодовыми базами без превышения лимитов контекста.

## Связанные записи

- [[ollama]] ([Ollama](../tools/ollama.md))
- [[lightrag-graph-rag]] ([LightRAG](../tools/lightrag-graph-rag.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))
