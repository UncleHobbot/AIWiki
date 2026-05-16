---
title: "The .claude Directory"
title_ru: "Директория .claude"
category: agents
tags: [claude-code, configuration, directory-structure, settings, anthropic]
updated: 2026-05-16
sources:
  - https://code.claude.com/docs/en/claude-directory
---

## Summary
Claude Code reads all configuration — CLAUDE.md, settings, skills, hooks, subagents, rules, and auto memory — from `.claude/` in your project and from `~/.claude/` in your home directory.

## Key Ideas
- **Project files** (`.claude/`) are committed to git and shared with the team; **global files** (`~/.claude/`) apply across all projects.
- Key files: `CLAUDE.md` (instructions), `settings.json` (permissions/hooks/env), `skills/<name>/SKILL.md` (reusable prompts), `agents/*.md` (subagent definitions), `.mcp.json` (team MCP servers), `rules/*.md` (path-scoped rules).
- `settings.local.json` is auto-gitignored — use it for personal overrides that shouldn't be shared.
- Auto memory lives in `~/.claude/projects/<project>/memory/MEMORY.md`; topic files (e.g. `debugging.md`) are read on demand.
- Session transcripts, file snapshots, and prompt history accumulate in `~/.claude/` and are cleaned up after `cleanupPeriodDays` (default: 30 days).
- Run `claude project purge` to delete all state for a project (transcripts, auto memory, task lists).

## Details
**Quick reference — which file to edit:**

| You want to | Edit |
|---|---|
| Give Claude project context | `CLAUDE.md` |
| Allow/block specific tool calls | `settings.json` permissions or hooks |
| Run a script before/after tool calls | `settings.json` hooks |
| Set environment variables | `settings.json` env |
| Keep personal overrides out of git | `settings.local.json` |
| Add a `/name` command | `skills/<name>/SKILL.md` |
| Define a specialized subagent | `agents/*.md` |
| Connect external tools over MCP | `.mcp.json` |

**Plaintext warning:** Transcripts are not encrypted at rest. OS file permissions are the only protection. If a tool reads a `.env` file or prints a credential, that value lands in the session JSONL. To reduce exposure: lower `cleanupPeriodDays`, set `CLAUDE_CODE_SKIP_PROMPT_HISTORY=1`, or use deny rules for credential files.

## Related Entries
- [[claude-code-extensions-overview]]
- [[claude-code-memory]]

---
<!-- RU -->

## Краткое описание
Claude Code читает всю конфигурацию — CLAUDE.md, настройки, навыки, хуки, подагентов, правила и автопамять — из `.claude/` в вашем проекте и из `~/.claude/` в домашней директории.

## Ключевые идеи
- **Файлы проекта** (`.claude/`) коммитятся в git и доступны команде; **глобальные файлы** (`~/.claude/`) применяются ко всем проектам.
- Ключевые файлы: `CLAUDE.md` (инструкции), `settings.json` (права/хуки/env), `skills/<name>/SKILL.md` (повторно используемые промпты), `agents/*.md` (определения подагентов), `.mcp.json` (командные MCP-серверы), `rules/*.md` (правила с привязкой к путям).
- `settings.local.json` автоматически добавляется в `.gitignore` — используйте для личных переопределений, которые не нужно публиковать.
- Автопамять хранится в `~/.claude/projects/<проект>/memory/MEMORY.md`; тематические файлы (например, `debugging.md`) читаются по запросу.
- Транскрипты сессий, снимки файлов и история промптов накапливаются в `~/.claude/` и удаляются через `cleanupPeriodDays` (по умолчанию: 30 дней).
- Команда `claude project purge` удаляет все данные состояния для проекта (транскрипты, автопамять, списки задач).

## Подробнее
**Быстрый справочник — какой файл редактировать:**

| Что нужно сделать | Редактировать |
|---|---|
| Дать Claude контекст проекта | `CLAUDE.md` |
| Разрешить/заблокировать вызовы инструментов | permissions или hooks в `settings.json` |
| Запускать скрипт до/после вызовов инструментов | hooks в `settings.json` |
| Задать переменные окружения | env в `settings.json` |
| Личные переопределения без публикации | `settings.local.json` |
| Добавить команду `/имя` | `skills/<имя>/SKILL.md` |
| Определить специализированного подагента | `agents/*.md` |
| Подключить внешние инструменты через MCP | `.mcp.json` |

**Предупреждение о plaintext:** транскрипты не шифруются в состоянии покоя. Единственная защита — права доступа ОС. Если инструмент прочитает файл `.env` или выведет учётные данные, это попадёт в JSONL сессии. Для снижения рисков: уменьшите `cleanupPeriodDays`, установите `CLAUDE_CODE_SKIP_PROMPT_HISTORY=1` или используйте правила deny для файлов с учётными данными.

## Связанные записи
- [[claude-code-extensions-overview]]
- [[claude-code-memory]]
