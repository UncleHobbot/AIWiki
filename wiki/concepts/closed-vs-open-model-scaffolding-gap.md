---
title: "Are Closed Models Better, or Just More Scaffolded? (Open vs Closed Gap Debate)"
title_ru: "Закрытые модели лучше, или просто сильнее обёрнуты? (Дебаты open vs closed)"
category: concepts
tags: [models, benchmarks, scaffolding, open-vs-closed, RAG, context-engineering]
aliases: [closed vs open model gap, scaffolding gap, claude vs glm scaffolding]
confidence: medium
updated: 2026-07-01
sources:
  - https://www.reddit.com/r/LocalLLaMA/comments/1ukp2bu/the_gap_between_closed_and_open_models_might_be/
---

## Summary
A widely-discussed community argument: when Claude outperforms an open model like GLM-5.2 on a benchmark, the gap may not reflect a better *model* but a more elaborate *product* wrapped around model inference. Because closed providers redact reasoning traces and hide the full conversation, we may be benchmarking "model inference" against "model + RAG + hidden tools + system prompts," which is apples-to-oranges.

## Key Ideas
- **The claim:** benchmarks compare open-model inference against the entire closed product surface, not raw model inference.
- Things closed providers could be doing behind the API (invisible to the benchmark):
  - RAG / knowledge injection (e.g., for software documentation).
  - Prompt preprocessing.
  - Context-dependent hidden system prompts.
  - Hidden internal tool calls.
  - "Clown-car MoE" / shelling out to specialized expert models.
- All of these can dramatically improve measurable performance while being served as a single model called "Claude."
- **Implication:** the true model-architecture gap between open and closed may be much smaller than headline benchmarks suggest; some gap is a *scaffolding* gap.

## Details
This is a reframing of what benchmarks actually measure. A frontier API endpoint is a black box; the only honest comparison is end-to-end product vs end-to-end product, or raw model vs raw model. Since open weights expose only the raw model while closed APIs expose the whole product, naive benchmarking systematically overstates the model-level lead of closed providers. The practical takeaway for open-model users: closing the observed gap may be more about building better scaffolding (retrieval, tools, routing) than waiting for better weights.

## Notable Quotes
> "The benchmarks compare model inference on GLM with the whole Claude product, and we don't know what that product does behind the scenes." — r/LocalLLaMA

## Related Entries
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[gpt-vs-glm-5-1-comparison]] ([GPT vs GLM-5.1 Comparison](../models/gpt-vs-glm-5-1-comparison.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[open-source-models-vs-opus-copilot-benchmark]] ([Open Source vs Opus/Copilot Benchmark](../models/open-source-models-vs-opus-copilot-benchmark.md))

---
<!-- RU -->

## Краткое описание
Широко обсуждаемый_community_-аргумент: когда Claude обгоняет открытую модель вроде GLM-5.2 на бенчмарке, разрыв может отражать не лучшую *модель*, а более elaborate *продукт*, обёрнутый вокруг model inference. Поскольку закрытые провайдеры редктируют reasoning traces и скрывают полную беседу, мы можем сравнивать «инференс модели» с «модель + RAG + скрытые инструменты + системные промпты» — яблоки с апельсинами.

## Ключевые идеи
- **Тезис:** бенчмарки сравнивают инференс открытой модели со всей продуктовой поверхностью закрытой, а не с raw model inference.
- Что закрытые провайдеры могут делать за API (невидимо для бенчмарка):
  - RAG / инъекция знаний (например, документация по ПО).
  - Препроцессинг промпта.
  - Контекстно-зависимые скрытые системные промпты.
  - Скрытые внутренние вызовы инструментов.
  - «Clown-car MoE» / делегирование специализированным экспертным моделям.
- Всё это резко улучшает измеримую производительность, подаваясь как одна модель «Claude».
- **Следствие:** истинный разрыв по архитектуре модели между open и closed может быть сильно меньше, чем в заголовках бенчмарков; часть разрыва — это разрыв *в scaffolding*.

## Подробнее
Это переформулировка того, что реально измеряют бенчмарки. Frontier API-эндпоинт — чёрный ящик; честное сравнение — либо «продукт против продукта», либо «сырая модель против сырой модели». Поскольку открытые веса дают только raw model, а закрытые API — весь продукт, наивное бенчмаркинг систематически завышает модельное превосходство закрытых провайдеров. Практический вывод для пользователей открытых моделей: сократить наблюдаемый разрыв чаще можно через лучший scaffolding (retrieval, инструменты, роутинг), а не ожидая лучших весов.

## Примечательные цитаты
> «Бенчмарки сравнивают model inference на GLM со всем продуктом Claude, а мы не знаем, что этот продукт делает за кулисами.» — r/LocalLLaMA

## Связанные записи
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[gpt-vs-glm-5-1-comparison]] ([GPT vs GLM-5.1 Comparison](../models/gpt-vs-glm-5-1-comparison.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[open-source-models-vs-opus-copilot-benchmark]] ([Open Source vs Opus/Copilot Benchmark](../models/open-source-models-vs-opus-copilot-benchmark.md))
