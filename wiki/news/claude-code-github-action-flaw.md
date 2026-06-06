---
title: "Claude Code GitHub Action Flaw: One Malicious Issue to Repo Takeover"
title_ru: "Уязвимость Claude Code GitHub Action: один вредоносный issue для захвата репозитория"
category: news
tags: [security, claude-code, github, vulnerability, anthropic, prompt-injection, supply-chain]
date: 2026-06-06
updated: 2026-06-06
sources:
  - https://thehackernews.com/2026/06/claude-code-github-action-flaw-let-one.html
  - https://thehackernews.com/2026/06/agentic-ai-is-transforming-defense-but.html
---

## Summary
Security researcher RyotaK (GMO Flatt Security) found a critical flaw in Anthropic's Claude Code GitHub Action that allowed full repository takeover via a single malicious GitHub issue. The same vulnerable workflow was used by Anthropic's own action repo, meaning a successful attack could have poisoned the upstream action and propagated malicious code downstream.

## Key Ideas
- The trigger check had a bypass: it waved through any actor whose name ended in `[bot]`, since GitHub Apps were assumed trusted. Anyone can register a GitHub App, install it on their repo, and use its token to open issues on any public repository.
- From there, indirect prompt injection planted instructions inside issue content. Claude was tricked into reading `/proc/self/environ` and exfiltrating OIDC credentials back into the issue body.
- Stealing the OIDC token let the attacker replay it for write access to the target's code, issues, and workflows. Aimed at the `claude-code-action` repo itself, it could poison the action that downstream projects pull.
- Anthropic rated the issues 7.8 under CVSS v4.0, paid a bug bounty, and patched within four days. Fixes are in claude-code-action v1.0.94.
- This follows a real supply-chain hit in February where prompt injection against Cline's action triage workflow stole an npm publish token and pushed unauthorized `cline@2.3.0`.

## Details
RyotaK reported around 50 separate ways to bypass Claude Code's permission system. The core issue: agent mode lacked the human-actor check that tag mode had. A softer route existed too — Anthropic's own example workflow shipped with `allowed_non_write_users: "*"`, letting anyone trigger it. Many repos copied that example and inherited the hole. A race-condition path also allowed editing a trusted user's issue before Claude read it, injecting a payload as "trusted" input.

The fix: update to claude-code-action v1.0.94 or later, audit workflows that let non-write users trigger Claude, and remove tools/permissions that can be used for exfiltration.

## Related Entries
- [[claude-code-github-action-prompt-injection]] ([Claude Code GitHub Action: Prompt Injection Flaw](../news/claude-code-github-action-prompt-injection.md))
- [[claude-code-remote-system-prompt-injection]] ([Claude Code Remote System Prompt Injection](../news/claude-code-remote-system-prompt-injection.md))
- [[mythos-aisi-cyber-capability-2026]] ([Mythos Cyber Capability](../news/mythos-aisi-cyber-capability-2026.md))

---
<!-- RU -->

## Краткое описание
Исследователь безопасности RyotaK (GMO Flatt Security) обнаружил критическую уязвимость в GitHub Action Anthropic Claude Code, позволяющую полный захват репозитория через один вредоносный issue. Та же уязвимая конфигурация использовалась в собственном репозитории Action Anthropic, что означало возможность отравления upstream-действия и распространения вредоносного кода на все зависимые проекты.

## Ключевые идеи
- Проверка триггера имела обход: любой актёр с именем, оканчивающимся на `[bot]`, пропускался автоматически. Любой может зарегистрировать GitHub App и использовать её токен для открытия issues в публичных репозиториях.
- Косвенная prompt-инъекция позволяла заставить Claude прочитать `/proc/self/environ` и эксфильтрировать OIDC-учётные данные обратно в тело issue.
- Краденный OIDC-токен давал доступ на запись к коду, issues и workflows целевого репозитория. При атаке на сам `claude-code-action` можно было отравить действие, загружаемое downstream-проектами.
- Anthropic оценила уязвимость в 7.8 по CVSS v4.0, выплатила баг-баунти и устранила проблему за четыре дня. Исправления в claude-code-action v1.0.94.
- Это следует за реальной атакой на цепочку поставок в феврале, когда prompt-инъекция в Cline похитила npm publish-токен.

## Подробнее
RyotaK сообщил около 50 различных способов обхода системы разрешений Claude Code. Основная проблема: режим агента не имел проверки человеческого актёра, которая была в режиме тегов. Существовал и более мягкий маршрут — собственный пример Anthropic поставлялся с `allowed_non_write_users: "*"`. Многие репозитории скопировали этот пример и унаследовали уязвимость.

## Связанные записи
- [[claude-code-github-action-prompt-injection]] ([Claude Code GitHub Action: Prompt Injection Flaw](../news/claude-code-github-action-prompt-injection.md))
- [[claude-code-remote-system-prompt-injection]] ([Claude Code Remote System Prompt Injection](../news/claude-code-remote-system-prompt-injection.md))
- [[mythos-aisi-cyber-capability-2026]] ([Mythos Cyber Capability](../news/mythos-aisi-cyber-capability-2026.md))
