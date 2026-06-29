---
title: "DeepSeek V4 Official Launch and Peak/Off-Peak API Pricing"
title_ru: "Официальный запуск DeepSeek V4 и пиковое/внепиковое ценообразование API"
category: news
tags: [deepseek, v4, api-pricing, peak-pricing, inference-cost]
aliases: [DeepSeek V4 peak pricing, DeepSeek peak-valley pricing, DSV4 pricing]
confidence: high
date: 2026-06-29
updated: 2026-06-29
sources:
  - https://www.reddit.com/r/DeepSeek/comments/1uio6yf/deepseek_v4_official_launch_peakoffpeak_pricing/
  - https://www.reddit.com/r/DeepSeek/comments/1uiq1lk/v4_peak_pricing_is_coming_midjuly_heres_how_to/
  - https://www.reddit.com/r/DeepSeek/comments/1uiv3uo/heres_a_concise_technicalfocused_summary_of_what/
  - https://www.reddit.com/r/GithubCopilot/comments/1uiyv1i/deepseek_to_double_token_cost_in_middle_of_july/
---

## Summary
DeepSeek announced the official (formal) release of V4 for mid-July 2026, paired with a new **peak/valley (time-of-day) pricing** model where API calls during designated peak hours cost **2× the regular rate**. Regular off-peak prices for both V4-Pro and V4-Flash remain unchanged.

## Key Ideas
- **Official launch mid-July 2026**: V4 transitions from preview to formal release, with a 24-hour advance notice before any pricing change takes effect.
- **Peak hours (UTC)**: 01:00–04:00 and 06:00–10:00 — only ~7 hours/day are peak; everything else stays at the existing rate. (Beijing-time equivalent: 09:00–12:00 and 14:00–18:00.)
- **2× multiplier applies to ALL token billing** — input (cache hit and miss) and output — for `deepseek-v4-pro` and `deepseek-v4-flash`.
- **Signal**: LLM API pricing is evolving from a flat per-call interface toward an electricity-grid-style schedulable compute market, where call timing, batching, and cost windows become an optimization axis.
- **Architecture enablers** (per community technical summary): hybrid CSA/HCA attention (Compressed Sparse + Heavily Compressed Attention) makes 1M-token context affordable; **Engram memory** separates long-term memory from active GPU cache with O(1) lookup; **Manifold-Constrained Hyper-Connections (mHC)** stabilize very deep MoE stacks.

## Details
The peak/valley mechanism is a load-balancing move. At 1M tokens, V4-Pro reportedly uses ~27% of V3.2's FLOPs and ~10% of its KV cache, making repo-scale code and long agent runs economically viable — but demand concentrated in certain hours strains capacity, hence time-of-day pricing.

**Practical mitigation (community tips):**
- Batch jobs, evals, and non-real-time workloads: cron them for off-peak windows to keep the old rate.
- US workdays fall mostly in the cheap window already.
- Turn off **thinking mode** for simple tasks — those tokens bill as output, where peak doubling hurts most.
- Continued usage after a pricing change = acceptance; users can opt out and request a refund.

## Notable Quotes
> "LLM API 正在从'固定价格的调用接口'，逐渐变成'类似电价的算力资源市场'。" — r/DeepSeek (translated: LLM APIs are evolving from fixed-price call interfaces into an electricity-tariff-like compute-resource market)

## Related Entries
- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- [[dspark-speculative-decoding]] ([DSpark: Speculative Decoding](../concepts/dspark-speculative-decoding.md))
- [[huawei-deepseek-v4-ascend-training]] ([Huawei-Led DeepSeek V4 Training on Ascend](huawei-deepseek-v4-ascend-training.md))

---
<!-- RU -->

## Краткое описание
DeepSeek анонсировала официальный релиз V4 на середину июля 2026 года вместе с новой моделью **пикового/внепикового (повременного) ценообразования**, при которой вызовы API в designated пиковые часы стоят **в 2 раза дороже обычной ставки**. Обычные внепиковые цены для V4-Pro и V4-Flash не меняются.

## Ключевые идеи
- **Официальный запуск в середине июля 2026**: V4 переходит из превью в формальный релиз, с уведомлением за 24 часа до любых изменений цен.
- **Пиковые часы (UTC)**: 01:00–04:00 и 06:00–10:00 — только ~7 часов в день пиковые; остальное время — по прежней ставке (по Пекину: 09:00–12:00 и 14:00–18:00).
- **Множитель 2× применяется ко ВСЕЙ биллинговой статистике** — input (cache hit и miss) и output — для `deepseek-v4-pro` и `deepseek-v4-flash`.
- **Сигнал**: ценообразование LLM API эволюционирует от фиксированного интерфейса за вызов к рынку планируемых вычислительных ресурсов по типу электротариффа, где время вызова, батчинг и окна стоимости становятся осью оптимизации.
- **Архитектурные новшества**: гибридное CSA/HCA внимание делает 1M-контекст доступным; **Engram memory** отделяет долгосрочную память от активного GPU-кэша с O(1) поиском; **mHC** стабилизирует очень глубокие MoE-стеки.

## Подробнее
Механизм peak/valley — это ход для балансировки нагрузки. На 1M токенов V4-Pro якобы использует ~27% FLOPs и ~10% KV-кэша от V3.2, делая работу с кодом масштаба репозитория и длинные agent-сессии экономически жизнеспособными — но спрос, сконцентрированный в определённые часы, перегружает мощности, отсюда повременное ценообразование.

**Практическая адаптация (советы сообщества):**
- Батч-задачи, эвалюации и нереалтайм-нагрузки: запускайте по cron во внепиковые окна.
- В США рабочий день в основном попадает в дешёвое окно.
- Отключайте **thinking mode** для простых задач — эти токены тарифицируются как output, где пиковое удвоение бьёт сильнее всего.

## Связанные записи
- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- [[dspark-speculative-decoding]] ([DSpark: Speculative Decoding](../concepts/dspark-speculative-decoding.md))
- [[huawei-deepseek-v4-ascend-training]] ([Huawei-Led DeepSeek V4 Training on Ascend](huawei-deepseek-v4-ascend-training.md))
