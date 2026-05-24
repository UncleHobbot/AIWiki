---
title: "Git Worktrees with Claude Code: Parallel Isolated Feature Work"
title_ru: "Git Worktrees в Claude Code: параллельная изолированная разработка"
category: tips
tags: [claude-code, git-worktrees, parallel-development, workflow, isolation, EnterWorktree, ExitWorktree]
aliases: [git worktrees, EnterWorktree, ExitWorktree, worktree Claude Code, parallel Claude Code]
confidence: medium
date: 2026-05-24
updated: 2026-05-24
sources:
  - https://t.me/prog_ai
---

## Summary
Claude Code's built-in `EnterWorktree` and `ExitWorktree` tools let you create isolated git worktrees per feature, enabling true parallel development — separate Claude Code windows work on independent branches simultaneously without blocking each other.

## Key Ideas
- **Two built-in tools**: `EnterWorktree` — creates and enters an isolated worktree; `ExitWorktree` — exits the worktree (with option to save or delete the branch/worktree).
- **Location**: worktrees are created under `project/.claude/worktrees/...`.
- **No blocking**: when you commit or modify files in `main`, that branch is "locked" for git. Worktrees give each feature its own working directory, so branches never block each other.
- **Multiple Claude Code windows**: open one window per worktree — each works independently on its branch.
- **Typical use cases**:
  - Urgent bug fix while feature development is in progress
  - Running test writing in parallel with feature implementation
  - Developing multiple features simultaneously
- **Cleanup**: use the `commit-commands` plugin (`/commit-commands:clean_gone`) to delete branches that are in "gone" state — you cannot delete a branch while it is checked out in a worktree, so this command handles the order correctly.
- **Works with Superpowers**: `using-git-worktrees` is one of the 14 skills in the Superpowers plugin, integrating naturally with the subagent-driven workflow.

## Details
The standard git problem: when you switch branches, your working directory changes — and if you have uncommitted changes or open processes in Claude Code, you lose context. Worktrees solve this by giving each branch its own complete working directory on disk.

**Usage pattern**:
1. Ask Claude Code "Enter a new worktree" — it creates `project/.claude/worktrees/<branch>/`
2. Open a second Claude Code window pointed at that worktree path
3. Work on the feature in the new window; original window stays on `main`
4. When done, use `ExitWorktree` in the second window (save or delete)
5. Run `commit-commands:clean_gone` to remove stale gone branches

The key gotcha: a branch cannot be deleted while it is checked out in a worktree. The `clean_gone` command from the `commit-commands` plugin handles this automatically by detecting which branches are safe to remove.

For teams using the Superpowers plugin, the `using-git-worktrees` skill integrates with the `subagent-driven-development` skill — each subagent can work in its own worktree, then changes are merged back via the `finishing-a-development-branch` skill.

## Related Entries
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin](../agents/superpowers-plugin-claude-code.md))
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))

---
<!-- RU -->

## Краткое описание
Встроенные инструменты Claude Code `EnterWorktree` и `ExitWorktree` позволяют создавать изолированные git-ворктри для каждой фичи, обеспечивая настоящую параллельную разработку — отдельные окна Claude Code работают в независимых ветках одновременно без блокировок.

## Ключевые идеи
- **Два встроенных инструмента**: `EnterWorktree` — создаёт и входит в изолированный ворктри; `ExitWorktree` — выходит (с опцией сохранить или удалить ветку/ворктри).
- **Расположение**: ворктри создаются в `project/.claude/worktrees/...`.
- **Без блокировок**: у каждой фичи свой рабочий каталог — ветки никогда не блокируют друг друга.
- **Несколько окон Claude Code**: открывайте одно окно на ворктри — каждое работает независимо в своей ветке.
- **Типичные сценарии**: срочный баг-фикс во время работы над фичей; написание тестов параллельно с реализацией; разработка нескольких фич одновременно.
- **Очистка**: плагин `commit-commands` (`/commit-commands:clean_gone`) удаляет ветки в состоянии «gone» — нельзя удалить ветку, пока она checkout'нута в ворктри, поэтому команда обрабатывает порядок корректно.

## Подробнее
**Паттерн использования**:
1. Попросите Claude Code «Войди в новое ворктри» — он создаст `project/.claude/worktrees/<branch>/`
2. Откройте второе окно Claude Code, указав путь к ворктри
3. Работайте над фичей во втором окне; первое остаётся на `main`
4. Когда закончите — `ExitWorktree` во втором окне (сохранить или удалить)
5. Запустите `commit-commands:clean_gone` для удаления зависших веток

Для пользователей Superpowers: скилл `using-git-worktrees` интегрируется с `subagent-driven-development` — каждый субагент работает в своём ворктри, потом изменения сливаются через `finishing-a-development-branch`.

## Связанные записи
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin](../agents/superpowers-plugin-claude-code.md))
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
