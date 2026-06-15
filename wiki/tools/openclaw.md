---
title: "OpenClaw"
title_ru: "OpenClaw"
category: tools
tags: [openclaw, agents, self-hosted, open-source]
aliases: [OpenClaw, OpenClaw agent platform]
confidence: medium
updated: 2026-06-14
sources:
  - https://github.com/OpenCloudBuild/OpenClaw
---

## Summary

OpenClaw is an open-source, self-hosted AI agent platform for running 24/7 background agents. Agents persist between sessions, can be invoked on a schedule or via webhooks, and connect to both closed (GPT, Claude) and open (Llama, Qwen) models through a unified interface.

## Key Ideas

- Designed for always-on background agents rather than interactive chat — agents survive restarts and run autonomously on triggers or schedules.
- Self-hostable by default, lowering the infrastructure tax; managed hosting options exist (Runware offers free hosting, pay only for inference tokens).
- Unified model interface: route between proprietary and open-weight LLMs without rewriting agent code.
- Extensible agent/tool model lets developers compose multi-step workflows.
- Security surfaced as a real concern: researchers (Imperva/Varonis) disclosed vulnerabilities in the platform, prompting hardening guidance.

## Details

OpenClaw positions itself against managed agent platforms by letting developers own their infrastructure while still getting agent-management primitives — persistence, scheduling, model routing, and tool composition. The recent move to make hosting free (via Runware) removed the fixed infrastructure cost, leaving a pure pay-as-you-go token model for experimentation.

Because the platform runs autonomous, long-lived agents with broad system access, its attack surface matters. Public disclosures of security vulnerabilities by Imperva and Varonis researchers highlighted risks around agent sandboxing and credential exposure, making isolation (e.g., sandboxed execution) and least-privilege configuration important for any production deployment.

## Notable Quotes

> "OpenClaw lets you run agents in the background 24/7 without managing servers." — Runware

## Related Entries

- [[openclaw-free-hosting]] ([OpenClaw Free Hosting](../news/openclaw-free-hosting.md))
- [[openclaw-agent-security-vulnerabilities]] ([OpenClaw Agent Security Vulnerabilities](../news/openclaw-agent-security-vulnerabilities.md))

---
<!-- RU -->

## Краткое описание

OpenClaw — open-source, self-hosted платформа AI-агентов для запуска фоновых агентов 24/7. Агенты сохраняются между сессиями, могут вызываться по расписанию или через webhooks и подключаются как к закрытым (GPT, Claude), так и к открытым (Llama, Qwen) моделям через единый интерфейс.

## Ключевые идеи

- Заточен под постоянно работающие фоновые агенты, а не интерактивный чат — агенты переживают перезапуски и работают автономно по триггерам или расписанию.
- По умолчанию self-hosted, что снижает «инфраструктурный налог»; существуют варианты управляемого хостинга (Runware предлагает бесплатный хостинг, оплата только за токены инференса).
- Единый интерфейс моделей: маршрутизация между проприетарными и открытыми LLM без переписывания кода агента.
- Расширяемая модель агент/инструмент позволяет разработчикам компоновать многошаговые workflows.
- Безопасность стала реальной проблемой: исследователи (Imperva/Varonis) раскрыли уязвимости платформы, что породило рекомендации по усилению защиты.

## Подробнее

OpenClaw позиционируется против управляемых платформ агентов, позволяя разработчикам владеть своей инфраструктурой, сохраняя при этом примитивы управления агентами — персистентность, планирование, маршрутизацию моделей и композицию инструментов. Недавний шаг по сделке хостинга бесплатным (через Runware) убрал фиксированную стоимость инфраструктуры, оставив чистую модель оплаты токенов по факту для экспериментов.

Поскольку платформа запускает автономных, долгоживущих агентов с широким системным доступом, её поверхность атаки имеет значение. Публичные раскрытия уязвимостей безопасности исследователями Imperva и Varonis подчеркнули риски, связанные с песочницей агента и раскрытием учётных данных, что делает изоляцию (например, песочницу выполнения) и конфигурацию минимальных привилегий важными для любого продакшен-развёртывания.

## Примечательные цитаты

> «OpenClaw позволяет запускать агентов в фоновом режиме 24/7 без управления серверами.» — Runware

## Связанные записи

- [[openclaw-free-hosting]] ([OpenClaw Free Hosting](../news/openclaw-free-hosting.md))
- [[openclaw-agent-security-vulnerabilities]] ([OpenClaw Agent Security Vulnerabilities](../news/openclaw-agent-security-vulnerabilities.md))
