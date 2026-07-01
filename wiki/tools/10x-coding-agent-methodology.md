---
title: "10x — A Working Method for Coding Agents (SKILL.md)"
title_ru: "10x — рабочий метод для кодинг-агентов (SKILL.md)"
category: tools
tags: [skills, claude-code, methodology, agent-behavior, system-prompt]
aliases: [10x, z3z1ma 10x]
confidence: medium
updated: 2026-07-01
sources:
  - https://github.com/z3z1ma/10x
  - https://www.reddit.com/r/ClaudeCode/comments/1ukseeo/i_think_many_claude_code_setup_problems_are/
---

## Summary
10x is an open-source, single-file Markdown methodology (`SKILL.md`) the author drops into coding agents. Its thesis: most "tooling" problems with coding agents are actually behavior problems — fix the agent's working method before adding another MCP server.

## Key Ideas
- **One file, plain Markdown**, shared as a skill across coding agents — no runtime required.
- Behaviors it enforces:
  - Challenge vague work before coding.
  - Separate discovery from execution.
  - Preserve durable repo context in `.10x/`.
  - Treat subagent output as claims, not truth.
  - Prove changes with evidence.
  - Leave a trail the next session can use.
- Includes an `autoresearch/` "lab" folder for testing and hill-climbing desirable agent behaviors — explicitly not the product.
- Philosophy: before reaching for another tool, give the agent a method.

## Details
The skill reframes agent setup as a behavioral problem. Rather than expanding the tool surface, it constrains how the agent operates: it must justify work, separate exploration from action, and persist context so a fresh session inherits prior findings. The `.10x/` directory acts as durable agent memory within the repo itself.

## Related Entries
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin](../agents/superpowers-plugin-claude-code.md))
- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))
- [[ship-skills-claude-code-pipeline]] ([Ship Skills](../tools/ship-skills-claude-code-pipeline.md))

---
<!-- RU -->

## Краткое описание
10x — открытая однофайловая методология на Markdown (`SKILL.md`), которую автор подключает к кодинг-агентам. Тезис: большинство «проблем с инструментами» у кодинг-агентов — на самом деле проблемы поведения; чините рабочий метод агента, прежде чем добавлять очередной MCP-сервер.

## Ключевые идеи
- **Один файл, обычный Markdown**, используется как skill в разных кодинг-агентах.
- Поведения, которые он закрепляет:
  - Уточнять размытую задачу до написания кода.
  - Разделять обнаружение (discovery) и выполнение (execution).
  - Сохранять устойчивый контекст репозитория в `.10x/`.
  - Считать вывод сабагентов утверждением, а не истиной.
  - Подтверждать изменения доказательствами.
  - Оставлять след, пригодный для следующей сессии.
- Включает папку `autoresearch/` — «лабораторию» для тестирования и улучшения желаемых поведений; это не продукт.
- Философия: прежде чем тянуться к новому инструменту, дайте агенту метод.

## Подробнее
Skill переформулирует настройку агента как поведенческую задачу: не расширяя поверхность инструментов, он ограничивает, как агент действует — обязан обосновывать работу, разделять исследование и действие, сохранять контекст, чтобы новая сессия наследовала найденное. Папка `.10x/` выступает устойчивой памятью агента внутри репозитория.

## Связанные записи
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin](../agents/superpowers-plugin-claude-code.md))
- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))
- [[ship-skills-claude-code-pipeline]] ([Ship Skills](../tools/ship-skills-claude-code-pipeline.md))
