---
title: "LoRA (Low-Rank Adaptation)"
title_ru: "LoRA (адаптация низкого ранга)"
category: concepts
tags: [lora, fine-tuning, low-rank, adaptation]
aliases: [LoRA, Low-Rank Adaptation, LoRA fine-tuning, QLoRA]
confidence: high
updated: 2026-06-14
sources:
  - https://arxiv.org/abs/2106.09685
---

## Summary

LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that freezes a model's original weights and learns small, low-rank update matrices ("adapters") instead. The adapters capture task-specific behavior at a fraction of the trainable parameters, memory, and storage cost of full fine-tuning — while the base model stays intact.

## Key Ideas

- **Freeze the base, train adapters:** original weights are frozen; trainable low-rank matrices (A·B decomposition) are inserted into selected layers, cutting trainable parameters to a small percentage.
- **Composable & swappable:** adapters are tiny files that can be hot-swapped per task and even stacked or merged, enabling one base model to serve many specializations.
- **Memory efficiency:** training fits on consumer GPUs (especially QLoRA, which combines LoRA with quantized base weights), democratizing custom fine-tuning.
- **Quality trade-off:** for many tasks LoRA matches full fine-tuning, but extreme domain shifts or maximum capability may still require full tuning.
- **Risk of catastrophic forgetting:** although the base weights are preserved, sequential adapter stacking or over-tuning can still degrade earlier capabilities — tools like Pyrecall detect this regression.

## Details

LoRA is grounded in the observation that weight updates during fine-tuning often have low "intrinsic rank." Instead of updating a full weight matrix W (of size d×k), LoRA learns two small matrices A (d×r) and B (r×k) with rank r ≪ min(d,k), such that the effective update is W + A·B. Because only A and B are trained and stored, the adapter is dramatically smaller than the base model — often tens of megabytes versus gigabytes.

This makes LoRA the dominant approach for community and enterprise fine-tuning: one strong base model plus a library of task adapters. The low cost also encourages iterative tuning, which is where catastrophic-forgetting risk appears — stacking adapters or running sequential training can quietly erode skills captured earlier, which is why regression-detection tooling matters in iterative LoRA workflows.

## Notable Quotes

> "We hypothesize that the change in weights during model adaptation has a low 'intrinsic rank,' leading us to propose Low-Rank Adaptation." — Hu et al., 2021 (LoRA paper)

## Related Entries

- [[pyrecall-catastrophic-forgetting]] ([Pyrecall — Catastrophic Forgetting Detection](../tools/pyrecall-catastrophic-forgetting.md))

---
<!-- RU -->

## Краткое описание

LoRA (Low-Rank Adaptation) — техника параметро-эффективного файн-тюнинга, которая замораживает исходные веса модели и вместо этого обучает небольшие матрицы обновлений низкого ранга («адаптеры»). Адаптеры фиксируют поведение, специфичное для задачи, при доле обучаемых параметров, памяти и хранилища от полного файн-тюнинга — базовая модель при этом остаётся нетронутой.

## Ключевые идеи

- **Заморозить базу, обучать адаптеры:** исходные веса заморожены; обучаемые матрицы низкого ранга (разложение A·B) вставляются в выбранные слои, сокращая обучаемые параметры до небольшого процента.
- **Композируемые и сменяемые:** адаптеры — крошечные файлы, которые можно горячо менять под задачу и даже накладывать или объединять, позволяя одной базовой модели обслуживать множество специализаций.
- **Эффективность по памяти:** обучение помещается на потребительские GPU (особенно QLoRA, сочетающая LoRA с квантованными базовыми весами), демократизируя кастомный файн-тюнинг.
- **Компромисс качества:** для многих задач LoRA не уступает полному файн-тюнингу, но при сильном сдвиге домена или максимальных требованиях к способности может потребоваться полный тюнинг.
- **Риск катастрофического забывания:** хотя базовые веса сохранены, последовательное наложение адаптеров или чрезмерный тюнинг всё равно могут ухудшить ранее полученные способности — инструменты вроде Pyrecall выявляют эту регрессию.

## Подробнее

LoRA основана на наблюдении, что обновления весов при файн-тюнинге часто имеют низкий «внутренний ранг». Вместо обновления полной матрицы весов W (размера d×k) LoRA обучает две малые матрицы A (d×r) и B (r×k) ранга r ≪ min(d,k), так что эффективное обновление равно W + A·B. Поскольку обучаются и хранятся только A и B, адаптер значительно меньше базовой модели — часто десятки мегабайт против гигабайтов.

Это делает LoRA доминирующим подходом для community- и энтерпрайз-файн-тюнинга: одна сильная базовая модель плюс библиотека задачных адаптеров. Низкая стоимость также поощряет итеративный тюнинг, где и возникает риск катастрофического забывания — наложение адаптеров или последовательные циклы обучения могут незаметно разрушить навыки, полученные ранее, поэтому инструментам обнаружения регрессии важно место в итеративных LoRA-workflow.

## Примечательные цитаты

> «Мы предполагаем, что изменение весов во время адаптации модели имеет низкий «внутренний ранг», что и приводит нас к предложению Low-Rank Adaptation.» — Hu et al., 2021 (статья о LoRA)

## Связанные записи

- [[pyrecall-catastrophic-forgetting]] ([Pyrecall — Catastrophic Forgetting Detection](../tools/pyrecall-catastrophic-forgetting.md))
