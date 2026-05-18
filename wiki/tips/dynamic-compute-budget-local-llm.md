---
title: "Dynamic Compute Budget Allocation for Local LLMs"
title_ru: "Динамическое распределение вычислительного бюджета для локальных LLM"
category: tips
tags: [local-llm, test-time-compute, qwen, hle, benchmark, inference, parallel-agents]
date: 2026-05-16
updated: 2026-05-16
sources:
  - https://github.com/ryoiki-tokuiten/Iterative-Contextual-Refinements
  - https://www.reddit.com/r/LocalLLaMA/comments/1te8sxt/dynamically_allocating_compute_budget_to_hard_set/
---

## Summary
Dynamic Compute Budget Allocation (DCA) is a test-time compute technique that lets a local Qwen-35B-A3B model approach GPT-5.4-xHigh performance on the Humanity's Last Exam (HLE) benchmark by having the model assign priority scores to hard problems and then spawning parallel sub-agents that generate multiple solution attempts per problem.

## Key Ideas
- Ask the LLM to assess a set of problems, assign a priority/difficulty score to each, and output a structured response that can be parallelized.
- Spin up independent parallel agents focused on each sub-approach; the number of solution attempts each agent generates equals the priority assigned to that problem.
- Qwen 3.6-35B-A3B baseline scores 21.4% on HLE (official); GPT-5.4-xHigh scores 41.6% (official). With DCA, Qwen reached 39.9% — within 2 points of the frontier model.
- Single-step denoising consistently beats multi-step (6.35× vs 3.53× token throughput per forward pass in related work).
- This produces a pool of solutions — there is no automatic final-answer selector. You must review the pool manually or add a synthesis step.

## Details
The technique is designed for throwing large compute budgets at problems you'd normally test against frontier models. It is **not** recommended as an always-on agent tool for coding tasks, because the wide divergence of parallel solution attempts makes it hard to integrate into a consistent codebase.

**Workflow:**
1. Give the LLM the target problem set and ask it to assign priorities.
2. Parse the structured output to determine how many solution attempts each problem gets.
3. For each problem and each approach, launch an independent agent that only sees its own sub-problem and other solutions in the pool (not the global context).
4. Collect all solutions; the user reviews or a synthesis model picks the most plausible ones.

**Single iteration is the sweet spot.** Going deeper (recursive refinement across multiple rounds) bloats the context window without proportionate quality gains in most experiments.

Community note (r/LocalLLaMA): "The community would probably pool money together to do this for Qwen 3.6 27B" — suggesting there's demand to apply this to smaller, cheaper local models.

## Related Entries
- [[orthrus-qwen3-acceleration]] ([Orthrus-Qwen3: Diffusion Attention for 7.8x LLM Speedup](../tools/orthrus-qwen3-acceleration.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
- [[sparky-offline-edge-ai-robot]] ([Sparky: Fully Offline Edge AI Robot](../tools/sparky-offline-edge-ai-robot.md))
---
<!-- RU -->

## Краткое описание
Динамическое распределение вычислительного бюджета (DCA) — техника тест-тайм вычислений, позволяющая локальной модели Qwen-35B-A3B приблизиться к производительности GPT-5.4-xHigh на бенчмарке HLE (Humanity's Last Exam), за счёт назначения приоритетов сложным задачам и запуска параллельных суб-агентов, генерирующих несколько попыток решения каждой задачи.

## Ключевые идеи
- Попросите LLM оценить набор задач, назначить приоритет/сложность каждой и выдать структурированный ответ, пригодный для параллелизации.
- Запустите независимые параллельные агенты, сосредоточенные на каждом под-подходе; количество попыток решения равно приоритету задачи.
- Базовая Qwen 3.6-35B-A3B набирает 21,4% на HLE (официально); GPT-5.4-xHigh — 41,6% (официально). С DCA Qwen достиг 39,9% — в 2 процентных пунктах от frontier-модели.
- Одношаговая денойзинг-генерация стабильно превосходит многошаговую (6,35× против 3,53× пропускная способность в связанных работах).
- Результат — пул решений без автоматического выбора финального ответа: человек (или модель-синтезатор) просматривает пул.

## Подробнее
Техника предназначена для ситуаций, когда вы хотите направить большой вычислительный бюджет на задачи, которые обычно тестируют на frontier-моделях. **Не рекомендуется** как постоянный инструмент агента для задач программирования: из-за расхождения параллельных попыток решения интеграция в единую кодовую базу затруднена.

**Рабочий процесс:**
1. Передайте LLM целевой набор задач и попросите назначить приоритеты.
2. Разберите структурированный вывод, чтобы определить, сколько попыток решения нужно на каждую задачу.
3. Для каждой задачи и каждого подхода запустите независимого агента, который видит только свою подзадачу и другие решения из пула.
4. Соберите все решения; пользователь просматривает их или модель-синтезатор выбирает наиболее правдоподобные.

**Одна итерация — оптимальная точка.** Более глубокое рекурсивное уточнение раздувает контекстное окно без пропорционального прироста качества в большинстве экспериментов.

Заметка сообщества (r/LocalLLaMA): «Сообщество, вероятно, скинется вместе, чтобы сделать это для Qwen 3.6 27B» — что говорит о спросе на применение техники к меньшим, более дешёвым локальным моделям.

## Связанные записи
- [[orthrus-qwen3-acceleration]] ([Orthrus-Qwen3: Diffusion Attention for 7.8x LLM Speedup](../tools/orthrus-qwen3-acceleration.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
- [[sparky-offline-edge-ai-robot]] ([Sparky: Fully Offline Edge AI Robot](../tools/sparky-offline-edge-ai-robot.md))
