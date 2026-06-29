---
title: "DSpark: Speculative Decoding for DeepSeek V4 Inference Acceleration"
title_ru: "DSpark: спекулятивное декодирование для ускорения инференса DeepSeek V4"
category: concepts
tags: [speculative-decoding, inference, deepseek, dspark, llm-acceleration]
aliases: [DSpark, DeepSeek Spark, DSpark speculative decoding]
confidence: medium
updated: 2026-06-29
sources:
  - https://www.reddit.com/r/singularity/comments/1uh4k19/dspark_speculative_decoding_accelerates_llm/
  - https://www.reddit.com/r/DeepSeek/comments/1uj1jgg/is_deepseek_very_fast_for_you_guys_too/
  - https://www.reddit.com/r/DeepSeek/comments/1uivdad/is_the_new_dspark_technology_available_via/
---

## Summary
DSpark is DeepSeek's speculative decoding technique integrated into DeepSeek V4, using a lightweight draft model to predict multiple tokens ahead so the main model can verify them in a single forward pass — materially raising decode speed (tokens/second) without changing the output distribution.

## Key Ideas
- **Speculative decoding basics**: a small/fast "draft" model proposes several candidate tokens; the large "target" model verifies them in parallel. Accepted tokens are emitted at near-draft speed; rejected tokens fall back to the target model's prediction. The output distribution is provably identical to greedy/sampled decoding from the target alone.
- **DSpark in V4**: DeepSeek shipped a `DeepSeek-V4-Flash-DSpark` variant with a decoder strapped on for better speed. Users report noticeably higher tokens/second after DSpark was enabled.
- **Acceptance rate is the key metric**: the fraction of draft tokens the target accepts per step. Higher acceptance → more tokens per forward pass → faster generation. Acceptance drops on hard/ambiguous continuations.
- **Why it matters now**: as model context and parameter counts grow, raw decode speed (not just quality) becomes the bottleneck for agentic workloads that generate many tokens.
- **Availability**: community reports indicate DSpark is live in DeepSeek's web/app serving; whether the DSpark flavour is exposed via the public API was unconfirmed at time of writing.

## Details
Speculative decoding reframes autoregressive generation from "one token per forward pass" to "N candidate tokens proposed, then verified in one pass." The cost saving comes from the target model verifying k tokens in roughly the time it would take to generate one — so when the draft model is accurate, throughput multiplies.

DSpark pairs naturally with DeepSeek V4's MoE architecture: because only ~49B of ~1.6T parameters activate per token, the verification pass is already cheap relative to a dense model of comparable quality, amplifying speculative decoding's benefit.

The community discussion also connects DSpark to the broader competitive picture (e.g., comparable speculative-decoding efforts from other labs) and notes that for coding agents, the raw speed-up reduces wall-clock latency on long generations.

## Related Entries
- [[deepseek-v4-peak-pricing]] ([DeepSeek V4 Launch and Peak Pricing](../news/deepseek-v4-peak-pricing.md))
- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- [[orthrus-qwen3-acceleration]] ([Orthrus-Qwen3: Diffusion Attention Speedup](../tools/orthrus-qwen3-acceleration.md))

---
<!-- RU -->

## Краткое описание
DSpark — техника спекулятивного декодирования от DeepSeek, встроенная в DeepSeek V4: лёгкая драфт-модель предсказывает несколько токенов вперёд, а основная модель проверяет их за один forward-pass, заметно повышая скорость декодирования (токенов в секунду) без изменения распределения выходных токенов.

## Ключевые идеи
- **Основы спекулятивного декодирования**: маленькая/быстрая «драфт»-модель предлагает несколько токенов-кандидатов; большая «целевая» модель проверяет их параллельно. Принятые токены выдаются почти со скоростью драфта; отвергнутые — пересчитываются целевой моделью. Распределение выходных токенов доказуемо идентично обычному декодированию.
- **DSpark в V4**: DeepSeek выпустила вариант `DeepSeek-V4-Flash-DSpark` с подключённым декодером для большей скорости. Пользователи отмечают заметный рост токенов в секунду.
- **Acceptance rate — ключевая метрика**: доля драфт-токенов, принимаемых целевой моделью за шаг. Выше принятие → больше токенов за forward-pass → быстрее генерация.
- **Почему это важно сейчас**: с ростом контекста и числа параметров именно скорость декодирования (а не только качество) становится узким местом для агентных нагрузок с большим объёмом генерации.
- **Доступность**: сообщество сообщает, что DSpark работает в web/app-сервиринге DeepSeek; доступность DSpark-варианта через публичный API на момент записи не подтверждена.

## Подробнее
Спекулятивное декодирование переформулирует авторегрессионную генерацию: вместо «один токен за forward-pass» — «N токенов-кандидатов предложены и проверены за один проход». Экономия возникает потому, что целевая модель проверяет k токенов примерно за то же время, что и генерацию одного.

DSpark естественно сочетается с MoE-архитектурой DeepSeek V4: поскольку на токен активируется лишь ~49B из ~1.6T параметров, проверочный проход уже дешев относительно плотной модели сопоставимого качества, что усиливает выгоды спекулятивного декодирования.

## Связанные записи
- [[deepseek-v4-peak-pricing]] ([DeepSeek V4 Launch and Peak Pricing](../news/deepseek-v4-peak-pricing.md))
- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- [[orthrus-qwen3-acceleration]] ([Orthrus-Qwen3: Diffusion Attention Speedup](../tools/orthrus-qwen3-acceleration.md))
