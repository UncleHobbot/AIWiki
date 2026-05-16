---
title: "LLM-Assisted Coding: A Systems Perspective"
title_ru: "LLM-ассистированный кодинг: системная перспектива"
category: tips
tags: [llm, ai-coding, systems-thinking, xp, lean, toc, code-review, pull-requests]
updated: 2026-05-16
sources:
  - https://youtu.be/eEA0gJnWLh0
---

## Summary
Dragan Stepanović (principal engineer, known for "from code review to co-creation" pattern) applies systems thinking, XP, Theory of Constraints, and Lean lenses to understand why common AI coding workflows fail — and how to restructure them.

## Key Ideas
- **Pull requests become the bottleneck**: with AI generating code 10x faster, the PR review queue is the new constraint; the system analysis is the same as TOC applied to any production line.
- **Counterintuitive insights from each lens**: XP says pair programming increases throughput (counterintuitive); TOC says focusing on one bottleneck matters more than optimizing everything; Lean says limit WIP; each applies to AI-augmented teams.
- **From code review to co-creation**: Dragan's famous pattern — shift from asynchronous reviews to synchronous co-development; in the AI era, this means humans and AI agents collaborating in real time rather than AI generating PRs for humans to review.
- **The interest rate analogy**: stimulating/slowing an economy by adjusting rates is analogous to adjusting how much AI does — too much at once overheats the system (just as low rates fuel inflation); incremental injection is healthier.
- **Systems perspective, not tool perspective**: most AI coding discourse focuses on which tool is best; Dragan focuses on how teams and workflows adapt as a system.

## Video Notes
- [~3:00] Dragan was invited after Alberto Brandolini (creator of EventStorming) noticed his posts and suggested the talk — a serendipitous path.
- [~7:00] Four career-long interests connected by counterintuitiveness: XP, Theory of Constraints, Lean, systems thinking.
- [~10:00] Federal Reserve interest rate chart as an analogy for how to manage AI injection into development workflows.
- Talk from AI Agents Montreal meetup (2026-04-27), speaker based in Berlin.

## Related Entries
- [[xp-practices-ai-assisted-development]]
- [[acdc-agent-centric-development-cycle]]
- [[claude-code-workflows-best-practices]]

---
<!-- RU -->

## Краткое описание
Драган Степанович (principal-инженер, известный паттерном «от code review к co-creation») применяет системное мышление, XP, теорию ограничений и Lean для понимания того, почему типичные рабочие процессы AI-кодинга терпят неудачу — и как их реструктурировать.

## Ключевые идеи
- **Pull request становится узким местом**: когда AI генерирует код в 10 раз быстрее, очередь ревью PR — новое ограничение системы; системный анализ тот же, что TOC применяет к любой производственной линии.
- **Контринтуитивные озарения от каждой линзы**: XP говорит, что парное программирование увеличивает пропускную способность (контринтуитивно); TOC — что концентрация на одном узком месте важнее оптимизации всего; Lean — ограничивайте WIP; каждый принцип применим к командам, дополненным AI.
- **От code review к co-creation**: знаменитый паттерн Драгана — переход от асинхронного ревью к синхронной совместной разработке; в эпоху AI это означает совместную работу людей и AI-агентов в реальном времени, а не генерацию PR агентами для ревью людьми.
- **Аналогия с процентными ставками**: стимулирование/замедление экономики путём корректировки ставок аналогично регулированию того, сколько делает AI — слишком много сразу перегревает систему; инкрементальное введение здоровее.
- **Системная перспектива, а не перспектива инструментов**: большинство дискуссий об AI-кодинге сосредоточено на том, какой инструмент лучше; Драган сосредоточен на том, как команды и рабочие процессы адаптируются как система.

## Заметки по видео
- [~3:00] Драган был приглашён после того, как Альберто Брандолини (создатель EventStorming) заметил его посты и предложил выступить — путь через серендипность.
- [~7:00] Четыре карьерных интереса, объединённых контринтуитивностью: XP, теория ограничений, Lean, системное мышление.
- [~10:00] График ставки ФРС как аналогия управления объёмом AI-инъекций в рабочие процессы разработки.
- Доклад на AI Agents Montreal meetup (2026-04-27), спикер из Берлина.

## Связанные записи
- [[xp-practices-ai-assisted-development]]
- [[acdc-agent-centric-development-cycle]]
- [[claude-code-workflows-best-practices]]
