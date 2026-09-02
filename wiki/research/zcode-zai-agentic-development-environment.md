---
title: "ZCode — Z.ai's Agentic Development Environment (Deep Dive)"
title_ru: "ZCode — агентная среда разработки от Z.ai (глубокий разбор)"
category: research
tags: [zcode, zai, glm, coding-agent, desktop-app, agentic-ide, chinese-llm, agents-md, mcp]
aliases: [Z Code, zcode.z.ai, ZCode ADE, ZCode 3.0]
confidence: high
updated: 2026-09-03
sources:
  - https://zcode.z.ai/en
  - https://zcode.z.ai/en/docs/agents
  - https://zcode.z.ai/en/docs/install
  - https://zcode.z.ai/en/docs/configuration
  - https://zcode.z.ai/en/changelog
  - https://z.ai/blog/glm-5.3
  - https://www.reddit.com/r/ZaiGLM/comments/1w3dp1h/
  - https://zcode.z.ai/cn/docs/qa
  - https://docs.z.ai/devpack/overview
  - https://github.com/zai-org
  - https://github.com/zai-org/zai-coding-plugins
  - https://www.reddit.com/r/ZaiGLM/comments/1uat8yw/harnesses_zcode_vs_claude_code/
  - https://www.reddit.com/r/ZaiGLM/comments/1u5pv7p/zcode_300_harness_vs_others/
  - https://www.reddit.com/r/ZaiGLM/comments/1u5jy0l/my_taste_on_free_glm52_with_zcode/
  - https://www.reddit.com/r/ZaiGLM/comments/1u9af41/zcode_free_trial_extremely_slow_and_connection/
  - https://www.reddit.com/r/ZaiGLM/comments/1uk6b12/well_zai_lied_about_no_weekly_limit_on_the_max/
  - https://www.reddit.com/r/ZaiGLM/comments/1ug9iha/heavy_claude_code_user_switching_to_glm52/
  - https://www.reddit.com/r/ZaiGLM/comments/1u6dmy4/glm_coding_plan_dilemma/
  - https://www.reddit.com/r/opencodeCLI/comments/1u93tn4/glm_coding_plan_value_for_money/
  - https://www.reddit.com/r/LocalLLaMA/comments/1u832oh/glm52_max_is_currently_the_third_best_model/
  - https://news.ycombinator.com/item?id=47636595
  - https://news.ycombinator.com/item?id=47641008
---

## Summary

**ZCode** is Z.ai's (Zhipu AI's) closed-source **desktop Agentic Development Environment (ADE)** — the official harness for the **GLM-5.2** model (1M-token context). Unlike Claude Code, Codex, or OpenCode (terminal CLIs), ZCode is a GUI application that positions an AI agent as the primary developer. It supports MCP, skills, sub-agents, multiple execution/permission modes, is configured via `AGENTS.md`, and is genuinely **multi-provider** (GLM plus any Anthropic- or OpenAI-compatible endpoint). Latest version **v3.2.2** (July 1, 2026); the 3.0 release introduced GLM-5.2 optimization and multi-agent collaboration.

## Key Ideas

- **Form factor: a desktop GUI app, not a CLI.** Z.ai explicitly calls it an "Agentic Development Environment (ADE) — unlike traditional IDEs, the AI Agent takes the lead role in development." Distributed as a signed installer (Windows .exe, macOS .dmg). Linux is internal beta only.
- **Deeply adapted for GLM-5.2** (1M-token context). ZCode's default agent is tuned for long-horizon task planning, multi-turn context retention, and continuous code changes on the GLM-5.2 model family.
- **Genuinely multi-provider.** Built-in support for Z.ai, BigModel (Zhipu), Anthropic, OpenAI, OpenRouter, Moonshot (Kimi), MiniMax, Xiaomi MiMo, DeepSeek, and any Anthropic/OpenAI-compatible endpoint. Automatic model-list detection.
- **First-class MCP, skills, and sub-agents.** Skills invoked via `$`; `@` references files; `/` runs saved commands; `#` links past conversations. The on-disk install contains a full agentic runtime with sub-agent session logs.
- **Five execution modes** (cycle with `Shift+Tab`): Default, Confirm Before Changes, Auto Edit, Plan Mode, Full Access — a permission-model granularity comparable to Claude Code.
- **Configured via `AGENTS.md`** (user-global at `~/.zcode/AGENTS.md` + workspace `AGENTS.md`). `CLAUDE.md` is used only as a one-time migration source during onboarding, not read at runtime.
- **Bilingual by design** — fully native Chinese and English docs; GLM is Chinese-origin, giving ZCode a real edge on Chinese-language prompts.
- **Free to start** with a daily GLM quota (new Zhipu registrations get ~20M tokens); scales via Lite/Pro/Max GLM Coding Plan subscriptions.

## What ZCode Actually Is (and Isn't)

A frequent point of confusion: **ZCode ≠ GLM Coding Plan ("devpack").**

- **ZCode** is the desktop ADE product at `zcode.z.ai` — the harness itself.
- **GLM Coding Plan** is a *subscription* that lets you run GLM models inside *third-party* CLI/IDE tools (Claude Code, Cline, OpenCode, Codex, etc.). The `docs.z.ai/devpack/` pages document this subscription, not ZCode.

ZCode is the only one of the major coding-agent surfaces that ships as a **desktop GUI application** rather than a terminal CLI. Cursor, Windsurf, and Trae are GUI *editors*; ZCode is an agent-first ADE that orchestrates the full development loop — planning, code editing, terminal, Git, and browser context — from one task surface.

## Details

### Installation & Platforms

| Platform | Status |
|---|---|
| macOS (Apple Silicon + Intel) | Stable |
| Windows | Stable |
| Linux | Internal beta (invite group) |

Installation is via a native signed installer downloaded from the homepage — **not** npm/brew/cargo. No public source repository exists under the [zai-org GitHub org](https://github.com/zai-org); ZCode is closed-source. The public repos are the SDKs (`z-ai-sdk-python`, `z-ai-sdk-java`) and the [zai-coding-plugins](https://github.com/zai-org/zai-coding-plugins) marketplace for Claude Code.

### Models & Providers

Built-in first-party models:

| Model | Context | Output | Notes |
|---|---|---|---|
| **GLM-5.2** | 1,000,000 (1M) | — | Flagship; ZCode Agent is "deeply adapted" for it |
| **GLM-5-Turbo** | 200,000 | 64,000 | Reasoning on/off toggle |

Both first-party provider endpoints (Z.ai for global, BigModel for China) speak the **Anthropic protocol** natively, with OpenAI-protocol endpoints also available. This is why GLM works inside Claude Code, Cline, and other Anthropic-compatible harnesses — and why ZCode itself can host Claude, Kimi, DeepSeek, etc.

### Execution Modes

| Mode | Behavior | Best for |
|---|---|---|
| **Default** | Standard strategy, balances progress with confirmations | Everyday dev, routine edits |
| **Confirm Before Changes** | Confirms every file edit or command | Critical code, production configs |
| **Auto Edit** | Auto file edits; commands still confirmed | Routine iteration |
| **Plan Mode** | Plans first, implements after confirmation | Complex multi-step tasks |
| **Full Access** | Minimal interruptions, continuous execution | Clear, lower-risk tasks |

### Project Instructions (`AGENTS.md`)

ZCode reads two sources — user-global (`~/.zcode/AGENTS.md`) appended first, then workspace (`AGENTS.md`). It does **not** merge across directory levels, scan child directories, expand `@import`, or pick rule files by task type. `CLAUDE.md` is consumed once during onboarding (content copied into `AGENTS.md`), then ignored at runtime.

### Pricing (GLM Coding Plan)

Token/quota-based, tied to a plan — not a flat seat subscription. Promo pricing as of mid-2026 (regular price in parentheses):

| Plan | Price (promo / regular) | Prompts / 5 hrs (standard) |
|---|---|---|
| Lite | ~$3 / ~$18 per month | ~80 |
| Pro | ~$15 / ~$72 per month | ~400 |
| Max | ~$20 / ~$160 per month | ~1,600 |

GLM-5.2 consumes more quota than older GLM models. A time-limited promo meters GLM-5.2 at a 0.67 factor (~1.5× usable quota) through July 31, 2026. Max is recommended for 2+ simultaneous projects.

## Community Reception

ZCode discussion is concentrated on **r/ZaiGLM**. Sentiment is **polarized**: the GLM models are widely praised; ZCode-the-harness and the Coding Plan draw frequent criticism.

### What users praise
- **Prompt-based usage model** (more granular than per-message plans like Claude/Codex).
- **Built-in skills** — e.g., a "frontend design" skill that produced "great" home-page results.
- **"Cozy," integrated single-vendor experience** (model + harness + plan in one product).
- The GLM-5.2 model itself: *"GLM 5.2 and Kimi K2.7 Code are the best agentic coding models"* (r/LocalLLaMA).
- A 14k-LoC test on r/opencodeCLI with 5 sub-agents over 14 min: *"results were actually quite good."*

### What users criticize
- **Throttling / reliability:** the free trial is reported "extremely slow" — a basic prompt taking 15+ minutes; "hype overstated." Non-ZCode clients using the Coding Plan (Hermes, OpenClaw) get spammed with 429 / code 1305 errors, suggesting z.ai prioritizes its own client.
- **"The in-house harness confuses the model":** an r/ZaiGLM thread on ZCode 3.0.0 claims the harness makes intent harder to understand and increases "cheating behavior"; the same user prefers third-party harnesses. A notable finding: **ZCode is not always the preferred harness even for its own vendor's plan.**
- **Max-plan weekly-limit controversy:** users who joined ~mid-February 2026 report Max was marketed as *no weekly cap* (only a rolling 5-hour cap), then a weekly cap (~1B tokens) was added — perceived as bait-and-switch, especially for yearly subscribers. See [[zai-max-plan-undisclosed-weekly-limit]].
- **Limited plugin shop** vs. Claude Code's ecosystem: *"ZCode is nice, cozy and works well, but plugins shop is very limited."* (r/ZaiGLM)
- **ToS risk:** non-coding use of the Coding Plan can trigger throttling and reportedly permanent bans after three offenses.

### Positioning vs. competitors
- **vs. Claude Code:** Cheaper (~1/3 to ~14× cheaper per token); weaker on latency, reliability, and (per some users) model intelligence. Claude wins SWE-bench benchmarks. ZCode's edge: prompt-based usage and the integrated model+plan+skills bundle.
- **vs. Codex / OpenCode:** Codex/OpenCode win speed, token-efficiency, sandbox maturity. ZCode wins cost and bidirectional capability — it both *is* an agent host *and* can orchestrate competitor CLIs.
- **Notable absence:** no dedicated third-party benchmark of ZCode-the-harness exists in Tier-2 press; coverage compares *models* (GLM vs Claude/GPT) or harnesses that exclude ZCode.

## Notable Quotes

> "ZCode is nice, cozy and works well, but plugins shop is very limited." — r/ZaiGLM
>
> "I've had a good experience, and it's 1/3rd of the price." — Hacker News
>
> "GLM 5.2 and Kimi K2.7 Code are the best agentic coding models. Insane work by Z and Moonshot." — r/LocalLLaMA

## Version History

- **v3.10.2** — Aug 31, 2026 (current at September update).
- **v3.7.7** — Aug 14, 2026: GLM-5.3 flagship available in ZCode (same day as the model launch).
- **v3.2.2** — July 1, 2026 (at the time of the original deep-dive below).
- **v3.0** — major milestone: "GLM-5.2 optimized, better multi-agent collaboration." The 3.x line is tied to the GLM-5.2 launch window (June 2026).
- Exact original release date not published in primary sources. Note: no public changelog entries exist for v3.4.x–v3.7.4 (July 16 – Aug 9) — a version-numbering gap that could not be verified.

## September 2026 Update (v3.3 → v3.10.2)

Two months of rapid iteration substantially changed the picture from the July deep-dive below:

### GLM-5.3 era (Aug 14 onward)
- **GLM-5.3** landed in ZCode in v3.7.7 (Aug 14, launch day) — ZCode is now branded "Official Harness for GLM-5.3." Three effort levels (low/high/max, default max). **Breaking change:** thinking can no longer be disabled at the API level.
- **GLM-5.3-Flash multimodal** arrived in v3.9.2 (Aug 26) out of the box for subscribers — screenshot/image understanding, improved Computer Use accuracy, permission prompts before computer control, Intel-chip macOS support.

### New capability surface (July–August)
- **Goal mode** — plan → code → test → verify loops until the target is met (long-horizon mode).
- **Remote Control** — monitor and steer long-running tasks from a phone via WeChat or Feishu.
- **Idle-time tasks** — subscribers run tasks free without consuming plan quota; custom-model subagents for them (v3.7.5).
- **Background sub-agents and bash** (v3.3.4), minute-based automations (v3.7.5), workspace-level Hooks (v3.8.1), MCP OAuth for local dev (v3.3.2), multi-language codebase Wiki generation (v3.3.6).
- **Computer Use / Browser Control** matured: video recording in the built-in browser, renamed from "Browser" (v3.10.1).
- **New Team plan** (v3.3.0); "Weekend Plan" free-quota claiming via friend invites (v3.10.1).

### Pricing shift: points-based quota
With GLM-5.3, the GLM Coding Plan switched to a **points-based quota**: points counted separately for input / cached-input / output tokens; **off-peak = 50% of standard points** (peak = 14:00–18:00 UTC+8 Mon–Fri; weekends are off-peak). Third-party trackers put GLM-5.3-Flash at 0.4× off-peak / 1.2× peak (unverified against official docs). A 1.5× limited-time quota boost in ZCode ran through Aug 31, stackable with ~30% cache savings. Tier prices per trackers: Lite ~$18, Pro ~$72–80, Max ~$160–168 per month (sources disagree; verify at z.ai/subscribe).

### Community reception shift
- **The harness criticism flipped:** *"ZCode was an awful harness until very recently, now it has a really high cache rate and barely ever tool call errors. They give 150% usage"* (r/ZaiGLM, Sept 2026) — directly contradicting the July "confuses the model" complaints.
- **Quota friction remains the top complaint:** "server busy" notices on free tiers, "very strict quota" reports (r/ZaiGLM, Aug 2026).
- **No ZCode↔AutoClaw integration exists** — AutoClaw is a separate Zhipu product (zero-threshold local agent supporting OpenClaw core capabilities); OpenClaw appears only as a GLM Coding Plan-compatible tool.
- **Linux remains beta** (x64 + ARM64 AppImage via Feishu beta group); no GA announcement found.

## Honest Gaps

- **No public CLI repo.** ZCode is closed-source; only SDKs and a plugin marketplace are open. An unofficial community CLI exists at `murticla/zai-cli` — not official.
- **Benchmark coverage of ZCode-the-harness is essentially absent** in Tier-2 press; all comparisons in the wild are model-level.
- **Most community findings are Tier 3** (single-user Reddit posts). The throttling, weekly-cap, and "confuses the model" claims recur across multiple independent users, which raises confidence, but none are officially confirmed by z.ai.

## Related Entries

- [[product-zai-glm]] ([z.ai / GLM](../models/product-zai-glm.md))
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[claude-code]] ([Claude Code](../tools/claude-code.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[kimi-code-cli]] ([Kimi Code CLI](../tools/kimi-code-cli.md))
- [[zai-max-plan-undisclosed-weekly-limit]] ([z.ai Max Plan — Undisclosed Weekly Limit](../news/zai-max-plan-undisclosed-weekly-limit.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[t3-code]] ([T3 Code](t3-code.md))
- [[t3-code]] ([T3 Code](t3-code.md))

---
<!-- RU -->

## Краткое описание

**ZCode** — закрытая **десктопная агентная среда разработки (ADE)** от Z.ai (Zhipu AI), официальный харнес для модели **GLM-5.2** (контекст 1M токенов). В отличие от Claude Code, Codex или OpenCode (терминальных CLI), ZCode — это GUI-приложение, где ИИ-агент выступает главным разработчиком. Поддерживает MCP, skills, сабагентов, несколько режимов исполнения/разрешений, настраивается через `AGENTS.md` и является **мультипровайдерным** (GLM плюс любой Anthropic- или OpenAI-совместимый эндпоинт). Актуальная версия **v3.2.2** (1 июля 2026); релиз 3.0 добавил оптимизацию под GLM-5.2 и много-агентное взаимодействие.

## Ключевые идеи

- **Форм-фактор: десктопное GUI-приложение, а не CLI.** Z.ai прямо называет это «агентной средой разработки (ADE) — в отличие от традиционных IDE, ИИ-агент берёт на себя ведущую роль в разработке». Распространяется как подписанный установщик (Windows .exe, macOS .dmg). Linux — только внутренняя бета.
- **Глубоко адаптирован под GLM-5.2** (контекст 1M токенов): длительное планирование задач, удержание контекста между ходами, непрерывные правки кода.
- **Действительно мультипровайдерный.** Встроенная поддержка Z.ai, BigModel (Zhipu), Anthropic, OpenAI, OpenRouter, Moonshot (Kimi), MiniMax, Xiaomi MiMo, DeepSeek и любого Anthropic/OpenAI-совместимого эндпоинта.
- **MCP, skills и сабагенты первого класса.** Skills через `$`; `@` — ссылки на файлы; `/` — сохранённые команды; `#` — прошлые беседы. В установке на диске — полноценный агентный рантайм с логами сабагентов.
- **Пять режимов исполнения** (`Shift+Tab`): Default, Confirm Before Changes, Auto Edit, Plan Mode, Full Access — детализация модели разрешений на уровне Claude Code.
- **Настраивается через `AGENTS.md`** (пользовательский `~/.zcode/AGENTS.md` + воркспейс `AGENTS.md`). `CLAUDE.md` используется только разово при онбординге, в рантайме не читается.
- **Двуязычен по дизайну** — полные нативные документации на китайском и английском; GLM — китайского происхождения.
- **Бесплатный старт** с дневной квотой GLM (новые регистрации Zhipu получают ~20M токенов); масштабируется через подписки Lite/Pro/Max.

## Чем ZCode является (и не является)

Частая путаница: **ZCode ≠ GLM Coding Plan («devpack»).**

- **ZCode** — десктопный ADE-продукт на `zcode.z.ai`, сам харнес.
- **GLM Coding Plan** — *подписка*, позволяющая запускать модели GLM в *сторонних* CLI/IDE (Claude Code, Cline, OpenCode, Codex). Страницы `docs.z.ai/devpack/` описывают подписку, а не ZCode.

ZCode — единственный из крупных surfaces кодинг-агентов, что поставляется как **десктопное GUI-приложение**, а не терминальный CLI. Cursor, Windsurf и Trae — GUI-*редакторы*; ZCode — agent-first ADE, оркестрирующий весь цикл разработки.

## Подробнее

### Установка и платформы

| Платформа | Статус |
|---|---|
| macOS (Apple Silicon + Intel) | Stable |
| Windows | Stable |
| Linux | Внутренняя бета (по приглашению) |

Установка — нативный подписанный установщик с домашней страницы, **не** npm/brew/cargo. Публичного репозитория с исходником под [zai-org на GitHub](https://github.com/zai-org) нет; ZCode закрыт. Открыты только SDK (`z-ai-sdk-python`, `z-ai-sdk-java`) и маркетплейс [zai-coding-plugins](https://github.com/zai-org/zai-coding-plugins) для Claude Code.

### Модели и провайдеры

Встроенные first-party модели: **GLM-5.2** (1M контекст, флагман, «глубоко адаптирован»), **GLM-5-Turbo** (200k контекст, 64k вывод, переключатель reasoning). Оба first-party эндпоинта (Z.ai для глобала, BigModel для Китая) говорят по протоколу **Anthropic** нативно — поэтому GLM работает в Claude Code, Cline и др., и наоборот — ZCode хостит Claude, Kimi, DeepSeek.

### Режимы исполнения

Default (стандарт), Confirm Before Changes (подтверждение каждой правки/команды), Auto Edit (авто-правки, команды с подтверждением), Plan Mode (план → реализация после подтверждения), Full Access (минимум прерываний).

### Инструкции проекта (`AGENTS.md`)

Два источника — пользовательский (`~/.zcode/AGENTS.md`, добавляется первым), затем воркспейс (`AGENTS.md`). Не мерджит по уровням директорий, не сканирует дочерние, не раскрывает `@import`. `CLAUDE.md` при онбординге копируется в `AGENTS.md` и далее игнорируется.

### Ценообразование (GLM Coding Plan)

Токеновая/квотная модель, привязанная к тарифу — не фиксированная подписка за место. Промо-цены на середину 2026 (регулярная в скобках): Lite ~$3 (~$18)/мес, Pro ~$15 (~$72)/мес, Max ~$20 (~$160)/мес. GLM-5.2 расходует больше квоты, чем старые модели; промо-фактор 0.67 (~1.5× квоты) до 31 июля 2026.

## Реакция сообщества

Дискуссии сосредоточены на **r/ZaiGLM**. Сентимент **поляризован**: модели GLM хвалят, сам харнес ZCode и Coding Plan часто критикуют.

### Что хвалят
- Prompt-based модель расхода (гранулярнее per-message планов Claude/Codex).
- Встроенные skills (например, «frontend design»).
- «Уютный» интегрированный опыт одного вендора (модель + харнес + тариф).
- Сам GLM-5.2: *«GLM 5.2 и Kimi K2.7 Code — лучшие агентные кодинг-модели»* (r/LocalLLaMA).

### Что критикуют
- **Троттлинг/надёжность:** бесплатный триал «крайне медленный», базовый промпт 15+ минут; сторонние клиенты (Hermes, OpenClaw) получают шквал 429/code 1305 — z.ai, по видимости, приоритизирует свой клиент.
- **«Харнес путает модель»:** тред на r/ZaiGLM о ZCode 3.0.0 утверждает, что встроенный харнес ухудшает понимание намерения и увеличивает «читинг»; автор предпочитает сторонние харнесы. Важная находка: **ZCode — не всегда предпочтительный харнес даже для плана собственного вендора.**
- **Контроверза о недельном лимите тарифа Max:** рекламировался как *без недельного потолка* (только скользящий 5-часовой), затем недельный потолок (~1B токенов) добавили тихо. См. [[zai-max-plan-undisclosed-weekly-limit]].
- **Ограниченный магазин плагинов** против экосистемы Claude Code.
- **Риск ToS:** некодинговое использование Coding Plan может привести к троттлингу и, по сообщениям, к перманентному бану после трёх нарушений.

### Позиционирование против конкурентов
- **vs. Claude Code:** дешевле (~1/3 – ~14× на токен), слабее по латентности, надёжности и (по мнению части пользователей) интеллекту модели. У ZCode — prompt-based расход и связка «модель+план+skills».
- **vs. Codex / OpenCode:** Codex/OpenCode выигрывают в скорости, токен-эффективности, зрелости песочницы. ZCode выигрывает по стоимости и бинаправленности — он и хост агента, и оркестратор чужих CLI.
- **Заметное отсутствие:** специализированного бенчмарка именно ZCode-харнеса в Tier-2 прессе нет; все сравнения — на уровне моделей.

## Примечательные цитаты

> «ZCode — приятный, уютный и хорошо работает, но магазин плагинов очень ограничен.» — r/ZaiGLM
>
> «У меня был хороший опыт, и это треть цены.» — Hacker News
>
> «GLM 5.2 и Kimi K2.7 Code — лучшие агентные кодинг-модели. Безумная работа Z и Moonshot.» — r/LocalLLaMA

## История версий

- **v3.2.2** — 1 июля 2026 (актуальная на момент написания).
- **v3.0** — крупный рубеж: «оптимизация под GLM-5.2, улучшенное много-агентное взаимодействие». Линейка 3.x привязана к окну запуска GLM-5.2 (июнь 2026).
- Точная дата первоначального релиза в первоисточниках не опубликована.

## История версий

- **v3.10.2** — 31 августа 2026 (актуальная на сентябрьское обновление).
- **v3.7.7** — 14 августа 2026: флагман GLM-5.3 доступен в ZCode (в день релиза модели).
- **v3.2.2** — 1 июля 2026 (на момент изначального разбора ниже).
- **v3.0** — крупный рубеж: «оптимизация под GLM-5.2, улучшенное много-агентное взаимодействие».
- Точная дата первоначального релиза не опубликована. Примечание: публичных записей changelog для v3.4.x–v3.7.4 нет (16 июля – 9 авг) — пробел в нумерации версий, который не удалось верифицировать.

## Сентябрьское обновление 2026 (v3.3 → v3.10.2)

Два месяца быстрой итерации заметно изменили картину июльского разбора ниже:

### Эра GLM-5.3 (с 14 августа)
- **GLM-5.3** появился в ZCode в v3.7.7 (14 августа, в день релиза модели) — ZCode теперь брендируется как «Official Harness for GLM-5.3». Три уровня effort (low/high/max, дефолт max). **Ломающее изменение:** thinking больше нельзя отключить на уровне API.
- **GLM-5.3-Flash мультимодальная** — в v3.9.2 (26 августа) из коробки для подписчиков: понимание скриншотов/изображений, улучшенная точность Computer Use, подтверждения перед управлением компьютером, поддержка Intel-маков.

### Новая поверхность возможностей (июль–август)
- **Режим Goal** — циклы план → код → тест → верификация до достижения цели.
- **Remote Control** — мониторинг и управление долгими задачами с телефона через WeChat или Feishu.
- **Idle-time задачи** — подписчики запускают задачи бесплатно, без расхода квоты плана.
- **Фоновые сабагенты и bash** (v3.3.4), минутные автоматизации (v3.7.5), Hooks на уровне воркспейса (v3.8.1), MCP OAuth для локальной разработки (v3.3.2), генерация Wiki кодовой базы (v3.3.6).
- **Computer Use / Browser Control** повзрослел: запись видео во встроенном браузере, переименован из «Browser» (v3.10.1).
- **Новый план Team** (v3.3.0); «Weekend Plan» с бесплатной квотой по приглашениям (v3.10.1).

### Смена ценообразования: очковая квота
С GLM-5.3 план GLM Coding перешёл на **очковую квоту**: очки считаются отдельно для входных / кэшированных / выходных токенов; **внепик = 50% стандартных очков** (пик = 14:00–18:00 UTC+8 пн–пт; выходные — внепик). Сторонние трекеры дают GLM-5.3-Flash 0.4× внепик / 1.2× пик (не верифицировано). Лимитированный буст квоты 1.5× в ZCode шёл до 31 августа. Цены тиров по трекерам: Lite ~$18, Pro ~$72–80, Max ~$160–168 в месяц (источники расходятся; проверяйте на z.ai/subscribe).

### Сдвиг в приёме сообществом
- **Критика харнеса развернулась:** «ZCode был ужасным харнесом до недавнего времени, теперь у него высокий cache rate и почти нет ошибок tool call. Дают 150% usage» (r/ZaiGLM, сентябрь 2026) — прямое противоречие июльским жалобам «путает модель».
- **Квотное трение остаётся главной жалобой:** «server busy» на бесплатных тирах, «очень строгая квота» (r/ZaiGLM, август 2026).
- **Интеграции ZCode↔AutoClaw не существует** — AutoClaw отдельный продукт Zhipu; OpenClaw лишь совместимый с GLM Coding Plan инструмент.
- **Linux остаётся в бете** (x64 + ARM64 AppImage через бета-группу Feishu); анонса GA не найдено.

## Честные пробелы

- **Нет публичного репозитория CLI.** ZCode закрыт; открыты только SDK и маркетплейс плагинов. Неофициальный community CLI — `murticla/zai-cli`, не официальный.
- **Бенчмарки именно ZCode-харнеса в Tier-2 прессе практически отсутствуют.**
- **Большинство находок сообщества — уровень 3** (единичные посты на Reddit). Шаблоны троттлинга, недельного потолка и «путает модель» повторяются у независимых пользователей, что повышает доверие, но z.ai официально это не подтверждает.

## Связанные записи

- [[product-zai-glm]] ([z.ai / GLM](../models/product-zai-glm.md))
- [[glm-5-2]] ([GLM-5.2](../models/glm-5-2.md))
- [[claude-code]] ([Claude Code](../tools/claude-code.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[kimi-code-cli]] ([Kimi Code CLI](../tools/kimi-code-cli.md))
- [[zai-max-plan-undisclosed-weekly-limit]] ([z.ai Max Plan — Undisclosed Weekly Limit](../news/zai-max-plan-undisclosed-weekly-limit.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
