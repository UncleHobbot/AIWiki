---
title: "How to Choose an LLM for Your AI Agent: API, Self-Host, or Hybrid"
title_ru: "Как выбрать LLM для AI-агента и не сжечь бюджет: API, self-host, гибрид"
category: tips
tags: [llm-selection, api-vs-self-host, model-routing, production, cost-optimization, open-source, enterprise]
date: 2026-05-16
updated: 2026-05-17
transcript: unavailable
sources:
  - https://www.youtube.com/watch?v=n1TMMZKYMpo
---

## Summary

Engineering framework for choosing between cloud API (Anthropic, OpenAI, Google), self-hosted open-source models (Llama, Qwen, Mistral, DeepSeek), and hybrid architectures with a router. No ideology ("API = slavery" or "open source = serious") — only engineering criteria: latency, data privacy, cost accounting, benchmark relevance, and when to add a router with fallback.

## Key Ideas
- **"One model for everything" is dead:** With millions of models on HuggingFace and providers releasing weekly, single-model strategies don't work in production
- **API vs self-host decision tree:** Engineering criteria only — latency requirements, data sensitivity, cost per token at your scale, team expertise
- **True cost of open source:** "Free" models aren't free when you factor in GPU provisioning, ops, monitoring, failure recovery, and the team to manage it all
- **Benchmarks are domain-blind:** MMLU, HumanEval, SWE-Bench scores are nearly meaningless for your specific domain. Build your own eval set
- **Router + fallback architecture:** When it makes sense to add a model router — typically when you have >2 distinct query types with different complexity/cost profiles
- **Hybrid as the mature choice:** Start with API, add self-host for high-volume/low-complexity tasks, route dynamically

## Video Notes

| Timestamp | Key Point |
|---|---|
| [0:00] | The model selection problem in 2026 |
| [~3:00] | API vs self-host: engineering criteria |
| [~6:00] | True cost of open-source models |
| [~9:00] | Why benchmarks don't help for your domain |
| [~12:00] | Router + fallback architecture |
| [~15:00] | Hybrid: when and how |

## Related Entries
- [[llm-wiki-chinese-models-comparison]]
- [[expensive-model-not-smart-agent]]
- [[dynamic-compute-budget-local-llm]]

---
<!-- RU -->

## Краткое описание

Инженерный фреймворк выбора между облачным API (Anthropic, OpenAI, Google), self-hosted open-source (Llama, Qwen, Mistral, DeepSeek) и гибридной архитектурой с роутером. Без идеологии — только инженерные критерии: задержка, конфиденциальность, учёт затрат, релевантность бенчмарков.

## Ключевые идеи
- **«Одна модель на всё» мертва:** Миллионы моделей на HuggingFace, релизы каждую неделю — одномодельная стратегия не работает
- **Дерево решений API vs self-host:** Только инженерные критерии — задержка, чувствительность данных, стоимость на токен
- **Истинная стоимость open source:** «Бесплатные» модели не бесплатные — GPU, ops, мониторинг, команда
- **Бенчмарки слепы к домену:** MMLU, HumanEval, SWE-Bench почти ничего не говорят о вашем домене
- **Архитектура роутер + fallback:** Когда добавлять роутер моделей — обычно при >2 типов запросов
- **Гибрид — зрелый выбор:** Начать с API, добавить self-host для высоконагруженных простых задач

## Заметки по видео

| Таймкод | Ключевой момент |
|---|---|
| [~3:00] | API vs self-host: инженерные критерии |
| [~6:00] | Истинная стоимость open-source моделей |
| [~9:00] | Почему бенчмарки не помогают |
| [~12:00] | Архитектура роутер + fallback |
| [~15:00] | Гибрид: когда и как |

## Связанные записи
- [[llm-wiki-chinese-models-comparison]]
- [[expensive-model-not-smart-agent]]
- [[dynamic-compute-budget-local-llm]]
