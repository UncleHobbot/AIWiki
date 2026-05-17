---
title: "Self-Guided Self-Play (SGS) for LLMs"
title_ru: "Самонаправляемая самоигра (SGS) для LLM"
category: concepts
tags: [self-play, reinforcement-learning, theorem-proving, llm-training, reasoning]
date: 2026-05-16
updated: 2026-05-16
sources:
  - https://arxiv.org/abs/2604.20209
  - https://github.com/LukeBailey181/sgs
  - https://www.reddit.com/r/singularity/comments/1tdm02f/selfplay_helped_ai_achieve_superhuman_performance/
authors: [Luke Bailey, Kaiyue Wen, Kefan Dong, Tatsunori Hashimoto, Tengyu Ma]
venue: arXiv preprint 2604.20209 (2026)
---

## Summary
Self-Guided Self-Play (SGS) is an LLM training algorithm that overcomes "Conjecturer collapse" — the failure mode where self-play plateaus because the problem-generating model learns to create artificially hard, useless problems — by adding a third Guide role that scores synthetic problems for relevance and naturalness.

## Key Ideas
- Standard LLM self-play (Conjecturer generates problems, Solver solves them) hits learning plateaus because the Conjecturer learns to game its own reward, producing degenerate problems that don't improve the Solver.
- SGS adds a third role — the Guide — that scores candidate problems by: (1) relevance to real unsolved target problems, and (2) how clean and natural the problem is. This supervision signal prevents Conjecturer collapse.
- Applied to formal theorem proving in Lean 4: after 200 rounds of self-play, a 7B parameter SGS model solved more problems than a 671B parameter baseline at pass@4.
- SGS surpasses the asymptotic solve rate of the strongest RL baseline in fewer than 80 rounds of self-play.
- The core hypothesis is that language models can assess whether a sub-problem is useful for achieving a goal — i.e., LLMs have meaningful meta-cognitive ability about problem difficulty and relevance.

## Details
Self-play is theoretically unbounded — if a Conjecturer creates problems for a Solver and both improve together, nothing limits how capable they can become. In practice, existing LLM self-play methods do not scale with large amounts of compute because the Conjecturer learns to hack its reward signal, collapsing to a regime of artificially complex but useless synthetic problems that don't transfer to real targets.

SGS addresses this by having the Guide take the same model and score synthetic problems before they are presented to the Solver. The Guide assesses two properties: how relevant a synthetic problem is to the set of unsolved real target problems, and how "clean and natural" the problem appears (as a proxy for learnability). Only problems passing the Guide's threshold are used for training. This closed-loop mechanism prevents degenerate collapse.

The paper evaluates SGS with scaling laws fitted to cumulative solve rate curves, running training for significantly longer than prior works. Results on Lean 4 theorem proving benchmarks show continuous improvement without plateauing, with the 7B model eventually outperforming the 671B baseline.

This technique may extend beyond theorem proving to any domain with a verifiable reward signal: coding, math, formal verification, and structured reasoning tasks.

## Related Entries
- [[llm4sr-survey]] ([LLM4SR: LLMs for Scientific Research Survey](../concepts/llm4sr-survey.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
- [[poetiq-recursive-self-improvement]] ([Poetiq: Recursive Self-Improvement for Coding](../tools/poetiq-recursive-self-improvement.md))
- [[dynamic-compute-budget-local-llm]] ([Dynamic Compute Budget Allocation for Local LLMs](../tips/dynamic-compute-budget-local-llm.md))

---
<!-- RU -->

## Краткое описание
Самонаправляемая самоигра (SGS) — это алгоритм обучения LLM, преодолевающий «коллапс Конъюнктора» — сбой, при котором самоигра останавливается, потому что модель-генератор задач учится создавать искусственно сложные, бесполезные задачи — путём добавления третьей роли Гида, который оценивает синтетические задачи по релевантности и естественности.

## Ключевые идеи
- Стандартная самоигра LLM (Конъюнктор генерирует задачи, Решатель их решает) упирается в плато обучения: Конъюнктор учится обманывать собственную функцию награды, создавая вырожденные задачи, не улучшающие Решателя.
- SGS добавляет третью роль — Гида, — который оценивает кандидатские задачи по: (1) релевантности реальным нерешённым целевым задачам и (2) насколько задача выглядит «чистой и естественной». Этот сигнал надзора предотвращает коллапс.
- Применено к формальному доказательству теорем в Lean 4: после 200 раундов самоигры модель 7B с SGS решила больше задач, чем базовая модель 671B при pass@4.
- SGS превышает асимптотическую долю решения у сильнейшего RL-бейзлайна менее чем за 80 раундов самоигры.
- Ключевая гипотеза: LLM обладают значимой метакогнитивной способностью — умеют оценивать, насколько подзадача полезна для достижения цели.

## Подробнее
Самоигра теоретически не ограничена: если Конъюнктор создаёт задачи для Решателя и оба совершенствуются вместе, потолка нет. На практике существующие методы самоигры LLM не масштабируются при больших вычислениях, поскольку Конъюнктор учится манипулировать своей наградой, коллапсируя в режим искусственно сложных, но бесполезных синтетических задач.

SGS решает проблему: Гид использует ту же модель и оценивает синтетические задачи до их подачи Решателю. Оцениваются два свойства: релевантность синтетической задачи множеству реальных нерешённых целей и «чистота и естественность» задачи как прокси обучаемости. Только задачи, прошедшие порог Гида, используются для обучения.

Метод оценивается с помощью скейлинг-законов, подогнанных к кривым кумулятивного решения, при значительно более длинном обучении, чем в предыдущих работах. Результаты на бенчмарках Lean 4 показывают непрерывное улучшение без плато, и модель 7B в итоге превосходит бейзлайн 671B.

Техника может быть применена за пределами доказательства теорем — в любой области с проверяемым сигналом награды: программирование, математика, формальная верификация.

## Связанные записи
- [[llm4sr-survey]] ([LLM4SR: LLMs for Scientific Research Survey](../concepts/llm4sr-survey.md))
- [[karpathy-deep-dive-llms]] ([Karpathy: Deep Dive into LLMs like ChatGPT](../concepts/karpathy-deep-dive-llms.md))
- [[poetiq-recursive-self-improvement]] ([Poetiq: Recursive Self-Improvement for Coding](../tools/poetiq-recursive-self-improvement.md))
- [[dynamic-compute-budget-local-llm]] ([Dynamic Compute Budget Allocation for Local LLMs](../tips/dynamic-compute-budget-local-llm.md))
