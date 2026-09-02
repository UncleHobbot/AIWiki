---
title: "OpenCrew — Kiro Crew with a Self-Hosted OpenCode Backend"
title_ru: "OpenCrew — Kiro Crew с самохостным бэкендом OpenCode"
category: agents
tags: [opencode, kiro, multi-agent, persistent-workspace, self-hosted, messaging]
aliases: [OpenCrew, KiroCrew opencode, persistent ai workspace]
confidence: low
updated: 2026-09-01
sources:
  - https://github.com/hamin2006/OpenCrew
  - https://kiro.dev/crew/
---

## Summary
OpenCrew is a fork of Kiro Crew (Kiro's persistent AI workspace) that replaces the `kiro-cli` backend with a self-hosted, headless OpenCode (built and tested on DeepSeek) — keeping Kiro Crew's dashboard and messaging channels while removing the Kiro account requirement. Very new and unproven (0 stars, days old), but the concept maps directly onto this wiki's OpenCode coverage.

## Key Ideas
- **Three-layer architecture:** surfaces (dashboard, CLI, messaging apps) → long-running Gateway (sessions, memory, scheduling, approvals) → agent sessions running OpenCode over the Agent Client Protocol via a Node shim.
- **Persistent sessions:** conversations, memory, schedules, and checkpoints survive gateway restarts — the "persistent workspace" pitch.
- **Self-evolving skills:** corrections and failures become durable workspace-scoped lessons; repeated patterns become editable markdown skills.
- **Unattended autonomy:** cron jobs, heartbeats, reactive webhooks, checkpointed multi-step runs (`kirocrew run TASK.md`) with plan/validate/retry.
- **Messaging integrations:** Telegram, Slack, Discord, Teams, Webex, WeCom, WeChat.
- **Security caveats:** interactive approvals, sensitive-path guards, 137 bundled deny patterns, audit trails — but the sandbox ships **off by default**; Apache-2.0 inherited from upstream.

## Details
Worth tracking as a signal of two converging trends: Kiro-style persistent crew workspaces becoming the product shape, and OpenCode becoming the default self-hosted agent runtime others build on (same pattern as [[relay-dsh-plugin-codex]] hosting Codex inside DSH). Maturity risk is real — it's a days-old personal fork of a days-old upstream — so treat it as an architecture reference, not a dependency.

## Related Entries
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[opencode-background-agents]] ([OpenCode Background Agents](../tools/opencode-background-agents.md))
- [[relay-dsh-plugin-codex]] ([relay-dsh-plugin-codex](../tools/relay-dsh-plugin-codex.md))
- [[orkestra-multi-cli]] ([Orkestra Multi-CLI](../tools/orkestra-multi-cli.md))

---
<!-- RU -->

## Краткое описание
OpenCrew — форк Kiro Crew (персистентное AI-воркспейс-решение Kiro), заменяющий бэкенд `kiro-cli` на самохостный headless OpenCode (собран и протестирован на DeepSeek) — сохраняет дашборд Kiro Crew и мессенджер-каналы, убирая требование аккаунта Kiro. Очень новый и непроверенный (0 звёзд), но концепция напрямую ложится на покрытие OpenCode в этой вики.

## Ключевые идеи
- **Трёхслойная архитектура:** поверхности (дашборд, CLI, мессенджеры) → долгоживущий Gateway (сессии, память, расписания, подтверждения) → агентные сессии на OpenCode через Agent Client Protocol.
- **Персистентные сессии:** разговоры, память, расписания и чекпоинты переживают перезапуск гейтвея.
- **Самоэволюционирующие навыки:** исправления и провалы становятся долговременными уроками воркспейса; повторяющиеся паттерны — редактируемыми markdown-скиллами.
- **Автономность без присмотра:** cron, heartbeats, reactive webhooks, чекпоинтированные многошаговые прогоны (`kirocrew run TASK.md`) с plan/validate/retry.
- **Мессенджеры:** Telegram, Slack, Discord, Teams, Webex, WeCom, WeChat.
- **Безопасность:** интерактивные подтверждения, guard'ы чувствительных путей, 137 deny-паттернов — но песочница **выключена по умолчанию**.

## Подробнее
Отслеживать как сигнал двух сходящихся трендов: персистентные crew-воркспейсы в стиле Kiro становятся формой продукта, а OpenCode — самохостным агентным рантаймом по умолчанию, на котором строят другие (тот же паттерн, что [[relay-dsh-plugin-codex]]). Риск зрелости реален — личный форк дни от роду — поэтому рассматривать как архитектурный референс, не зависимость.

## Связанные записи
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[opencode-background-agents]] ([OpenCode Background Agents](../tools/opencode-background-agents.md))
- [[relay-dsh-plugin-codex]] ([relay-dsh-plugin-codex](../tools/relay-dsh-plugin-codex.md))
- [[orkestra-multi-cli]] ([Orkestra Multi-CLI](../tools/orkestra-multi-cli.md))
