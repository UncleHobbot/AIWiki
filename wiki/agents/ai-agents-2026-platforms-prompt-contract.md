---
title: "AI Agents in 2026: Platforms, Prompt Contracts, and Self-Modifying Memory"
title_ru: "AI-агенты в 2026: платформы, контракты промптов и самомодифицирующаяся память"
category: agents
tags: [ai-agents, claude-code, codex, openclaw, antigravity, prompt-contract, memory, claude-md, agent-platforms, 2026]
aliases: [prompt contract, agent prompt structure, goal constraints format failure, agent platforms comparison, AI agents guide 2026]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.youtube.com/watch?v=4TvH-OZhwxI
---

## Summary

A practical guide to AI agents in 2026: the four leading platforms (Claude Code, OpenAI Codex, OpenClaw, AntiGravity), the "prompt contract" framework for reliable agent prompts (Goal / Constraints / Format / Failure), and the self-modifying memory pattern that prevents agents from repeating the same mistakes across sessions.

## Key Ideas

- **Agent = LLM + Tools + Memory + Goals + Loop** (Observe → Think → Act → repeat until goal met)
- **Prompt contract has four required sections**: Goal (outcome, not action), Constraints (what agent cannot do), Format (exact shape of output), Failure (what to do when stuck)
- **Self-modifying memory**: instruct agent to append new rules to CLAUDE.md whenever you correct it — agents learn from your corrections permanently
- **Platform selection rule of thumb**: words/code → Claude Code; lowest friction (already in ChatGPT) → Codex; life automation → OpenClaw; visual/frontend → AntiGravity
- **Claude Code is not just a coding tool** — the name misleads; it handles file cleanup, PDF parsing, batch rename, data extraction — anything describable in plain English on a computer

## Details

All four platforms share the same agent loop. What differs is what's "wired around the brain": tools available, memory format, interface, and ecosystem integration.

**Claude Code** — Anthropic's official desktop agent. Requires Claude Pro ($17–20/month). Strongest for complex, orchestrated tasks with transparent reasoning you can steer mid-flight. Best when you want a thinking partner, not a missile.

**OpenAI Codex** — Included in ChatGPT Plus ($20/month). Lowest friction for existing ChatGPT users. VS Code/Cursor IDE integration with built-in diff view. Has a cloud sandbox mode (hand off task, walk away, review finished branch). Best for developers already living in ChatGPT.

**OpenClaw (Open Claw)** — Self-hosted, lives inside messengers (Telegram, WhatsApp, iMessage, Discord, Signal, Slack, 20+ apps). Install via one terminal command. Text from anywhere, agent acts on your computer and replies. Best for life automation: email triage, reminders, document creation, project management.

**AntiGravity (Google)** — Heavily modified VS Code fork powered by Gemini 3 Pro. Free public preview, no card required. Multimodal (reads screenshots, analyzes layouts). Best for frontend, design iteration, landing pages, visual work.

**Prompt Contract in practice**: vague chatbot-style prompts cause agents to go off-rails and burn tokens. A complete prompt specifies: Goal ("build a single-page landing site for my SaaS launch optimized for email sign-ups above the fold, ready for local review before deploying"), Constraints (single index.html, inline CSS, no JS frameworks, no external CDN, no deploy), Format (landing folder with index.html + brief.md listing sections with headline copy used), Failure (if target audience unclear from project notes, stop and ask one consolidated question rather than guessing).

**Self-modifying memory**: each platform has a memory file (CLAUDE.md for Claude Code, agents.md for OpenClaw). Instruction: "If I corrected you or you hit a bug from a wrong assumption, append a new rule to the learned_rules section at the bottom of this file." Session 1: 1 rule. Session 5: 20 rules. Session 20: the agent rarely makes preference mistakes — it has been writing its own scar tissue.

## Video Notes

- [0:00] Chatbot vs agent: same brain, different scaffolding (chef analogy)
- [4:00] Four platform tour: Claude Code, Codex, OpenClaw, AntiGravity
- [18:00] Prompt contract framework: Goal / Constraints / Format / Failure
- [35:00] Memory: CLAUDE.md and self-modifying rules pattern
- [40:00] Action plan: pick one platform, write a real task as a contract, add 3 rules to memory file

## Related Entries

- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent Pipeline](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[autonomous-personal-agents-openclaw-hermes-zeroclaw]] ([OpenClaw and Personal Agents](../agents/autonomous-personal-agents-openclaw-hermes-zeroclaw.md))
- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))
- [[context-engineering-ai-agents-pipeline]] ([Context Engineering](../tips/context-engineering-ai-agents-pipeline.md))

---
<!-- RU -->

## Краткое описание

Практическое руководство по AI-агентам в 2026: четыре ведущие платформы (Claude Code, OpenAI Codex, OpenClaw, AntiGravity), фреймворк "контракт промпта" (Цель / Ограничения / Формат / Сбой) и паттерн самомодифицирующейся памяти.

## Ключевые идеи

- **Агент = LLM + Инструменты + Память + Цели + Петля** (Наблюдение → Мышление → Действие)
- **Контракт промпта — 4 обязательных раздела**: Цель (результат, а не действие), Ограничения (что нельзя делать), Формат (точная форма вывода), Сбой (что делать при проблемах)
- **Самомодифицирующаяся память**: инструкция агенту добавлять новые правила в CLAUDE.md при каждой коррекции — агент учится постоянно
- **Правило выбора платформы**: слова/код → Claude Code; минимальное трение → Codex; автоматизация жизни → OpenClaw; визуальное/frontend → AntiGravity

## Подробнее

Все четыре платформы используют одну и ту же петлю агента. Отличаются доступные инструменты, формат памяти, интерфейс и экосистемная интеграция.

**Контракт промпта**: расплывчатые промпты заставляют агентов отклоняться и тратить токены впустую. Полный промпт включает: Цель (не "сделай лендинг", а "создай одностраничный сайт для запуска SaaS, оптимизированный для email-подписок выше сгиба, готовый к локальному просмотру"), Ограничения, Формат (точный список файлов), Сбой (если целевая аудитория непонятна — задай один сводный вопрос).

**Самомодифицирующаяся память**: инструкция агенту добавлять правила в CLAUDE.md при любой коррекции. Сессия 1: 1 правило. Сессия 5: 20 правил. К сессии 20 агент редко делает повторяющиеся ошибки.

## Заметки по видео

- [4:00] Обзор четырёх платформ
- [18:00] Фреймворк контракта промпта
- [35:00] Паттерн самомодифицирующейся памяти

## Связанные записи

- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent Pipeline](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[autonomous-personal-agents-openclaw-hermes-zeroclaw]] ([OpenClaw and Personal Agents](../agents/autonomous-personal-agents-openclaw-hermes-zeroclaw.md))
- [[claude-code-memory]] ([Claude Code Memory](../agents/claude-code-memory.md))
- [[context-engineering-ai-agents-pipeline]] ([Context Engineering](../tips/context-engineering-ai-agents-pipeline.md))
