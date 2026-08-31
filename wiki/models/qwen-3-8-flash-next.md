---
title: "Qwen 3.8 Flash Next: 125B Params, 6B Active, Hybrid Attention"
title_ru: "Qwen 3.8 Flash Next: 125B параметров, 6B активных, гибридное внимание"
category: models
tags: [qwen, alibaba, moe, sparse-attention, mtp, n-gram-embedding, local-llm, long-context, open-weights, gated-deltanet]
aliases: [Qwen3.8, Qwen 3.8 Flash Next, Qwen3.8-Flash-Next, Qwen 3.8 27B]
confidence: high
date: 2026-08-31
updated: 2026-08-31
sources:
  - https://huggingface.co/Qwen/Qwen3.8-Flash-Next
  - https://www.reddit.com/r/Qwen_AI/comments/1w1thge/
  - https://www.reddit.com/r/LocalLLaMA/comments/1w38s2d/
---

## Summary
Qwen 3.8 Flash Next is Alibaba's efficiency-focused release: 125B total parameters with only 6B activated at inference, using a hybrid Gated DeltaNet + Qwen Sparse Attention architecture, 262K native context extensible to 1M, and n-gram embeddings as an alternative to conventional MoE scaling.

## Key Ideas
- **125B total / 6B active**: plus 51B n-gram embedding parameters and 4B multi-token prediction (MTP) parameters, across 48 layers with a 2,560 hidden dimension. The design prioritizes cost-effective production deployment over raw scale.
- **Qwen Sparse Attention (QSA) at micro-block level**: unlike token-level sparse attention, QSA operates on micro-blocks, cutting latency specifically for long-context work. Paired with Gated DeltaNet in a hybrid attention scheme.
- **N-gram embedding instead of pure MoE**: an alternative parameter-scaling route that is friendlier to memory-constrained hardware — the reason this model runs well on consumer GPUs despite its total size.
- **Context: 262,144 native → 1M with YaRN/RoPE scaling**. Community threads report practical caveats around the RoPE/YaRN configuration when pushing past native length in `llama-server`.
- **Strong agentic benchmarks**: SWE-bench Pro 62.5, CoWorkBench 73.9 (long-horizon office tasks), GPQA Diamond 91.7 (scientific reasoning), ClawEval-MM 64.4 pass@3 (multimodal tool use).
- **Gated Residual**: a new residual mechanism with data-dependent gates, providing finer-grained cross-layer expressiveness while preserving training stability.

## Details

### Why the Architecture Matters
Qwen 3.8's headline claim is architectural innovation over scale. The 6B active parameter count means inference cost tracks a small model while capability tracks a much larger one. For self-hosters this is the decisive property — the r/LocalLLaMA threads accompanying the release are dominated by people fitting it onto single consumer cards.

### Community Deployment Results
Real-world numbers reported across r/LocalLLaMA and r/Qwen_AI in the days after release:
- **~75 tok/s decode** for Qwen 3.8 27B on a 16GB RTX 5080
- **>200 tok/s at 180K context** for the 27B NVFP4 quant on a single RTX 5090
- **50 t/s decode, 2,900 t/s prefill** for Flash Next NVFP4 on 2× DGX Spark
- **~25 tok/s with MTP=2** on a single DGX Spark

Quantization activity was immediate and heavy — Unsloth GGUFs, i1-IQ4_XS variants, and NVFP4 builds all appeared within the first days, with active community debate over whether hand-rolling quants is still worthwhile now that Unsloth Dynamic 3.0 exists.

### Note on Version Sprawl
The Qwen 3.8 generation spans several variants (27B, Flash Next, Coder Next) plus a large ecosystem of community fine-tunes and quantizations. Benchmark figures above are from the official Flash Next model card; per-variant numbers differ.

## Related Entries
- [[glm-5-3-release]] ([GLM-5.3: Open Weights](../models/glm-5-3-release.md))
- [[llm-wiki-chinese-models-comparison]] ([Chinese Models Comparison](../models/llm-wiki-chinese-models-comparison.md))
- [[orthrus-qwen3-acceleration]] ([Orthrus: Qwen3 Acceleration](../tools/orthrus-qwen3-acceleration.md))
- [[open-source-models-vs-opus-copilot-benchmark]] ([Open Source Models vs Opus](../models/open-source-models-vs-opus-copilot-benchmark.md))

---
<!-- RU -->

## Краткое описание
Qwen 3.8 Flash Next — релиз Alibaba с упором на эффективность: 125B общих параметров при всего 6B активных на инференсе, гибридная архитектура Gated DeltaNet + Qwen Sparse Attention, контекст 262K с расширением до 1M и n-gram эмбеддинги как альтернатива обычному масштабированию MoE.

## Ключевые идеи
- **125B всего / 6B активных**: плюс 51B параметров n-gram эмбеддингов и 4B параметров multi-token prediction (MTP), 48 слоёв, скрытая размерность 2560.
- **Qwen Sparse Attention (QSA) на уровне микроблоков**: в отличие от разреженного внимания на уровне токенов, QSA работает с микроблоками, снижая задержку именно для длинного контекста.
- **N-gram эмбеддинги вместо чистого MoE**: альтернативный путь масштабирования параметров, более дружелюбный к железу с ограниченной памятью — причина, по которой модель хорошо идёт на потребительских GPU.
- **Контекст: 262 144 нативно → 1M через YaRN/RoPE**. В обсуждениях сообщества отмечаются нюансы настройки RoPE/YaRN при выходе за нативную длину в `llama-server`.
- **Сильные агентные бенчмарки**: SWE-bench Pro 62.5, CoWorkBench 73.9, GPQA Diamond 91.7, ClawEval-MM 64.4 pass@3.
- **Gated Residual**: новый механизм остаточных связей с зависящими от данных гейтами.

## Подробнее

**Почему важна архитектура.** Главное заявление Qwen 3.8 — архитектурная инновация вместо масштаба. 6B активных параметров означают, что стоимость инференса соответствует небольшой модели, а способности — гораздо большей.

**Результаты развёртывания у сообщества** в первые дни после релиза: ~75 tok/s декодирования для 27B на 16GB RTX 5080; более 200 tok/s при контексте 180K для NVFP4-кванта 27B на одной RTX 5090; 50 t/s декодирования и 2900 t/s prefill для Flash Next NVFP4 на 2× DGX Spark.

Квантование началось немедленно: GGUF от Unsloth, варианты i1-IQ4_XS и сборки NVFP4 появились в первые дни, с активной дискуссией о том, стоит ли собирать кванты вручную теперь, когда есть Unsloth Dynamic 3.0.

## Связанные записи
- [[glm-5-3-release]] ([GLM-5.3: открытые веса](../models/glm-5-3-release.md))
- [[llm-wiki-chinese-models-comparison]] ([Сравнение китайских моделей](../models/llm-wiki-chinese-models-comparison.md))
- [[orthrus-qwen3-acceleration]] ([Orthrus: ускорение Qwen3](../tools/orthrus-qwen3-acceleration.md))
- [[open-source-models-vs-opus-copilot-benchmark]] ([Open Source модели против Opus](../models/open-source-models-vs-opus-copilot-benchmark.md))
