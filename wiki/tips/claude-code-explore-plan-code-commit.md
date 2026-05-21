---
title: "The Explore → Plan → Code → Commit Workflow in Claude Code"
title_ru: "Рабочий процесс Explore → Plan → Code → Commit в Claude Code"
category: tips
tags: [claude-code, workflow, plan-mode, agentic-coding, best-practices, explore, commit]
aliases: [Explore Plan Code Commit, Claude Code workflow, plan mode workflow, 4-step Claude workflow]
confidence: high
date: 2026-05-21
updated: 2026-05-21
sources:
  - https://www.youtube.com/watch?v=xJQuF02NAK8
---

## Summary

Anthropic's official recommended workflow for Claude Code is a four-step loop — Explore, Plan, Code, Commit — designed to prevent the most common failure mode: jumping straight to code generation without sufficient planning, which leads to expensive course corrections later.

## Key Ideas

- **Explore first, code last.** Most developers jump straight to asking Claude to write code. The correct entry point is exploration — understanding the codebase before proposing solutions.
- **Plan mode = read-only research.** Use `Shift+Tab` to enter plan mode. In plan mode, Claude *cannot* edit files — it only reads them to gather research and produce a plan of action. This is the safest phase to check Claude's understanding.
- **Course-correct before any code is written.** The plan phase is "the best place to course correct" — reviewing and revising the plan costs nothing. Once code is written, corrections are expensive.
- **Approve to proceed.** After reviewing the plan, select "Approve" to transition Claude to execution mode. You can choose whether Claude auto-accepts edits or asks permission for each file change.
- **Explore without plan mode.** You can also ask Claude to explore the codebase without entering plan mode — simply ask it to read and describe the relevant area before you pose the implementation question.

## Video Notes

From Anthropic's official YouTube channel (May 17, 2026). Short instructional clip demonstrating the workflow end-to-end with a real example: adding WebP conversion to an image upload pipeline.

**Step-by-step:**
1. `Shift+Tab` → enter plan mode
2. Ask Claude to explore the relevant area: *"Figure out where in the pipeline [X] should happen, whether we need new dependencies, and how to approach it."*
3. Claude reads files, optionally searches the web, returns a structured plan
4. Review and revise the plan until it meets your criteria
5. Approve → Claude executes, committing once complete

**Why this matters:** the four-step structure mirrors the same discipline as TDD — making explicit the boundary between "understanding" and "doing." Claude in plan mode cannot hallucinate a change; it can only hallucinate a proposed approach, which is much cheaper to catch and correct.

## Related Entries

- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[test-driven-agentic-behaviours]] ([Test-Driven Agentic Behaviours](../tips/test-driven-agentic-behaviours.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development](../tips/spec-driven-development-bmad.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows Best Practices](../tips/claude-code-workflows-best-practices.md))

---
<!-- RU -->

## Краткое описание

Официальный рекомендованный рабочий процесс Anthropic для Claude Code — четырёхшаговый цикл: Explore → Plan → Code → Commit. Он создан для предотвращения самой распространённой ошибки: прямого перехода к генерации кода без достаточного планирования, что приводит к дорогостоящим исправлениям позже.

## Ключевые идеи

- **Сначала исследование, код — в конце.** Большинство разработчиков сразу просят Claude писать код. Правильная точка входа — исследование: понять кодовую базу до предложения решений.
- **Режим плана = чтение без изменений.** `Shift+Tab` для входа в режим плана. В этом режиме Claude *не может* редактировать файлы — только читает их для исследования и создания плана действий.
- **Корректировка до написания кода.** Фаза планирования — «лучшее место для корректировки»: правки плана ничего не стоят. После написания кода исправления дороги.
- **Одобрить для перехода к выполнению.** После проверки плана нажмите «Approve» для перехода Claude в режим выполнения. Можно выбрать: автоматически принимать правки файлов или подтверждать каждую.
- **Исследование без режима плана.** Можно попросить Claude исследовать кодовую базу без входа в режим плана — просто попросить прочитать и описать нужную область.

## Заметки по видео

Официальный канал Anthropic на YouTube (17 мая 2026). Короткий обучающий клип с примером: добавление конвертации WebP в пайплайн загрузки изображений.

**Пошагово:**
1. `Shift+Tab` → режим плана
2. Попросите Claude исследовать нужную область
3. Claude читает файлы, предлагает структурированный план
4. Проверьте и скорректируйте план
5. Одобрите → Claude выполняет и коммитит

## Связанные записи

- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[test-driven-agentic-behaviours]] ([Test-Driven Agentic Behaviours](../tips/test-driven-agentic-behaviours.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development](../tips/spec-driven-development-bmad.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows Best Practices](../tips/claude-code-workflows-best-practices.md))
