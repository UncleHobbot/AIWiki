---
title: "Karpathy Killed RAG: Obsidian + Claude Code Second Brain"
title_ru: "Карпати убил RAG одним промптом: Obsidian + Claude Code"
category: tips
tags: [karpathy, llm-wiki, obsidian, claude-code, rag, second-brain, knowledge-base]
date: 2026-04-18
updated: 2026-05-17
transcript: unavailable
sources:
  - https://www.youtube.com/watch?v=xU7Llr8DUUk
---

## Summary

Russian-language walkthrough of Karpathy's LLM Wiki approach using Obsidian + Claude Code as a "second brain." Demonstrates setting up the system, loading articles, and comparing with traditional RAG. The video argues Karpathy's prompt-driven knowledge management pattern eliminates the need for RAG pipelines.

## Key Ideas
- **Karpathy's method:** A single well-crafted system prompt in Claude Code replaces complex RAG infrastructure for personal knowledge management
- **Obsidian as the vault:** Markdown files in Obsidian serve as the knowledge store; Claude Code reads them directly via AGENTS.md context injection
- **5-minute setup:** The entire system (Obsidian vault + Claude Code config) can be configured in under 5 minutes
- **RAG comparison:** Traditional RAG requires chunking, embeddings, vector databases, retrieval pipelines — Karpathy's approach sidesteps all of this by using the LLM's native context window
- **Russian-language resource:** One of the first comprehensive Russian tutorials on the LLM Wiki pattern

## Video Notes

| Timestamp | Key Point |
|---|---|
| [0:00] | Introduction to Karpathy's method |
| [01:12] | How the system works and why it deserves attention |
| [03:54] | Setting up Obsidian and Claude Code |
| [07:59] | Loading your first article into the system |
| [10:47] | Comparison with traditional RAG |
| [12:21] | Conclusion |

## Details

This Russian-language video by Yuri Kirichenko is a practical guide to implementing Karpathy's LLM Wiki pattern. It covers the full setup from scratch: configuring Obsidian as the markdown vault, connecting Claude Code to read the vault structure via AGENTS.md, and processing the first article into the wiki format. The key argument is that Karpathy's approach — using structured markdown files with a schema layer (AGENTS.md) for context injection — achieves what RAG promises without any of the infrastructure overhead (vector databases, embedding pipelines, retrieval steps).

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-implementations-landscape]] ([LLM Wiki Implementations Landscape: State of the Ecosystem (May 2026)](../concepts/llm-wiki-implementations-landscape.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
- [[andrej-karpathy]] ([Andrej Karpathy](../people/andrej-karpathy.md))

---
<!-- RU -->

## Краткое описание

Практический гайд по методу Карпати — создание «второго мозга» на Obsidian + Claude Code за 5 минут. Демонстрируется настройка системы, загрузка статей и сравнение с традиционным RAG. Подход Карпати заменяет сложную RAG-инфраструктуру одним системным промптом.

## Ключевые идеи
- **Метод Карпати:** Один хорошо составленный системный промпт в Claude Code заменяет сложную RAG-инфраструктуру для управления личными знаниями
- **Obsidian как хранилище:** Markdown-файлы в Obsidian служат хранилищем знаний; Claude Code читает их напрямую через инъекцию контекста через AGENTS.md
- **Настройка за 5 минут:** Вся система (хранилище Obsidian + конфигурация Claude Code) настраивается менее чем за 5 минут
- **Сравнение с RAG:** Традиционный RAG требует чанкинга, эмбеддингов, векторных БД, пайплайнов поиска — подход Карпати обходит всё это, используя нативное контекстное окно LLM
- **Русскоязычный ресурс:** Один из первых подробных русскоязычных туториалов по паттерну LLM Wiki

## Заметки по видео

| Таймкод | Ключевой момент |
|---|---|
| [0:00] | Вступление — метод Карпати |
| [01:12] | Как работает система и почему заслуживает внимания |
| [03:54] | Настройка Obsidian и Claude Code |
| [07:59] | Загрузка первой статьи в систему |
| [10:47] | Сравнение с традиционным RAG |
| [12:21] | Заключение |

## Подробнее

Видео Юрия Кириченко — практическое руководство по реализации паттерна LLM Wiki Карпати. Ключевой аргумент: подход Карпати — использование структурированных markdown-файлов со слоем схемы (AGENTS.md) для инъекции контекста — достигает того, что обещает RAG, без какой-либо инфраструктурной нагрузки (векторные БД, пайплайны эмбеддингов, этапы поиска).

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[llm-wiki-implementations-landscape]] ([LLM Wiki Implementations Landscape: State of the Ecosystem (May 2026)](../concepts/llm-wiki-implementations-landscape.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
- [[andrej-karpathy]] ([Andrej Karpathy](../people/andrej-karpathy.md))
