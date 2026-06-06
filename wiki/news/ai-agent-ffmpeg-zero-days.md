---
title: "AI Agent Uncovers 21 Zero-Days in FFmpeg"
title_ru: "AI-агент обнаружил 21 zero-day в FFmpeg"
category: news
tags: [security, ai-agent, ffmpeg, vulnerability, autonomous, zero-day, chrome]
date: 2026-06-06
updated: 2026-06-06
sources:
  - https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html
---

## Summary
Security startup depthfirst used an autonomous AI agent to find 21 previously unknown zero-day vulnerabilities in FFmpeg, the ubiquitous media library. The run cost approximately $1,000. Several bugs had been latent for 15-20 years, with one stack overflow dating back to 2003.

## Key Ideas
- The autonomous agent scanned FFmpeg's ~1.5 million lines of C and produced 21 confirmed zero-days, each with a reproducible proof-of-concept input.
- Nine CVEs assigned so far (CVE-2026-39210 through CVE-2026-39218); the rest are fixed but not yet numbered.
- Most are heap or stack overflows in parsers and demuxers, spanning the TS demuxer to the VP9 decoder. One stack overflow in service-description-table code sat untouched for 23 years.
- Same week, Google shipped Chrome 149 with patches for a record 429 security bugs. The worst (CVE-2026-10881, CVSS 9.6) let a crafted page escape the ANGLE sandbox.
- Google's Big Sleep agent and Anthropic's Mythos model previously found FFmpeg bugs too. Another autonomous tool found an authenticated RCE in Redis present since version 7.2.0.

## Details
The findings demonstrate that AI vulnerability discovery has become cheap and scalable. The bottleneck has shifted from finding bugs to triaging reports, shipping fixes, and getting them installed — work that still falls to volunteers and a thin layer of human triagers. FFmpeg is widely bundled in media pipelines, Python wheels, container images, and appliances, so embedded copies need patching too, not just system packages. For Chrome, update to 149.0.7827.53/54 or confirm auto-update has run.

## Related Entries
- [[claude-code-github-action-flaw]] ([Claude Code GitHub Action Flaw](../news/claude-code-github-action-flaw.md))
- [[http2-bomb-openai-codex-discovery]] ([HTTP/2 Bomb Discovered by OpenAI Codex](../news/http2-bomb-openai-codex-discovery.md))
- [[project-glasswing-anthropic-vulnerability-discovery]] ([Project Glasswing: Mythos AI Finds 10,000 Vulnerabilities](../news/project-glasswing-anthropic-vulnerability-discovery.md))

---
<!-- RU -->

## Краткое описание
Стартап depthfirst использовал автономный AI-агент для обнаружения 21 ранее неизвестной zero-day уязвимости в FFmpeg — повсеместно используемой медиабиблиотеке. Стоимость одного прогона составила примерно $1,000. Некоторые ошибки оставались незамеченными 15–20 лет.

## Ключевые идеи
- Автономный агент просканировал ~1.5 млн строк C в FFmpeg и обнаружил 21 подтверждённый zero-day с воспроизводимыми proof-of-concept.
- Девять CVE уже назначены (CVE-2026-39210 — CVE-2026-39218); остальные исправлены, но ещё не пронумерованы.
- Большинство — переполнения кучи или стека в парсерах и демуксерах. Один stack overflow в коде service-description-table оставался незамеченным 23 года.
- В ту же неделю Google выпустил Chrome 149 с рекордными 429 исправлениями безопасности. Наихудший (CVE-2026-10881, CVSS 9.6) позволял escape из песочницы ANGLE.
- Google Big Sleep и Anthropic Mythos ранее также находили уязвимости в FFmpeg. Другой автономный инструмент обнаружил authenticated RCE в Redis, присутствующий с версии 7.2.0.

## Подробнее
Результаты показывают, что обнаружение уязвимостей с помощью AI стало дешёвым и масштабируемым. Узкое место сместилось с поиска багов на обработку отчётов, выпуск исправлений и их установку — работу, которая всё ещё выполняется волонтёрами. FFmpeg часто встраивается в медиа-конвейеры, Python-пакеты и контейнеры, поэтому встраиваемые копии также требуют обновления.

## Связанные записи
- [[claude-code-github-action-flaw]] ([Claude Code GitHub Action Flaw](../news/claude-code-github-action-flaw.md))
- [[http2-bomb-openai-codex-discovery]] ([HTTP/2 Bomb Discovered by OpenAI Codex](../news/http2-bomb-openai-codex-discovery.md))
- [[project-glasswing-anthropic-vulnerability-discovery]] ([Project Glasswing: Mythos AI Finds 10,000 Vulnerabilities](../news/project-glasswing-anthropic-vulnerability-discovery.md))
