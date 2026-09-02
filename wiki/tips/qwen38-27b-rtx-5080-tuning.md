---
title: "Qwen3.8-27B Q4_K_M on RTX 5080 16GB — Selective FFN Offload Tuning"
title_ru: "Qwen3.8-27B Q4_K_M на RTX 5080 16GB — тюнинг с выборочным выносом FFN"
category: tips
tags: [qwen, local-llm, rtx-5080, llama-cpp, ffn-offload, kv-cache, unsloth, pi-agent]
aliases: [qwen3.8 rtx 5080, ffn placement tuning, 27b 16gb vram]
confidence: medium
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/LocalLLaMA/comments/1w5c04h/first_localllm_tuning_attempt_qwen3827b_true_q4_k/
  - https://github.com/johnconnor2020/qwen38-27b-rtx5080-16gb
---

## Summary
A first serious local-LLM tuning writeup: **Qwen3.8-27B UD-Q4_K_M (Unsloth) at a stable ~13.2 tok/s with ~50–61K input context on an RTX 5080 16GB**, using llama.cpp b10760 (CUDA 13.3), 65,536 context, Q4_0 KV cache, Flash Attention, and **Pi as the coding agent**. The decisive technique: selective FFN placement — keep attention/KV and most tensors on GPU, offload the 16 largest FFN tensor groups (~2.76 GiB) to CPU.

## Key Ideas
- **The result:** 13.247/13.260/13.261 tok/s at 49,738 input tokens across three runs; 13.055 tok/s at 61,238 tokens — flat, no cliff, 4/4 retrieval in every run.
- **The technique — selective FFN offload:** FFN weights are the bulk of a model's bytes but are used once per token per layer; attention/KV must be on-GPU for speed, FFN can live in CPU RAM at modest cost. Offloading just the 16 largest groups freed enough VRAM for 65K context.
- **Why Q4_K_M over IQ3:** IQ3 quants were fast but coding quality disappointed; UD-Q4_K_M (16.46 GB) kept quality while the offload recovered the speed.
- **End-to-end validation:** the agent read a broken implementation + separate test, edited only the implementation, ran PowerShell, and got PASS — a real coding-agent loop, not just a perplexity number.
- Full config published in the linked repo.

## Details
Complements [[unsloth-qwen38-27b-gguf]] (the release) with the practical "how to actually run it on 16GB" tuning recipe. The selective-FFN trick is the transferable part: on any 16GB card, attention+KV on GPU with the largest FFN groups in system RAM is the standard play for long-context coding agents — and pairing with a capable harness (Pi) makes it a real daily-driver setup.

## Related Entries
- [[unsloth-qwen38-27b-gguf]] ([Unsloth Qwen3.8-27B GGUF](unsloth-qwen38-27b-gguf.md))
- [[ollama]] ([Ollama](../tools/ollama.md))
- [[clifford-control-plane-local-ai]] ([Clifford](../tools/clifford-control-plane-local-ai.md))
- [[dual-dgx-spark-deepseek-v4-flash]] ([Dual DGX Spark DeepSeek V4 Flash](dual-dgx-spark-deepseek-v4-flash.md))

---
<!-- RU -->

## Краткое описание
Первый серьёзный тюнинг локальной LLM: **Qwen3.8-27B UD-Q4_K_M (Unsloth) на стабильных ~13.2 tok/s с ~50–61K входного контекста на RTX 5080 16GB** — llama.cpp b10760 (CUDA 13.3), контекст 65,536, KV-кэш Q4_0, Flash Attention и **Pi как кодинг-агент**. Решающая техника: выборочное размещение FFN — attention/KV и большинство тензоров на GPU, 16 крупнейших групп тензоров FFN (~2.76 ГиБ) вынесены на CPU.

## Ключевые идеи
- **Результат:** 13.25 tok/s при 49.7K входных токенах (три прогона), 13.06 tok/s при 61.2K — ровно, без обрыва, извлечение 4/4 в каждом прогоне.
- **Техника — выборочный вынос FFN:** веса FFN — основная масса байт модели, но используются один раз на токен на слой; attention/KV должны быть на GPU ради скорости, FFN может жить в RAM по разумной цене.
- **Почему Q4_K_M, а не IQ3:** IQ3 был быстрым, но качество кодинга разочаровало; UD-Q4_K_M (16.46 ГБ) сохранил качество, а вынос вернул скорость.
- **Сквозная валидация:** агент прочитал сломанную реализацию + отдельный тест, отредактировал только реализацию, запустил PowerShell и получил PASS — реальный агентный цикл, а не число перплексии.
- Полный конфиг опубликован в репо.

## Подробнее
Дополняет запись о релизе практическим рецептом «как реально запустить на 16GB». Трюк с выборочным FFN переносим: на любой 16GB-карте attention+KV на GPU с крупнейшими группами FFN в системной памяти — стандартный ход для длинноконтекстных кодинг-агентов.

## Связанные записи
- [[unsloth-qwen38-27b-gguf]] ([Unsloth Qwen3.8-27B GGUF](unsloth-qwen38-27b-gguf.md))
- [[ollama]] ([Ollama](../tools/ollama.md))
- [[clifford-control-plane-local-ai]] ([Clifford](../tools/clifford-control-plane-local-ai.md))
- [[dual-dgx-spark-deepseek-v4-flash]] ([Dual DGX Spark DeepSeek V4 Flash](dual-dgx-spark-deepseek-v4-flash.md))
