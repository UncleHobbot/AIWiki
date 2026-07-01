---
title: "Arc Gate — Proxy That Strips Instruction Authority from External Agent Content"
title_ru: "Arc Gate — прокси, лишающий внешний контент права инструктировать агента"
category: tools
tags: [prompt-injection, security, agent-proxy, agentdojo, defense]
aliases: [Arc Gate, arc-gate]
confidence: medium
updated: 2026-07-01
sources:
  - https://www.reddit.com/r/AI_Agents/comments/1ukmxdu/i_built_a_proxy_that_prevents_ai_agents_from/
---

## Summary
Arc Gate is a defense proxy built on the principle that external content (webpages, emails, tool results) has zero instruction authority over an AI agent — regardless of how an injected instruction is worded. It is integrated with a single URL change and reports strong numbers on standard prompt-injection benchmarks.

## Key Ideas
- **Data-vs-instruction separation by policy**, not pattern matching: anything arriving from a tool result, webpage, or email cannot act as an instruction to the agent.
- Reported results (vendor-tested, treat as medium confidence):
  - **AgentDojo v1** (ETH Zurich, ICLR 2024): 100% unsafe-action prevention, 0% false positives.
  - **InjecAgent** (UIUC, ACL 2024): 99% blind-test detection across 200 cases.
  - **CAIAT** cross-agent benchmark: 81% vs LLM Guard's 50%, 0% false positives on benign controls.
- Honest gap: LLM Guard scores 0% on semantic-manipulation attacks; Arc Gate scores 50% — neither catches everything.
- Pattern-based defenses miss subtle injections; Arc Gate positions itself as a structural rather than lexical defense.

## Details
Most prompt-injection defenses scan for obvious malicious patterns and fail on reworded or semantic attacks. Arc Gate changes the threat model: instead of asking "is this content malicious?", it asserts "this content has no right to instruct the agent at all." The integration model is a drop-in proxy (one endpoint change), which makes it deployable in front of existing agent stacks without code changes.

## Related Entries
- [[agentjacking-attack]] ([Agentjacking Attack](../news/agentjacking-attack.md))
- [[microsoft-agent-governance-toolkit]] ([Microsoft Agent Governance Toolkit](microsoft-agent-governance-toolkit.md))
- [[heimdall-ai-security-scanner]] ([Heimdall AI Security Scanner](heimdall-ai-security-scanner.md))

---
<!-- RU -->

## Краткое описание
Arc Gate — защитный прокси, построенный на принципе: внешний контент (веб-страницы, письма, результаты инструментов) не имеет права инструктировать ИИ-агента, независимо от формулировки внедрённой команды. Подключается заменой одного URL и показывает сильные результаты на стандартных бенчмарках prompt injection.

## Ключевые идеи
- **Разделение данных и инструкций через политику**, а не поиск по шаблонам: всё, что приходит из инструмента, веб-страницы или письма, не может быть инструкцией.
- Заявленные результаты (от вендора, уровень доверия средний):
  - **AgentDojo v1**: 100% блокировки опасных действий, 0% ложных срабатываний.
  - **InjecAgent**: 99% обнаружения в слепом тесте (200 случаев).
  - **CAIAT**: 81% против 50% у LLM Guard, 0% ложных срабатываний на benign-контроле.
- Честный пробел: на семантических атаках LLM Guard даёт 0%, Arc Gate — 50%; ни один инструмент не ловит всё.
- Защита на основе шаблонов пропускает тонкие инъекции; Arc Gate — структурная, а не лексическая защита.

## Подробнее
Большинство защит от prompt injection ищут очевидные вредоносные паттерны и падают на перефразированных атаках. Arc Gate меняет модель угроз: вместо вопроса «вредолен ли контент?» он утверждает «у этого контента вообще нет права инструктировать агента». Модель интеграции — прокси, подключаемый заменой одного эндпоинта.

## Связанные записи
- [[agentjacking-attack]] ([Agentjacking Attack](../news/agentjacking-attack.md))
- [[microsoft-agent-governance-toolkit]] ([Microsoft Agent Governance Toolkit](microsoft-agent-governance-toolkit.md))
- [[heimdall-ai-security-scanner]] ([Heimdall AI Security Scanner](heimdall-ai-security-scanner.md))
