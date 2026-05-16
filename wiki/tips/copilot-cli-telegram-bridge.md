---
title: "Using Telegram as a Mobile Front-End for GitHub Copilot CLI"
title_ru: "Telegram как мобильный фронтенд для GitHub Copilot CLI"
category: tips
tags: [github-copilot, telegram, mobile, remote-dev, cli, security, extension]
updated: 2026-05-15
sources:
  - https://codewithdan.com/using-telegram-with-github-copilot-cli/
  - https://x.com/DanWahlin/status/2054948983747883151
---

## Summary
Using the `examon/copilot-cli-telegram-bridge` extension, you can send prompts to a running Copilot CLI session from your phone via Telegram and get responses back — enabling real coding agent work without a terminal in front of you.

## Key Ideas
- **Proper integration, not PTY streaming:** The bridge uses `joinSession` from `@github/copilot-sdk/extension` — it relays messages to the active Copilot CLI session rather than screen-scraping a terminal, so output is clean chat text, not ANSI escape sequences.
- **Install in 3 steps:** Enable experimental mode (`/experimental on`), install the plugin (`/plugin install examon/copilot-cli-telegram-bridge`), create a Telegram bot via @BotFather, then run `/telegram setup <name>` and `/telegram connect <name>` inside Copilot CLI.
- **Security is the critical concern:** The bot token is stored in plain text in `bots.json` (mode 600). A Telegram bot wired to a coding agent is effectively remote developer access — treat it as such. Lock to your Telegram user ID via `access.json`; never share the bot or use it in a group chat.
- **Permission flags matter:** Use `--allow-all-tools` + explicit `--deny-tool` patterns for the safer option, or `--yolo` (all tools/paths/URLs) in a disposable isolated VM only.
- **Gotcha — slash commands:** Copilot CLI slash commands like `/model` don't route through the CLI router via Telegram. Use them directly in the terminal session.
- **Gotcha — approval hangs:** Without `--yolo`, tool approval prompts don't surface cleanly through Telegram — the session appears to "type forever." Mitigate with permissive allow/deny flags or run in `--yolo` mode with appropriate isolation.

## Details
Dan Wahlin (Microsoft) documented this setup after using it during a family vacation in Spain — checking in on a project and adding features from his phone during downtime, without needing a terminal or iPad.

**Full setup flow:**
1. Inside Copilot CLI: `/experimental on`
2. `/plugin install examon/copilot-cli-telegram-bridge` → restart Copilot CLI → run `/copilot-cli-telegram-bridge:telegram-install` → restart again
3. Create bot with @BotFather → copy token (never paste it in code, docs, or chat)
4. `/telegram setup <botname>` → paste token when prompted (extension intercepts, validates, stores to `bots.json`, redacts from agent)
5. `/telegram connect <botname>` → send pairing code from Telegram to complete ID binding

**Safe launch command (constrained):**
```
copilot --experimental --allow-all-tools \
  --add-dir ~/projects/my-project \
  --allow-url github.com --allow-url api.github.com \
  --deny-tool='shell(git push)' --deny-tool='shell(rm)' \
  --deny-tool='shell(sudo)' \
  --model gpt-5.5 --no-remote --disallow-temp-dir \
  --secret-env-vars=TELEGRAM_BOT_TOKEN,GITHUB_TOKEN
```

**Permissive launch command (isolated VM only):**
```
copilot --experimental --yolo --model gpt-5.5 \
  --no-remote --disallow-temp-dir \
  --secret-env-vars=TELEGRAM_BOT_TOKEN,GITHUB_TOKEN
```

**Key security rules:**
- `bots.json` and `access.json` — keep mode 600, never commit, never cloud-sync
- `access.json` is shared across all bots in the extension dir — one pairing grants access to all registered bots
- Don't send prompts or outputs containing secrets, customer data, or proprietary code through Telegram (goes through Telegram's Bot API)
- Re-check the exact commit you install before running any extension

## Related Entries
- [[github-copilot-cli]]
- [[github-copilot-app]]

---
<!-- RU -->

## Краткое описание
С помощью расширения `examon/copilot-cli-telegram-bridge` можно отправлять промпты в запущенную сессию Copilot CLI прямо с телефона через Telegram и получать ответы обратно — полноценная работа с агентом без терминала под рукой.

## Ключевые идеи
- **Интеграция, а не PTY-стриминг:** Мост использует `joinSession` из `@github/copilot-sdk/extension` — он передаёт сообщения активной сессии Copilot CLI, а не считывает вывод терминала, поэтому ответы — чистый текст чата без ANSI-последовательностей.
- **Установка в 3 шага:** Включить экспериментальный режим (`/experimental on`), установить плагин (`/plugin install examon/copilot-cli-telegram-bridge`), создать бота Telegram через @BotFather, затем выполнить `/telegram setup <name>` и `/telegram connect <name>` внутри Copilot CLI.
- **Безопасность — ключевая проблема:** Токен бота хранится в открытом виде в `bots.json` (права 600). Telegram-бот, подключённый к агенту для кодирования — это фактически удалённый доступ разработчика. Ограничьте его своим Telegram user ID через `access.json`; никогда не используйте в групповых чатах.
- **Флаги разрешений важны:** Используйте `--allow-all-tools` с явными `--deny-tool` для более безопасного варианта, или `--yolo` (все инструменты/пути/URL) только в одноразовой изолированной VM.
- **Подводный камень — команды со слэшем:** Команды Copilot CLI вроде `/model` не маршрутизируются через CLI-роутер через Telegram. Используйте их напрямую в терминальной сессии.
- **Подводный камень — зависание на одобрении:** Без `--yolo` запросы на одобрение инструментов не всплывают чисто через Telegram — сессия выглядит как «бесконечно печатает».

## Подробнее
Дэн Уолин (Microsoft) задокументировал этот процесс настройки после использования во время семейного отпуска в Испании — он проверял проект и добавлял функции с телефона во время пауз.

**Правила безопасности:**
- `bots.json` и `access.json` — права 600, никогда не коммитить, не синхронизировать с облаком
- `access.json` общий для всех ботов в директории расширения — одно сопряжение даёт доступ ко всем зарегистрированным ботам
- Не отправляйте промпты или ответы с секретами, данными клиентов или конфиденциальным кодом через Telegram

## Связанные записи
- [[github-copilot-cli]]
- [[github-copilot-app]]
