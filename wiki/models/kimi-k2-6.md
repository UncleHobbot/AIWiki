---
title: "Kimi K2.6"
title_ru: "Kimi K2.6"
category: models
tags: [kimi, moonshot, chinese-llm, coding, open-source]
date: 2026-05-16
updated: 2026-06-14
sources:
  - https://huggingface.co/moonshotai/Kimi-K2.6
  - https://openrouter.ai/moonshotai/kimi-k2.6
---

## Summary

Kimi K2.6 is Moonshot AI's open-weight multimodal MoE model (1T/32B), released April 20, 2026. Strong coding performance with LiveCodeBench 89.6 and SWE-bench Pro 58.6. 256K context, Agent Swarm up to 300 sub-agents. Superseded for coding tasks by Kimi K2.7 Code.

## Key Ideas

- Open-weight model family from Moonshot AI built on a 1T total / 32B active parameter MoE architecture.
- Released April 20, 2026; natively multimodal and positioned as a strong coding and long-context model.
- Benchmarks: LiveCodeBench 89.6 and SWE-bench Pro 58.6 at launch, competitive with top open-weight coding models.
- 256K context window and "Agent Swarm" support for up to 300 sub-agents working in parallel on decomposed tasks.

## Details

Kimi K2.6 extends Moonshot's K2 series with larger scale and a broader modality mix. The MoE design keeps inference costs lower than a dense 1T model while preserving high output quality. It is available through Moonshot's own platform, Hugging Face, and OpenRouter, making it easy to drop into existing APIs.

In practice, K2.6 is often compared against GLM-5.1 and DeepSeek-Coder-V2 as a Chinese open-weight coding model. It was the coding flagship until Kimi K2.7 Code was released with improved SWE-bench and agentic scores. K2.6 remains useful for cost-sensitive or long-context scenarios, especially where the 256K window and agent swarm fit the workload.

## Notable Quotes

> "Kimi K2.6: a 1T/32B MoE model with native multimodality, 256K context, and Agent Swarm support." — Moonshot AI

## Related Entries

- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Comparison](llm-wiki-chinese-models-comparison.md))
- [[kimi-k2-7-code]] ([Kimi K2.7 Code](kimi-k2-7-code.md))

---
<!-- RU -->

## Краткое описание

Kimi K2.6 — открытая мультимодальная модель Moonshot AI на базе MoE 1T/32B, выпущена 20 апреля 2026 года. Сильные результаты в кодинге: LiveCodeBench 89.6, SWE-bench Pro 58.6. Контекст 256K, Agent Swarm до 300 подагентов. Для кодинга вытеснена Kimi K2.7 Code.

## Ключевые идеи

- Семейство открытых моделей Moonshot AI на архитектуре MoE: 1T параметров всего, 32B активных на выводе.
- Выпущена 20 апреля 2026 года; изначально мультимодальная и заточена под кодинг и длинный контекст.
- Бенчмарки: LiveCodeBench 89.6 и SWE-bench Pro 58.6 на момент релиза — конкурентоспособно с лучшими открытыми кодинг-моделями.
- Контекстное окно 256K и поддержка Agent Swarm до 300 подагентов, работающих параллельно над декомпозированными задачами.

## Подробнее

Kimi K2.6 развивает серию K2 от Moonshot, увеличивая масштаб и расширяя набор модальностей. Архитектура MoE снижает затраты на inference по сравнению с плотной 1T-моделью, сохраняя высокое качество вывода. Модель доступна через платформу Moonshot, Hugging Face и OpenRouter, что упрощает интеграцию в существующие API.

На практике K2.6 часто сравнивают с GLM-5.1 и DeepSeek-Coder-V2 как с китайской открытой кодинг-моделью. До выхода Kimi K2.7 Code она была флагманом для кодинга; K2.6 остаётся полезной в сценариях с ограниченным бюджетом или длинным контекстом, особенно где применимы окно 256K и Agent Swarm.

## Примечательные цитаты

> "Kimi K2.6: a 1T/32B MoE model with native multimodality, 256K context, and Agent Swarm support." — Moonshot AI

## Связанные записи

- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Comparison](llm-wiki-chinese-models-comparison.md))
- [[kimi-k2-7-code]] ([Kimi K2.7 Code](kimi-k2-7-code.md))
