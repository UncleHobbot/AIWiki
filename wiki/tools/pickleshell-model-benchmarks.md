---
title: "PickleShell Model Benchmarks — Evidence-First Coding-Agent Evaluation"
title_ru: "PickleShell Model Benchmarks — оценка кодинг-агентов с доказательствами прежде рейтингов"
category: tools
tags: [benchmark, coding-agent, clean-room, blind-review, opencode, methodology]
aliases: [pickleshell benchmarks, models-benchmark, evidence first benchmark]
confidence: medium
updated: 2026-09-01
sources:
  - https://pickleshell.github.io/model-benchmarks.html
  - https://github.com/pickleshell/models-benchmark
---

## Summary
An open-source (MIT) coding-model/agent-runtime benchmark built on OpenCode and Codex, with the motto **"Evidence first, rankings second"**: clean-room runs (fresh workspace, one immutable attempt, no retries), systemd sandbox isolation, identity-blind judging, and manual publication of all evidence — including failures. Rare in a benchmark landscape dominated by vendor-runboards.

## Key Ideas
- **Clean-room methodology:** one attempt per route in a fresh workspace — no retries, no history contamination (a 31-candidate historical archive was excluded from rankings for exactly that reason).
- **Published suite:** bug fixing (76 routes), feature implementation (62 routes / 84 outcomes), refactoring (41 routes / 83 outcomes), repository navigation (80 routes), tests/edge cases (15 routes); plus a Retry-After patch run (44 routes, ~93% completed).
- **Blind 4-criteria judging:** correctness, reliability/edge cases, maintainability, scope discipline — each 0–10, overall = mean; GPT-5.6 Sol as canonical reviewer, Gemini cross-check "broadly agreed."
- **Judge hygiene:** Claude Opus 4.8 was *removed* as a judge after repeatedly missing seeded hidden defects — an unusual act of benchmark self-correction.
- **Honest cost accounting:** unknown costs stay null; the author spent ~$40 of his own API money.

## Details
The transferable value is the methodology, not the current rankings (public per-model score tables are thin — results live in run-record pages and a companion repo). One clean attempt, blind judging, published failures, and a judge that can be fired for missing seeded defects is a template for credible coding-agent evaluation — a nice contrast with [[reap-coding-agent-benchmark-curation]] (auto-curating from production) and the static-benchmark overfit problem.

## Related Entries
- [[reap-coding-agent-benchmark-curation]] ([REAP — Coding-Agent Benchmarks from Production](../research/reap-coding-agent-benchmark-curation.md))
- [[artificial-analysis-coding-agent-index]] ([Artificial Analysis Coding Agent Index](../news/artificial-analysis-coding-agent-index.md))
- [[llm2014-llm-benchmark]] ([llm2014 LLM Benchmark](../research/llm2014-llm-benchmark.md))

---
<!-- RU -->

## Краткое описание
Открытый (MIT) бенчмарк кодинг-моделей/агентных рантаймов на базе OpenCode и Codex с девизом **«Доказательства прежде рейтингов»**: clean-room прогоны (чистый воркспейс, одна неизменяемая попытка, без ретраев), изоляция через systemd sandbox, слепое судейство и ручная публикация всех доказательств — включая провалы.

## Ключевые идеи
- **Clean-room методология:** одна попытка на маршрут в чистом воркспейсе — без ретраев и контаминации историей (исторический архив на 31 кандидата исключён из рейтингов именно поэтому).
- **Опубликованный набор:** багфикс (76 маршрутов), фичи (62/84), рефакторинг (41/83), навигация по репо (80), тесты/edge cases (15); плюс прогон Retry-After патчей (44, ~93%).
- **Слепое судейство по 4 критериям:** корректность, надёжность, поддерживаемость, дисциплина объёма — 0–10, итог = среднее; GPT-5.6 Sol как канонический судья, Gemini перепроверяет.
- **Гигиена судей:** Claude Opus 4.8 *снят* с судейства за пропуски заранее заложенных дефектов.
- **Честный учёт стоимости:** неизвестные цены остаются null; автор потрал ~$40 своих API-денег.

## Подробнее
Переносимая ценность — методология, а не текущие рейтинги. Одна чистая попытка, слепое судейство, опубликованные провалы и увольняемый судья — шаблон достоверной оценки кодинг-агентов, хороший контраст с [[reap-coding-agent-benchmark-curation]] и проблемой переобучения статичных бенчмарков.

## Связанные записи
- [[reap-coding-agent-benchmark-curation]] ([REAP — Coding-Agent Benchmarks from Production](../research/reap-coding-agent-benchmark-curation.md))
- [[artificial-analysis-coding-agent-index]] ([Artificial Analysis Coding Agent Index](../news/artificial-analysis-coding-agent-index.md))
- [[llm2014-llm-benchmark]] ([llm2014 LLM Benchmark](../research/llm2014-llm-benchmark.md))
