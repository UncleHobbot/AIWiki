---
title: "Unsloth Qwen3.8-27B GGUF — Dynamic Quants for Local Inference"
title_ru: "Unsloth Qwen3.8-27B GGUF — динамические кванты для локального инференса"
category: models
tags: [qwen, unsloth, gguf, quantization, local-llm, vision, mtp, 256k-context]
aliases: [Qwen3.8 27B GGUF, unsloth qwen3.8, qwen3.8 quants]
confidence: high
updated: 2026-09-01
sources:
  - https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
---

## Summary
Unsloth's quantized GGUF release of Qwen3.8-27B (Apache-2.0 base): 20+ "UD" (Unsloth Dynamic) variants from ~6 GB (UD-IQ1_S) to ~31 GB (UD-Q8_K_XL), plus standard K-quants and BF16 — built on the `qwen3_5` architecture with **262,144-token context and vision support** (mmproj projectors included), a separate MTP weight file for speculative decoding, and an imatrix calibration file for llama.cpp-family runtimes.

## Key Ideas
- **UD dynamic quants:** selectively keep higher precision on sensitive layers — the mid-range anchors are UD-Q2_K_XL (~9.8 GB), UD-Q4_K_M (~16.5 GB), UD-Q6_K (~22 GB).
- **Vision-capable:** mmproj-BF16/F16 projector files (~0.93 GB) ship in-repo.
- **MTP speculative decoding:** `mtp-Qwen3.8-27B-Q4_0.gguf` (~1.37 GB) shipped separately — the same multi-token-prediction latency trick as Tencent Hy4 ([[tencent-hy4-preview]]).
- **262K context** on a 27B-class model makes it a serious local long-context option.
- Full size spectrum: ~6 GB (IQ1) → ~31 GB (Q8) → ~55 GB (BF16 sharded); total repo ~1.05 TB.

## Details
For local-agent builders this is the practical "one model, many machines" release: a 16–22 GB quant fits a 24 GB card with 256K context and vision, while the 6–10 GB tiers serve laptop-class setups. Unsloth's UD line has become the default GGUF distillation for open models; pairing with the MTP file is the newer twist worth testing in llama.cpp when support lands.

## Related Entries
- [[tencent-hy4-preview]] ([Tencent Hy4 Preview](../news/tencent-hy4-preview.md))
- [[ollama]] ([Ollama](../tools/ollama.md))
- [[llm-wiki-chinese-models-comparison]] ([Chinese Models Comparison](llm-wiki-chinese-models-comparison.md))
- [[clifford-control-plane-local-ai]] ([Clifford Control Plane](../tools/clifford-control-plane-local-ai.md))

---
- [[sliding-window-beats-linear-attention]] ([Sliding-Window Beats Linear Attention](../research/sliding-window-beats-linear-attention.md))
- [[qwen38-27b-rtx-5080-tuning]] ([Qwen3.8-27B on RTX 5080](../tips/qwen38-27b-rtx-5080-tuning.md))
<!-- RU -->

## Краткое описание
Квантованный GGUF-релиз Unsloth для Qwen3.8-27B (база Apache-2.0): 20+ вариантов «UD» (Unsloth Dynamic) от ~6 ГБ (UD-IQ1_S) до ~31 ГБ (UD-Q8_K_XL), плюс стандартные K-кванты и BF16 — на архитектуре `qwen3_5` с **контекстом 262 144 токена и поддержкой зрения** (mmproj-проекторы в комплекте), отдельным файлом весов MTP для спекулятивного декодирования и imatrix-файлом калибровки для рантаймов семейства llama.cpp.

## Ключевые идеи
- **UD-динамические кванты:** избирательно сохраняют повышенную точность на чувствительных слоях — средние якоря: UD-Q2_K_XL (~9.8 ГБ), UD-Q4_K_M (~16.5 ГБ), UD-Q6_K (~22 ГБ).
- **Зрение:** mmproj-BF16/F16 проекторы (~0.93 ГБ) в репо.
- **MTP-спекулятивное декодирование:** `mtp-Qwen3.8-27B-Q4_0.gguf` (~1.37 ГБ) отдельным файлом — тот же трюк, что у Tencent Hy4.
- **262K контекста** у модели класса 27B — серьёзная локальная опция для длинного контекста.
- Полный спектр: ~6 ГБ (IQ1) → ~31 ГБ (Q8) → ~55 ГБ (BF16); весь репо ~1.05 ТБ.

## Подробнее
Для билдеров локальных агентов это практичный релиз «одна модель — много машин»: квант 16–22 ГБ влезает в карту 24 ГБ с контекстом 256K и зрением, а тиры 6–10 ГБ — для ноутбуков. Линия UD стала дефолтной GGUF-дистилляцией открытых моделей; связка с MTP-файлом — новая фишка для тестирования в llama.cpp.

## Связанные записи
- [[tencent-hy4-preview]] ([Tencent Hy4 Preview](../news/tencent-hy4-preview.md))
- [[ollama]] ([Ollama](../tools/ollama.md))
- [[llm-wiki-chinese-models-comparison]] ([Chinese Models Comparison](llm-wiki-chinese-models-comparison.md))
- [[clifford-control-plane-local-ai]] ([Clifford Control Plane](../tools/clifford-control-plane-local-ai.md))
