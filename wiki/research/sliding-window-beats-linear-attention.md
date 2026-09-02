---
title: "Sliding-Window Attention Beats Post-Trained Linear Attention (arXiv 2608.28444)"
title_ru: "Скользящее окно внимания превосходит пост-тренировочную линейную attention (arXiv 2608.28444)"
category: research
tags: [attention, sliding-window, linear-attention, long-context, architecture, sinks]
aliases: [SWA vs linear attention, sliding window attention sinks]
confidence: high
updated: 2026-09-01
sources:
  - https://arxiv.org/abs/2608.28444
---

## Summary
A paper by Jolicoeur-Martineau et al. (Aug 28, 2026) argues that sliding-window attention (SWA) with attention sinks is a better long-context foundation than post-trained linear attention: SWA matches or beats post-trained Linear Attention models on the tasks studied, achieves **2–10× higher performance** on long-context reasoning benchmarks (Needle-in-a-Haystack, BABILong), and needs **no post-training** to get there — while staying fast and memory-efficient.

## Key Ideas
- **The claim:** the industry trend toward hybrid linear-attention architectures may be a detour — the simpler, hardware-friendly SWA was the right long-context primitive all along.
- **2–10× on long-context reasoning** (NIAH, BABILong) vs post-trained linear models.
- **No post-training required:** hybrid/linear models need an extra post-training phase to become competitive; SWA doesn't.
- **Speed concern addressed:** SWA's window keeps compute bounded, mitigating the quadratic-cost objection to full attention.
- **Explicit recommendation:** the authors call on researchers to switch to SWA instead of post-training linear models.

## Details
If it holds up, this matters for anyone choosing or training long-context open models: the "linear attention for infinite context" narrative has been driving architecture choices (and marketing) for two years. The paper's case is that a small sink-anchored window recovers most long-context utility at a fraction of the complexity. Caveats: results are the authors' own benchmarks; hybrid architectures still dominate some production efficiency profiles. Track whether follow-up work replicates the 2–10× gap.

## Related Entries
- [[llm-wiki-chinese-models-comparison]] ([Chinese Models Comparison](../models/llm-wiki-chinese-models-comparison.md))
- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- [[orthrus-qwen3-acceleration]] ([Orthrus-Qwen3 Acceleration](../tools/orthrus-qwen3-acceleration.md))

---
<!-- RU -->

## Краткое описание
Статья Jolicoeur-Martineau и др. (28 авг 2026) утверждает, что sliding-window attention (SWA) с attention-синками — лучшая основа для длинного контекста, чем пост-тренировочная линейная attention: SWA не уступает и превосходит линейные модели, показывая **в 2–10 раз выше** результаты на бенчмарках длинного контекста (NIAH, BABILong) — и **не требует пост-тренировки**, оставаясь быстрой и экономной по памяти.

## Ключевые идеи
- **Тезис:** отраслевой тренд на гибридные linear-attention архитектуры может оказаться обходным путём — простой и дружественный к железу SWA был верной основой длинного контекста с самого начала.
- **2–10× на long-context reasoning** (NIAH, BABILong) против пост-тренированных линейных моделей.
- **Без пост-тренировки:** гибридным/линейным моделям нужна доп. фаза пост-тренировки; SWA — нет.
- **Скорость:** окно SWA ограничивает вычисления, снимая возражение квадратичной стоимости.
- **Явная рекомендация:** авторы призывают исследователей переключиться на SWA.

## Подробнее
Если подтвердится, это важно для всех, кто выбирает или обучает модели с длинным контекстом: нарратив «linear attention для бесконечного контекста» два года двигал архитектурные решения. По мнению авторов, небольшое окно с якорем-sink даёт большую часть утилиты длинного контекста за долю сложности. Оговорки: бенчмарки авторские; гибриды всё ещё доминируют в некоторых production-профилях эффективности.

## Связанные записи
- [[llm-wiki-chinese-models-comparison]] ([Chinese Models Comparison](../models/llm-wiki-chinese-models-comparison.md))
- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- [[orthrus-qwen3-acceleration]] ([Orthrus-Qwen3 Acceleration](../tools/orthrus-qwen3-acceleration.md))
