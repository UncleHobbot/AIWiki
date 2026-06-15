---
title: "MTP Hardware-Dependent Speedup (Gemma 4)"
title_ru: "Ускорение MTP зависит от железа (Gemma 4)"
category: tips
tags: [mtp, multi-token-prediction, gemma-4, inference-speed, hardware, ollama]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://bric.pe.kr/blog/mtp-hardware-dependent-gemma-12b-3090-vs-m1-max
  - https://www.reddit.com/r/ollama/comments/1u2s7kf/gemma_4_12b_qat_mtp_195x_on_my_3090_but_087x/
---

## Summary
Multi-Token Prediction (MTP) speedup varies drastically by hardware. Gemma 4 12B QAT + MTP delivers 1.95x on RTX 3090 but 0.87x (slower) on M1 Max. MTP only helps when the verify pass is cheap relative to running the draft model.

## Key Ideas
- MTP with Gemma 4 12B QAT: 1.95x speedup on RTX 3090 (167 vs 86 tokens/sec)
- 1.74x on RTX 5070 Ti laptop — still a strong gain
- 0.87x on M1 Max — actually slower with MTP enabled
- MTP only pays off when the verification pass is cheap compared to the draft forward pass
- Fast CUDA GPUs benefit; Apple Silicon unified memory does not (draft overhead eats the gain)
- Always measure before assuming MTP helps your hardware

## Details
Multi-Token Prediction is a speculative decoding technique where a draft model proposes multiple next tokens and the main model verifies them in a single forward pass. The speedup depends on how cheap that verification is relative to running the draft model separately.

On an RTX 3090, the CUDA architecture makes the verify pass extremely fast, so the draft model's proposals get validated almost for free — resulting in nearly 2x throughput. The RTX 5070 Ti laptop shows a similar pattern at 1.74x. But on Apple's M1 Max with unified memory, the memory bandwidth and compute characteristics are different enough that the draft overhead exceeds the savings from batch verification, making MTP counterproductive.

The practical takeaway: MTP is not a universal speedup knob. Before enabling it in Ollama or any inference engine, benchmark on your actual hardware. The 3090 result is impressive, but the M1 Max regression is a reminder that hardware architecture matters more than the technique itself.

## Related Entries
- [[speculative-decoding]] ([Speculative Decoding](../concepts/speculative-decoding.md))
- [[ollama]] ([Ollama Tips](../tips/ollama-tips.md))

---
<!-- RU -->

## Краткое описание
Ускорение Multi-Token Prediction (MTP) радикально зависит от оборудования. Gemma 4 12B QAT + MTP даёт 1.95x на RTX 3090, но 0.87x (медленнее) на M1 Max. MTP помогает только тогда, когда проход верификации дешев относительно запуска черновой модели.

## Ключевые идеи
- MTP с Gemma 4 12B QAT: ускорение 1.95x на RTX 3090 (167 против 86 токенов/сек)
- 1.74x на RTX 5070 Ti laptop — всё ещё заметный прирост
- 0.87x на M1 Max — с MTP фактически медленнее
- MTP окупается только когда верификация дешёва по сравнению с прямым проходом черновой модели
- Быстрые CUDA GPU выигрывают; унифицированная память Apple Silicon — нет (накладные расходы черновика съедают выигрыш)
- Всегда измеряйте перед тем как предполагать, что MTP поможет вашему оборудованию

## Подробнее
Multi-Token Prediction — это техника спекулятивного декодирования, при которой черновая модель предлагает несколько следующих токенов, а основная модель верифицирует их за один прямой проход. Ускорение зависит от того, насколько дешёвая эта верификация по сравнению с отдельным запуском черновой модели.

На RTX 3090 архитектура CUDA делает проход верификации крайне быстрым, поэтому предложения черновой модели проверяются почти бесплатно — результат почти двукратный прирост пропускной способности. RTX 5070 Ti laptop показывает аналогичную картину с 1.74x. Но на M1 Max с унифицированной памятью характеристики пропускной способности памяти и вычислений достаточно отличаются, чтобы накладные расходы черновика превысили экономию от пакетной верификации, сделав MTP контрпродуктивным.

Практический вывод: MTP — не универсальный регулятор ускорения. Перед включением в Ollama или любом движке инференса — сделайте бенчмарк на вашем реальном оборудовании. Результат на 3090 впечатляет, но регрессия на M1 Max напоминает, что архитектура железа важнее самой техники.

## Связанные записи
- [[speculative-decoding]] ([Speculative Decoding](../concepts/speculative-decoding.md))
- [[ollama]] ([Ollama Tips](../tips/ollama-tips.md))
