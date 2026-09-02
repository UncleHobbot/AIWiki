---
title: "orchestrate-sol-terra-luna — 3-Tier GPT-5.6 Workflow Skill"
title_ru: "orchestrate-sol-terra-luna — трёхуровневый воркфлоу-скилл для GPT-5.6"
category: tips
tags: [gpt-5.6, sol, terra, luna, orchestration, skill, cost-tiering]
aliases: [sol terra luna orchestrate, 3-tier gpt-5.6, gpt-5.6 workflow skill]
confidence: medium
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/codex/comments/1w5d1r0/a_3tier_gpt56_workflow_ive_been_using_for_a_while/
  - https://github.com/irons163/orchestrate-sol-terra-luna
---

## Summary
A community skill (`orchestrate-sol-terra-luna`) that splits the GPT-5.6 model family into a three-tier workflow balancing cost and intelligence: **Sol** for goal understanding, task decomposition, architecture decisions, result checking, and final integration; **Terra Max** for hard but well-bounded analysis, implementation, deep code review, and complex debugging; **Luna Max** for clear, repeatable, easy-to-verify tasks — search, testing, reproduction, mechanical edits, summarization.

## Key Ideas
- **Tier-to-task mapping:** strategic (Sol) / analytical (Terra) / mechanical (Luna) — the same cost-tiering logic as [[gpt-5-6-pareto-frontier-copilot]] but operationalized as a skill with explicit routing rules.
- **Quota guidance:** on Plus, keep main reasoning at ~Sol Mid or Terra Max — higher burns the 5-hour limit quickly.
- **Why it works:** GPT-5.6's reasoning tiers populate the Pareto frontier themselves ([[gpt-5-6-pareto-frontier-copilot]]); the skill just routes tasks to the right tier *before* spending.
- Pairs with the wiki's cost-discipline cluster ([[anthropic-cost-optimization-cookbook]], [[tokenray-cost-dashboard]]).

## Details
The transferable pattern: model-family tier routing as a *skill* rather than manual model picking. Any multi-tier model family (GPT-5.6 Sol/Terra/Luna, GLM-5.3/GLM-5.3-Flash, Opus/Sonnet/Haiku) supports the same shape. The quota-aware defaults make it practical for subscription users, not just API users.

## Related Entries
- [[gpt-5-6-pareto-frontier-copilot]] ([GPT-5.6 Pareto Frontier](../models/gpt-5-6-pareto-frontier-copilot.md))
- [[gpt-5-6-sol-preview]] ([GPT-5.6 Sol Preview](../news/gpt-5-6-sol-preview.md))
- [[anthropic-cost-optimization-cookbook]] ([Anthropic Cost Optimization Cookbook](anthropic-cost-optimization-cookbook.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](hard-gates-over-soft-prompts.md))

---
<!-- RU -->

## Краткое описание
Комьюнити-скилл (`orchestrate-sol-terra-luna`), разбивающий семейство GPT-5.6 на трёхуровневый воркфлоу для баланса стоимости и интеллекта: **Sol** — понимание цели, декомпозиция задач, архитектурные решения, проверка результатов, финальная интеграция; **Terra Max** — сложный, но ограниченный анализ, имплементация, глубокое ревью кода, сложный дебаг; **Luna Max** — ясные, повторяемые, легко проверяемые задачи — поиск, тестирование, воспроизведение, механические правки, суммаризация.

## Ключевые идеи
- **Сопоставление тир-задача:** стратегический (Sol) / аналитический (Terra) / механический (Luna) — та же логика cost-tiering, что в записи о Парето, но операционализованная как скилл с явными правилами маршрутизации.
- **Квотные советы:** на Plus держать основной reasoning около Sol Mid или Terra Max — выше быстро сжигает 5-часовой лимит.
- **Почему работает:** тиры reasoning GPT-5.6 сами заполняют границу Парето; скилл просто маршрутизирует задачи в нужный тир *до* трат.
- Сочетается с кластером экономии вики.

## Подробнее
Переносимый паттерн: маршрутизация по тирам семейства моделей как *скилл*, а не ручной выбор модели. Любое многоуровневое семейство (Sol/Terra/Luna, GLM-5.3/Flash, Opus/Sonnet/Haiku) поддерживает ту же форму. Квотные дефолты делают его практичным для подписчиков, а не только API-пользователей.

## Связанные записи
- [[gpt-5-6-pareto-frontier-copilot]] ([GPT-5.6 Pareto Frontier](../models/gpt-5-6-pareto-frontier-copilot.md))
- [[gpt-5-6-sol-preview]] ([GPT-5.6 Sol Preview](../news/gpt-5-6-sol-preview.md))
- [[anthropic-cost-optimization-cookbook]] ([Anthropic Cost Optimization Cookbook](anthropic-cost-optimization-cookbook.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](hard-gates-over-soft-prompts.md))
