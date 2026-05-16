---
title: "Han: AI Skills Plugin for Claude Code"
title_ru: "Han: плагин AI-навыков для Claude Code"
category: tools
tags: [claude-code, plugin, skills, agents, code-review, planning, solo-engineer]
updated: 2026-05-16
sources:
  - https://github.com/testdouble/han
---

## Summary
Han is a Claude Code plugin by Test Double that gives solo or small-team engineers access to a swarm of specialist AI agents for planning, code review, architectural analysis, and documentation — work that normally requires a full team.

## Key Ideas
- **15 skills, 21 agents:** Each skill dispatches specialist agents (PMs, adversarial reviewers, investigators, architects, testing/security specialists) that do the heavy judgment work, then hand back a trustable artifact.
- **Composable workflow:** Skills are designed to chain — plan a feature → plan implementation → iterative plan review → code review → write PR description, all through named handoffs.
- **Skill categories:** Planning (`/plan-a-feature`, `/plan-implementation`, `/plan-a-phased-build`, `/iterative-plan-review`), investigation (`/investigate`), review (`/code-review`, `/gh-pr-review`, `/architectural-analysis`, `/gap-analysis`, `/test-planning`), and documentation.
- **Sizing model:** `small/medium/large` dispatch model controls how many agents swarm skills like `/code-review` and `/plan-a-feature`, letting you trade cost for thoroughness.
- **YAGNI enforcement:** Every planning, review, and architecture skill applies an evidence-based "You Aren't Gonna Need It" rule before committing items to an artifact.
- **Install via marketplace:** One command adds the plugin to any Claude Code session across all projects.

## Details
Han fills the gap for engineers working without a team of specialists. Instead of approximating a PM conversation or architecture review in a single chat thread, Han spins up agents that behave like specialists: the project manager interviews you before writing a plan, the adversarial reviewer stress-tests the plan, the code reviewer checks for security and test coverage independently.

The plugin is designed for composition. A typical feature workflow: run `/plan-a-feature` to build a spec via evidence-based interview → `/plan-implementation` to turn the spec into a phased plan → `/iterative-plan-review` to stress-test it → implement → `/code-review` on the diff → PR description. Each skill hands structured artifacts to the next.

The `Sizing` model (documented in Han's own docs) lets you control agent swarm size for the most compute-heavy skills (`small` = 3 agents, `large` = 7+), balancing token cost vs. depth of analysis.

## Notable Quotes
> "Han turns planning, review, and documentation work that would normally take a team into a set of deterministic skills you run from Claude Code." — Han README

## Related Entries
- [[claude-code-extensions-overview]]
- [[claude-code-plugins-guide]]

---
<!-- RU -->

## Краткое описание
Han — плагин Claude Code от Test Double, дающий соло-разработчикам или небольшим командам доступ к рою специализированных AI-агентов для планирования, код-ревью, архитектурного анализа и документации.

## Ключевые идеи
- **15 навыков, 21 агент:** Каждый навык запускает специализированных агентов (PM, «критик», исследователь, архитектор, эксперт по тестированию/безопасности), которые выполняют тяжёлую аналитическую работу и возвращают проверяемый артефакт.
- **Компонуемый workflow:** Навыки спроектированы для цепочки: план фичи → план реализации → проверка плана → код-ревью → описание PR — всё через именованные передачи управления.
- **Категории навыков:** Планирование (`/plan-a-feature`, `/plan-implementation`, `/plan-a-phased-build`, `/iterative-plan-review`), расследование (`/investigate`), ревью (`/code-review`, `/gh-pr-review`, `/architectural-analysis`, `/gap-analysis`, `/test-planning`) и документация.
- **Модель масштабирования:** `small/medium/large` управляет количеством агентов в рое, позволяя торговать стоимостью запроса на глубину анализа.
- **YAGNI-принцип:** Каждый навык для планирования, ревью и архитектуры применяет доказательное правило «You Aren't Gonna Need It» перед добавлением пункта в артефакт.
- **Установка через маркетплейс:** Одна команда добавляет плагин во все сессии Claude Code.

## Подробнее
Han закрывает пробел для разработчиков, работающих без команды специалистов. Вместо того чтобы имитировать разговор с PM или архитектурное ревью в одном чат-треде, Han запускает агентов, которые ведут себя как специалисты: PM проводит интервью перед написанием плана, «критик» проверяет план на уязвимости, код-ревьюер независимо проверяет безопасность и тест-покрытие.

Типичный feature-workflow: `/plan-a-feature` (сбор требований через интервью) → `/plan-implementation` (преобразование спецификации в фазовый план) → `/iterative-plan-review` (стресс-тест плана) → реализация → `/code-review` по diff → описание PR. Каждый навык передаёт структурированные артефакты следующему.

Модель `Sizing` позволяет управлять размером роя агентов для наиболее ресурсоёмких навыков (`small` = 3 агента, `large` = 7+), балансируя стоимость токенов и глубину анализа.

## Примечательные цитаты
> «Han превращает работу по планированию, ревью и документации, которая обычно требует целой команды, в набор детерминированных навыков, запускаемых из Claude Code.» — README Han

## Связанные записи
- [[claude-code-extensions-overview]]
- [[claude-code-plugins-guide]]
