---
title: "Rogue Agent — Stored XSS Hijacks Google Dialogflow CX Chatbots"
title_ru: "Rogue Agent — хранимый XSS перехватывает чатботы Google Dialogflow CX"
category: news
tags: [dialogflow, xss, chatbot-hijack, tenable, google, agent-security, stored-xss]
aliases: [Rogue Agent dialogflow, dialogflow cx xss, rogue agent chatbot]
confidence: high
date: 2026-07-08
updated: 2026-07-11
sources:
  - https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let-attackers.html
---

## Summary
Tenable disclosed a vulnerability in **Google Dialogflow CX** that could have let an attacker create a hidden "Rogue Agent" to hijack chatbots via a stored-XSS chain. The flaw allowed an attacker to inject malicious scripts into a chatbot's configuration, which would then execute in the context of other users' sessions — turning a customer-service bot into a credential/session theft vector.

## Key Ideas
- **Surface:** Google Dialogflow CX — enterprise conversational AI platform used to build chatbots that handle customer interactions.
- **Mechanism — stored XSS chain:** malicious script injected into the chatbot's configuration; executes in the session context of other users who interact with or administer the bot.
- **"Rogue Agent":** the injected payload effectively creates a second, hidden agent operating inside the legitimate one — hence the name.
- **Impact:** hijack of chatbot sessions — theft of credentials, session tokens, or manipulation of the bot's responses to users.
- Fixed by Google after Tenable's responsible disclosure.
- **Why it matters:** chatbots are agents with real tool/data access; a stored XSS in a chatbot platform is not just a defacement — it's a persistent agent-hijack primitive.

## Details
Rogue Agent connects two otherwise-separate threads in this wiki: the classic stored-XSS vulnerability class (decades old) and the agent-hijack threat model (new). Dialogflow CX chatbots increasingly connect to backends, databases, and APIs — so a hijacked chatbot is a pivoting point into the org's systems. The lesson: agent platforms need the same output-encoding and config-sanitization rigor as any web app, because a stored XSS in an agent config is effectively a supply-chain compromise of every conversation that agent handles.

## Related Entries
- [[writer-ai-agent-builder-tenant-token-leak]] ([Writer AI Agent Builder Token Leak](writer-ai-agent-builder-tenant-token-leak.md))
- [[bioshocking-ai-browser-credential-leak]] ([BioShocking — AI Browser Credential Leak](bioshocking-ai-browser-credential-leak.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[langgraph-rce-vulnerability]] ([LangGraph RCE Vulnerability](langgraph-rce-vulnerability.md))

---
<!-- RU -->

## Краткое описание
Tenable раскрыла уязвимость в **Google Dialogflow CX**, позволявшую атакующему создать скрытого «Rogue Agent» для перехвата чатботов через цепочку хранимого XSS. Скрипт, внедрённый в конфигурацию чатбота, выполнялся в контексте сессий других пользователей — превращая бота поддержки в вектор кражи учётных данных.

## Ключевые идеи
- **Поверхность:** Google Dialogflow CX — enterprise-платформа разговорного ИИ для чатботов.
- **Механизм — цепочка хранимого XSS:** вредоносный скрипт в конфиге бота; выполняется в контексте сессий других пользователей/админов.
- **«Rogue Agent»:** payload создаёт второго, скрытого агента внутри легитимного.
- **Влияние:** перехват сессий чатбота — кража учётных данных, токенов, манипуляция ответами.
- Исправлено Google после responsible disclosure Tenable.
- **Почему важно:** чатботы — агенты с доступом к данным/инструментам; хранимый XSS в платформе чатботов — примитив персистентного agent-hijack.

## Подробнее
Rogue Agent связывает две нити: классическую уязвимость хранимого XSS (десятилетия) и новую модель угроз agent-hijack. Чатботы Dialogflow CX подключены к бэкендам, БД, API — перехваченный бот — точка пивота в системы организации. Урок: агентские платформы нуждаются в том же output-encoding и sanitize конфигов, что и веб-приложения, потому что хранимый XSS в конфиге агента — это компрометация цепочки поставок каждого разговора.

## Связанные записи
- [[writer-ai-agent-builder-tenant-token-leak]] ([Writer AI Agent Builder Token Leak](writer-ai-agent-builder-tenant-token-leak.md))
- [[bioshocking-ai-browser-credential-leak]] ([BioShocking — AI Browser Credential Leak](bioshocking-ai-browser-credential-leak.md))
- [[agentjacking-attack]] ([Agentjacking Attack](agentjacking-attack.md))
- [[langgraph-rce-vulnerability]] ([LangGraph RCE Vulnerability](langgraph-rce-vulnerability.md))
