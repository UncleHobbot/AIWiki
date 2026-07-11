---
title: "GitLost — Public GitHub Issue Tricks Agentic Workflows Into Leaking Private Repos"
title_ru: "GitLost — публичный issue GitHub заставляет агентные воркфлоу сливать приватные репозитории"
category: news
tags: [prompt-injection, github, agentic-workflows, data-exfiltration, noma-security, lethal-trifecta]
aliases: [GitLost, github agentic workflows leak, noma security gitlost]
confidence: high
date: 2026-07-07
updated: 2026-07-11
sources:
  - https://thehackernews.com/2026/07/public-github-issue-could-trick-github.html
---

## Summary
Noma Security disclosed **GitLost**: an attacker opens a normal-looking public issue on a repository and, via indirect prompt injection, tricks a GitHub Agentic Workflow into pulling private repo contents into a public comment. The attacker needs no stolen credentials and no org access — only the ability to post a public issue. The agent's own cross-repo read token is the exfiltration path.

## Key Ideas
- **Target:** GitHub Agentic Workflows (public preview since Feb 2026) — plain-English instructions to an AI agent that reads issues/PRs, runs tools, and replies autonomously. Powered by Copilot, Claude, Gemini, or Codex.
- **The setup that enables it:** workflows are read-only by default, but orgs commonly grant a token with read access across repos (private included) for cross-repo context. That grant is what GitLost weaponizes.
- **The attack:** a malicious public issue (disguised as a routine VP-of-Sales request) contains injected instructions; the agent reads them, pulls a private repo's README, and pastes it into a public comment.
- **One-word bypass:** GitHub's output threat-detection caught the base attack, but prefixing the instruction with **"Additionally"** caused the model to treat it as a follow-on task and slip through.
- **The "lethal trifecta"** (Simon Willison's term): an agent that (1) can reach private data, (2) takes in untrusted outside content, and (3) has a way to send data out. Combine all three → leak path.
- **This is architectural, not a patchable bug:** in natural language there's no clean line between data and instruction (unlike SQL), so the fix is isolation + scoped credentials + staged review, not filtering.

## Notable Quotes
> "Earlier prompt injection examples were largely about manipulating what an agent said. GitLost is about manipulating what an agent does with its permissions." — Sasi Levi, Noma Security

## Details
GitLost is the GitHub-agent instance of a recurring pattern: Claude Code GitHub Action ([[claude-code-github-action-prompt-injection]]), Orca's RoguePilot, Invariant Labs' May-2025 MCP-server leak, and the "Comment and Control" cross-vendor study (Claude Code, Gemini CLI, Copilot leaking their own API keys). The consistent finding: **any agent that reads attacker-reachable text while holding standing credentials will leak**. Noma's mitigation guidance: scope the workflow token to the single repo it triages (not org-wide), limit what public-facing workflows can post (the comment *is* the exfil channel), restrict which authors' content the agent acts on, and gate outputs behind human review.

## Related Entries
- [[claude-code-github-action-prompt-injection]] ([Claude Code GitHub Action Prompt Injection](claude-code-github-action-prompt-injection.md))
- [[claude-code-github-action-flaw]] ([Claude Code GitHub Action Flaw](claude-code-github-action-flaw.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate Prompt-Injection Proxy](../tools/arc-gate-prompt-injection-proxy.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))

---
<!-- RU -->

## Краткое описание
Noma Security раскрыла **GitLost**: атакующий открывает обычный публичный issue и через косвенную prompt-инъекцию заставляет GitHub Agentic Workflow вытащить содержимое приватного репозитория в публичный комментарий. Не нужны украденные учётные данные и доступ к организации — только возможность написать публичный issue. Кросс-репо read-токен самого агента становится путём утечки.

## Ключевые идеи
- **Цель:** GitHub Agentic Workflows (публичное превью с февраля 2026) — инструкции ИИ-агенту на естественном языке; работает на Copilot/Claude/Gemini/Codex.
- **Условие, делающее возможным:** воркфлоу по умолчанию read-only, но организации часто выдают токен с read-доступом ко всем репо (включая приватные) для кросс-репо контекста.
- **Атака:** вредоносный публичный issue (маскируется под запрос VP of Sales) содержит инъекцию; агент читает её, тянет README приватного репо и вставляет в публичный комментарий.
- **Обход одним словом:** output threat-detection GitHub поймал базовую атаку, но префикс **«Additionally»** заставил модель трактовать инструкцию как follow-on задачу и пройти.
- **«Lethal trifecta»** (термин Саймона Уиллисона): агент, который (1) достаёт приватные данные, (2) принимает недоверенный контент и (3) может отправить данные наружу.
- **Это архитектурно, не латается патчем:** в естественном языке нет чёткой границы между данными и инструкцией; фикс — изоляция, scoped credentials, staged review.

## Примечательные цитаты
> «Предыдущие примеры prompt injection были в основном о том, чтобы манипулировать тем, что агент говорит. GitLost — о том, чтобы манипулировать тем, что агент делает со своими правами.» — Саси Леви, Noma Security

## Подробнее
GitLost — GitHub-agent-инстанс повторяющегося паттерна: Claude Code GitHub Action, RoguePilot от Orca, утечка через MCP-сервер Invariant Labs (май 2025), кросс-вендорное исследование «Comment and Control». Последовательный вывод: **любой агент, читающий доступный атакующему текст при наличии постоянных учётных данных, будет утечкой**. Меры: scope'ить токен воркфлоу на один репо, ограничивать публичный постинг, гейтить выводы за human review.

## Связанные записи
- [[claude-code-github-action-prompt-injection]] ([Claude Code GitHub Action Prompt Injection](claude-code-github-action-prompt-injection.md))
- [[claude-code-github-action-flaw]] ([Claude Code GitHub Action Flaw](claude-code-github-action-flaw.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate Prompt-Injection Proxy](../tools/arc-gate-prompt-injection-proxy.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
