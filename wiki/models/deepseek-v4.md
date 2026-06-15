---
title: "DeepSeek V4"
title_ru: "DeepSeek V4"
category: models
tags: [deepseek, v4, chinese-llm, moe, open-source]
aliases: [DeepSeek V4, DeepSeek-V4]
confidence: medium
updated: 2026-06-14
sources:
  - https://www.deepseek.com/
  - https://huggingface.co/deepseek-ai
---

## Summary

DeepSeek V4 is the flagship large language model from DeepSeek. It is a Mixture-of-Experts (MoE) architecture with ~1.6T total parameters and ~49B active parameters per token, a 1 million-token context window, and weights released under the permissive MIT license.

## Key Ideas

- Mixture-of-Experts architecture: ~1.6T total parameters with ~49B activated per token, balancing frontier quality with manageable inference cost.
- 1 million-token context window for long-document reasoning and large-codebase tasks.
- Released as open weights under the MIT license — one of the largest openly available frontier-class models.
- Offered in tiers (Flash for speed/low-latency, Pro for deeper reasoning) to cover both cost-sensitive and high-quality use cases.
- Strong coding benchmark results (e.g., LiveCodeBench ~93.5), placing it competitively against Western frontier models.

## Details

DeepSeek V4 continues DeepSeek's strategy of pushing open-weight frontier models with efficient MoE routing. By activating only ~49B of ~1.6T parameters per token, it aims to deliver frontier-level reasoning and coding at a fraction of the dense-equivalent compute cost. The 1M context window puts it in the top tier for long-context work alongside competitors like GLM-5.2 and Kimi.

The open MIT-licensed weights make DeepSeek V4 a popular base for community fine-tunes and self-hosted deployments, and a benchmark for Chinese domestic hardware — a Huawei-led team demonstrated post-training V4 on 1,000 Ascend 910C chips. The tiered Flash/Pro serving options let developers trade latency for depth depending on the task.

## Related Entries

- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models Comparison](llm-wiki-chinese-models-comparison.md))
- [[huawei-deepseek-v4-ascend-training]] ([Huawei-Led DeepSeek V4 Training on Ascend](../news/huawei-deepseek-v4-ascend-training.md))

---
<!-- RU -->

## Краткое описание

DeepSeek V4 — флагманская большая языковая модель от DeepSeek. Это архитектура Mixture-of-Experts (MoE) с ~1,6 трлн суммарных параметров и ~49B активных параметров на токен, контекстным окном 1 миллион токенов и весами, выпущенными под пермиссивной лицензией MIT.

## Ключевые идеи

- Архитектура Mixture-of-Experts: ~1,6 трлн суммарных параметров с ~49B активируемых на токен, что балансирует frontier-качество и управляемую стоимость инференса.
- Контекстное окно 1 миллион токенов для рассуждений над длинными документами и задач в крупных кодовых базах.
- Выпущена с открытыми весами под лицензией MIT — одна из крупнейших открыто доступных моделей frontier-класса.
- Предлагается уровнями (Flash для скорости/низкой задержки, Pro для более глубокого reasoning), покрывая как чувствительные к стоимости, так и требующие высокого качества сценарии.
- Сильные результаты на кодинговых бенчмарках (например, LiveCodeBench ~93,5), что ставит её в конкурентное положение против западных frontier-моделей.

## Подробнее

DeepSeek V4 продолжает стратегию DeepSeek по продвижению моделей frontier-класса с открытыми весами и эффективной MoE-маршрутизацией. Активируя лишь ~49B из ~1,6 трлн параметров на токен, модель стремится обеспечить reasoning и кодинг уровня frontier при доле вычислительных затрат dense-эквивалента. Контекстное окно 1M ставит её в топовый эшелон по длинному контексту наряду с конкурентами вроде GLM-5.2 и Kimi.

Открытые веса под лицензией MIT делают DeepSeek V4 популярной базой для community-файн-тюнов и self-hosted-развёртываний, а также бенчмарком для китайского отечественного оборудования — команда под руководством Huawei продемонстрировала пост-обучение V4 на 1000 чипах Ascend 910C. Уровневые варианты обслуживания Flash/Pro позволяют разработчикам балансировать задержку и глубину в зависимости от задачи.

## Связанные записи

- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models Comparison](llm-wiki-chinese-models-comparison.md))
- [[huawei-deepseek-v4-ascend-training]] ([Huawei-Led DeepSeek V4 Training on Ascend](../news/huawei-deepseek-v4-ascend-training.md))
