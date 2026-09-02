---
title: "Hillock — Local Neuro-Symbolic Memory Engine for Ollama"
title_ru: "Hillock — локальный нейросимвольный движок памяти для Ollama"
category: tools
tags: [memory, knowledge-graph, hyperdimensional-computing, ollama, local-first, rag-alternative, agpl]
aliases: [Hillock, neuro-symbolic memory, hypervector memory]
confidence: medium
updated: 2026-09-01
sources:
  - https://github.com/roandejager/Hillock
---

## Summary
Hillock (78 stars, AGPL-3.0, v0.6.0) is a 100% local, gradient-free neuro-symbolic memory engine that pairs with Ollama for final response generation. It combines a SQLite knowledge graph, Hebbian synaptic plasticity, and 10,000-dimensional hyperdimensional computing (VSA/HDC) — explicitly positioned as a replacement for heavy vector-DB + LLM-extraction local RAG stacks on edge hardware.

## Key Ideas
- **Three memory layers:** SQLite SPO-triple knowledge graph (no vector drift), Hebbian plasticity engine for associative recall, and a 10,000-D bipolar hypervector reservoir with fading memory (decay 0.95/step).
- **TALON ingestion with zero generative-LLM calls:** FastCoref coreference, MiniLM bi-encoder predicate router (<2 ms), GLiREL zero-shot relation extraction — vs 15–30 min for an 8B-LLM extraction pipeline, it claims ~5 s per 30-sentence doc.
- **HYDRA honesty gate:** ColBERT-style MaxSim gating natively in 10,000-D bipolar space; a hard 0.55 cosine threshold blocks unanswerable questions *before* the LLM — hardcoded refusal instead of hallucination.
- **Multi-hop reasoning (v0.6.0):** positional-permutation binding of 2–3-hop relational paths at ingestion; sub-dimensional projection cascade early-rejects 95% of candidates in ~0.5 ms.
- **Edge-friendly:** <1.2 GB VRAM (tested on a GTX 1070, CPU-only fallback); Ollama is called only for grounded generation after the gate.

## Details
Hillock's thesis inverts the local-RAG stack: instead of LLM-extracted vectors + a vector DB, use symbolic triples + hypervectors for storage and gating, and reserve the LLM purely for language generation. The honesty gate is the standout idea — refusing to answer when the graph can't ground it attacks hallucination structurally rather than by prompting. Fits the wiki's memory cluster ([[shokunin-memory-system]], [[noosphere-ai-memory]]) as the "no-LLM-in-the-loop" extreme.

## Related Entries
- [[shokunin-memory-system]] ([Shokunin Memory System](shokunin-memory-system.md))
- [[noosphere-ai-memory]] ([Noosphere AI Memory](noosphere-ai-memory.md))
- [[ollama]] ([Ollama](ollama.md))
- [[local-rag-obsidian-zotero]] ([Local RAG Stack](local-rag-obsidian-zotero.md))

---
<!-- RU -->

## Краткое описание
Hillock (78 звёзд, AGPL-3.0, v0.6.0) — 100% локальный, безградиентный нейросимвольный движок памяти, работающий в паре с Ollama для финальной генерации. Сочетает SQLite-граф знаний, хеббовскую синаптическую пластичность и гиперразмерные вычисления (10 000-мерные VSA/HDC) — позиционируется как замена тяжёлым локальным RAG-стекам «векторная БД + LLM-экстракция» на edge-железе.

## Ключевые идеи
- **Три слоя памяти:** SQLite граф SPO-триплет (без дрейфа векторов), движок хеббовской пластичности для ассоциативного recall и 10 000-мерный биполярный гипервекторный резервуар с затуханием (0.95/шаг).
- **TALON-ингестия без генеративных LLM-вызовов:** FastCoref, MiniLM-роутер (<2 мс), GLiREL zero-shot извлечение отношений — ~5 с на документ в 30 предложений против 15–30 минут у 8B-LLM-пайплайна.
- **Ворота честности HYDRA:** MaxSim-гейтинг в 10 000-мерном пространстве; жёсткий порог 0.55 блокирует неотвечаемые вопросы *до* LLM — структурный отказ вместо галлюцинации.
- **Multi-hop (v0.6.0):** позиционно-перестановочное связывание путей 2–3 хопов при ингестии; каскад раннего отклонения 95% кандидатов за ~0.5 мс.
- **Edge-дружелюбность:** <1.2 ГБ VRAM (GTX 1070, CPU-fallback); Ollama зовётся только для генерации после ворот.

## Подробнее
Тезис Hillock переворачивает локальный RAG-стек: вместо LLM-экстракции векторов и векторной БД — символические триплеты и гипервекторы для хранения и гейтинга, а LLM — чисто для генерации языка. Ворота честности — главная идея: отказ отвечать, когда граф не может заземлить вопрос, атакует галлюцинацию структурно, а не промптами.

## Связанные записи
- [[shokunin-memory-system]] ([Shokunin Memory System](shokunin-memory-system.md))
- [[noosphere-ai-memory]] ([Noosphere AI Memory](noosphere-ai-memory.md))
- [[ollama]] ([Ollama](ollama.md))
- [[local-rag-obsidian-zotero]] ([Local RAG Stack](local-rag-obsidian-zotero.md))
