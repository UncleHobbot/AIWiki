---
title: "Claude Code Extensions: Skills, MCP, Hooks, Subagents"
title_ru: "Расширения Claude Code: Skills, MCP, Hooks, Subagents"
category: agents
tags: [claude-code, skills, mcp, hooks, subagents, plugins, anthropic]
updated: 2026-05-16
sources:
  - https://code.claude.com/docs/en/features-overview
---

## Summary
Claude Code's extension layer lets you add persistent context (CLAUDE.md), reusable workflows (Skills), external service connections (MCP), isolated workers (Subagents), event automation (Hooks), and installable bundles (Plugins).

## Key Ideas
- **CLAUDE.md** — always-on context loaded every session; use for "always do X" rules, build commands, project conventions.
- **Skills** — markdown files with knowledge or workflows; descriptions load at session start, full content loads on demand; invoke with `/skill-name`.
- **MCP** — connects Claude to external services (databases, Slack, browser); gives Claude tools it wouldn't otherwise have.
- **Subagents** — isolated workers with their own context window; only the summary returns to your main session, keeping it clean.
- **Hooks** — deterministic scripts/HTTP/LLM/subagent triggered by lifecycle events (PostToolUse, SessionStart, etc.); guaranteed to fire unlike CLAUDE.md instructions.
- **Plugins** — bundle skills + hooks + subagents + MCP into one installable unit with namespaced commands (`/plugin:skill`).

## Details
**When to use each:**

| Trigger | Add |
|---|---|
| Claude gets something wrong twice | CLAUDE.md |
| You keep typing the same prompt | Save as a skill |
| You paste the same playbook repeatedly | Skill |
| Claude can't see data in a browser tab | MCP server |
| A side task floods your conversation | Subagent |
| Something must happen every time without asking | Hook |
| A second repo needs the same setup | Plugin |

**Key distinctions:**
- Skills add knowledge/workflows to Claude's context; subagents run work in isolation.
- CLAUDE.md loads every session automatically; skills load on demand.
- Hooks enforce behavior (a `PreToolUse` hook blocking `.env` writes is a guarantee); CLAUDE.md instructions are requests, not guarantees.
- Hook output lands back in context; hooks themselves consume zero context while idle.

**Context costs by feature:** CLAUDE.md (every request, full content), Skills (descriptions every request, body on use), MCP (tool names only until used), Subagents (isolated), Hooks (zero until output returned).

## Related Entries
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-code-directory]] ([The .claude Directory](../agents/claude-code-directory.md))
- [[claude-code-memory]] ([Claude Code Memory: CLAUDE.md and Auto Memory](../agents/claude-code-memory.md))
- [[claude-code-frameworks]] ([Claude Code Skill Frameworks: GSD, Superpowers, Ouroboros, Han](../tools/claude-code-frameworks.md))
- [[entire-platform]] ([Entire: Agent Session Checkpointing for Git](../tools/entire-platform.md))
- [[gnosis-mcp]] ([Gnosis MCP: Documentation Search Server for AI Agents](../tools/gnosis-mcp.md))
- [[mcp-financial-data-server]] ([Self-Hosted MCP Server for Financial Data](../tools/mcp-financial-data-server.md))
- [[agent-lifecycle-hooks-copilot-vscode]] ([Agent Lifecycle Hooks in Copilot CLI and Claude Code](../tips/agent-lifecycle-hooks-copilot-vscode.md))
- [[microsoft-waza]] ([Microsoft Waza: Agent Skill Evaluator](../tools/microsoft-waza.md))
---
<!-- RU -->

## Краткое описание
Слой расширений Claude Code позволяет добавлять постоянный контекст (CLAUDE.md), повторно используемые рабочие процессы (Skills), подключение внешних сервисов (MCP), изолированных работников (Subagents), автоматизацию событий (Hooks) и устанавливаемые пакеты (Plugins).

## Ключевые идеи
- **CLAUDE.md** — постоянный контекст, загружаемый в каждую сессию; используется для правил «всегда делай X», команд сборки, соглашений проекта.
- **Skills (навыки)** — markdown-файлы со знаниями или рабочими процессами; описания загружаются при старте сессии, полное содержание — по требованию; вызов через `/имя-навыка`.
- **MCP** — подключает Claude к внешним сервисам (базы данных, Slack, браузер); предоставляет инструменты, которых иначе у Claude нет.
- **Subagents (подагенты)** — изолированные работники с собственным окном контекста; в основную сессию возвращается только резюме, сохраняя чистоту контекста.
- **Hooks** — детерминированные скрипты/HTTP/LLM/подагент, срабатывающие по событиям жизненного цикла (PostToolUse, SessionStart и др.); гарантированно выполняются в отличие от инструкций CLAUDE.md.
- **Plugins** — пакеты из навыков + хуков + подагентов + MCP в одном устанавливаемом модуле с пространством имён (`/плагин:навык`).

## Подробнее
**Когда что использовать:**

| Триггер | Добавьте |
|---|---|
| Claude дважды ошибся в чём-то | CLAUDE.md |
| Вы снова и снова пишете один и тот же промпт | Навык |
| Вы трижды вставляли один и тот же чеклист | Навык |
| Claude не видит данные во вкладке браузера | MCP-сервер |
| Побочная задача затопляет ваш разговор выводом | Подагент |
| Что-то должно происходить каждый раз автоматически | Хук |
| Второй репозиторий нуждается в той же настройке | Плагин |

**Ключевые различия:**
- Навыки добавляют знания/процессы в контекст Claude; подагенты выполняют работу изолированно.
- CLAUDE.md загружается автоматически каждую сессию; навыки — по требованию.
- Хуки обеспечивают выполнение (хук PreToolUse, блокирующий запись в `.env` — это гарантия); инструкции CLAUDE.md — это просьба, а не гарантия.
- Вывод хука попадает обратно в контекст; сами хуки в простое не потребляют контекст.

**Стоимость контекста по типу расширения:** CLAUDE.md (каждый запрос, полностью), Skills (описания каждый запрос, тело при использовании), MCP (только имена инструментов до использования), Subagents (изолированы), Hooks (ноль до возврата вывода).

## Связанные записи
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-code-directory]] ([The .claude Directory](../agents/claude-code-directory.md))
- [[claude-code-memory]] ([Claude Code Memory: CLAUDE.md and Auto Memory](../agents/claude-code-memory.md))
- [[claude-code-frameworks]] ([Claude Code Skill Frameworks: GSD, Superpowers, Ouroboros, Han](../tools/claude-code-frameworks.md))
- [[entire-platform]] ([Entire: Agent Session Checkpointing for Git](../tools/entire-platform.md))
- [[gnosis-mcp]] ([Gnosis MCP: Documentation Search Server for AI Agents](../tools/gnosis-mcp.md))
- [[mcp-financial-data-server]] ([Self-Hosted MCP Server for Financial Data](../tools/mcp-financial-data-server.md))
- [[agent-lifecycle-hooks-copilot-vscode]] ([Agent Lifecycle Hooks in Copilot CLI and Claude Code](../tips/agent-lifecycle-hooks-copilot-vscode.md))
- [[microsoft-waza]] ([Microsoft Waza: Agent Skill Evaluator](../tools/microsoft-waza.md))
