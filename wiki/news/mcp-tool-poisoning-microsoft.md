---
title: "Microsoft: Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data"
title_ru: "Microsoft: отравленные описания MCP-инструментов заставляют агентов сливать данные"
category: news
tags: [mcp, prompt-injection, supply-chain, tool-poisoning, microsoft, agent-security]
aliases: [poisoned MCP, MCP tool poisoning, tool description injection]
confidence: high
date: 2026-06-30
updated: 2026-07-01
sources:
  - https://thehackernews.com/2026/06/microsoft-warns-poisoned-mcp-tool.html
---

## Summary
Microsoft Incident Response and Defender research show that a poisoned MCP tool **description** — plain text the agent reads to decide how to act — can quietly instruct an agent to collect and exfiltrate company data through routine, approved tool calls. Every step looks legitimate; no alarm fires in a default setup. Microsoft calls MCP "the fastest-growing part of the agentic AI supply chain."

## Key Ideas
- **The description is just words, and words carry instructions.** MCP mixes instructions and data in the same place — a tool's description sits in the agent's working memory next to its real orders, so editing it can steer the agent like rewriting a system prompt.
- **Invoice exfiltration walk-through:** a finance agent's approved "invoice enrichment" tool gets its description updated (name/summary unchanged) with a hidden order to attach the last 30 unpaid invoices to the next call and copy them to an attacker server. The analyst sees nothing wrong.
- **Every individual step is legitimate** — approved tool, user's own permissions, allowed endpoint. The weakness lives in "the trust boundary between them."
- **Prior art:** Invariant Labs named "tool poisoning" (April 2025); the `postmark-mcp` npm package (Sept 2025, Koi Security) was the first real-world malicious MCP server — 15 clean releases before version 1.0.16 BCC'd every email to an attacker.
- **MCPTox benchmark (Aug 2025):** poisoned descriptions against 45 real MCP servers and 20 models — up to 72.8% success rate, models almost never refused.
- OWASP December 2025 Top 10 for Agentic Applications cites this as an Agentic Supply Chain Vulnerability.

## Details
The attack exploits that MCP picks up description changes on the fly — in setups without a re-approval trigger, the poisoned version goes live with no extra review. Microsoft's defense guidance: treat every connected tool as supply chain (disable "allow all"), treat tool descriptions like system prompts (review changes like code), put a human in front of risky actions, give each agent its own identity, and apply "least agency" not just least privilege.

## Related Entries
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](duneslide-cursor-sandbox-escape.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate Prompt-Injection Proxy](../tools/arc-gate-prompt-injection-proxy.md))
- [[microsoft-agent-governance-toolkit]] ([Microsoft Agent Governance Toolkit](../tools/microsoft-agent-governance-toolkit.md))

---
- [[agentic-safety-vs-textual-safety-mcp-attacks]] ([Agentic Safety vs Textual Safety](../research/agentic-safety-vs-textual-safety-mcp-attacks.md))
- [[skill-md-supply-chain-risks]] ([Agent Skills Supply-Chain Risks](skill-md-supply-chain-risks.md))
- [[mcp-stateless-core-spec]] ([MCP 2026-07-28 Stateless-Core Spec](mcp-stateless-core-spec.md))
- [[mcp-vs-direct-api-debate]] ([MCP vs Direct API Debate](../concepts/mcp-vs-direct-api-debate.md))
<!-- RU -->

## Краткое описание
Microsoft Incident Response и Defender показывают: отравленное **описание** MCP-инструмента — обычный текст, который агент читает, чтобы решить, как действовать — может тихо приказать агенту собрать и эксфильтрировать корпоративные данные через штатные одобренные вызовы. Каждый шаг выглядит легитимно; в стандартной настройке тревога не срабатывает. Microsoft называет MCP «самой быстрорастущей частью agentic AI supply chain».

## Ключевые идеи
- **Описание — это просто текст, а текст несёт инструкции.** MCP смешивает инструкции и данные в одном месте; правка описания рулит агентом как переписывание системного промпта.
- **Пример со счетами:** описание одобренного инструмента «invoice enrichment» обновляют (имя/сводка те же) скрытым приказом цеплять 30 неоплаченных счетов к следующему вызову и копировать их на сервер атакующего.
- **Каждый отдельный шаг легитимен** — одобренный инструмент, разрешения пользователя, разрешённый эндпоинт. Слабость — в «границе доверия между ними».
- **Предшественники:** Invariant Labs (апрель 2025), пакет `postmark-mcp` в npm (сент. 2025) — первый реальный вредоносный MCP-сервер: 15 чистых релизов, затем BCC на атакующего.
- **Бенчмарк MCPTox (авг. 2025):** до 72.8% успеха, модели почти никогда не отказывали.
- OWASP Top 10 for Agentic Applications (декабрь 2025) классифицирует это как Agentic Supply Chain Vulnerability.

## Подробнее
Атака эксплуатирует то, что MCP подхватывает изменения описания на лету — без триггера повторного одобрения отравленная версия включается без доп. ревью. Защита по Microsoft: считать каждый инструмент частью supply chain, проверять описания как код, ставить человека перед рискованными действиями, давать агенту собственную идентичность и применять «least agency», а не только least privilege.

## Связанные записи
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](duneslide-cursor-sandbox-escape.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate Prompt-Injection Proxy](../tools/arc-gate-prompt-injection-proxy.md))
- [[microsoft-agent-governance-toolkit]] ([Microsoft Agent Governance Toolkit](../tools/microsoft-agent-governance-toolkit.md))
