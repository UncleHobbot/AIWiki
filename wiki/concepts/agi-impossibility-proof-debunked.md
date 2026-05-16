---
title: "Barriers to Complexity-Theoretic Proofs That AGI Is Impossible"
title_ru: "Барьеры для доказательств теоретической сложности невозможности AGI"
category: concepts
tags: [agi, complexity-theory, ml-theory, van-rooij, impossibility, machine-learning]
date: 2026-05-16
updated: 2026-05-16
sources:
  - https://arxiv.org/abs/2411.06498
  - https://www.reddit.com/r/MachineLearning/comments/1tc1xr3/humanlevel_performance_via_ml_was_not_proven/
authors: [Michael Guerzhoy]
venue: "Computational Brain & Behavior (2026)"
---

## Summary
Guerzhoy (2026) demonstrates that Van Rooij et al.'s widely-cited "Ingenia Theorem" — claiming to prove that achieving human-like intelligence via machine learning is computationally intractable — contains an unjustified assumption that fatally undermines the proof, published as a response in the same journal.

## Key Ideas
- The Van Rooij et al. 2024 proof assumes a specific distribution over (input, output) tuples representing "human situation-behaviour," but this assumption is never justified and cannot be, since "human-like" is never mathematically defined.
- The fatal flaw: if you substitute "ImageNet inputs/labels" for "human situation-behaviour tuples" everywhere in the proof, it equally "proves" that learning to classify ImageNet is intractable — an absurd conclusion, since we already do it.
- Two fundamental barriers make the proof irreparable: (1) any repair must precisely define "human-like intelligence," which remains philosophically contested; (2) any repair must account for the inductive biases of specific ML systems, which are key to feasibility analysis.
- A third barrier: attempts to save the proof by restricting to subsets of the data face definitional problems in choosing which subsets.
- The r/MachineLearning community received the original Van Rooij paper with widespread skepticism from researchers with relevant expertise; the Guerzhoy rebuttal was published as the first formal response after ~2 years.

## Details
The "Ingenia Theorem" made significant noise on the internet after its 2024 publication in *Computational Brain & Behavior*. The paper claimed to reduce a known NP-hard problem to the problem of learning a human-level classifier from data, concluding that AGI via machine learning is impossible in a complexity-theoretic sense.

Guerzhoy's analysis identifies the critical flaw: the proof introduces a construct corresponding to "distribution of human situation-behaviour tuples" when framing the problem, then silently swaps this for "for all polytime-sampleable distributions" when executing the formal proof. This bait-and-switch means the proof is not about human-like intelligence at all — it is a generic statement about learning arbitrary functions, which says nothing about the specific case of human cognition.

The rebuttal was published in the same journal (*Computational Brain & Behavior*, April 2026). The core point: complexity-theoretic arguments can only say something about AGI if they can be grounded in properties of human intelligence specifically — and no such grounding exists in the Van Rooij proof.

The original authors reportedly dismissed early criticism on social media as "mansplaining," which delayed formal academic response. The Guerzhoy paper establishes that no straightforward repair exists and identifies three independent classes of barriers.

## Related Entries
- [[karpathy-deep-dive-llms]]
- [[llm4sr-survey]]

---
<!-- RU -->

## Краткое описание
Герджой (2026) доказывает, что широко цитируемая «теорема Ingenia» Ван Рой и соавторов — якобы доказывающая вычислительную неразрешимость достижения человекоподобного интеллекта через машинное обучение — содержит необоснованное допущение, опубликовав опровержение в том же журнале.

## Ключевые идеи
- Доказательство Ван Рой и др. 2024 предполагает конкретное распределение пар (вход, выход), представляющих «ситуацию-поведение человека», но это допущение никогда не обосновывается — и не может быть обосновано, поскольку «человекоподобие» математически не определено.
- Роковой изъян: если заменить «человеческие ситуации-поведения» на «входы-метки ImageNet» во всём доказательстве, оно в равной мере «доказывает», что обучение классификации ImageNet неразрешимо — абсурдный вывод, опровергаемый практикой.
- Два фундаментальных барьера делают доказательство неисправимым: (1) любое исправление требует точного определения «человекоподобного интеллекта» — философски спорного понятия; (2) любое исправление должно учитывать индуктивные смещения конкретных систем МО, ключевые для анализа осуществимости.
- Третий барьер: попытки спасти доказательство за счёт ограничения подмножествами данных сталкиваются с проблемами определения этих подмножеств.
- Сообщество r/MachineLearning встретило исходную работу Ван Рой с широким скептицизмом со стороны специалистов; опровержение Герджоя — первый формальный ответ спустя ~2 года.

## Подробнее
«Теорема Ingenia» привлекла широкое внимание после публикации в 2024 году в журнале *Computational Brain & Behavior*. Статья утверждала, что сводит известную NP-трудную задачу к задаче обучения классификатору человеческого уровня, заключая о принципиальной вычислительной неразрешимости AGI через МО.

Анализ Герджоя выявляет критический изъян: доказательство вводит конструкцию «распределения ситуаций-поведений человека» при постановке задачи, но затем незаметно заменяет её на «для всех полиномиально-сэмплируемых распределений» при проведении формального доказательства. Это подмена понятий: доказательство становится общим утверждением об обучении произвольным функциям, ничего не говорящим о специфике человеческого познания.

Опровержение опубликовано в том же журнале (*Computational Brain & Behavior*, апрель 2026). Ключевой тезис: аргументы теоретической сложности могут что-то сказать об AGI только при условии, что они опираются на специфические свойства человеческого интеллекта — а в доказательстве Ван Рой такой опоры нет.

## Связанные записи
- [[karpathy-deep-dive-llms]]
- [[llm4sr-survey]]
