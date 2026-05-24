---
title: "Intern-S2-Preview: 35B Scientific Multimodal Foundation Model"
title_ru: "Intern-S2-Preview: 35B мультимодальная научная foundation-модель"
category: models
tags: [internlm, scientific-ai, multimodal, open-weights, qwen3, task-scaling, rl, mtp, crystal-structure]
aliases: [Intern S2, InternLM S2, Intern-S2]
confidence: medium
date: 2026-05-22
updated: 2026-05-24
sources:
  - https://huggingface.co/internlm/Intern-S2-Preview
  - https://www.reddit.com/r/LocalLLaMA/comments/1tdrw0s/internlminterns2preview_hugging_face/
---

## Summary
Intern-S2-Preview is a 35B scientific multimodal foundation model from Shanghai AI Lab (InternLM team) that matches the performance of the trillion-parameter Intern-S1-Pro on core scientific tasks, using only 35B parameters continued-pretrained from Qwen3.5.

## Key Ideas
- **Task scaling over parameter scaling**: instead of simply making the model bigger, Intern-S2-Preview scales the *difficulty, diversity, and coverage of scientific tasks* across the full training pipeline — from pre-training through RL.
- **35B vs. trillion-param parity**: achieves performance comparable to Intern-S1-Pro on multiple professional scientific benchmarks at roughly 3% of the parameter count.
- **First open-source model with crystal structure generation**: can generate material crystal structures AND make real-valued predictions — a capability not previously available in open models.
- **Enhanced scientific agent capabilities**: strong results on scientific agent benchmarks, meaning it can use tools and APIs autonomously in research workflows.
- **Efficient RL reasoning**: uses shared-weight Multi-Token Prediction (MTP) with KL loss during RL to reduce training/inference mismatch, substantially improving MTP accept rate and token generation speed.
- **CoT compression**: shortens chain-of-thought responses without degrading reasoning quality — improves both efficiency and performance.
- **Based on Qwen3.5**: continued pretraining from Qwen3.5 (35B), making it compatible with Qwen3.5's tokenizer and infrastructure.

## Details
The key innovation is **task scaling** — systematically covering hundreds of specialized scientific tasks (chemistry, biology, materials science, physics) in a full-chain pipeline: curating task data for pre-training, supervised fine-tuning, and finally reinforcement learning. This approach forces the model to develop genuine scientific reasoning rather than pattern-matching on a narrow benchmark.

The crystal structure generation capability makes it particularly useful for materials science workflows: the model can both *generate* candidate crystal structures and *predict* real-valued properties (bond lengths, energies, etc.) within a single forward pass. No other open-weights model had combined these two capabilities before Intern-S2-Preview.

The RL training phase also introduces CoT compression — a technique that teaches the model to reason more concisely without sacrificing accuracy, addressing a common issue where extended thinking chains become redundant and slow.

## Related Entries
- [[cola-dlm-bytedance-diffusion-lm]] ([Cola-DLM](../models/cola-dlm-bytedance-diffusion-lm.md))
- [[agent-operating-system]] ([Agent Operating System](../agents/agent-operating-system.md))

---
<!-- RU -->

## Краткое описание
Intern-S2-Preview — это 35B мультимодальная научная foundation-модель от Шанхайской лаборатории ИИ (команда InternLM), которая достигает производительности триллионно-параметровой Intern-S1-Pro на ключевых научных задачах — используя всего 35B параметров на основе Qwen3.5.

## Ключевые идеи
- **Масштабирование задач вместо параметров**: вместо увеличения размера модели Intern-S2-Preview масштабирует сложность, разнообразие и охват научных задач на всех этапах обучения — от предобучения до RL.
- **35B параметров против триллионов**: сопоставимые результаты с Intern-S1-Pro на профессиональных научных бенчмарках при ~3% от числа параметров.
- **Первая open-source модель с генерацией кристаллических структур**: способна генерировать структуры кристаллов материалов и делать вещественные предсказания.
- **Улучшенные агентские возможности для науки**: сильные результаты на бенчмарках научных агентов.
- **Эффективное RL-рассуждение**: разделённые веса MTP с KL-loss и сжатие CoT — рассуждения короче, но не хуже.
- **Основана на Qwen3.5**: продолженное предобучение от Qwen3.5 (35B).

## Подробнее
Ключевая инновация — **масштабирование задач**: сотни специализированных научных задач по химии, биологии, материаловедению и физике включены в полный обучающий конвейер: данные для предобучения, SFT и RL. Это заставляет модель развивать настоящее научное мышление, а не просто подбирать паттерны.

Возможность генерации кристаллических структур особенно ценна для материаловедческих воркфлоу: модель может одновременно *генерировать* кандидатные структуры и *предсказывать* вещественные свойства (длины связей, энергии) в рамках одного прямого прохода.

## Связанные записи
- [[cola-dlm-bytedance-diffusion-lm]] ([Cola-DLM](../models/cola-dlm-bytedance-diffusion-lm.md))
- [[agent-operating-system]] ([Agent Operating System](../agents/agent-operating-system.md))
