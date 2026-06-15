---
title: "Pyrecall — Detect Catastrophic Forgetting"
title_ru: "Pyrecall — обнаружение катастрофического забывания"
category: tools
tags: [fine-tuning, catastrophic-forgetting, lora, safety, detection]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://github.com/Arths17/Pyrecall
---

## Summary
Tool that detects catastrophic forgetting in fine-tuned models by snapshotting skill scores before and after training. If a LoRA or fine-tune degrades performance on previously learned tasks, Pyrecall identifies the regression and can roll back. Addresses a key problem in iterative model customization.

## Key Ideas
- Snapshots skill/capability scores before fine-tuning begins
- Compares post-training scores against pre-training baseline to detect regression
- Works with LoRA adapters and full fine-tunes
- Can automatically roll back to pre-training state if degradation is detected
- Addresses the well-known but under-measured problem of catastrophic forgetting

## Details
Catastrophic forgetting is one of the most insidious problems in model customization: you fine-tune a model to be better at task A, and it silently becomes worse at task B. Most teams don't notice until the regression surfaces in production. Pyrecall makes this invisible problem visible.

The tool establishes a baseline by running a battery of skill benchmarks before training begins. After fine-tuning completes, it re-runs the same benchmarks and compares scores. Any statistically significant regression is flagged, giving teams a clear signal that the fine-tune introduced unwanted side effects.

This is particularly valuable for teams doing iterative fine-tuning — stacking LoRA adapters or running sequential training runs — where each step risks degrading capabilities from previous steps.

## Related Entries
- [[lora-low-rank-adaptation]] ([LoRA](../concepts/lora-low-rank-adaptation.md))
- [[lora-low-rank-adaptation]] ([Fine-Tuning Best Practices](../tips/fine-tuning-best-practices.md))

---
<!-- RU -->

## Краткое описание
Инструмент для обнаружения катастрофического забывания в файн-тюнинированных моделях путём снятия снапшотов оценок навыков до и после обучения. Если LoRA или файн-тюн ухудшает производительность на ранее изученных задачах, Pyrecall выявляет регрессию и может выполнить откат. Решает ключевую проблему итеративной настройки моделей.

## Ключевые идеи
- Создаёт снапшоты оценок навыков/возможностей до начала файн-тюнинга
- Сравнивает оценки после обучения с дотренировочным базовым уровнем для обнаружения регрессии
- Работает с LoRA-адаптерами и полным файн-тюнингом
- Может автоматически откатиться к состоянию до обучения при обнаружении деградации
- Решает хорошо известную, но плохо измеряемую проблему катастрофического забывания

## Подробнее
Катастрофическое забывание — одна из самых коварных проблем в настройке моделей: вы файн-тюните модель, чтобы она лучше справлялась с задачей A, и она незаметно становится хуже в задаче B. Большинство команд замечают это только тогда, когда регрессия проявляется в продакшене. Pyrecall делает эту невидимую проблему видимой.

Инструмент устанавливает базовый уровень, запуская набор навыковых бенчмарков до начала обучения. После завершения файн-тюнинга он повторно запускает те же бенчмарки и сравнивает оценки. Любая статистически значимая регрессия помечается, давая командам чёткий сигнал о том, что файн-тюн ввёл нежелательные побочные эффекты.

Это особенно ценно для команд, занимающихся итеративным файн-тюнингом — наложением LoRA-адаптеров или последовательными циклами обучения — где каждый шаг рискует ухудшить возможности, полученные на предыдущих шагах.

## Связанные записи
- [[lora-low-rank-adaptation]] ([LoRA](../concepts/lora-low-rank-adaptation.md))
- [[lora-low-rank-adaptation]] ([Fine-Tuning Best Practices](../tips/fine-tuning-best-practices.md))
