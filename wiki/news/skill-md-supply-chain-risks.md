---
title: "Agent Skills Supply-Chain Risks — What's Inside the SKILL.md Files You npx-Install?"
title_ru: "Риски цепочки поставок agent skills — что внутри SKILL.md, которые вы ставите через npx"
category: news
tags: [skills, supply-chain, prompt-injection, malware, skillmd, npm, security]
aliases: [SKILL.md security, skills supply chain, agent skills malware]
confidence: medium
date: 2026-07-11
updated: 2026-07-11
sources:
  - https://www.reddit.com/r/opencode/comments/1ut2j1t/everyones_npx_skills_adding_random_skillmd_files/
  - https://medium.com/@guidorusso95/github-copilot-changed-pricing-so-i-rebuilt-my-entire-ai-coding-stack-with-chinese-models-8620172ea868
---

## Summary
The Agent Skills ecosystem (`SKILL.md`) exploded from zero to ~350,000 packages in about two months — the same milestone took npm a decade. The install-and-forget UX mirrors npm circa 2013, except now the code you install runs *inside an agent that has your shell and your API keys*. Security research caught up fast: prompt injection in roughly a third of sampled skills on one marketplace, and credential-stealer malware campaigns distributed as regular skills.

## Key Ideas
- **Scale & speed:** the Skills ecosystem hit ~350k packages in ~2 months; npm took a decade to reach the same count.
- **Same UX, higher stakes:** install-and-forget `npx skills add` feels like npm 2013, but the installed code runs inside an agent with shell + API-key access — a much richer attack surface than a build pipeline.
- **Documented risks:**
  - **Prompt injection** in roughly a third of sampled skills on one marketplace.
  - **Credential-stealer malware** campaigns packaged as regular skills.
- **Why this is worse than npm:** a malicious npm package runs at build time; a malicious skill runs every time the agent is active, with the user's full permissions, and can be triggered indirectly via prompt injection from other content.
- Tier 3 (community report citing security research); the specific marketplace and research-paper references should be verified against the primary sources.

## Details
This is the agent-skills analogue of the [[mcp-tool-poisoning-microsoft]] finding and the broader [[amazon-q-mcp-config-rce]] pattern: every convenient extension mechanism (npm packages, MCP servers, SKILL.md files) becomes a supply-chain attack surface, and the agent ecosystem is repeating npm's history — but with higher stakes because the runtime has live credentials and shell access. The defense direction is the same Microsoft recommends for MCP: treat every installed skill as supply chain, review its contents like code, and don't run `skills add` against untrusted sources.

## Related Entries
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[stop-slop-skill]] ([stop-slop Skill](../tools/stop-slop-skill.md))
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin](../agents/superpowers-plugin-claude-code.md))

---
<!-- RU -->

## Краткое описание
Экосистема Agent Skills (`SKILL.md`) выросла с нуля до ~350 000 пакетов примерно за два месяца — npm шёл до той же отметки десятилетие. UX «установил и забыл» повторяет npm образца 2013 года, но теперь код выполняется *внутри агента с вашим шеллом и API-ключами*. Исследования безопасности быстро догнали: prompt injection примерно в трети проверенных skills на одной площадке, кампании malware-кражи учётных данных в виде обычных skills.

## Ключевые идеи
- **Масштаб и скорость:** ~350k пакетов за ~2 месяца; npm шёл до этого десятилетие.
- **Тот же UX, выше ставки:** `npx skills add` ощущается как npm 2013, но код работает внутри агента с шеллом и ключами.
- **Задокументированные риски:** prompt injection примерно в трети sampled skills; кампании credential-stealer-malware под видом skills.
- **Почему хуже npm:** вредоносный npm-пакет работает при сборке; вредоносный skill — при каждом активном агенте, с полными правами и косвенно через prompt injection.
- Уровень 3 (сообщество ссылается на research); конкретные площадки и paper'ы стоит сверить с первоисточником.

## Подробнее
Это agent-skills-аналог находки [[mcp-tool-poisoning-microsoft]] и паттерна [[amazon-q-mcp-config-rce]]: каждый удобный механизм расширения становится поверхностью атаки цепочки поставок, и агентная экосистема повторяет историю npm — но с более высокими ставками. Направление защиты то же: считать каждый skill частью supply chain, проверять содержимое как код.

## Связанные записи
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[stop-slop-skill]] ([stop-slop Skill](../tools/stop-slop-skill.md))
- [[superpowers-plugin-claude-code]] ([Superpowers Plugin](../agents/superpowers-plugin-claude-code.md))
