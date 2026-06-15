---
title: "Investigate-Then-Handoff: A Workflow for Better Coding-Agent Plans"
title_ru: "Сначала исследование, потом передача: workflow для лучших планов coding agent"
category: tips
tags: [claude-code, planning, context-management, workflow, prompting]
confidence: low
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1u5jm9f/better_codingagent_results_start_before_the_plan/
---

## Summary
Instead of asking a coding agent to produce a plan and then correcting it, ask it to investigate the problem and come back with questions — work through constraints together, then save the agreed decisions as a short handoff document for a fresh implementation session.

## Key Ideas
- Old workflow: describe a task, request a plan, correct the plan, watch the implementation — but this means reviewing "polished assumptions" rather than testing whether the agent actually understood the problem.
- New workflow: ask the agent to investigate first and return with clarifying questions, not a finished plan.
- Work through constraints and possible approaches together before committing to decisions.
- Save the agreed decisions as a short, explicit handoff document.
- Start implementation in a **fresh session** using that handoff — long conversations preserve bad assumptions as readily as good ones.
- A fresh implementation agent, working from a compressed and challenged set of decisions, has less noise and fewer reasons to improvise off-spec.

## Details
The core insight is that a polished-looking plan can mask a misunderstanding of the actual problem — an agent that confidently proposes a multi-step plan may have skipped the step of genuinely understanding constraints. By flipping the order (investigate → ask questions → human and agent jointly decide → write a short handoff → fresh session implements), the human's highest-leverage work becomes framing the problem and testing assumptions, rather than line-editing a plan document.

The "fresh session for implementation" part is notable on its own: it deliberately discards the investigation conversation's accumulated context (including any bad assumptions or dead-end reasoning) and replaces it with a compact, vetted summary — similar in spirit to context-compaction best practices discussed elsewhere in this wiki, but applied proactively rather than reactively. This is a single Reddit user's reported workflow (Tier 3, low confidence) but the pattern — separate "understanding" and "doing" phases with a deliberate context reset between them — aligns with broader spec-driven development approaches (e.g. GitHub Spec-Kit's constitution → spec → plan → tasks → implement pipeline).

## Related Entries
- [[github-spec-kit]] ([GitHub Spec-Kit: Spec-Driven Development Toolkit](../tools/github-spec-kit.md))
- [[claude-usage-limits-token-management]] ([10 Ways to Stop Hitting Claude's Usage Limits](../tips/claude-usage-limits-token-management.md))

---
<!-- RU -->

## Краткое описание
Вместо того чтобы просить coding agent сразу составить план, а потом исправлять его, лучше попросить агента сначала исследовать задачу и вернуться с вопросами — совместно проработать ограничения, а затем сохранить согласованные решения как короткий документ передачи (handoff) для свежей сессии реализации.

## Ключевые идеи
- Старый workflow: описать задачу, запросить план, исправить план, наблюдать реализацию — но это означает рецензирование "отполированных предположений", а не проверку, действительно ли агент понял задачу.
- Новый workflow: попросить агента сначала исследовать и вернуться с уточняющими вопросами, а не с готовым планом.
- Совместно проработать ограничения и возможные подходы перед принятием решений.
- Сохранить согласованные решения как короткий, явный документ передачи (handoff).
- Начать реализацию в **новой сессии**, используя этот handoff — длинные разговоры сохраняют плохие предположения так же легко, как и хорошие.
- Свежий агент реализации, работающий со сжатым и проверенным набором решений, имеет меньше "шума" и меньше причин импровизировать вне спецификации.

## Подробнее
Главная идея в том, что красиво оформленный план может скрывать непонимание реальной задачи — агент, уверенно предлагающий многошаговый план, мог пропустить этап действительного понимания ограничений. Поменяв порядок (исследование → вопросы → совместное решение человека и агента → короткий handoff → реализация в новой сессии), человек переключается с построчного редактирования плана на постановку задачи и проверку предположений — это становится его наиболее ценной работой.

Часть про "новую сессию для реализации" примечательна сама по себе: она намеренно отбрасывает накопленный контекст исследовательского разговора (включая любые неверные предположения или тупиковые рассуждения) и заменяет его компактным, проверенным резюме — по духу похоже на практики работы с context-compaction, описанные в других записях этой wiki, но применяется проактивно, а не реактивно. Это рабочий метод одного пользователя Reddit (tier 3, низкая достоверность), но сам паттерн — разделение фаз "понимания" и "выполнения" с намеренным сбросом контекста между ними — согласуется с более широкими подходами spec-driven development (например, пайплайн GitHub Spec-Kit: constitution → spec → plan → tasks → implement).

## Связанные записи
- [[github-spec-kit]] ([GitHub Spec-Kit: Spec-Driven Development Toolkit](../tools/github-spec-kit.md))
- [[claude-usage-limits-token-management]] ([10 Ways to Stop Hitting Claude's Usage Limits](../tips/claude-usage-limits-token-management.md))
