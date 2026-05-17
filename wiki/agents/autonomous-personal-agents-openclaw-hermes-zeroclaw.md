---
title: "Autonomous Personal AI Agents: OpenClaw, Hermes, ZeroClaw, NemoClaw, Zo"
title_ru: "Автономные персональные AI-агенты: OpenClaw, Hermes, ZeroClaw, NemoClaw, Zo"
category: agents
tags: [autonomous-agent, openclaw, hermes-agent, zeroclaw, nemoclaw, zo, self-hosted, telegram, personal-assistant, synology, ollama, local-llm]
aliases: [OpenClaw, ZeroClaw, NemoClaw, Hermes Agent, Zo Computer, claw family, personal AI agent]
confidence: medium
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://github.com/openclaw/openclaw
  - https://github.com/NousResearch/hermes-agent
  - https://github.com/zeroclaw-labs/zeroclaw
  - https://github.com/NVIDIA/NemoClaw
  - https://www.zo.computer/
  - https://canitrunopenclaw.com/devices/synology-ds923-plus
  - https://ollama.com/blog/openclaw
  - https://hermes-agent.nousresearch.com/docs/
---

## Summary
Five personal autonomous AI agent platforms — OpenClaw, Hermes Agent, ZeroClaw, NemoClaw, and Zo — compared across features, local hosting on modest hardware (Synology NAS), local LLM support, and real-world personal task automation including real estate search, appointment booking, and calendar management. ZeroClaw stands out for NAS deployment (<5 MB RAM); OpenClaw has the richest feature set; Hermes Agent is the most production-stable; Zo is the easiest cloud-managed option.

## Key Ideas
- **The Claw family** is a naming convention for a class of always-on personal AI agents: OpenClaw (original, Node.js, ~250k stars), ZeroClaw (Rust rewrite, <5 MB RAM), NemoClaw (NVIDIA security wrapper on OpenClaw), PicoClaw (Go, IoT/ultra-low-power).
- **ZeroClaw is the clear choice for a Synology NAS at stock 4 GB RAM** — its Rust binary uses under 5 MB idle, while OpenClaw needs 8 GB+ for browser automation and NemoClaw requires 8 GB minimum.
- **All agents except Zo support local LLMs via Ollama** — meaning they can run entirely privately on a home server with Qwen3.6, Llama 3.3, or similar models.
- **Real personal task automation is real**: OpenClaw has documented cases of autonomous Zillow offer submission, doctor appointment booking via outbound phone calls (via Ring-a-Ding/Vapi skills), and scheduled email/calendar management.
- **Zo is the only non-self-hostable option** — a fully managed $18/month cloud service that sacrifices local control for extreme ease-of-use.

## The Claw Family

Four of the five agents share a conceptual lineage — the "claw" suffix became a community convention for always-on personal AI agents:

| Name | Language | Stars | Relation | Key Differentiator |
|---|---|---|---|---|
| [OpenClaw](https://github.com/openclaw/openclaw) | Node.js | ~250,000 | Original | Full-featured, largest community, 23+ integrations |
| [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | Rust | ~20,000 | Independent rewrite | 3.4 MB binary, <5 MB RAM, <10 ms startup |
| [NemoClaw](https://github.com/NVIDIA/NemoClaw) | Docker stack | — | Security wrapper on OpenClaw | NVIDIA OpenShell sandbox, enterprise guardrails |
| [PicoClaw](https://github.com/sipeed/picoclaw) | Go | — | Independent rewrite | IoT, $10 hardware, ESP32/Raspberry Pi |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | TypeScript/Python | ~134,000 | Unrelated (Nous Research) | Self-improving skill loop, best stability |
| [Zo](https://www.zo.computer/) | Managed cloud | — | Unrelated | $18/month cloud service, zero self-hosting |

---

## Agent Profiles

### OpenClaw
**GitHub:** [openclaw/openclaw](https://github.com/openclaw/openclaw) | **Docs:** [docs.openclaw.ai](https://docs.openclaw.ai/)

Originally "Clawdbot" (Nov 2025), renamed after trademark issue. Fastest-growing open-source project ever (~250k stars in ~60 days). Now stewards by a non-profit foundation.

**Key features:**
- 23+ messaging channel integrations (see Integrations section)
- Full browser automation: navigation, form filling, JavaScript rendering, screenshot capture
- Voice phone calls via Ring-a-Ding/Vapi/Pine Voice skills — agent calls doctor's office and books autonomously
- Cron/heartbeat scheduler for fully unattended operation
- Live Canvas with A2UI visual workspace
- Skills/plugin marketplace
- MCP server integration
- Multi-agent routing with isolated workspaces

**Requirements:** Node.js 22.16+, minimum 4 GB RAM (text-only), 8 GB for browser automation, 10 GB SSD minimum. No GPU needed for cloud LLMs.

**Local LLMs:** Ollama official support since v2.1 (March 2026). Recommended: Qwen3.6 27B, Llama 3.3, MiniMax M2.5. Requires 64k+ context window.

**Stability:** Mixed. Rapid growth outpaced engineering maturity; widespread breakage in v2026.4.26; security advisory (May 2026) found 245,000 exposed instances. v2.26+ trending toward production-grade.

---

### Hermes Agent
**GitHub:** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **Docs:** [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/docs/)

MIT license, ~134k stars. Built by Nous Research (Feb 2026). Distinguishing feature: self-improving skill loop — agent creates reusable skills from experience; a Curator subsystem grades, consolidates, and prunes skills on a 7-day cycle.

**Key features:**
- 70+ built-in tools: search, web extract, vision, image generation, TTS, shell, file, memory, git, HTTP, browser
- Browser automation: Browserbase (cloud, CAPTCHA solving), Browser Use, local CDP/Chrome, local Chromium
- Subagent delegation: spawn parallel agents for sub-tasks
- FTS5 session search + LLM summarization for cross-session memory
- User modeling (personalization over time)
- Cron scheduler in natural language
- Windows native beta (bundled Python 3.11, Node, ripgrep, ffmpeg)
- Runs on $5/month VPS (Hetzner CX22)

**Requirements:** Minimum 1 vCPU / 2 GB RAM (text-only), recommended 4–8 GB with browser. ~20 GB storage. Docker official image available. No GPU required.

**Local LLMs:** Full support — Ollama, vLLM, SGLang, llama.cpp, LM Studio, LiteLLM, any OpenAI-compatible endpoint. Also: OpenRouter (200+ models), NVIDIA NIM, GLM, Moonshot, MiniMax.

**Stability:** Most production-stable of all five. Documented at $0.24/hour VPS deployments running 8+ hours/day. Active Nous Research maintainership. No widespread breakage incidents.

---

### ZeroClaw
**GitHub:** [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | **Docs:** [docs.zeroclawlabs.ai](https://docs.zeroclawlabs.ai/en/)

Complete Rust rewrite of the Claw concept — not a fork of OpenClaw. 20k+ stars. Tagline: "Zero overhead. Zero compromise."

**Key features:**
- 3.4 MB binary (minimal kernel ~6.6 MB), <5 MB idle RAM, <10 ms startup
- Multi-channel: one agent answers across all configured channels simultaneously
- Standard Operating Procedures (SOP): event-triggered automation with MQTT, webhooks, cron, approval gates
- Hardware integration: GPIO/I2C/SPI/USB for Raspberry Pi, STM32, Arduino, ESP32
- OS-level sandboxes, command policies, workspace boundaries, cryptographic tool receipts
- Web dashboard (HTTP/WebSocket): chat, memory browsing, config management
- Zero external dependencies for memory (SQLite, Markdown, or ephemeral — no vector DB)
- 28+ built-in LLM providers; pre-built binaries for Linux, macOS, Windows, ARM, x86, RISC-V

**Requirements:** Exceptional — under 5 MB RAM at idle. Runs on $10 hardware. Pre-built binaries, no Node.js or Python required. Docker available with distroless base image.

**Local LLMs:** Ollama + any OpenAI-compatible endpoint via `--provider` flag.

**Stability:** Pre-1.0 (v0.1.6). Code quality concerns (261 `.unwrap()` calls, potential deadlocks, only 3 integration tests). 30% of roadmap milestones slipped. Community PRs not reliably addressed. Not recommended for mission-critical unattended workflows yet. Ideal for lightweight personal use where the minimal footprint is the primary requirement.

---

### NemoClaw
**GitHub:** [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | **Page:** [nvidia.com/en-us/ai/nemoclaw](https://www.nvidia.com/en-us/ai/nemoclaw/)

NVIDIA's open-source reference stack built on OpenClaw (announced March 16, 2026). Adds security and policy enforcement; does not replace OpenClaw's capabilities.

**What it adds over OpenClaw:**
- OpenShell sandbox: Landlock + seccomp + network namespaces isolation
- Model router: auto-selects model by query complexity across 14 dimensions
- Egress network policy management
- Privacy router: keeps sensitive data local, routes only permissioned requests to cloud
- State persistence and snapshot management
- Local Nemotron model support

**Requirements:** 4 vCPU / 8 GB RAM minimum (sandbox image alone is 2.4 GB compressed), 16 GB recommended, 20–40 GB storage. Linux Docker primary path; macOS Apple Silicon and WSL2 supported. NVIDIA GPU preferred but not required for core functionality (local Nemotron inference requires GPU).

**Local LLMs:** Ollama via pool-config.yaml; NVIDIA Endpoints for Nemotron.

**Stability:** Alpha — explicitly "early preview." Not production-ready. Designed for NVIDIA workstations, DGX Station, DGX Spark — not NAS devices.

---

### Zo
**Website:** [zo.computer](https://www.zo.computer/) | **Pricing:** from $18/month

Managed cloud computer-as-a-service. Not open-source; not self-hostable. Access via web, Mac/Windows app, or iOS app.

**Key features:**
- 100 GB free cloud storage per account
- Pre-built integrations: Gmail, Google Calendar, Google Drive, Dropbox, Linear, Notion
- Agent creation via natural language ("Every Monday, pull my Linear board and email me a summary")
- Bring your own API keys (OpenAI, Anthropic, Cerebras, Groq, Gemini)
- Web hosting at zo.space subdomain
- Cloud snapshots with point-in-time restoration

**Requirements:** None for the user — fully managed cloud.

**Local LLMs:** Not supported. Cloud-only service.

**Stability:** Most reliable of all five — fully managed, no infrastructure concerns. Trade-off: no self-hosting, limited messenger coverage, no local control.

---

## Personal Task Capabilities

| Task | OpenClaw | Hermes | ZeroClaw | NemoClaw | Zo |
|---|---|---|---|---|---|
| Real estate search (Zillow, etc.) | ✅ Confirmed (372 Zillow offers/day documented) | ✅ Possible (browser) | 🟡 Possible (browser) | ✅ Inherits OpenClaw | 🟡 Limited |
| Doctor appointment (web form) | ✅ Browser form-filling | 🟡 Implied | 🟡 Possible | ✅ Inherits OpenClaw | ❌ Not documented |
| Doctor appointment (phone call) | ✅ Ring-a-Ding/Vapi skills | ❌ Not documented | ❌ Not documented | ✅ Inherits OpenClaw | ❌ |
| Calendar management | ✅ Cron + integrations | ✅ Apple Calendar, Google | 🟡 Cron/SOP | ✅ | ✅ Google Calendar |
| Email management | ✅ Scheduled summarization | ✅ Gmail pipeline documented | 🟡 SOP triggers | ✅ | ✅ Gmail |
| Price monitoring / shopping | ✅ Browser | ✅ Car price monitoring documented | 🟡 Browser | ✅ | 🟡 |
| Unattended cron jobs | ✅ Fire-and-forget | ✅ Natural language scheduler | ✅ SOP/cron | ✅ | 🟡 Rules-based only |

---

## Synology NAS Hosting (DS923+, AMD Ryzen R1600, 4 GB RAM stock, no GPU)

| Agent | 4 GB stock | 8–16 GB upgraded | Notes |
|---|---|---|---|
| **ZeroClaw** | ✅ **Ideal** (<5 MB RAM) | ✅ | Best choice for NAS; text+tools only at 4 GB |
| **OpenClaw** | ⚠️ Barely (text-only, pre-built image) | ✅ (browser at 8 GB+) | Upgrade RAM first; avoid local build (2 GB RAM spike) |
| **Hermes Agent** | ⚠️ Tight (2 GB min, no browser) | ✅ | Stable on x86-64; $5/month VPS often easier |
| **NemoClaw** | ❌ (8 GB minimum) | ⚠️ (tight) | Designed for NVIDIA workstations, not NAS |
| **Zo** | N/A | N/A | Cloud service — no deployment |

**Practical recommendation for DS923+:**
- **At 4 GB (stock):** ZeroClaw only. Runs comfortably, uses trivial RAM.
- **At 8–16 GB (upgraded):** OpenClaw with pre-built GHCR image (`ghcr.io/openclaw/openclaw:latest`), full browser automation. Use Container Manager (Docker) on DSM 7.x.
- **VPS alternative:** Hermes Agent on a $5–7/month Hetzner CX22 — simpler than NAS management and gives full RAM headroom.

**Note on ARM64 Synology models** (DS124, DS223, etc.): Hermes Agent has an [open bug (#20230)](https://github.com/NousResearch/hermes-agent/issues/20230) where Python tools are missing in ARM64 containers. DS923+ uses AMD Ryzen (x86-64) so this bug does NOT apply to it.

---

## Messenger Integrations

| Platform | OpenClaw | Hermes | ZeroClaw | NemoClaw | Zo |
|---|---|---|---|---|---|
| Telegram | ✅ | ✅ | ✅ | ✅ | ✅ |
| WhatsApp | ✅ | ✅ | ✅ | ✅ | ❌ |
| Signal | ✅ | ✅ | ✅ | ✅ | ❌ |
| Discord | ✅ | ✅ | ✅ | ✅ | ❌ |
| Slack | ✅ | ✅ | ✅ | ✅ | ❌ |
| iMessage | ✅ | ❌ | ❌ | ✅ | ❌ |
| Matrix | ✅ | ✅ | ✅ | ✅ | ❌ |
| Microsoft Teams | ✅ | ✅ | ❌ | ✅ | ❌ |
| Google Chat | ✅ | ✅ | ❌ | ✅ | ❌ |
| Facebook Messenger | ❌ | ❌ | ❌ | ❌ | ❌ |
| Email (SMTP/IMAP) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Synology Chat | ✅ | ❌ | ❌ | ✅ | ❌ |
| **Total** | **23+** | **20+** | **30+** | **23+** | **4** |

**Facebook Messenger:** None of these agents has a documented Facebook Messenger integration as of May 2026. Facebook's restricted Graph API makes unofficial Messenger integrations unreliable. The closest alternative is WhatsApp Business API, which OpenClaw and Hermes support.

---

## Details

**The killer use case for OpenClaw** is phone-based appointment booking. The Ring-a-Ding, Pine Voice, ClawdTalk, and Vapi skills enable the agent to make an actual outbound phone call to a doctor's office, navigate the IVR or talk to reception, and book a time slot — all autonomously without any browser or web form. This is the only agent in this comparison where this is confirmed working.

**Real estate automation at scale** has been documented with OpenClaw: one user configured the agent to submit lowball offers on 372 Zillow listings per day — fully autonomous, browser-driven, running on cron. The same pipeline applies to property monitoring, price alert triggers, and listing comparison across sites.

**The Hermes Agent self-improvement loop** is architecturally distinctive. After each task, the agent writes a skill — a reusable procedure for that type of task. A Curator agent (added in v0.12.0) runs on a 7-day cycle, grades all skills by success rate, consolidates duplicates, and prunes underperforming ones. Over weeks of use, the agent accumulates a personal skill library tuned to your exact workflows. No other agent in this comparison has this.

**Security concerns with OpenClaw** are real. A May 2026 security advisory found approximately 245,000 publicly exposed instances via Shodan/ZoomEye through a chain vulnerability. If self-hosting OpenClaw, ensure it is not exposed to the public internet (use Tailscale, Cloudflare Tunnel, or bind to localhost only). ZeroClaw and NemoClaw have stronger security defaults by design.

**Zo is the easiest path** if you don't want to manage infrastructure and $18/month is acceptable. Its Google Calendar and Gmail integrations are polished and pre-built. The trade-off: no local models, limited messengers (no WhatsApp, Signal, Discord), and no ability to inspect or modify the runtime. It is the appropriate choice for non-technical users or as a fallback.

## Related Entries
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[tencent-db-agent-memory]] ([TencentDB Agent Memory: Local Long-Term Memory for AI Agents](../tools/tencent-db-agent-memory.md))
- [[new-organizational-models-ai-agents]] ([New Organizational Models for the Age of AI Agents](../agents/new-organizational-models-ai-agents.md))
- [[package-hallucination-mcp]] ([Package Hallucination Catcher: MCP Server for LLM Package Recommendations](../tools/package-hallucination-mcp.md))

---
<!-- RU -->

## Краткое описание
Пять платформ автономных персональных AI-агентов — OpenClaw, Hermes Agent, ZeroClaw, NemoClaw и Zo — сравниваются по функциям, развёртыванию на Synology NAS, поддержке локальных LLM и реальным сценариям использования: поиск недвижимости, запись к врачу, управление календарём и мессенджерами.

## Ключевые идеи
- **Семейство Claw** — это соглашение об именовании для класса всегда включённых персональных AI-агентов: OpenClaw (оригинал, Node.js, ~250k звёзд), ZeroClaw (переписан на Rust, <5 МБ RAM), NemoClaw (обёртка безопасности NVIDIA поверх OpenClaw), PicoClaw (Go, IoT).
- **ZeroClaw — лучший выбор для Synology NAS при 4 ГБ RAM** — двоичный файл Rust использует менее 5 МБ в режиме ожидания, тогда как OpenClaw требует 8 ГБ+ для автоматизации браузера, а NemoClaw — минимум 8 ГБ.
- **Все агенты, кроме Zo, поддерживают локальные LLM через Ollama** — они могут работать полностью приватно на домашнем сервере.
- **Реальная автоматизация личных задач подтверждена**: OpenClaw документально обеспечивает автономную подачу предложений на Zillow, запись к врачу по телефону (через навык Ring-a-Ding/Vapi) и управление электронной почтой/календарём.
- **Zo — единственный вариант без self-hosting**: полностью управляемый облачный сервис за $18/месяц.

## Семейство Claw

| Название | Язык | Звёзды | Связь | Ключевое отличие |
|---|---|---|---|---|
| [OpenClaw](https://github.com/openclaw/openclaw) | Node.js | ~250 000 | Оригинал | Полнофункциональный, 23+ интеграции |
| [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | Rust | ~20 000 | Независимая переработка | 3,4 МБ бинарник, <5 МБ RAM |
| [NemoClaw](https://github.com/NVIDIA/NemoClaw) | Docker | — | Обёртка NVIDIA на OpenClaw | Sandbox OpenShell, корпоративные политики |
| [PicoClaw](https://github.com/sipeed/picoclaw) | Go | — | Независимая переработка | IoT, оборудование за $10 |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | TS/Python | ~134 000 | Несвязанный (Nous Research) | Самосовершенствование навыков, лучшая стабильность |
| [Zo](https://www.zo.computer/) | Облако | — | Несвязанный | $18/месяц, без self-hosting |

## Профили агентов

### OpenClaw
**GitHub:** [openclaw/openclaw](https://github.com/openclaw/openclaw) | **Документация:** [docs.openclaw.ai](https://docs.openclaw.ai/)

Первоначально «Clawdbot» (нояб. 2025), переименован после претензий по товарному знаку. Самый быстрорастущий open-source проект в истории (~250k звёзд за ~60 дней).

**Ключевые возможности:** 23+ интеграции мессенджеров, полная автоматизация браузера, голосовые звонки через Ring-a-Ding/Vapi (агент сам звонит в клинику и записывает), планировщик cron/heartbeat для работы без присмотра, маркетплейс навыков, интеграция MCP.

**Требования:** Node.js 22.16+, минимум 4 ГБ RAM (только текст), 8 ГБ для браузера, 10 ГБ SSD. GPU не требуется.

**Стабильность:** Неоднозначная. Широкие сбои в v2026.4.26; уязвимость безопасности в мае 2026. Версия v2.26+ стабилизируется.

### Hermes Agent
**GitHub:** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **Документация:** [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/docs/)

MIT, ~134k звёзд, Nous Research. Ключевая функция: петля самосовершенствования — агент создаёт навыки из опыта; модуль Curator оценивает, объединяет и удаляет навыки раз в 7 дней.

**Ключевые возможности:** 70+ встроенных инструментов, автоматизация браузера (в т.ч. Browserbase с разгадыванием CAPTCHA), делегирование суб-агентам, кросс-сессионная память, cron на естественном языке, Windows native beta.

**Требования:** минимум 1 vCPU / 2 ГБ RAM (только текст), рекомендуется 4–8 ГБ. Работает на VPS за $5/месяц.

**Стабильность:** Наиболее production-стабильный из пяти. Активная поддержка Nous Research.

### ZeroClaw
**GitHub:** [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | **Документация:** [docs.zeroclawlabs.ai](https://docs.zeroclawlabs.ai/en/)

Полная переработка на Rust. 20k+ звёзд. Бинарник 3,4 МБ, <5 МБ RAM в режиме ожидания, запуск <10 мс. Предкомпилированные бинарники для Linux, macOS, Windows, ARM, x86, RISC-V.

**Стабильность:** Pre-1.0 (v0.1.6). Проблемы качества кода (261 вызов `.unwrap()`). Идеально для лёгкого персонального использования, особенно на NAS/низкопотребляющем оборудовании.

### NemoClaw
**GitHub:** [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | **Страница:** [nvidia.com/en-us/ai/nemoclaw](https://www.nvidia.com/en-us/ai/nemoclaw/)

Стек безопасности NVIDIA поверх OpenClaw. Добавляет: sandbox Landlock + seccomp + netns, маршрутизатор моделей, управление политиками сети, приватный роутер. Минимальные требования: 8 ГБ RAM, 20 ГБ диск. Альфа-версия.

### Zo
**Сайт:** [zo.computer](https://www.zo.computer/) | **Цена:** от $18/месяц

Управляемый облачный компьютер-как-услуга. Не поддаётся self-hosting. Встроенные интеграции с Gmail, Google Calendar, Google Drive, Dropbox, Linear, Notion. Самый надёжный из пяти, но без локального контроля.

## Возможности для личных задач

| Задача | OpenClaw | Hermes | ZeroClaw | Zo |
|---|---|---|---|---|
| Поиск недвижимости (Zillow и др.) | ✅ Подтверждено | ✅ Возможно | 🟡 Возможно | 🟡 Ограничено |
| Запись к врачу (веб-форма) | ✅ | 🟡 | 🟡 | ❌ |
| Запись к врачу (телефонный звонок) | ✅ Ring-a-Ding/Vapi | ❌ | ❌ | ❌ |
| Управление календарём | ✅ | ✅ | 🟡 | ✅ Google Calendar |
| Управление email | ✅ | ✅ | 🟡 | ✅ Gmail |
| Мониторинг цен | ✅ | ✅ Подтверждено | 🟡 | 🟡 |
| Задачи по расписанию (cron) | ✅ | ✅ | ✅ | 🟡 |

## Размещение на Synology DS923+ (AMD Ryzen R1600, 4 ГБ RAM)

| Агент | 4 ГБ (штатно) | 8–16 ГБ | Примечания |
|---|---|---|---|
| **ZeroClaw** | ✅ Идеально (<5 МБ RAM) | ✅ | Лучший выбор для NAS |
| **OpenClaw** | ⚠️ Едва (только текст) | ✅ (браузер при 8 ГБ+) | Использовать готовый GHCR-образ |
| **Hermes Agent** | ⚠️ Очень тесно | ✅ | VPS за $5/мес проще |
| **NemoClaw** | ❌ (минимум 8 ГБ) | ⚠️ | Для NAS не предназначен |
| **Zo** | N/A | N/A | Только облако |

## Интеграции мессенджеров

| Платформа | OpenClaw | Hermes | ZeroClaw | Zo |
|---|---|---|---|---|
| Telegram | ✅ | ✅ | ✅ | ✅ |
| WhatsApp | ✅ | ✅ | ✅ | ❌ |
| Signal | ✅ | ✅ | ✅ | ❌ |
| Discord | ✅ | ✅ | ✅ | ❌ |
| Slack | ✅ | ✅ | ✅ | ❌ |
| Matrix | ✅ | ✅ | ✅ | ❌ |
| iMessage | ✅ | ❌ | ❌ | ❌ |
| Synology Chat | ✅ | ❌ | ❌ | ❌ |
| Email | ✅ | ✅ | ✅ | ✅ |
| Facebook Messenger | ❌ | ❌ | ❌ | ❌ |
| **Итого** | **23+** | **20+** | **30+** | **4** |

**Facebook Messenger:** ни один из пяти агентов не имеет подтверждённой интеграции с Facebook Messenger по состоянию на май 2026. Ограниченный Graph API Facebook делает неофициальные интеграции ненадёжными. Ближайшая альтернатива — WhatsApp Business API (поддерживается OpenClaw и Hermes).

## Связанные записи
- [[claude-code-agentic-loop]] ([Claude Code Agentic Loop](../agents/claude-code-agentic-loop.md))
- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[tencent-db-agent-memory]] ([TencentDB Agent Memory: Local Long-Term Memory for AI Agents](../tools/tencent-db-agent-memory.md))
- [[new-organizational-models-ai-agents]] ([New Organizational Models for the Age of AI Agents](../agents/new-organizational-models-ai-agents.md))
- [[package-hallucination-mcp]] ([Package Hallucination Catcher: MCP Server for LLM Package Recommendations](../tools/package-hallucination-mcp.md))
