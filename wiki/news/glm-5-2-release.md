---
title: "GLM-5.2 Released — Open Weights Coming, 1M Context, Free Coding Plan Access"
title_ru: "Выход GLM-5.2 — открытые веса, контекст 1M, доступ в бесплатном плане"
category: news
tags: [glm, zai, zhipu, glm-5.2, open-weights, coding-model, release]
aliases: [GLM-5.2, GLM 5.2, GLM5.2]
confidence: low
date: 2026-06-12
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/ZaiGLM/comments/1u4k2bu/to_developers_glm52_is_now_fully_open_cuttingedge/
  - https://www.reddit.com/r/ZaiGLM/comments/1u4p3zl/glm_52_is_out_open_weights_to_be_released_next/
  - https://www.reddit.com/r/ZaiGLM/comments/1u4l2ji/glm52_glm51_and_glm5turbo_with_double_usage_until/
  - https://www.reddit.com/r/ZaiGLM/comments/1u5jy0l/my_taste_on_free_glm52_with_zcode/
  - https://www.reddit.com/r/ZaiGLM/comments/1u4n4l4/glm52_community_swe_benchmark/
---

## Summary
Zhipu AI (Z.ai) released GLM-5.2, its newest coding/reasoning model, immediately available to all GLM Coding Plan tiers (Lite/Pro/Max/Team), with the API and MIT-licensed open weights promised "next week" — continuing Z.ai's commitment to open-weight frontier models.

## Key Ideas
- GLM-5.2 ships with a "truly usable" 1M token context window and Z.ai claims it maintains the lead in long-range tasks among domestic (Chinese) coding models.
- The model became available to GLM Coding Plan subscribers (Lite/Pro/Max/Team) the night of release; the public API and open-sourced weights (MIT license) are promised within a week.
- Z.ai framed the open release explicitly as a response to instability among Western frontier labs — "frontier intelligence should not belong only to a few, nor should it be withdrawn at any time by a few rules."
- To soften the transition, Z.ai extended the "double usage" promotion for GLM-5.2, GLM-5.1, and GLM-5-Turbo through the end of September.
- Early community reports describe GLM-5.2 as noticeably faster in non-thinking mode (approaching the speed of the 5.1-Turbo variant) while improving on coding correctness vs 5.1.
- A community-run benchmark (by a Chinese blogger known as "toyama nao" on Zhihu, see llm2014.github.io/llm_benchmark) was circulated showing GLM-5.2's SWE-bench-style performance alongside other frontier models — treat as informal/community data pending official numbers.

## Details
GLM-5.2 is the latest entry in Zhipu's GLM-5 coding/reasoning line, following GLM-5.1 and GLM-5-Turbo. Unlike many frontier labs that have recently restricted access for non-US users or gated capabilities, Z.ai positioned this release as a deliberate counter-move: ship the model to paying coding-plan users immediately, then open-source the weights under MIT within days. This mirrors the open-weights strategy that has made GLM models a recurring point of comparison against DeepSeek, Kimi, and Qwen in this wiki's other entries.

Community first impressions (from r/ZaiGLM) are generally positive — users report GLM-5.2 feels close to the 5.1-Turbo variant in raw speed for non-thinking tasks while being noticeably better at coding tasks than 5.1. A separate community benchmark thread compared all of Z.ai's coding models (5.2, 5.1-Turbo, 4.7, 4.5-Air) against DeepSeek V4 Pro and Flash across a Python/Streamlit + LangGraph + LanceDB research pipeline — see [[deepseek-v4-vs-opus-kimi]] and [[llm-wiki-chinese-models-comparison]] for related Chinese-model comparisons. As with all Reddit-sourced reports, these figures are unverified community data (Tier 3) pending official benchmarks once the weights and API ship.

## Related Entries
- [[product-zai-glm]] ([Z.ai GLM](../models/product-zai-glm.md))
- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models Comparison](../models/llm-wiki-chinese-models-comparison.md))
- [[gpt-vs-glm-5-1-comparison]] ([GPT vs GLM-5.1](../models/gpt-vs-glm-5-1-comparison.md))
- [[kimi-2-6-vs-glm-5-1-agent-reliability]] ([Kimi 2.6 vs GLM 5.1](../models/kimi-2-6-vs-glm-5-1-agent-reliability.md))

---
<!-- RU -->

## Краткое описание
Zhipu AI (Z.ai) выпустила GLM-5.2 — новую модель для кодинга и рассуждений, сразу доступную всем тарифам GLM Coding Plan (Lite/Pro/Max/Team), с API и открытыми весами (лицензия MIT), обещанными "на следующей неделе" — продолжая стратегию Z.ai по открытым frontier-моделям.

## Ключевые идеи
- GLM-5.2 поставляется с "реально пригодным" контекстным окном 1M токенов; Z.ai заявляет лидерство среди китайских моделей для кодинга на длинных задачах.
- Модель стала доступна подписчикам GLM Coding Plan (Lite/Pro/Max/Team) в ночь релиза; публичный API и открытые веса (MIT) обещаны в течение недели.
- Z.ai прямо назвала открытый релиз ответом на нестабильность западных frontier-лабораторий — "передовой интеллект не должен принадлежать лишь немногим и не должен отзываться по чьему-то решению".
- Чтобы смягчить переход, Z.ai продлила акцию "двойного использования" для GLM-5.2, GLM-5.1 и GLM-5-Turbo до конца сентября.
- Первые отзывы сообщества описывают GLM-5.2 как заметно быстрее в режиме без "thinking" (близко к скорости варианта 5.1-Turbo), с улучшением качества кодинга по сравнению с 5.1.
- В сообществе распространялся независимый бенчмарк (от китайского блогера "toyama nao" на Zhihu, llm2014.github.io/llm_benchmark) с результатами GLM-5.2 в духе SWE-bench рядом с другими frontier-моделями — это неофициальные данные сообщества до публикации официальных цифр.

## Подробнее
GLM-5.2 — новейшая модель в линейке GLM-5 для кодинга и рассуждений Zhipu, после GLM-5.1 и GLM-5-Turbo. В отличие от многих frontier-лабораторий, недавно ограничивших доступ для пользователей не из США или закрывших часть возможностей, Z.ai представила этот релиз как осознанный встречный шаг: модель сразу доступна платным подписчикам coding plan, а затем веса будут открыты под MIT в течение нескольких дней. Это повторяет стратегию открытых весов, которая делает модели GLM регулярным объектом сравнения с DeepSeek, Kimi и Qwen в других записях этой wiki.

Первые впечатления сообщества (r/ZaiGLM) в целом положительные — пользователи отмечают, что GLM-5.2 близка по скорости к варианту 5.1-Turbo в режиме без "thinking", при заметном улучшении качества кодинга по сравнению с 5.1. В отдельном треде сравнивались все кодинг-модели Z.ai (5.2, 5.1-Turbo, 4.7, 4.5-Air) с DeepSeek V4 Pro и Flash на пайплайне Python/Streamlit + LangGraph + LanceDB — см. [[deepseek-v4-vs-opus-kimi]] и [[llm-wiki-chinese-models-comparison]] для похожих сравнений китайских моделей. Как и все данные с Reddit, эти цифры — неподтверждённые отчёты сообщества (Tier 3) до публикации официальных бенчмарков после выхода весов и API.

## Связанные записи
- [[product-zai-glm]] ([Z.ai GLM](../models/product-zai-glm.md))
- [[llm-wiki-chinese-models-comparison]] ([Сравнение китайских LLM](../models/llm-wiki-chinese-models-comparison.md))
- [[gpt-vs-glm-5-1-comparison]] ([GPT vs GLM-5.1](../models/gpt-vs-glm-5-1-comparison.md))
- [[kimi-2-6-vs-glm-5-1-agent-reliability]] ([Kimi 2.6 vs GLM 5.1](../models/kimi-2-6-vs-glm-5-1-agent-reliability.md))
