---
title: "CodeBoarding: Live Architecture Diagrams That Track Agent Changes"
title_ru: "CodeBoarding: живые архитектурные диаграммы, отслеживающие изменения агента"
category: tools
tags: [opencode, architecture, visualization, static-analysis, code-review, agentic-coding]
aliases: [CodeBoarding/CodeBoarding]
confidence: low
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/opencode/comments/1u4ugb2/visualizing_the_impact_of_opencodes_plan_before/
  - https://github.com/CodeBoarding/CodeBoarding
---

## Summary
CodeBoarding is an open-source engine that ingests a codebase and produces diagram representations of it using static analysis (control-flow graphs) plus a slim LLM layer, with dynamic highlighting that shows in near real time which components an agent (e.g. OpenCode) has changed — and a newer feature that previews which components a planned change will impact *before* it executes.

## Key Ideas
- Based on static analysis (control-flow graphs) with a "slim layer of LLMs" for accuracy, allowing near-real-time, accurate diagrams.
- Originally built so developers could explore unfamiliar codebases visually.
- Added dynamic highlighting: when an agent (OpenCode) changes a file, the corresponding diagram component updates live, letting you watch the agent work on the architecture map rather than reading raw diffs.
- New direction (in progress at time of posting): visualize the *impact of a plan before executing it* — shows which components will be affected, whether new components are expected, and the severity/size of the change — to catch agent misinterpretations before paying for a wrong execution.
- Repo: https://github.com/CodeBoarding/CodeBoarding

## Details
The author frames this as a response to a recurring pain point with agentic coding: agents propose plans, and the only way to know whether a plan is "right" is to execute it and then diff the result — which costs time and tokens if the agent misread the task. By generating an architecture diagram from static analysis and then projecting a plan's impact onto that diagram *before* execution, CodeBoarding aims to give a fast, visual sanity check — does the planned blast radius match what the developer expects, and are there unexpected new components?

This is conceptually related to other "observability for agentic coding" tools surfacing in the OpenCode/Claude Code communities around the same period (e.g. a separate VS Code extension shared in r/ClaudeCode that draws a live architecture map tied to real files, updated as the agent edits). Community source (Tier 3 — Reddit self-promotion); the plan-impact-preview feature was described as still in development.

## Related Entries
- [[opencode-background-agents]] ([opencode-background-agents](../tools/opencode-background-agents.md))

---
<!-- RU -->

## Краткое описание
CodeBoarding — open-source движок, который анализирует кодовую базу и строит диаграммные представления с помощью статического анализа (графы потока управления) и тонкого слоя LLM, с динамической подсветкой, показывающей почти в реальном времени, какие компоненты изменил агент (например, OpenCode) — а также новая функция предпросмотра того, какие компоненты затронет запланированное изменение *до* его выполнения.

## Ключевые идеи
- Основан на статическом анализе (графы потока управления) с "тонким слоем LLM" для точности, что позволяет строить точные диаграммы почти в реальном времени.
- Изначально создан, чтобы разработчики могли визуально исследовать незнакомые кодовые базы.
- Добавлена динамическая подсветка: когда агент (OpenCode) меняет файл, соответствующий компонент диаграммы обновляется в реальном времени — можно наблюдать за работой агента на архитектурной карте, а не читать необработанные diff.
- Новое направление (в разработке на момент публикации): визуализация *влияния плана до его выполнения* — показывает, какие компоненты будут затронуты, появятся ли новые компоненты и какая у изменения серьёзность/размер — чтобы выявить неверную интерпретацию задачи агентом до затрат на выполнение неправильного плана.
- Репозиторий: https://github.com/CodeBoarding/CodeBoarding

## Подробнее
Автор описывает это как ответ на распространённую проблему agentic coding: агенты предлагают планы, и единственный способ узнать, "правильный" ли план — выполнить его и затем сравнить результат, что стоит времени и токенов, если агент неверно понял задачу. Генерируя архитектурную диаграмму на основе статического анализа и затем проецируя влияние плана на эту диаграмму *до* выполнения, CodeBoarding стремится дать быструю визуальную проверку — соответствует ли запланированный "радиус поражения" ожиданиям разработчика, и не появляются ли неожиданные новые компоненты.

Это концептуально связано с другими инструментами "observability для agentic coding", появляющимися в сообществах OpenCode/Claude Code в тот же период (например, отдельное расширение VS Code, представленное в r/ClaudeCode, которое строит живую архитектурную карту, привязанную к реальным файлам и обновляемую по мере правок агента). Источник community (tier 3 — самопродвижение на Reddit); функция предпросмотра влияния плана на момент публикации была описана как находящаяся в разработке.

## Связанные записи
- [[opencode-background-agents]] ([opencode-background-agents](../tools/opencode-background-agents.md))
