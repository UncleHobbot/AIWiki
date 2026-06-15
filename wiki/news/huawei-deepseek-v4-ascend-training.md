---
title: "Huawei Post-Trains DeepSeek V4 on Domestic Chips"
title_ru: "Huawei дообучила DeepSeek V4 на отечественных чипах"
category: news
tags: [deepseek, huawei, ascend, china, ai-chips, training, sanctions]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://www.reddit.com/r/DeepSeek/comments/1u2xnd3/huaweiled_team_claims_it_posttrained_deepseeks/
---

## Summary

A Huawei-led team claims to have successfully post-trained DeepSeek's 1.6-trillion-parameter V4 model using 1,000 Ascend 910C chips, demonstrating that Chinese domestic AI hardware can handle frontier-scale model work. This has significant implications for the effectiveness of US export controls on NVIDIA hardware.

## Key Ideas

- 1,000 Ascend 910C chips used for post-training of DeepSeek V4 (1.6T parameters)
- Post-training (fine-tuning and alignment), not pretraining from scratch — a lower but still demanding computational task
- Demonstrates viability of Huawei's domestic AI chips for frontier-scale model work
- Directly challenges the effectiveness of US chip export restrictions targeting China
- DeepSeek V4 is one of the largest open-weight models, making this a high-profile demonstration
- Raises questions about whether export controls accelerate domestic chip development rather than slow AI progress

## Details

The announcement from the Huawei-led team represents a significant milestone in China's push for AI chip self-sufficiency. While post-training is computationally less demanding than pretraining a model from scratch, fine-tuning and aligning a 1.6-trillion-parameter model still requires substantial distributed computing infrastructure and chip-level performance.

The Ascend 910C is Huawei's flagship AI accelerator, designed as a domestic alternative to NVIDIA's A100/H100 series. US export controls have restricted NVIDIA's ability to sell high-end AI chips to Chinese customers, creating a market opening for domestic alternatives. This demonstration suggests that the gap between domestic and NVIDIA hardware may be narrowing faster than anticipated.

The geopolitical implications are substantial. If Chinese domestic chips can reliably support frontier model training and fine-tuning, US export controls may need to be reevaluated. Critics argue that restrictions may actually accelerate China's domestic chip development by creating guaranteed demand for local alternatives.

## Related Entries

- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- Huawei Ascend ([Huawei Ascend](../tools/huawei-ascend.md))
- US chip export controls ([US Chip Export Controls](../news/us-chip-export-controls.md))

---
<!-- RU -->

## Краткое описание

Команда под руководством Huawei заявила об успешном дообучении модели DeepSeek V4 с 1,6 трлн параметров на 1000 чипах Ascend 910C. Это демонстрирует, что китайское отечественное AI-оборудование способно справляться с задачами масштаба передовых моделей, что ставит под вопрос эффективность американских экспортных ограничений на чипы NVIDIA.

## Ключевые идеи

- 1000 чипов Ascend 910C использованы для пост-обучения DeepSeek V4 (1,6 трлн параметров)
- Речь о пост-обучении (fine-tuning и alignment), а не о предобучении с нуля — менее затратная, но всё ещё требовательная вычислительная задача
- Демонстрирует жизнеспособность отечественных AI-чипов Huawei для работы с моделями frontier-масштаба
- Прямой вызов эффективности американских экспортных ограничений на чипы, направленных против Китая
- DeepSeek V4 — одна из крупнейших моделей с открытыми весами, что делает демонстрацию особенно показательной
- Ставит вопрос: ускоряют ли экспортные ограничения развитие отечественных чипов вместо замедления AI-прогресса

## Подробнее

Заявление команды Huawei — важная веха в стремлении Китая к независимости в области AI-чипов. Хотя пост-обучение вычислительно менее затратно, чем предобучение модели с нуля, fine-tuning и alignment модели с 1,6 трлн параметров всё равно требуют значительной распределённой вычислительной инфраструктуры и производительности на уровне чипов.

Ascend 910C — флагманский AI-ускоритель Huawei, созданный как отечественная альтернатива серии NVIDIA A100/H100. Американские экспортные ограничения запретили NVIDIA продавать высокопроизводительные AI-чипы китайским заказчикам, создав рыночную нишу для отечественных альтернатив. Демонстрация показывает, что разрыв между отечественными чипами и продукцией NVIDIA сокращается быстрее ожидаемого.

Геополитические последствия значительны. Если китайские отечественные чипы могут надёжно поддерживать обучение и fine-tuning frontier-моделей, экспортные ограничения США могут потребовать переоценки. Критики утверждают, что ограничения фактически ускоряют развитие китайских чипов, создавая гарантированный спрос на локальные альтернативы.

## Связанные записи

- [[deepseek-v4]] ([DeepSeek V4](../models/deepseek-v4.md))
- Huawei Ascend ([Huawei Ascend](../tools/huawei-ascend.md))
- US chip export controls ([US Chip Export Controls](../news/us-chip-export-controls.md))
