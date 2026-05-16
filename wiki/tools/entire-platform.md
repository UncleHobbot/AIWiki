---
title: "Entire: Agent Session Checkpointing for Git"
title_ru: "Entire: чекпоинты сессий агентов для git"
category: tools
tags: [git, agent, claude-code, opencode, checkpoint, context, session-capture, open-source]
updated: 2026-05-15
sources:
  - https://entire.io/home
  - https://docs.entire.io/overview
  - https://docs.entire.io/agents/copilot-cli
  - https://docs.entire.io/agents/opencode
---

## Summary
Entire is an open-source CLI that hooks into your git workflow and captures full AI agent sessions as "Checkpoints" — linked to git commits so you can always see not just *what* code was written, but *why*, with the ability to rewind or resume any past session.

## Key Ideas
- **Checkpoints = commit + full agent context:** Every `git commit` creates a Checkpoint containing the prompt, full transcript, tool calls, file changes, token usage, and timestamps — stored in the `entire/checkpoints/v1` git branch. No external database.
- **Solves agent amnesia:** Agents start every session from zero, repeating the same mistakes because they have no history of how the codebase was built. Entire gives future sessions access to that history.
- **"Why did we write it this way?"** Any commit can be traced back to the agent session that produced it — reviewers see the reasoning, not just the diff. Commits get an `Entire-Checkpoint` git trailer.
- **Rewind and resume:** `entire checkpoint rewind` restores to a previous checkpoint mid-session. `entire session resume <id>` continues from any past session, restoring the transcript so the agent picks up where it left off.
- **Multi-agent support:** Claude Code, Gemini CLI, OpenCode, Cursor, GitHub Copilot CLI, FactoryAI supported. More coming.
- **Local-first, open-source, MIT:** `curl -fsSL https://entire.io/install.sh | bash`. 3.8k+ stars. $60M seed round announced.

## Details
**Install and setup:**
```bash
curl -fsSL https://entire.io/install.sh | bash

# Enable for an agent in your repo
entire agent add copilot-cli    # or: opencode, claude-code, cursor
copilot                          # start working; sessions are captured automatically
```

**What gets captured per session:**

| Data | Copilot CLI | OpenCode |
|---|---|---|
| Conversation transcript | ✓ | ✓ |
| File changes | ✓ | ✓ (edit, write, patch tools) |
| Tool calls with inputs/outputs | — | ✓ |
| Token usage | ✓ (aggregate, end-of-session) | ✓ (input, output, reasoning, cache) |
| Timestamps | ✓ | ✓ |

**Key commands:**
```bash
entire status                         # view current session state
entire checkpoint rewind              # restore to previous checkpoint
entire session resume <session-id>    # continue from a past session
entire checkpoint explain             # inspect any commit's agent context
```

**How sessions are stored:** data written to the `entire/checkpoints/v1` branch in your git repo — no hosted service, no external database. Just your repo. Visible on `entire.io` after `git push`.

**OpenCode integration note:** requires Bun runtime (used by OpenCode's plugin system). The `ingest-git` approach (`entire agent add opencode`) installs a TypeScript plugin that hooks into OpenCode's event system.

**Copilot CLI note:** `entire agent add copilot-cli` creates `.github/hooks/entire.json`, which Copilot CLI discovers and executes at key lifecycle events. The integration is in preview.

**Best practice:** commit at logical stopping points rather than having the agent auto-commit. This gives you meaningful Checkpoint granularity. PRs show `Entire-Checkpoint` trailers that reviewers can follow to view the full session.

## Related Entries
- [[github-copilot-cli]]
- [[github-copilot-app]]
- [[llm-wiki-enterprise-patterns]]

---
<!-- RU -->

## Краткое описание
Entire — CLI с открытым исходным кодом, встраивающийся в git-workflow и захватывающий полные сессии AI-агентов как «Checkpoints», связанные с git-коммитами. Позволяет видеть не только *что* написано, но и *почему*, с возможностью перемотки или возобновления любой прошлой сессии.

## Ключевые идеи
- **Checkpoint = коммит + полный контекст агента:** Каждый `git commit` создаёт Checkpoint с промптом, полной записью диалога, вызовами инструментов, изменёнными файлами, использованием токенов и временными метками — хранится в ветке `entire/checkpoints/v1`. Без внешней базы данных.
- **Решает проблему амнезии агентов:** Агенты начинают каждую сессию с нуля, повторяя одни и те же ошибки, потому что не знают истории кодовой базы. Entire даёт будущим сессиям доступ к этой истории.
- **«Почему мы написали это именно так?»** Любой коммит можно проследить до агентской сессии, его создавшей — ревьюеры видят обоснование, а не только diff. Коммиты получают git-трейлер `Entire-Checkpoint`.
- **Перемотка и возобновление:** `entire checkpoint rewind` восстанавливает предыдущий checkpoint прямо в ходе сессии. `entire session resume <id>` продолжает любую прошлую сессию, восстанавливая транскрипт.
- **Мульти-агентная поддержка:** Claude Code, Gemini CLI, OpenCode, Cursor, GitHub Copilot CLI, FactoryAI.
- **Локальный, открытый, MIT:** 3.8k+ звёзд. Объявлен seed-раунд на $60M.

## Подробнее
**Установка:**
```bash
curl -fsSL https://entire.io/install.sh | bash
entire agent add copilot-cli    # или: opencode, claude-code, cursor
copilot                          # сессии захватываются автоматически
```

**Хранение сессий:** данные пишутся в ветку `entire/checkpoints/v1` вашего репозитория — без хостинга, без внешней БД. Видны на `entire.io` после `git push`.

**Ключевые команды:**
```bash
entire status                         # состояние текущей сессии
entire checkpoint rewind              # восстановить предыдущий checkpoint
entire session resume <session-id>    # продолжить прошлую сессию
entire checkpoint explain             # изучить контекст агента для коммита
```

**Лучшая практика:** делайте коммиты в логических точках остановки, а не позволяйте агенту коммитить автоматически — это даёт осмысленную гранулярность Checkpoint. PR-ы показывают трейлеры `Entire-Checkpoint`, по которым ревьюеры переходят к полной сессии.

## Связанные записи
- [[github-copilot-cli]]
- [[github-copilot-app]]
- [[llm-wiki-enterprise-patterns]]
