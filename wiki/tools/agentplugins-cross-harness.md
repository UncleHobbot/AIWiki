---
title: "AgentPlugins — Write Once, Ship to Any Coding Agent Harness"
title_ru: "AgentPlugins — напиши плагин один раз, запускай в любом харнесе"
category: tools
tags: [plugins, cross-harness, copilot, opencode, claude-code, mcp, skills]
aliases: [AgentPlugins, sigilco agentplugins]
confidence: medium
updated: 2026-07-01
sources:
  - https://github.com/sigilco/agentplugins
  - https://www.reddit.com/r/GithubCopilot/comments/1ukqjps/i_wanted_to_try_out_more_workflows_on_copilot_cli/
---

## Summary
AgentPlugins is an open-source (Apache-2.0) toolchain that lets you author a plugin once in a single manifest and compile it down to the native primitives of any supported coding agent harness (GitHub Copilot CLI, OpenCode, Claude Code, and others).

## Key Ideas
- **Single manifest → many harnesses.** One declarative plugin definition is routed by a compiler into harness-native skills, agents, hooks, and commands per target.
- **Capability gaps are explicit, not silent.** The compiler emits a warning when a capability has no equivalent on a given harness, instead of silently breaking.
- **Targets power-user workflows** that are unevenly supported across harnesses: reduced token usage (snip/rtk-style), multi-agent orchestration, and long-running auto-improving workflows.
- Motivation: the author moved from OpenCode/Pi to Copilot CLI and found plugin architectures fragmented across every harness.

## Details
Each harness now exposes its own extension surface — Claude Code has skills/hooks, OpenCode has its plugin format, Copilot has commands/extensions. AgentPlugins treats these as compilation targets rather than separate ecosystems. The manifest describes intent; the compiler produces per-harness artifacts. This avoids the rewrite tax when a team standardizes on one CLI but wants community plugins built for another.

## Related Entries
- [[opencode]] ([OpenCode](opencode.md))
- [[claude-code]] ([Claude Code](claude-code.md))
- [[product-github-copilot]] ([GitHub Copilot](product-github-copilot.md))

---
<!-- RU -->

## Краткое описание
AgentPlugins — открытый (Apache-2.0) инструмент, позволяющий описать плагин один раз в едином манифесте и скомпилировать его в нативные примитивы любого поддерживаемого харнеса (GitHub Copilot CLI, OpenCode, Claude Code и др.).

## Ключевые идеи
- **Один манифест → много харнесов.** Декларативное определение плагина компилятор превращает в нативные skills, agents, hooks и команды конкретного харнеса.
- **Пробелы в возможностях явные, а не тихие.** Компилятор предупреждает, если у харнеса нет аналога возможности, вместо того чтобы молча сломаться.
- **Ориентирован на power-user сценарии**, которые поддерживаются харнесами неравномерно: сокращение расхода токенов, много-агентная оркестрация, длительные самоулучшающиеся процессы.
- Мотивация: автор перешёл с OpenCode/Pi на Copilot CLI и обнаружил, что архитектуры плагинов фрагментированы.

## Подробнее
Каждый харнес предоставляет свою поверхность расширения. AgentPlugins рассматривает их как цели компиляции, а не как отдельные экосистемы: манифест описывает намерение, а компилятор создаёт артефакты под конкретный харнес. Это избавляет от переписывания плагинов при стандартизации команды на одном CLI.

## Связанные записи
- [[opencode]] ([OpenCode](opencode.md))
- [[claude-code]] ([Claude Code](claude-code.md))
- [[product-github-copilot]] ([GitHub Copilot](product-github-copilot.md))
