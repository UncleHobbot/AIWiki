---
title: "T3 Code — The Agent Harness Control Surface by Theo Browne (Ping.gg)"
title_ru: "T3 Code — поверхность управления агентными харнесами от Theo Browne (Ping.gg)"
category: tools
tags: [t3-code, theo-browne, agent-orchestration, git-worktrees, mobile-control, open-source, ping-gg]
aliases: [t3.code, t3code, T3 Code, agent harness control surface]
confidence: high
updated: 2026-09-03
sources:
  - https://github.com/pingdotgg/t3code
  - https://t3.codes
  - https://flaviocopes.com/t3-code/
  - https://betterstack.com/community/guides/ai/t3-code/
  - https://x.com/theo/status/2079752200243560688
  - https://www.indiehackers.com/post/tech/theo-browne-on-how-hes-bringing-in-over-1m-yr-as-a-creator-and-founder-tJPQiOnONnf7pJ9m1PTP
  - https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-08-t3-code-doubles-down-on-zero-markup-pricing-as-a-trust-play/
---

## Summary

**T3 Code** (stylized `t3.code`, repo `pingdotgg/t3code`) is a free, open-source **"agent harness control surface"** — "a harness for your AI harnesses." Built by **Theo Browne** (t3.gg, T3 Stack, T3 Chat) under his company **Ping.gg**, it is a local-first GUI (desktop + web + mobile) for orchestrating and supervising the AI coding agents *already installed on your machine* — Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Grok, and custom agents via config. It runs **no models itself** and charges nothing: you keep your existing subscriptions. Production-launched ~July 28, 2026; **20,000 GitHub stars within a month**; v0.2.x line with active nightlies as of September 2026.

## Key Ideas

- **It sits one layer above agent CLIs — the layer this wiki calls orchestration.** T3 Code does not replace Claude Code/Codex/OpenCode; it requires them installed and supervises them: run/monitor multiple agents simultaneously, status pills, thinking preview, completion/failure alerts, and atomic **queue/drain** controls (queue tasks, then drain all agents at once).
- **Mobile remote control is the differentiator.** iOS + Android apps let you launch, monitor, and steer desktop agents remotely (ngrok tunnel + QR pairing) — no competing harness ships this. "Runs Every AI Coding Agent From One Screen."
- **Git-worktree-centric safety model:** per-agent worktree isolation, orphaned-worktree cleanup (`t3 worktree prune`), and two-tier git safety — the master worktree is protected from destructive operations; agents work on their own branches with auto-push, auto-rebase, and PR-open.
- **Spec-driven workflow:** a `spec.md` per worktree drives brainstorm → plan → execute; plan consultation via CLI args.
- **Free with zero markup as a trust play:** no subscription, no seat pricing — you pay only the underlying providers. Theo made a "public bet" on cost transparency vs subscription-based competitors (EnterpriseDNA analysis, Aug 2026).
- **Extensibility by delegation, not replacement:** agent routing via `.t3/agents.json` (custom agents supported, v0.2.33); branch orchestration graph (v0.2.30); CLI companions `t3 daemon` (background server) and `t3 doctor` (environment diagnosis). MCP/skills support is *inherited* from the wrapped agents — T3 Code ships no native extension marketplace.
- **Complementary, not competitive** — the correct mental model vs ZCode: ZCode is a vendor harness trying to be your one-stop surface (model + plan + GUI); T3 Code is a vendor-agnostic layer above whatever harnesses you already pay for.

## Details

### Architecture & platforms

Desktop app (Windows, macOS, Linux; Tauri v2), a locally-served web GUI at `http://localhost:3000` (LAN-accessible), and iOS/Android mobile apps for remote control. No CLI-first workflow — the CLI tools (`daemon`, `doctor`, `worktree prune`) support the GUI, not replace it. Cross-agent handoff exists but Theo explicitly declines to standardize it.

### Release history

- Repo created Feb 8, 2026; developed largely in the open (streamed on Theo's channel).
- Hyped launch July 21–22, 2026 ("I'm proud that we get to do it entirely in the open"); production launch ~July 28, 2026.
- v0.2.30 branch-orchestration graph; v0.2.33 custom agent routing; nightly channel active (0.0.39-nightly, Sept 2, 2026).
- Reported user counts conflict between sources: 60k+ (IndieHackers) vs ~120k control-plane users (podcast) — both Theo-reported.

### Community reception — polarized

- **Adoption is real:** 20k stars in ~a month post-launch; BetterStack and Flavio Copes published official-depth guides; a comparison ecosystem with CodeAgentSwarm (closest analogue) exists.
- **Skepticism is equally real:** HN threads on Theo are characteristically hostile; r/LocalLLaMA flags a contradiction between "owned by the community" rhetoric and not accepting community contributions; skeptics note his on-stream agent demos frequently fail.
- Theo's own positioning is maximalist: *"T3 Code is one of the best agentic code tools right now… about to leap frog the others"* (X, Jul 2026) — marketing, not assessment.
- Monetization remains an open question — community demand for a paid tier exists; Theo's revenue currently comes from T3 Chat (~$1M+/yr).

### vs ZCode (see [[zcode-zai-agentic-development-environment]])

Both address the same real problem — supervising multiple long-running agent sessions — from opposite ends. ZCode bundles model + plan + GUI from one vendor (and now pushes GLM-5.3 + points-quota + mobile Remote Control); T3 Code is model-agnostic, free, and BYO-subscription. ZCode's Remote Control (WeChat/Feishu) is the direct answer to T3's mobile apps. If you standardize on GLM, ZCode is deeper; if you run mixed agents (Claude + Codex + Gemini), T3 Code is the neutral layer.

## Notable Quotes

> "A harness for your AI harnesses." — T3 Code README
>
> "I'm proud that we get to do it entirely in the open." — Theo Browne, launch
>
> "T3 Code doubles down on zero-markup pricing as a trust play." — EnterpriseDNA

## Honest Gaps

- **Exact license** reported as MIT but not directly verified from the LICENSE file.
- **No T3-Code-native MCP/extension API** verified — extensibility is delegated to wrapped agents.
- **User counts (60k vs 120k) conflict** between sources; both are Theo-reported, no independent metric.
- **No dedicated HN launch thread found** — reception lives on X/YouTube/Reddit/blogs, which biases the picture both ways.
- Windows desktop availability implied by Tauri + a SourceForge mirror, but the official platform matrix wasn't directly read.

## Related Entries

- [[zcode-zai-agentic-development-environment]] ([ZCode — Z.ai's ADE](zcode-zai-agentic-development-environment.md))
- [[claude-code]] ([Claude Code](claude-code.md))
- [[opencode]] ([OpenCode](opencode.md))
- [[orkestra-multi-cli]] ([Orkestra Multi-CLI](orkestra-multi-cli.md))
- [[agentplugins-cross-harness]] ([AgentPlugins](agentplugins-cross-harness.md))
- [[using-git-worktrees-claude-code]] ([Git Worktrees in Claude Code](../tips/using-git-worktrees-claude-code.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](../tips/hard-gates-over-soft-prompts.md))

---
<!-- RU -->

## Краткое описание

**T3 Code** (стилизовано `t3.code`, репо `pingdotgg/t3code`) — бесплатная открытая **«поверхность управления агентными харнесами»** — «харнес для ваших харнесов». Создана **Theo Browne** (t3.gg, T3 Stack, T3 Chat) под эгидой его компании **Ping.gg**: локальная GUI-среда (десктоп + веб + мобильные) для оркестрации и надзора за ИИ-кодинг-агентами, *уже установленными на вашей машине* — Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Grok и кастомных агентов через конфиг. Сама **не запускает моделей** и ничего не стоит: вы сохраняете существующие подписки. Продакшн-релиз ~28 июля 2026; **20 000 звёзд GitHub за месяц**; линия v0.2.x с активными nightly на сентябрь 2026.

## Ключевые идеи

- **Сидит на слой выше агентных CLI — слой оркестрации.** T3 Code не заменяет Claude Code/Codex/OpenCode, а требует их установленными и надзирает: одновременный запуск/мониторинг множества агентов, статус-плашки, превью мышления, алерты завершения/падения и атомарные **queue/drain**-управления (поставить задачи в очередь, затем запустить всех разом).
- **Мобильное удалённое управление — главный дифференциатор.** Приложения iOS + Android позволяют запускать, мониторить и вести десктопных агентов удалённо (ngrok-туннель + QR-связка) — ни один конкурент этого не даёт.
- **Модель безопасности вокруг git-worktree:** изоляция агентов по воркспейсам, очистка осиротевших (`t3 worktree prune`), двухуровневая git-безопасность — мастер-воркспейс защищён от разрушительных операций; агенты работают в своих ветках с auto-push, auto-rebase и открытием PR.
- **Spec-driven воркфлоу:** `spec.md` на воркспейс ведёт brainstorm → plan → execute.
- **Бесплатно с нулевой наценкой как ставка на доверие:** ни подписки, ни по-местной оплаты — платите только провайдерам. Theo публично сделал «ставку» на прозрачность стоимости против подписочных конкурентов.
- **Расширяемость через делегирование, а не замену:** маршрутизация агентов через `.t3/agents.json`; граф оркестрации веток (v0.2.30); CLI-спутники `t3 daemon` и `t3 doctor`. Поддержка MCP/skills *наследуется* от обёрнутых агентов.
- **Дополняющий, а не конкурирующий** — правильная модель против ZCode: ZCode — вендорский харнес «всё в одном» (модель + план + GUI); T3 Code — вендор-агностичный слой над харнесами, за которые вы уже платите.

## Подробнее

### Архитектура и платформы

Десктоп-приложение (Windows, macOS, Linux; Tauri v2), локальный веб-GUI на `http://localhost:3000` (доступен по LAN) и мобильные приложения iOS/Android для удалённого управления. CLI-инструменты (`daemon`, `doctor`, `worktree prune`) поддерживают GUI, а не заменяют его.

### История релизов

Репо создан 8 февраля 2026; разработка в открытом режиме (стримы Theo). Разогретый запуск 21–22 июля 2026; продакшн-релиз ~28 июля 2026. v0.2.30 — граф оркестрации веток; v0.2.33 — маршрутизация кастомных агентов; активный nightly-канал. Числа пользователей расходятся между источниками: 60k+ против ~120k — оба от Theo.

### Реакция сообщества — поляризована

**Внедрение реально:** 20k звёзд за ~месяц; гайды от BetterStack и Flavio Copes; экосистема сравнений с CodeAgentSwarm (ближайший аналог). **Скепсис equally реален:** враждебные треды HN о Theo; r/LocalLLaMA отмечает противоречие между риторикой «принадлежит сообществу» и отказом принимать контрибуции; скептики замечают, что агентные демо на стримах часто падают. Позиционирование самого Theo максималистично — маркетинг, не оценка.

### против ZCode (см. [[zcode-zai-agentic-development-environment]])

Оба решают одну реальную проблему — надзор за множеством долгоживущих агентных сессий — с противоположных концов. ZCode бандлит модель + план + GUI от одного вендора (теперь с GLM-5.3 + очковой квотой + мобильным Remote Control); T3 Code — модель-агностичен, бесплатен и BYO-подписка. Remote Control у ZCode (WeChat/Feishu) — прямой ответ на мобильные приложения T3. Если стандартизуетесь на GLM — ZCode глубже; если гоняете смешанных агентов (Claude + Codex + Gemini) — T3 Code нейтральный слой.

## Примечательные цитаты

> «Харнес для ваших харнесов.» — README T3 Code
>
> «Горжусь, что делаем это полностью открыто.» — Theo Browne, запуск
>
> «T3 Code делает ставку на нулевую наценку как на элемент доверия.» — EnterpriseDNA

## Честные пробелы

- **Точная лицензия** — сообщается MIT, но файл LICENSE напрямую не проверен.
- **Нативного MCP/extension API T3 Code** не верифицировано — расширяемость делегирована обёрнутым агентам.
- **Числа пользователей (60k против 120k) расходятся**; оба от Theo, независимой метрики нет.
- **Отдельного треда запуска на HN не найдено** — реакция живёт в X/YouTube/Reddit/блогах, что искажает картину в обе стороны.
- Доступность Windows-десктопа подразумевается Tauri + зеркало на SourceForge, но официальная матрица платформ не прочитана напрямую.

## Связанные записи

- [[zcode-zai-agentic-development-environment]] ([ZCode — Z.ai's ADE](zcode-zai-agentic-development-environment.md))
- [[claude-code]] ([Claude Code](claude-code.md))
- [[opencode]] ([OpenCode](opencode.md))
- [[orkestra-multi-cli]] ([Orkestra Multi-CLI](orkestra-multi-cli.md))
- [[agentplugins-cross-harness]] ([AgentPlugins](agentplugins-cross-harness.md))
- [[using-git-worktrees-claude-code]] ([Git Worktrees in Claude Code](../tips/using-git-worktrees-claude-code.md))
- [[hard-gates-over-soft-prompts]] ([Hard Gates Beat Soft Prompts](../tips/hard-gates-over-soft-prompts.md))
