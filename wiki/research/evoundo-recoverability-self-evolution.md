---
title: "EvoUndo — Recoverability-Constrained Self-Evolution for Agent Harnesses"
title_ru: "EvoUndo — самоэволюция агентных харнесов с проверкой обратимости"
category: research
tags: [self-evolution, agent-harness, recoverability, arxiv, mutation, safety]
aliases: [EvoUndo, recoverability self-evolution, agent self-modification]
confidence: high
updated: 2026-09-02
sources:
  - https://arxiv.org/abs/2608.28363
  - https://www.reddit.com/r/MachineLearning/comments/1w4m0hq/evoundo_recoverabilityconstrained_selfevolution/
---

## Summary
**EvoUndo** (arXiv 2608.28363) addresses the safety hole in self-evolving agents: LLM agents increasingly modify their own prompts, tools, middleware, and execution harnesses at runtime — but a mutation that improves capability in *one* state may be unrecoverable in *another*. Across 600 one-shot self-evolution tasks, **197 capability-improving mutations failed recoverability verification**; conventional repair recovered 0/197, a deterministic oracle recovered 48/197, and an extended recovery calculus reached 191/197.

## Key Ideas
- **The risk model:** self-modification is measured by immediate capability gain, not by whether the change can be safely undone later in a different state.
- **Headline numbers:** 197/600 "improving" mutations were unrecoverable under the original recovery representation — a 33% latent-damage rate invisible to capability metrics.
- **Repair results:** 0/197 with conventional repair → 48/197 with a deterministic oracle → 191/197 with the extended recovery calculus. The recovery *language* was the bottleneck, not the concept.
- **Contribution:** a framework for representing, synthesizing, diagnosing, and independently verifying recoverability across counterfactual states.
- Ties directly to the wiki's self-evolution cluster ([[poetiq-recursive-self-improvement]], [[10x-coding-agent-methodology]]) and the [[hard-gates-over-soft-prompts]] principle: structure over exhortation.

## Details
EvoUndo gives "let the agent improve its own harness" a safety formalism: a mutation is not an improvement unless it's *reversibly* an improvement. The 0/197 conventional-repair result is the striking part — if your recovery representation is the mutation's own description, you can't undo what the description glosses over. Practical takeaway for anyone building self-modifying agent systems: log mutations in a recovery calculus, not in prose.

## Related Entries
- [[poetiq-recursive-self-improvement]] ([Poetiq Recursive Self-Improvement](../tools/poetiq-recursive-self-improvement.md))
- [[10x-coding-agent-methodology]] ([10x Methodology](../tools/10x-coding-agent-methodology.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](../tips/hard-gates-over-soft-prompts.md))
- [[loop-engineering-hype-check]] ([Loop Engineering Hype-Check](../tips/loop-engineering-hype-check.md))

---
- [[model-diversity-multi-agent-verification]] ([Model Diversity Verification](model-diversity-multi-agent-verification.md))
<!-- RU -->

## Краткое описание
**EvoUndo** (arXiv 2608.28363) закрывает дыру безопасности самоэволюционирующих агентов: LLM-агенты всё чаще модифицируют собственные промпты, инструменты, middleware и харнесы в рантайме — но мутация, улучшающая возможности в *одном* состоянии, может быть невозвратимой в *другом*. На 600 one-shot задачах самоэволюции **197 улучшающих мутаций не прошли проверку обратимости**; обычный repair восстановил 0/197, детерминированный оракул — 48/197, расширенное recovery-исчисление — 191/197.

## Ключевые идеи
- **Модель риска:** самомодификация оценивается по немедленному приросту возможностей, а не по тому, можно ли изменение безопасно отменить позже в другом состоянии.
- **Главные числа:** 197 из 600 «улучшающих» мутаций невозвратимы в исходном представлении восстановления — 33% скрытого ущерба, невидимого для метрик возможностей.
- **Результаты ремонта:** 0/197 → 48/197 → 191/197. Узкое место — *язык* восстановления, не концепция.
- **Вклад:** фреймворк представления, синтеза, диагностики и независимой верификации обратимости в контрфактических состояниях.

## Подробнее
EvoUndo даёт фразе «пусть агент улучшает свой харнес» формализм безопасности: мутация — не улучшение, если она не *обратимо* улучшение. Результат 0/197 обычного repair — самое поразительное: если ваше представление восстановления — это собственное описание мутации, вы не отмените то, что описание умалчивает. Практический вывод для само-модифицирующихся систем: логируйте мутации в recovery-исчислении, а не в прозе.

## Связанные записи
- [[poetiq-recursive-self-improvement]] ([Poetiq Recursive Self-Improvement](../tools/poetiq-recursive-self-improvement.md))
- [[10x-coding-agent-methodology]] ([10x Methodology](../tools/10x-coding-agent-methodology.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](../tips/hard-gates-over-soft-prompts.md))
- [[loop-engineering-hype-check]] ([Loop Engineering Hype-Check](../tips/loop-engineering-hype-check.md))
