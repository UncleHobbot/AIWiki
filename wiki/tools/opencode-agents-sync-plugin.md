---
title: "opencode-agents-sync: Auto-Updating AGENTS.md After Compaction"
title_ru: "opencode-agents-sync: автообновление AGENTS.md после compaction"
category: tools
tags: [opencode, plugin, agents-md, context-management, compaction, mimo-code]
aliases: [ozgurulukir/opencode-agents-sync]
confidence: low
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/opencode/comments/1u4yaiq/showcase_opencodeagentssync_autoupdate_your/
  - https://www.reddit.com/r/opencodeCLI/comments/1u4yay6/showcase_opencodeagentssync_autoupdate_your/
  - https://github.com/ozgurulukir/opencode-agents-sync
---

## Summary
opencode-agents-sync is an OpenCode plugin that automatically refreshes a project's `AGENTS.md` file after context auto-compaction, having the LLM consolidate new discoveries and remove duplicates so the next session starts with up-to-date project knowledge.

## Key Ideas
- Fires after OpenCode's `experimental.compaction.autocontinue` auto-compaction event.
- Sends a dedicated prompt through the normal agent loop (with full tool access) so the LLM can read, merge, and rewrite `AGENTS.md` directly.
- Includes "cascade prevention" so it won't trigger an infinite loop on repeated compactions.
- Custom prompt template with hot reload — drop a new template file and it applies without restarting.
- When restarting OpenCode with `-c` (continue) or starting a new session, the project-level `AGENTS.md` already contains the latest consolidated notes.
- Tested with OpenCode v1.14.48 and MiMo Code v0.1.0, suggesting compatibility with OpenCode forks.
- Installed via symlink into the `plugins/` directory.

## Details
The plugin targets a common pain point in long agent sessions: once context gets compacted, hard-won discoveries about the codebase (conventions, gotchas, file locations) tend to be lost or have to be re-derived. By hooking into the compaction lifecycle, opencode-agents-sync turns `AGENTS.md` into a living memory file that gets curated automatically by the agent itself, rather than requiring the developer to manually update it.

The author cross-posted to both r/opencode and r/opencodeCLI under "[Showcase]". This is a small, early community plugin (Tier 3 — Reddit/GitHub self-promotion) but addresses a real architectural gap that other "agent memory" tools (e.g. Memgram) are also trying to solve from different angles — one via plugin-driven file curation, the other via an external vector-store memory layer.

## Related Entries
- [[mimo-code-xiaomi-opencode-fork]] ([MiMo Code](../tools/mimo-code-xiaomi-opencode-fork.md))
- [[zsh-opencode-plugin]] ([zsh-opencode-plugin](../tools/zsh-opencode-plugin.md))

---
<!-- RU -->

## Краткое описание
opencode-agents-sync — плагин для OpenCode, который автоматически обновляет файл `AGENTS.md` проекта после auto-compaction контекста: LLM сама объединяет новые находки и удаляет дубликаты, чтобы следующая сессия начиналась с актуальных знаний о проекте.

## Ключевые идеи
- Срабатывает после события auto-compaction (`experimental.compaction.autocontinue`) в OpenCode.
- Отправляет специальный промпт через обычный agent loop (с полным доступом к инструментам), чтобы LLM могла прочитать, объединить и перезаписать `AGENTS.md`.
- Включает защиту от "каскадов" — не запускается в бесконечном цикле при повторных compaction.
- Кастомный шаблон промпта с hot reload — новый файл шаблона применяется без перезапуска.
- При перезапуске OpenCode с флагом `-c` (continue) или старте новой сессии `AGENTS.md` уже содержит свежие консолидированные заметки.
- Протестирован с OpenCode v1.14.48 и MiMo Code v0.1.0, что говорит о совместимости с форками OpenCode.
- Устанавливается через симлинк в директорию `plugins/`.

## Подробнее
Плагин решает распространённую проблему длинных agent-сессий: после compaction контекста ценные находки о кодовой базе (соглашения, особенности, расположение файлов) часто теряются или их приходится выводить заново. Подключаясь к жизненному циклу compaction, opencode-agents-sync превращает `AGENTS.md` в "живой" файл памяти, который агент сам курирует автоматически — без необходимости вручную обновлять его разработчиком.

Автор опубликовал пост одновременно в r/opencode и r/opencodeCLI с тегом "[Showcase]". Это небольшой ранний community-плагин (источник tier 3 — самопродвижение на Reddit/GitHub), но он решает реальный архитектурный разрыв, который другие инструменты "agent memory" (например, Memgram) также пытаются закрыть с другой стороны — один через курирование файлов плагином, другой через внешний слой памяти на векторной БД.

## Связанные записи
- [[mimo-code-xiaomi-opencode-fork]] ([MiMo Code](../tools/mimo-code-xiaomi-opencode-fork.md))
- [[zsh-opencode-plugin]] ([zsh-opencode-plugin](../tools/zsh-opencode-plugin.md))
