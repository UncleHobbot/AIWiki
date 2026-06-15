---
title: "Grind — Claude Code Non-Stop Hook"
title_ru: "Grind — хук непрерывной работы Claude Code"
category: tools
tags: [claude-code, hooks, automation, continuous-coding]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://github.com/cloudlinqed/grind
  - https://www.reddit.com/r/ClaudeCode/comments/1u3dn5x/
---

## Summary
Claude Code hook that fires every time the agent pauses or tries to take a break. Compares current state against the plan and end goal, then reprompts to continue if the task isn't complete. Designed for overnight/long-running projects where Claude Code tends to stop mid-way.

## Key Ideas
- Hooks into Claude Code's pause/break events and reprompts automatically
- Compares current state against the original plan and end goal before deciding to continue
- Purpose-built for long-running tasks and overnight automation
- Warning: can consume subscription usage rapidly due to continuous operation
- Part of the growing Claude Code hooks ecosystem

## Details
Grind solves a specific pain point with Claude Code: the agent frequently pauses to ask clarifying questions or declares it needs a break, even when the task is well-defined. For developers running overnight builds or long refactoring sessions, this means waking up to an incomplete task.

The hook intercepts these pause events, evaluates whether the original goal has been met, and if not, generates a new prompt to continue. It does not bypass Claude Code's safety mechanisms — it simply keeps the agent focused on the stated objective.

Users should be cautious about usage costs. Running Claude Code continuously for hours can exhaust subscription limits quickly. The tool is best suited for well-scoped tasks with clear completion criteria.

## Notable Quotes
> "Warning: can consume subscription usage rapidly." — README

## Related Entries
- [[ship-skills-claude-code-pipeline]] ([Ship Skills](../tools/ship-skills-claude-code-pipeline.md))
- [[claude-code]] ([Claude Code](../tools/claude-code.md))

---
<!-- RU -->

## Краткое описание
Хук для Claude Code, срабатывающий каждый раз, когда агент приостанавливается или пытается сделать перерыв. Сравнивает текущее состояние с планом и конечной целью, затем повторно запрашивает продолжение, если задача не завершена. Разработано для ночных и длительных проектов, где Claude Code склонен останавливаться на середине.

## Ключевые идеи
- Перехватывает события паузы/перерыва Claude Code и автоматически повторно запрашивает
- Сравнивает текущее состояние с исходным планом и конечной целью перед принятием решения о продолжении
- Создано специально для длительных задач и ночной автоматизации
- Предупреждение: может быстро израсходовать лимиты подписки из-за непрерывной работы
- Часть растущей экосистемы хуков Claude Code

## Подробнее
Grind решает конкретную проблему Claude Code: агент часто приостанавливается, чтобы задать уточняющие вопросы или объявляет о необходимости перерыва, даже когда задача чётко определена. Для разработчиков, запускающих ночные сборки или длительные сессии рефакторинга, это означает пробуждение с незавершённой задачей.

Хук перехватывает эти события паузы, оценивает, достигнута ли исходная цель, и если нет, генерирует новый запрос для продолжения. Он не обходит механизмы безопасности Claude Code — просто удерживает агента в фокусе на заявленной цели.

Пользователям следует быть осторожными с расходами. Непрерывная работа Claude Code в течение часов может быстро исчерпать лимиты подписки. Инструмент лучше всего подходит для чётко ограниченных задач с ясными критериями завершения.

## Примечательные цитаты
> «Предупреждение: может быстро израсходовать лимиты подписки.» — README

## Связанные записи
- [[ship-skills-claude-code-pipeline]] ([Ship Skills](../tools/ship-skills-claude-code-pipeline.md))
- [[claude-code]] ([Claude Code](../tools/claude-code.md))
