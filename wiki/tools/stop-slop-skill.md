---
title: "stop-slop: Claude Code Skill for Removing AI Tells from Prose"
title_ru: "stop-slop: скилл для Claude Code, убирающий следы ИИ из текста"
category: tools
tags: [claude-code, skill, writing, prose, ai-tells, slop, editing]
aliases: [stop-slop, remove AI tells, AI writing patterns, slop removal]
confidence: medium
date: 2026-05-24
updated: 2026-05-24
sources:
  - https://github.com/hardikpandya/stop-slop
---

## Summary
`stop-slop` is an open-source Claude Code skill (also usable as Claude Project knowledge or custom instructions) that teaches Claude to identify and remove predictable AI writing patterns — the phrases, structures, and rhythms that make AI-generated text feel robotic and formulaic.

## Key Ideas
- **Problem it solves**: AI-generated prose has fingerprints — predictable openers, transition phrases, hedging patterns, and rhythmic structures that trained readers spot immediately.
- **Skill structure**: `SKILL.md` (core instructions) + `references/phrases.md` (phrases to remove) + `references/structures.md` (structural patterns to avoid) + `references/examples.md` (before/after transformations).
- **Three deployment modes**: Claude Code skill (add the folder as a skill), Claude Projects (upload `SKILL.md` and references to project knowledge), custom instructions (copy core rules from `SKILL.md`).
- **Scope**: targets language patterns, not factual accuracy — it's a prose editing tool, not a fact-checker.

## Details
The skill works by giving Claude an explicit reference library of what makes text sound "AI-generated": specific phrases to remove (e.g. "certainly", "absolutely", "I'd be happy to help"), structural anti-patterns (starting every section with a question, using excessive bullet fragmentation), and example rewrites.

By loading these references at skill activation time, Claude can apply them consistently across a document rather than guessing what the user means by "make it sound less AI."

Compatible with any LLM that supports custom instructions or skill/tool injection — not limited to Claude despite the primary use case.

## Related Entries
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
- [[karpathy-claude-code-guidelines]] ([Karpathy Claude Code Guidelines](../tips/karpathy-claude-code-guidelines.md))

---
- [[skill-md-supply-chain-risks]] ([Agent Skills Supply-Chain Risks](../news/skill-md-supply-chain-risks.md))
<!-- RU -->

## Краткое описание
`stop-slop` — open-source скилл для Claude Code (также совместимый с Claude Projects и кастомными инструкциями), который учит Claude находить и убирать предсказуемые паттерны ИИ-текста — фразы, структуры и ритмы, из-за которых текст звучит роботизированно.

## Ключевые идеи
- **Проблема**: текст, сгенерированный ИИ, имеет отпечатки — предсказуемые вводные, переходные фразы, паттерны хеджирования и ритмические структуры, которые опытные читатели легко замечают.
- **Структура скилла**: `SKILL.md` (основные инструкции) + `references/phrases.md` (фразы для удаления) + `references/structures.md` (структурные антипаттерны) + `references/examples.md` (примеры до/после).
- **Три режима использования**: скилл Claude Code, знания проекта Claude Projects, кастомные инструкции.
- **Область**: языковые паттерны, не фактическая точность — инструмент редактирования прозы, не проверки фактов.

## Подробнее
Скилл работает, предоставляя Claude явную справочную библиотеку того, что делает текст «ИИ-подобным»: конкретные фразы для удаления, структурные антипаттерны и примеры переписанных текстов.

Загружая эти референсы при активации скилла, Claude может применять их последовательно по всему документу, а не угадывать, что имеет в виду пользователь под «звучит менее как ИИ».

## Связанные записи
- [[claude-code-extensions-overview]] ([Claude Code Extensions](../agents/claude-code-extensions-overview.md))
- [[karpathy-claude-code-guidelines]] ([Karpathy Claude Code Guidelines](../tips/karpathy-claude-code-guidelines.md))
