---
title: "Package Hallucination Catcher: MCP Server for LLM Package Recommendations"
title_ru: "Ловушка галлюцинаций пакетов: MCP-сервер для рекомендаций LLM"
category: tools
tags: [hallucination, mcp, npm, pypi, package-manager, security, llm-coding, claude-code]
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://www.reddit.com/r/ChatGPTCoding/comments/1srhmnr/20_of_packages_chatgpt_recommends_dont_exist/
  - https://arxiv.org/abs/2406.10279
---

## Summary
A community-built MCP server intercepts LLM package recommendations before `npm install` or `pip install` runs, checking each suggested package name against real registries to catch the roughly 1-in-5 hallucinated package names that LLMs generate — names that attackers increasingly pre-register as malicious squatted packages.

## Key Ideas
- A 2024 academic study (arXiv:2406.10279) measured how often major LLMs recommend packages that don't exist on npm or PyPI: the rate came in at **19.7%** — nearly 1 in 5 recommendations.
- The attack surface this creates is real: attackers scrape common LLM hallucinations and pre-register those exact package names on npm/PyPI with malicious payloads, turning a hallucination into a supply-chain attack vector.
- The MCP server sits between the coding agent and the shell: when an agent proposes an install command, the server validates the package name against the live registry before the command executes.
- Works with any MCP-capable coding agent (Claude Code, Cursor, Codex CLI, OpenCode) — no changes to the agent's workflow required.
- Zero false-negative risk for real packages: if a name exists in the registry, it passes through. The check only fires on non-existent names.

## Details
LLM-assisted coding regularly produces `pip install` and `npm install` commands for packages that don't exist. The model confidently generates plausible-sounding library names — often combinations of real words from related packages — without any grounding in what is actually published. At a 19.7% rate, a developer relying on an AI coding agent for package management will encounter a hallucinated package recommendation roughly every five installs.

The security dimension makes this more than a convenience problem. Supply-chain attackers have begun monitoring popular AI outputs and registering hallucinated package names the moment they appear in LLM-generated code. A developer who runs the suggested install against a squatted package gets malware, not the library they expected.

The MCP server solution is architecturally simple: register it as an MCP tool named something like `validate_package`, and instruct Claude Code (or any agent) to call it before any install command. The tool makes a HEAD request to the registry API, returns `{exists: true}` or `{exists: false, alternatives: [...]}`, and the agent either proceeds or asks the user to clarify the intended package.

**Affected registries:** npm (JavaScript/Node.js), PyPI (Python). Cargo (Rust) and crates.io have lower hallucination rates because Rust package names are less ambiguous in training data.

## Related Entries
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))
- [[gnosis-mcp]] ([Gnosis MCP: Documentation Search Server for AI Agents](../tools/gnosis-mcp.md))
- [[mcp-financial-data-server]] ([Self-Hosted MCP Server for Financial Data](../tools/mcp-financial-data-server.md))
- [[cloakbrowser-stealth-chromium]] ([CloakBrowser: Stealth Chromium for Bot Detection Bypass](../tools/cloakbrowser-stealth-chromium.md))
- [[equibles-mcp-financial-data]] ([Equibles: Financial Data MCP](../tools/equibles-mcp-financial-data.md))

---
- [[hallusquatting-ai-hallucination-botnet]] ([HalluSquatting](../news/hallusquatting-ai-hallucination-botnet.md))
<!-- RU -->

## Краткое описание
Разработанный сообществом MCP-сервер перехватывает рекомендации пакетов от LLM до запуска `npm install` или `pip install`, проверяя каждое предложенное имя пакета в реальных реестрах — чтобы поймать примерно каждый пятый галлюцинированный пакет, имена которых злоумышленники всё активнее регистрируют как вредоносные squatted-пакеты.

## Ключевые идеи
- Академическое исследование 2024 года (arXiv:2406.10279) измерило частоту рекомендаций несуществующих пакетов ведущими LLM: результат — **19,7%**, почти каждая пятая рекомендация.
- Реальная поверхность атаки: злоумышленники парсят типичные галлюцинации LLM и заранее регистрируют эти точные имена в npm/PyPI с вредоносной нагрузкой — галлюцинация превращается в вектор атаки на цепочку поставок.
- MCP-сервер располагается между coding agent и оболочкой: когда агент предлагает команду установки, сервер проверяет имя пакета в реестре до выполнения команды.
- Совместим с любым MCP-совместимым агентом: Claude Code, Cursor, Codex CLI, OpenCode — никаких изменений рабочего процесса агента не требуется.
- Нулевой риск ложных отрицаний для реальных пакетов: если имя существует в реестре — оно проходит проверку. Проверка срабатывает только для несуществующих имён.

## Подробнее
AI-ассистированное кодирование регулярно генерирует команды `pip install` и `npm install` для несуществующих пакетов. Модель уверенно создаёт правдоподобно звучащие имена библиотек — часто комбинации реальных слов из связанных пакетов — без привязки к реально опубликованному. При частоте 19,7% разработчик, полагающийся на AI-агент для управления пакетами, столкнётся с галлюцинированной рекомендацией примерно каждые пять установок.

Измерение безопасности делает это больше чем проблемой удобства. Злоумышленники в цепочках поставок начали мониторить вывод популярных AI-систем и регистрировать галлюцинированные имена пакетов сразу, как они появляются в AI-генерированном коде. Разработчик, запускающий предложенную установку со squatted-пакетом, получает вредоносное ПО вместо ожидаемой библиотеки.

Решение с MCP-сервером архитектурно простое: зарегистрировать его как MCP-инструмент с именем `validate_package` и указать Claude Code (или любому агенту) вызывать его перед любой командой установки. Инструмент делает HEAD-запрос к API реестра и возвращает `{exists: true}` или `{exists: false, alternatives: [...]}`.

## Связанные записи
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))
- [[gnosis-mcp]] ([Gnosis MCP: Documentation Search Server for AI Agents](../tools/gnosis-mcp.md))
- [[mcp-financial-data-server]] ([Self-Hosted MCP Server for Financial Data](../tools/mcp-financial-data-server.md))
- [[equibles-mcp-financial-data]] ([Equibles: Financial Data MCP](../tools/equibles-mcp-financial-data.md))
