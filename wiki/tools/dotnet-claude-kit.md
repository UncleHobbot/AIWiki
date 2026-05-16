---
title: "dotnet-claude-kit"
title_ru: "dotnet-claude-kit"
category: tools
tags: [claude-code, dotnet, csharp, plugins, skills, mcp, roslyn]
updated: 2026-05-16
sources:
  - https://github.com/codewithmukesh/dotnet-claude-kit
---

## Summary
A curated knowledge and action layer that turns Claude Code into a senior .NET 10 / C# 14 expert — includes 47 skills, 10 specialist agents, 16 slash commands, 10 rules, 5 project templates, and 15 Roslyn-powered MCP tools.

## Key Ideas
- Drop a single `CLAUDE.md` into your repo (or install via `/plugin marketplace add codewithmukesh/dotnet-claude-kit`) and Claude instantly knows .NET conventions, modern C# 14 patterns, and architecture best practices.
- Roslyn MCP tools let Claude navigate your codebase via semantic queries (30–150 tokens each) instead of reading whole files (500–2000+ tokens each) — roughly 10× token savings on exploration.
- Includes an interactive setup flow: Claude asks architecture questions (VSA, Clean Architecture, DDD, Modular Monolith) and generates a customized `CLAUDE.md` for greenfield or existing projects.
- Enforces modern patterns automatically: `TimeProvider` instead of `DateTime.Now`, direct `DbContext` instead of repository wrappers, `WebApplicationFactory + Testcontainers` instead of in-memory fakes.
- Six hooks run automatically: format-on-edit, anti-pattern checks on commit, test result analysis, structure validation.

## Details
Out of the box, Claude Code doesn't know your .NET conventions. It generates `DateTime.Now`, wraps EF Core in unnecessary repository abstractions, and reads entire source files for context. `dotnet-claude-kit` fixes this by adding an architecture-aware, token-efficient knowledge layer.

The action layer (v0.4.0+) goes beyond knowledge: slash commands like `/scaffold` generate complete features with the Result pattern, FluentValidation, OpenAPI metadata, pagination, `CancellationToken`, and tests in one shot. `/health-check` runs an automated codebase analysis and returns a graded report card. `/code-review` performs a multi-dimensional MCP-powered review across anti-patterns, diagnostics, API surface changes, and test coverage.

The kit also includes a "Convention Learning" capability: Claude detects project-specific naming and structure patterns and enforces them in new code.

## Notable Quotes
> "Less time reviewing and correcting Claude's output. More time shipping features." — README

## Related Entries
- [[claude-code-plugins-guide]]
- [[claude-code-extensions-overview]]

---
<!-- RU -->

## Краткое описание
Слой знаний и действий, превращающий Claude Code в старшего .NET 10 / C# 14 разработчика — включает 47 навыков, 10 специализированных агентов, 16 slash-команд, 10 правил, 5 шаблонов проектов и 15 MCP-инструментов на основе Roslyn.

## Ключевые идеи
- Достаточно добавить один `CLAUDE.md` в репозиторий (или установить плагин через `/plugin marketplace add codewithmukesh/dotnet-claude-kit`) — Claude сразу начинает следовать .NET-соглашениям и паттернам C# 14.
- MCP-инструменты на основе Roslyn позволяют Claude анализировать код через семантические запросы (30–150 токенов), а не читать целые файлы (500–2000+ токенов) — примерно 10× экономия токенов.
- Интерактивный мастер настройки: Claude задаёт вопросы об архитектуре (VSA, Clean Architecture, DDD, Modular Monolith) и генерирует кастомизированный `CLAUDE.md`.
- Автоматически применяет современные паттерны: `TimeProvider` вместо `DateTime.Now`, прямой `DbContext` вместо репозиториев, `WebApplicationFactory + Testcontainers` вместо моков.
- Шесть хуков работают автоматически: форматирование при редактировании, проверка антипаттернов при коммите, анализ результатов тестов.

## Подробнее
Claude Code без настройки не знает .NET-конвенций: генерирует устаревшие паттерны и читает целые файлы для контекста. `dotnet-claude-kit` добавляет архитектурно-осознанный, токено-эффективный слой знаний поверх Claude.

Слой действий (v0.4.0+): команда `/scaffold` генерирует полный feature-файл с паттерном Result, FluentValidation, метаданными OpenAPI, пагинацией, `CancellationToken` и тестами. `/health-check` анализирует кодовую базу и возвращает оценки по категориям (A–F). `/code-review` выполняет многоуровневое ревью через MCP: антипаттерны, диагностика, API-изменения, покрытие тестами.

Функция «Convention Learning» обнаруживает специфичные для проекта паттерны именования и структуры и применяет их в новом коде.

## Примечательные цитаты
> «Меньше времени на ревью и исправление вывода Claude. Больше времени на разработку фич.» — README

## Связанные записи
- [[claude-code-plugins-guide]]
- [[claude-code-extensions-overview]]
