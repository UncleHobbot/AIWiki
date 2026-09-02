---
title: "Browser-Snapshot Format vs Token Cost — 35 Agent Trials"
title_ru: "Формат снимка браузера против стоимости токенов — 35 испытаний агента"
category: research
tags: [browser-agent, token-cost, context-engineering, opera-compact, benchmarks]
aliases: [opera-compact, browser snapshot token cost]
confidence: medium
updated: 2026-07-01
sources:
  - https://www.reddit.com/r/AI_Agents/comments/1ukm69c/ran_35_agent_trials_across_4_browsersnapshot/
---

## Summary
A controlled experiment (35 trials) from the Opera browser-tooling team found that the format used to represent a browser page to an agent has no effect on task pass rate but a ~5× effect on input-token cost. A compressed "opera-compact" format cut average input tokens from 179k to 36k per task with identical 100% pass rate.

## Key Ideas
- **Setup:** 7 browser tasks (adapted from AXI's bench-browser suite), gpt-5.5 medium reasoning, 5 runs per condition = 35 trials.
- **Pass rate identical across all four formats (100%)** — the format only changes what the agent pays in tokens, not whether it succeeds.
- Results table (Pass / Avg input tokens / Tool calls):
  - Unprocessed MCP (chrome-devtools-mcp): 100% / 179.2k / 2.1
  - AXI reference CLI: 100% / 102.2k / 1.5
  - Opera raw output (compression off): 100% / 107.5k / 1.6
  - Opera compressed (opera-compact): 100% / 36.3k / 1.4
- Core insight: when agents drive browsers, most context goes to re-reading page structure every step; cutting structurally redundant content is where the savings live.

## Details
The study isolates a variable many browser-agent benchmarks ignore: the representation cost of the page itself. Because an agent re-fetches the page snapshot at each step, verbose representations compound across a session. The compressed format removes elements the agent doesn't act on while preserving what the task needs. Note: authors are on the Opera team building browser tooling, so treat vendor positioning with appropriate skepticism — but the methodology (fixed task set, fixed model, multiple runs) is sound.

## Related Entries
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[headroom-token-saver]] ([Headroom Token Saver](../tools/headroom-token-saver.md))
- [[context-warp-drive]] ([Context Warp Drive](../tools/context-warp-drive.md))

---
- [[anywebmcp-webmcp-any-site]] ([AnyWebMCP](../tools/anywebmcp-webmcp-any-site.md))
<!-- RU -->

## Краткое описание
Контролируемый эксперимент (35 испытаний) от команды браузерных инструментов Opera показал, что формат представления веб-страницы агенту не влияет на процент успеха задания, но даёт ~5× разницу в стоимости входных токенов. Сжатый формат «opera-compact» сократил среднее число входных токенов с 179k до 36k при том же 100% успехе.

## Ключевые идеи
- **Условия:** 7 браузерных задач (адаптировано из bench-browser от AXI), gpt-5.5 medium reasoning, по 5 запусков на условие = 35 испытаний.
- **Процент успеха одинаков (100%)** во всех четырёх форматах — формат меняет только плату в токенах.
- Таблица (Успех / Входные токены / Вызовы инструментов):
  - Необработанный MCP (chrome-devtools-mcp): 100% / 179.2k / 2.1
  - AXI reference CLI: 100% / 102.2k / 1.5
  - Сырой вывод Opera (без сжатия): 100% / 107.5k / 1.6
  - Сжатый (opera-compact): 100% / 36.3k / 1.4
- Главный вывод: большую часть контекста агент тратит на перечитывание структуры страницы на каждом шаге; устранение структурно избыточного contenта даёт экономию.

## Подробнее
Исследование изолирует переменную, которую игнорируют многие бенчмарки браузерных агентов: стоимость представления самой страницы. Поскольку агент перечитывает снимок на каждом шаге, избыточные представления накапливаются. Сжатый формат удаляет элементы, на которые агент не действует, сохраняя нужное для задачи. Важно: авторы — сотрудники Opera, поэтому вендорскую позицию стоит оценивать критически, но методика корректна.

## Связанные записи
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[headroom-token-saver]] ([Headroom Token Saver](../tools/headroom-token-saver.md))
- [[context-warp-drive]] ([Context Warp Drive](../tools/context-warp-drive.md))
