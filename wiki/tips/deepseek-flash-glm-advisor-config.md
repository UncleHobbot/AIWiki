---
title: "DeepSeek Flash + GLM 5.2 Advisor: Cost-Optimized Multi-Model OpenCode Config"
title_ru: "DeepSeek Flash + GLM 5.2 advisor: оптимизированная по стоимости мульти-модельная конфигурация OpenCode"
category: tips
tags: [opencode, deepseek, glm-5.2, subagent, cost-optimization, config]
aliases: [DeepSeek Flash GLM advisor, opencode advisor subagent, cheap orchestrator config]
confidence: medium
updated: 2026-06-29
sources:
  - https://www.reddit.com/r/opencode/comments/1ugyxlk/how_to_set_up_deepseek_flash_glm_52_advisor_in/
---

## Summary
A community-shared OpenCode configuration that uses DeepSeek V4 Flash as the cheap, fast primary orchestrator (1M context, ~$0.0003 per mechanical call) and promotes GLM 5.2 as an advisor subagent that only burns credits on calls that need actual reasoning — a cost-optimized two-tier routing pattern.

## Key Ideas
- **Two-tier routing**: a cheap/fast model handles routine orchestration; a stronger model steps in only for reasoning-heavy subtasks.
- **DeepSeek Flash as primary**: handles the bulk of mechanical engineering work cheaply (~$0.0003 per call) with a 1M-token context window for large-context awareness.
- **GLM 5.2 as advisor subagent**: invoked only when the task needs genuine reasoning, so expensive credits are spent only where they matter.
- **Config lives in `opencode.jsonc`** (global `~/.config/opencode/`, project-level `~/.opencode/`, or per-repo `.opencode/`) — the `agent` block defines `mode: "primary"` for Flash and a subagent role for GLM.
- **The economics**: paying ~fractions of a cent for orchestration calls and reserving the pricier model for the ~small fraction of calls that need it dramatically lowers average cost per task.

## Details
The pattern exploits the observation that most of an agent's work in a coding session is mechanical (reading files, running commands, formatting) and doesn't need frontier reasoning. By defaulting to the cheapest competent model and only escalating to the reasoning model on demand, you get near-equivalent outcomes at a fraction of the cost.

This is a concrete instance of the broader "model routing" / "orchestrator + specialist subagent" architecture: route by task difficulty rather than sending everything through the most expensive model. The advisor-subagent framing keeps the strong model's cost proportional to how often it's actually consulted.

## Notable Quotes
> "Flash pays ~$0.0003 per mechanical call. GLM only burns credits on the calls that need it." — r/opencode

## Related Entries
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[deepseek-v4-peak-pricing]] ([DeepSeek V4 Launch and Peak Pricing](../news/deepseek-v4-peak-pricing.md))

---
<!-- RU -->

## Краткое описание
Разделяемая сообществом конфигурация OpenCode, в которой DeepSeek V4 Flash выступает дешёвым быстрым первичным оркестратором (1M контекст, ~$0.0003 за механический вызов), а GLM 5.2 подключается как advisor-субагент только для вызовов, требующих настоящего рассуждения — оптимизированный по стоимости двухуровневый паттерн маршрутизации.

## Ключевые идеи
- **Двухуровневая маршрутизация**: дешёвая/быстрая модель ведёт рутинную оркестрацию; более сильная модель подключается лишь для рассужденчески тяжёлых подзадач.
- **DeepSeek Flash как primary**: дёшево ведёт основную механическую инженерную работу (~$0.0003 за вызов) с окном 1M токенов.
- **GLM 5.2 как advisor-субагент**: вызывается только когда задаче нужно настоящее рассуждение, так что дорогие кредиты тратятся лишь там, где это важно.
- **Конфиг живёт в `opencode.jsonc`** (глобально, на уровне проекта или per-repo) — блок `agent` задаёт `mode: "primary"` для Flash и роль субагента для GLM.
- **Экономика**: платя доли цента за оркестрацию и оставляя дорогую модель для малой доли вызовов, средняя стоимость задачи резко падает.

## Подробнее
Паттерн эксплуатирует наблюдение, что большая часть работы агента в кодинг-сессии механическая (чтение файлов, запуск команд, форматирование) и не требует frontier-рассуждения. По умолчанию используя самую дешёвую компетентную модель и эскалируя к рассужденческой модели по требованию, вы получаете почти эквивалентный результат за малую долю стоимости.

Это конкретный экземпляр более широкой архитектуры «model routing» / «оркестратор + специалист-субагент»: маршрутизация по сложности задачи, а не прогон всего через самую дорогую модель.

## Связанные записи
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[deepseek-v4-peak-pricing]] ([DeepSeek V4 Launch and Peak Pricing](../news/deepseek-v4-peak-pricing.md))
