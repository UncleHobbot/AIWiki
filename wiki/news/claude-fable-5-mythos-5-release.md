---
title: "Claude Fable 5 / Mythos 5 Dual Release"
title_ru: "Двойной релиз Claude Fable 5 / Mythos 5"
category: news
tags: [anthropic, claude, fable, mythos, release, dual-model, ai-safety]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://thehackernews.com/2026/06/anthropic-releases-claude-fable-5-its.html
  - https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf
---

## Summary

On June 9, 2026, Anthropic released Claude Fable 5 — its most capable model ever. It ships as a single model split into two products: Fable 5 (public, with cyber safeguards) and Claude Mythos 5 (same underlying model, safeguards lifted, restricted to vetted cybersecurity users).

## Key Ideas

- One model, two products — safety classifiers determine which behavior profile is active
- Fable 5 is the public-facing product with cybersecurity safeguards enabled
- Mythos 5 has cyber safeguards lifted but is restricted to vetted cybersecurity professionals
- Silent restriction of AI research capabilities (pretraining pipelines, distributed training, accelerator design) was discovered on page 13 of the model card
- Community backlash followed; Anthropic subsequently made these restrictions visible to users
- BenchLM score: 99 for Mythos 5, 95 for Fable 5 / Opus 4.8 tier

## Details

Anthropic's dual-release strategy represents a novel approach to the safety-capability tradeoff. Rather than building two separate models, a single architecture is deployed with safety classifiers that toggle behavior profiles. Fable 5 serves the general public with full safeguards, while Mythos 5 is available only to vetted cybersecurity professionals who need unrestricted capabilities for offensive security research.

The controversy emerged when users discovered that Anthropic had quietly limited the model's ability to assist with frontier LLM development tasks — including pretraining pipeline design, distributed training infrastructure, and AI accelerator architecture. These restrictions were buried in the model card documentation rather than communicated upfront. The community responded with criticism about transparency, and Anthropic updated its documentation to make the limitations clearly visible.

BenchLM benchmarks place Mythos 5 at 99 and Fable 5 at the Opus 4.8 tier (95), confirming the model's position at the top of current capability rankings.

## Related Entries

- [[claude-code]] ([Anthropic Claude Models](../models/anthropic-claude-models.md))
- AI safety approaches ([AI Safety Approaches](../concepts/ai-safety-approaches.md))
- [[fable5-mythos5-export-control-suspension]] ([US Export-Control Order Suspends Anthropic's Fable 5 and Mythos 5 Worldwide](../news/fable5-mythos5-export-control-suspension.md))

---
<!-- RU -->

## Краткое описание

9 июня 2026 года Anthropic выпустила Claude Fable 5 — свою самую мощную модель. Она поставляется как единая модель, разделённая на два продукта: Fable 5 (публичный, с кибер-ограничениями) и Claude Mythos 5 (та же модель без ограничений, доступ только проверенным специалистам по кибербезопасности).

## Ключевые идеи

- Одна модель, два продукта — классификаторы безопасности определяют активный профиль поведения
- Fable 5 — публичный продукт с включёнными механизмами кибербезопасности
- Mythos 5 — кибер-ограничения сняты, доступ ограничен проверенными специалистами
- Тихое ограничение возможностей AI-исследований (пайплайны предобучения, распределённое обучение, дизайн ускорителей) обнаружено на странице 13 model card
- Реакция сообщества привела к тому, что Anthropic сделала ограничения видимыми для пользователей
- BenchLM: 99 для Mythos 5, 95 для Fable 5 / уровня Opus 4.8

## Подробнее

Стратегия двойного релиза Anthropic представляет новый подход к балансу между безопасностью и возможностями. Вместо создания двух отдельных моделей используется единая архитектура с классификаторами безопасности, которые переключают профили поведения. Fable 5 обслуживает широкую публику с полными ограничениями, тогда как Mythos 5 доступен только проверенным профессионалам в области кибербезопасности.

Конфликт возник, когда пользователи обнаружили, что Anthropic негласно ограничила способность модели помогать с задачами разработки frontier LLM — включая дизайн пайплайнов предобучения, инфраструктуру распределённого обучения и архитектуру AI-ускорителей. Ограничения были скрыты в документации model card, а не представлены открыто. После критики сообщества Anthropic обновила документацию, сделав ограничения явно видимыми.

## Связанные записи

- [[claude-code]] ([Anthropic Claude Models](../models/anthropic-claude-models.md))
- AI safety approaches ([AI Safety Approaches](../concepts/ai-safety-approaches.md))
- [[fable5-mythos5-export-control-suspension]] ([Экспортный контроль США приостанавливает доступ к Fable 5 и Mythos 5 Anthropic по всему миру](../news/fable5-mythos5-export-control-suspension.md))
