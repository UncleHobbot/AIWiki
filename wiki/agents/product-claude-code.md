---
title: "Claude Code"
title_ru: "Claude Code"
category: agents
tags: [claude-code, anthropic, coding-agent, cli]
aliases: [Claude Code, claude-code]
updated: 2026-05-26
sources:
  - https://code.claude.com/docs/en/how-claude-code-works
---

## Summary
Claude Code is Anthropic's agentic coding assistant that runs in the terminal, built on a three-phase loop of gathering context, taking action, and verifying results. It supports skills, MCP, hooks, subagents, and persistent memory via CLAUDE.md.

## Core Entries
- [[claude-code-agentic-loop]] ([Agentic Loop](../agents/claude-code-agentic-loop.md)) — Three-phase loop: gather context, act, verify
- [[claude-code-directory]] ([The .claude Directory](../agents/claude-code-directory.md)) — Configuration hierarchy: CLAUDE.md, skills, hooks, agents
- [[claude-code-extensions-overview]] ([Extensions](../agents/claude-code-extensions-overview.md)) — Skills, MCP, hooks, subagents
- [[claude-code-memory]] ([Memory](../agents/claude-code-memory.md)) — CLAUDE.md and auto memory systems
- [[claude-code-permission-modes]] ([Permission Modes](../agents/claude-code-permission-modes.md)) — Ask, auto-accept, and custom modes

## Tips and Best Practices
- [[claude-code-workflows-best-practices]] ([Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[claude-code-12-setup-tricks]] ([12 Setup Tricks](../tips/claude-code-12-setup-tricks.md))
- [[claude-code-9-mistakes-wasting-tokens]] ([9 Mistakes That Waste Tokens](../tips/claude-code-9-mistakes-wasting-tokens.md))
- [[claude-code-prompting-era]] ([New Prompting Era](../tips/claude-code-prompting-era.md))
- [[claude-code-deferral-behavior]] ([Deferral Behavior](../tips/claude-code-deferral-behavior.md))
- [[claude-code-explore-plan-code-commit]] ([Explore → Plan → Code → Commit](../tips/claude-code-explore-plan-code-commit.md))
- [[karpathy-claude-code-guidelines]] ([Karpathy-Inspired Guidelines](../tips/karpathy-claude-code-guidelines.md))
- [[claude-usage-limits-token-management]] ([10 Ways to Stop Hitting Limits](../tips/claude-usage-limits-token-management.md))
- [[using-git-worktrees-claude-code]] ([Git Worktrees](../tips/using-git-worktrees-claude-code.md))

## Plugins and Frameworks
- [[claude-code-frameworks]] ([Skill Frameworks](../tools/claude-code-frameworks.md)) — GSD, Superpowers, Ouroboros, Han
- [[claude-code-plugins-guide]] ([Plugins Guide: Top 36](../tips/claude-code-plugins-guide.md))
- [[claude-code-handoff-prototype-skills]] ([Skills: /handoff, /prototype](../tips/claude-code-handoff-prototype-skills.md))
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin](../agents/superpowers-plugin-claude-code.md))
- [[han-claude-code-plugin]] ([Han Plugin](../tools/han-claude-code-plugin.md))
- [[dotnet-claude-kit]] ([dotnet-claude-kit](../tools/dotnet-claude-kit.md))
- [[dotnet-agent-skills]] ([.NET Agent Skills](../tools/dotnet-agent-skills.md))

## News
- [[claude-code-remote-system-prompt-injection]] ([Remote Prompt Injection](../news/claude-code-remote-system-prompt-injection.md))
- [[claude-code-usage-reset-may-2026]] ([Usage Reset](../news/claude-code-usage-reset-may-2026.md))

---
<!-- RU -->

## Краткое описание
Claude Code — агент программирования от Anthropic, работающий в терминале. Построен на трёхфазном цикле: сбор контекста, выполнение действия, проверка результатов. Поддерживает навыки, MCP, хуки, субагенты и постоянную память через CLAUDE.md.

## Основные записи
- [[claude-code-agentic-loop]] — Трёхфазный цикл: собрать контекст, действовать, проверить
- [[claude-code-directory]] — Иерархия конфигурации: CLAUDE.md, навыки, хуки, агенты
- [[claude-code-extensions-overview]] — Навыки, MCP, хуки, субагенты
- [[claude-code-memory]] — Системы CLAUDE.md и авто-памяти
- [[claude-code-permission-modes]] — Режимы Ask, auto-accept и пользовательские

## Советы и лучшие практики
- [[claude-code-workflows-best-practices]] — Рабочие процессы и лучшие практики
- [[claude-code-12-setup-tricks]] — 12 трюков настройки
- [[claude-code-9-mistakes-wasting-tokens]] — 9 ошибок, тратящих токены
- [[claude-code-prompting-era]] — Новая эра промптинга
- [[claude-code-deferral-behavior]] — Поведение откладывания задач
- [[claude-code-explore-plan-code-commit]] — Explore → Plan → Code → Commit
- [[karpathy-claude-code-guidelines]] — Руководства в стиле Карпатого
- [[claude-usage-limits-token-management]] — 10 способов перестать упираться в лимиты
- [[using-git-worktrees-claude-code]] — Git worktrees

## Плагины и фреймворки
- [[claude-code-frameworks]] — Фреймворки навыков: GSD, Superpowers, Ouroboros, Han
- [[claude-code-plugins-guide]] — Гид по плагинам: топ-36
- [[claude-code-handoff-prototype-skills]] — Навыки: /handoff, /prototype
- [[superpowers-plugin-claude-code]] — Плагин Superpowers
- [[han-claude-code-plugin]] — Плагин Han
- [[dotnet-claude-kit]] — dotnet-claude-kit
- [[dotnet-agent-skills]] — .NET Agent Skills

## Новости
- [[claude-code-remote-system-prompt-injection]] — Удалённая инъекция системного промпта
- [[claude-code-usage-reset-may-2026]] — Сброс лимитов использования
