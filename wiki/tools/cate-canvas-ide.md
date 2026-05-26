---
title: "Cate: Canvas IDE for Claude Code Workflows"
title_ru: "Cate: canvas-рабочее пространство для воркфлоу Claude Code"
category: tools
tags: [claude-code, ide, canvas, workspace, terminals, git-worktrees, open-source, mit]
aliases: [Cate IDE, CATE canvas, cate cero-ai]
confidence: medium
date: 2026-05-25
updated: 2026-05-25
sources:
  - https://github.com/0-AI-UG/cate
  - https://www.reddit.com/r/ClaudeCode/comments/1tmjpbt/using_claude_code_inside_a_cate_figma_like_canvas/
---

## Summary
Cate is an open-source desktop workspace that places Claude Code on a persistent canvas alongside terminals, browser previews, documentation, and git branches — solving the context-switching friction of managing multiple windows during agentic development sessions.

## Key Ideas
- **Persistent canvas**: combine Claude Code terminal, dev server terminal, browser preview, docs/issues, and file editor into a single persistent layout that can be restored later.
- **Problem solved**: agentic coding workflows generate 4-6 tool windows (agent terminal, server terminal, browser preview, docs, files, multiple branches/worktrees) — Cate puts them all on one canvas.
- **Use cases**: multi-terminal Claude Code setups, workflows needing browser preview alongside the agent, multi-branch or git worktree setups.
- **Open source, MIT licensed**: free to use and extend; website at `cate.cero-ai.com`.
- **Not a built-in agent**: Cate is a workspace shell — it hosts Claude Code (CLI) rather than replacing it.

## Details
The core value proposition is persistent visual context. When you return to a task the next day, a normal terminal setup requires you to reopen terminals, restart the dev server, navigate back to docs, and remember which branches you had open. Cate restores the entire layout in one step.

It is analogous to a spatial IDE concept (like Figma's canvas, but for developer workflows) — Claude Code runs in a terminal tile on the canvas, adjacent to whatever context it needs. Users can also run other harnesses that support CLI input (e.g., "oh-my-claude type harnesses" per community questions).

The tool is early-stage and MIT licensed; the developer has signaled intent to add color theme support and better subagent layout visualization.

## Related Entries
- [[using-git-worktrees-claude-code]] ([Git Worktrees in Claude Code](../tips/using-git-worktrees-claude-code.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin](../agents/superpowers-plugin-claude-code.md))

---
<!-- RU -->

## Краткое описание
Cate — открытое десктопное рабочее пространство, которое размещает Claude Code на постоянном canvas вместе с терминалами, браузерным превью, документацией и git-ветками, решая проблему переключения контекста при агентных сессиях разработки.

## Ключевые идеи
- **Постоянный canvas**: объедините терминал Claude Code, терминал dev-сервера, браузерный превью, документацию и редактор файлов в один постоянный макет, восстанавливаемый при следующем запуске.
- **Решаемая проблема**: агентные воркфлоу генерируют 4-6 окон инструментов — Cate размещает их все на одном canvas.
- **Сценарии использования**: многотерминальные сетапы Claude Code, воркфлоу с браузерным превью рядом с агентом, мультибранч- и git-worktree-сетапы.
- **Open source, MIT**: бесплатно, расширяемо; сайт: `cate.cero-ai.com`.
- **Не встроенный агент**: Cate — оболочка рабочего пространства, хостит Claude Code (CLI), а не заменяет его.

## Подробнее
Ключевая ценность — постоянный визуальный контекст. Когда вы возвращаетесь к задаче на следующий день, стандартный терминальный сетап требует заново открыть терминалы, перезапустить dev-сервер, вернуться к документации и вспомнить активные ветки. Cate восстанавливает весь макет одним действием.

Инструмент находится на ранней стадии разработки, MIT-лицензирован.

## Связанные записи
- [[using-git-worktrees-claude-code]] ([Git Worktrees in Claude Code](../tips/using-git-worktrees-claude-code.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin](../agents/superpowers-plugin-claude-code.md))
