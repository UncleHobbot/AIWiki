---
title: "DuneSlide — Prompt-Injection Sandbox Escape in Cursor (CVE-2026-50548/50549)"
title_ru: "DuneSlide — побег из песочницы Cursor через prompt injection (CVE-2026-50548/50549)"
category: news
tags: [cursor, prompt-injection, sandbox-escape, mcp, cve, code-execution, security]
aliases: [DuneSlide, CVE-2026-50548, CVE-2026-50549, cursor sandbox escape]
confidence: high
date: 2026-07-01
updated: 2026-07-01
sources:
  - https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html
---

## Summary
Two critical flaws in the Cursor AI code editor (CVE-2026-50548 and CVE-2026-50549, both CVSS 9.8) let a single ordinary-looking prompt break out of the editor's terminal sandbox and execute arbitrary commands on the developer's machine — zero-click, no approval box. Dubbed **DuneSlide** by Cato AI Labs; patched in Cursor 3.0 (April 2, 2026). All pre-3.0 versions are affected.

## Key Ideas
- **Zero-click sandbox escape:** instructions planted in something the agent reads (an MCP service, a web-search result) ride along with a normal user question — no click or approval needed.
- **Both flaws write one forbidden file, then use it to disable the sandbox:**
  - **CVE-2026-50548:** the sandbox allows writes into a command's `working_directory`; when the agent sets it to a non-default system path (e.g. the sandbox helper binary or `~/.zshrc`), Cursor adds it to the allowed-write list without question.
  - **CVE-2026-50549:** Cursor's symlink resolution check falls back to trusting the in-project path when the check fails (missing target or attacker-removed read access) — so a symlink pointing outside the project writes straight through.
- **Impact:** once the sandbox is neutralized, the next command runs as the user — full machine control plus any signed-in cloud/SaaS sessions.
- **No known exploitation in the wild;** Cursor initially rejected the report (Feb 19) saying its threat model didn't cover MCP misuse, then reopened and shipped fixes in 3.0.
- Part of a recurring pattern: CurXecute (CVE-2025-54135), MCPoison (CVE-2025-54136), CVE-2026-26268 (git hook) — each defeats a different Cursor guardrail.

## Details
The 2.x sandbox was Cursor's answer to the earlier prompt-injection wave. DuneSlide escapes that answer through the filesystem: both variants overwrite the `cursorsandbox` helper (or a startup file), so subsequent terminal commands run unsandboxed. Cato says it is disclosing similar flaws in other coding agents and argues the problem is structural — agents that read the open web must treat every input as hostile.

## Related Entries
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate Prompt-Injection Proxy](../tools/arc-gate-prompt-injection-proxy.md))

---
- [[ghostapproval-symlink-coding-agent-flaw]] ([GhostApproval Symlink Flaws](ghostapproval-symlink-coding-agent-flaw.md))
<!-- RU -->

## Краткое описание
Два критических бага в AI-редакторе Cursor (CVE-2026-50548 и CVE-2026-50549, оба CVSS 9.8) позволяют одному обычному промпту вырваться из терминальной песочницы и выполнить произвольные команды на машине разработчика — zero-click, без окна подтверждения. Названы **DuneSlide** (Cato AI Labs); исправлены в Cursor 3.0 (2 апреля 2026). Все версии до 3.0 уязвимы.

## Ключевые идеи
- **Zero-click побег из песочницы:** инструкции, спрятанные в том, что читает агент (MCP-сервис, результат веб-поиска), едут вместе с обычным вопросом пользователя.
- **Оба бага пишут один запрещённый файл, затем отключают песочницу:**
  - **CVE-2026-50548:** песочница разрешает запись в `working_directory`; если агент указывает системный путь (бинарник-помощник песочницы или `~/.zshrc`), Cursor добавляет его в whitelist без вопросов.
  - **CVE-2026-50549:** проверка symlink'ов Cursor'а при ошибке падает в fallback и доверяет in-project пути — symlink наружу пишет прямо через неё.
- **Влияние:** после отключения песочницы следующая команда выполняется от имени пользователя — полный контроль над машиной и облачными сессиями.
- **Эксплуатации в дикой природе не зафиксировано;** Cursor сначала отклонил репорт (19 февраля), затем переоткрыл и выпустил фикс в 3.0.
- Часть серии: CurXecute, MCPoison, CVE-2026-26268 — каждый обходит разные ограждения Cursor.

## Подробнее
Песочница 2.x была ответом Cursor на предыдущую волну prompt injection. DuneSlide сбегает через файловую систему: оба варианта перезаписывают хелпер `cursorsandbox` (или стартовый файл), поэтому последующие команды идут без песочницы. Cato сообщает о похожих багах в других кодинг-агентах и считает проблему структурной.

## Связанные записи
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](mcp-tool-poisoning-microsoft.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate Prompt-Injection Proxy](../tools/arc-gate-prompt-injection-proxy.md))
