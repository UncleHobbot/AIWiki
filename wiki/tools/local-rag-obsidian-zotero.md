---
title: "Local RAG: 100% Local Stack for Obsidian, Zotero, and Claude Code"
title_ru: "Local RAG: 100% локальный стек для Obsidian, Zotero и Claude Code"
category: tools
tags: [local-rag, lightrag, ollama, mcp, obsidian, zotero, privacy, offline, rag, knowledge-graph]
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://github.com/Ricardo-Kaminski/local-rag
---

## Summary

A complete privacy-first RAG stack that runs entirely on your machine using LightRAG + Ollama + MCP. Indexes Obsidian vaults (.md) and Zotero storage (.pdf), builds a knowledge graph with entity/relation extraction, and serves results to Claude Code via MCP tools. No API keys, no cloud, no data leaves your computer.

## Key Ideas
- **100% local:** No API keys, no cloud, no data leaves machine. Uses Ollama for both LLM (qwen2.5:14b) and embeddings (nomic-embed-text)
- **LightRAG server:** Knowledge graph (entities + relations) + vector index (NanoVectorDB), REST API at localhost:9621
- **Dual frontend:** Claude Code via MCP tools (query_rag, insert_document, rag_health, list_sources, get_graph_labels) and Obsidian via Smart Connect plugin
- **Ingestion pipeline:** Python script processes Obsidian .md and Zotero .pdf files into LightRAG index
- **Three query modes:** local, global, hybrid (default) — matching LightRAG's multi-hop reasoning capabilities
- **Hardware requirements:** Minimum 8GB RAM, recommended 16GB + 8-12GB GPU VRAM. Tested on RTX 3060 12GB
- **Alternative LLM option:** Can swap Ollama for Claude API as response LLM while keeping Ollama for embeddings
- **Standalone MCP package:** If you already have LightRAG running, install just the MCP server via `pip install local-rag-stack`
- **CLI tools:** `local-rag ingest` (index once), `local-rag watch` (continuous daemon), `local-rag start` (server + watcher), `local-rag mcp` (MCP server)

## Details

This tool bridges the gap between Karpathy's LLM Wiki pattern (which is markdown-first, compilation-based) and traditional RAG (which is vector-search-based). It offers a middle ground: local RAG with knowledge graph capabilities, suitable for privacy-sensitive environments where data cannot leave the machine.

The architecture is clean: documents flow through an ingestion pipeline into LightRAG (which maintains both a knowledge graph and vector index), then serve queries via MCP to Claude Code or via Smart Connect to Obsidian. The knowledge graph entity extraction gives it an advantage over pure vector RAG — it can answer questions that require connecting information across documents.

Compared to the LLM Wiki pattern, this is "RAG done right locally" — it still does per-query retrieval, but with graph-enhanced reasoning and zero privacy risk.

## Related Entries
- [[lightrag-graph-rag]]
- [[gnosis-mcp]]
- [[llm-wiki-pattern]]
- [[gnosis-mcp-vs-llm-wiki-pattern]]

---
<!-- RU -->

## Краткое описание

Полный приватный RAG-стек, работающий полностью локально на базе LightRAG + Ollama + MCP. Индексирует хранилища Obsidian (.md) и Zotero (.pdf), строит граф знаний с извлечением сущностей и связей, обслуживает запросы через MCP-инструменты в Claude Code. Без API-ключей, без облака, данные не покидают компьютер.

## Ключевые идеи
- **100% локально:** Без API-ключей, без облака. Ollama для LLM (qwen2.5:14b) и эмбеддингов (nomic-embed-text)
- **Сервер LightRAG:** Граф знаний (сущности + связи) + векторный индекс (NanoVectorDB), REST API на localhost:9621
- **Двойной фронтенд:** Claude Code через MCP-инструменты и Obsidian через Smart Connect
- **Три режима запросов:** local, global, hybrid (по умолчанию) — многошаговое рассуждение LightRAG
- **Требования:** Минимум 8 ГБ RAM, рекомендуется 16 ГБ + 8-12 ГБ VRAM. Протестировано на RTX 3060 12 ГБ
- **Альтернативный LLM:** Можно заменить Ollama на Claude API для ответов, оставив Ollama для эмбеддингов

## Связанные записи
- [[lightrag-graph-rag]]
- [[gnosis-mcp]]
- [[llm-wiki-pattern]]
- [[gnosis-mcp-vs-llm-wiki-pattern]]
