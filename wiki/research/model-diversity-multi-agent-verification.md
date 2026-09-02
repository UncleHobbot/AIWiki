---
title: "Does Model Diversity Make Multi-Agent Verification Stronger? (720-Eval Pre-Registered Test)"
title_ru: "Делает ли разнообразие моделей мульти-агентную верификацию сильнее? (720 оценок, пре-регистрация)"
category: research
tags: [multi-agent, verification, model-diversity, pre-registration, corroboration, evals]
aliases: [model diversity verification, corroboration independence, errslima 1f517]
confidence: medium
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1w5e95j/does_model_diversity_actually_make_multiagent/
  - https://github.com/errslima/1f517/blob/main/experiments/corroboration-independence/RESULTS.md
---

## Summary
A pre-registered experiment testing the intuition that multi-agent corroboration requires *different* models (same-model confirmations share blind spots). 60 findings-shaped claims (30 true, 30 planted false-but-plausible), 3 evaluators per arm in fresh sessions, 720 evaluations total — and the author **failed their own kill condition**, i.e. the data did not support the diversity intuition as cleanly as expected. Part of a larger "shared evidence pool" project where agents deposit falsifiable, version-scoped claims about public artifacts for other agents to confirm or refute.

## Key Ideas
- **The design:** pre-registration with a public kill condition *before* running — rare hygiene in agent research. 60 claims × 3 evaluators × arms = 720 evaluations, no tools, fresh sessions.
- **The claim construction:** false claims each invert one verified detail (a version, a default, a direction) — plausible enough to survive casual checking.
- **The result:** the diversity hypothesis did not survive its kill condition — the author published the negative result anyway and invited design critique.
- **The larger project (1f517):** a shared evidence pool where each claim is falsifiable and version-scoped (e.g. "tsc with `strict` omitted behaves as if strict were false" — spoiler: it doesn't).

## Details
Negative results with pre-registered kill conditions are exactly what the agent-evals space needs more of ([[anthropic-cost-optimization-cookbook]] makes the same point about eval-driven decisions). The open question the experiment leaves: *when do N confirmations mean something* — is it diversity, independence of failure modes, claim difficulty, or evaluator calibration? The full RESULTS.md is the primary source worth reading before citing numbers.

## Related Entries
- [[anthropic-cost-optimization-cookbook]] ([Anthropic Cost Optimization Cookbook](../tips/anthropic-cost-optimization-cookbook.md))
- [[pickleshell-model-benchmarks]] ([PickleShell Model Benchmarks](../tools/pickleshell-model-benchmarks.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))

---
<!-- RU -->

## Краткое описание
Пре-регистрированный эксперимент, проверяющий интуицию, что мульти-агентное подтверждение требует *разных* моделей (подтверждения одной моделью делят слепые зоны). 60 утверждений в формате findings (30 истинных, 30 правдоподобно-ложных), 3 оценщика на группу в свежих сессиях, 720 оценок — и автор **провалил собственное kill-условие**: данные не поддержали интуицию разнообразия так чисто, как ожидалось. Часть проекта «общего пула доказательств», где агенты депонируют фальсифицируемые утверждения о публичных артефактах.

## Ключевые идеи
- **Дизайн:** пре-регистрация с публичным kill-условием *до* запуска — редкая гигиена в агентных исследованиях.
- **Конструкция утверждений:** ложные инвертируют одну проверенную деталь (версию, дефолт, направление) — достаточно правдоподобно, чтобы пережить беглую проверку.
- **Результат:** гипотеза разнообразия не пережила kill-условие; негативный результат опубликован с приглашением к критике дизайна.
- **Проект 1f517:** общий пул доказательств с фальсифицируемыми, version-scoped утверждениями.

## Подробнее
Негативные результаты с пре-регистрированными kill-условиями — именно то, чего не хватает пространству агентных оценок. Открытый вопрос эксперимента: *когда N подтверждений что-то значат* — разнообразие, независимость режимов отказа, сложность утверждений или калибровка оценщиков? Полный RESULTS.md — первоисточник, который стоит прочесть до цитирования чисел.

## Связанные записи
- [[anthropic-cost-optimization-cookbook]] ([Anthropic Cost Optimization Cookbook](../tips/anthropic-cost-optimization-cookbook.md))
- [[pickleshell-model-benchmarks]] ([PickleShell Model Benchmarks](../tools/pickleshell-model-benchmarks.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
