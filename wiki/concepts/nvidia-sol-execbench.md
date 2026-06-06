---
title: "NVIDIA SOL-ExecBench"
title_ru: "NVIDIA SOL-ExecBench"
category: concepts
tags: [benchmark, nvidia, ai-generated-code, cuda, code-correctness, gpu-kernels]
aliases: [ExecBench, SOL ExecBench]
confidence: medium
date: 2026-05-28
updated: 2026-06-06
sources:
  - https://research.nvidia.com/benchmarks/sol-execbench
---

## Summary
NVIDIA SOL-ExecBench is a benchmark that evaluates the correctness and performance of AI-generated CUDA kernels. It highlights a critical failure mode: AI-generated GPU code that compiles and runs without errors but produces silently incorrect results, potentially corrupting model training.

## Key Ideas
- AI-generated CUDA kernels can compile and execute successfully yet produce wrong numerical results — a "silent correctness" failure that is far more dangerous than a crash.
- The benchmark tests whether LLM-generated GPU code is functionally equivalent to reference implementations, not just whether it compiles.
- This problem generalizes beyond CUDA: any domain where AI generates performance-critical code (shader programming, embedded systems, numerical computing) faces the same silent-correctness risk.
- Standard unit tests and type checks do not catch these errors — specialized equivalence testing or differential testing is required.

## Details
As coding agents increasingly generate low-level systems code, the assumption that "it compiles and runs" equals "it works" becomes dangerous. GPU kernels are a particularly acute case because numerical errors can propagate through millions of training iterations before anyone notices degraded model quality.

SOL-ExecBench addresses this by providing a standardized suite of CUDA kernel tasks where the correct output is known, and the benchmark measures both functional correctness and execution speed. A kernel that runs fast but produces wrong results scores poorly.

This connects to a broader theme in AI-generated code: the need for semantic verification, not just syntactic correctness. Traditional CI checks (compilation, linting, basic tests) are insufficient when the code author is a model that may produce plausible-looking but subtly wrong implementations.

The benchmark is particularly relevant for teams using AI agents to write or optimize GPU code for ML training pipelines, where a single corrupted kernel can silently degrade model accuracy across an entire training run.

## Notable Quotes
> "AI-generated CUDA kernels silently breaking training" — Inbox annotation on SOL-ExecBench

## Related Entries
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[clean-architecture-ai-coding-era]] ([Clean Architecture in AI Coding Era](../concepts/clean-architecture-ai-coding-era.md))
- [[minicheck-fact-verification]] ([MiniCheck Fact Verification](../tools/minicheck-fact-verification.md))

---
<!-- RU -->

## Краткое описание
NVIDIA SOL-ExecBench — это бенчмарк для оценки корректности и производительности CUDA-ядер, сгенерированных ИИ. Он выявляет критический тип ошибок: сгенерированный GPU-код компилируется и выполняется без ошибок, но выдаёт неправильные результаты, что может незаметно разрушить процесс обучения модели.

## Ключевые идеи
- Сгенерированные ИИ CUDA-ядра могут компилироваться и выполняться успешно, но давать неверные численные результаты — «тихая некорректность», опаснее краша.
- Бенчмарк проверяет функциональную эквивалентность сгенерированного кода эталонной реализации, а не только факт компиляции.
- Проблема распространяется за пределы CUDA: любой домен, где ИИ генерирует критичный к производительности код, сталкивается с тем же риском тихих ошибок.
- Стандартные unit-тесты и проверки типов не ловят такие ошибки — требуется специализированное тестирование эквивалентности.

## Подробнее
По мере того как кодинг-агенты всё чаще генерируют низкоуровневый системный код, предположение «скомпилировалось и запустилось = работает» становится опасным. GPU-ядра — особенно острый случай: численные ошибки могут распространяться через миллионы итераций обучения, прежде чем кто-то заметит снижение качества модели.

SOL-ExecBench решает эту проблему, предоставляя стандартизированный набор задач для CUDA-ядер, где правильный результат известен, а бенчмарк измеряет как функциональную корректность, так и скорость выполнения. Ядро, работающее быстро, но выдающее неверные результаты, получает низкую оценку.

Это связано с более широкой темой в ИИ-генерируемом коде: необходимостью семантической верификации, а не только синтаксической корректности. Традиционные CI-проверки (компиляция, линтинг, базовые тесты) недостаточны, когда автор кода — модель, которая может создать правдоподобную, но тонко некорректную реализацию.

## Примечательные цитаты
> «Сгенерированные ИИ CUDA-ядра незаметно ломают обучение» — аннотация к SOL-ExecBench

## Связанные записи
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[clean-architecture-ai-coding-era]] ([Clean Architecture in AI Coding Era](../concepts/clean-architecture-ai-coding-era.md))
- [[minicheck-fact-verification]] ([MiniCheck Fact Verification](../tools/minicheck-fact-verification.md))
