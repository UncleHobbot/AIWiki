---
title: "Claude Code Memory: CLAUDE.md and Auto Memory"
title_ru: "Память Claude Code: CLAUDE.md и автопамять"
category: agents
tags: [claude-code, memory, claude-md, auto-memory, context, anthropic]
updated: 2026-05-16
sources:
  - https://code.claude.com/docs/en/memory
---

## Summary
Claude Code persists knowledge across sessions through two complementary systems: CLAUDE.md files (instructions you write) and auto memory (notes Claude writes itself based on your patterns and corrections).

## Key Ideas
- **CLAUDE.md** — you write it; contains instructions and rules; loaded into every session in full (target under 200 lines).
- **Auto memory** — Claude writes it automatically; contains build commands, debugging insights, preferences Claude discovers; stored in `~/.claude/projects/<project>/memory/`.
- Both load at session start; Claude treats them as context, not enforced configuration — specific and concise instructions work best.
- CLAUDE.md can import other files with `@path/to/file` syntax; imports expand at launch but still cost tokens.
- **Path-scoped rules** (`.claude/rules/` with YAML `paths:` frontmatter) only load when Claude opens matching files — save context on large projects.
- Use `/memory` to browse loaded CLAUDE.md files, toggle auto memory, and open memory files in your editor.
- Project-root CLAUDE.md **survives compaction** (re-read from disk); nested subdirectory CLAUDE.md files do not — they reload when matching files are next opened.

## Details
**CLAUDE.md scope hierarchy** (load order, broadest → most specific):
1. Managed policy (`C:\Program Files\ClaudeCode\CLAUDE.md` on Windows) — org-wide, cannot be excluded
2. User (`~/.claude/CLAUDE.md`) — personal, all projects
3. Project (`./CLAUDE.md` or `./.claude/CLAUDE.md`) — team-shared via git
4. Local (`./CLAUDE.local.md`) — personal project-specific, gitignored

**When to add to CLAUDE.md:** when Claude makes the same mistake twice; when a review catches something Claude should have known; when you type the same correction two sessions in a row.

**Auto memory storage:** `MEMORY.md` acts as an index (first 200 lines / 25KB loaded every session); detailed notes go into separate topic files (e.g. `debugging.md`) read on demand. Auto memory is machine-local and shared across all worktrees of the same git repo.

**Troubleshooting:** run `/memory` to verify files are loaded; make instructions more specific; check for conflicting rules across CLAUDE.md files. If instruction is lost after `/compact`, put it in CLAUDE.md not just in conversation.

## Related Entries
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-code-directory]] ([The .claude Directory](../agents/claude-code-directory.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))

---
- [[packmind-local-second-brain]] ([PackMind](../tools/packmind-local-second-brain.md))
<!-- RU -->

## Краткое описание
Claude Code сохраняет знания между сессиями через две взаимодополняющие системы: файлы CLAUDE.md (инструкции, которые пишете вы) и автопамять (заметки, которые Claude делает сам на основе ваших паттернов и исправлений).

## Ключевые идеи
- **CLAUDE.md** — вы пишете его сами; содержит инструкции и правила; загружается в каждую сессию полностью (рекомендуется до 200 строк).
- **Автопамять** — Claude ведёт её автоматически; содержит команды сборки, инсайты по отладке, предпочтения, которые Claude обнаруживает; хранится в `~/.claude/projects/<проект>/memory/`.
- Оба механизма загружаются при старте сессии; Claude воспринимает их как контекст, а не как принудительную конфигурацию — конкретные и краткие инструкции работают лучше всего.
- CLAUDE.md может импортировать другие файлы синтаксисом `@путь/к/файлу`; импорты разворачиваются при запуске, но всё равно расходуют токены.
- **Правила с привязкой к путям** (`.claude/rules/` с frontmatter `paths:`) загружаются только при открытии соответствующих файлов — экономят контекст в больших проектах.
- Используйте `/memory` для просмотра загруженных CLAUDE.md-файлов, переключения автопамяти и открытия файлов памяти в редакторе.
- Корневой CLAUDE.md проекта **переживает уплотнение контекста** (перечитывается с диска); вложенные CLAUDE.md в поддиректориях — нет, они перезагрузятся при следующем открытии соответствующих файлов.

## Подробнее
**Иерархия областей CLAUDE.md** (порядок загрузки, от широкой к узкой):
1. Managed policy (`C:\Program Files\ClaudeCode\CLAUDE.md` на Windows) — для всей организации, нельзя исключить
2. Пользователь (`~/.claude/CLAUDE.md`) — личный, все проекты
3. Проект (`./CLAUDE.md` или `./.claude/CLAUDE.md`) — командный, через git
4. Локальный (`./CLAUDE.local.md`) — личный для данного проекта, в gitignore

**Когда добавлять в CLAUDE.md:** когда Claude дважды делает одну и ту же ошибку; когда ревью выявляет то, что Claude должен был знать; когда вы вводите одно и то же исправление в двух разных сессиях.

**Хранение автопамяти:** `MEMORY.md` служит индексом (первые 200 строк / 25 КБ загружаются каждую сессию); подробные заметки идут в отдельные тематические файлы (например, `debugging.md`), читаемые по запросу. Автопамять локальна для машины и общая для всех рабочих деревьев одного git-репозитория.

**Диагностика:** запустите `/memory` для проверки загружённых файлов; конкретизируйте инструкции; проверьте конфликты правил между CLAUDE.md-файлами. Если инструкция теряется после `/compact`, поместите её в CLAUDE.md, а не только в разговор.

## Связанные записи
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-code-directory]] ([The .claude Directory](../agents/claude-code-directory.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions: Skills, MCP, Hooks, Subagents](../agents/claude-code-extensions-overview.md))
