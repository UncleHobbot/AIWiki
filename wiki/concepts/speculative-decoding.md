---
title: "Speculative Decoding"
title_ru: "Спекулятивное декодирование"
category: concepts
tags: [speculative-decoding, mtp, multi-token-prediction, inference]
aliases: [Speculative Decoding, Spec Decoding, Multi-Token Prediction, MTP]
confidence: high
updated: 2026-06-14
sources:
  - https://arxiv.org/abs/2211.17192
  - https://arxiv.org/abs/2401.04088
---

## Summary

Speculative decoding is an inference acceleration technique where a small, fast "draft" model proposes multiple upcoming tokens and the large target model verifies them in a single forward pass. Because verification is cheaper than generation, accepted tokens are produced several at a time, increasing throughput without changing the output distribution.

## Key Ideas

- **Draft + verify:** a lightweight draft model guesses the next K tokens; the target model checks all K in one parallel forward pass, accepting those that match its distribution.
- **Math-free fidelity:** the technique is rejection-sampled so the final output distribution is identical to standard autoregressive decoding — quality is preserved.
- **Multi-Token Prediction (MTP):** a closely related variant where the model itself is trained to predict multiple future tokens, often used as the draft mechanism (e.g., in DeepSeek-style and Gemma QAT models).
- **Speedup is hardware-dependent:** gains are largest when verification is cheap relative to a separate draft pass (fast CUDA GPUs) and can vanish or regress on unified-memory architectures like Apple Silicon.
- **Widely adopted:** supported in inference engines like vLLM, TensorRT-LLM, and Ollama.

## Details

Standard autoregressive decoding generates one token per forward pass, leaving the model's parallel capacity underused. Speculative decoding exploits that headroom: the draft model produces several candidate tokens cheaply, and the target model evaluates them together. Each accepted token is essentially "free" compared to generating it standalone, so the more the draft agrees with the target, the bigger the speedup.

The practical catch is that the win depends on hardware and draft accuracy. On fast CUDA GPUs, batched verification is nearly free, yielding up to ~2x throughput. On Apple Silicon with unified memory, the draft-model overhead can exceed the verification savings, producing slower-than-baseline results. The practical guidance is therefore to benchmark MTP/speculative decoding on real hardware rather than assume a universal speedup.

## Notable Quotes

> "Speculative decoding uses a small draft model to propose tokens that a large model verifies in parallel — accelerating inference with no loss in quality." — Leviathan et al., 2022

## Related Entries

- [[mtp-hardware-dependent-speedup]] ([MTP Hardware-Dependent Speedup](../tips/mtp-hardware-dependent-speedup.md))
- [[ollama]] ([Ollama](../tools/ollama.md))

---
<!-- RU -->

## Краткое описание

Спекулятивное декодирование — техника ускорения инференса, при которой небольшая быстрая «черновая» модель предлагает несколько следующих токенов, а большая целевая модель проверяет их за один прямой проход. Поскольку верификация дешевле генерации, принятые токены выдаются сразу по несколько штук, повышая пропускную способность без изменения распределения вывода.

## Ключевые идеи

- **Черновик + проверка:** лёгкая черновая модель угадывает следующие K токенов; целевая модель проверяет все K за один параллельный прямой проход, принимая те, что совпадают с её распределением.
- **Точность без математики:** техника основана на rejection sampling, поэтому итоговое распределение вывода идентично стандартному авторегрессионному декодированию — качество сохраняется.
- **Multi-Token Prediction (MTP):** близкий вариант, при котором сама модель обучается предсказывать несколько будущих токенов и часто используется как механизм черновика (например, в моделях в стиле DeepSeek и Gemma QAT).
- **Ускорение зависит от оборудования:** выигрыш максимален, когда верификация дёшева относительно отдельного прохода черновика (быстрые CUDA GPU), и может исчезать или регрессировать на архитектурах с унифицированной памятью вроде Apple Silicon.
- **Широко внедрено:** поддерживается в движках инференса, таких как vLLM, TensorRT-LLM и Ollama.

## Подробнее

Стандартное авторегрессионное декодирование генерирует один токен за прямой проход, недоиспользуя параллельную ёмкость модели. Спекулятивное декодирование задействует этот запас: черновая модель дёшево производит несколько токенов-кандидатов, а целевая модель оценивает их вместе. Каждый принятый токен по сути «бесплатен» по сравнению с его самостоятельной генерацией, поэтому чем больше черновик совпадает с целевой моделью, тем выше ускорение.

Практическая загвоздка в том, что выигрыш зависит от оборудования и точности черновика. На быстрых CUDA GPU пакетная верификация почти бесплатна, давая до ~2x пропускной способности. На Apple Silicon с унифицированной памятью накладные расходы черновой модели могут превысить экономию от верификации, давая результаты медленнее базовых. Поэтому практическое руководство — делать бенчмарк MTP/спекулятивного декодирования на реальном оборудовании, а не предполагать универсальное ускорение.

## Примечательные цитаты

> «Спекулятивное декодирование использует небольшую черновую модель для предложения токенов, которые большая модель проверяет параллельно — ускоряя инференс без потери качества.» — Leviathan et al., 2022

## Связанные записи

- [[mtp-hardware-dependent-speedup]] ([MTP Hardware-Dependent Speedup](../tips/mtp-hardware-dependent-speedup.md))
- [[ollama]] ([Ollama](../tools/ollama.md))
