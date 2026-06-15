---
title: "kosa-4B-it-v1: Qwen3-4B Fine-Tune Beating Phi-4-mini"
title_ru: "kosa-4B-it-v1: fine-tune Qwen3-4B, превосходящий Phi-4-mini"
category: models
tags: [qwen, qwen3-4b, fine-tune, small-models, benchmarks, phi-4-mini]
aliases: [kosa-4B-it-v1, kosa-labs]
confidence: medium
updated: 2026-06-14
sources:
  - https://huggingface.co/kosa-labs/kosa-4B-it-v1
  - https://www.reddit.com/r/Qwen_AI/comments/1u4kinc/kosa4bitv1_finetuned_qwen34b_beats_its_base_on/
---

## Summary
kosa-labs released kosa-4B-it-v1, an instruction-tuned fine-tune of Qwen3-4B-Instruct-2507 that improves over the base model on all six benchmarks tested (+5.7 average) and outscores Phi-4-mini-instruct by roughly 7 points average, with raw evaluation result files published for verification.

## Key Ideas
- Built on top of Qwen3-4B-Instruct-2507, evaluated with the same lm-evaluation-harness session (v0.4.12, vLLM, bf16, temperature 0, chat template applied) for both base and fine-tuned models.
- Reported gains over the Qwen3-4B base: GSM8K strict 73.24% → 84.23%, GSM8K flexible 79.15% → 85.60%, IFEval prompt-strict 83.36% → 85.77%, IFEval instruction-strict 88.61% → 90.29%, ARC-Challenge (acc_norm) 43.09% → 52.13%, MMLU 61.89% → 65.76% — average 71.56% → 77.30%.
- Outperforms Phi-4-mini-instruct by roughly +7 points average in the same harness.
- Training data was checked for benchmark contamination (13-gram and 8-gram overlap against all four test sets, with a positive control to confirm the contamination checker itself works) and came back clean.
- Raw result JSONs are published in the model's HuggingFace repo under `/benchmarks`, allowing independent verification rather than trusting reported numbers alone.

## Details
This is a small-model fine-tune release notable mainly for its methodological transparency: rather than just posting benchmark deltas, kosa-labs ran both the base Qwen3-4B-Instruct-2507 and their fine-tune through an identical lm-evaluation-harness configuration and published the raw JSON outputs. Combined with an explicit contamination check (n-gram overlap with a positive control), this gives the numbers more credibility than typical "we beat X" community posts — though it remains a single independent lab's self-reported result (Tier 3, community), and broader third-party reproduction would further confirm it.

The result is relevant to the broader trend of small (sub-8B) open-weight models closing the gap with larger ones through targeted fine-tuning — see [[choose-llm-api-self-host-hybrid]] and [[small-models-clean-architecture]] for related discussion on when small local models are sufficient for agentic/coding workloads. A ~7 point average improvement over Phi-4-mini at the 4B scale would make kosa-4B-it-v1 a candidate for resource-constrained local deployments where Qwen3-4B was already being considered.

## Related Entries
- [[small-models-clean-architecture]] ([Small Models + Clean Architecture](../tips/small-models-clean-architecture.md))
- [[choose-llm-api-self-host-hybrid]] ([Choosing an LLM: API, Self-Host, or Hybrid](../tips/choose-llm-api-self-host-hybrid.md))
- [[nex-n2-pro-mini-qwen-finetune]] ([Nex-N2 Pro/Mini Qwen 3.5 Fine-Tunes](../models/nex-n2-pro-mini-qwen-finetune.md))
- [[llm-wiki-chinese-models-comparison]] ([Chinese LLM Models Comparison](../models/llm-wiki-chinese-models-comparison.md))

---
<!-- RU -->

## Краткое описание
kosa-labs выпустила kosa-4B-it-v1 — instruction-tuned fine-tune модели Qwen3-4B-Instruct-2507, которая улучшает результаты по всем шести протестированным бенчмаркам (+5.7 в среднем) и превосходит Phi-4-mini-instruct примерно на 7 баллов в среднем, с публикацией исходных файлов оценки для проверки.

## Ключевые идеи
- Построена на базе Qwen3-4B-Instruct-2507, оценена в одной и той же сессии lm-evaluation-harness (v0.4.12, vLLM, bf16, temperature 0, с применением chat template) как для базовой, так и для fine-tuned модели.
- Заявленный прирост относительно базы Qwen3-4B: GSM8K strict 73.24% -> 84.23%, GSM8K flexible 79.15% -> 85.60%, IFEval prompt-strict 83.36% -> 85.77%, IFEval instruction-strict 88.61% -> 90.29%, ARC-Challenge (acc_norm) 43.09% -> 52.13%, MMLU 61.89% -> 65.76% — в среднем 71.56% -> 77.30%.
- Превосходит Phi-4-mini-instruct примерно на +7 баллов в среднем в той же системе оценки.
- Обучающие данные проверены на контаминацию бенчмарков (перекрытие 13-грамм и 8-грамм со всеми четырьмя тестовыми наборами, с positive control для проверки самого чекера) — контаминации не обнаружено.
- Исходные JSON-файлы результатов опубликованы в репозитории модели на HuggingFace в папке `/benchmarks`, что позволяет независимую проверку, а не просто доверие заявленным цифрам.

## Подробнее
Это релиз fine-tune небольшой модели, примечательный главным образом методологической прозрачностью: вместо простого заявления о приросте бенчмарков, kosa-labs прогнала и базовую Qwen3-4B-Instruct-2507, и свой fine-tune через идентичную конфигурацию lm-evaluation-harness и опубликовала исходные JSON-результаты. В сочетании с явной проверкой на контаминацию (перекрытие n-грамм с positive control) это придаёт цифрам больше достоверности, чем типичные посты сообщества "мы превзошли X" — хотя это всё ещё самостоятельно заявленный результат одной независимой лаборатории (Tier 3, community), и независимое воспроизведение третьими сторонами добавило бы уверенности.

Результат вписывается в более широкий тренд: небольшие (до 8B) открытые модели сокращают разрыв с более крупными за счёт целевого fine-tuning — см. [[choose-llm-api-self-host-hybrid]] и [[small-models-clean-architecture]] о том, когда небольших локальных моделей достаточно для агентных/кодинг-задач. Прирост ~7 баллов в среднем над Phi-4-mini на масштабе 4B делает kosa-4B-it-v1 кандидатом для ресурсо-ограниченных локальных развёртываний, где уже рассматривалась Qwen3-4B.

## Связанные записи
- [[small-models-clean-architecture]] ([Маленькие модели + чистая архитектура](../tips/small-models-clean-architecture.md))
- [[choose-llm-api-self-host-hybrid]] ([Выбор LLM: API, self-host или гибрид](../tips/choose-llm-api-self-host-hybrid.md))
- [[nex-n2-pro-mini-qwen-finetune]] ([Nex-N2 Pro/Mini — fine-tunes Qwen 3.5](../models/nex-n2-pro-mini-qwen-finetune.md))
- [[llm-wiki-chinese-models-comparison]] ([Сравнение китайских LLM](../models/llm-wiki-chinese-models-comparison.md))
