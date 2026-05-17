---
title: "UI-TARS Desktop & Agent TARS: ByteDance Multimodal AI Agent Stack"
title_ru: "UI-TARS Desktop и Agent TARS: мультимодальный AI-агент стек от ByteDance"
category: agents
tags: [ui-tars, bytedance, gui-agent, multimodal, computer-use, browser-automation, mcp, vision-language-model, agent-stack]
aliases: [UI-TARS, Agent TARS, UI-TARS-desktop, ByteDance agent]
confidence: high
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://github.com/bytedance/UI-TARS-desktop
  - https://arxiv.org/abs/2501.12326
---

## Summary
UI-TARS Desktop and Agent TARS are two open-source multimodal AI agent projects from ByteDance that use visual language models to control computers and browsers through natural language — capable of booking hotels and flights autonomously, controlling any desktop app via screenshots, and integrating with MCP tools for real-world task automation.

## Key Ideas
- **Computer use via vision**: the UI-TARS model understands screenshots and generates precise mouse/keyboard actions — not DOM-scraping or accessibility APIs, but actual visual understanding like a human would use a computer.
- **Two products in one repo**: Agent TARS (CLI + web UI, general purpose, MCP-integrated) and UI-TARS Desktop (native desktop app for local computer control). They share the underlying model but have different interfaces.
- **Real task automation confirmed**: documented demonstrations include booking the earliest flight from San Jose to New York on Priceline, booking a Ritz-Carlton hotel on Booking.com within a $5,000 budget, and generating charts via MCP-connected tools — all from natural language instructions.
- **Remote operator mode**: UI-TARS Desktop v0.2.0+ supports Remote Computer Operator and Remote Browser Operator — control any computer or browser over the network, not just the local machine.
- **MCP-native architecture**: Agent TARS's kernel is built on MCP and supports mounting arbitrary MCP servers, making it composable with the broader tool ecosystem.

## Details

### Agent TARS vs. UI-TARS Desktop

**Agent TARS** is the general-purpose multimodal agent stack:
- CLI (`npx @agent-tars/cli@latest`) and Web UI
- Hybrid browser control: GUI Agent mode, DOM mode, or hybrid strategy
- MCP kernel: mount any external MCP server for real-world integrations
- Event Stream architecture: protocol-driven streaming drives Context Engineering and the agent UI
- Best for: research, automation pipelines, API-first workflows

**UI-TARS Desktop** is the native GUI agent application:
- Driven by UI-TARS and Seed-1.5-VL/1.6 series vision-language models
- Local computer operator: control any app on your local machine via screenshots
- Remote computer and remote browser operators (v0.2.0+)
- Cross-platform: Windows, macOS, Browser
- Best for: desktop task automation, replacing manual repetitive computer work

### Quick Start (Agent TARS)

```bash
npx @agent-tars/cli@latest
# or
npm install @agent-tars/cli@latest -g
agent-tars --provider anthropic --model claude-3-7-sonnet-latest --apiKey YOUR_KEY
```

### Documented Real-World Demonstrations

1. **Flight booking**: "Book the earliest flight from San Jose to New York on September 1st and the last return flight on September 6th on Priceline" — autonomous browsing, form filling, booking completion.

2. **Hotel booking**: "I am in Los Angeles September 1–6, budget $5,000. Book the Ritz-Carlton closest to the airport on Booking.com and compile a transportation guide." — multi-step task, multi-site research.

3. **Tool-augmented chart generation**: "Draw a chart of Hangzhou's weather for one month" — via MCP-connected charting tools.

### Vision-Language Model Foundation

UI-TARS Desktop is powered by the **UI-TARS model** (arXiv:2501.12326) — a native GUI agent model pre-trained to understand desktop UI elements, icons, and spatial relationships in screenshots. The Seed-1.5-VL/1.6 series is its updated successor. These are not general-purpose LLMs with screenshots bolted on — they are specialized for GUI interaction with training data focused on computer control tasks.

### Comparison to Other Computer-Use Agents

| | UI-TARS | OpenClaw (browser) | Hermes Agent (browser) |
|---|---|---|---|
| Interface | Screenshots (vision) | DOM + CDP | DOM + Browserbase |
| Local app control | ✅ Full desktop | ❌ Browser only | ❌ Browser only |
| Remote control | ✅ v0.2.0+ | ❌ | ❌ |
| Model required | Specialized VLM | Any LLM | Any LLM |
| CAPTCHA solving | Not mentioned | Via Browserbase | Via Browserbase |

## Related Entries
- [[autonomous-personal-agents-openclaw-hermes-zeroclaw]] ([Autonomous Personal AI Agents: OpenClaw, Hermes, ZeroClaw, NemoClaw, Zo](../agents/autonomous-personal-agents-openclaw-hermes-zeroclaw.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[acdc-agent-centric-development-cycle]] ([AC/DC — Agent-Centric Development Cycle](../agents/acdc-agent-centric-development-cycle.md))

---
<!-- RU -->

## Краткое описание
UI-TARS Desktop и Agent TARS — два open-source мультимодальных AI-агентных проекта от ByteDance, которые используют визуально-языковые модели для управления компьютерами и браузерами через естественный язык: способны автономно бронировать отели и авиабилеты, управлять любым десктопным приложением через скриншоты и интегрироваться с MCP-инструментами для автоматизации реальных задач.

## Ключевые идеи
- **Управление компьютером через зрение**: модель UI-TARS понимает скриншоты и генерирует точные действия мышью/клавиатурой — не скрапинг DOM, а настоящее визуальное понимание.
- **Два продукта в одном репозитории**: Agent TARS (CLI + веб-UI, общего назначения, MCP-интегрированный) и UI-TARS Desktop (нативное приложение для локального управления компьютером).
- **Реальная автоматизация задач подтверждена**: бронирование ранних рейсов на Priceline, бронирование Ritz-Carlton на Booking.com в рамках бюджета $5,000, генерация графиков через MCP-инструменты.
- **Режим удалённого оператора**: UI-TARS Desktop v0.2.0+ поддерживает Remote Computer Operator и Remote Browser Operator.
- **MCP-нативная архитектура**: ядро Agent TARS построено на MCP и поддерживает подключение произвольных MCP-серверов.

## Подробнее

**Agent TARS** — агентный стек общего назначения: CLI (`npx @agent-tars/cli@latest`), гибридное управление браузером (GUI-агент, DOM или гибрид), MCP-ядро для подключения внешних инструментов, архитектура Event Stream для Context Engineering.

**UI-TARS Desktop** — нативное GUI-агентное приложение: управляется моделями UI-TARS и Seed-1.5-VL/1.6, локальный и удалённый операторы компьютера/браузера (v0.2.0+), кросс-платформенный (Windows, macOS, Browser).

**Основа**: модель UI-TARS (arXiv:2501.12326) — специализированная VLM для взаимодействия с GUI, обученная на данных об управлении компьютером, а не общий LLM со скриншотами.

## Связанные записи
- [[autonomous-personal-agents-openclaw-hermes-zeroclaw]] ([Autonomous Personal AI Agents: OpenClaw, Hermes, ZeroClaw, NemoClaw, Zo](../agents/autonomous-personal-agents-openclaw-hermes-zeroclaw.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[acdc-agent-centric-development-cycle]] ([AC/DC — Agent-Centric Development Cycle](../agents/acdc-agent-centric-development-cycle.md))
