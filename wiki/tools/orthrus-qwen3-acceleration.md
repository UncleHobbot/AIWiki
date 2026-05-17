---
title: "Orthrus-Qwen3: Diffusion Attention for 7.8x LLM Speedup"
title_ru: "Orthrus-Qwen3: Диффузионное внимание для ускорения LLM в 7.8 раз"
category: tools
tags: [diffusion, acceleration, speculative-decoding, qwen3, llm-efficiency]
updated: 2026-05-15
sources:
  - https://github.com/chiennv2000/orthrus
  - https://arxiv.org/abs/2605.12825
  - https://www.reddit.com/r/LocalLLaMA/comments/1te5xpu/orthrusqwen38b_up_to_78tokensforward_on_qwen38b/
---

## Summary

Orthrus adds a parallel diffusion attention head to frozen autoregressive transformers, achieving up to 7.8x tokens/forward with provably identical output distributions.

## Key Ideas
- Trainable diffusion attention module injected into each layer alongside frozen AR backbone
- Both heads share a single KV cache — overhead is O(1), approximately 4.5 MiB
- Diffusion head projects 32 tokens in parallel; AR head verifies and accepts longest matching prefix
- Output distribution is mathematically identical to the frozen base model
- Single-step denoising outperforms multi-step (6.35 vs 3.53 TPF)
- KL distillation beats cross-entropy on acceptance rate

## Details

Orthrus freezes the entire base model and trains only the diffusion attention modules (16% of total parameters). Training requires less than 1 billion tokens and completes in 24 hours on 8x H200 GPUs.

On MATH-500, the acceptance length reaches 11.7 tokens compared to 7.9 for DFlash and 3.5 for EAGLE-3. Unlike speculative decoding approaches, Orthrus requires no external drafter model, no separate KV cache, and has zero time-to-first-token penalty because there is no drafter to initialize and synchronize.

Compared to diffusion language models like Dream, Fast-dLLM-v2, SDAR, and Mercury, Orthrus does not modify the base model weights. This means accuracy matches Qwen3-8B exactly, while diffusion LMs that modify weights lose accuracy (e.g., Fast-dLLM-v2 drops 11 points on MATH-500).

The community expressed strong interest in seeing this technique applied to larger models like Qwen 3.6 27B.

## Related Entries
- [[dynamic-compute-budget-local-llm]] ([Dynamic Compute Budget Allocation for Local LLMs](../tips/dynamic-compute-budget-local-llm.md))
- [[deepseek-v4-vs-opus-kimi]] ([DeepSeek V4 Pro vs Claude Opus 4.7 vs Kimi K2.6 Benchmark](../models/deepseek-v4-vs-opus-kimi.md))

---
<!-- RU -->

## Краткое описание

Orthrus добавляет параллельный модуль диффузионного внимания к замороженным авторегрессионным трансформерам, достигая ускорения до 7.8x по токенам за проход с математически идентичным распределением выходов.

## Ключевые идеи
- Обучаемый модуль диффузионного внимания внедряется в каждый слой рядом с замороженной AR-основа
- Обе головки используют общий KV-кэш — накладные расходы O(1), около 4.5 МиБ
- Диффузионная головка проецирует 32 токена параллельно; AR-головка проверяет и принимает наибольший совпадающий префикс
- Распределение выходов математически идентично замороженной базовой модели
- Одношаговое шумоподавление превосходит многошаговое (6.35 vs 3.53 TPF)
- KL-дистилляция превосходит кросс-энтропию по уровню принятия

## Подробнее

Orthrus замораживает всю базовую модель и обучает только модули диффузионного внимания (16% от общего числа параметров). Обучение требует менее 1 миллиарда токенов и завершается за 24 часа на 8x H200 GPU.

На MATH-500 длина принятия достигает 11.7 токенов по сравнению с 7.9 для DFlash и 3.5 для EAGLE-3. В отличие от подходов спекулятивного декодирования, Orthrus не требует внешней модели-генератора, отдельного KV-кэша и имеет нулевой штраф на время до первого токена.

По сравнению с диффузионными языковыми моделями, Orthrus не модифицирует веса базовой модели, что означает полное сохранение точности Qwen3-8B.

Сообщество выразило большой интерес к применению этой техники к большим моделям, таким как Qwen 3.6 27B.

## Связанные записи
- [[dynamic-compute-budget-local-llm]] ([Dynamic Compute Budget Allocation for Local LLMs](../tips/dynamic-compute-budget-local-llm.md))
- [[deepseek-v4-vs-opus-kimi]] ([DeepSeek V4 Pro vs Claude Opus 4.7 vs Kimi K2.6 Benchmark](../models/deepseek-v4-vs-opus-kimi.md))
