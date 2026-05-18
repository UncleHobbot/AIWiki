---
title: "AI Agents: ARR Framework, OODA Loop, and Why Agents Fail"
title_ru: "AI-агенты: фреймворк ARR, петля OODA и почему агенты ошибаются"
category: concepts
tags: [ai-agents, arr-framework, ooda-loop, agent-failure, judgment, narrow-agent, automation, vague-goals]
aliases: [ARR framework, autonomous recurring reviewable, OODA agent loop, agent failure modes, why AI agents fail]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.youtube.com/watch?v=P5sKKnWCvzk
---

## Summary

A concise conceptual framework for understanding, using, and succeeding with AI agents. The ARR framework (Autonomous, Recurring, Reviewable) tells you when to use an agent vs. a prompt. The OODA loop explains how agents adapt when plans break. The key failure mode is not bad models — it's vague human instructions that agents faithfully amplify.

## Key Ideas

- **ARR framework for task selection**: a task is a good agent candidate if it is Autonomous (runs without live judgment), Recurring (happens repeatedly), and Reviewable (you can verify correctness) — if any condition fails, use a prompt instead
- **Agents decide next actions; chatbots predict next words** — this is the fundamental architectural difference, not just a capability difference
- **OODA loop**: agents adapt like fighter pilots — Observe the current state, Orient to what matters, Decide next action, Act; repeat faster than the environment changes
- **Agents are amplifiers, not fixers**: they amplify vague thinking, bad processes, and unclear goals — giving an agent a bad instruction produces a bad result faster and with more confidence
- **GPS check before automating**: Goal (one clear sentence), Proof (what does good look like?), Steps (describe each step precisely) — if you can't answer all three, don't automate yet
- **The opportunity is narrow, not broad**: "find a highly specific task people hate doing but must do repeatedly — that's where the money is"

## Details

**The chatbot vs. agent mental shift**: Using a prompt is like sitting next to a student driver — you guide every turn. Using an agent is like hiring a driver — you set the destination, sit in the back, and it handles route, traffic, and all step-by-step decisions. The same model can be either, depending on what's "wired around the brain."

**Agent anatomy — four internal workers around the LLM core**:
1. Analyst — finds patterns in data
2. Planner — decides what matters and what belongs in the output
3. Operator — executes the output or takes action
4. Auditor — checks for weak logic, missing context, refines

**OODA loop origin**: Air Force Colonel John Boyd studied why American F-86 fighters beat technically superior Soviet MiGs in the Korean War. The answer: American pilots had better cockpit visibility and could complete their decision cycle faster. Boyd called this the OODA loop (Observe-Orient-Decide-Act). An agent uses the same loop when a workflow breaks: it doesn't just follow the script, it reroutes. A workflow follows process; an agent adapts process.

**Why agents fail in real life**: "An agent is a mirror — it reflects the quality of your thinking back at you." CMOs, CEOs, and teams building AI fail not because the models are bad, but because humans haven't clarified the process first. The GPS check (Goal/Proof/Steps) is a self-assessment before automating anything. The difference between "summarize my emails every morning" and "every morning at 7 AM, read my unread emails, categorize by urgency, draft replies to routine messages, and flag anything from my top five customers" is exactly where the mess lives.

**The real opportunity**: "Output gets cheap — content, code, analysis all becoming super cheap. When intelligence becomes cheap, judgment becomes expensive. When output becomes infinite, taste becomes scarce." The winners aren't building the broadest agents — they build the one agent that understands one workflow, one market, one user pain better than everyone else.

## Video Notes

- [0:00] ARR framework introduction
- [4:00] Agent anatomy: four internal workers (analyst, planner, operator, auditor)
- [6:00] OODA loop — Air Force origin and agent application
- [9:00] Why agents fail: amplify vague thinking, GPS check
- [11:00] The narrow opportunity: specific repeated tasks, judgment as the scarce resource

## Related Entries

- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent Pipeline](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[ai-agents-2026-platforms-prompt-contract]] ([AI Agents 2026 Guide](../agents/ai-agents-2026-platforms-prompt-contract.md))
- [[agent-orchestration-multi-model-framework]] ([Agent Orchestration Framework](../agents/agent-orchestration-multi-model-framework.md))
- [[context-engineering-ai-agents-pipeline]] ([Context Engineering](../tips/context-engineering-ai-agents-pipeline.md))

---
<!-- RU -->

## Краткое описание

Концептуальный фреймворк для понимания, применения и успеха с AI-агентами. ARR-фреймворк (Autonomous, Recurring, Reviewable) указывает, когда использовать агента, а когда промпт. Петля OODA объясняет адаптацию агентов. Главная причина неудач агентов — не плохие модели, а размытые инструкции людей.

## Ключевые идеи

- **ARR-фреймворк**: задача — хороший кандидат для агента, если она Автономна (работает без живого контроля), Повторяется и Проверяема — если хотя бы одно условие не выполняется, используйте промпт
- **Агенты решают, какое действие предпринять; чатботы предсказывают следующее слово** — фундаментальная архитектурная разница
- **Петля OODA**: агенты адаптируются как пилоты-истребители — Наблюдать, Ориентироваться, Решать, Действовать
- **Агенты — усилители, а не исправители**: они усиливают размытое мышление и плохие процессы
- **GPS-проверка перед автоматизацией**: Цель (одно ясное предложение), Доказательство (как выглядит хороший результат?), Шаги (опишите каждый шаг точно)
- **Возможность — в узком, не широком**: найдите конкретную задачу, которую люди ненавидят, но обязаны делать регулярно

## Подробнее

**Анатомия агента — четыре внутренних "работника" вокруг LLM**:
1. Аналитик — находит паттерны в данных
2. Планировщик — решает, что важно и что войдёт в вывод
3. Оператор — выполняет вывод или действие
4. Аудитор — проверяет логику, уточняет

**Происхождение петли OODA**: полковник ВВС Джон Бойд изучал, почему американские F-86 побеждали технически превосходящие советские МиГи в Корейской войне. Ответ: лучший обзор и более быстрый цикл решений. Агент делает то же самое при сбое рабочего процесса — не следует скрипту, а перепроектирует маршрут.

**Почему агенты ошибаются**: "Агент — это зеркало. Он отражает качество вашего мышления." Разница между "суммаризируй мои письма утром" и "каждое утро в 7:00 прочитай непрочитанные письма, категоризируй по срочности, набросай ответы на рутинные, пометь письма от топ-5 клиентов" — именно там живёт хаос.

## Заметки по видео

- [0:00] Введение ARR-фреймворка
- [4:00] Анатомия агента: четыре внутренних работника
- [6:00] Петля OODA — военное происхождение и применение в агентах
- [9:00] Почему агенты ошибаются; GPS-проверка

## Связанные записи

- [[anatomy-ai-agent-pipeline-loop-tools]] ([Anatomy of an AI Agent Pipeline](../agents/anatomy-ai-agent-pipeline-loop-tools.md))
- [[ai-agents-2026-platforms-prompt-contract]] ([AI Agents 2026 Guide](../agents/ai-agents-2026-platforms-prompt-contract.md))
- [[agent-orchestration-multi-model-framework]] ([Agent Orchestration Framework](../agents/agent-orchestration-multi-model-framework.md))
- [[context-engineering-ai-agents-pipeline]] ([Context Engineering](../tips/context-engineering-ai-agents-pipeline.md))
