---
title: "One Epoch of MQL5 Fine-Tuning: Qwen2.5-Coder-14B 1% → 92% Compile Success"
title_ru: "Одна эпоха fine-tuning на MQL5: Qwen2.5-Coder-14B с 1% до 92% успешной компиляции"
category: research
tags: [fine-tuning, domain-adaptation, qwen, mql5, compiler-verification, rocm, amd]
aliases: [MQL5 fine-tune, qwen coder domain tuning, compile benchmark mql5]
confidence: medium
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/Qwen_AI/comments/1w5ggzy/one_epoch_of_domain_finetuning_took/
---

## Summary
A practitioner's 11-month MQL5 (MetaTrader 5 language) dataset project — machine-verified through the real compiler and a backtest pipeline — produced a benchmark with three arms over the same 184 prompts: base Qwen2.5-Coder-14B-Instruct **2/184 (1.09%)**, the same model after **one epoch** of fine-tuning **170/184 (92.39%)**, and gpt-5.6-sol **179/184 (97.28%)**. Headline: clean domain data moved a 14B model from useless to within ~5 points of frontier in a single epoch. All training and local eval ran on an AMD R9700 under ROCm — no NVIDIA.

## Key Ideas
- **The three-arm result:** base 1.09% → fine-tuned 92.39% (+91.3pp, McNemar p = 2.29e-49) vs frontier 97.28% (gap 4.89pp, p = 0.0225).
- **Data quality was the whole game:** 11 months of spec generation plus machine verification (real compiler + backtest) — not quantity of data, but every completion verified by ground truth.
- **Compiler-as-verifier:** MQL5 gives a hard, automated correctness signal — a luxury domain. The method generalizes to any domain with machine-checkable outputs.
- **AMD-only training** on one R9700 (ROCm) is itself a data point on non-NVIDIA fine-tuning feasibility.
- Honest framing: "the point was never beating GPT" — the author published despite losing to the frontier model.

## Details
This is a clean demonstration of the narrow-domain fine-tuning playbook: pick a domain with a machine-verifiable success signal, build a verified dataset over months, one epoch, near-frontier. It complements the [[reap-coding-agent-benchmark-curation]] theme (real evaluation from real usage) — here the eval *is* the compiler.

## Related Entries
- [[unsloth-qwen38-27b-gguf]] ([Unsloth Qwen3.8-27B GGUF](../models/unsloth-qwen38-27b-gguf.md))
- [[gpt-5-6-sol-preview]] ([GPT-5.6 Sol](../news/gpt-5-6-sol-preview.md))
- [[llm2014-llm-benchmark]] ([llm2014 Benchmark](llm2014-llm-benchmark.md))

---
<!-- RU -->

## Краткое описание
11-месячный проект датасета MQL5 (язык MetaTrader 5) с машинной верификацией через реальный компилятор и бэктест-пайплайн дал бенчмарк из трёх групп на одних и тех же 184 промптах: базовый Qwen2.5-Coder-14B-Instruct **2/184 (1.09%)**, та же модель после **одной эпохи** fine-tuning **170/184 (92.39%)**, gpt-5.6-sol **179/184 (97.28%)**. Главный вывод: чистые доменные данные подняли 14B-модель с бесполезной до ~5 пунктов от фронтира за одну эпоху. Обучение и локальный eval — на AMD R9700 под ROCm, без NVIDIA.

## Ключевые идеи
- **Результат трёх групп:** 1.09% → 92.39% (+91.3pp, McNemar p = 2.29e-49) против фронтира 97.28% (разрыв 4.89pp, p = 0.0225).
- **Качество данных — вся игра:** 11 месяцев генерации спецификаций плюс машинная верификация каждой модели — не количество, а заземление в истину.
- **Компилятор как верификатор:** MQL5 даёт жёсткий автоматический сигнал корректности — роскошь домена. Метод обобщается на любые области с машинно-проверяемым выводом.
- **Обучение только на AMD** (R9700, ROCm) — само по себе datapoint о жизнеспособности non-NVIDIA fine-tuning.
- Честная рамка: «целью никогда не было победить GPT».

## Подробнее
Чистая демонстрация плейбука узкодоменного fine-tuning: домен с машинно-проверяемым сигналом успеха, месяцы верифицированного датасета, одна эпоха — почти фронтир. Дополняет тему [[reap-coding-agent-benchmark-curation]] — здесь eval и есть компилятор.

## Связанные записи
- [[unsloth-qwen38-27b-gguf]] ([Unsloth Qwen3.8-27B GGUF](../models/unsloth-qwen38-27b-gguf.md))
- [[gpt-5-6-sol-preview]] ([GPT-5.6 Sol](../news/gpt-5-6-sol-preview.md))
- [[llm2014-llm-benchmark]] ([llm2014 Benchmark](llm2014-llm-benchmark.md))
