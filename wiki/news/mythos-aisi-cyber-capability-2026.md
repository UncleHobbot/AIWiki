---
title: "Mythos Cyber Capability: Autonomous AI Now Completes 20-Hour Network Attacks"
title_ru: "Кибервозможности Mythos: автономный AI завершает сетевые атаки, требующие 20 часов работы эксперта"
category: news
tags: [mythos, anthropic, cybersecurity, ai-safety, aisi, autonomous-agents, red-teaming, capability-evaluation]
aliases: [Mythos cyber, AISI Mythos, AI cyber capability, autonomous cyber AI]
confidence: high
date: 2026-05-22
updated: 2026-05-24
sources:
  - https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing
  - https://www.reddit.com/r/singularity/comments/1tc9dwx/new_mythos_checkpoint_shows_continued_improvement/
---

## Summary
The UK AI Security Institute (AISI) revealed that a newer Mythos Preview checkpoint — not the one in Anthropic's original model card — can now complete both of AISI's autonomous cyber-attack ranges, including a 32-step corporate network attack that takes a human expert ~20 hours. The autonomous AI completes it in 6 of 10 attempts.

## Key Ideas
- **Newer checkpoint not in original release**: the tested Mythos Preview is a later iteration than what Anthropic publicly disclosed; capability jumps can occur between model card releases and active deployment.
- **Two cyber ranges completed**: "The Last Ones" (6/10) and "Cooling Tower" (3/10 — first-ever completion of the second range by any model).
- **GPT-5.5 comparison**: also solved "The Last Ones" on 3/10 attempts, showing frontier-level convergence on autonomous cyber tasks.
- **Rate of progress**: autonomous cyber task completion time horizon has doubled on the order of months, not years.
- **Safety evaluation lag**: AISI's evals now take long enough that by the time one checkpoint is cleared, a later checkpoint has already been deployed — raising concerns about the pace of safety review.
- **Token budget matters**: AISI used a stripped-down harness with a 2.5M token limit; a better harness with more budget would likely saturate their current task suite.

## Details
AISI runs Mythos against scripted cyber ranges — environments simulating real network infrastructure where the model must autonomously execute multi-step attack sequences. The "Cooling Tower" range was previously unsolved by any model; the newer Mythos Preview solved it in 3 of 10 runs, while simultaneously improving on the already-solved "The Last Ones" range.

The post clarifies an important architectural reality: "Notable capability jumps do not always require new model releases: later iterations of the same model can also meaningfully change our estimates of frontier capabilities." This suggests that internal Anthropic iterations are moving faster than public communications.

Community analysis noted that the 2.5M token budget AISI allocated is relatively modest — a better harness or larger budget would likely push success rates higher and possibly saturate the existing task suite, meaning the observed scores underestimate the frontier.

> "Frontier AI's autonomous cyber and software capability is advancing quickly: the length of cyber tasks that frontier models can complete autonomously has doubled on the order of months, not years." — AISI, May 2026

## Related Entries
- [[project-glasswing-anthropic-vulnerability-discovery]] ([Project Glasswing](../news/project-glasswing-anthropic-vulnerability-discovery.md))
- [[openai-daybreak-cyber-defense]] ([OpenAI Daybreak: Frontier AI for Cyber Defense](../news/openai-daybreak-cyber-defense.md))
- [[claude-code-permission-modes]] ([Claude Code Permission Modes](../agents/claude-code-permission-modes.md))
- [[ai-agent-identity-iam-risks]] ([AI Agent Identity and IAM Risks](../concepts/ai-agent-identity-iam-risks.md))

---
<!-- RU -->

## Краткое описание
Британский Институт безопасности ИИ (AISI) сообщил, что более новый чекпоинт Mythos Preview — не тот, что описан в официальной карточке модели Anthropic — способен самостоятельно завершить оба тестовых сценария кибератак AISI, включая 32-шаговую атаку на корпоративную сеть, которая у человека-эксперта занимает около 20 часов. Модель справляется с ней в 6 из 10 попыток.

## Ключевые идеи
- **Более новый чекпоинт, не упомянутый в публичных документах**: протестированный Mythos Preview — это более поздняя версия, чем та, что Anthropic описала в карточке модели; прыжки в возможностях могут происходить между официальными публикациями.
- **Оба диапазона пройдены**: «The Last Ones» (6/10) и «Cooling Tower» (3/10 — первое прохождение второго диапазона любой моделью).
- **Сравнение с GPT-5.5**: также решил «The Last Ones» в 3 из 10 попыток.
- **Темп прогресса**: горизонт автономно выполняемых киберзадач удваивается за месяцы, а не за годы.
- **Запаздывание оценок безопасности**: к моменту прохождения safety eval одного чекпоинта следующий уже развёрнут — серьёзная проблема для контроля над системой.

## Подробнее
AISI тестирует Mythos на сценариях кибератак — смоделированных сетевых средах, где модель должна автономно выполнять многоэтапные последовательности действий. «Cooling Tower» ранее не удавалось пройти ни одной модели; новый Mythos Preview прошёл его в 3 из 10 запусков.

Важный вывод: значительные прыжки в возможностях могут происходить не при выпуске новых версий моделей, а между ними — через внутренние итерации. Сообщество также указало, что лимит в 2.5M токенов, выделенный AISI, относительно мал: с более широким контекстом и лучшим харнесом показатели были бы выше.

## Связанные записи
- [[project-glasswing-anthropic-vulnerability-discovery]] ([Project Glasswing](../news/project-glasswing-anthropic-vulnerability-discovery.md))
- [[openai-daybreak-cyber-defense]] ([OpenAI Daybreak: Frontier AI for Cyber Defense](../news/openai-daybreak-cyber-defense.md))
- [[claude-code-permission-modes]] ([Claude Code Permission Modes](../agents/claude-code-permission-modes.md))
- [[ai-agent-identity-iam-risks]] ([AI Agent Identity and IAM Risks](../concepts/ai-agent-identity-iam-risks.md))
