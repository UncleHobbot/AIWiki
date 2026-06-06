---
title: "ChatGPT Lockdown Mode: OpenAI's Defense Against Prompt Injection Exfiltration"
title_ru: "Режим блокировки ChatGPT: защита OpenAI от эксфильтрации через prompt-инъекцию"
category: news
tags: [chatgpt, openai, security, prompt-injection, data-protection]
date: 2026-06-06
updated: 2026-06-06
sources:
  - https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html
---

## Summary
OpenAI is rolling out Lockdown Mode to ChatGPT — an optional security setting that limits tools and capabilities connecting to the web or external services, designed to reduce the risk of data exfiltration from prompt injection attacks. Available across Free, Go, Plus, Pro, and self-serve Business plans.

## Key Ideas
- Lockdown Mode disables live web browsing (limited to cached content only), image support, deep research, agent mode, Canvas networking, and file downloads for data analysis.
- The feature does not stop prompt injections from occurring. Instead, it eliminates potential pathways through which stolen data could be exfiltrated to attacker-controlled infrastructure.
- Lockdown Mode and Developer Mode cannot be used simultaneously; enabling one disables the other.
- OpenAI acknowledges residual risk: malicious instructions in uploaded files can still affect ChatGPT's behavior and cause incorrect answers, even in Lockdown Mode.
- Launched alongside a new active session management feature letting users review and log out of individual or all ChatGPT sessions.

## Details
Prompt injection remains a "frontier" unsolved problem across all LLMs. Lockdown Mode builds upon existing sandboxing and URL-based data exfiltration controls to limit outbound network requests. It is primarily designed for users and organizations handling sensitive data who require stricter protection guarantees. OpenAI explicitly states the feature is "not intended for everyone" and does not guarantee complete elimination of exfiltration risk.

## Related Entries
- [[gemini-android-notification-hijack]] ([Gemini Android Notification Hijack](../news/gemini-android-notification-hijack.md))
- [[claude-code-github-action-flaw]] ([Claude Code GitHub Action Flaw](../news/claude-code-github-action-flaw.md))

---
<!-- RU -->

## Краткое описание
OpenAI развёртывает режим блокировки (Lockdown Mode) для ChatGPT — опциональную настройку безопасности, ограничивающую инструменты и возможности, подключающиеся к вебу или внешним сервисам. Цель — снизить риск эксфильтрации данных через атаки prompt-инъекцией.

## Ключевые идеи
- Lockdown Mode отключает живой веб-браузинг (только кешированный контент), поддержку изображений, глубокое исследование, режим агента, сетевые функции Canvas и загрузку файлов для анализа данных.
- Функция не предотвращает prompt-инъекции. Вместо этого она устраняет потенциальные каналы, через которые украденные данные могут быть переданы на инфраструктуру злоумышленника.
- Lockdown Mode и Developer Mode нельзя использовать одновременно.
- OpenAI признаёт остаточный риск: вредоносные инструкции в загруженных файлах могут влиять на поведение ChatGPT даже в режиме блокировки.
- Запущено вместе с новой функцией управления активными сессиями для просмотра и выхода из отдельных или всех сессий ChatGPT.

## Подробнее
Prompt-инъекция остаётся нерешённой «фронтальной» проблемой для всех LLM. Lockdown Mode строится поверх существующих механизмов песочницы и элементов управления эксфильтрацией через URL, ограничивая исходящие сетевые запросы. Функция предназначена в первую очередь для пользователей и организаций, работающих с конфиденциальными данными.

## Связанные записи
- [[gemini-android-notification-hijack]] ([Gemini Android Notification Hijack](../news/gemini-android-notification-hijack.md))
- [[claude-code-github-action-flaw]] ([Claude Code GitHub Action Flaw](../news/claude-code-github-action-flaw.md))
