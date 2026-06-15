---
title: "Kimi K2.7-Code Released — Open-Sourced Coding Model with Lower Reasoning Overhead"
title_ru: "Выход Kimi K2.7-Code — открытая модель для кодинга со сниженной нагрузкой на рассуждения"
category: news
tags: [kimi, moonshot, k2.7, coding-model, open-source, release]
aliases: [Kimi K2.7, K2.7-Code, Kimi K2.7-Code]
confidence: low
date: 2026-06-12
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/kimi/comments/1u3ri2w/kimik27code_our_latest_coding_model_is_now/
  - https://www.reddit.com/r/kimi/comments/1u3sefv/kimi_k27_is_out_yo_live_on_kimi_code_now/
  - https://www.reddit.com/r/kimi/comments/1u4sacc/kimi_k27_goes_caveman_mode_to_save_tokens/
  - https://www.reddit.com/r/kimi/comments/1u4a2yy/does_the_new_kimi_k27_use_up_your_credits_twice/
---

## Summary
Moonshot AI released and open-sourced Kimi K2.7-Code, an upgrade to its coding/agent model that the company says improves coding and agent benchmark scores over K2.6 while cutting reasoning-token usage by 30%, available immediately via the Kimi API and Kimi Code CLI.

## Key Ideas
- Moonshot's official announcement claims +21.8% on "Kimi Code Bench v2", +11.0% on "Program Bench", and +31.5% on "MLS Bench Lite" versus K2.6 — all unverified vendor-reported benchmarks (Tier 3, community-relayed).
- Claimed 30% lower reasoning-token usage compared to K2.6 ("less overthinking"), aimed at improving long-horizon coding task success and instruction-following.
- A "6x High-Speed Mode" was teased as "coming soon" but not yet available at release.
- Available immediately through the Kimi API and the [[kimi-code-cli]] tool (model ID reportedly still `kimi-for-coding`).
- Community reaction is mixed on cost: despite the "30% less reasoning" claim, several users on paid plans (e.g. the $40 "Alegretto"/Moderato tiers) report K2.7 consuming credits/quota faster than K2.6 in practice — possibly due to longer or more frequent tool-call loops rather than raw reasoning tokens.
- Separately, users noted K2.7 sometimes switches to a terse "caveman mode" (short, fragment-like responses) apparently as a token-saving behavior, which some found jarring.

## Details
K2.7-Code is positioned as an iterative but meaningful upgrade within Moonshot's Kimi K2 coding line, following K2.6 (covered in [[kimi-2-6-vs-glm-5-1-agent-reliability]] and [[deepseek-v4-vs-opus-kimi]]). The headline pitch — better coding benchmarks plus fewer reasoning tokens — would be a notable efficiency win if it holds up under independent testing, since reasoning-token overhead is a major cost driver for agentic coding workloads.

However, early hands-on reports from r/kimi complicate the efficiency story: multiple users on metered plans report K2.7 burning through hourly/weekly quotas faster than K2.6 for similar tasks, with one user noting a single prompt consumed 3% of a 5-hour limit. This may reflect increased tool-calling/agentic loop activity rather than the reasoning-token metric Moonshot highlighted, or simply early-release calibration issues with usage accounting. As with the GLM-5.2 release the same week (see [[glm-5-2-release]]), treat vendor benchmark percentages as directional until independently reproduced.

## Related Entries
- [[kimi-code-cli]] ([Kimi Code CLI](../tools/kimi-code-cli.md))
- [[kimi-2-6-vs-glm-5-1-agent-reliability]] ([Kimi 2.6 vs GLM 5.1](../models/kimi-2-6-vs-glm-5-1-agent-reliability.md))
- [[deepseek-v4-vs-opus-kimi]] ([DeepSeek V4 vs Opus vs Kimi](../models/deepseek-v4-vs-opus-kimi.md))
- [[glm-5-2-release]] ([GLM-5.2 Release](../news/glm-5-2-release.md))

---
<!-- RU -->

## Краткое описание
Moonshot AI выпустила и открыла исходный код Kimi K2.7-Code — обновление модели для кодинга и агентов, которое, по заявлению компании, улучшает показатели бенчмарков по кодингу и агентным задачам по сравнению с K2.6, сократив при этом использование reasoning-токенов на 30%. Доступна сразу через Kimi API и Kimi Code CLI.

## Ключевые идеи
- По официальному анонсу Moonshot: +21.8% на "Kimi Code Bench v2", +11.0% на "Program Bench" и +31.5% на "MLS Bench Lite" по сравнению с K2.6 — неподтверждённые показатели от вендора (Tier 3, через сообщество).
- Заявлено снижение использования reasoning-токенов на 30% по сравнению с K2.6 ("меньше переосмысления"), что должно улучшить успешность долгих агентных задач кодинга и следование инструкциям.
- Анонсирован "режим 6x High-Speed", но на момент релиза он ещё не доступен ("скоро").
- Доступна сразу через Kimi API и инструмент [[kimi-code-cli]] (ID модели по сообщениям всё ещё `kimi-for-coding`).
- Реакция сообщества по поводу стоимости неоднозначна: несмотря на заявление "на 30% меньше reasoning", несколько пользователей платных тарифов (например, $40 "Alegretto"/Moderato) сообщают, что K2.7 расходует кредиты/квоту быстрее, чем K2.6, на похожих задачах — возможно из-за более длинных или частых циклов вызова инструментов, а не из-за самих reasoning-токенов.
- Отдельно пользователи отметили, что K2.7 иногда переходит в лаконичный "caveman mode" (короткие, обрывочные ответы) — видимо, как поведение для экономии токенов, что некоторых смутило.

## Подробнее
K2.7-Code — итеративное, но заметное обновление в линейке Kimi K2 для кодинга от Moonshot, после K2.6 (см. [[kimi-2-6-vs-glm-5-1-agent-reliability]] и [[deepseek-v4-vs-opus-kimi]]). Главный тезис — улучшенные бенчмарки кодинга при меньшем числе reasoning-токенов — был бы значимой победой в эффективности, если подтвердится независимыми тестами, поскольку накладные расходы на reasoning-токены — основной фактор стоимости агентных задач кодинга.

Однако первые отзывы с r/kimi усложняют картину эффективности: несколько пользователей на тарифах с лимитами сообщают, что K2.7 расходует часовые/недельные квоты быстрее, чем K2.6, на похожих задачах — один пользователь отметил, что один промпт израсходовал 3% 5-часового лимита. Это может отражать рост активности агентных циклов вызова инструментов, а не метрику reasoning-токенов, на которую ссылается Moonshot, либо проблемы калибровки учёта использования на раннем этапе релиза. Как и с релизом GLM-5.2 на той же неделе (см. [[glm-5-2-release]]), к процентным показателям вендора стоит относиться как к ориентировочным до независимой проверки.

## Связанные записи
- [[kimi-code-cli]] ([Kimi Code CLI](../tools/kimi-code-cli.md))
- [[kimi-2-6-vs-glm-5-1-agent-reliability]] ([Kimi 2.6 vs GLM 5.1](../models/kimi-2-6-vs-glm-5-1-agent-reliability.md))
- [[deepseek-v4-vs-opus-kimi]] ([DeepSeek V4 vs Opus vs Kimi](../models/deepseek-v4-vs-opus-kimi.md))
- [[glm-5-2-release]] ([Релиз GLM-5.2](../news/glm-5-2-release.md))
