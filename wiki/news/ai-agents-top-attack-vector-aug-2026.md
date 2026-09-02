---
title: "AI Agents Are Now the #1 Breach Attack Vector (August 2026 Incident Review)"
title_ru: "ИИ-агенты — теперь атакующий вектор №1 (обзор инцидентов за август 2026)"
category: news
tags: [breach-statistics, attack-vector, agent-security, incident-review, mckesson]
aliases: [agents top attack vector, august 2026 breaches, agent incidents]
confidence: medium
date: 2026-09-01
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/ollama/comments/1w4g75q/august_2026_38_companies_breached_331m_records/
---

## Summary
A community-compiled review of every AI-security incident in August 2026: **123 incidents, 23 critical / 97 high severity, 38 named organizations, 331M+ records exposed.** The headline finding: **AI-agent exploits (37 incidents) are now the single largest attack-vector category** — ahead of credential theft (28), zero-days (23), supply chain (12), phishing (9), data exfiltration (8), and ransomware (6). 65 incidents involved AI as weapon or target.

## Key Ideas
- **The crossover moment:** agent exploits overtaking credential theft as the top vector marks the shift from "agents are a future risk" to "agents are the current front door."
- **Biggest incidents:** McKesson (284M records — the month's largest by far), Carhartt (12.9M), Exact Sciences (10.9M), CareCloud (3.7M) — three of four in or adjacent to healthcare.
- **Confirmed RCEs:** five across Microsoft SharePoint, Windows, F5/nginx, and PyPI (twice).
- **Context:** independently corroborates the wiki's agent-security cluster — [[agentjacking-attack]], [[gitlost-github-agentic-workflow-leak]], [[hallusquatting-ai-hallucination-botnet]], [[friendly-fire-ai-code-review-agents-tricked]] — as facets of the same statistically dominant vector.
- Tier 3 (community compilation), but incident-level claims are checkable and the vector ranking matches vendor reporting direction.

## Details
The practical implication for security teams: EDR-style alerting tuned for human attackers ([[ai-coding-agents-triggering-edr-rules]]) plus agent-specific attack surfaces (MCP poisoning, prompt injection, hallucinated packages) now outrank the classic triad. The month's numbers give the wiki's agent-security cluster its quantitative anchor.

## Related Entries
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[gitlost-github-agentic-workflow-leak]] ([GitLost](gitlost-github-agentic-workflow-leak.md))
- [[ai-coding-agents-triggering-edr-rules]] ([AI Coding Agents Triggering EDR Rules](ai-coding-agents-triggering-edr-rules.md))
- [[mcp-tool-poisoning-microsoft]] ([MCP Tool Poisoning](mcp-tool-poisoning-microsoft.md))

---
<!-- RU -->

## Краткое описание
Обзор всех ИИ-инцидентов безопасности за август 2026: **123 инцидента, 23 критических / 97 высоких, 38 организаций, 331M+ утекших записей.** Главный вывод: **эксплойты ИИ-агентов (37 инцидентов) — теперь крупнейшая категория атакующих векторов** — впереди кражи учётных данных (28), zero-days (23), supply chain (12), фишинга (9), эксфильтрации (8) и ransomware (6).

## Ключевые идеи
- **Момент перехода:** эксплойты агентов обошли кражу креденшелов — сдвиг от «агенты — риск будущего» к «агенты — текущая парадная дверь».
- **Крупнейшие инциденты:** McKesson (284M записей), Carhartt (12.9M), Exact Sciences (10.9M), CareCloud (3.7M) — три из четырёх в здравоохранении или рядом.
- **Подтверждённые RCE:** пять — Microsoft SharePoint, Windows, F5/nginx, PyPI (дважды).
- **Контекст:** независимо подтверждает агентно-безопасностный кластер вики как грани одного статистически доминирующего вектора.
- Уровень 3 (компиляция сообщества), но отдельные инциденты проверяемы, а ранжирование векторов совпадает с направлением вендорских отчётов.

## Подробнее
Практический вывод для секьюрити-команд: алертинг под человеческих атакующих плюс агентные поверхности (MCP poisoning, prompt injection, галлюцинированные пакеты) теперь ранжируются выше классической триады. Числа месяца дают количественный якорь агентно-безопасностному кластеру вики.

## Связанные записи
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[gitlost-github-agentic-workflow-leak]] ([GitLost](gitlost-github-agentic-workflow-leak.md))
- [[ai-coding-agents-triggering-edr-rules]] ([AI Coding Agents Triggering EDR Rules](ai-coding-agents-triggering-edr-rules.md))
- [[mcp-tool-poisoning-microsoft]] ([MCP Tool Poisoning](mcp-tool-poisoning-microsoft.md))
