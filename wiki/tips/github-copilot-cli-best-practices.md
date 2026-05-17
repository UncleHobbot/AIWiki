---
title: "GitHub Copilot CLI: Best Practices and Workflows"
title_ru: "GitHub Copilot CLI: лучшие практики и рабочие процессы"
category: tips
tags: [github-copilot, cli, terminal, best-practices, agentic-workflow, plan-mode, context-management]
updated: 2026-05-16
sources:
  - https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices
  - https://developer.microsoft.com/blog/get-started-with-github-copilot-cli-a-free-hands-on-course
---

## Summary
GitHub Copilot CLI is a terminal-native agentic coding assistant. These are the key patterns that make it most effective: instruction layering, model selection by task complexity, plan-first execution, and focused sessions.

## Key Ideas
- **Layered instructions:** Copilot reads from `~/.copilot/copilot-instructions.md` (global), `.github/copilot-instructions.md` (repo), and `.github/instructions/**/*.instructions.md` (modular) — repo always overrides global. Keep instructions concise and actionable.
- **Model selection matters:** Auto mode reduces rate-limiting; Opus 4.5 for complex architecture/debugging; Sonnet 4.5 for day-to-day coding; Codex 5.2 for code generation and second-opinion reviews. Switch mid-session with `/model`.
- **Plan mode before complex tasks:** Press Shift+Tab or use `/plan` to make Copilot ask clarifying questions, produce a structured plan with checkboxes, and save it to `plan.md` before writing a line of code.
- **Tool permission management:** Preconfigure allowed tools via `--allow-tool` and `--deny-tool` flags (e.g. `shell(git:*)` to allow all git commands). Reset with `/reset-allowed-tools`.
- **Infinite sessions, focused context:** Sessions don't expire (auto-compact preserves essentials), but use `/clear` or `/new` between unrelated tasks for better response quality.
- **`/delegate` for async work:** Send tasks to the cloud Copilot agent for tangential/asynchronous work (documentation, refactoring separate modules) while you continue locally.
- **Three interaction modes:** Interactive (conversational back-and-forth), Plan (structured planning before execution), One-shot/programmatic (single-command execution for automation).
- **Custom agents + skills:** `.agent.md` files create specialized assistants; skills auto-trigger based on your prompt and can be shared team-wide via `.github/agents/` and `.github/skills/`.

## Details
The recommended pattern for complex tasks is Explore → Plan → Implement → Verify → Commit. In practice: start a fresh session, read the relevant files without writing (`Explore: Read the authentication files but don't write code yet`), then `/plan Implement password reset flow`, review and edit the plan, then proceed with implementation. Run tests, fix failures, then commit with a descriptive message.

A free open-source beginner course (GitHub Copilot CLI for Beginners, 8 chapters) covers this workflow end to end, including custom agents, skills, and MCP server integration. The course uses a consistent book-collection app project across all chapters to build intuition for when to reach for an agent vs. a skill vs. an MCP server.

For team use: standardize instructions in `.github/copilot-instructions.md`, share agents in `.github/agents/`, and share skills in `.github/skills/`. This gives the whole team consistent AI behavior without individual setup.

Context visualization: use `/context` to see a breakdown of token usage (system/tools/message history/free space). Use `/compact` manually if needed, though auto-compaction handles most cases. Use `/session` to inspect checkpoints and temporary files.

## Notable Quotes
> "Plan mode is more like mapping your route to the restaurant before you start driving. Interactive mode is a back-and-forth conversation with a waiter. And one-shot mode is like going through the drive-through." — GitHub Copilot CLI for Beginners course

## Related Entries
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[agentic-ai-development-copilot-lessons]] ([Agentic AI Development with GitHub Copilot: Lessons Learned](../tips/agentic-ai-development-copilot-lessons.md))
- [[copilot-cli-telegram-bridge]] ([Using Telegram as a Mobile Front-End for GitHub Copilot CLI](../tips/copilot-cli-telegram-bridge.md))

---
<!-- RU -->

## Краткое описание
GitHub Copilot CLI — агентный помощник по написанию кода, работающий в терминале. Ключевые паттерны для максимальной эффективности: слоистые инструкции, выбор модели по сложности задачи, планирование перед реализацией и сфокусированные сессии.

## Ключевые идеи
- **Слоистые инструкции:** Copilot читает из `~/.copilot/copilot-instructions.md` (глобально), `.github/copilot-instructions.md` (репозиторий) и `.github/instructions/**/*.instructions.md` (модульно) — настройки репозитория всегда перекрывают глобальные. Держите инструкции краткими и конкретными.
- **Выбор модели имеет значение:** Auto снижает rate-limiting; Opus 4.5 — для сложной архитектуры и отладки; Sonnet 4.5 — для повседневного кодирования; Codex 5.2 — для генерации кода и ревью. Переключайте в середине сессии через `/model`.
- **Режим планирования перед сложными задачами:** Shift+Tab или `/plan` заставляют Copilot задавать уточняющие вопросы, формировать структурированный план с чекбоксами и сохранять его в `plan.md` до написания кода.
- **Управление разрешениями инструментов:** Предварительно настройте через `--allow-tool` и `--deny-tool` (например, `shell(git:*)` — разрешить все git-команды). Сброс — `/reset-allowed-tools`.
- **Бесконечные сессии, сфокусированный контекст:** Сессии не истекают (авто-компакция сохраняет главное), но используйте `/clear` или `/new` между несвязанными задачами для лучшего качества ответов.
- **`/delegate` для асинхронной работы:** Отправляйте задачи облачному агенту Copilot для второстепенной работы (документация, рефакторинг отдельных модулей), пока вы работаете локально.
- **Три режима взаимодействия:** Интерактивный (диалог), плановый (структурированное планирование перед выполнением), одиночный/программный (одна команда для автоматизации).
- **Кастомные агенты и навыки:** `.agent.md` создают специализированных помощников; навыки автоматически активируются по вашему запросу и могут быть общими для команды через `.github/agents/` и `.github/skills/`.

## Подробнее
Рекомендуемый паттерн для сложных задач: Исследовать → Спланировать → Реализовать → Проверить → Зафиксировать. На практике: откройте новую сессию, прочитайте нужные файлы без записи (`Explore: Read the authentication files but don't write code yet`), затем `/plan Implement password reset flow`, проверьте и отредактируйте план, после чего приступайте к реализации.

Бесплатный open-source курс для начинающих (GitHub Copilot CLI for Beginners, 8 глав) охватывает этот workflow целиком, включая кастомные агенты, навыки и интеграцию с MCP-серверами. Курс использует один проект (приложение для управления коллекцией книг) во всех главах, чтобы выработать интуицию: когда тянуться за агентом, навыком, а когда — за MCP-сервером.

Для командного использования: стандартизируйте инструкции в `.github/copilot-instructions.md`, расшаривайте агентов в `.github/agents/` и навыки в `.github/skills/`. Это даёт всей команде согласованное поведение AI без индивидуальной настройки.

## Примечательные цитаты
> «Режим планирования — это как прокладывать маршрут перед поездкой. Интерактивный режим — диалог с официантом. А однострочный режим — как заказ через окошко drive-through.» — Курс GitHub Copilot CLI for Beginners

## Связанные записи
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[agentic-ai-development-copilot-lessons]] ([Agentic AI Development with GitHub Copilot: Lessons Learned](../tips/agentic-ai-development-copilot-lessons.md))
- [[copilot-cli-telegram-bridge]] ([Using Telegram as a Mobile Front-End for GitHub Copilot CLI](../tips/copilot-cli-telegram-bridge.md))
