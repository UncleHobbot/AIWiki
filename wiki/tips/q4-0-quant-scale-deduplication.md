---
title: "Deduplicating Quantization Scales to Shrink Q4_0 GGUF Files"
title_ru: "Дедупликация scale-значений для уменьшения GGUF-файлов в Q4_0"
category: tips
tags: [quantization, gguf, q4_0, llama-cpp, qwen, model-compression]
aliases: [scale deduplication, Q4_0 size reduction]
confidence: low
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/LocalLLaMA/comments/1u56gdy/storing_an_index_to_a_scale_instead_of_the_scale/
---

## Summary
A LocalLLaMA user found that Q4_0-quantized GGUF weight files contain many duplicate per-block "scale" values, and that storing an index into a small table of unique scales (instead of repeating the scale itself) could shrink a Qwen3.6-27B Q4_0 file by roughly 318MB (~2% of ~15GB) — though it requires custom inference code to decode.

## Key Ideas
- Q4_0 quantization stores a scale factor per block of weights alongside the 4-bit quantized values; the post found that many of these scale values repeat across blocks in both Qwen3.5-2B and Qwen3.6-27B.
- Instead of storing the full scale value for every block, you could store a small dictionary of unique scales plus a per-block index into that dictionary — a classic dictionary-compression / delta-encoding idea applied to quantization metadata.
- Napkin-math estimate for Qwen3.6-27B (Q4_0, ~15GB, 64 layers): each sub-layer (ffn_down/ffn_gate/ffn_up, ~89.1M weights each) is ~47.8MB, and across the model this scale-deduplication could reclaim a minimum of ~318MB.
- The author is explicit this is a small, "interesting but not huge" gain (~2%), and that it's not necessarily universal across all models — only verified empirically on two Qwen checkpoints.
- The catch: exploiting this requires **custom inference code** — standard llama.cpp / GGUF readers expect scales stored inline, not as dictionary indices, so this isn't a drop-in quantization flag.

## Details
This is exploratory, hobbyist-level research (Reddit, confidence: low) rather than a shipped feature, but it's a useful data point for anyone interested in squeezing more out of GGUF quantization formats. The author was originally investigating whether duplicate *weight* values (not scales) could be exploited for compression, and stumbled onto the fact that the per-block scale factors — which Q4_0 stores alongside the quantized weights to allow dequantization — are themselves highly repetitive.

The proposed fix follows the same logic as standard dictionary compression: build a table of the N unique scale values that actually appear in a tensor, then store a small index (e.g., a few bits) per block pointing into that table instead of the full scale value (typically an FP16 or similar). For a ~15GB Qwen3.6-27B Q4_0 file, this could save a minimum of ~318MB just from the FFN sub-layers examined — with more potential savings in other sub-layers not covered by the napkin math.

The practical barrier is that this changes the on-disk tensor layout in a way incompatible with existing GGUF readers, so it would require either a new quantization type (like the GGML team adding Q4_K variants over time) or a post-processing/recompression step paired with a patched inference engine. Worth tracking if llama.cpp or similar projects pick up "scale table" style quantization formats in the future — it's the kind of small structural win that can compound across many models.

## Related Entries
- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models Comparison](../models/llm-wiki-chinese-models-comparison.md))

---
<!-- RU -->

## Краткое описание
Пользователь LocalLLaMA обнаружил, что GGUF-файлы весов, квантованных в Q4_0, содержат много повторяющихся значений «scale» на блок, и что хранение индекса в небольшой таблице уникальных scale-значений (вместо повторения самого значения) могло бы уменьшить файл Qwen3.6-27B Q4_0 примерно на 318MB (~2% от ~15GB) — хотя для этого требуется собственный код инференса.

## Ключевые идеи
- Квантование Q4_0 хранит коэффициент масштабирования (scale) для каждого блока весов рядом с 4-битными квантованными значениями; автор обнаружил, что многие из этих scale-значений повторяются между блоками как в Qwen3.5-2B, так и в Qwen3.6-27B.
- Вместо хранения полного значения scale для каждого блока можно хранить небольшой словарь уникальных scale-значений плюс индекс в этот словарь для каждого блока — классическая идея словарного сжатия / delta-кодирования, применённая к метаданным квантования.
- Прикидочная оценка для Qwen3.6-27B (Q4_0, ~15GB, 64 слоя): каждый суб-слой (ffn_down/ffn_gate/ffn_up, по ~89.1M весов) занимает ~47.8MB, и в целом по модели такая дедупликация scale могла бы вернуть как минимум ~318MB.
- Автор прямо отмечает, что это небольшой, «интересный, но не огромный» выигрыш (~2%), и что эффект не обязательно универсален для всех моделей — проверено эмпирически только на двух чекпойнтах Qwen.
- Подвох: для использования этой идеи требуется **собственный код инференса** — стандартные читатели llama.cpp / GGUF ожидают, что scale хранится «inline», а не как индекс в словаре, так что это не просто флаг квантования «из коробки».

## Подробнее
Это исследовательская, хоббийная работа (Reddit, confidence: low), а не готовая фича, но она даёт полезную точку данных для тех, кто интересуется дальнейшим сжатием форматов квантования GGUF. Автор изначально изучал, можно ли использовать повторяющиеся значения *весов* (не scale) для сжатия, и наткнулся на то, что коэффициенты масштабирования на блок — которые Q4_0 хранит рядом с квантованными весами для деквантования — сами очень повторяющиеся.

Предложенное решение следует той же логике, что и стандартное словарное сжатие: построить таблицу из N уникальных scale-значений, реально встречающихся в тензоре, а затем хранить небольшой индекс (например, несколько бит) на блок, указывающий в эту таблицу, вместо полного значения scale (обычно FP16 или аналог). Для файла Qwen3.6-27B Q4_0 размером ~15GB это могло бы сэкономить минимум ~318MB только на изученных FFN-суб-слоях — с потенциалом дополнительной экономии в других суб-слоях, не учтённых в прикидке.

Практическое препятствие — это изменяет формат хранения тензора на диске несовместимым образом с существующими читателями GGUF, поэтому потребуется либо новый тип квантования (как команда GGML со временем добавляла варианты Q4_K), либо шаг постобработки/перекомпрессии в паре с патченым inference-движком. Стоит следить, не подхватят ли llama.cpp или похожие проекты формат квантования в стиле «таблицы scale» в будущем — это тот тип небольшого структурного выигрыша, который может накапливаться по множеству моделей.

## Связанные записи
- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models Comparison](../models/llm-wiki-chinese-models-comparison.md))
