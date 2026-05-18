---
title: "LLM Project Memory via Git: Plan-Execute-Distill Loop"
title_ru: "Накопление знаний проекта через Git: цикл «план–выполнение–дистилляция»"
category: tips
tags: [workflow, git, llm-memory, context, coding-patterns, plan-distill]
aliases: [plan execute distill, LLM git workflow, knowledge accumulation workflow, distill loop]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.reddit.com/r/ChatGPTCoding/comments/1sqwmx9/sanity_check_using_git_to_make_llmassisted_work/
---

## Summary

Instead of losing context after each LLM coding session, a structured Plan → Execute → Distill → Commit cycle stores knowledge permanently in the git repo. The distillation step — extracting only what's reusable into playbooks and lessons — is the only step that compounds over time; skipping it turns the workflow into ordinary note-taking.

## Key Ideas

- **The core loop**: Plan (define approach, store in repo) → Execute (LLM-assisted coding) → Close out (what happened vs. plan) → Distill (extract reusables, update guides) → Commit (future tasks start from better context).
- **Distillation is the compounding step**: writing what was learned in a reusable form — playbooks, repo guidance, lessons — is where value accumulates. "Doing the plan is fun, shipping the code is fun, writing the 'what we learned and when NOT to do this' doc feels like overhead" — but it's the only step that matters long-term.
- **Short plans**: cap plans at 3-4 sentences. Short plans force you to confront the real unknowns. Plans that balloon to 300 lines hide ambiguity instead of resolving it.
- **Separate state from decisions**: store current code state in files, store *why* decisions were made in a DECISIONS.md. Git history records what changed, not why — the LLM needs the why to avoid re-litigating past choices.
- **Tool-agnostic**: the loop works across Claude Code, Codex, Cursor, or any LLM tool — value is in the workflow structure, not the specific agent.
- **Commit execution artifacts**: even messy execution logs become valuable debugging context. Use a `scratchpad/` folder that's committed but excluded from LLM context rather than gitignored.

## Details

The problem this solves: without a retention loop, every LLM session starts cold. The model re-learns what doesn't work, re-makes the same architecture decisions, and overloads prompts with accumulated compensatory context. The plan→distill loop builds a project memory that genuinely compounds.

The workflow stores three artifact types in the repo:
1. **Plans** (committed): approach, constraints, expectations — written before execution.
2. **Task artifacts** (scratchpad/, committed but not injected into LLM context): execution logs, intermediate outputs, debugging notes.
3. **Distilled knowledge** (committed, injected into context): playbooks, repo guidance, lessons learned — only what is reusable.

Common failure mode: adopting the plan and execute steps but skipping distillation. Without distillation, the repo fills with plans and artifacts but the model still starts cold next session.

## Notable Quotes

> "The distillation step is where most people quit. Writing the plan is fun, shipping the code is fun, writing the 'what we learned and when NOT to do this' doc feels like overhead. But that's the only step that actually compounds. Everything else is just normal work with an LLM." — r/ChatGPTCoding community

> "Prompting is praying. Verification is how you get real results." — r/ChatGPTCoding

## Related Entries

- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](./claude-code-workflows-best-practices.md))
- [[karpathy-claude-code-guidelines]] ([Karpathy's Claude Code Guidelines](./karpathy-claude-code-guidelines.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development with BMAD](./spec-driven-development-bmad.md))

---
<!-- RU -->

## Краткое описание

Вместо того чтобы терять контекст после каждой сессии с LLM, структурированный цикл «план → выполнение → дистилляция → коммит» сохраняет знания постоянно в git-репозитории. Шаг дистилляции — единственный, который накапливает ценность со временем.

## Ключевые идеи

- **Базовый цикл**: Планирование (определить подход, сохранить в репо) → Выполнение (LLM-кодинг) → Закрытие задачи (что случилось vs. план) → Дистилляция (извлечь переиспользуемое) → Коммит (следующие задачи стартуют с лучшего контекста).
- **Дистилляция — это шаг накопления**: написание полезных на будущее руководств, уроков и плейбуков — единственный шаг, который даёт долгосрочную ценность. Большинство бросают именно здесь.
- **Короткие планы**: ограничивайте планы 3–4 предложениями. Короткие планы заставляют столкнуться с реальными неизвестными. Длинные планы прячут неопределённость.
- **Разделяйте состояние и решения**: текущий код — в файлах, *причины* решений — в DECISIONS.md. Git-история фиксирует что изменилось, но не почему.
- **Независимость от инструментов**: цикл работает с Claude Code, Codex, Cursor и любым другим LLM-инструментом.
- **Коммитьте артефакты выполнения**: даже черновые логи полезны при отладке. Используйте папку `scratchpad/`, закоммиченную, но не вводимую в контекст LLM.

## Подробнее

Проблема, которую это решает: без цикла удержания знаний каждая LLM-сессия начинается с нуля. Модель заново изучает, что не работает, и перегружает промпты накопленным компенсаторным контекстом. Цикл план→дистилляция строит «память проекта», которая реально накапливается.

В репо хранятся три типа артефактов: планы (закоммичены и вводятся в контекст), артефакты выполнения (черновики, лог отладки — закоммичены, но исключены из контекста LLM), дистиллированные знания (плейбуки, уроки — закоммичены и вводятся в контекст).

## Примечательные цитаты

> «Шаг дистилляции — это то, где большинство сдаётся. Написание плана — весело, написание кода — весело, написание документа о том, что мы узнали и когда НЕ нужно это делать, кажется накладными расходами. Но именно этот шаг единственный, который накапливается со временем.» — r/ChatGPTCoding

## Связанные записи

- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](./claude-code-workflows-best-practices.md))
- [[karpathy-claude-code-guidelines]] ([Karpathy's Claude Code Guidelines](./karpathy-claude-code-guidelines.md))
- [[spec-driven-development-bmad]] ([Spec-Driven Development with BMAD](./spec-driven-development-bmad.md))
