---
title: "Parallelism Beats Higher Quants: Dual-GPU Subagent Strategy for Local Coding Agents"
title_ru: "Параллелизм важнее высоких квантов: стратегия субагентов на двух GPU для локальных кодинг-агентов"
category: tips
tags: [local-llm, multi-gpu, subagents, parallelism, quantization, qwen, coding-agent]
aliases: [dual GPU parallelism, subagent parallelism, parallelism over quants]
confidence: medium
updated: 2026-06-29
sources:
  - https://www.reddit.com/r/LocalLLaMA/comments/1uiuyyp/going_from_single_gpu_to_dual_gpu_is_nice_but_not/
---

## Summary
A r/LocalLLaMA practitioner reports that doubling VRAM (24 GB → 2×24 GB) did not improve local coding-agent quality the expected way (running higher quants for a "smarter" model). Instead, the biggest win came from **parallelism**: running a Qwen 27B orchestrator with a large context while spinning up 2 narrower Qwen 35B-A3B subagents in parallel — yielding 3 concurrent agents where there was previously only one.

## Key Ideas
- **The expectation vs. reality gap**: expected that 2× VRAM → higher quants → smarter model; in practice, the quality jump from Qwen 27B UD-Q4-XL to Q6/Q8 is rather small for coding.
- **Parallelism is the real multiplier**: splitting tasks into narrower subtasks passed to subagents (often Qwen 35B-A3B) that are "good enough when the task is narrow and well-defined."
- **Subagent lifecycle as a resource lever**: each subagent works with a ~115k context limit, reports back to the orchestrator, then dies — freeing the slot so another can spin up. This enables 2 concurrent subagents alongside the orchestrator.
- **No model unload/reload thrash**: because subagents are short-lived and scoped, you avoid the expensive model-swap latency of running one giant model.
- **Higher throughput, not higher IQ**: the win is more total work per unit time, not a single smarter agent.

## Details
This is a practical data point against the "always use the biggest/highest-quant model you can fit" instinct. For agentic coding — where work decomposes into many independent, well-scoped subtasks — the throughput of a small parallel swarm can beat a single high-quant brute-force run, because subagents with narrow scope perform well even at modest quants.

The pattern mirrors production agent-orchestration ideas (orchestrator + specialist subagents with isolated context) but applied to a single local workstation, using GPU memory as the scheduling constraint: keep the orchestrator resident, and rotate cheap subagents through the remaining capacity.

## Notable Quotes
> "Instead of getting a smarter LLM, I am using qwen 27B with a lot of context as the orchestrator, having split the tasks into smaller/narrower subtasks that then I can pass down to subagents." — r/LocalLLaMA

## Related Entries
- [[agent-orchestration-multi-model-framework]] ([Agent Orchestration: Multi-Model Frameworks](../agents/agent-orchestration-multi-model-framework.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[deepseek-flash-glm-advisor-config]] ([DeepSeek Flash + GLM Advisor Config](deepseek-flash-glm-advisor-config.md))

---
<!-- RU -->

## Краткое описание
Практик из r/LocalLLaMA сообщает, что удвоение VRAM (24 ГБ → 2×24 ГБ) не улучшило качество локального кодинг-агента ожидаемым образом (более высокие кванты → «умнее» модель). Главный выигрыш дал **параллелизм**: оркестратор Qwen 27B с большим контекстом плюс 2 узких субагента Qwen 35B-A3B параллельно — итого 3 конкурентных агента вместо одного.

## Ключевые идеи
- **Разрыв ожидания и реальности**: ожидалось, что 2× VRAM → более высокие кванты → умнее модель; на практике скачок качества от Qwen 27B UD-Q4-XL к Q6/Q8 для кодинга довольно мал.
- **Параллелизм — настоящий множитель**: разбиение задач на узкие подзадачи, передаваемые субагентам (часто Qwen 35B-A3B), «достаточно хороших, когда задача узкая и чётко определена».
- **Жизненный цикл субагента как рычаг ресурса**: каждый субагент работает с лимитом контекста ~115k, отчитывается оркестратору и умирает — освобождая слот для следующего. Это даёт 2 конкурирующих субагента рядом с оркестратором.
- **Без трэша выгрузки/загрузки моделей**: субагенты короткоживущие и ограниченные по сфере, что избегает дорогой задержки смены моделей.
- **Выше throughput, а не выше IQ**: выигрыш — больше общей работы за единицу времени, а не один более умный агент.

## Подробнее
Это практическое свидетельство против инстинкта «всегда бери самую большую/высококвантованную модель, какую влезет». Для агентного кодинга — где работа разбивается на множество независимых чётко очерченных подзадач — throughput малого параллельного роя может обыграть один высококвантованный брутфорс, поскольку субагенты с узкой сферой хорошо работают даже на скромных квантах.

Паттерн зеркалит продакшен-идеи оркестрации агентов (оркестратор + субагенты-специалисты с изолированным контекстом), но применён к одной локальной рабочей станции, где память GPU — ограничение планировщика.

## Связанные записи
- [[agent-orchestration-multi-model-framework]] ([Agent Orchestration: Multi-Model Frameworks](../agents/agent-orchestration-multi-model-framework.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[deepseek-flash-glm-advisor-config]] ([DeepSeek Flash + GLM Advisor Config](deepseek-flash-glm-advisor-config.md))
