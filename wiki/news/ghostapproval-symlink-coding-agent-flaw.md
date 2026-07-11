---
title: "GhostApproval — Symlink Flaws Let Malicious Repos Hijack AI Coding Agents"
title_ru: "GhostApproval — уязвимости symlink позволяют вредоносным репо перехватывать ИИ-кодинг-агентов"
category: news
tags: [symlink, coding-agent, claude-code, codex, amazon-q, supply-chain, wiz, security]
aliases: [GhostApproval, ghost approval symlink, symlink coding agent]
confidence: high
date: 2026-07-10
updated: 2026-07-11
sources:
  - https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html
---

## Summary
Wiz Research disclosed **GhostApproval**, a class of symlink-handling flaws in AI coding agents (Claude Code, Amazon Q Developer, Codex) that lets a malicious repository trick the agent into writing to sensitive locations — SSH keys, shell startup files (`~/.zshrc`, `~/.bashrc`) — while the UI shows a benign project-local path. It is the symlink analogue of the [[duneslide-cursor-sandbox-escape]] file-write escapes and the [[amazon-q-mcp-config-rce]] repo-config pattern.

## Key Ideas
- **Mechanism — symlink redirection:** a repo contains a symlink whose displayed path looks project-local, but whose resolved target points outside the workspace (e.g. `~/.ssh/authorized_keys`, `~/.zshrc`). When the agent writes "inside the project," it actually writes to the attacker's target.
- **Why it slips past review:** the agent (and the user reviewing diffs) sees the *project-relative* path in the UI; the dangerous resolved path is invisible.
- **Affected:** Claude Code, Amazon Q Developer, Codex — the major coding agents. All have since shipped fixes.
- **Impact:** persistence on the developer's host — next shell start, next SSH login — without needing a separate code-execution primitive.
- **Pattern continuity:** same root cause as DuneSlide's CVE-2026-50549 (Cursor symlink-resolution fallback) and the repo-config-as-RCE class ([[amazon-q-mcp-config-rce]]): the agent trusts filesystem layout from untrusted sources.

## Details
GhostApproval belongs to the growing family of "the repo is the attack" flaws. The shared lesson: any filesystem path an agent resolves from repository content is untrusted input, and the resolved target must be checked against the project boundary *before* writing. The symlink variant is especially dangerous because the UI lie (project path shown, system path written) defeats manual review of diffs.

## Related Entries
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](duneslide-cursor-sandbox-escape.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[guardfall-coding-agent-shell-injection]] ([GuardFall Coding Agent Shell Injection](guardfall-coding-agent-shell-injection.md))
- [[skill-md-supply-chain-risks]] ([Agent Skills Supply-Chain Risks](skill-md-supply-chain-risks.md))

---
<!-- RU -->

## Краткое описание
Wiz Research раскрыла **GhostApproval** — класс уязвимостей обработки symlink в ИИ-кодинг-агентах (Claude Code, Amazon Q Developer, Codex), позволяющий вредоносному репозиторию заставить агента писать в чувствительные места — SSH-ключи, стартовые файлы оболочки (`~/.zshrc`, `~/.bashrc`) — пока в UI отображается безобидный локальный путь проекта. Это symlink-аналог файловых побегов DuneSlide.

## Ключевые идеи
- **Механизм — перенаправление symlink:** репо содержит symlink, отображаемый путь которого выглядит как локальный, но цель указывает вне воркспейса. Агент «пишет внутри проекта», фактически записывая в цель атакующего.
- **Почему проходит ревью:** агент и пользователь видят *проектный* путь; опасный резолвенный путь невидим.
- **Затронуты:** Claude Code, Amazon Q Developer, Codex — все выпустили фиксы.
- **Влияние:** персистентность на хосте разработчика — следующий старт оболочки, следующий SSH-логин.
- **Преемственность:** тот же корень, что у CVE-2026-50549 DuneSlide и класса repo-config-as-RCE ([[amazon-q-mcp-config-rce]]).

## Подробнее
GhostApproval входит в растущее семейство «репо — это атака». Общий урок: любой путь, который агент резолвит из контента репозитория, — недоверенный ввод, и резолвленную цель надо проверять против границы проекта *до* записи. Symlink-вариант опасен тем, что UI-ложь (проектный путь показан, системный записан) побеждает ручное ревью диффов.

## Связанные записи
- [[duneslide-cursor-sandbox-escape]] ([DuneSlide Cursor Sandbox Escape](duneslide-cursor-sandbox-escape.md))
- [[amazon-q-mcp-config-rce]] ([Amazon Q MCP Config RCE](amazon-q-mcp-config-rce.md))
- [[guardfall-coding-agent-shell-injection]] ([GuardFall Coding Agent Shell Injection](guardfall-coding-agent-shell-injection.md))
- [[skill-md-supply-chain-risks]] ([Agent Skills Supply-Chain Risks](skill-md-supply-chain-risks.md))
