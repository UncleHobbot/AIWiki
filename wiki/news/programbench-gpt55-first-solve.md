---
title: "ProgramBench: GPT-5.5 Achieves First Solve on Difficult SWE Benchmark"
title_ru: "ProgramBench: GPT-5.5 впервые решает сложный SWE-бенчмарк"
category: news
tags: [benchmarks, gpt-5-5, swe-bench, programbench, openai, coding-agents, evaluation]
aliases: [ProgramBench, program bench, SWE benchmark 2026]
confidence: medium
date: 2026-05-19
updated: 2026-05-19
sources:
  - https://programbench.com/blog/gpt-5-5-first-solve/
  - https://github.com/facebookresearch/ProgramBench/
  - https://www.reddit.com/r/singularity/comments/1tb6kum/
---

## Summary

ProgramBench — a new, harder software-engineering benchmark from Facebook Research — saw its first-ever task solve by GPT-5.5 (high/xhigh tier), which also significantly outperforms Anthropic's Claude Opus 4.7 on the leaderboard.

## Key Ideas

- **Harder than SWE-bench:** ProgramBench targets tasks that require multi-file reasoning, long-horizon planning, and program synthesis — areas where prior SWE-bench saturates.
- **First solve by GPT-5.5:** GPT-5.5 at the high/xhigh compute tier solved a task for the first time, marking a milestone for the benchmark.
- **Opus 4.7 significantly outperformed:** GPT-5.5 opens a visible gap over Claude Opus 4.7 on this benchmark, according to community-shared leaderboard screenshots.
- **Facebook Research provenance:** Released by facebookresearch on GitHub, indicating academic rigour in benchmark construction.
- **Community reaction:** r/singularity discussion (524 pts, 94 comments) framed this as evidence GPT-5.5 is a meaningful leap from GPT-4o-class models for hard coding tasks.

## Details

ProgramBench addresses a known weakness of SWE-bench Verified: top models now score above 50% on that benchmark, making it insufficient to distinguish frontier model capability. ProgramBench raises the ceiling with tasks that require:

- Understanding program structure across multiple interconnected files
- Writing correct code on the first pass without iterative debugging loops
- Handling ambiguous specifications that require inference from context

The first public solve by GPT-5.5 at the high compute tier signals that the benchmark remains challenging enough to differentiate current frontier models. The gap over Opus 4.7 — which was itself a significant step up from Claude 3.5 Sonnet — suggests the coding capability ceiling is still moving fast.

No official paper has been published as of this writing; the benchmark is available on GitHub and results are tracked on the programbench.com leaderboard.

## Related Entries

- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
- [[gpt55-frontiermath-benchmark-errors]] ([GPT-5.5 FrontierMath Benchmark Errors](../news/gpt55-frontiermath-benchmark-errors.md))

---
<!-- RU -->

## Краткое описание

ProgramBench — новый сложный SWE-бенчмарк от Facebook Research — зафиксировал первое в истории успешное решение задачи моделью GPT-5.5 (уровень high/xhigh), которая также значительно опережает Claude Opus 4.7 Anthropic в таблице лидеров.

## Ключевые идеи

- **Сложнее SWE-bench:** ProgramBench нацелен на задачи, требующие рассуждений по нескольким файлам, долгосрочного планирования и синтеза программ — области, где SWE-bench уже насыщен.
- **Первое решение GPT-5.5:** GPT-5.5 на уровне high/xhigh впервые решил задачу, обозначив веху для бенчмарка.
- **Opus 4.7 значительно отстаёт:** GPT-5.5 открывает заметный разрыв над Claude Opus 4.7, согласно скриншотам таблицы лидеров из сообщества.
- **Происхождение из Facebook Research:** Опубликован facebookresearch на GitHub, что указывает на академическую строгость в построении бенчмарка.
- **Реакция сообщества:** Обсуждение на r/singularity (524 балла, 94 комментария) расценило это как свидетельство того, что GPT-5.5 является значимым скачком от моделей класса GPT-4o для сложных задач кодирования.

## Подробнее

ProgramBench устраняет известную слабость SWE-bench Verified: ведущие модели уже набирают выше 50% на этом бенчмарке, что делает его недостаточным для различения возможностей моделей. ProgramBench повышает планку задачами, которые требуют понимания структуры программы в нескольких взаимосвязанных файлах, написания правильного кода с первого раза и работы с неоднозначными спецификациями.

Первое публичное решение GPT-5.5 при высоком compute-уровне сигнализирует, что бенчмарк остаётся достаточно сложным для дифференциации текущих моделей. Разрыв над Opus 4.7 — который сам по себе был значительным шагом вперёд — говорит о том, что потолок возможностей кодирования продолжает расти.

## Связанные записи

- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
- [[gpt55-frontiermath-benchmark-errors]] ([GPT-5.5 FrontierMath Benchmark Errors](../news/gpt55-frontiermath-benchmark-errors.md))
