---
title: "Self-Improving GUI Agent (MIT)"
title_ru: "Самоулучшающийся GUI-агент (MIT)"
category: agents
tags: [gui-agent, self-improvement, yolo, ocr, windows, open-source, mit]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://www.reddit.com/r/AI_Agents/comments/1u2y8rh/i_built_a_selfimproving_gui_agent_that_learns/
---

## Summary
Open-source (MIT license) GUI agent that automates Windows desktop tasks by watching the screen and executing clicks/keystrokes. Combines cheap local models (YOLO for element detection, OCR for text) with LLM calls only for decision-making, dramatically reducing cost vs. pure vision-model approaches.

## Key Ideas
- Uses YOLO for UI element detection + OCR for text extraction; LLM is only called for high-level decisions
- Self-improvement loop: after each task completion, reviews what happened and extracts reusable skills into persistent memory
- Gets better the more you use it — learned skills compound over time
- Controls any Windows desktop application without API access
- Most clicks/interactions never touch the expensive model, yielding significant cost savings over $200/month vision-model alternatives

## Details
The agent takes a hybrid approach to GUI automation. Instead of sending every screenshot to a costly vision LLM, it runs YOLO locally to detect buttons, inputs, and other UI elements, then uses OCR to read text on screen. The LLM is only invoked when a decision needs to be made about what to do next. This architecture keeps per-interaction costs low while maintaining the flexibility of LLM-driven automation.

The self-improvement mechanism is the key differentiator. After completing a task, the agent reviews the sequence of actions and outcomes, then extracts generalized, reusable skills into a persistent memory store. Over time, the agent builds a library of competencies that make future tasks faster and more reliable — a form of experiential learning that compound with usage.

## Related Entries
- compound tools ([Compound Tools](../tips/compound-tools.md))
- agent memory patterns ([Agent Memory Patterns](../concepts/agent-memory-patterns.md))

---
<!-- RU -->

## Краткое описание
GUI-агент с открытым исходным кодом (лицензия MIT), автоматизирующий задачи на рабочем столе Windows через наблюдение за экраном и выполнение кликов/нажатий клавиш. Сочетает дешёвые локальные модели (YOLO для обнаружения элементов, OCR для текста) с вызовами LLM только для принятия решений, существенно снижая стоимость по сравнению с подходами на чистых vision-моделях.

## Ключевые идеи
- Использует YOLO для обнаружения UI-элементов + OCR для извлечения текста; LLM вызывается только для принятия решений высокого уровня
- Цикл самоулучшения: после выполнения задачи анализирует произошедшее и извлекает переиспользуемые навыки в постоянную память
- Работает тем лучше, чем чаще используется — накопленные навыки усиливаются со временем
- Управляет любым приложением на рабочем столе Windows без доступа к API
- Большинство кликов и взаимодействий не затрагивают дорогую модель, что даёт значительную экономию по сравнению с vision-моделями за $200/месяц

## Подробнее
Агент использует гибридный подход к автоматизации GUI. Вместо отправки каждого скриншота дорогой vision LLM, он запускает YOLO локально для обнаружения кнопок, полей ввода и других UI-элементов, а затем применяет OCR для чтения текста на экране. LLM привлекается только тогда, когда нужно принять решение о следующем действии. Такая архитектура удерживает стоимость каждого взаимодействия на низком уровне, сохраняя при этом гибкость автоматизации на базе LLM.

Механизм самоулучшения — ключевое отличие. После завершения задачи агент анализирует последовательность действий и результатов, затем извлекает обобщённые, переиспользуемые навыки в постоянное хранилище памяти. Со временем агент формирует библиотеку компетенций, делающую будущие задачи быстрее и надёжнее — форма обучения на опыте, которая накапливается с использованием.

## Связанные записи
- compound tools ([Compound Tools](../tips/compound-tools.md))
- agent memory patterns ([Agent Memory Patterns](../concepts/agent-memory-patterns.md))
