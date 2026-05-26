---
title: "Yet Another Statusline (YAS): Claude Code Status Bar Tool"
title_ru: "Yet Another Statusline (YAS): строка статуса для Claude Code"
category: tools
tags: [claude-code, statusline, terminal, context-usage, subagents, open-source]
aliases: [YAS, yet-another-statusline, tmck-code statusline, Claude Code statusbar]
confidence: medium
date: 2026-05-25
updated: 2026-05-25
sources:
  - https://github.com/tmck-code/yet-another-statusline
  - https://www.reddit.com/r/ClaudeCode/comments/1tmdxu9/yet_another_statusline/
---

## Summary
Yet Another Statusline (YAS) is an open-source Claude Code status bar tool that displays context usage, token consumption, and subagent information in a persistent statusline. It is one of several community statusline implementations, distinguished by planned color theme support and detailed subagent visibility.

## Key Ideas
- **Displays**: context usage percentage, token counts, subagent status.
- **Color theme support** planned in upcoming releases.
- **Subagent info** displayed alongside main session stats.
- **Community pattern**: multiple independent statusline implementations exist for Claude Code (this is explicitly "yet another one"), reflecting strong community demand for context visibility.
- **Terminal-first**: designed for the terminal UI of Claude Code (not the VSCode extension, which has its own built-in status display).
- **Open source**: MIT licensed, available on GitHub at `github.com/tmck-code/yet-another-statusline`.

## Details
Context usage visibility is one of the most-requested quality-of-life features for Claude Code terminal users — knowing when the context window is filling up is critical for planning when to compact or start new sessions. YAS provides this at a glance in the statusline without requiring manual `/status` checks.

The community naming ("yet another") acknowledges a pattern: as Claude Code gained adoption, multiple developers independently built statusline tools. Each has slightly different trade-offs in what metrics to surface, visual style, and platform compatibility.

## Related Entries
- [[cate-canvas-ide]] ([Cate Canvas IDE](../tools/cate-canvas-ide.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
- [[claude-code-permission-modes]] ([Claude Code Permission Modes](../agents/claude-code-permission-modes.md))

---
<!-- RU -->

## Краткое описание
Yet Another Statusline (YAS) — open-source строка статуса для Claude Code, отображающая использование контекста, количество токенов и информацию о субагентах. Это одна из нескольких независимых реализаций statusline в сообществе, с запланированной поддержкой цветовых тем и детальным отображением субагентов.

## Ключевые идеи
- **Отображает**: процент заполнения контекста, количество токенов, статус субагентов.
- **Поддержка цветовых тем** запланирована в следующих версиях.
- **Паттерн сообщества**: несколько независимых реализаций statusline для Claude Code, отражающих высокий спрос на визуализацию контекста.
- **Для терминала**: предназначен для терминального UI Claude Code, не для расширения VSCode.
- **Open source**: MIT-лицензия, GitHub: `github.com/tmck-code/yet-another-statusline`.

## Подробнее
Видимость использования контекста — одна из наиболее востребованных функций для терминальных пользователей Claude Code: знать, когда контекстное окно заполняется, критически важно для планирования компакции или начала новых сессий. YAS предоставляет эту информацию в строке статуса без необходимости вручную вызывать `/status`.

## Связанные записи
- [[cate-canvas-ide]] ([Cate Canvas IDE](../tools/cate-canvas-ide.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
- [[claude-code-permission-modes]] ([Claude Code Permission Modes](../agents/claude-code-permission-modes.md))
