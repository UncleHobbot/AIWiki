---
title: "Claude Code Agentic Loop"
title_ru: "Агентный цикл Claude Code"
category: agents
tags: [claude-code, agentic-loop, context-window, tools, anthropic]
updated: 2026-05-16
sources:
  - https://code.claude.com/docs/en/how-claude-code-works
  - https://code.claude.com/docs/en/context-window
---

## Summary
Claude Code is an agentic assistant built on a three-phase loop — gather context, take action, verify results — powered by Claude models and a rich set of built-in tools.

## Key Ideas
- The agentic loop cycles through **gather context → take action → verify results** repeatedly until the task is complete; you can interrupt at any point.
- Claude Code is the **agentic harness** around Claude models: it provides tools, context management, and execution environment that turn a language model into a capable coding agent.
- Five tool categories give Claude agency: file operations, search, execution (shell/git), web access, and code intelligence (LSP, via plugins).
- The **context window** holds your conversation, file reads, command outputs, CLAUDE.md, auto memory, skill descriptions, and system instructions — all consuming tokens together.
- Claude compacts automatically when context fills, but instructions from early in conversation can be lost; put persistent rules in CLAUDE.md.
- Sessions are saved as JSONL files under `~/.claude/projects/`; resume with `claude --continue` or `claude --resume`.
- **Subagents** get their own isolated context window — delegating research to a subagent keeps your main conversation clean.

## Details
When you give Claude a task, it doesn't produce a single response. Instead it chains dozens of tool calls — reading files, editing code, running tests, checking results — adjusting course based on what each step reveals. A bug fix might cycle read→edit→test→read→edit multiple times before converging.

**What loads at session start:** CLAUDE.md files (project + user + org), auto memory (first 200 lines of MEMORY.md), MCP tool names (schemas deferred), skill descriptions. Each of these costs tokens before you type anything.

**Context management controls:** `/context` shows live breakdown by category; `/compact [focus]` compresses history; `/clear` resets entirely. Path-scoped rules (`.claude/rules/`) load only when matching files are opened, saving context. Skill bodies re-inject after compaction (capped at 5,000 tokens/skill, 25,000 total).

**What survives compaction:** system prompt, project-root CLAUDE.md, auto memory, invoked skill bodies (truncated). Path-scoped rules and nested CLAUDE.md files are lost until a matching file is read again.

## Related Entries
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))
- [[claude-code-memory]] ([Claude Code Memory: CLAUDE.md and Auto Memory](../agents/claude-code-memory.md))
- [[claude-code-permission-modes]] ([Claude Code Permission Modes](../agents/claude-code-permission-modes.md))
- [[how-coding-agents-read-code]] ([How AI Coding Agents Really Read Code (Inside the Runtime)](../agents/how-coding-agents-read-code.md))

---
<!-- RU -->

## Краткое описание
Claude Code — агентный ассистент, работающий по трёхфазному циклу: сбор контекста, выполнение действий, проверка результатов — с использованием моделей Claude и богатого набора встроенных инструментов.

## Ключевые идеи
- Агентный цикл повторяет фазы **сбор контекста → действие → проверка** до завершения задачи; вы можете прервать его в любой момент.
- Claude Code — это **агентная оболочка** вокруг моделей Claude: она предоставляет инструменты, управление контекстом и среду выполнения, превращающую языковую модель в полноценного кодового агента.
- Пять категорий инструментов: операции с файлами, поиск, выполнение команд (shell/git), веб-доступ и code intelligence (через плагины).
- **Окно контекста** содержит разговор, прочитанные файлы, вывод команд, CLAUDE.md, автопамять, описания навыков и системные инструкции — всё вместе потребляет токены.
- Claude автоматически уплотняет контекст при заполнении, но инструкции из начала разговора могут теряться — кладите постоянные правила в CLAUDE.md.
- Сессии сохраняются как JSONL-файлы в `~/.claude/projects/`; возобновление: `claude --continue` или `claude --resume`.
- **Подагенты** получают собственное изолированное окно контекста — делегирование исследований подагенту сохраняет чистоту основного разговора.

## Подробнее
Когда вы даёте Claude задание, он не возвращает единственный ответ. Вместо этого он выстраивает цепочки из десятков вызовов инструментов — читает файлы, редактирует код, запускает тесты, проверяет результаты — корректируя курс по итогам каждого шага. Исправление бага может несколько раз пройти цикл read→edit→test→read→edit до получения результата.

**Что загружается при старте сессии:** файлы CLAUDE.md (проектный + пользовательский + организационный), автопамять (первые 200 строк MEMORY.md), имена MCP-инструментов (схемы откладываются), описания навыков. Всё это стоит токенов ещё до первого сообщения.

**Управление контекстом:** `/context` показывает актуальную разбивку по категориям; `/compact [фокус]` сжимает историю; `/clear` сбрасывает полностью. Правила с указанием путей (`.claude/rules/`) загружаются только при открытии соответствующих файлов, экономя контекст.

**Что переживает уплотнение:** системный промпт, корневой CLAUDE.md проекта, автопамять, тела вызванных навыков (с ограничением 5 000 токенов/навык, 25 000 суммарно). Правила с привязкой к путям и вложенные CLAUDE.md теряются до повторного открытия соответствующих файлов.

## Связанные записи
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))
- [[claude-code-memory]] ([Claude Code Memory: CLAUDE.md and Auto Memory](../agents/claude-code-memory.md))
- [[claude-code-permission-modes]] ([Claude Code Permission Modes](../agents/claude-code-permission-modes.md))
- [[how-coding-agents-read-code]] ([How AI Coding Agents Really Read Code (Inside the Runtime)](../agents/how-coding-agents-read-code.md))
