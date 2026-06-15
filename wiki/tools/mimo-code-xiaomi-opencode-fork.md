---
title: "MiMo-Code — Xiaomi's OpenCode Fork"
title_ru: "MiMo-Code — форк OpenCode от Xiaomi"
category: tools
tags: [opencode, xiaomi, mimo, fork, agentic-coding]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://github.com/XiaomiMiMo/MiMo-Code
  - https://www.reddit.com/r/opencodeCLI/comments/1u2ve5e/xiaomis_oc_fork_has_some_features_that_i_really/
---

## Summary

Xiaomi released MiMo-Code, a fork of OpenCode optimized for their MiMo models, featuring non-blocking agent delegation and inline build-mode switching — built to close 5K open GitHub issues on their own repo.

## Key Ideas

- Spawns sub-agents and continues the session in parallel (non-blocking delegation)
- Asks user to switch to Build mode inline rather than stopping the session
- Option to turn off questions entirely for fully autonomous operation
- Still rough and buggy — agent delegation doesn't always work reliably
- Demonstrates corporate investment in the OpenCode ecosystem; Xiaomi needs it to manage their own issue backlog

## Details

MiMo-Code is Xiaomi's answer to a practical problem: they have over 5,000 open GitHub issues on the MiMo-Code repository and need an agentic coding tool that can work through them efficiently. Rather than use vanilla OpenCode, they forked it and added features tuned to their workflow.

The most interesting feature is non-blocking agent delegation. In standard OpenCode, when you spawn a sub-agent the main session blocks until it completes. MiMo-Code lets the primary session continue working while a delegated agent handles a subtask in the background. This is closer to how human engineers actually delegate — you hand off a task and keep working.

The inline Build mode prompt is a UX improvement: instead of the agent stopping and asking "should I switch to Build mode?", it presents the option inline and lets the user confirm without breaking flow. The option to disable questions entirely enables a "fire and forget" workflow for well-understood tasks.

The fork is still early-stage. Community reports note that agent delegation sometimes fails silently, and the tight coupling with MiMo models means some features degrade with other providers.

## Related Entries

- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[amore-opencode-research-plugin]] ([amore](../tools/amore-opencode-research-plugin.md))
- [[opencoderag-rag-plugin]] ([OpenCodeRAG](../tools/opencoderag-rag-plugin.md))
- [[mimo-v25-pro-dflash-1000tps]] ([Xiaomi Serves MiMo V2.5 Pro at 1000-3000 tok/s with DFlash + Persistent Kernel](../news/mimo-v25-pro-dflash-1000tps.md))

---
<!-- RU -->

## Краткое описание

Xiaomi выпустила MiMo-Code — форк OpenCode, оптимизированный для моделей MiMo, с неблокирующей делегацией агентов и встроенным переключением в режим сборки. Создан для закрытия 5K открытых issues на собственном репозитории.

## Ключевые идеи

- Запускает подагенты и продолжает сессию параллельно (неблокирующая делегация)
- Предлагает пользователю переключиться в режим Build inline, не останавливая сессию
- Опция полного отключения вопросов для полностью автономной работы
- Пока сырой и нестабильный — делегация агентов не всегда работает надёжно
- Демонстрирует корпоративные инвестиции в экосистему OpenCode; Xiaomi нужен инструмент для управления собственным бэклогом issues

## Подробнее

MiMo-Code — ответ Xiaomi на практическую проблему: более 5000 открытых GitHub issues в репозитории MiMo-Code, и нужен агентный инструмент кодирования, способный эффективно с ними работать. Вместо использования стандартного OpenCode они создали форк и добавили функции, настроенные под их рабочий процесс.

Наиболее интересная функция — неблокирующая делегация агентов. В стандартном OpenCode при запуске подагента основная сессия блокируется до завершения. MiMo-Code позволяет основной сессии продолжать работу, пока делегированный агент обрабатывает подзадачу в фоновом режиме. Это ближе к тому, как инженеры делегируют задачи в реальности — передаёшь задачу и продолжаешь работать.

Inline-запрос режима Build — улучшение UX: вместо остановки и вопроса «переключиться в режим Build?» агент представляет опцию встроенно, позволяя пользователю подтвердить без прерывания потока. Опция отключения вопросов включает режим «запусти и забудь» для понятных задач.

Форк пока на ранней стадии. Пользователи сообщают, что делегация агентов иногда завершается молча, а тесная связка с моделями MiMo означает, что некоторые функции ухудшаются с другими провайдерами.

## Связанные записи

- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[amore-opencode-research-plugin]] ([amore](../tools/amore-opencode-research-plugin.md))
- [[opencoderag-rag-plugin]] ([OpenCodeRAG](../tools/opencoderag-rag-plugin.md))
- [[mimo-v25-pro-dflash-1000tps]] ([Xiaomi обслуживает MiMo V2.5 Pro со скоростью 1000-3000 ток/с с DFlash и Persistent Kernel](../news/mimo-v25-pro-dflash-1000tps.md))
