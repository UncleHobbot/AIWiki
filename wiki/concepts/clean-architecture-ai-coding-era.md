---
title: "Clean Architecture in the AI Coding Era"
title_ru: "Чистая архитектура в эпоху AI-кода"
category: concepts
tags: [clean-architecture, ai-coding, context-engineering, llm-code-quality, architecture, entity, use-case]
date: 2025-09-24
updated: 2026-05-17
transcript: unavailable
sources:
  - https://www.youtube.com/watch?v=8tVAeYASYT0
---

## Summary

Dmitry Bereznitsky explains why Clean Architecture principles become critical when AI writes 80% of your code. Proper structure — Entities, Use Cases, Dependency Rule — gives LLMs the boundaries they need to generate quality code. Without architecture, AI-generated code spirals into unmaintainable complexity.

## Key Ideas
- **AI paradox:** Speed of AI coding vs. loss of control — when AI writes 80% of code, architecture is the only safety net
- **Entity vs ORM models:** In Clean Architecture, Entities represent business logic, not database rows. This distinction is critical for AI — LLMs generate better code when boundaries are clear
- **Use Cases help LLMs:** Well-defined Use Cases give LLMs a scoped context for code generation, dramatically improving quality
- **Dependency Rule and data flow:** Dependencies point inward (from frameworks to domain). AI tools that understand this generate architecturally correct code
- **Frameworks vs Clean Architecture:** Spring, Django, and similar frameworks contradict Clean Architecture by coupling domain to infrastructure
- **Practical example:** Order creation flow through all architecture layers

## Video Notes

| Timestamp | Key Point |
|---|---|
| [0:00] | The AI development paradox: speed vs control |
| [02:12] | Video plan overview |
| [02:55] | Clean Architecture history and principles |

## Details

The core argument: when AI writes most of your code, the architecture becomes more important, not less. LLMs generate better code when they have clear boundaries (Entities, Use Cases, interface adapters). Without these boundaries, AI-generated code accumulates technical debt at alarming speed — clean architecture provides the guardrails that keep AI productive long-term.

## Related Entries
- [[agentic-ai-coding-patterns-tornhill]] ([Agentic AI Coding: Best Practice Patterns for Speed with Quality](../tips/agentic-ai-coding-patterns-tornhill.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development in the Real World: From BMAD to Custom Skills](../tips/spec-driven-development-bmad.md))
- [[llm-assisted-coding-systems-perspective]] ([LLM-Assisted Coding: A Systems Perspective](../tips/llm-assisted-coding-systems-perspective.md))

---
<!-- RU -->

## Краткое описание

Дмитрий Березницкий объясняет, почему принципы чистой архитектуры становятся критическими, когда ИИ пишет 80% кода. Правильная структура — Entities, Use Cases, правило зависимостей — даёт LLM границы, необходимые для генерации качественного кода.

## Ключевые идеи
- **Парадокс ИИ:** Скорость ИИ-кодирования vs потеря контроля — когда ИИ пишет 80% кода, архитектура — единственная страховка
- **Entity vs ORM-модели:** Entities представляют бизнес-логику, а не строки БД. Это различие критично для ИИ
- **Use Cases помогают LLM:** Чётко определённые Use Cases дают LLM контекст для генерации кода
- **Правило зависимостей:** Зависимости направлены внутрь (от фреймворков к домену)
- **Фреймворки vs чистая архитектура:** Spring, Django противоречат чистой архитектуре

## Заметки по видео

| Таймкод | Ключевой момент |
|---|---|
| [0:00] | Парадокс AI-разработки: скорость vs контроль |

## Связанные записи
- [[agentic-ai-coding-patterns-tornhill]] ([Agentic AI Coding: Best Practice Patterns for Speed with Quality](../tips/agentic-ai-coding-patterns-tornhill.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development in the Real World: From BMAD to Custom Skills](../tips/spec-driven-development-bmad.md))
- [[llm-assisted-coding-systems-perspective]] ([LLM-Assisted Coding: A Systems Perspective](../tips/llm-assisted-coding-systems-perspective.md))
