---
title: "GitHub Copilot Now Natively Integrated into JetBrains IDEs"
title_ru: "GitHub Copilot теперь нативно интегрирован в JetBrains IDE"
category: news
tags: [github-copilot, jetbrains, ide-integration, agentic-coding]
aliases: [copilot jetbrains, copilot acp]
confidence: high
date: 2026-06-30
updated: 2026-07-01
sources:
  - https://www.reddit.com/r/GithubCopilot/comments/1ujs9aw/github_copilot_is_now_natively_integrated_into/
  - https://blog.jetbrains.com/ai/2026/06/github-copilot-now-an-integrated-agent/
---

## Summary
As of late June 2026, GitHub Copilot is a first-class, natively integrated agent inside JetBrains IDEs — no plugin install or registry configuration required. It is the product of a joint effort between JetBrains and GitHub/Microsoft.

## Key Ideas
- **Native first-class agent** in JetBrains IDEs, available out of the box across the IDE family.
- **No setup:** no registry configuration or extra plugin install — works for anyone already on a Copilot plan.
- Two paths now coexist: Copilot via JetBrains AI Assistant over **ACP** (Agent Client Protocol), or the dedicated GitHub Copilot plugin for the full Copilot experience.
- Validates ACP as the emerging interop standard between agent backends and IDE frontends.

## Details
The integration means teams standardized on Copilot no longer need the standalone plugin to get agent behavior inside JetBrains tools. The ACP-based path lets the same Copilot backend serve multiple IDE frontends, a sign that the agent ↔ IDE boundary is settling on a shared protocol rather than bespoke plugins per vendor pair.

## Related Entries
- [[product-github-copilot]] ([GitHub Copilot](../tools/product-github-copilot.md))
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[github-copilot-app]] ([GitHub Copilot App](github-copilot-app.md))

---
<!-- RU -->

## Краткое описание
С конца июня 2026 года GitHub Copilot стал first-class, нативно интегрированным агентом внутри JetBrains IDE — без установки плагина или настройки реестра. Это результат совместной работы JetBrains и GitHub/Microsoft.

## Ключевые идеи
- **Нативный first-class агент** в JetBrains IDE, доступен из коробки во всём семействе.
- **Без настройки:** не требует конфигурации реестра или доп. плагина — работает для любого пользователя Copilot.
- Сосуществуют два пути: Copilot через JetBrains AI Assistant по **ACP** (Agent Client Protocol), либо отдельный плагин GitHub Copilot для полного опыта.
- Подтверждает ACP как emerging-стандарт interoperability между бэкендами агентов и фронтендами IDE.

## Подробнее
Интеграция означает, что командам на Copilot больше не нужен отдельный плагин для агентского поведения в JetBrains. Путь на базе ACP позволяет одному бэкенду Copilot обслуживать несколько IDE-фронтендов — признак того, что граница «агент ↔ IDE» settling'ится на общем протоколе.

## Связанные записи
- [[product-github-copilot]] ([GitHub Copilot](../tools/product-github-copilot.md))
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[github-copilot-app]] ([GitHub Copilot App](github-copilot-app.md))
