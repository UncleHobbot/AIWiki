---
title: "ToolHound — Tool-Calling Failure Taxonomy (Beyond a Single Accuracy Number)"
title_ru: "ToolHound — таксономия ошибок вызова инструментов (сверх одного числа точности)"
category: research
tags: [tool-calling, benchmark, failure-taxonomy, small-models, mlx, qwen, granite, gemma]
aliases: [ToolHound, tool call failure taxonomy, Code-byte404 toolhound]
confidence: medium
updated: 2026-07-11
sources:
  - https://github.com/Code-byte404/toolhound
  - https://www.reddit.com/r/Qwen_AI/comments/1uosrgh/currentgen_small_models_have_basically_solved/
---

## Summary
**ToolHound** is an MLX harness that stops reporting tool-calling as a single "accuracy" number and instead pins every failure on one of four root causes. Its latest finding: current-gen small models (2–12B) have essentially solved tool-call *syntax* — parse/schema/tool metrics are ~1.00 — so the only thing left to get wrong is argument-value selection.

## Key Ideas
- **Four-way failure taxonomy** — every failure is classified into exactly one of:
  1. `framework_template_bug` — the harness's own template is wrong.
  2. `framework_parser_gap` — the harness can't parse a valid call.
  3. `model_format_failure` — the model can't emit a parseable call.
  4. `model_decision_failure` — valid format, but wrong tool or wrong arguments.
- **Why this matters:** a single "71% correct" hides *which layer* broke, and different models need *opposite* fixes. A format failure needs prompt/format changes; a decision failure needs a better model.
- **Latest lineup (three families, three native tool-call formats):**
  - **Qwen3.5-2B** — XML format (`<function=NAME>...`).
  - **Granite-3.3-2B** — JSON list format (`<|tool_call|>[{...}]`).
  - **Gemma-4-12B** — (third distinct native format).
- **Headline result:** small models have basically solved tool-call *syntax*. Parse/schema/tool metrics are ~1.00 across all three; the residual errors are `model_decision_failure` — the model picked the wrong argument values.

## Details
ToolHound is a diagnostic instrument, not a leaderboard. By forcing every failure into one of four buckets — and separating harness bugs from model bugs — it reveals that the "tool-calling is unreliable" narrative for small models is stale: the syntax layer is solved. What remains is a *decision-quality* problem (which values to put in the arguments), which is a model-intelligence issue, not a format-compliance issue. That distinction changes what you fix and how.

## Related Entries
- [[browser-snapshot-format-token-cost]] ([Browser Snapshot Format vs Token Cost](browser-snapshot-format-token-cost.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[reap-coding-agent-benchmark-curation]] ([REAP — Coding-Agent Benchmarks from Production](reap-coding-agent-benchmark-curation.md))

---
<!-- RU -->

## Краткое описание
**ToolHound** — MLX-харнес, который перестаёт сообщать о вызове инструментов одним числом «точность» и вместо этого относит каждый сбой к одной из четырёх причин. Новейшая находка: современные маленькие модели (2–12B) фактически решили *синтаксис* вызова инструментов — метрики parse/schema/tool ~1.00, остаётся лишь ошибка выбора значений аргументов.

## Ключевые идеи
- **Таксономия из четырёх причин:** каждый сбой классифицируется ровно в одну:
  1. `framework_template_bug` — баг шаблона харнеса.
  2. `framework_parser_gap` — харнес не парсит валидный вызов.
  3. `model_format_failure` — модель не выдаёт парсимый вызов.
  4. `model_decision_failure` — формат валиден, но выбран не тот инструмент/аргументы.
- **Почему важно:** одно число «71%» скрывает, *какой слой* сломался; разным моделям нужны *противоположные* фиксы.
- **Свежий состав (три семейства, три нативных формата):** Qwen3.5-2B (XML), Granite-3.3-2B (JSON list), Gemma-4-12B.
- **Главный результат:** маленькие модели решили *синтаксис* вызова; остаточные ошибки — `model_decision_failure`.

## Подробнее
ToolHound — диагностический инструмент, не лидерборд. Разделяя баги харнеса и баги модели, он показывает, что нарратив «вызов инструментов у маленьких моделей ненадёжен» устарел: синтаксис решён. Осталось — проблема качества *решений* (какие значения подставить), что является вопросом интеллекта модели, а не соответствия формату.

## Связанные записи
- [[browser-snapshot-format-token-cost]] ([Browser Snapshot Format vs Token Cost](browser-snapshot-format-token-cost.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[reap-coding-agent-benchmark-curation]] ([REAP — Coding-Agent Benchmarks from Production](reap-coding-agent-benchmark-curation.md))
