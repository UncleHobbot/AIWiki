---
title: "Critical LLM Knowledge Base for Developers: Tokens to Production AI Agents"
title_ru: "Критическая база знаний LLM: от токенов до AI-агентов в продакшене"
category: concepts
tags: [llm, transformers, context-window, token, attention, reasoning, ai-agents, context-engineering, production]
date: 2025-11-14
updated: 2026-05-17
transcript: unavailable
sources:
  - https://www.youtube.com/watch?v=GD0MwuGAP18
---

## Summary

Dmitry Bereznitsky's comprehensive one-hour guide to LLM fundamentals for practicing engineers: how tokens, attention, and transformers work; why context windows are critical for AI assistants; prefill vs decode phases; LLM vs reasoning models vs AI agents as three complexity levels; and why context engineering matters more than prompt engineering. 139K views — one of the most popular Russian-language AI engineering resources.

## Key Ideas
- **Transformer architecture under the hood:** How tokens, attention mechanism, and transformers power GPT, Claude, and other LLMs
- **Context window management:** Why context windows are critical for AI assistants (Cursor, Claude Code) and how to manage them
- **Prefill vs decode phases:** Understanding the two inference phases enables cost optimization through caching and proper API usage
- **Three levels of complexity:** LLM → Reasoning models → AI agents — when to use each level
- **Context engineering > prompt engineering:** Context is more important than prompts. What you feed the model matters more than how you phrase the question
- **RAG vs fine-tuning decision:** When to use each approach for production systems
- **Conscious AI architecture:** Building production-ready AI solutions requires deliberate architecture, not random prompting

## Video Notes

| Timestamp | Key Point |
|---|---|
| [0:00] | Full guide overview — from tokens to production AI agents |
| [~10:00] | Token mechanics, attention, transformer architecture |
| [~20:00] | Context window management in Cursor, Claude Code |
| [~30:00] | Prefill vs decode, cost optimization, API caching |
| [~40:00] | LLM vs Reasoning models vs AI agents — three levels |
| [~50:00] | Context engineering: why context > prompts |

## Details

This 55-minute video has become a canonical Russian-language reference for LLM fundamentals. At 139K views, it's one of the most-watched Russian AI engineering tutorials. The video bridges the gap between academic transformer explanations and practical production concerns, covering everything from token-level mechanics to architectural decisions for production AI systems.

The key thesis: "context engineering" is the discipline that matters most for production AI. While prompt engineering focuses on phrasing, context engineering focuses on what information the model receives, in what order, and with what structure — a philosophy directly aligned with Karpathy's LLM Wiki pattern.

## Related Entries
- [[rags-evolution-agentic-ai]]
- [[llm-assisted-coding-systems-perspective]]
- [[agent-harness-engineering]]

---
<!-- RU -->

## Краткое описание

Часовой гид Дмитрия Березницкого по основам LLM для инженеров-практиков: как работают токены, attention и трансформеры; почему контекстное окно критично для AI-ассистентов; prefill vs decode; три уровня сложности (LLM → Reasoning → Agents); и почему контекстная инженерия важнее промпт-инжиниринга. 139K просмотров.

## Ключевые идеи
- **Архитектура трансформера:** Как токены, механизм внимания и трансформеры работают под капотом GPT, Claude и других LLM
- **Управление контекстным окном:** Почему контекстные окна критичны для AI-ассистентов (Cursor, Claude Code)
- **Prefill vs decode:** Две фазы инференса — понимание для оптимизации затрат через кэширование
- **Три уровня сложности:** LLM → Reasoning-модели → AI-агенты — когда использовать каждый
- **Контекстная инженерия > промпт-инжиниринг:** Контекст важнее промптов
- **RAG vs fine-tuning:** Когда использовать каждый подход в продакшене

## Заметки по видео

| Таймкод | Ключевой момент |
|---|---|
| [~10:00] | Механика токенов, attention, архитектура трансформера |
| [~20:00] | Управление контекстным окном в Cursor, Claude Code |
| [~30:00] | Prefill vs decode, оптимизация затрат, API-кэширование |
| [~40:00] | LLM vs Reasoning-модели vs AI-агенты — три уровня |
| [~50:00] | Контекстная инженерия: почему контекст > промпты |

## Связанные записи
- [[rags-evolution-agentic-ai]]
- [[llm-assisted-coding-systems-perspective]]
- [[agent-harness-engineering]]
