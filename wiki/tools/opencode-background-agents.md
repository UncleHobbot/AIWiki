---
title: "opencode-background-agents: Async Sub-Agent Delegation with Mid-Run Control"
title_ru: "opencode-background-agents: асинхронная делегация sub-agent с управлением во время выполнения"
category: tools
tags: [opencode, plugin, sub-agents, async, context-management, delegation]
aliases: [AeonDave/opencode-background-agents]
confidence: low
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/opencode/comments/1u3w41g/opencodebackgroundagents_async_subagent/
  - https://github.com/AeonDave/opencode-background-agents
---

## Summary
opencode-background-agents is an OpenCode plugin that runs delegated sub-agent tasks asynchronously in their own background sessions, with a supervisor interface to check status, peek at live transcripts, steer the run mid-execution, or stop it — solving the problem of long sub-agent runs being lost to context compaction.

## Key Ideas
- Calling `delegate(prompt, agent)` returns an ID immediately; the sub-agent runs in its own OpenCode session in the background (fire-and-forget).
- Adds interactive supervisor controls: status check, live transcript peek, mid-run steering, and stop.
- Builds on `kdcokenny/opencode-background-agents` for the core async-delegation idea, and the delegation engine from `code-yeongyu/oh-my-opencode`.
- Adds reliability work around lifecycle management and restart recovery — background tasks survive a restart instead of silently disappearing.
- Designed to fix two pain points: (1) a long research/refactor task being interrupted by mid-run context compaction and losing its result, and (2) the developer being blocked waiting for a sub-agent to finish.

## Details
The author describes months of using OpenCode as a primary coding assistant and repeatedly hitting the same failure mode: kicking off a long-running delegated task, having the context window compact mid-task, and either losing the in-progress result or having to re-run it from scratch. This plugin reframes sub-agent delegation as genuinely async — the parent session is not blocked, and the background session is resilient to compaction and process restarts.

This sits in the same design space as other "agent orchestration" plugins emerging in the OpenCode ecosystem (e.g. opencode-agents-sync for memory persistence), reflecting a broader community trend toward treating multi-agent delegation as a first-class, fault-tolerant primitive rather than a synchronous blocking call. Community source (Tier 3 — Reddit/GitHub self-promotion), no independent benchmarks given.

## Related Entries
- [[opencode-agents-sync-plugin]] ([opencode-agents-sync](../tools/opencode-agents-sync-plugin.md))

---
<!-- RU -->

## Краткое описание
opencode-background-agents — плагин для OpenCode, который запускает делегированные задачи sub-agent асинхронно в отдельных фоновых сессиях, с интерфейсом supervisor для проверки статуса, просмотра транскрипта в реальном времени, управления выполнением и остановки — решая проблему потери длинных запусков sub-agent из-за compaction контекста.

## Ключевые идеи
- Вызов `delegate(prompt, agent)` возвращает ID немедленно; sub-agent выполняется в собственной фоновой сессии OpenCode (fire-and-forget).
- Добавляет интерактивное управление supervisor: проверка статуса, просмотр транскрипта в реальном времени, управление во время выполнения и остановка.
- Основан на `kdcokenny/opencode-background-agents` (идея асинхронной делегации) и движке делегации из `code-yeongyu/oh-my-opencode`.
- Добавляет надёжность: управление жизненным циклом и восстановление после перезапуска — фоновые задачи переживают перезапуск, а не пропадают.
- Решает две проблемы: (1) длинная задача исследования/рефакторинга прерывается compaction контекста и теряет результат, (2) разработчик блокируется в ожидании завершения sub-agent.

## Подробнее
Автор описывает месяцы использования OpenCode как основного coding assistant и постоянное столкновение с одной и той же проблемой: запускается длинная делегированная задача, контекстное окно сжимается посередине выполнения (compaction), и промежуточный результат либо теряется, либо его приходится перезапускать с нуля. Плагин делает делегацию sub-agent по-настоящему асинхронной — родительская сессия не блокируется, а фоновая сессия устойчива к compaction и перезапускам процесса.

Это часть более широкого направления в экосистеме OpenCode — плагинов для оркестрации агентов (например, opencode-agents-sync для сохранения памяти), отражающего тенденцию рассматривать делегацию нескольким агентам как полноценный, устойчивый к сбоям примитив, а не синхронный блокирующий вызов. Источник community (tier 3 — самопродвижение на Reddit/GitHub), независимых бенчмарков не приведено.

## Связанные записи
- [[opencode-agents-sync-plugin]] ([opencode-agents-sync](../tools/opencode-agents-sync-plugin.md))
