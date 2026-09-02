---
title: "llm2014 LLM Benchmark — Independent Long-Term Model Tracking"
title_ru: "llm2014 LLM Benchmark — независимый долгосрочный трекинг моделей"
category: research
tags: [benchmark, leaderboard, glm, kimi, gpt, independent, private-question-bank]
aliases: [llm2014 benchmark, community llm benchmark, long-term llm tracking]
confidence: medium
updated: 2026-09-01
sources:
  - https://llm2014.github.io/llm_benchmark
  - https://github.com/llm2014/llm_benchmark
---

## Summary
A personal, Chinese-language "long-term LLM intelligence tracking leaderboard" (1,575 stars, actively maintained through Sep 2026) using a private monthly-rolling question bank (~28 questions / 270 test cases) covering logic, math, coding, and intuition. Notable as an independent, non-vendor signal for the wiki's monitored models — with the explicit caveat that it's one person's benchmark.

## Key Ideas
- **Methodology:** private questions (no public-set contamination), per-question point scoring (max 10), reasoning must be *correct* (lucky guesses score 0), format violations score 0, 3 runs per model taking the max, run via OpenRouter/Zenmux with official settings; month-to-month swing ±3 points.
- **Current logic leaderboard (2026-09):** GPT-5.6 Sol 78.98, Kimi-K3 72.70, Opus 5 71.99, GLM-5.3 70.56 (+16.8% MoM, ¥28/1M tokens), GLM-5.3-Flash 66.52.
- **Longitudinal value:** monthly CSV archives let you track model families over time — the July archive holds the GLM-5.2 numbers.
- **Self-aware framing:** the author explicitly warns "not authoritative, not comprehensive — don't blindly trust any evaluation."
- Sits between vendor benchmarks and the evidence-first [[pickleshell-model-benchmarks]] approach: more consistent than ad-hoc threads, less rigorous than clean-room suites.

## Details
For GLM/Kimi tracking specifically, this is the strongest independent cross-model signal among the wiki's sources — private questions defeat benchmark-training contamination, and the monthly cadence captures model-family trajectory (GLM-5.2 → GLM-5.3's +16.8% jump). Use it directionally; the single-rater scoring and small bank (28 questions) mean individual-month numbers are noisy.

## Related Entries
- [[llm-wiki-chinese-models-comparison]] ([Chinese Models Comparison](../models/llm-wiki-chinese-models-comparison.md))
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[kimi-k2-7-code]] ([Kimi K2.7 Code](../models/kimi-k2-7-code.md))
- [[pickleshell-model-benchmarks]] ([PickleShell Model Benchmarks](../tools/pickleshell-model-benchmarks.md))

---
- [[qwen25-coder-mql5-finetune]] ([MQL5 Fine-Tune: 1% → 92%](qwen25-coder-mql5-finetune.md))
<!-- RU -->

## Краткое описание
Персональный (кит.-язычный) «долгосрочный лидерборд интеллекта LLM» (1575 звёзд, активен по сен 2026) с приватным ежемесячно обновляемым банком вопросов (~28 вопросов / 270 тестов) по логике, математике, кодингу и интуиции. Ценен как независимый невендорский сигнал по отслеживаемым моделям — с оговоркой, что это бенчмарк одного человека.

## Ключевые идеи
- **Методология:** приватные вопросы (без контаминации), балльная оценка (макс 10), рассуждение должно быть *верным* (удачные угадывания — 0 баллов), нарушение формата — 0, 3 прогона на модель с взятием максимума; колебания ±3 балла месяц к месяцу.
- **Текущий лидерборд логики (2026-09):** GPT-5.6 Sol 78.98, Kimi-K3 72.70, Opus 5 71.99, GLM-5.3 70.56 (+16.8% за месяц), GLM-5.3-Flash 66.52.
- **Лонгитюдная ценность:** ежемесячные CSV-архивы позволяют трекать траекторию семейств моделей.
- **Честная рамка:** автор прямо предупреждает «не авторитетно, не исчерпывающе — не доверяйте слепо никакой оценке».

## Подробнее
Для трекинга GLM/Kimi это сильнейший независимый кросс-модельный сигнал среди источников вики — приватные вопросы побеждают контаминацию обучением, а месячный ритм фиксирует траекторию семейств. Использовать направленно: один рейтёр и маленький банк (28 вопросов) делают отдельные месяцы шумными.

## Связанные записи
- [[llm-wiki-chinese-models-comparison]] ([Chinese Models Comparison](../models/llm-wiki-chinese-models-comparison.md))
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[kimi-k2-7-code]] ([Kimi K2.7 Code](../models/kimi-k2-7-code.md))
- [[pickleshell-model-benchmarks]] ([PickleShell Model Benchmarks](../tools/pickleshell-model-benchmarks.md))
