---
title: "Self-Replicating AI Worm on Local Open-Weight Models"
title_ru: "Самореплицирующийся AI-червь на локальных открытых моделях"
category: news
tags: [ai-security, self-replicating, worm, local-models, open-weight, university-of-toronto, arxiv]
date: 2026-06-11
updated: 2026-06-11
sources:
  - https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html
---

## Summary

University of Toronto researchers built a proof-of-concept AI-driven computer worm that uses a locally hosted open-weight LLM to reason through a network, generate tailored attack strategies per target, and self-replicate — all without human intervention or commercial AI services.

## Key Ideas

- Uses open-weight LLMs running locally — no cloud API means no monitoring or detection via API logs
- The worm reasons about each target environment and generates custom attack strategies
- Self-replicates autonomously without human intervention
- Proof-of-concept only, but demonstrates a realistic risk of open-weight model misuse
- Raises policy questions about whether open-weight model security research should be restricted

## Details

The research team demonstrated that an AI worm operating entirely on local open-weight models can autonomously navigate a network, analyze each target, craft individualized exploits, and spread to new hosts. Because all inference happens locally, there is no API call trail for security teams or providers to monitor — a fundamental shift from prior AI-assisted attack research that relied on commercial APIs.

The worm's reasoning engine analyzes the target environment, selects appropriate attack vectors, and generates tailored payloads. Each new infection carries its own copy of the local model, enabling fully autonomous propagation. The researchers published their findings as a preprint on arXiv.

The work reopens the debate about open-weight model risks: the same accessibility that enables beneficial research also enables misuse at scale, with no practical way to monitor or throttle malicious use of locally hosted models.

## Notable Quotes

> The absence of any API footprint makes this class of threat fundamentally different from AI-assisted attacks that route through commercial services.

## Related Entries

- AI security threats ([AI Security Threats](../concepts/ai-security-threats.md))
- open-weight models ([Open-Weight Models](../concepts/open-weight-models.md))
- [[smart-tv-ai-scraping-proxies]] ([Smart TVs as AI Scraping Proxies: Bright Data SDK Turns Devices Into Exit Nodes](../news/smart-tv-ai-scraping-proxies.md))

---
<!-- RU -->

## Краткое описание

Исследователи из Университета Торонто создали демонстрационный AI-червь, использующий локально размещённую открытую LLM для анализа сети, генерации индивидуальных стратегий атаки и саморепликации — всё без участия человека или коммерческих AI-сервисов.

## Ключевые идеи

- Использует открытые модели локально — нет облачного API, а значит нет мониторинга или обнаружения через логи API
- Червь анализирует каждую целевую среду и генерирует индивидуальные стратегии атаки
- Самореплицируется автономно без участия человека
- Демонстрационный концепт, но показывает реальный риск злоупотребления открытыми моделями
- Поднимает вопросы политики: следует ли ограничивать исследования безопасности открытых моделей

## Подробнее

Команда исследователей продемонстрировала, что AI-червь, работающий полностью на локальных открытых моделях, способен автономно перемещаться по сети, анализировать каждую цель, создавать индивидуальные эксплойты и распространяться на новые хосты. Поскольку весь вывод происходит локально, нет следа API-вызовов, который могли бы отслеживать команды безопасности или провайдеры — фундаментальное отличие от предыдущих исследований AI-ассистированных атак, полагавшихся на коммерческие API.

Механизм рассуждений червя анализирует целевую среду, выбирает подходящие векторы атаки и генерирует адаптированные полезные нагрузки. Каждая новая инфекция несёт собственную копию локальной модели, обеспечивая полностью автономное распространение. Результаты опубликованы в виде препринта на arXiv.

Исследование вновь открывает дискуссию о рисках открытых моделей: та же доступность, которая обеспечивает полезные исследования, также позволяет злоупотребления в масштабе, без практической возможности мониторинга или ограничения вредоносного использования локальных моделей.

## Примечательные цитаты

> Отсутствие какого-либо следа API делает этот класс угроз фундаментально отличным от AI-ассистированных атак, маршрутизируемых через коммерческие сервисы.

## Связанные записи

- AI security threats ([AI Security Threats](../concepts/ai-security-threats.md))
- open-weight models ([Open-Weight Models](../concepts/open-weight-models.md))
- [[smart-tv-ai-scraping-proxies]] ([Умные телевизоры как прокси для AI-скрейпинга: SDK Bright Data превращает устройства в узлы выхода](../news/smart-tv-ai-scraping-proxies.md))
