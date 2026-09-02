---
title: "Claude Opus 4.8: Parallel Subagents, Fast Mode, and Stronger Agentic Judgment"
title_ru: "Claude Opus 4.8: параллельные субагенты, Fast Mode и улучшенное агентное мышление"
category: news
tags: [anthropic, claude, opus, model-release, agentic, claude-code, parallel-subagents, fast-mode]
aliases: [Opus 4.8, claude-opus-4-8, Claude 4.8]
confidence: high
date: 2026-05-28
updated: 2026-06-05
sources:
  - https://www.anthropic.com/news/claude-opus-4-8
  - https://www.reddit.com/r/ollama/comments/1twpep6/claude_code_opus_48_vs_local_qwen36_27b_oneshot/
  - https://www.reddit.com/r/singularity/comments/1ts5b6u/opus_48_leads_the_singularity_gate_new_benchmark/
---

## Summary
Claude Opus 4.8, released May 28, 2026, improves on Opus 4.7 with sharper agentic judgment, dynamic parallel subagents in Claude Code for massive-scale tasks, a new effort-control feature on claude.ai, and a Fast Mode that runs at 2.5× speed at 3× cheaper pricing.

## Key Ideas
- **Parallel subagents in Claude Code**: dynamic workflows now let Claude Code spin up and coordinate parallel subagents for large-scale tasks — the biggest workflow change since agentic mode launched.
- **4× fewer missed code flaws**: Opus 4.8 is approximately four times less likely than 4.7 to allow code defects to pass unreported, while also being more willing to flag uncertainties.
- **Effort control on claude.ai**: users can now balance quality vs. speed explicitly, choosing how much compute to spend on a given task.
- **Fast Mode**: 2.5× faster, 3× cheaper than standard Opus 4.8 (same input/output token pricing as Opus 4.7 at $5/$25 per million tokens for standard; Fast Mode at $10/$50).
- **Benchmarks**: outperforms 4.7 on coding, agentic tasks, reasoning, and knowledge work; independent community benchmarks show it surpassing GPT-5.5 High on some agentic tasks.

## Details
The parallel subagents feature in Claude Code is the most significant architectural addition. Rather than sequential agent work, Claude Code can now delegate independent work streams to parallel subagents simultaneously — useful for large refactors, cross-service integrations, or any task that can be decomposed into independent pieces. Users on the community report this makes "massive-scale tasks" practical for the first time.

The improvement in code defect detection (4× better than 4.7) directly addresses one of the main criticisms of agentic coding tools: the agent writes code that looks correct but contains subtle security or correctness issues. Opus 4.8's stronger self-review mode catches more of these before they reach a pull request.

Fast Mode trades some quality for significant cost and latency reduction — at 3× cheaper, it becomes practical for high-volume tasks like initial triage, bulk classification, or draft generation where the standard quality ceiling is unnecessary.

API model ID: `claude-opus-4-8`

## Related Entries
- [[product-claude-code]] ([Claude Code](../agents/product-claude-code.md))
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-security-plugin-code-review]] ([Claude Security Plugin](../news/claude-security-plugin-code-review.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))

---
- [[claude-opus-5-backlash]] ([Opus 5 Backlash](claude-opus-5-backlash.md))
<!-- RU -->

## Краткое описание
Claude Opus 4.8, выпущенный 28 мая 2026 года, улучшает 4.7 более точным агентным мышлением, динамическими параллельными субагентами в Claude Code, новым управлением усилиями на claude.ai и Fast Mode со скоростью в 2,5× быстрее при стоимости в 3× ниже.

## Ключевые идеи
- **Параллельные субагенты в Claude Code**: динамические workflow теперь позволяют Claude Code запускать и координировать параллельных субагентов для масштабных задач.
- **В 4× меньше пропущенных дефектов кода**: Opus 4.8 примерно в четыре раза реже пропускает дефекты кода незамеченными, а также чаще сообщает о неопределённостях.
- **Управление усилиями на claude.ai**: пользователи теперь могут явно балансировать качество и скорость, выбирая объём вычислений для задачи.
- **Fast Mode**: в 2,5× быстрее, в 3× дешевле стандартного Opus 4.8.
- **Бенчмарки**: превосходит 4.7 по кодингу, агентным задачам, рассуждению и работе со знаниями.

## Подробнее
Параллельные субагенты в Claude Code — самое значимое архитектурное дополнение. Вместо последовательной агентной работы Claude Code теперь может делегировать независимые потоки работы параллельным субагентам одновременно — полезно для крупных рефакторингов, межсервисных интеграций или любых задач, которые можно разбить на независимые части.

Улучшение обнаружения дефектов кода (в 4× лучше, чем 4.7) напрямую решает одну из главных проблем агентных инструментов программирования: агент пишет код, который выглядит правильным, но содержит скрытые дефекты безопасности или корректности.

API идентификатор модели: `claude-opus-4-8`

## Связанные записи
- [[product-claude-code]] ([Claude Code](../agents/product-claude-code.md))
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-security-plugin-code-review]] ([Claude Security Plugin](../news/claude-security-plugin-code-review.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
