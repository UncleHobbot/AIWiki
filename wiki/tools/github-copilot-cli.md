---
title: "GitHub Copilot CLI"
title_ru: "GitHub Copilot CLI"
category: tools
tags: [github, copilot, cli, agent, coding-agent, terminal, pull-request]
updated: 2026-05-15
sources:
  - https://github.blog/ai-and-ml/github-copilot/from-idea-to-pull-request-a-practical-guide-to-building-with-github-copilot-cli/
---

## Summary
GitHub Copilot CLI is a GitHub-aware coding agent that lives in the terminal, letting you move from natural-language intent to reviewable diffs and pull requests without leaving the command line.

## Key Ideas
- **Human-approved execution:** Copilot proposes commands and diffs but never runs or applies changes without explicit user approval — you stay in control of what runs and what ships.
- **Intent-first workflow:** Start by describing what you want to build; `/plan` outlines the work before touching code; then review concrete diffs before anything executes.
- **Three-moment mental model:** CLI for low-ceremony momentum (explore, scaffold, diagnose failures), IDE for precision and design decisions, GitHub for review, collaboration, and shipping.
- **Mechanical changes at scale:** Well suited for repo-wide renames, refactors, and test updates — changes that are easy to describe but tedious to execute; produces a concrete diff instead of prose.
- **/delegate to GitHub:** Once changes are ready, Copilot CLI can commit, push, and open a pull request (adding Copilot as a reviewer) via natural language.
- **Copilot SDK:** For teams building developer tools where agentic execution is part of the *product*, the Copilot SDK gives programmatic access to the same planning and execution engine without custom orchestration.

## Details
Copilot CLI fits into the existing developer workflow rather than replacing it. The canonical cycle is: `copilot > <intent>` to explore → review proposed commands → `!<command>` to run → ask about failures in the same session → review diffs → commit and open PR.

The `/plan` flag (or Shift+Tab for planning mode) separates the design phase from execution. `explain` is useful when you want to understand a failure; `suggest` is better when you want a concrete, reviewable proposal. This keeps the agent grounded in actual output rather than abstract prompts.

The CLI is not a design substitute: it deliberately does not handle edge cases, API design decisions, or choices you'll need to defend in code review. Those belong in the IDE. Copilot CLI is most valuable for getting unstuck fast, not for making final decisions.

The Copilot SDK (technical preview as of 2026) exposes the same execution engine programmatically but omits GitHub-specific features like repo-scoped memory and delegated PR workflows. Use CLI for your own terminal workflow; use the SDK when embedding agentic capabilities inside an application.

## Related Entries
- [[llm-wiki-pattern]]
- [[llmwiki-open-source]]
- [[cpt-copilot-terminal]]

---
<!-- RU -->

## Краткое описание
GitHub Copilot CLI — это GitHub-ориентированный агент для кодирования, работающий в терминале: позволяет переходить от намерения на естественном языке к проверяемым diff-ам и pull request-ам, не выходя из командной строки.

## Ключевые идеи
- **Выполнение только с одобрения пользователя:** Copilot предлагает команды и diff-ы, но никогда не запускает и не применяет изменения без явного подтверждения — вы контролируете всё, что выполняется и попадает в репозиторий.
- **Workflow с приоритетом намерения:** Начните с описания того, что хотите построить; `/plan` набрасывает план до прикосновения к коду; затем просмотрите конкретные diff-ы, прежде чем что-то выполнится.
- **Модель трёх моментов:** CLI — для быстрого старта без лишних ритуалов (исследование, скаффолдинг, диагностика сбоев), IDE — для точности и принятия проектных решений, GitHub — для ревью, совместной работы и выпуска.
- **Механические изменения в масштабе:** Хорошо подходит для переименований по всему репозиторию, рефакторингов и обновлений тестов — изменений, которые просто описать, но долго выполнять вручную; выдаёт конкретный diff вместо текстового объяснения.
- **/delegate на GitHub:** Когда изменения готовы, Copilot CLI может сделать commit, push и открыть pull request (добавив Copilot в ревьюеры) на естественном языке.
- **Copilot SDK:** Для команд, строящих инструменты разработчика, где агентное выполнение — часть *продукта*, Copilot SDK открывает программный доступ к тому же движку планирования и исполнения без необходимости строить собственную оркестрацию.

## Подробнее
Copilot CLI вписывается в существующий workflow разработчика, а не заменяет его. Канонический цикл: `copilot > <намерение>` — исследование → просмотр предложенных команд → `!<команда>` для выполнения → вопросы о сбоях в том же сеансе → просмотр diff-ов → commit и открытие PR.

Флаг `/plan` (или Shift+Tab для режима планирования) разделяет фазу проектирования и выполнения. `explain` полезен, когда нужно понять суть сбоя; `suggest` лучше, когда нужно конкретное, проверяемое предложение. Это не даёт агенту отрываться от реального вывода в пользу абстрактных подсказок.

CLI — не замена проектирования: он намеренно не обрабатывает граничные случаи, решения по API и выборы, которые придётся защищать на код-ревью. Это задача IDE. Copilot CLI наиболее ценен для быстрого выхода из затруднительного положения, а не для принятия окончательных решений.

Copilot SDK (техническое превью на 2026 год) предоставляет тот же движок исполнения программно, но без GitHub-специфичных возможностей: контекста, привязанного к репозиторию, и делегированных PR-workflow. Используйте CLI для своего терминального workflow; SDK — когда встраиваете агентные возможности в приложение.

## Связанные записи
- [[llm-wiki-pattern]]
- [[llmwiki-open-source]]
- [[cpt-copilot-terminal]]
