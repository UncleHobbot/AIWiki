---
title: "Gemini Android Voice Assistant Hijack via Poisoned Notifications"
title_ru: "Перехват голосового ассистента Gemini на Android через отравленные уведомления"
category: news
tags: [gemini, google, security, android, prompt-injection, voice-assistant]
date: 2026-06-06
updated: 2026-06-06
sources:
  - https://thehackernews.com/2026/06/whatsapp-slack-notifications-could.html
---

## Summary
SafeBreach researcher Or Yair found that a single poisoned notification from WhatsApp, Slack, SMS, Signal, Instagram, or Messenger could hijack Google Gemini's voice assistant on Android — opening URLs, faking messages from contacts, pushing into Zoom calls, or poisoning long-term memory. No malicious app needed. Google has patched server-side.

## Key Ideas
- Gemini's Utilities feature reads and acts on notification text, treating it as instructions. Anything that can push a notification can deliver a payload — an "effectively infinite" attack surface.
- The "Fake Context Alignment" bypass runs two illusions simultaneously: a legitimate-looking authorization for the security check, and a harmless exchange for the human. In the "obfuscated" variant, Gemini asks the real question in Chinese, then follows in English with something innocuous.
- In the "muted" variant, text-to-speech skips hyperlinks hidden behind clickable text, so the malicious question is invisible to the driver but present on screen for the security check.
- Beyond faking output, the attack achieved smart home control (opening windows via Google Home), cross-app navigation (forcing Zoom calls), IP geolocation, and persistent memory poisoning (stored attacker-chosen facts at the account level).
- Android-only vector. Fix is server-side; no app update needed. Mitigation: disconnect Utilities in Gemini's Connected Apps settings.

## Details
The research builds on SafeBreach's earlier "Invitation Is All You Need" work using malicious Google Calendar invites. After Google hardened Gemini against indirect prompt injection, Yair found a way around the new defenses. Reported August 2025, confirmed fixed November 2025. The most dangerous aspect for hands-free use: while driving and not looking at the screen, a fake "your manager asked you to upload docs to this Drive folder" is hard to second-guess when spoken aloud.

## Related Entries
- [[chatgpt-lockdown-mode]] ([ChatGPT Lockdown Mode](../news/chatgpt-lockdown-mode.md))
- [[claude-code-github-action-flaw]] ([Claude Code GitHub Action Flaw](../news/claude-code-github-action-flaw.md))

---
<!-- RU -->

## Краткое описание
Исследователь SafeBreach Or Yair обнаружил, что одно отравленное уведомление от WhatsApp, Slack, SMS, Signal или Instagram может перехватить голосовой ассистент Google Gemini на Android — открывать URL, подделывать сообщения от контактов, принудительно подключать к Zoom-звонкам или отравлять долговременную память. Вредоносное приложение не требуется. Google устранил уязвимость на стороне сервера.

## Ключевые идеи
- Функция Gemini Utilities читает и выполняет текст уведомлений, воспринимая его как инструкции. Любой источник уведомлений может доставить полезную нагрузку — атаковая поверхность «практически бесконечна».
- Обход «Fake Context Alignment» создаёт две иллюзии одновременно: легитимную авторизацию для проверки безопасности и безобменный диалог для человека. В варианте «obfuscated» Gemini задаёт настоящий вопрос на китайском, затем переключается на английский.
- В варианте «muted» синтез речи пропускает гиперссылки, скрытые за кликабельным текстом — вредоносный вопрос невидим для водителя, но присутствует на экране для проверки безопасности.
- Помимо подделки вывода, атака позволяла управление умным домом, межприложенческую навигацию, геолокацию по IP и стойкое отравление памяти на уровне аккаунта.
- Вектор только для Android. Исправление на стороне сервера; обновление приложения не требуется.

## Подробнее
Исследование развивает предыдущую работу SafeBreach «Invitation Is All You Need» с вредоносными приглашениями Google Calendar. После того как Google усилил защиту Gemini от косвенной prompt-инъекции, Yair нашёл способ обойти новые механизмы защиты. Наиболее опасный аспект при использовании без рук: за рулём фальшивое «ваш руководитель просит загрузить документы» сложно подвергнуть сомнению, когда это произносится вслух.

## Связанные записи
- [[chatgpt-lockdown-mode]] ([ChatGPT Lockdown Mode](../news/chatgpt-lockdown-mode.md))
- [[claude-code-github-action-flaw]] ([Claude Code GitHub Action Flaw](../news/claude-code-github-action-flaw.md))
