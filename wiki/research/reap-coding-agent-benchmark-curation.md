---
title: "REAP — Automatic Curation of Coding-Agent Benchmarks from Production Usage"
title_ru: "REAP — автоматическое формирование бенчмарков кодинг-агентов из продакшн-использования"
category: research
tags: [benchmark, coding-agent, evaluation, agent-bench, REAP]
aliases: [REAP, REAP benchmark]
confidence: low
updated: 2026-07-01
sources:
  - https://www.reddit.com/r/MachineLearning/comments/1uk713d/reap_automatic_curation_of_coding_agent/
---

## Summary
REAP is a research project ([R]-tagged) proposing automatic curation of coding-agent benchmarks derived from interactive production usage — i.e., turning real agent sessions into benchmark tasks rather than hand-authored eval scenarios.

## Key Ideas
- **Motivation:** hand-built coding-agent benchmarks (SWE-bench-style) are expensive, static, and drift away from real usage; REAP generates them from production traces instead.
- **Source:** r/MachineLearning [R] post — title only, no abstract in the selftext (Tier 3, low confidence until the paper is read).
- Signals a broader trend: benchmarks that self-refresh from real agent interactions to stay representative as agentic workflows evolve.
- Pairs with the live debate that SWE-bench-style static benchmarks overfit to known repos and saturate quickly.

## Details
The [R] designation on r/MachineLearning denotes research. The post itself contains only a link and no extended abstract, so details are limited to the title's framing: automatically curating coding-agent evaluation tasks from interactive production usage. Worth tracking for the full paper; recorded here as a low-confidence stub pending the primary source.

## Related Entries
- [[open-source-models-vs-opus-copilot-benchmark]] ([Open Source vs Opus/Copilot Benchmark](../models/open-source-models-vs-opus-copilot-benchmark.md))
- [[artificial-analysis-coding-agent-index]] ([Artificial Analysis Coding Agent Index](../news/artificial-analysis-coding-agent-index.md))
- [[programbench-gpt55-first-solve]] ([ProgramBench GPT-5.5 First Solve](../news/programbench-gpt55-first-solve.md))

---
<!-- RU -->

## Краткое описание
REAP — исследовательский проект (тег [R]), предлагающий автоматическое формирование бенчмарков кодинг-агентов из интерактивного продакшн-использования: превращение реальных сессий агента в задачи вместо ручного написания eval-сценариев.

## Ключевые идеи
- **Мотивация:** рукотворные бенчмарки (в стиле SWE-bench) дороги, статичны и отрываются от реального использования; REAP генерирует их из production-трейсов.
- **Источник:** пост [R] в r/MachineLearning — только заголовок, расширенного абстракта в selftext нет (уровень 3, низкая достоверность до прочтения статьи).
- Указывает на тренд: бенчмарки, самообновляющиеся из реальных взаимодействий агентов.
- Сочетается с дискуссией о том, что статичные бенчмарки переобучаются на известные репозитории и быстро насыщаются.

## Подробнее
Тег [R] обозначает research. Сам пост содержит лишь ссылку без расширенного абстракта, поэтому детали ограничены формулировкой заголовка: автоматическая кураторская оценка задач для кодинг-агентов из интерактивного продакшна. Записано как заглушка с низкой достоверностью до появления первоисточника.

## Связанные записи
- [[open-source-models-vs-opus-copilot-benchmark]] ([Open Source vs Opus/Copilot Benchmark](../models/open-source-models-vs-opus-copilot-benchmark.md))
- [[artificial-analysis-coding-agent-index]] ([Artificial Analysis Coding Agent Index](../news/artificial-analysis-coding-agent-index.md))
- [[programbench-gpt55-first-solve]] ([ProgramBench GPT-5.5 First Solve](../news/programbench-gpt55-first-solve.md))
