---
title: "Smart TVs as AI Scraping Proxies: Bright Data SDK Turns Devices Into Exit Nodes"
title_ru: "Умные телевизоры как прокси для AI-скрейпинга: SDK Bright Data превращает устройства в узлы выхода"
category: news
tags: [ai-industry, web-scraping, privacy, bright-data, residential-proxies, smart-tv]
date: 2026-06-06
updated: 2026-06-06
sources:
  - https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html
---

## Summary
A researcher reverse-engineered Bright Data's iOS SDK, documenting how free apps embed it to turn smart TVs and phones into residential proxy exit nodes for AI-focused web scraping. Bright Data (formerly Luminati) operates the world's largest residential proxy network (400M+ IPs), heavily marketed to the AI industry for bypassing anti-bot defenses.

## Key Ideas
- The SDK's peer channel that carries scraping jobs has no real authentication. On iOS, its traffic bypasses configured VPNs and evades standard security monitoring tools.
- A connected TV is close to ideal for proxy use: always plugged in, fast connection, effectively unmetered, and unattended. The SDK allows up to 200 GB of traffic per month.
- The consent gap: one Roku app (Petflix) said it would use the device "occasionally," but SDK settings allow 200 GB/month and near-continuous background operation.
- Bright Data's partner list includes smart-TV app makers PlayWorks Digital, CloudTV, and Longvision. Google, Amazon, and Roku have since restricted background proxy SDKs; Bright Data still lists Samsung Tizen and LG webOS.
- Blockable at router level: block proxyjs.brdtnet.com, proxyjs.luminatinet.com, proxyjs.bright-sdk.com, clientsdk.bright-sdk.com, clientsdk.brdtnet.com.

## Details
The model is not new — it traces back to Hola VPN selling users' bandwidth via Luminati in 2015 at $20/GB. What changed is the buyer: anti-bot defenses from Cloudflare and DataDome block datacenter IPs, so AI scrapers route through residential connections. Krebs reported in October 2025 that botnet proxies like Aisuru fuel large-scale AI data harvesting. Bright Data says its exit nodes opt in through consent screens; whether that consent is meaningful is the open question.

## Related Entries
- [[ai-agent-ffmpeg-zero-days]] ([AI Agent Uncovers 21 Zero-Days in FFmpeg](../news/ai-agent-ffmpeg-zero-days.md))
- [[chatgpt-lockdown-mode]] ([ChatGPT Lockdown Mode](../news/chatgpt-lockdown-mode.md))

---
<!-- RU -->

## Краткое описание
Исследователь реконструировал iOS SDK компании Bright Data, задокументировав, как бесплатные приложения встраивают его и превращают умные телевизоры и телефоны в резидентные прокси-узлы для AI-скрейпинга. Bright Data (ранее Luminati) управляет крупнейшей в мире сетью резидентных прокси (400M+ IP), активно продвигаемой AI-индустрии для обхода антибот-защиты.

## Ключевые идеи
- Одноранговый канал SDK, передающий задания скрейпинга, не имеет реальной аутентификации. На iOS трафик обходит настроенный VPN и уклоняется от стандартных инструментов мониторинга.
- Подключённый телевизор идеален для прокси: всегда включён, быстрое соединение, безлимитный трафик, без присмотра. SDK допускает до 200 ГБ трафика в месяц.
- Разрыв в согласии: приложение Petflix на Roku заявляло «нерегулярное» использование, но настройки SDK позволяют 200 ГБ/мес и почти непрерывную фоновую работу.
- Список партнёров Bright Data включает разработчиков Smart TV-приложений PlayWorks Digital, CloudTV и Longvision. Google, Amazon и Roku ограничили фоновые прокси-SDK; Bright Data всё ещё работает на Samsung Tizen и LG webOS.
- Блокируется на уровне роутера: proxyjs.brdtnet.com, proxyjs.luminatinet.com, proxyjs.bright-sdk.com и др.

## Подробнее
Модель не нова — она восходит к Hola VPN, продававшей пропускную способность пользователей через Luminati в 2015 году по $20/ГБ. Изменился покупатель: антибот-защита Cloudflare и DataDome блокирует IP дата-центров, поэтому AI-скрейперы маршрутизируют трафик через резидентные соединения. Bright Data утверждает, что узлы подключения основаны на согласии; насколько это согласие осмысленно — открытый вопрос.

## Связанные записи
- [[ai-agent-ffmpeg-zero-days]] ([AI Agent Uncovers 21 Zero-Days in FFmpeg](../news/ai-agent-ffmpeg-zero-days.md))
- [[chatgpt-lockdown-mode]] ([ChatGPT Lockdown Mode](../news/chatgpt-lockdown-mode.md))
