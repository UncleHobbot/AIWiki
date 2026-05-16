---
title: "Test-Driven Agentic Behaviours"
title_ru: "Test-driven разработка для агентного поведения"
category: tips
tags: [ai-agents, tdd, test-driven, agentic, claude-code, quality, behaviors]
updated: 2026-05-16
sources:
  - https://youtu.be/J6QILoLM0CE
---

## Summary
Antony Marcano demonstrates how to apply test-driven development principles to define and verify agentic AI behaviors — specifying what an AI agent should do before it does it, rather than prompting and hoping.

## Key Ideas
- **Behaviors as specs**: define agentic behaviors as explicit, testable specifications before the agent executes them — the AI equivalent of writing tests before code.
- **TDD discipline + AI agents**: the same fast-feedback-loop discipline that TDD brings to code applies to agent workflows; verify agent behavior systematically rather than ad-hoc.
- **Clarifying questions early, deep dives later**: a practical interaction model — interrupt for confusing things immediately, save detail questions for the end (applicable to both human talks and AI agent sessions).
- **Demo required Claude Code**: the talk was supposed to include a live Claude Code demo but Claude had elevated errors during the session — illustrating how agentic workflows depend on reliable tool availability.
- **Behavior-first design**: think about what the agent should accomplish (observable outcomes) before thinking about how it will accomplish it (implementation).

## Video Notes
- Talk from AI Agents Montreal meetup (2026-05-15), speaker Antony Marcano.
- Live demo was canceled due to Claude service outage during the session — a real-world reminder of agentic system dependencies.
- Antony has a companion YouTube video demonstrating the concepts in action; referenced during the talk.
- Key prompt for agents: write test scenarios for the agent behavior, then verify the agent satisfies them.

## Related Entries
- [[xp-practices-ai-assisted-development]]
- [[agentic-ai-coding-patterns-tornhill]]
- [[claude-code-agentic-loop]]

---
<!-- RU -->

## Краткое описание
Энтони Маркано демонстрирует, как применять принципы test-driven development к определению и верификации агентного AI-поведения — задавать спецификацию того, что должен делать AI-агент, до его выполнения, а не промптить и надеяться на лучшее.

## Ключевые идеи
- **Поведение как спецификация**: определять агентное поведение как явные, тестируемые спецификации до выполнения агентом — AI-эквивалент написания тестов до кода.
- **Дисциплина TDD + AI-агенты**: та же дисциплина быстрой обратной связи, которую TDD привносит в код, применима к рабочим процессам агентов; верифицировать поведение агента систематически, а не ad-hoc.
- **Уточняющие вопросы сразу, глубокое погружение позже**: практическая модель взаимодействия — прерывайте для непонятных вещей немедленно, оставляйте детальные вопросы на конец (применимо как к докладам людей, так и к сессиям AI-агентов).
- **Демо требовало Claude Code**: доклад должен был включать живое демо Claude Code, но во время сессии Claude имел повышенную частоту ошибок — иллюстрирует, как агентные рабочие процессы зависят от надёжности инструментов.
- **Поведение прежде реализации**: думайте о том, что должен достигнуть агент (наблюдаемые результаты), прежде чем думать о том, как он это сделает.

## Заметки по видео
- Доклад на AI Agents Montreal meetup (2026-05-15), спикер Энтони Маркано.
- Живое демо было отменено из-за сбоя в сервисе Claude во время сессии — реальный пример зависимости агентных систем.
- У Энтони есть сопровождающее YouTube-видео, демонстрирующее концепции в действии; упоминается в докладе.
- Ключевой промпт для агентов: напишите тест-сценарии для поведения агента, затем проверьте, что агент им соответствует.

## Связанные записи
- [[xp-practices-ai-assisted-development]]
- [[agentic-ai-coding-patterns-tornhill]]
- [[claude-code-agentic-loop]]
