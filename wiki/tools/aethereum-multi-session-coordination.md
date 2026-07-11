---
title: "aethereum — Shared Coordination Room for Multiple Claude Code Sessions"
title_ru: "aethereum — общая комната координации для нескольких сессий Claude Code"
category: tools
tags: [claude-code, multi-agent, session-coordination, api-shape, concurrency]
aliases: [aethereum, multi-session coordination]
confidence: medium
updated: 2026-07-11
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1utgmhd/multiple_claude_code_sessions_on_one_repo_kept/
---

## Summary
**aethereum** is a tool for developers running multiple Claude Code sessions on the same repo (e.g. across laptop + desktop). It gives sessions a shared "room" where each agent declares the interfaces it owns and what it's currently touching — so when one session changes an API shape, the others hear about it before building on the old version. Free during beta; `npx aethereum init`, no account needed.

## Key Ideas
- **Problem solved:** 2–3 Claude Code sessions on the same repo silently break each other — one changes an API shape while another keeps generating code against the old one. Nothing is committed yet, so git has no idea; it surfaces only when the build breaks.
- **What didn't work:** small frequent commits (shrinks the window, doesn't close it); a conventions file read on start (good for naming drift, useless for live changes).
- **What works — a shared room:** each session declares the interfaces it owns and what it's currently touching; when one declares a change, the others are notified before they build on the stale shape.
- CLI: `npx aethereum init`. Free during beta, no account.
- Addresses a real gap in multi-agent dev: git tracks committed state, but live uncommitted agent edits are invisible to other sessions.

## Details
This is a coordination layer for the uncommitted-edit window that git doesn't cover. As multi-session coding agent setups become common (orchestrator + workers, laptop + desktop), the "two agents edit the same interface" race condition is a recurring real-world failure. aethereum treats it as a publish/subscribe problem on interface ownership.

## Related Entries
- [[claude-code]] ([Claude Code](claude-code.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](../tips/hard-gates-over-soft-prompts.md))
- [[using-git-worktrees-claude-code]] ([Git Worktrees in Claude Code](../tips/using-git-worktrees-claude-code.md))

---
<!-- RU -->

## Краткое описание
**aethereum** — инструмент для разработчиков, запускающих несколько сессий Claude Code на одном репо (например, ноутбук + десктоп). Даёт сессиям общую «комнату», где каждый агент декларирует интерфейсы, которыми владеет, и что сейчас правит, — поэтому при изменении API-shape остальные узнают об этом до того, как строить на старой версии. Бесплатно в бете; `npx aethereum init`, без аккаунта.

## Ключевые идеи
- **Решаемая проблема:** 2–3 сессии Claude Code на одном репо молча ломают друг друга — одна меняет API-shape, другая генерирует код под старый. Ничего не закоммичено, git ничего не знает; всплывает при сломанной сборке.
- **Что не помогло:** мелкие частые коммиты; файл конвенций при старте.
- **Что работает — общая комната:** каждая сессия декларирует интерфейсы и текущие правки; при изменении другие оповещаются.
- CLI: `npx aethereum init`. Бесплатно в бете.
- Закрывает пробел multi-agent-разработки: git отслеживает закоммиченное, а незакоммиченные live-правки агентов невидимы для других сессий.

## Подробнее
Это слой координации для окна незакоммиченных правок, не покрываемого git. С распространением multi-session сетапов (оркестратор + воркеры, ноутбук + десктоп) race condition «два агента правят один интерфейс» — повторяющийся реальный сбой. aethereum трактует его как publish/subscribe по владению интерфейсами.

## Связанные записи
- [[claude-code]] ([Claude Code](claude-code.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](../tips/hard-gates-over-soft-prompts.md))
- [[using-git-worktrees-claude-code]] ([Git Worktrees in Claude Code](../tips/using-git-worktrees-claude-code.md))
