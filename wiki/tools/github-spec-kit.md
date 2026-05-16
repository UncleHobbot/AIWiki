---
title: "GitHub Spec-Kit: Spec-Driven Development Toolkit"
title_ru: "GitHub Spec-Kit: инструментарий для спецификационной разработки"
category: tools
tags: [spec-driven-development, github, cli, claude-code, codex, ai-coding, workflow]
updated: 2026-05-16
sources:
  - https://github.com/github/spec-kit
---

## Summary
GitHub Spec-Kit is an open-source CLI toolkit (`specify-cli`) for Spec-Driven Development — a structured workflow where executable specifications drive implementation, replacing vibe coding with a reproducible multi-step process of constitution → spec → plan → tasks → implement.

## Key Ideas
- Core philosophy: specifications are executable, not discarded scaffolding. The `what` and `why` are defined first, then the `how` is generated from them by AI.
- Five-command core workflow: `/speckit.constitution` (governing principles) → `/speckit.specify` (requirements) → `/speckit.plan` (tech stack + architecture) → `/speckit.tasks` (actionable task list) → `/speckit.implement` (build it)
- Supports 30+ AI coding agents: Claude Code, Codex CLI, Gemini CLI, Cursor, Copilot, OpenCode, Windsurf, Pi, and more — integrates via slash commands or agent skills depending on the harness.
- Extensible through community **extensions** (add new commands/workflows) and **presets** (customize spec/plan/task templates) that stack with priority ordering.
- Works for greenfield projects (0-to-1), iterative enhancement (brownfield modernization), and creative exploration (parallel implementations across different stacks).

## Details
Install via `uv tool install specify-cli` from the GitHub releases. After `specify init my-project --integration copilot` (or whatever agent), the AI coding agent gains access to spec-kit slash commands directly.

**The workflow in practice:**
1. `/speckit.constitution` — create a governing principles document (code quality, testing standards, UX consistency, performance). This guides all subsequent development.
2. `/speckit.specify` — describe what to build in plain language, focused on user stories and outcomes, not implementation.
3. `/speckit.clarify` — (optional) let the agent identify underspecified areas before planning.
4. `/speckit.plan` — provide tech stack and architecture choices; the agent generates a technical implementation plan.
5. `/speckit.analyze` — cross-artifact consistency check (run after tasks, before implement).
6. `/speckit.tasks` — convert the plan into an actionable task list; optionally push to GitHub Issues via `/speckit.taskstoissues`.
7. `/speckit.implement` — execute all tasks and build the feature.

Community extensions can add Jira integration, post-implementation code review, V-Model test traceability, and more. Community presets can enforce compliance-oriented formats, domain terminology, or organizational standards.

The toolkit was mentioned in r/ClaudeCode as an alternative to CLAUDE.md-based skill frameworks, with the comment: "I use Github Speckit for anything non-trivial."

## Related Entries
- [[spec-driven-development-bmad]]
- [[claude-code-plugins-guide]]
- [[awesome-agent-skills]]

---
<!-- RU -->

## Краткое описание
GitHub Spec-Kit — open-source CLI-инструментарий (`specify-cli`) для спецификационной разработки (Spec-Driven Development): структурированного рабочего процесса, в котором исполняемые спецификации управляют реализацией, заменяя вибкодинг воспроизводимой многоэтапной схемой: конституция → спецификация → план → задачи → реализация.

## Ключевые идеи
- Ключевая философия: спецификации исполняемы, а не просто временные опоры. Сначала определяется «что» и «зачем», затем из этого ИИ генерирует «как».
- Пять ключевых команд: `/speckit.constitution` → `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`
- Поддерживает 30+ AI-агентов: Claude Code, Codex CLI, Gemini CLI, Cursor, Copilot, OpenCode, Windsurf, Pi и другие — интегрируется через slash-команды или agent skills в зависимости от агента.
- Расширяется через **расширения** (новые команды) и **пресеты** (кастомизация шаблонов спецификаций/планов/задач) с приоритетным стекированием.
- Работает для greenfield-проектов (с нуля), итеративного улучшения (модернизация legacy) и творческого исследования (параллельные реализации на разных стеках).

## Подробнее
Установка через `uv tool install specify-cli` из GitHub releases. После `specify init my-project --integration copilot` (или нужного агента) AI-агент получает доступ к slash-командам spec-kit.

**Рабочий процесс:**
1. `/speckit.constitution` — создать документ управляющих принципов (качество кода, стандарты тестирования, UX, производительность).
2. `/speckit.specify` — описать что строить на обычном языке: пользовательские истории и результаты, не реализацию.
3. `/speckit.clarify` — (опционально) агент выявляет недоспецифицированные области до планирования.
4. `/speckit.plan` — указать технологический стек и архитектуру; агент генерирует технический план реализации.
5. `/speckit.tasks` — конвертировать план в список задач; опционально — в GitHub Issues через `/speckit.taskstoissues`.
6. `/speckit.implement` — выполнить все задачи и построить функцию.

Сообщество расширяет инструментарий: интеграция с Jira, ревью кода после реализации, трассировка V-Model, организационные стандарты. Упомянут в r/ClaudeCode: «Я использую Github Speckit для всего нетривиального.»

## Связанные записи
- [[spec-driven-development-bmad]]
- [[claude-code-plugins-guide]]
- [[awesome-agent-skills]]
