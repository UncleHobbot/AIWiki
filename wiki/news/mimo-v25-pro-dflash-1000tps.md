---
title: "Xiaomi Serves MiMo V2.5 Pro at 1000-3000 tok/s with DFlash + Persistent Kernel"
title_ru: "Xiaomi обслуживает MiMo V2.5 Pro со скоростью 1000-3000 ток/с с DFlash и Persistent Kernel"
category: news
tags: [xiaomi, mimo, inference, speculative-decoding, mxfp4, dflash, serving]
aliases: [MiMo-V2.5-Pro-FP4-DFlash, DFlash, Tilert]
confidence: medium
date: 2026-06-14
updated: 2026-06-14
sources:
  - https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash
  - https://mimo.xiaomi.com/blog/mimo-tilert-1000tps
  - https://www.reddit.com/r/LocalLLaMA/comments/1u5jxob/mimo_v25pro_mxfp4_dflash_xiaomi_is_serving_this/
  - https://www.reddit.com/r/LocalLLaMA/comments/1u5jtr8/xiaomi_is_now_serving_mimo_v25_at_10003000tps/
---

## Summary
Xiaomi is now serving its MiMo V2.5 Pro model at 1000-3000 tokens/sec using a new MXFP4-quantized "DFlash" variant combined with a persistent-kernel serving technique called "Tilert." The DFlash model weights are already published on Hugging Face, with a full open-source release of the serving stack promised soon.

## Key Ideas
- **DFlash** is an MXFP4-quantized version of MiMo V2.5 Pro (`XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash` on Hugging Face), designed for very high-throughput serving.
- **Tilert** is the name of the persistent-kernel serving technique Xiaomi describes in its blog post (`mimo.xiaomi.com/blog/mimo-tilert-1000tps`), credited for enabling the 1000-3000 tok/s throughput figures.
- The DFlash model weights are already released; Xiaomi has signaled the broader open-source serving stack (Tilert-related tooling) is coming soon but is not yet public.
- The 1000-3000 tok/s range likely reflects aggregate/batched throughput on Xiaomi's own serving infrastructure, not necessarily single-stream decode speed for a local user — local LocalLLaMA users should expect different numbers when self-hosting.
- This continues Xiaomi's pattern of aggressive inference-efficiency work around the MiMo line (see also MiMo-Code, Xiaomi's OpenCode fork), positioning MiMo as a speed-optimized alternative among Chinese frontier-adjacent models.

## Details
MXFP4 (4-bit microscaling floating point) is an increasingly common quantization format for high-throughput LLM serving, trading some precision for substantially reduced memory bandwidth requirements — which is often the main bottleneck for token generation speed. Combining MXFP4 quantization ("DFlash") with a "persistent kernel" approach (keeping GPU kernels resident and avoiding repeated launch overhead, referred to here as "Tilert") appears to be Xiaomi's recipe for the reported 1000-3000 tok/s figures.

Community reaction in r/LocalLLaMA was focused on whether the open-source release (promised "coming soon") would let people replicate these numbers locally, and how DFlash compares in quality to the full-precision MiMo V2.5 Pro. As of this writing, the DFlash weights are public on Hugging Face but the serving-side techniques (Tilert) are described in the blog post without full code release — so reproducing the headline throughput numbers outside Xiaomi's infrastructure isn't yet possible.

This fits into the broader 2026 trend of Chinese AI labs (Xiaomi, DeepSeek, Moonshot/Kimi, Z.ai/GLM) competing not just on raw benchmark scores but on serving efficiency and cost-per-token — an increasingly important axis given that frontier-adjacent open models are becoming "good enough" for many tasks, shifting competition toward how cheaply and quickly they can be served at scale.

## Related Entries
- [[mimo-code-xiaomi-opencode-fork]] ([MiMo-Code — Xiaomi's OpenCode Fork](../tools/mimo-code-xiaomi-opencode-fork.md))
- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models Comparison](../models/llm-wiki-chinese-models-comparison.md))

---
<!-- RU -->

## Краткое описание
Xiaomi теперь обслуживает свою модель MiMo V2.5 Pro со скоростью 1000-3000 токенов/сек, используя новый вариант с квантованием MXFP4 под названием «DFlash» в сочетании с техникой обслуживания «Tilert» на основе persistent kernel. Веса модели DFlash уже опубликованы на Hugging Face, полный открытый релиз стека обслуживания обещан в ближайшее время.

## Ключевые идеи
- **DFlash** — это версия MiMo V2.5 Pro с квантованием MXFP4 (`XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash` на Hugging Face), предназначенная для обслуживания с очень высокой пропускной способностью.
- **Tilert** — название техники обслуживания на основе persistent kernel, описанной Xiaomi в блог-посте (`mimo.xiaomi.com/blog/mimo-tilert-1000tps`), которой приписывается достижение показателей 1000-3000 ток/с.
- Веса модели DFlash уже выпущены; Xiaomi сообщила, что более широкий открытый стек обслуживания (связанный с Tilert) появится «скоро», но пока не опубликован.
- Диапазон 1000-3000 ток/с, вероятно, отражает агрегированную/батчевую пропускную способность на собственной инфраструктуре Xiaomi, а не скорость decode для одного потока у локального пользователя — при самостоятельном хостинге пользователи LocalLLaMA должны ожидать других цифр.
- Это продолжает паттерн агрессивной работы Xiaomi над эффективностью инференса в линейке MiMo (см. также MiMo-Code, форк OpenCode от Xiaomi), позиционируя MiMo как ориентированную на скорость альтернативу среди китайских frontier-моделей.

## Подробнее
MXFP4 (4-битный microscaling floating point) — всё более распространённый формат квантования для высокопроизводительного обслуживания LLM, который обменивает часть точности на существенное снижение требований к пропускной способности памяти — часто это основной узкий момент для скорости генерации токенов. Сочетание квантования MXFP4 («DFlash») с подходом «persistent kernel» (когда GPU-ядра остаются резидентными, избегая повторных накладных расходов на запуск, здесь это называется «Tilert»), по-видимому, и есть рецепт Xiaomi для заявленных 1000-3000 ток/с.

Реакция сообщества в r/LocalLLaMA сосредоточилась на том, позволит ли открытый релиз («скоро») воспроизвести эти цифры локально, и как DFlash сравнивается по качеству с полноточной MiMo V2.5 Pro. На момент написания веса DFlash публично доступны на Hugging Face, но техники обслуживания (Tilert) описаны в блог-посте без полного релиза кода — так что воспроизвести заявленную пропускную способность за пределами инфраструктуры Xiaomi пока невозможно.

Это укладывается в более широкий тренд 2026 года: китайские AI-лаборатории (Xiaomi, DeepSeek, Moonshot/Kimi, Z.ai/GLM) конкурируют не только по чистым показателям бенчмарков, но и по эффективности обслуживания и стоимости за токен — это всё более важная ось, учитывая, что открытые модели уровня frontier становятся «достаточно хороши» для многих задач, смещая конкуренцию в сторону того, насколько дёшево и быстро их можно обслуживать в масштабе.

## Связанные записи
- [[mimo-code-xiaomi-opencode-fork]] ([MiMo-Code — форк OpenCode от Xiaomi](../tools/mimo-code-xiaomi-opencode-fork.md))
- [[llm-wiki-chinese-models-comparison]] ([Сравнение китайских LLM](../models/llm-wiki-chinese-models-comparison.md))
