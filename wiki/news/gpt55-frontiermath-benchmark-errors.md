---
title: "GPT-5.5 Flags Fatal Errors in ~1/3 of FrontierMath Benchmark Problems"
title_ru: "GPT-5.5 обнаруживает критические ошибки примерно в 1/3 задач бенчмарка FrontierMath"
category: news
tags: [benchmarks, gpt-5-5, frontiermath, epoch-ai, evaluation, benchmark-integrity, math-reasoning]
aliases: [FrontierMath errors, GPT-5.5 FrontierMath, benchmark self-audit]
confidence: medium
date: 2026-05-20
updated: 2026-05-20
sources:
  - https://www.reddit.com/r/singularity/comments/1tb6kum/
---

## Summary

GPT-5.5 was used to audit Epoch AI's FrontierMath benchmark and flagged fatal errors in approximately one third of Tier 1–4 problems — revealing that the model is now capable enough to sanity-check the very benchmarks designed to test it.

## Key Ideas

- **~1/3 of Tiers 1–4 have fatal errors.** An AI-assisted review using GPT-5.5 found that roughly one third of FrontierMath's lower difficulty tiers contain errors severe enough to invalidate the problems.
- **Initial flags came from GPT-5.5.** Noam Brown (OpenAI) confirmed the errors were originally surfaced by GPT-5.5, which was used as an automated auditor of the problem set.
- **Benchmark self-audit is a capability threshold.** The model being strong enough to reliably identify errors in its own evaluation suite is a qualitative milestone — it means the benchmark's difficulty ceiling may be lower than assumed.
- **Corrected scores pending.** Epoch AI acknowledged the issue and will need to correct FrontierMath scores across all models once the valid problem set is finalised. All existing leaderboard comparisons are affected.
- **FrontierMath remains hard overall.** The upper tiers (5+) use research-grade problems unlikely to be affected; the issue is concentrated in Tiers 1–4 which test competition/olympiad-level mathematics.

## Details

FrontierMath, released by Epoch AI in late 2024, was positioned as a benchmark that would remain challenging even for GPT-4-class models — with published solve rates near 2% for the best models at launch. The benchmark was constructed by professional mathematicians to be resistant to data contamination.

The discovery that GPT-5.5 can flag errors in the problem set has two implications:

1. **Benchmark inflation:** Some of the difficulty that was attributed to mathematical hardness was actually due to problem errors — meaning the model's low solve rates on those problems told us less than assumed.
2. **Capability signal:** A model that can detect a fatal flaw in a mathematics problem (e.g., a problem with no valid solution, or with an undetermined answer) has reached a level of mathematical understanding that exceeds what those problems were designed to test.

The community reaction on r/singularity (424 pts, 43 comments) noted this as "a pretty interesting moment: the model is already strong enough to sanity-check the benchmark." Critics pointed out that FrontierMath's research-level upper tiers likely remain valid, and that the corrected benchmark may still be significantly harder than GPT-5.5's demonstrated solve rate.

This echoes a broader pattern in frontier AI evaluation: as models improve, they expose weaknesses in the evaluation infrastructure itself, creating a continuous arms race between benchmark construction and model capability.

## Related Entries

- [[programbench-gpt55-first-solve]] ([ProgramBench: GPT-5.5 First Solve](../news/programbench-gpt55-first-solve.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs](../concepts/karpathy-deep-dive-llms.md))

---
<!-- RU -->

## Краткое описание

GPT-5.5 использовался для аудита бенчмарка FrontierMath от Epoch AI и обнаружил критические ошибки примерно в одной трети задач уровней 1–4 — показывая, что модель теперь достаточно сильна, чтобы проверять сами бенчмарки, разработанные для её тестирования.

## Ключевые идеи

- **~1/3 уровней 1–4 содержат критические ошибки.** Проверка с помощью GPT-5.5 обнаружила, что примерно треть задач нижних уровней FrontierMath содержит ошибки, делающие задачи недействительными.
- **Первичные флаги поставил GPT-5.5.** Ноам Браун (OpenAI) подтвердил, что ошибки были изначально обнаружены GPT-5.5, использованным как автоматизированный аудитор задач.
- **Самоаудит бенчмарка — порог возможностей.** Модель, способная надёжно выявлять ошибки в собственном наборе оценок — это качественная веха: потолок сложности бенчмарка может быть ниже, чем предполагалось.
- **Скорректированные результаты ожидаются.** Epoch AI признала проблему; все существующие сравнения в таблице лидеров затронуты.
- **Верхние уровни FrontierMath остаются надёжными.** Задачи исследовательского уровня (уровни 5+) с высокой вероятностью не затронуты; проблема сосредоточена в уровнях 1–4.

## Подробнее

FrontierMath, выпущенный Epoch AI в конце 2024 года, позиционировался как бенчмарк, остающийся сложным даже для моделей класса GPT-4. Открытие, что GPT-5.5 может находить ошибки в наборе задач, имеет два следствия: (1) часть сложности объяснялась ошибками задач, а не их математической глубиной; (2) модель, способная обнаружить критический изъян в математической задаче, достигла уровня понимания, превышающего то, что эти задачи были призваны измерять. Это отражает более широкую закономерность: по мере улучшения моделей они выявляют слабые места в инфраструктуре оценки.

## Связанные записи

- [[programbench-gpt55-first-solve]] ([ProgramBench: GPT-5.5 First Solve](../news/programbench-gpt55-first-solve.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs](../concepts/karpathy-deep-dive-llms.md))
