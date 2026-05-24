---
title: "Superpowers Plugin for Claude Code: Structured Agentic Workflow Skills"
title_ru: "Плагин Superpowers для Claude Code: структурированные скиллы агентного воркфлоу"
category: agents
tags: [claude-code, superpowers, plugin, skills, workflow, subagent, planning, tdd, code-review]
aliases: [superpowers, orba/superpowers, superpowers plugin, Claude Code superpowers]
confidence: medium
date: 2026-05-24
updated: 2026-05-24
sources:
  - https://t.me/prog_ai/1005
---

## Summary
The Superpowers plugin (`orba/superpowers`) extends Claude Code with a structured pipeline of workflow skills: brainstorm → write plan → execute plan, with subagent-driven development as the recommended execution mode. It provides 14 reusable skills covering the full development lifecycle from spec to branch completion.

## Key Ideas
- **Structured pipeline**: the plugin chains skills automatically — brainstorming writes a spec to `docs/superpowers/specs/`, writing-plans produces an execution plan, executing-plans (or subagent-driven-development) implements it.
- **Two execution modes**: *subagent-driven* (recommended) — one dedicated agent per task, cross-task review, fast iteration; *inline execution* — runs in the current session with checkpoints.
- **Subagent-driven development** spawns a separate agent for each task and runs `receiving-code-review` between tasks automatically.
- **14 skills** in the plugin (current version):
  - `using-superpowers` — introductory skill, explains how to discover other skills
  - `brainstorming` — turns an idea into a design through dialogue, writes spec
  - `writing-plans` — creates a detailed implementation plan from the spec
  - `executing-plans` — executes plan in the current session with checkpoints
  - `subagent-driven-development` — executes plan via subagents with two-stage review
  - `dispatching-parallel-agents` — launches independent tasks in parallel
  - `test-driven-development` — TDD workflow for subagents when implementing features
  - `systematic-debugging` — systematic debugging: analysis, tracing, fix
  - `requesting-code-review` — template for submitting code for review
  - `receiving-code-review` — handling review feedback before applying changes
  - `verification-before-completion` — verify before claiming the task is done
  - `writing-skills` — create and edit skill files themselves
  - `finishing-a-development-branch` — finalize branch: tests, PR, merge
  - `using-git-worktrees` — isolated work via git worktrees
- **Deprecated commands** (removed in next major version): `write-plan` → `writing-plans`, `execute-plan` → `executing-plans`, `brainstorm` → `brainstorming`.
- **Known gap**: no automatic post-execution plan verification step — community feedback suggests adding a check that the agent actually implemented everything the plan specified.

## Details
The plugin is installed from the official Claude Code plugin registry (listed first in `/plugins`). Once installed, it augments the standard `/plan` flow: where Claude Code normally just plans, Superpowers adds the brainstorming spec and the full structured pipeline.

The subagent-driven mode is particularly powerful for multi-task plans: each task runs in isolation with full context, preventing earlier tasks from contaminating later ones. The two-stage code review (after each task, and at branch finalization) catches regressions before they accumulate.

The `finishing-a-development-branch` skill closes the loop: after all tasks are complete, it runs tests, creates the PR, and optionally merges. This makes the entire flow from idea to merged PR something Claude Code can handle with minimal human intervention.

## Related Entries
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
- [[using-git-worktrees-claude-code]] ([Git Worktrees in Claude Code](../tips/using-git-worktrees-claude-code.md))
- [[acdc-agent-centric-development-cycle]] ([AC/DC Development Cycle](../agents/acdc-agent-centric-development-cycle.md))

---
<!-- RU -->

## Краткое описание
Плагин Superpowers (`orba/superpowers`) расширяет Claude Code структурированным конвейером скиллов: брейнсторминг → написание плана → выполнение, с режимом subagent-driven development как рекомендуемым способом выполнения. Предоставляет 14 переиспользуемых скиллов для полного цикла разработки от спеки до финализации ветки.

## Ключевые идеи
- **Структурированный конвейер**: плагин автоматически соединяет скиллы — brainstorming пишет спеку в `docs/superpowers/specs/`, writing-plans создаёт план выполнения, executing-plans (или subagent-driven-development) реализует его.
- **Два режима выполнения**: *subagent-driven* (рекомендуется) — отдельный агент на каждую задачу, ревью между задачами, быстрая итерация; *inline execution* — выполнение в текущей сессии с чекпоинтами.
- **14 скиллов** в плагине (текущая версия): using-superpowers, brainstorming, writing-plans, executing-plans, subagent-driven-development, dispatching-parallel-agents, test-driven-development, systematic-debugging, requesting-code-review, receiving-code-review, verification-before-completion, writing-skills, finishing-a-development-branch, using-git-worktrees.
- **Устаревшие команды**: `write-plan` → `writing-plans`, `execute-plan` → `executing-plans`, `brainstorm` → `brainstorming`.
- **Известный пробел**: отсутствует автоматическая постпроверка реализации плана — комьюнити указывает, что не хватает шага, проверяющего полноту выполнения.

## Подробнее
Плагин устанавливается из официального реестра плагинов Claude Code (первый в списке `/plugins`). После установки он дополняет стандартный поток `/plan`: добавляет брейнсторминг со спекой и полный структурированный конвейер.

Режим subagent-driven особенно эффективен для многозадачных планов: каждая задача выполняется изолированно с полным контекстом, двухэтапное ревью ловит регрессии до их накопления.

Скилл `finishing-a-development-branch` замыкает цикл: после завершения всех задач запускает тесты, создаёт PR и опционально выполняет merge.

## Связанные записи
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
- [[using-git-worktrees-claude-code]] ([Git Worktrees in Claude Code](../tips/using-git-worktrees-claude-code.md))
- [[acdc-agent-centric-development-cycle]] ([AC/DC Development Cycle](../agents/acdc-agent-centric-development-cycle.md))
