---
title: "GLM-5.2 Nested Tool-Call Bug — Second Call Encoded Inside First Call's Arguments"
title_ru: "Баг вложенных tool-call'ов GLM-5.2 — второй вызов внутри аргументов первого"
category: news
tags: [glm-5.2, tool-calling, bug, multi-tool, zai, reliability]
aliases: [GLM 5.2 nested tool call, glm tool call in arguments]
confidence: medium
date: 2026-07-10
updated: 2026-07-11
sources:
  - https://www.reddit.com/r/ZaiGLM/comments/1ur9sha/glm_52_encoding_a_second_tool_call_inside_the/
---

## Summary
A reported GLM-5.2 tool-calling bug: when asked to emit two tool calls in one turn (e.g. `respond()` then `edit()`), the model sometimes encodes the second call *inside the arguments of the first* as raw text — producing one malformed `respond()` call whose text argument contains an unparsed `<tool_call>edit(...)</tool_call>` string, instead of two separate well-formed calls.

## Key Ideas
- **Expected output:** two separate tool calls — `respond(...)` then `edit(...)`.
- **Actual output:** one malformed `respond()` whose text argument contains the `edit()` call as raw text.
- **Reproduction:** a GLM-5.2 Telegram agent; the user asks whether this is a known issue with multiple tool calls in a single turn.
- **Significance:** multi-tool-call-in-one-turn is a common agentic pattern; a model that can't reliably separate calls forces harness-level workarounds (call splitting, retry on parse failure).
- Relates to the [[toolhound-tool-call-failure-taxonomy]] finding that small-model tool-call *syntax* is largely solved — GLM-5.2's issue is a residual format edge case in multi-call emission, not a general syntax failure.

## Details
This is a concrete tool-format edge case worth flagging for anyone building a GLM-5.2-based agent that emits multiple tool calls per turn. The harness-side mitigation is to parse aggressively for nested tool-call tags inside text arguments, or to instruct the model to emit one call per turn. It's a reminder that "tool calling works" papers over many such edge cases that only surface in production.

## Related Entries
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[toolhound-tool-call-failure-taxonomy]] ([ToolHound — Tool-Call Failure Taxonomy](../research/toolhound-tool-call-failure-taxonomy.md))
- [[zcode-zai-agentic-development-environment]] ([ZCode — Z.ai's ADE](../research/zcode-zai-agentic-development-environment.md))

---
<!-- RU -->

## Краткое описание
Заявленный баг вызова инструментов у GLM-5.2: при попытке выдать два вызова за один ход (например, `respond()`, затем `edit()`) модель иногда кодирует второй вызов *внутри аргументов первого* как сырой текст — получается один битый `respond()`, в текстовом аргументе которого лежит неразобранная строка `<tool_call>edit(...)</tool_call>`.

## Ключевые идеи
- **Ожидалось:** два отдельных вызова — `respond(...)`, затем `edit(...)`.
- **Фактически:** один битый `respond()`, в аргументе-тексте которого содержится вызов `edit()` как сырой текст.
- **Воспроизведение:** Telegram-агент на GLM-5.2.
- **Значение:** мульти-вызов за один ход — частый агентный паттерн; модель, не способная надёжно разделить вызовы, требует обходов на уровне харнеса.
- Перекликается с [[toolhound-tool-call-failure-taxonomy]]: синтаксис вызова у маленьких моделей в основном решён, но у GLM-5.2 остаются граничные случаи.

## Подробнее
Конкретный edge case формата инструментов для тех, кто строит GLM-5.2-агента с несколькими вызовами за ход. Смягчение на уровне харнеса — агрессивный парсинг вложенных тегов tool-call внутри текстовых аргументов или инструкция выдавать один вызов за ход.

## Связанные записи
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[toolhound-tool-call-failure-taxonomy]] ([ToolHound — Tool-Call Failure Taxonomy](../research/toolhound-tool-call-failure-taxonomy.md))
- [[zcode-zai-agentic-development-environment]] ([ZCode — Z.ai's ADE](../research/zcode-zai-agentic-development-environment.md))
