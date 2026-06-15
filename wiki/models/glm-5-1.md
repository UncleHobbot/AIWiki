---
title: "GLM-5.1"
title_ru: "GLM-5.1"
category: models
tags: [glm, zai, chinese-llm, coding, agentic, open-source]
date: 2026-05-16
updated: 2026-06-14
sources:
  - https://huggingface.co/zai-org/GLM-5.1
  - https://openrouter.ai/zai/glm-5.1
  - https://docs.z.ai/guides/llm/glm-5.1.md
---

## Summary

GLM-5.1 is Z.AI's (Zhipu AI) open-weight coding and agentic flagship, released April 7, 2026. 754B-parameter MoE, 203K context, MIT license. Leads Chinese models on Agent Arena and WebDev Arena, with strong long-horizon autonomous work (8+ hours). Predecessor to GLM-5.2 which adds 1M context.

## Key Ideas

- Open-weights bilingual (Chinese/English) model from Z.AI / Zhipu AI, released under the permissive MIT license.
- 754B total parameters in a Mixture-of-Experts (MoE) architecture with 203K-token context window.
- Strong agentic capabilities: scores at the top of Chinese models on Agent Arena and WebDev Arena, and can run multi-hour autonomous coding sessions.
- Available through Hugging Face, OpenRouter, and the Z.AI platform; serves as the foundation for the GLM-5 family.

## Details

GLM-5.1 targets both standalone coding and long-horizon agentic use. It inherits the GLM (General Language Modeling) pre-training and post-training recipe, with enhanced tool-use, planning, and reflection tuning for multi-turn tasks. The 203K context enables large codebases, long specs, and extended conversation histories to fit in a single prompt.

Benchmark positioning highlights Chinese-model leadership in agentic arenas, especially end-to-end web development and autonomous tool workflows. Community reports emphasize 8+ hour reliable runs for complex tasks. GLM-5.2 later extends the context window to 1M tokens and refines the same architecture; GLM-5.1 remains relevant for cost-limited deployments and as the comparison baseline.

## Notable Quotes

> "GLM-5.1: Z.AI's open-weight coding and agentic flagship with 754B MoE parameters and a 203K context." — community summary

## Related Entries

- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Comparison](llm-wiki-chinese-models-comparison.md))
- [[glm-5-2]] ([GLM-5.2](glm-5-2.md))

---
<!-- RU -->

## Краткое описание

GLM-5.1 — флагманская открытая модель Z.AI (Zhipu AI) для кодинга и агентных задач, выпущена 7 апреля 2026 года. MoE на 754B параметров, контекст 203K, лицензия MIT. Лидирует среди китайских моделей в Agent Arena и WebDev Arena, поддерживает длительную автономную работу (8+ часов). Предшественница GLM-5.2 с контекстом 1M.

## Ключевые идеи

- Открытая двуязычная (китайский/английский) модель от Z.AI / Zhipu AI под разрешительной лицензией MIT.
- 754B параметров всего в архитектуре Mixture-of-Experts (MoE) с контекстным окном 203K токенов.
- Сильные агентные способности: лидирует среди китайских моделей в Agent Arena и WebDev Arena и способна работать в автономных сессиях в несколько часов.
- Доступна через Hugging Face, OpenRouter и платформу Z.AI; служит основой семейства GLM-5.

## Подробнее

GLM-5.1 ориентирована как на самостоятельный кодинг, так и на долгосрочные агентные задачи. Модель унаследовала рецепт предобучения и дообучения GLM (General Language Modeling) с дополнительной настройкой на использование инструментов, планирование и рефлексию для многоходовых задач. Контекст 203K позволяет поместить в один prompt большие кодовые базы, длинные спецификации и длинные истории диалога.

Позиция в бенчмарках подчёркивает лидерство среди китайских моделей в агентных аренах, особенно в сквозной веб-разработке и автономных workflow с инструментами. Сообщество отмечает надёжность в сложных задачах длительностью 8+ часов. GLM-5.2 позже расширяет контекст до 1M токенов и уточняет ту же архитектуру; GLM-5.1 остаётся актуальной для ограниченных по затратам развёртываний и как базовая модель для сравнения.

## Примечательные цитаты

> "GLM-5.1: Z.AI's open-weight coding and agentic flagship with 754B MoE parameters and a 203K context." — community summary

## Связанные записи

- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Comparison](llm-wiki-chinese-models-comparison.md))
- [[glm-5-2]] ([GLM-5.2](glm-5-2.md))
