---
title: "DeepSeek V4 Pro vs Claude Opus 4.7 vs Kimi K2.6 Benchmark"
title_ru: "Сравнение DeepSeek V4 Pro, Claude Opus 4.7 и Kimi K2.6"
category: models
tags: [deepseek, claude-opus, kimi, benchmarks, coding-agents]
updated: 2026-05-15
sources:
  - https://www.reddit.com/r/kimi/comments/1tcrrwu/tested_deepseek_v4_pro_and_flash_against_claude/
  - https://blog.kilo.ai/p/we-tested-deepseek-v4-pro-and-flash
---

## Summary

Kilo CLI tested DeepSeek V4 Pro and Flash against Claude Opus 4.7 and Kimi K2.6 on a complex workflow orchestration backend. DeepSeek V4 Pro scored 77/100 ($2.25), landing between Opus 4.7 (91) and Kimi K2.6 (68).

## Key Ideas
- Test: 20-endpoint workflow orchestration backend with persistent state, lease management, retries, event streaming
- DeepSeek V4 Pro: 77/100, $2.25 — passed its own test suite but TypeScript build failed
- DeepSeek V4 Flash: 60/100, $0.02 — a new price category, but setup script failed and entry endpoint was mounted wrong
- Claude Opus 4.7: 91/100 — had only one reproducible bug
- Kimi K2.6: 68/100 — missed live event streaming entirely
- Recovery under contention remains the hardest problem for all models
- V4 Pro enforces lease on heartbeats but not on completions
- V4 Flash tool calling held up surprisingly well despite code quality gaps

## Details

The test used a rigorous infrastructure spec rather than typical coding benchmarks. A 7-category rubric was applied uniformly. All models ran in thinking mode in Kilo CLI.

Key finding: the gap in surface coverage between open-weight and frontier proprietary models is narrow. The gap in correctness within hard-coded paths — lease recovery, cross-run scheduling, expired-lease rejection — is still present but narrowing.

DeepSeek V4 Flash at $0.02 for the entire run represents a new price tier where running the same task 3-4 times to compare attempts is still cheaper than a single Kimi K2.6 run.

## Related Entries
- [[orthrus-qwen3-acceleration]]
- [[gpt-vs-glm-5-1-comparison]]
- [[llm-wiki-chinese-models-comparison]]

---
<!-- RU -->

## Краткое описание

Kilo CLI протестировала DeepSeek V4 Pro и Flash против Claude Opus 4.7 и Kimi K2.6 на сложном бэкенде оркестрации рабочих процессов. DeepSeek V4 Pro набрал 77/100 ($2.25), заняв место между Opus 4.7 (91) и Kimi K2.6 (68).

## Ключевые идеи
- Тест: бэкенд оркестрации с 20 эндпоинтами, персистентным состоянием, управлением арендой, повторами и потоковой передачей событий
- DeepSeek V4 Pro: 77/100, $2.25 — прошёл собственные тесты, но сборка TypeScript завершилась ошибкой
- DeepSeek V4 Flash: 60/100, $0.02 — новая ценовая категория, но скрипт установки и маршрутизация сломаны
- Claude Opus 4.7: 91/100 — только один воспроизводимый баг
- Восстановление при конкуренции остаётся самой сложной задачей для всех моделей
- V4 Flash показал неожиданно хорошую надёжность вызова инструментов

## Подробнее

Тест использовал строгую инфраструктурную спецификацию вместо типичных кодинговых бенчмарков. Основной вывод: разрыв в покрытии между моделями с открытыми весами и проприетарными моделями сужается. Разрыв в корректности внутри сложных путей — восстановление аренды, межпотоковое планирование — всё ещё существует, но сокращается.

DeepSeek V4 Flash за $0.02 за весь запуск представляет новую ценовую категорию, где троекратное выполнение задачи всё равно дешевле одного запуска Kimi K2.6.

## Связанные записи
- [[orthrus-qwen3-acceleration]]
- [[gpt-vs-glm-5-1-comparison]]
- [[llm-wiki-chinese-models-comparison]]
