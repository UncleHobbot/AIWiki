---
title: "Kimi K2.7 Code: Moonshot's Coding-Optimized K2.6 Successor"
title_ru: "Kimi K2.7 Code: оптимизированная для кодинга преемница K2.6 от Moonshot"
category: models
tags: [kimi, moonshot, chinese-llm, coding, open-source, k2-7]
date: 2026-06-12
updated: 2026-06-14
sources:
  - https://huggingface.co/moonshotai/Kimi-K2.7-Code
  - https://platform.kimi.ai/docs/guide/kimi-k2-7-code-quickstart
  - https://openrouter.ai/models/moonshotai/kimi-k2.7-code
  - https://benchlm.ai/models/kimi-k2-7-code
---

## Summary

Released June 12, 2026, Kimi K2.7 Code is a coding-specialized variant of the Kimi K2 architecture. It keeps the same 1T/32B MoE architecture and 256K context as K2.6, but is post-trained for long-horizon coding and agentic tasks. Published benchmarks show solid gains over K2.6 but still trail GPT-5.5 and Claude Opus 4.8 on most coding tests. It is not a general-purpose model — no MMLU, GPQA, or AIME scores were published.

## Key Ideas

- **Coding-specialized only** — not a general successor to K2.6; the core K2.7 general model is separate.
- **Same architecture as K2.6** — 1T total / 32B activated MoE parameters and 256K context window.
- **Post-trained for long-horizon coding and agents** — optimized for multi-step repositories, tool use, and extended coding sessions.
- **Improves over K2.6 on all six Moonshot benchmarks** — gains across Kimi Code Bench v2, Program Bench, MLS Bench Lite, Kimi Claw 24/7, MCP Atlas, and MCP Mark Verified.
- **Still trails top Western models** — GPT-5.5 and Claude Opus 4.8 lead on most of the same tasks.
- **~30% fewer thinking tokens than K2.6** — Moonshot reports reduced inference-time reasoning cost.
- **Open weights under Modified MIT** — weights are available for download and local use with a source-code attribution clause.

## Benchmarks

| Benchmark | Kimi K2.6 | Kimi K2.7 Code | GPT-5.5 | Claude Opus 4.8 |
|---|---|---|---|---|
| Kimi Code Bench v2 | 50.9 | 62.0 | 69.0 | 67.4 |
| Program Bench | 48.3 | 53.6 | 69.1 | 63.8 |
| MLS Bench Lite | 26.7 | 35.1 | 35.5 | 42.8 |
| Kimi Claw 24/7 | 42.9 | 46.9 | 52.8 | 50.4 |
| MCP Atlas | 69.4 | 76.0 | 79.4 | 81.3 |
| MCP Mark Verified | 72.8 | 81.1 | 92.9 | 76.4 |

## Details

Kimi K2.7 Code is Moonshot's bid to keep the Kimi K2 family competitive in agentic coding. By keeping the same MoE architecture as K2.6 and applying additional post-training, Moonshot improved scores on its own coding/agent benchmarks by several points each while claiming a ~30% reduction in thinking-token usage. The model is distributed with a Modified MIT license, which adds a source-code attribution requirement.

The benchmark table above comes from Moonshot's published comparisons. On four of the six benchmarks, K2.7 Code still sits below GPT-5.5 and Claude Opus 4.8; it only clearly leads on the MCP Mark Verified task. Note that these are Moonshot-selected benchmarks and may not reflect broader SWE-bench, LiveCodeBench, or AIME performance. No MMLU, GPQA, or general-domain scores were released, reinforcing that this is a narrow, coding-oriented release.

For practitioners, K2.7 Code is most interesting as a drop-in upgrade to K2.6 for coding agents and long-context tool workflows, not as a replacement for frontier general models.

## Pricing

| Provider | Input ($/M tokens) | Output ($/M tokens) | Cache Hit Input | Context |
|----------|--------------------|--------------------|-----------------|---------|
| **Kimi Platform** | $0.95 | $4.00 | $0.19 | 262,144 |
| **OpenRouter** | $0.75 | $3.50 | — | 262,144 |

Kimi Platform cache-hit input is significantly cheaper ($0.19/M), making repeated codebase queries affordable for long agentic runs. OpenRouter offers a simpler flat rate with no cache tier. The official price is the same as K2.6 for output and cache-miss input; only cache-hit input rose slightly ($0.19 vs K2.6's $0.16).

## Related Entries

- [[glm-5-2]] ([GLM-5.2](./glm-5-2.md))
- [[kimi-k2-6]] ([Kimi K2.6](kimi-k2-6.md))
- [[moonshot-kimi]] ([Moonshot Kimi](../tools/moonshot-kimi.md))

---
<!-- RU -->

## Краткое описание

Выпущена 12 июня 2026 года, Kimi K2.7 Code — специализированный для кодинга вариант архитектуры Kimi K2. Та же архитектура MoE 1T/32B, что и у K2.6, и контекст 256K, но с post-training для долгосрочных кодинговых и агентных задач. Опубликованные бенчмарки показывают заметный рост по сравнению с K2.6, но всё ещё отстают от GPT-5.5 и Claude Opus 4.8 в большинстве кодинговых тестов. Не является универсальной моделью — оценки MMLU, GPQA, AIME не опубликованы.

## Ключевые идеи

- **Только для кодинга** — не универсальная преемница K2.6; основная модель K2.7 существует отдельно.
- **Та же архитектура, что и у K2.6** — MoE с 1T общих и 32B активных параметров, контекст 256K.
- **Post-training для долгосрочного кодинга и агентов** — оптимизирована под многошаговые репозитории, использование инструментов и длинные кодинговые сессии.
- **Превосходит K2.6 по всем шести бенчмаркам Moonshot** — рост по Kimi Code Bench v2, Program Bench, MLS Bench Lite, Kimi Claw 24/7, MCP Atlas и MCP Mark Verified.
- **Всё ещё отстаёт от топовых западных моделей** — GPT-5.5 и Claude Opus 4.8 лидируют в большинстве тех же задач.
- **Примерно на 30% меньше thinking-токенов, чем у K2.6** — Moonshot отмечает снижение стоимости inference-time reasoning.
- **Открытые веса под Modified MIT** — веса доступны для скачивания и локального использования с условием атрибуции исходного кода.

## Бенчмарки

| Бенчмарк | Kimi K2.6 | Kimi K2.7 Code | GPT-5.5 | Claude Opus 4.8 |
|---|---|---|---|---|
| Kimi Code Bench v2 | 50.9 | 62.0 | 69.0 | 67.4 |
| Program Bench | 48.3 | 53.6 | 69.1 | 63.8 |
| MLS Bench Lite | 26.7 | 35.1 | 35.5 | 42.8 |
| Kimi Claw 24/7 | 42.9 | 46.9 | 52.8 | 50.4 |
| MCP Atlas | 69.4 | 76.0 | 79.4 | 81.3 |
| MCP Mark Verified | 72.8 | 81.1 | 92.9 | 76.4 |

## Подробнее

Kimi K2.7 Code — попытка Moonshot удержать семейство Kimi K2 конкурентоспособным в агентном кодинге. Сохранив ту же архитектуру MoE, что и у K2.6, и добавив дополнительное post-training, Moonshot повысил оценки на собственных кодинговых и агентных бенчмарках на несколько пунктов в каждом, заявив при этом о снижении количества thinking-токенов примерно на 30%. Модель распространяется под лицензией Modified MIT, которая добавляет требование атрибуции исходного кода.

Таблица бенчмарков выше взята из опубликованных Moonshot сравнений. В четырёх из шести бенчмарков K2.7 Code всё ещё уступает GPT-5.5 и Claude Opus 4.8; явное лидерство наблюдается только в задаче MCP Mark Verified. Стоит помнить, что это подобранные Moonshot тесты и они могут не отражать общую производительность на SWE-bench, LiveCodeBench или AIME. MMLU, GPQA и другие общие оценки не раскрыты, что подчёркивает узкую кодинговую направленность релиза.

Для практиков K2.7 Code интересна скорее как прямая замена K2.6 в coding-агентах и длинных tool-ориентированных сценариях, а не как альтернатива универсальным frontier-моделям.

## Ценообразование

| Провайдер | Ввод ($/М токенов) | Вывод ($/М токенов) | Ввод с cache hit | Контекст |
|----------|--------------------|--------------------|-----------------|---------|
| **Kimi Platform** | $0.95 | $4.00 | $0.19 | 262,144 |
| **OpenRouter** | $0.75 | $3.50 | — | 262,144 |

Cache-hit ввод на Kimi Platform заметно дешевле ($0.19/М), что делает повторные запросы к кодовой базе доступными для длительных агентных сессий. OpenRouter предлагает более простой фlat-рейт без кэш-уровня. Официальная цена совпадает с K2.6 по выводу и вводу без попадания в кэш; только cache-hit ввод вырос незначительно ($0.19 против $0.16 у K2.6).

## Связанные записи

- [[glm-5-2]] ([GLM-5.2](./glm-5-2.md))
- [[kimi-k2-6]] ([Kimi K2.6](kimi-k2-6.md))
- [[moonshot-kimi]] ([Moonshot Kimi](../tools/moonshot-kimi.md))
