---
title: "Anthropic Cost Optimization Cookbook — Pass Rate vs Cost-per-Task Pareto"
title_ru: "Anthropic Cost Optimization Cookbook — Парето «проходимость против стоимости задачи»"
category: tips
tags: [cost-optimization, prompt-caching, eval, model-selection, claude, checklist]
aliases: [cost optimization cookbook, anthropic cost checklist, cost per task]
confidence: high
updated: 2026-09-01
sources:
  - https://github.com/anthropics/claude-cookbooks/blob/main/cost_optimization/cost_optimization.ipynb
---

## Summary
Anthropic's Applied AI team notebook laying out their ordered checklist for cutting Claude API spend without lowering quality — measured as **pass rate vs cost per task** (not per token, since a pricier model that finishes in fewer turns can be cheaper end-to-end), plotted as a Pareto staircase on a mock insurance-claims agent. Headline result: **sonnet·medium with explicit cache breakpoints — ~13× cheaper than baseline while holding 10/10 pass rate.**

## Key Ideas
- **The ordered checklist (deliberate sequence):** (1) baseline + eval, (2) prompt caching, (3) input token management, (4) agent-loop efficiency, (5) output token management, (6) Batch API, (7) model selection/effort — model choice is *last* because it caps the intelligence ceiling; caching is *first* because it changes what you pay, not what the model can do.
- **Pareto winner:** sonnet·medium + explicit cache breakpoint on the shared system prompt (that single breakpoint roughly halved cost per task); effort ladder holds 10/10 through sonnet·medium, slips at sonnet·low; Haiku managed ~55%.
- **Levers that FAILED this workload** (validate everything against your eval): tool-wrapping the 12K-token manual matched savings but lost accuracy; tool search adds overhead under ~10K schema tokens; code execution adds tokens without numeric work; context editing never fired on 5–6-turn loops; subagent routing was cheapest but dropped a claim (compressed rule card lost a carve-out).
- **Concrete tactics:** byte-stable prefixes with volatile content moved to the user turn; images ≈ 1 token per 28×28 patch (1280×720 ≈ 1,200 tokens — pre-downscale); route big CSVs/PDFs through Files API + code execution instead of inlining; Batch API = flat 50% off, single-shot only.
- **Production guidance:** ~50 eval cases and ≥5 trials per configuration to beat nondeterminism; includes a workload-shape → lever mapping table.

## Details
This is the wiki's missing bridge between token-cost tactics ([[mcp-tool-schema-bloat-token-cost]], [[browser-snapshot-format-token-cost]]) and model-selection strategy ([[gpt-5-6-pareto-frontier-copilot]]). The discipline that generalizes: *build the eval first, then walk the checklist in order, and let the Pareto plot tell you where to stop* — most teams invert this and start with model swaps. Baseline for reference: Opus 5 at effort=high, no caching = 10/10 at ~$0.29/task (~$2,906 per 10k tasks).

## Related Entries
- [[gpt-5-6-pareto-frontier-copilot]] ([GPT-5.6 Pareto Frontier](../models/gpt-5-6-pareto-frontier-copilot.md))
- [[mcp-tool-schema-bloat-token-cost]] ([MCP Tool-Schema Bloat](mcp-tool-schema-bloat-token-cost.md))
- [[browser-snapshot-format-token-cost]] ([Browser Snapshot Format vs Token Cost](../research/browser-snapshot-format-token-cost.md))
- [[opencode-12m-token-burn]] ([OpenCode 12M Token Burn](opencode-12m-token-burn.md))

---
- [[gpt-5-6-three-tier-workflow]] ([3-Tier GPT-5.6 Workflow](gpt-5-6-three-tier-workflow.md))
<!-- RU -->

## Краткое описание
Ноутбук прикладной команды Anthropic с упорядоченным чеклистом снижения расходов на Claude API без потери качества — метрика **проходимость против стоимости за задачу** (не за токен: дорогая модель, завершающая за меньше ходов, может быть дешевле в итоге), с графиком Парето на мок-агенте страховых претензий. Главный результат: **sonnet·medium с явными cache-брейкпоинтами — в ~13 раз дешевле базлайна при 10/10.**

## Ключевые идеи
- **Упорядоченный чеклист:** (1) базлайн + eval, (2) prompt caching, (3) управление входными токенами, (4) эффективность агентного лупа, (5) выходные токены, (6) Batch API, (7) выбор модели/effort — выбор модели *последний* (потолок интеллекта), кэш *первый* (меняет цену, не возможности).
- **Парето-победитель:** sonnet·medium + явный брейкпоинт кэша на системном промпте (один брейкпоинт ≈ вдвое дешевле задачу); лестница effort держит 10/10 до sonnet·medium; Haiku — ~55%.
- **Рычаги, НЕ сработавшие на этой нагрузке** (проверяйте на своём eval): оборачивание 12K-токенного мануала в инструмент; tool search при <10K токенов схем; code execution без численных задач; context editing не срабатывал на лупах 5–6 ходов; subagent-роутинг был cheapest, но потерял одну претензию.
- **Конкретика:** байт-стабильные префиксы, волатильное — в user turn; изображения ≈ 1 токен на патч 28×28 (1280×720 ≈ 1200 токенов); большие CSV/PDF — через Files API + code execution; Batch API = −50%, только single-shot.
- **Production-совет:** ~50 eval-кейсов и ≥5 прогонов на конфигурацию против недетерминизма.

## Подробнее
Это недостающий мост вики между тактиками экономии токенов и стратегией выбора моделей. Обобщаемая дисциплина: *сначала eval, затем чеклист по порядку, и пусть график Парето скажет, где остановиться* — большинство команд делает наоборот, начиная со смены модели. Базлайн: Opus 5 effort=high без кэша = 10/10 при ~$0.29/задача.

## Связанные записи
- [[gpt-5-6-pareto-frontier-copilot]] ([GPT-5.6 Pareto Frontier](../models/gpt-5-6-pareto-frontier-copilot.md))
- [[mcp-tool-schema-bloat-token-cost]] ([MCP Tool-Schema Bloat](mcp-tool-schema-bloat-token-cost.md))
- [[browser-snapshot-format-token-cost]] ([Browser Snapshot Format vs Token Cost](../research/browser-snapshot-format-token-cost.md))
- [[opencode-12m-token-burn]] ([OpenCode 12M Token Burn](opencode-12m-token-burn.md))
