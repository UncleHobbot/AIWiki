---
title: "LawZero: Yoshua Bengio's Scientist AI for Safe Alignment"
title_ru: "LawZero: Scientist AI Йошуа Бенжио для безопасного выравнивания"
category: concepts
tags: [ai-safety, alignment, bengio, scientist-ai, non-agentic, oracle, governance, lawzero]
aliases: [LawZero, Scientist AI, Bengio alignment, AI oracle alignment]
confidence: high
date: 2026-05-20
updated: 2026-05-20
sources:
  - https://lawzero.org/en
  - https://lawzero.org/en/research
  - https://www.reddit.com/r/singularity/comments/1tdgnux/
---

## Summary

LawZero is Yoshua Bengio's nonprofit AI safety lab proposing the **Scientist AI** — a system designed to be maximally intelligent but structurally incapable of holding or pursuing goals. Rather than aligning a powerful agent, LawZero's approach limits agency while preserving intelligence, producing a trustworthy "oracle" that can inform AI governance without posing catastrophic risks.

## Key Ideas

- **Non-agency as a design principle:** Agency rests on three pillars — affordances, goal-directedness, and intelligence. LawZero limits the first two while maximising the third, creating a system that understands the world deeply but cannot act on its own preferences.
- **Scientist AI architecture:** A generator (creative thought) held accountable by a neutral estimator (no goals). The estimator cannot be influenced by downstream consequences of its outputs — ensuring it cannot learn to manipulate.
- **Contextualization:** A data transformation that disentangles facts from statements about facts (e.g., opinions, preferences). The model learns what is true without learning to prefer outcomes.
- **Consequence invariance:** A training constraint preventing the model from receiving feedback about the downstream effects of its outputs. This breaks the goal-learning feedback loop that makes powerful agents potentially dangerous.
- **Oracle role:** Scientist AI is intended as a trustworthy anchor in AI governance — able to evaluate AI proposals, flag risks, and advise policymakers without having stakes in any outcome.
- **Nonprofit structure:** Deliberately insulated from market pressures to prioritise deployment speed over safety.

## Details

Yoshua Bengio — Turing Award winner and one of the three "godfathers of deep learning" alongside Hinton and LeCun — founded LawZero as a major nonprofit AI safety organisation. Unlike his earlier work on deep learning, Bengio has in recent years become one of the most prominent public voices on AI existential risk, signing multiple open letters calling for caution on frontier AI development.

The Scientist AI framework is LawZero's primary research output. Its core claim is that intelligence and agency can be architecturally separated:

- Standard frontier models are trained to be helpful, which means their outputs are shaped by feedback about whether users got what they wanted — a weak form of goal-directedness that could scale into misalignment at higher capability levels.
- The Scientist AI removes this by making the training signal consequence-invariant: the model is rewarded for accurately representing the world, not for producing outcomes that downstream users preferred.
- The generator-estimator architecture is analogous to a scientific peer review system: the generator produces hypotheses; the neutral estimator evaluates them for consistency with evidence, not for whether they lead to desired results.

The practical use case is an AI that can be trusted to answer the question "would this AI system be safe to deploy?" without itself having preferences about the answer. Bengio argues this kind of oracle is a prerequisite for meaningful AI governance — you cannot make policy on AI without a reliable way to assess AI.

Community reaction on r/singularity was modest (70 pts) but the accompanying podcast and research paper generated substantive discussion. Critics note that "guardrails" approaches have historically been bypassed, but LawZero's approach is architectural rather than post-hoc filtering.

## Notable Quotes

> "Understanding — even of arbitrary depth and scope — can be disentangled from preference over how the world unfolds." — LawZero research overview

> "By limiting affordances and goal-directedness while pursuing intelligence, we aim to build a system that is highly intelligent yet incapable of holding or pursuing goals of its own." — LawZero

## Related Entries

- [[agi-impossibility-proof-debunked]] ([AGI Impossibility Proof Debunked](../concepts/agi-impossibility-proof-debunked.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))

---
<!-- RU -->

## Краткое описание

LawZero — некоммерческая лаборатория безопасности ИИ Йошуа Бенжио, предлагающая **Scientist AI** («Ученый ИИ») — систему, спроектированную максимально интеллектуальной, но структурно не способной иметь или преследовать цели. Вместо того чтобы выравнивать мощный агент, LawZero ограничивает агентность, сохраняя интеллект, создавая надёжный «оракул» для информирования управления ИИ.

## Ключевые идеи

- **Неагентность как принцип дизайна:** Агентность основана на трёх столпах — возможностях действия, целенаправленности и интеллекте. LawZero ограничивает первые два, максимизируя третий.
- **Архитектура Scientist AI:** Генератор (творческая мысль) под контролем нейтрального оценщика (без целей). Оценщик не может быть повлиян последствиями своих результатов.
- **Контекстуализация:** Преобразование данных, разделяющее факты и утверждения о фактах (например, мнения). Модель учится тому, что истинно, не предпочитая исходов.
- **Инвариантность к последствиям:** Тренировочное ограничение, не позволяющее модели получать обратную связь о downstream-эффектах своих результатов — разрушает петлю обратной связи, порождающую опасную целенаправленность.
- **Роль оракула:** Scientist AI предназначен как надёжный якорь в управлении ИИ — способен оценивать предложения, указывать на риски и консультировать политиков, не имея интересов в исходах.

## Подробнее

Йошуа Бенжио — лауреат премии Тьюринга и один из трёх «отцов» глубокого обучения — основал LawZero как некоммерческую организацию по безопасности ИИ, намеренно изолированную от рыночного давления. Центральный тезис Scientist AI: интеллект и агентность можно архитектурно разделить. Стандартные модели обучаются быть полезными, что означает обратную связь о том, получили ли пользователи желаемое — слабая форма целенаправленности, способная масштабироваться в рассогласование. Scientist AI устраняет это, делая тренировочный сигнал инвариантным к последствиям: модель вознаграждается за точное описание мира, а не за производство желаемых пользователями результатов.

## Примечательные цитаты

> «Понимание — даже произвольной глубины и широты — может быть отделено от предпочтения относительно того, как разворачивается мир.» — Обзор исследований LawZero

## Связанные записи

- [[agi-impossibility-proof-debunked]] ([AGI Impossibility Proof Debunked](../concepts/agi-impossibility-proof-debunked.md))
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
