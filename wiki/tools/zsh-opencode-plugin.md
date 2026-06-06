---
title: "zsh-opencode-plugin"
title_ru: "zsh-opencode-plugin"
category: tools
tags: [opencode, zsh, shell, cli, plugin, oh-my-zsh, completions, aliases]
aliases: [opencode zsh plugin, mskadu zsh-opencode]
confidence: high
date: 2026-06-06
updated: 2026-06-06
sources:
  - https://github.com/mskadu/zsh-opencode-plugin
---

## Summary
A zsh plugin for the opencode AI coding agent providing 50+ aliases, tab-completion, and oh-my-zsh compatibility. All aliases use the `oc` prefix with a mnemonic naming scheme.

## Key Ideas
- All aliases use `oc` prefix with a systematic naming scheme: 1 letter = flag, 2 letters = subcommand, 3+ letters = subcommand + flag.
- Provides tab-completion for all opencode commands and flags, cached on first shell startup.
- Fully compatible with oh-my-zsh (add `opencode` to plugins array) or standalone (source directly).
- Covers the full opencode CLI surface: TUI launch, session management, model selection, MCP server management, auth, export/import, stats, debugging, GitHub agent, and more.
- Key aliases: `oc` (launch TUI), `occ` (continue session), `ocr` (non-interactive run), `ocmo` (list models), `ocst` (usage stats).

## Details
The plugin (`opencode.plugin.zsh`) is a single shell script that defines aliases and manages completion caching. It requires opencode CLI on `$PATH` and zsh 5.1+. For oh-my-zsh users, installation is adding `opencode` to the `plugins=()` array. Standalone users source the plugin file directly from `.zshrc`.

The alias naming convention is designed for discoverability. After `oc`, the letters map to opencode subcommands and flags: `ocm` = `--model`, `ocr` = `run`, `ocmo` = `models`, `ocmor` = `models --refresh`. Common verbs from other tools are included: `oclogin`, `oclogout`.

Tab-completion runs `opencode completion zsh` on first startup and caches the result to `$ZSH_CACHE_DIR/completions/_opencode`. Oh-my-zsh sets this automatically; standalone shells fall back to `$HOME/.cache/zsh`.

## Notable Quotes
> "All aliases use the `oc` prefix. The scheme helps you guess them." — README

## Related Entries
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[cpt-copilot-terminal]] ([CPT Copilot Terminal](../tools/cpt-copilot-terminal.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))

---
<!-- RU -->

## Краткое описание
Плагин zsh для AI-кодинг-агента opencode с 50+ алиасами, таб-комплитном и совместимостью с oh-my-zsh. Все алиасы используют префикс `oc` с мнемонической схемой именования.

## Ключевые идеи
- Все алиасы используют префикс `oc` с систематической схемой: 1 буква = флаг, 2 буквы = подкоманда, 3+ букв = подкоманда + флаг.
- Предоставляет таб-комплит для всех команд и флагов opencode, кэшируемый при первом запуске оболочки.
- Полная совместимость с oh-my-zsh (добавить `opencode` в массив plugins) или автономное использование (source напрямую).
- Покрывает весь CLI opencode: запуск TUI, управление сессиями, выбор моделей, управление MCP-серверами, авторизацию, экспорт/импорт, статистику, отладку, GitHub-агент и многое другое.
- Ключевые алиасы: `oc` (запуск TUI), `occ` (продолжить сессию), `ocr` (неинтерактивный запуск), `ocmo` (список моделей), `ocst` (статистика использования).

## Подробнее
Плагин (`opencode.plugin.zsh`) — это один shell-скрипт, определяющий алиасы и управляющий кэшированием комплишенов. Требует opencode CLI в `$PATH` и zsh 5.1+. Для пользователей oh-my-zsh установка заключается в добавлении `opencode` в массив `plugins=()`. Автономные пользователи подключают файл плагина через `source` в `.zshrc`.

Соглашение об именовании алиасов разработано для удобства запоминания. После `oc` буквы соответствуют подкомандам и флагам opencode: `ocm` = `--model`, `ocr` = `run`, `ocmo` = `models`, `ocmor` = `models --refresh`.

Таб-комплит выполняет `opencode completion zsh` при первом запуске и кэширует результат в `$ZSH_CACHE_DIR/completions/_opencode`. Oh-my-zsh устанавливает эту переменную автоматически; автономные оболочки используют `$HOME/.cache/zsh`.

## Примечательные цитаты
> «Все алиасы используют префикс `oc`. Схема помогает угадывать их.» — README

## Связанные записи
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[cpt-copilot-terminal]] ([CPT Copilot Terminal](../tools/cpt-copilot-terminal.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
