---
title: "Agent Lifespan Engineering: AgingBench and the Four Aging Mechanisms"
title_ru: "Инженерия жизненного цикла агентов: AgingBench и четыре механизма деградации"
category: concepts
tags: [agents, deployment, memory, benchmark, reliability, aging, harness-engineering, lifespan]
aliases: [AgingBench, agent aging, agent lifespan, compression aging, interference aging]
confidence: high
date: 2026-05-25
updated: 2026-06-05
sources:
  - https://arxiv.org/abs/2605.26302
  - https://www.reddit.com/r/MachineLearning/comments/1tqaoio/your_agents_are_aging_too_agent_lifespan/
---

## Summary
AgingBench (arXiv 2605.26302) introduces longitudinal reliability evaluation for deployed AI agents, finding that agent reliability is a lifespan property of the full harness — not a snapshot property of the base model — and that behavioral tests can remain clean while factual precision silently decays.

## Key Ideas
- **Reliability is a harness property**: even with frozen model weights, an agent's effective state keeps changing as it compresses history, retrieves from a growing memory store, revises facts, and undergoes maintenance. Day-one benchmarks miss this entirely.
- **Four aging mechanisms**: compression aging (context compression degrades recall), interference aging (new memories corrupt older ones), revision aging (fact updates create inconsistency), maintenance aging (routine ops introduce drift).
- **Diagnostic mismatch**: behavioral tests (does the agent complete the task?) can pass while factual precision (does it recall the right details?) decays — so passing CI tests doesn't mean the agent is reliable long-term.
- **Switching models mid-deployment causes regressions**: a community reproducer found that switching Claude Code's model from Sonnet 4.6 to Opus 4.7 *dropped* PyTest pass rates by ~15% — counter-intuitive evidence that the harness + model combination matters as a system.
- **Stage-targeted repair**: AgingBench diagnoses failures at the write, retrieval, and utilization stages of the memory pipeline — allowing repair to target the actual broken stage rather than retraining or replacing the whole model.

## Details

### The Four Aging Mechanisms

| Mechanism | What Causes It | Symptom |
|---|---|---|
| **Compression aging** | Context compaction loses nuance | Retrieved summaries are less precise than originals |
| **Interference aging** | New writes corrupt old memories | Agent recalls wrong version of a past decision |
| **Revision aging** | Fact updates leave stale references | Agent uses outdated fact for a decision |
| **Maintenance aging** | Routine ops (reindexing, cleanup) introduce drift | Agent behavior changes across sessions without apparent reason |

### Temporal Dependency Graphs + Counterfactual Probes
AgingBench uses two novel diagnostic tools:
- **Temporal dependency graphs**: model which facts depend on which prior facts, enabling targeted queries about whether the right version of a fact is being retrieved at each point in time.
- **Paired counterfactual probes**: ask the agent the same question with and without a known memory update, to isolate whether it's retrieving the current or stale version.

### Key Empirical Findings (across 7 scenarios, 14 models, ~400 runs)
- Agent aging is **not one-dimensional**: behavioral tests can remain clean while factual precision decays.
- **Derived-state tracking** (tracking facts that are derived from other facts) collapses sharply within a single model.
- **The same wrong answer requires different repairs** depending on which aging mechanism caused it — a compression error needs compaction tuning; an interference error needs memory isolation.

### Implication for Harness Engineering
AgingBench challenges the dominant assumption that deploying a stronger model solves reliability problems. Long-lived agents need:
1. **Lifespan evaluation** alongside day-one benchmarks
2. **Mechanism-level diagnosis** to identify which aging type is occurring
3. **Stage-targeted repair** (write → retrieval → utilization) rather than whole-model replacement

## Related Entries
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[learn-harness-engineering-course]] ([Learn Harness Engineering Course](../concepts/learn-harness-engineering-course.md))
- [[anthropic-agent-memory-dreaming]] ([Anthropic Agent Memory & Dreaming](../agents/anthropic-agent-memory-dreaming.md))
- [[claude-opus-4-8-release]] ([Claude Opus 4.8](../news/claude-opus-4-8-release.md))

---
<!-- RU -->

## Краткое описание
AgingBench (arXiv 2605.26302) вводит продольную оценку надёжности для развёрнутых AI-агентов, показывая, что надёжность агента — это свойство жизненного цикла всего harness, а не снимок базовой модели, и что поведенческие тесты могут оставаться зелёными, пока фактическая точность незаметно деградирует.

## Ключевые идеи
- **Надёжность — свойство harness**: даже при замороженных весах эффективное состояние агента постоянно меняется по мере сжатия истории, роста хранилища памяти, пересмотра фактов и обслуживания. Бенчмарки «первого дня» это полностью упускают.
- **Четыре механизма деградации**: компрессионное старение, интерференционное старение, ревизионное старение, эксплуатационное старение.
- **Диагностическое несоответствие**: поведенческие тесты (выполняет ли агент задачу?) могут проходить, пока фактическая точность (вспоминает ли правильные детали?) тихо деградирует.
- **Смена модели в середине деплоя вызывает регрессии**: переключение Claude Code с Sonnet 4.6 на Opus 4.7 снизило процент прохождения PyTest на ~15% — контринтуитивное свидетельство того, что harness + модель важны как система.
- **Целевое восстановление по стадиям**: AgingBench диагностирует сбои на стадиях записи, поиска и использования в конвейере памяти.

## Подробнее

**Четыре механизма деградации:**
- **Компрессионное старение**: сжатие контекста теряет нюансы — извлечённые резюме менее точны, чем оригиналы.
- **Интерференционное старение**: новые записи искажают старые воспоминания — агент вспоминает неправильную версию прошлого решения.
- **Ревизионное старение**: обновления фактов оставляют устаревшие ссылки — агент использует старый факт для нового решения.
- **Эксплуатационное старение**: рутинные операции (переиндексация, очистка) вносят дрейф — поведение агента меняется между сессиями без видимой причины.

**Ключевые выводы (~400 запусков, 7 сценариев, 14 моделей):**
- Деградация агента нелинейна: поведенческие тесты чистые, точность фактов деградирует.
- Одинаковый неправильный ответ требует разных исправлений в зависимости от механизма.
- Надёжное долгосрочное развёртывание требует: продольной оценки жизненного цикла, диагностики по механизмам, целевого восстановления по стадиям.

## Связанные записи
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[learn-harness-engineering-course]] ([Learn Harness Engineering Course](../concepts/learn-harness-engineering-course.md))
- [[anthropic-agent-memory-dreaming]] ([Anthropic Agent Memory & Dreaming](../agents/anthropic-agent-memory-dreaming.md))
- [[claude-opus-4-8-release]] ([Claude Opus 4.8](../news/claude-opus-4-8-release.md))
