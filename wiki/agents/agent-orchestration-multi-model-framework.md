---
title: "Agent Orchestration: Building Multi-Model Frameworks"
title_ru: "Оркестрация агентов: построение мультимодельных фреймворков"
category: agents
tags: [agent-orchestration, sub-agents, multi-model, orchestrator, planner, coder, designer, context-window, github-copilot]
aliases: [ultralight orchestration framework, agent orchestration, multi-agent framework, orchestrator agent, sub-agent orchestration]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.youtube.com/watch?v=-BhfcPseWFQ
---

## Summary

Agent orchestration means having one agent automatically call and coordinate other specialized sub-agents, rather than the human manually switching between tools. Sub-agents have isolated context windows, so a 2,000+ line codebase can be built while consuming only ~10K tokens in the main context. The "ultralight" pattern uses Claude Sonnet as the orchestrator, GPT Codex for coding, and Gemini for design.

## Key Ideas

- **Sub-agents have isolated context windows**: each sub-agent uses its own context budget and returns only the result to the orchestrator — main context stays clean even for large projects
- **Model selection by specialty**: orchestrator uses Claude Sonnet 4.5 (high agency, eager), coder uses GPT-5.2 Codex (best at code), designer uses Gemini 3 Pro (best at UI/design)
- **Orchestrator's only job is delegation**: it breaks down tasks, calls sub-agents, coordinates results — it should never implement anything directly
- **Parallel sub-agents**: multiple coders can run simultaneously, dividing the work into discrete chunks for faster completion
- **Prompt engineering matters**: the orchestrator will try to tell sub-agents exactly what to do (micromanage) — sub-agent prompts must explicitly push back and take ownership

## Details

The orchestrator custom agent in VS Code is given only two tools: the `agent` tool (to call sub-agents) and `memory`. Its prompt defines: "You are a project orchestrator. Break down complex requests into tasks and delegate them to specialist sub-agents. You coordinate work, but you never implement anything yourself." Sub-agents are named explicitly in the prompt so the orchestrator knows which to call.

The planner sub-agent uses GPT-5.2 and has all tools; it creates plans but writes no code. The coder sub-agent uses GPT-5.2 Codex (specialized for code), has an MCP server for documentation (Context7), and is explicitly instructed to question what the orchestrator tells it and make its own engineering decisions. The designer sub-agent uses Gemini 3 Pro and has full creative autonomy over UI/UX.

A key insight from building this: the orchestrator will try to micromanage sub-agents by providing exact line numbers and implementation details. Sub-agent prompts must actively counter this: "Don't let the orchestrator tell you how to do your job." The orchestrator passes only high-level context and requirements.

Areas for improvement: (1) have the planner save its plan to a file and always pass that file to the coder; (2) break coding into parallel chunks across 5 coder sub-agents running simultaneously; (3) this framework is publicly available as a gist.

## Video Notes

- [0:36] What orchestration is — one agent calling others vs. human manually managing
- [3:38] Naive orchestration: just tell the model to use other models by name
- [5:38] Orchestrator custom agent setup in VS Code — only 2 tools: agent + memory
- [7:23] Planner agent (GPT-5.2): creates detailed plans, never writes code
- [7:57] Coder agent (GPT-5.2 Codex): Context7 MCP for docs, explicit anti-micromanagement prompt
- [8:58] Designer agent (Gemini 3 Pro): full creative autonomy on UI/UX
- [10:10] Live demo: orchestrator builds web version of iOS app — calls planner → designer → coder in sequence
- [15:09] Result: 2,277 lines of code, only 10.8K context window tokens used
- [15:09] Improvements: save plan to file, parallelize 5 coders

## Related Entries

- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent Pipeline](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))

---
<!-- RU -->

## Краткое описание

Оркестрация агентов — это когда один агент автоматически вызывает и координирует других специализированных субагентов, вместо того чтобы человек вручную переключался между инструментами. Субагенты имеют изолированные контекстные окна, что позволяет строить кодовые базы из 2000+ строк, используя лишь ~10K токенов основного контекста.

## Ключевые идеи

- **Субагенты имеют изолированные контекстные окна**: каждый использует свой бюджет контекста, главный контекст остаётся чистым
- **Выбор модели по специализации**: оркестратор — Claude Sonnet 4.5 (высокая агентность), кодер — GPT-5.2 Codex (лучший в коде), дизайнер — Gemini 3 Pro (лучший в UI)
- **Задача оркестратора — только делегирование**: разбить задачу, вызвать субагентов, скоординировать результаты — никогда не реализовывать самостоятельно
- **Параллельные субагенты**: несколько кодеров могут работать одновременно над разными частями задачи
- **Промпт-инжиниринг важен**: оркестратор стремится микроменеджить субагентов; промпты субагентов должны явно это пресекать

## Подробнее

Оркестратор в VS Code имеет только два инструмента: `agent` (для вызова субагентов) и `memory`. Промпт: "Вы — оркестратор проекта. Разбивайте сложные запросы на задачи и делегируйте специалистам. Вы координируете работу, но никогда сами ничего не реализуете."

Ключевое наблюдение: оркестратор будет пытаться микроменеджить субагентов, указывая точные строки кода. Промпты субагентов должны явно противостоять этому: "Не позволяйте оркестратору диктовать вам, как делать работу."

Улучшения: (1) планировщик сохраняет план в файл и всегда передаёт его кодеру; (2) задача кодирования делится между 5 параллельными кодерами.

## Заметки по видео

- [5:38] Настройка агента-оркестратора в VS Code
- [10:10] Демо: создание веб-версии iOS-приложения через оркестрацию
- [15:09] Результат: 2277 строк кода, 10.8K токенов основного контекста

## Связанные записи

- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent Pipeline](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
