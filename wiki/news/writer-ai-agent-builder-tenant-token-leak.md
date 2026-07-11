---
title: "Writer AI Agent Builder Flaw — Session Token Leak Across Tenants"
title_ru: "Уязвимость Writer AI Agent Builder — утечка токенов сессии между тенантами"
category: news
tags: [writer-ai, multi-tenant, session-token, agent-builder, tenable, idor, security]
aliases: [Writer AI agent preview leak, writer ai tenant isolation]
confidence: high
date: 2026-07-09
updated: 2026-07-11
sources:
  - https://thehackernews.com/2026/07/writer-ai-flaw-could-let-agent-previews.html
---

## Summary
Tenable disclosed a flaw in Writer's **Agent Builder**: agent previews were accessible via unguessable-but-enumerable URLs that leaked session tokens across tenants. An attacker could share a preview link; when a victim in another tenant opened it, the attacker captured their session token — a cross-tenant identity boundary break in a platform where agents increasingly hold privileged tool access.

## Key Ideas
- **Surface:** Writer's Agent Builder preview feature — shareable links to view/test an agent.
- **Flaw:** the preview URL leaked the viewer's session token; the token was accessible to the agent's owner even if the viewer was in a *different tenant*.
- **Attack:** attacker creates an agent, generates a preview link, sends it to a victim in another org; when the victim opens it, the attacker gets the victim's session token.
- **Impact:** cross-tenant session hijack — an account-boundary break, not just a within-tenant privilege issue.
- Fixed by Writer after Tenable's responsible disclosure.
- **Why it matters for agents:** as agents gain tool/MCP access to business systems, a leaked session token isn't just "view as user" — it's "run the user's agent and its tools."

## Details
This is a classic multi-tenant isolation failure (IDOR-adjacent: the preview endpoint didn't enforce tenant boundaries on the session token), but the blast radius is larger in an agent platform because agents carry tool credentials. The pattern reinforces a lesson relevant to anyone building agent infrastructure: preview/share features are an under-audited attack surface, and tenant isolation must be enforced at the session-token layer, not assumed from URL unguessability.

## Related Entries
- [[gitlost-github-agentic-workflow-leak]] ([GitLost — GitHub Agentic Workflow Leak](gitlost-github-agentic-workflow-leak.md))
- [[bioshocking-ai-browser-credential-leak]] ([BioShocking — AI Browser Credential Leak](bioshocking-ai-browser-credential-leak.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))

---
<!-- RU -->

## Краткое описание
Tenable раскрыла уязвимость в **Agent Builder** от Writer: превью агентов были доступны по URL, который утекал токен сессии между тенантами. Атакующий мог поделиться ссылкой-превью; когда жертва из другого тенанта открывала её, атакующий получал её токен сессии — нарушение границы идентичности между тенантами.

## Ключевые идеи
- **Поверхность:** функция превью Agent Builder — sharable-ссылки для просмотра/теста агента.
- **Уязвимость:** URL превью утекал токен зрителя; он был доступен владельцу агента, даже если зритель — из *другого тенанта*.
- **Атака:** атакующий создаёт агента, генерирует ссылку, отправляет жертве из другого тенанта; при открытии — захват токена.
- **Влияние:** межтенантный перехват сессии — нарушение границ аккаунта.
- Исправлено Writer после responsible disclosure Tenable.
- **Почему важно для агентов:** токен сессии в агентской платформе — не просто «видеть как пользователь», а «запускать агента пользователя и его инструменты».

## Подробнее
Это классический сбой изоляции мультитенанта (близко к IDOR), но радиус поражения больше, потому что агенты несут инструментальные учётные данные. Паттерн: preview/share-функции — малоаудитируемая поверхность атаки; изоляция тенантов должна обеспечиваться на уровне токена сессии, а не предполагаться из «угадываемости» URL.

## Связанные записи
- [[gitlost-github-agentic-workflow-leak]] ([GitLost — GitHub Agentic Workflow Leak](gitlost-github-agentic-workflow-leak.md))
- [[bioshocking-ai-browser-credential-leak]] ([BioShocking — AI Browser Credential Leak](bioshocking-ai-browser-credential-leak.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
