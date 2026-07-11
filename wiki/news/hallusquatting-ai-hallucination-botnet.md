---
title: "HalluSquatting — Weaponizing AI Hallucinations to Build Botnets via Coding Agents"
title_ru: "HalluSquatting — оружие галлюцинаций ИИ для построения ботнетов через кодинг-агентов"
category: news
tags: [hallucination, slopsquatting, prompt-injection, botnet, supply-chain, coding-agent, tel-aviv-university]
aliases: [HalluSquatting, hallu squatting, slopsquatting botnet]
confidence: high
date: 2026-07-08
updated: 2026-07-11
sources:
  - https://thehackernews.com/2026/07/new-hallusquatting-attack-could-trick.html
---

## Summary
Researchers at Tel Aviv University (Ben Nassi's group), Technion, and Intuit disclosed **HalluSquatting**: an attack that chains AI hallucination + indirect prompt injection to turn coding agents into a botnet delivery channel. The attacker learns the fake package/repo names an AI predictably invents, registers them first, and waits for the agent to fetch the trap on a user's behalf — then the agent's own terminal tool installs the bot. Peak success rate: up to 85% for repository requests, 100% for skill installs.

## Key Ideas
- **The two-quirk chain:** (1) hallucination (AI invents a plausible-but-fake name) + (2) indirect prompt injection (the registered fake contains hidden instructions the agent follows).
- **4-step recipe:** pick a trending target (not in training data → AI guesses) → learn the most-invented fake name by querying repeatedly → register that name on GitHub/plugin store with adversarial instructions → wait for a real user's agent to fetch it.
- **Why it works:** the agent has a built-in terminal, so once the planted instructions take over, "install a bot" is something it can do autonomously.
- **Consistency of the mistake:** across phrasings and across vendors' models, the same wrong name was chosen in up to 85% of repo requests and 100% of skill installs.
- **Tested against:** Cursor, Windsurf, GitHub Copilot, Cline, Gemini CLI, OpenClaw family — all ran attacker code (harmless test payloads; real malware takes the same path).
- **A new botnet class:** no passwords, no worming, no network exploit (the payload arrives as text the AI reads); works across operating systems; one planted name can reach many machines.
- Lineage: "slopsquatting" (fake npm packages — `react-codeshift`, 237 projects) → "phantom squatting" (~250k hallucinated domains, Unit 42) → HalluSquatting (runs code by hijacking the fetching agent).

## Details
HalluSquatting is notable because it reaches *code execution* by weaponizing the agent's own fetch-and-run workflow, not a software vulnerability. The defense is closing the one condition the attack needs: an agent that fetches an outside resource and runs it with no one checking. Most effective fix: make the assistant **search before it fetches** (a real lookup grounds the agent in what actually exists). Near-term user levers: avoid auto-run modes (Claude Code's `--dangerously-skip-permissions`, Gemini CLI's yolo mode); treat any name an AI hands you as a guess, not a fact; verify the name resolves to the expected source. Platform levers: stop reusing well-known repo names under new accounts; pre-register the fake names AIs invent (the typosquatting defense applied to hallucinations).

## Notable Quotes
> "Attacks always get better; they never get worse." — the researchers, framing their numbers as a lower bound

## Related Entries
- [[skill-md-supply-chain-risks]] ([Agent Skills Supply-Chain Risks](skill-md-supply-chain-risks.md))
- [[package-hallucination-mcp]] ([Package Hallucination MCP](../tools/package-hallucination-mcp.md))
- [[friendly-fire-ai-code-review-agents-tricked]] ([Friendly Fire — AI Code-Review Agents Tricked](friendly-fire-ai-code-review-agents-tricked.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))

---
<!-- RU -->

## Краткое описание
Исследователи Тель-Авивского университета (группа Бена Насси), Technion и Intuit раскрыли **HalluSquatting**: атаку, цепляющую галлюцинации ИИ + косвенную prompt-инъекцию для превращения кодинг-агентов в канал доставки ботнета. Атакующий выясняет выдуманные ИИ имена пакетов/репо, регистрирует их первым и ждёт, пока агент пользователя не подтянет ловушку — затем собственный терминал агента ставит бот. Пиковый успех: до 85% для запросов репо, 100% для установки skills.

## Ключевые идеи
- **Цепочка из двух свойств:** (1) галлюцинация + (2) косвенная prompt-инъекция.
- **Рецепт из 4 шагов:** выбрать trending-цель → узнать самое частое выдуманное имя → зарегистрировать его с вредоносными инструкциями → ждать.
- **Почему работает:** у агента есть встроенный терминал; «поставить бот» — то, что он может сделать автономно.
- **Стабильность ошибки:** до 85% для репо, 100% для skills, независимо от формулировок и вендора модели.
- **Протестировано на:** Cursor, Windsurf, GitHub Copilot, Cline, Gemini CLI, OpenClaw — все выполнили код атакующего.
- **Новый класс ботнета:** без паролей, без червя, без сетевого эксплойта; payload приходит как текст; кросс-ОС.
- Линия: «slopsquatting» (фейковые npm) → «phantom squatting» (домены) → HalluSquatting (выполняет код).

## Подробнее
HalluSquatting достигает *выполнения кода*, оружиеизируя собственный fetch-and-run воркфлоу агента, а не уязвимость ПО. Защита — закрыть единственное условие: агент, который тянет внешний ресурс и выполняет его без проверки. Самый эффективный фикс: **искать перед fetch**. Ближайшие рычаги: избегать auto-run режимов (`--dangerously-skip-permissions`, yolo mode); считать любое имя от ИИ догадкой; верифицировать источник. Платформы: не переиспользовать известные имена репо; пререгистрировать выдуманные ИИ имена.

## Примечательные цитаты
> «Атаки всегда улучшаются; никогда не ухудшаются.» — исследователи, называя свои числа нижней границей

## Связанные записи
- [[skill-md-supply-chain-risks]] ([Agent Skills Supply-Chain Risks](skill-md-supply-chain-risks.md))
- [[package-hallucination-mcp]] ([Package Hallucination MCP](../tools/package-hallucination-mcp.md))
- [[friendly-fire-ai-code-review-agents-tricked]] ([Friendly Fire — AI Code-Review Agents Tricked](friendly-fire-ai-code-review-agents-tricked.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
