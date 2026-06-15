---
title: "The Verifier Tax: Safety-Success Tradeoffs in Tool-Using LLM Agents"
title_ru: "Verifier Tax: компромисс между безопасностью и успехом у tool-using агентов"
category: concepts
tags: [agents, ai-safety, tool-use, evaluation, benchmarks, verification]
aliases: [Verifier Tax, safe success vs unsafe success]
confidence: medium
updated: 2026-06-14
sources:
  - https://dl.acm.org/doi/full/10.1145/3786335.3813160
  - https://www.reddit.com/r/MachineLearning/comments/1u58mkq/the_verifier_tax_horizondependent_safetysuccess/
  - https://www.reddit.com/r/AI_Agents/comments/1u584ui/should_ai_agent_benchmarks_separate_safe_success/
---

## Summary
A paper presented at ACM CAIS 2026 argues that standard "task completion" metrics for tool-using LLM agents are misleading, because an agent can complete a task while violating a safety or policy constraint — and adding runtime verification to catch this introduces a "Verifier Tax" that gets worse as tasks get longer.

## Key Ideas
- Outcomes for tool-using agents should be split into three categories: **safe success** (task done, no constraint violated), **unsafe success** (task done, but a constraint was violated — wrong tool, skipped approval, leaked data, policy breach), and **failure**.
- The authors evaluate this on τ-bench / Tau-bench tool-use scenarios.
- They propose a **two-tier verification architecture**: fast deterministic policy/tool checks first, followed by an LLM-based verifier for more contextual safety judgments.
- Verification reduces unsafe success rates, but the same verification also reduces overall task completion — and this tradeoff grows worse as the task horizon (number of steps) increases. The authors call this the **Verifier Tax**.
- Practical implication: a system can become measurably safer while looking "worse" on conventional success-rate benchmarks, which can mislead teams comparing agents purely by completion rate.

## Details
The core critique is that most agent benchmarks report a single binary "did it finish the task" signal. For agents that call external tools (file systems, APIs, payment systems, code execution), this hides an important failure mode: the agent can finish the assigned task while doing something it shouldn't — using an unauthorized tool, bypassing a required human approval, or leaking sensitive information in the process.

To address this, the paper separates outcomes into three buckets and studies how adding verification layers shifts the distribution between them. Their two-tier design runs cheap deterministic checks (tool allowlists, policy rules) first, and escalates to an LLM-based verifier only for ambiguous or contextual cases — a pattern similar to defense-in-depth designs seen elsewhere in agent safety tooling.

The headline finding — the Verifier Tax — is that the safety/completion tradeoff is not fixed but horizon-dependent: for short tasks, verification has little cost, but for longer multi-step tasks, each additional verification checkpoint compounds the chance of a false-positive block, dragging down completion rates even when the agent's actions were actually safe. This suggests benchmark designers should report safe-success vs. unsafe-success vs. failure separately, rather than collapsing them into one "success rate," especially when comparing agents across different task horizons.

## Related Entries
- [[llm-assumption-propagation]] ([LLM Confusion Management](../tips/llm-assumption-propagation.md))

---
<!-- RU -->

## Краткое описание
Доклад на ACM CAIS 2026 утверждает, что стандартные метрики «завершения задачи» для tool-using LLM-агентов вводят в заблуждение: агент может завершить задачу, нарушив при этом политику безопасности, а добавление верификации в реальном времени создаёт «Verifier Tax» — компромисс, который усиливается с ростом длины задачи.

## Ключевые идеи
- Результаты работы tool-using агентов следует делить на три категории: **safe success** (задача выполнена, ограничения не нарушены), **unsafe success** (задача выполнена, но нарушено ограничение — неверный инструмент, пропущенный шаг согласования, утечка данных, нарушение политики) и **failure**.
- Авторы оценивают подход на сценариях τ-bench / Tau-bench.
- Предложена **двухуровневая архитектура верификации**: сначала быстрые детерминированные проверки политики/инструментов, затем LLM-верификатор для более сложных, контекстных случаев безопасности.
- Верификация снижает долю unsafe success, но одновременно снижает общую долю завершённых задач — и этот компромисс усиливается с ростом горизонта задачи (числа шагов). Авторы называют это **Verifier Tax**.
- Практический вывод: система может стать измеримо безопаснее, но при этом «хуже» выглядеть по традиционным метрикам успешности — что может вводить команды в заблуждение при сравнении агентов только по completion rate.

## Подробнее
Основная критика в том, что большинство бенчмарков агентов отображают единственный бинарный сигнал — «завершена ли задача». Для агентов, вызывающих внешние инструменты (файловые системы, API, платёжные системы, выполнение кода), это скрывает важный класс отказов: агент может завершить задачу, но сделать что-то недопустимое — использовать неавторизованный инструмент, обойти требуемое подтверждение человека или раскрыть чувствительные данные в процессе.

Для решения этой проблемы авторы разделяют результаты на три категории и изучают, как добавление слоёв верификации сдвигает их распределение. Их двухуровневая архитектура сначала выполняет дешёвые детерминированные проверки (списки разрешённых инструментов, правила политики), а к LLM-верификатору обращается только в неоднозначных или контекстных случаях — паттерн, похожий на подходы defense-in-depth в других инструментах безопасности агентов.

Главный результат — Verifier Tax — показывает, что компромисс между безопасностью и завершённостью задачи не постоянен, а зависит от горизонта задачи: для коротких задач верификация почти не влияет на результат, но для длинных многошаговых задач каждая дополнительная проверка увеличивает шанс ложноположительной блокировки, снижая completion rate даже когда действия агента на самом деле были безопасны. Это означает, что разработчикам бенчмарков стоит отдельно сообщать safe-success, unsafe-success и failure, а не объединять их в единый «success rate», особенно при сравнении агентов с разными горизонтами задач.

## Связанные записи
- [[llm-assumption-propagation]] ([LLM Confusion Management](../tips/llm-assumption-propagation.md))
