---
title: "CloakBrowser: Stealth Chromium for Bot Detection Bypass"
title_ru: "CloakBrowser: скрытый Chromium для обхода детекции ботов"
category: tools
tags: [cloakbrowser, stealth-browser, chromium, playwright, puppeteer, bot-detection, fingerprinting, scraping]
aliases: [CloakBrowser, CloakHQ, stealth browser, stealth Chromium]
confidence: high
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://github.com/CloakHQ/CloakBrowser
  - https://x.com/sharbel/status/2055680438417412359
---

## Summary

CloakBrowser is a stealth Chromium browser that passes every bot detection test by modifying fingerprints at the C++ source level (49 patches). Drop-in Playwright/Puppeteer replacement with the same API — just swap the import. 30/30 detection tests passed, 0.9 reCAPTCHA v3 score, +9.1K GitHub stars in one week.

## Key Ideas
- **49 source-level C++ patches:** Not JS injection or config tweaks — actual Chromium source modifications for canvas, WebGL, audio, fonts, GPU, screen, WebRTC, network timing, automation signals, and CDP input behavior
- **Drop-in Playwright/Puppeteer replacement:** Same API, one-line import swap. `pip install cloakbrowser` or `npm install cloakbrowser`
- **30/30 detection tests passed:** Cloudflare Turnstile (3 live tests), FingerprintJS, BrowserScan, and 30+ other detection sites
- **0.9 reCAPTCHA v3 score:** Human-level, server-verified
- **humanize=True:** Human-like mouse curves, keyboard timing, and scroll patterns via single flag
- **Auto-updating binary:** Background update checks, always on the latest stealth build. ~200MB auto-downloads on first run
- **CloakBrowser Manager:** Free open-source self-hosted alternative to Multilogin/GoLogin/AdsPower. Docker-based profile management with noVNC
- **MIT licensed:** Free, no subscriptions, no usage limits
- **Fastest growing repo:** +9.1K stars in one week (per @sharbel weekly roundup)

## Details

CloakBrowser solves the fundamental problem with browser automation: antibot systems detect automation through fingerprints at the browser engine level. Traditional stealth plugins (like puppeteer-extra-plugin-stealth) try to patch these at the JavaScript level, which can be detected. CloakBrowser modifies the Chromium C++ source directly — 49 patches covering canvas, WebGL, audio context, font enumeration, GPU info, screen properties, WebRTC, network timing, and Chrome DevTools Protocol signals.

The result is a real Chromium binary that antibot systems score as a normal browser. The migration path from Playwright is a single import line change. Current version: v0.3.28 (Chromium 146.0.7680.177.4).

## Related Entries
- [[react-doctor]] ([React Doctor: AI-Generated React Code Linter](../tools/react-doctor.md))
- [[package-hallucination-mcp]] ([Package Hallucination Catcher: MCP Server for LLM Package Recommendations](../tools/package-hallucination-mcp.md))
- [[ui-tars-desktop-multimodal-agent]] ([UI-TARS Desktop & Agent TARS: ByteDance Multimodal AI Agent Stack](../agents/ui-tars-desktop-multimodal-agent.md))

---
<!-- RU -->

## Краткое описание

CloakBrowser — скрытый браузер на базе Chromium, проходящий все тесты детекции ботов благодаря модификации отпечатков на уровне исходного кода C++ (49 патчей). Замена Playwright/Puppeteer с тем же API — достаточно заменить импорт. 30/30 тестов пройдено, оценка reCAPTCHA v3 — 0.9, +9.1K звёзд на GitHub за неделю.

## Ключевые идеи
- **49 патчей на уровне исходного кода C++:** Не JS-инъекция — реальные модификации исходного кода Chromium для canvas, WebGL, аудио, шрифтов, GPU, WebRTC, сетевых таймингов и сигналов автоматизации
- **Замена Playwright/Puppeteer:** Тот же API, замена одной строки импорта. `pip install cloakbrowser` или `npm install cloakbrowser`
- **30/30 тестов детекции пройдено:** Cloudflare Turnstile, FingerprintJS, BrowserScan и 30+ других
- **Оценка reCAPTCHA v3: 0.9** — на уровне человека, верифицировано сервером
- **humanize=True:** Человекоподобные кривые мыши, тайминг клавиатуры и паттерны прокрутки
- **Автообновление бинарника:** Фоновые проверки обновлений, ~200 МБ автоматически загружается при первом запуске
- **MIT лицензия:** Бесплатно, без подписок, без ограничений использования

## Связанные записи
- [[react-doctor]] ([React Doctor: AI-Generated React Code Linter](../tools/react-doctor.md))
- [[package-hallucination-mcp]] ([Package Hallucination Catcher: MCP Server for LLM Package Recommendations](../tools/package-hallucination-mcp.md))
- [[ui-tars-desktop-multimodal-agent]] ([UI-TARS Desktop & Agent TARS: ByteDance Multimodal AI Agent Stack](../agents/ui-tars-desktop-multimodal-agent.md))
