---
title: "Agent Lifecycle Hooks in Copilot CLI and Claude Code"
title_ru: "Хуки жизненного цикла агента в Copilot CLI и Claude Code"
category: tips
tags: [hooks, agent-lifecycle, github-copilot, claude-code, pre-tool-use, eslint, context-injection, deterministic]
aliases: [agent hooks, copilot hooks, claude code hooks, PreToolUse hook, lifecycle events]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.youtube.com/watch?v=03CfGf9iw_U
---

## Summary

Hooks are deterministic event handlers that fire at specific points in the AI agent lifecycle. Unlike the model itself, hooks run predictably — you control when they fire. The most powerful hook is `PreToolUse`, which can block file writes until code passes a linter, forcing the AI to produce correct code rather than move on with errors.

## Key Ideas

- **Hooks fire deterministically** — not based on model decisions, so they can be used for guardrails and quality gates without relying on the AI to self-enforce
- **`PreToolUse` is the most valuable hook**: it can deny tool calls (e.g., block a file write if ESLint fails), forcing the model to fix issues before continuing
- **Context injection via `SessionStart`**: inject env info (Node version, OS details) at session start so the model doesn't need to run tool calls to discover it
- **Hooks are just JSON files**: place them in `.github/hooks/` or your user profile's `.copilot`/`.cloud` folders
- **Seven lifecycle events**: SessionStart, UserPromptSubmitted, PreToolUse, PostToolUse, SubAgentStart, SubAgentStop, ErrorOccurred

## Details

The agent lifecycle runs: user sends prompt → agent loop starts (reasoning → tool calls → sub-agents → reasoning) → response. Hooks attach commands to specific points in this loop. Each hook runs as a Bash or PowerShell script; the script receives a JSON payload about the current event (prompt text, tool being called, file being written, etc.).

Only some hooks are "blocking" — `PreToolUse` is the main one that can return a "deny" response to prevent the tool call from executing. This is used to implement quality gates: the hook checks if the file the agent is about to write passes ESLint; if not, it returns `{deny: true, reason: "lint errors"}`, and the model is forced to try again. This creates a loop where the agent cannot move to another file until the current file lints cleanly.

For `SessionStart` context injection, the script runs `node --version` and returns `{additionalContext: "User's Node version is 20.11.0"}` as JSON. The model then knows this without making a tool call. Other useful injections: OS type, active git branch, recent terminal errors.

Hooks are currently in experimental/preview mode in VS Code — they must be enabled in User Settings. The Copilot CLI picks up hook changes only after `/new` (restart); VS Code hot-reloads them without restart.

## Video Notes

- [0:25] Agent loop overview: prompt → reasoning → tool calls → sub-agents → response
- [2:11] Seven hook event types with explanations
- [4:48] Setting up hooks in VS Code; hooks as JSON files
- [6:15] Creating first hook: `UserPromptSubmitted` with echo command
- [9:15] Logging hook output to a file; `currentWorkingDirectory` config
- [14:40] Injecting Node version via `SessionStart` hook
- [17:01] ESLint gate using `PreToolUse` — the recommended pattern for all projects

## Related Entries

- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[github-copilot-cli-best-practices]] ([GitHub Copilot CLI Best Practices](../tips/github-copilot-cli-best-practices.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions Overview](../agents/claude-code-extensions-overview.md))

---
<!-- RU -->

## Краткое описание

Хуки — это детерминированные обработчики событий, которые срабатывают в конкретных точках жизненного цикла AI-агента. Самый мощный — `PreToolUse`, который может блокировать запись файлов до прохождения линтера, заставляя модель писать правильный код.

## Ключевые идеи

- **Хуки срабатывают детерминированно** — не по решению модели, поэтому подходят для качественных ворот без зависимости от самоконтроля AI
- **`PreToolUse` — самый ценный хук**: может отклонять вызовы инструментов (например, запись файла при ошибках ESLint), вынуждая модель исправить код перед продолжением
- **Инъекция контекста через `SessionStart`**: передайте данные окружения (версию Node, ОС) в начале сессии, чтобы модель не делала лишних инструментальных вызовов
- **Хуки — просто JSON-файлы**: помещаются в `.github/hooks/` или пользовательский профиль `.copilot`/`.cloud`
- **Семь событий жизненного цикла**: SessionStart, UserPromptSubmitted, PreToolUse, PostToolUse, SubAgentStart, SubAgentStop, ErrorOccurred

## Подробнее

Жизненный цикл агента: пользователь отправляет промпт → цикл агента (рассуждение → вызовы инструментов → субагенты → рассуждение) → ответ. Хуки привязывают команды к конкретным точкам этого цикла. Каждый хук выполняется как скрипт Bash или PowerShell и получает JSON-пейлоад о текущем событии.

Только некоторые хуки являются "блокирующими" — главный из них `PreToolUse`. Используется для ESLint-ворот: хук проверяет, проходит ли файл линтер; если нет — возвращает `{deny: true}`, и модель вынуждена повторять попытку. Агент не может перейти к другому файлу, пока текущий не проходит линтинг.

## Заметки по видео

- [2:11] Семь типов хук-событий с пояснениями
- [14:40] Инъекция версии Node через хук `SessionStart`
- [17:01] ESLint-ворота через `PreToolUse` — рекомендуемый паттерн для всех проектов

## Связанные записи

- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[github-copilot-cli-best-practices]] ([GitHub Copilot CLI Best Practices](../tips/github-copilot-cli-best-practices.md))
- [[claude-code-extensions-overview]] ([Claude Code Extensions Overview](../agents/claude-code-extensions-overview.md))
