---
title: "XP Practices Are the Missing Piece for AI-Assisted Development"
title_ru: "Практики XP — недостающее звено для разработки с AI-ассистентом"
category: tips
tags: [ai-coding, xp, tdd, test-driven-development, continuous-integration, claude-code, quality]
updated: 2026-05-16
sources:
  - https://youtu.be/M58tOdNHbxM
---

## Summary
Paul Hammond (20+ years experience, 13+ years XP practitioner) argues that Extreme Programming practices — TDD, pairing, CI, trunk-based development — are exactly what make AI-assisted development sustainable rather than just fast.

## Key Ideas
- **AI broke the confidence loop**: when Paul first used AI coding agents, they did too much at once and he lost the high-trust-in-tests feeling he had built over 13 years of TDD.
- **Fast feedback is the core**: TDD gives a feedback loop measured in seconds; AI without TDD extends that loop to minutes or hours, which degrades quality.
- **XP practices constrain AI helpfully**: short increments, fast feedback, continuous refactoring, and trunk-based development naturally limit the blast radius of AI mistakes.
- **100% coverage alone is not enough**: the talks demonstrates that coverage metrics can be gamed; what matters is whether tests capture behavior and give you confidence to deploy.
- **Sustainable means long-term**: speed without maintainability collapses; AI speeds up initial delivery but XP keeps the codebase healthy as it evolves.

## Video Notes
- [~5:00] Paul frames the talk around sustainability, not speed — a distinct angle from most AI coding content.
- [~8:00] He describes AI as an "interesting parlor trick" at first — impressive in parts but not trustworthy without a tight feedback loop.
- [~10:00] Key claim: AI that does "too much all in one go" is incompatible with sustainable development; you need to constrain it with small, verifiable steps.
- Talk from AI Agents Montreal meetup (2026-04-05), speaker from Manchester UK.

## Related Entries
- [[test-driven-agentic-behaviours]] ([Test-Driven Agentic Behaviours](../tips/test-driven-agentic-behaviours.md))
- [[agentic-ai-coding-patterns-tornhill]] ([Agentic AI Coding: Best Practice Patterns for Speed with Quality](../tips/agentic-ai-coding-patterns-tornhill.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))

---
<!-- RU -->

## Краткое описание
Пол Хаммонд (20+ лет опыта, 13+ лет практики XP) утверждает, что практики Extreme Programming — TDD, парное программирование, CI, trunk-based development — это именно то, что делает разработку с AI-ассистентом устойчивой, а не просто быстрой.

## Ключевые идеи
- **AI разрушил петлю доверия**: когда Пол впервые использовал AI-агенты, они делали слишком много сразу, и он потерял ощущение высокого доверия к тестам, выработанное за 13 лет TDD.
- **Быстрая обратная связь — это основа**: TDD даёт цикл обратной связи в секундах; AI без TDD растягивает его до минут или часов, что снижает качество.
- **Практики XP полезно ограничивают AI**: короткие инкременты, быстрая обратная связь, непрерывный рефакторинг и trunk-based development естественным образом ограничивают масштаб ошибок AI.
- **100% покрытия само по себе недостаточно**: метрики покрытия можно фальсифицировать; важно, фиксируют ли тесты поведение и дают ли вам уверенность для деплоя.
- **Устойчивость — это долгосрочно**: скорость без сопровождаемости рушится; AI ускоряет начальную разработку, но XP сохраняет кодовую базу здоровой по мере её эволюции.

## Заметки по видео
- [~5:00] Пол формулирует тему вокруг устойчивости, а не скорости — особый угол, отличный от большинства AI-контента.
- [~8:00] Описывает AI как «занятный фокус» поначалу — впечатляющий, но ненадёжный без тесного цикла обратной связи.
- [~10:00] Ключевой тезис: AI, который делает «слишком много за один раз», несовместим с устойчивой разработкой; его нужно ограничивать малыми верифицируемыми шагами.
- Доклад на AI Agents Montreal meetup (2026-04-05), спикер из Манчестера, UK.

## Связанные записи
- [[test-driven-agentic-behaviours]] ([Test-Driven Agentic Behaviours](../tips/test-driven-agentic-behaviours.md))
- [[agentic-ai-coding-patterns-tornhill]] ([Agentic AI Coding: Best Practice Patterns for Speed with Quality](../tips/agentic-ai-coding-patterns-tornhill.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
