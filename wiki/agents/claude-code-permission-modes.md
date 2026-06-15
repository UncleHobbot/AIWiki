---
title: "Claude Code Permission Modes"
title_ru: "Режимы прав доступа Claude Code"
category: agents
tags: [claude-code, permissions, auto-mode, plan-mode, safety, anthropic]
updated: 2026-05-16
sources:
  - https://code.claude.com/docs/en/permission-modes
---

## Summary
Claude Code's permission modes control how often it pauses to ask approval before editing files or running commands — from reviewing every action to fully autonomous execution with background safety checks.

## Key Ideas
- **Six modes:** `default` (reads only; asks for everything else), `acceptEdits` (auto-approves file edits + common filesystem commands), `plan` (reads only, proposes plan before acting), `auto` (everything with classifier safety checks), `dontAsk` (only pre-approved tools), `bypassPermissions` (no checks — containers/VMs only).
- Cycle through `default → acceptEdits → plan` with **Shift+Tab** in the CLI.
- **Auto mode** uses a separate classifier model to block scope escalation, unknown infrastructure, or hostile-content-driven actions; available on Max/Team/Enterprise plans with Sonnet 4.6+.
- **Protected paths** are never auto-approved in any mode except `bypassPermissions`: `.git`, `.vscode`, `.idea`, `.husky`, `.claude` (except `commands/`, `agents/`, `skills/`, `worktrees/`), and key dotfiles.
- Set a persistent default: `"permissions": {"defaultMode": "acceptEdits"}` in `settings.json`.
- Auto mode blocks certain actions by default: `curl | bash`, production deploys, force-push to main, mass cloud storage deletion; allows local file ops, reading `.env`, installing lock-file deps.

## Details
**Auto mode conditions stated in conversation:** if you say "don't push" or "wait until I review," the classifier treats this as a block signal until you explicitly lift it. This boundary can be lost if compaction removes the message — use a deny rule for hard guarantees.

**Auto mode fallback:** if the classifier blocks an action 3 times in a row or 20 times total in a session, auto mode pauses and prompts you. Repeated blocks usually mean the classifier lacks context about your infrastructure.

**Plan mode approval flow:** after Claude presents a plan, you can: approve and start in auto mode, approve with `acceptEdits`, approve with manual review, keep planning, or refine with Ultraplan. `Ctrl+G` opens the plan in your text editor for direct editing.

**bypassPermissions:** requires `--permission-mode bypassPermissions` or `--dangerously-skip-permissions` flag; cannot be entered from inside an already-running session; refused when running as root/sudo on Linux/macOS.

## Related Entries
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[temenos-agent-sandbox]] ([temenos — Sandbox for Agent-Executed Code](../tools/temenos-agent-sandbox.md))

---
<!-- RU -->

## Краткое описание
Режимы прав доступа Claude Code управляют тем, как часто он делает паузу для запроса разрешения перед редактированием файлов или выполнением команд — от проверки каждого действия до полностью автономного выполнения с фоновыми проверками безопасности.

## Ключевые идеи
- **Шесть режимов:** `default` (только чтение; всё остальное — с запросом), `acceptEdits` (авто-одобрение правок файлов + обычных файловых команд), `plan` (только чтение, предлагает план перед действиями), `auto` (всё с проверками безопасности классификатором), `dontAsk` (только предварительно разрешённые инструменты), `bypassPermissions` (без проверок — только в контейнерах/VM).
- Переключение `default → acceptEdits → plan` через **Shift+Tab** в CLI.
- **Auto режим** использует отдельную модель-классификатор для блокировки расширения области, неизвестной инфраструктуры или действий, вызванных враждебным контентом; доступен на тарифах Max/Team/Enterprise с Sonnet 4.6+.
- **Защищённые пути** не авто-одобряются ни в каком режиме, кроме `bypassPermissions`: `.git`, `.vscode`, `.idea`, `.husky`, `.claude` (кроме `commands/`, `agents/`, `skills/`, `worktrees/`) и ключевые dotfiles.
- Постоянный режим по умолчанию: `"permissions": {"defaultMode": "acceptEdits"}` в `settings.json`.
- Авто-режим по умолчанию блокирует: `curl | bash`, деплой в продакшн, force-push в main, массовое удаление в облачном хранилище; разрешает: локальные операции с файлами, чтение `.env`, установку зависимостей из lock-файла.

## Подробнее
**Границы, заявленные в разговоре в авто-режиме:** если вы написали «не пушить» или «подожди, пока я не проверю», классификатор воспринимает это как сигнал блокировки до явной отмены. Эта граница может быть потеряна при сжатии контекста — для жёстких гарантий используйте правило deny.

**Откат авто-режима:** если классификатор 3 раза подряд или 20 раз суммарно заблокировал действие, авто-режим приостанавливается и выводит запрос. Повторные блокировки обычно означают, что классификатору не хватает информации о вашей инфраструктуре.

**Процесс одобрения плана в plan-режиме:** после представления плана Claude предлагает варианты: одобрить и запустить в авто-режиме, одобрить с `acceptEdits`, одобрить с ручной проверкой каждого изменения, продолжить планирование или уточнить через Ultraplan. `Ctrl+G` открывает план в текстовом редакторе для прямого редактирования.

**bypassPermissions:** требует флага `--permission-mode bypassPermissions` или `--dangerously-skip-permissions`; нельзя войти из уже запущенной сессии; отклоняется при запуске от root/sudo на Linux/macOS.

## Связанные записи
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[temenos-agent-sandbox]] ([temenos — песочница для кода, выполняемого агентами](../tools/temenos-agent-sandbox.md))
