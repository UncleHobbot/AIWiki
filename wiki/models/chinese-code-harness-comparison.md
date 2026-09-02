---
title: "Kimi Code vs GLM (Z Code) vs Qwen Code vs OpenCode Go — Subscription Comparison"
title_ru: "Kimi Code против GLM (Z Code) против Qwen Code против OpenCode Go — сравнение подписок"
category: models
tags: [kimi, glm, qwen, opencode, comparison, tau2-bench, leaderboard, chinese-models]
aliases: [kimi vs glm vs qwen code, chinese coding subscription comparison]
confidence: low
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/ZaiGLM/comments/1w4kwbs/kimi_code_vs_glm_z_code_vs_qwen_code_vs_open_code/
  - https://openrouter.ai/benchmarks/tau2-bench-airline
  - https://arena.ai/leaderboard/agent/code
---

## Summary
A Claude Code + GPT-5 subscriber shopping for a Chinese-model subscription compiled the problem: **the two main leaderboards disagree on the ranking.** OpenRouter's tau2-bench-airline puts **GLM > Qwen > Kimi**; LLM Arena's agent/code leaderboard puts **Kimi > GLM > Qwen**. The post (cross-posted to r/ZaiGLM and r/opencode) is a live instance of the benchmark-disagreement problem this wiki tracks.

## Key Ideas
- **Ranking instability across benchmarks:** tau2-bench (agentic tool-use) and Arena's code leaderboard invert the order — each measures a different capability slice.
- **The buyer's actual criteria** (from the post): performance *and* token volume — but token-volume terms are exactly where subscriptions differ most opaquely ([[zai-max-plan-undisclosed-weekly-limit]], [[kimi-code-quota-audit]]).
- **Context:** GLM has ZCode, Kimi has Kimi Code, Qwen has Qwen Code, and OpenCode Go is the vendor-agnostic option — harness+plan bundles, not just models.
- **Resolution direction:** use leaderboards for capability *slices* only; decide on quota math and harness fit; see [[llm2014-llm-benchmark]] for an independent longitudinal signal.

## Details
The meta-lesson generalizes: when two credible leaderboards invert, the honest answer is "it depends on which slice you weight" — tool-use vs code-agent behavior. This entry will stay low-confidence until a single source shows consistent ordering across both benchmark families.

## Related Entries
- [[llm2014-llm-benchmark]] ([llm2014 Benchmark](../research/llm2014-llm-benchmark.md))
- [[zcode-zai-agentic-development-environment]] ([ZCode](../research/zcode-zai-agentic-development-environment.md))
- [[kimi-code-cli]] ([Kimi Code CLI](../tools/kimi-code-cli.md))
- [[glm-5-3-flash-vs-deepseek-v4-flash]] ([GLM-5.3 Flash vs DeepSeek V4 Flash](glm-5-3-flash-vs-deepseek-v4-flash.md))

---
<!-- RU -->

## Краткое описание
Подписчик Claude Code + GPT-5, выбирающий подписку на китайские модели, зафиксировал проблему: **два главных лидерборда противоречат друг другу.** Tau2-bench-airline от OpenRouter: **GLM > Qwen > Kimi**; лидерборд agent/code от LLM Arena: **Kimi > GLM > Qwen**. Пост (кросспост в r/ZaiGLM и r/opencode) — живой инстанс проблемы расхождения бенчмарков.

## Ключевые идеи
- **Нестабильность рейтингов между бенчмарками:** tau2-bench (агентный tool-use) и Arena code инвертируют порядок — каждый меряет свой срез способностей.
- **Реальные критерии покупателя** (из поста): производительность *и* объём токенов — но именно условия объёма наиболее непрозрачны.
- **Контекст:** у GLM есть ZCode, у Kimi — Kimi Code, у Qwen — Qwen Code, плюс вендор-агностичный OpenCode Go — связки «харнес+план», а не просто модели.
- **Направление разрешения:** лидерборды — только для срезов способностей; решение — по математике квот и соответствию харнеса; независимый лонгитюд — [[llm2014-llm-benchmark]].

## Подробнее
Мета-урок обобщается: когда два достоверных лидерборда инвертированы, честный ответ — «зависит от того, какой срез вы взвешиваете». Запись останется с низкой достоверностью, пока единый источник не покажет согласованный порядок в обоих семействах бенчмарков.

## Связанные записи
- [[llm2014-llm-benchmark]] ([llm2014 Benchmark](../research/llm2014-llm-benchmark.md))
- [[zcode-zai-agentic-development-environment]] ([ZCode](../research/zcode-zai-agentic-development-environment.md))
- [[kimi-code-cli]] ([Kimi Code CLI](../tools/kimi-code-cli.md))
- [[glm-5-3-flash-vs-deepseek-v4-flash]] ([GLM-5.3 Flash vs DeepSeek V4 Flash](glm-5-3-flash-vs-deepseek-v4-flash.md))
