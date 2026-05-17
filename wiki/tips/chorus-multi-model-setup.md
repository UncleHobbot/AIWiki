---
title: "CHORUS: Multi-Model Coding Setup"
title_ru: "CHORUS: Мультимодельная настройка для кодинга"
category: tips
tags: [chorus, multi-model, kimi, claude, codex, gemini, opencode, workflow]
date: 2026-05-15
updated: 2026-05-15
sources:
  - https://www.reddit.com/r/kimi/comments/1t6xog7/kimi_claude_codex_gemini_opencode_chorus/
  - https://github.com/chorus-codes/chorus
---

## Summary

CHORUS is an open-source tool that orchestrates 2–4 different AI coding assistants (Claude Code, Codex, Gemini CLI, Kimi, OpenCode) to review the same code in parallel, catching bugs that any single model would miss — at zero extra cost by piggybacking on CLI subscriptions you already pay for.

## Key Ideas

- Different vendors have different blind spots — mixing Claude, GPT, Gemini, and Kimi in a review catches bugs no single model sees
- Uses your existing AI subscriptions (Claude Pro, ChatGPT Plus, Gemini Advanced) with zero additional API bills; reviews cost $0 out of pocket
- Supports unanimous or majority consensus quorum rules, plus assignable reviewer personas (security, performance, architecture)
- Runs entirely locally — your code never goes to a new vendor, only to the AI tools you already trust
- Integrates via MCP server so you can trigger reviews from inside any CLI or IDE

## Details

The core insight behind CHORUS is that a model reviewing its own output is theatre — same training data, same biases. When you have Claude write code and then GPT and Gemini review it independently, each catches different classes of bugs. In a real example from the author: Opus approved a PR clean, Kimi flagged a missing tenant check on a service-role query, and Gemini caught a race condition in a retry loop — three reviewers, three different bugs, one PR.

CHORUS works as a local daemon (port 7707) that spawns your installed AI CLI tools as subprocesses, feeds them the diff or task, parses their structured output, and applies a quorum rule (unanimous or majority) to produce a verdict. A web-based cockpit UI (port 5050) lets you visualize reviews in real time. It also registers as an MCP server, so you can kick off reviews from inside Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Kimi, or OpenCode using plain English.

Pre-built templates cover common workflows: `code-review` (1 writer + 2 reviewers, both must agree), `bug-diagnose` (one hypothesizes, one challenges), `architect-review` (3 vendors critique a plan), and `red-green` (TDD where one AI writes tests blind to the other's code). Reviewer personas like Sentinel (security), Cartographer (cross-platform), Accountant (cost regressions), and Profiler (performance) let you assign focus areas to each reviewer, widening the net further.

The project is Apache-2.0 licensed, installable via `npm i -g chorus-codes`, and requires Node 20+ plus at least one supported AI CLI. It was created by the 99xAgency community and went viral on r/kimi (235 upvotes, 61 comments) as a practical answer to the growing problem of over-reliance on a single AI coding assistant.

## Notable Quotes

> "Three reviewers, three different bugs, one PR." — 99xAgency, r/kimi

> "One AI writes. Three review. You ship only when they agree — using AI subscriptions you already pay for." — Chorus README

## Related Entries

- [[github-copilot-pricing-exodus]] ([GitHub Copilot Usage-Based Pricing Triggers User Exodus](../news/github-copilot-pricing-exodus.md))
- [[cline-roo-alternatives]] ([Alternatives to Cline and Roo Code in 2026](../tips/cline-roo-alternatives.md))

---
<!-- RU -->

## Краткое описание

CHORUS — это open-source инструмент, который координирует 2–4 различных AI-ассистента для кодинга (Claude Code, Codex, Gemini CLI, Kimi, OpenCode) для параллельного ревью одного и того же кода, выявляя баги, которые ни одна модель не нашла бы по отдельности — без дополнительных расходов, за счёт использования уже оплаченных CLI-подписок.

## Ключевые идеи

- Разные вендоры имеют разные слепые зоны — комбинация Claude, GPT, Gemini и Kimi в ревью ловит баги, которые не видит ни одна модель по отдельности
- Использует ваши текущие AI-подписки (Claude Pro, ChatGPT Plus, Gemini Advanced) без дополнительных API-расходов; ревью стоят $0 из кармана
- Поддерживает правила консенсуса — единогласное или большинство, а также назначаемые персоны для ревьюеров (security, performance, архитектура)
- Работает полностью локально — ваш код не передаётся новому вендору, только тем AI-инструментам, которым вы уже доверяете
- Интегрируется через MCP-сервер, позволяя запускать ревью из любого CLI или IDE

## Подробнее

Главная идея CHORUS в том, что модель, проверяющая собственный вывод — это фарс: те же обучающие данные, те же смещения. Когда Claude пишет код, а GPT и Gemini проверяют его независимо, каждый находит разные классы ошибок. В реальном примере автора: Opus одобрил PR без замечаний, Kimi обнаружил отсутствующую проверку tenant в service-role запросе, а Gemini поймал race condition в retry loop — три ревьюера, три разных бага, один PR.

CHORUS работает как локальный демон (порт 7707), который запускает установленные AI CLI-инструменты как подпроцессы, передаёт им diff или задачу, парсит структурированный вывод и применяет правило кворума (единогласие или большинство) для вынесения вердикта. Web-интерфейс cockpit (порт 5050) позволяет визуализировать ревью в реальном времени. Инструмент также регистрируется как MCP-сервер, поэтому запускать ревью можно изнутри Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Kimi или OpenCode обычным английским языком.

Встроенные шаблоны покрывают типичные сценарии: `code-review` (1 автор + 2 ревьюера, оба должны согласиться), `bug-diagnose` (один выдвигает гипотезу, другой оспаривает), `architect-review` (3 вендора критикуют план) и `red-green` (TDD, где один AI пишет тесты вслепую от кода другого). Персоны ревьюеров — Sentinel (безопасность), Cartographer (кроссплатформенность), Accountant (регрессия стоимости), Profiler (производительность) — позволяют задать каждому ревьюеру фокус, расширяя охват проверок.

Проект распространяется под лицензией Apache-2.0, устанавливается через `npm i -g chorus-codes` и требует Node 20+ и хотя бы один поддерживаемый AI CLI. Создан сообществом 99xAgency и стал вирусным на r/kimi (235 upvotes, 61 комментарий) как практический ответ на проблему чрезмерной зависимости от одного AI-ассистента.

## Примечательные цитаты

> "Три ревьюера, три разных бага, один PR." — 99xAgency, r/kimi

> "Один AI пишет. Три проверяют. Вы отправляете код только когда они согласны — используя AI-подписки, за которые вы уже платите." — Chorus README

## Связанные записи

- [[github-copilot-pricing-exodus]] ([GitHub Copilot Usage-Based Pricing Triggers User Exodus](../news/github-copilot-pricing-exodus.md))
- [[cline-roo-alternatives]] ([Alternatives to Cline and Roo Code in 2026](../tips/cline-roo-alternatives.md))
