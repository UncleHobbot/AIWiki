---
title: "Claude Code v2.1.150: Remote System Prompt Injection via Bootstrap API"
title_ru: "Claude Code v2.1.150: удалённая инъекция системного промпта через Bootstrap API"
category: news
tags: [claude-code, security, transparency, system-prompt, growthbook, anthropic, feature-flags]
aliases: [Claude Code bootstrap, tengu_heron_brook, Claude Code system prompt injection, remote bootstrap]
confidence: high
date: 2026-05-25
updated: 2026-05-25
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1tmizuy/claude_code_v21150_now_allows_anthropic_to/
  - https://github.com/anthropics/claude-code/issues/62061
---

## Summary
A researcher reverse-engineering the Claude Code binary discovered that v2.1.150 introduced live remote system prompt injection: at startup Claude Code calls `api.anthropic.com/api/claude_cli/bootstrap`, caches the response to disk, and injects any returned string into the LLM's system prompt. A GrowthBook feature flag (`tengu_heron_brook`) then refreshes this injected content every 60 seconds in the background.

## Key Ideas
- **Two injection points**: (1) `api.anthropic.com/api/claude_cli/bootstrap` — called at startup, cached to disk. (2) GrowthBook flag `tengu_heron_brook` — background sync every 60 seconds.
- **Shell access**: the injected content shares the same system prompt context as the core behavioral instructions — inside a session where the model has shell access.
- **Previously dead code**: prior versions had the same injection point wired in but it returned `null`. This was activated in v2.1.150, logged in the changelog as "Internal infrastructure improvements (no user-facing changes)."
- **Disable flags**: `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` blocks the network fetch; `DISABLE_GROWTHBOOK=1` disables the feature flag sync.
- **Community reaction**: split between "they already control the model, why does this matter?" and "this is an undisclosed expansion of remote control over a tool with shell access."
- **GitHub issue #62061** filed by the researcher; some community members noted Claude Code runs a remote LLM anyway, so Anthropic can influence behavior on the server side regardless.

## Details
The researcher used binary analysis (`npm pack` + `strings`) to identify two minified functions: `nAA` (reads cached bootstrap from disk) and `n0A` (fetches from network at startup). `Rv("heron_brook", () => nAA())` registers the fetched string as a section of the system prompt alongside core behavioral instructions.

The security concern is specifically the combination: (a) live remote content, (b) refreshing every 60 seconds, (c) injected into a model with full shell access on the user's machine. Previous versions had this code path but it was a no-op.

Anthropic's position, implied by the lack of changelog disclosure, is that this falls under routine infrastructure. The community note that Claude Code is a closed binary running a remote model — so Anthropic influences Claude's behavior through model updates regardless — is technically accurate but misses the local injection point.

Practically, setting `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` blocks it for security-conscious users.

## Related Entries
- [[claude-code-github-action-prompt-injection]] ([Claude Code GitHub Action: Prompt Injection Flaw](../news/claude-code-github-action-prompt-injection.md))
- [[claude-code-permission-modes]] ([Claude Code Permission Modes](../agents/claude-code-permission-modes.md))
- [[project-glasswing-anthropic-vulnerability-discovery]] ([Project Glasswing](../news/project-glasswing-anthropic-vulnerability-discovery.md))
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))

---
<!-- RU -->

## Краткое описание
Исследователь, анализировавший бинарник Claude Code, обнаружил, что в версии v2.1.150 была введена живая удалённая инъекция системного промпта: при старте Claude Code обращается к `api.anthropic.com/api/claude_cli/bootstrap`, кэширует ответ на диск и внедряет любую возвращённую строку в системный промпт модели. GrowthBook-флаг `tengu_heron_brook` обновляет этот контент каждые 60 секунд в фоне.

## Ключевые идеи
- **Две точки инъекции**: (1) `api.anthropic.com/api/claude_cli/bootstrap` — вызов при старте, кэш на диске; (2) GrowthBook-флаг `tengu_heron_brook` — фоновое обновление каждые 60 секунд.
- **Доступ к шеллу**: внедрённый контент разделяет контекст системного промпта с основными поведенческими инструкциями модели, которая имеет доступ к shell.
- **Ранее был мёртвым кодом**: в предыдущих версиях точка инъекции существовала, но возвращала `null`. В v2.1.150 активирована без явного упоминания в changelog.
- **Флаги отключения**: `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` блокирует сетевой запрос; `DISABLE_GROWTHBOOK=1` отключает синхронизацию флага.
- **Issue #62061** на GitHub — filed автором исследования.

## Подробнее
Исследователь использовал бинарный анализ для выявления двух минифицированных функций: `nAA` (читает кэш bootstrap с диска) и `n0A` (сетевой запрос при старте). `Rv("heron_brook", () => nAA())` регистрирует полученную строку как раздел системного промпта наряду с основными поведенческими инструкциями.

Проблема безопасности: сочетание живого удалённого контента, обновляемого каждые 60 секунд, с инъекцией в модель с полным доступом к shell на машине пользователя. Практически: установка `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` блокирует это для security-ориентированных пользователей.

## Связанные записи
- [[claude-code-github-action-prompt-injection]] ([Claude Code GitHub Action: Prompt Injection Flaw](../news/claude-code-github-action-prompt-injection.md))
- [[claude-code-permission-modes]] ([Claude Code Permission Modes](../agents/claude-code-permission-modes.md))
- [[project-glasswing-anthropic-vulnerability-discovery]] ([Project Glasswing](../news/project-glasswing-anthropic-vulnerability-discovery.md))
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
