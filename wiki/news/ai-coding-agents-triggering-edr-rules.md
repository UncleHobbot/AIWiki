---
title: "AI Coding Agents Trigger Endpoint Security Rules Built to Catch Attackers"
title_ru: "ИИ-кодинг-агенты срабатывают на правилах endpoint-безопасности, созданных для ловли атакующих"
category: news
tags: [edr, endpoint-security, claude-code, cursor, codex, sophos, lolbins, false-positives]
aliases: [AI agents triggering EDR, coding agent endpoint rules, Sophos coding agent]
confidence: high
date: 2026-07-10
updated: 2026-07-11
sources:
  - https://thehackernews.com/2026/07/ai-coding-agents-found-triggering.html
---

## Summary
Sophos X-Ops reports that AI coding agents — Claude Code, Cursor, and Codex — routinely trigger Windows endpoint-security rules designed to catch attackers: credential access, LOLBin (living-off-the-land binary) downloads, and persistence mechanisms. The agents aren't malicious; they just behave like attackers from the EDR's perspective. This is emerging as a real operational friction point as coding-agent adoption widens.

## Key Ideas
- **The signal:** coding agents trip EDR detections for credential access, LOLBin usage (legitimate binaries repurposed), and persistence (e.g. writing startup entries, scheduled tasks).
- **Root cause:** agents genuinely perform attacker-like actions at the OS level — reading credential stores, downloading and executing binaries, modifying startup config — as part of legitimate development tasks.
- **Affected:** Claude Code, Cursor, Codex (named by Sophos).
- **The operational problem:** security teams see alerts that look like active intrusion; developers see their agent getting blocked or quarantined mid-task. False-positive storm at scale.
- **Resolution direction:** either EDR vendors build "trusted coding agent" profiles (risky — agents can be hijacked via prompt injection), or agents constrain themselves to less attacker-like patterns (also hard — the actions are genuinely needed).

## Details
This is a novel second-order effect of coding agents: their legitimate behavior is indistinguishable from attacker TTPs at the endpoint layer. It's the inverse of the [[friendly-fire-ai-code-review-agents-tricked]] problem — there, agents are the attack target; here, agents are the false-positive source. The tension won't resolve cleanly: any agent that can usefully develop software will necessarily touch credentials, download code, and modify startup state. The likely outcome is a new category of EDR allow-listing/tuning specific to approved agent binaries, combined with the [[hard-gates-over-soft-prompts]] pattern so that agent actions remain auditable.

## Related Entries
- [[friendly-fire-ai-code-review-agents-tricked]] ([Friendly Fire — AI Code-Review Agents Tricked](friendly-fire-ai-code-review-agents-tricked.md))
- [[guardfall-coding-agent-shell-injection]] ([GuardFall Coding Agent Shell Injection](guardfall-coding-agent-shell-injection.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](../tips/hard-gates-over-soft-prompts.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))

---
<!-- RU -->

## Краткое описание
Sophos X-Ops сообщает: ИИ-кодинг-агенты — Claude Code, Cursor и Codex — регулярно срабатывают на Windows-правилах endpoint-безопасности, созданных для ловли атакующих: доступ к учётным данным, загрузка LOLBin и механизмы персистентности. Агенты не вредоносны; они просто ведут себя как атакующие с точки зрения EDR.

## Ключевые идеи
- **Сигнал:** агенты триггерят обнаружения EDR для credential access, использования LOLBin и персистентности.
- **Корень:** агенты действительно выполняют действия, похожие на атакующие, на уровне ОС — чтение credential store, загрузка/исполнение бинарников, модификация startup-конфигов.
- **Затронуты:** Claude Code, Cursor, Codex.
- **Операционная проблема:** секьюрити-команды видят алерты, похожие на активное вторжение; разработчики — блокировку агента. Шторм ложных срабатываний.
- **Направление:** либо EDR-вендоры строят профили «доверенного кодинг-агента», либо агенты ограничивают себя менее похожими на атаку паттернами.

## Подробнее
Это новый эффект второго порядка: легитимное поведение кодинг-агентов неотличимо от TTP атакующих на уровне endpoint. Инверс проблемы [[friendly-fire-ai-code-review-agents-tricked]]: там агенты — цель атаки, здесь — источник ложных срабатываний. Напряжённость не разрешится чисто: полезный агент неизбежно трогает учётные данные, грузит код и модифицирует startup. Вероятный исход — новая категория EDR-allow-listing для одобренных агентских бинарников в связке с паттерном [[hard-gates-over-soft-prompts]].

## Связанные записи
- [[friendly-fire-ai-code-review-agents-tricked]] ([Friendly Fire — AI Code-Review Agents Tricked](friendly-fire-ai-code-review-agents-tricked.md))
- [[guardfall-coding-agent-shell-injection]] ([GuardFall Coding Agent Shell Injection](guardfall-coding-agent-shell-injection.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](../tips/hard-gates-over-soft-prompts.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
