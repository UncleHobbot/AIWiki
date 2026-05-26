---
title: ".NET Agent Skills: Microsoft's Official Skills for AI Coding Agents"
title_ru: ".NET Agent Skills: официальные навыки Microsoft для AI-агентов программирования"
category: tools
tags: [dotnet, microsoft, agent-skills, copilot, claude-code, csharp]
confidence: high
updated: 2026-05-26
sources:
  - https://github.com/dotnet/skills
  - https://x.com/iammukeshm/status/2057000917086478356
---

## Summary
Microsoft's official .NET Agent Skills repository provides 14 curated plugin packages that AI coding agents (Copilot CLI, Claude Code, Cursor, Codex) load on demand for consistent, high-quality .NET development across ASP.NET Core, Blazor, MAUI, EF, diagnostics, and more.

## Key Ideas
- 14 specialized skill plugins covering the full .NET ecosystem: core .NET, data/EF, diagnostics, MSBuild, NuGet, upgrade/migration, MAUI, AI/ML, template engine, testing, ASP.NET Core, Blazor, and .NET 11 features
- Follows the agentskills.io open standard — compatible with Copilot CLI, Claude Code, VS Code Copilot, Cursor, and OpenAI Codex
- Installation via marketplace: `/plugin marketplace add dotnet/skills` then `/plugin install <plugin>@dotnet-agent-skills`
- Includes a dashboard tracking accuracy and efficiency scoring trends for each plugin
- Solves the "prompt from scratch every time" problem: knowledge lives in the repo, agents load what they need, code stays consistent across the team

## Details
The .NET team at Microsoft open-sourced their internal skills repository in May 2026, bringing the same "skills as code" approach that won in the Claude Code and Cursor communities to the .NET ecosystem. Each plugin contains structured knowledge about its domain — not just examples, but decision trees, common pitfalls, and idiomatic patterns that the .NET team has refined internally.

The key insight is that most AI prompts in .NET projects get written from scratch every time: same context, same examples, same patterns. Skills flip this by making knowledge persistent and loadable. The `dotnet-ai` plugin alone covers technology selection, LLM integration, agentic workflows, RAG pipelines, MCP, and classic ML with ML.NET — essentially a senior .NET AI engineer's brain in a loadable package.

## Related Entries
- [[dotnet-claude-kit]] ([dotnet-claude-kit](../tools/dotnet-claude-kit.md))
- [[awesome-agent-skills]] ([Awesome Agent Skills](../tools/awesome-agent-skills.md))
- [[mattpocock-skills-repo]] ([Matt Pocock](../tools/mattpocock-skills-repo.md))
- [[claude-code-frameworks]] ([Claude Code Frameworks](../tools/claude-code-frameworks.md))

---
<!-- RU -->

## Краткое описание
Официальный репозиторий .NET Agent Skills от Microsoft предоставляет 14 кураторских пакетов плагинов, которые AI-агенты программирования (Copilot CLI, Claude Code, Cursor, Codex) загружают по требованию для согласованной и качественной .NET-разработки.

## Ключевые идеи
- 14 специализированных плагинов покрывают всю экосистему .NET: базовый .NET, данные/EF, диагностика, MSBuild, NuGet, миграции, MAUI, AI/ML, шаблонизатор, тестирование, ASP.NET Core, Blazor и новые возможности .NET 11
- Следует открытому стандарту agentskills.io — совместим с Copilot CLI, Claude Code, VS Code Copilot, Cursor и OpenAI Codex
- Установка через маркетплейс: `/plugin marketplace add dotnet/skills`, затем `/plugin install <plugin>@dotnet-agent-skills`
- Включает дашборд для отслеживания тенденций точности и эффективности каждого плагина
- Решает проблему «промпт с нуля каждый раз»: знания хранятся в репозитории, агенты загружают нужное, код остаётся согласованным в команде

## Подробнее
Команда .NET в Microsoft открыла свой внутренний репозиторий навыков в мае 2026 года, принеся подход «skills as code», который завоевал популярность в сообществах Claude Code и Cursor, в экосистему .NET. Каждый плагин содержит структурированные знания о своей предметной области — не только примеры, но и деревья решений, типичные ошибки и идиоматичные паттерны, которые команда .NET отточила внутри компании.

Ключевая идея: большинство AI-промптов в .NET-проектах пишутся с нуля каждый раз — один и тот же контекст, примеры и паттерны. Навыки меняют это, делая знания постоянными и загружаемыми. Только плагин `dotnet-ai` покрывает выбор технологий, интеграцию LLM, агентные рабочие процессы, RAG-пайплайны, MCP и классическое ML с ML.NET — по сути, опыт senior .NET AI-инженера в загружаемом пакете.

## Связанные записи
- [[dotnet-claude-kit]] ([dotnet-claude-kit](../tools/dotnet-claude-kit.md))
- [[awesome-agent-skills]] ([Awesome Agent Skills](../tools/awesome-agent-skills.md))
- [[mattpocock-skills-repo]] ([Matt Pocock](../tools/mattpocock-skills-repo.md))
- [[claude-code-frameworks]] ([Claude Code Frameworks](../tools/claude-code-frameworks.md))
