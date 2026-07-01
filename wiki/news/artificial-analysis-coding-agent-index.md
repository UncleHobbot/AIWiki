---
title: "Artificial Analysis Coding Agent Index: Benchmarking Model+Harness Combinations"
title_ru: "Coding Agent Index от Artificial Analysis: бенчмарк комбинаций модель+харнес"
category: news
tags: [benchmarks, coding-agents, swe-bench, terminal-bench, artificial-analysis, leaderboard, model-comparison, harness]
aliases: [AA Coding Agent Index, Artificial Analysis coding agent, coding agent leaderboard]
confidence: medium
date: 2026-05-22
updated: 2026-05-22
sources:
  - https://artificialanalysis.ai/agents/coding-agents
  - https://www.reddit.com/r/singularity/comments/1tcs72k/
---

## Summary

Artificial Analysis launched a **Coding Agent Index** that benchmarks model and harness *combinations* rather than models in isolation — using three complementary benchmarks to measure real-world coding agent performance across task completion, terminal operation, and code understanding.

## Key Ideas

- **Model + harness, not model alone.** The index explicitly evaluates which *model+harness combination* performs best, acknowledging that the same model can perform very differently depending on the agent framework wrapping it.
- **Three-benchmark composite:** SWE-Bench-Pro-Hard-AA (150 hard coding tasks from Scale AI), Terminal-Bench v2 (84 agentic terminal tasks: sysadmin, cryptography, ML), and SWE-Atlas-QnA (124 technical codebase questions).
- **Cost-per-task metric.** The index also reports pay-per-token API cost per task (accounting for cached vs uncached token pricing), making it a practical cost-efficiency comparison, not just a capability one.
- **Broad task coverage.** The three benchmarks deliberately cover different competencies: autonomous task completion (SWE-Bench), terminal/CLI agent operation (Terminal-Bench), and deep code comprehension without execution (SWE-Atlas-QnA).
- **r/singularity traction.** 168 pts, 56 comments — strong community interest as a reference benchmark for 2026 coding agent comparisons.

## Details

Artificial Analysis is an independent AI benchmarking organisation that operates the [artificialanalysis.ai](https://artificialanalysis.ai) leaderboard. The Coding Agent Index is their first agent-specific product, extending their existing model benchmarks to the agent+harness layer.

### The Three Benchmarks

**SWE-Bench-Pro-Hard-AA** (150 tasks): Sampled from Scale AI's SWE-Bench Pro, deliberately selecting tasks that current frontier models struggle with. Rewards genuine problem-solving capability over benchmark saturation.

**Terminal-Bench v2** (84 tasks, Laude Institute): Agentic terminal tasks covering system administration, cryptography, and ML workflows. Tests whether agents can operate effectively in real shell environments, not just edit code files.

**SWE-Atlas-QnA** (124 questions, Scale AI): Text-answer questions about real codebases — how code behaves, root causes of bugs, architectural explanations. Tests code understanding without execution, closer to what a senior engineer review looks like.

### Why Model + Harness Matters

The same LLM (e.g., Claude Opus 4.7 or GPT-5.5) can produce significantly different results depending on whether it's running in Claude Code, Codex CLI, OpenCode, or a custom harness. The index makes this explicit by tracking both variables, which makes its results more actionable: "use GPT-5.5 with harness X for terminal tasks" is more useful than "GPT-5.5 is the best coding model."

## Related Entries

- [[programbench-gpt55-first-solve]] ([ProgramBench: GPT-5.5 First Solve](../news/programbench-gpt55-first-solve.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[claude-code-explore-plan-code-commit]] ([Explore→Plan→Code→Commit Workflow](../tips/claude-code-explore-plan-code-commit.md))
- [[reap-coding-agent-benchmark-curation]] ([REAP — Coding-Agent Benchmarks from Production](../research/reap-coding-agent-benchmark-curation.md))

---
<!-- RU -->

## Краткое описание

Artificial Analysis запустила **Coding Agent Index** — бенчмарк, оценивающий *комбинации модель+харнес*, а не модели в отдельности. Используются три дополнительных бенчмарка для измерения реальной производительности агентов кодирования по выполнению задач, терминальным операциям и пониманию кода.

## Ключевые идеи

- **Модель + харнес, а не только модель.** Индекс явно оценивает, какая *комбинация модель+харнес* показывает лучший результат — признавая, что одна и та же модель может работать очень по-разному в зависимости от обёртывающего агентного фреймворка.
- **Три бенчмарка:** SWE-Bench-Pro-Hard-AA (150 сложных задач от Scale AI), Terminal-Bench v2 (84 агентные терминальные задачи: системное администрирование, криптография, ML), SWE-Atlas-QnA (124 технических вопроса о кодовых базах).
- **Метрика стоимости на задачу.** Индекс также сообщает стоимость токенов API на задачу, делая его практичным сравнением экономической эффективности.
- **Широкое покрытие задач.** Три бенчмарка намеренно охватывают разные компетенции: автономное выполнение задач, терминальные/CLI операции, глубокое понимание кода без исполнения.

## Подробнее

Artificial Analysis — независимая организация по бенчмаркингу ИИ. Coding Agent Index — их первый агент-специфичный продукт, расширяющий существующие бенчмарки моделей до слоя агент+харнес.

**SWE-Bench-Pro-Hard-AA**: 150 задач из SWE-Bench Pro Scale AI, намеренно отобранных как сложные для текущих моделей.

**Terminal-Bench v2**: 84 агентные терминальные задачи: системное администрирование, криптография, ML-рабочие процессы. Проверяет, может ли агент эффективно работать в реальных оболочках.

**SWE-Atlas-QnA**: 124 текстовых вопроса о реальных кодовых базах — поведение кода, корневые причины ошибок, архитектурные объяснения. Тестирует понимание кода без исполнения.

## Связанные записи

- [[programbench-gpt55-first-solve]] ([ProgramBench: GPT-5.5 First Solve](../news/programbench-gpt55-first-solve.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[claude-code-explore-plan-code-commit]] ([Explore→Plan→Code→Commit Workflow](../tips/claude-code-explore-plan-code-commit.md))
- [[reap-coding-agent-benchmark-curation]] ([REAP — Coding-Agent Benchmarks from Production](../research/reap-coding-agent-benchmark-curation.md))
