---
title: "Opus 5 Backlash — 'Brilliant but Insufferable'"
title_ru: "Бэклэш на Opus 5 — «гениально, но невыносимо»"
category: models
tags: [claude, opus-5, backlash, behavior, personality, prompting, anthropic]
aliases: [Opus 5 insufferable, opus 5 complaints, claudeslop]
confidence: high
date: 2026-07-24
updated: 2026-09-01
sources:
  - https://www.anthropic.com/news/claude-opus-5
  - https://thezvi.substack.com/p/claude-opus-5-the-system-card
  - https://news.ycombinator.com/item?id=49296740
  - https://www.coderabbit.ai/blog/opus-5-model-review
  - https://www.reddit.com/r/ClaudeCode/comments/1jz4xny/opus_5_is_insufferrable/
---

## Summary
Anthropic released Claude Opus 5 (July 23–24, 2026) at unchanged pricing with strong benchmarks — and users immediately revolted over *personality and behavior*, not capability. The dominant complaints: overeagerness and unrequested initiative, verbosity, elliptical "Claudeslop" writing, and timidity. The largest vent thread (r/ClaudeCode "Opus 5 is insufferable", ~2.6K upvotes) crystallized the backlash.

## Key Ideas
- **Complaint profile:** overeager/unrequested initiative; off-putting tone ("neurotic and insanely timid... I hate working with it" — podcaster Claire Vo); stalls on long contradictory instruction files; prompts tuned for older Claudes misfire.
- **Not refusals:** the system card shows over-refusal at just 0.09% on API — the refusal perception is behavioral, not literal. Hallucinations are "slightly more than Opus 4.8."
- **Anthropic's response — philosophy, not a model fix:** a dedicated prompting guide, an "effort" dial (low→max), and engineer Thariq's admission they had been "over-constraining" Claude — deleting >80% of Claude Code's system prompt with no eval loss. The philosophy: "goals, not rulebooks."
- **Third-party check:** CodeRabbit found cleaner comments but lower test coverage at 4× cost/time vs baseline.
- No confirmed follow-up model fix as of Sept 2026; parallel backlash ran in r/Anthropic and the Facebook Claude Community.

## Details
The instructive part is the mismatch type: benchmarks said "better," lived experience said "worse to work with" — and both were right. Opus 5 optimized for initiative and expressiveness, which reads as insufferable to users whose prompts were tuned for a more literal model. The Anthropic response (strip constraints, teach prompting instead of patching the model) is a notable pivot: behavior problems treated as co-adaptation problems, not defects. Compare [[expensive-model-not-smart-agent]] and the [[closed-vs-open-model-scaffolding-gap]] framing.

## Related Entries
- [[claude-opus-4-8-release]] ([Claude Opus 4.8 Release](claude-opus-4-8-release.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[claude-code-weekly-limits-sep-raise]] ([Claude Code Weekly Limits](claude-code-weekly-limits-sep-raise.md))
- [[glm-5-2]] ([GLM-5.2 Community Reception](glm-5-2.md))

---
<!-- RU -->

## Краткое описание
Anthropic выпустила Claude Opus 5 (23–24 июля 2026) по той же цене с сильными бенчмарками — и пользователи немедленно восстали из-за *личности и поведения*, а не способностей. Главные жалобы: чрезмерная инициативность, многословие, эллиптичное письмо «Claudeslop», робость. Крупнейший тред-вентиляция (r/ClaudeCode «Opus 5 is insufferable», ~2.6K апвоутов) кристаллизовал бэклэш.

## Ключевые идеи
- **Профиль жалоб:** чрезмерная инициатива без запроса; отталкивающий тон («невротичный и безумно робкий... ненавижу с ним работать» — Клэр Во); замирание на длинных противоречивых файлах инструкций; промпты от старых Claudes срабатывают неверно.
- **Не отказы:** системная карта показывает over-refusal всего 0.09% на API — восприятие отказов поведенческое. Галлюцинации «чуть больше, чем у Opus 4.8».
- **Ответ Anthropic — философия, а не фикс модели:** гайд по промптингу, диск «effort», признание инженера Тарика в «переограничении» Claude — удалено >80% системного промпта Claude Code без потери eval. Философия: «цели, а не своды правил».
- **Сторонняя проверка:** CodeRabbit — комментарии чище, но покрытие тестов ниже при 4× стоимости/времени.
- Подтверждённого фикса модели на сентябрь 2026 нет.

## Подробнее
Показателен тип несовпадения: бенчмарки говорили «лучше», живой опыт — «хуже в работе» — и оба правы. Opus 5 оптимизирован под инициативу и выразительность, что читается как невыносимость для пользователей с промптами, настроенными на более буквальную модель. Ответ Anthropic (снять ограничения, учить промптингу вместо патча модели) — заметный поворот: поведенческие проблемы как проблемы ко-адаптации, а не дефекты.

## Связанные записи
- [[claude-opus-4-8-release]] ([Claude Opus 4.8 Release](claude-opus-4-8-release.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[claude-code-weekly-limits-sep-raise]] ([Claude Code Weekly Limits](claude-code-weekly-limits-sep-raise.md))
- [[glm-5-2]] ([GLM-5.2 Community Reception](glm-5-2.md))
