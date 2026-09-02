---
title: "DHH on Agentic Programming, Vibe Coding, and Omarchy (Lex Fridman #501)"
title_ru: "DHH об агентном программировании, vibe coding и Omarchy (Lex Fridman #501)"
category: people
tags: [dhh, lex-fridman, agentic-engineering, vibe-coding, omarchy, rails, video-notes]
aliases: [DHH agentic, David Heinemeier Hansson AI, Omarchy agentic OS]
confidence: medium
updated: 2026-09-01
sources:
  - https://www.youtube.com/watch?v=NYFGCESmikA
  - https://news.ycombinator.com/item?id=49467437
---

## Summary
David Heinemeier Hansson (DHH), Ruby on Rails creator, describes his late-2025 conversion from AI-coding skeptic to one of the most prolific agentic engineers — now with AI writing 80–100% of his code. The conversation covers why he rejects both "agentic engineering" and "vibe coding" as terms, how agent work replaced single-threaded flow-state programming with parallel orchestration, and his Omarchy "agentic OS" Linux distribution.

## Key Ideas
- **From autocomplete skeptic to agentic convert:** a year earlier DHH liked chatbots as tutors but rejected autocomplete; agents "started as curiosities for five minutes and then got amazing." Now AI writes 80% of code — or 100% for non-public-facing products.
- **Terminology matters:** he hates "agentic engineering" ("we need a word as plain as *programming*") and rejects "vibe coding" for real work — vibe coding "smells exactly like script kiddies did in the early 2000s." His line: vibe coding = telling an agent to build software and *never looking at the implementation*; if you review the code, it's agent-accelerated development, i.e. still programming.
- **The flow-state shift:** hand-coding was single-threaded — deep immersion in one problem was "the portal to flow." With agents it becomes parallel processing: orchestrating many agents at once requires a different toolset and a different kind of attention.
- **Omarchy — the agentic OS:** his Arch-based Linux distro ships preinstalled with the full agent workshop (Neovim, terminal, OBS, Kden Live video editor, and his own keyboard-driven "Cut" clip editor). He frames it as part of an early "agentic OS / malleable computer" movement.
- **Subscription economics:** he runs *multiple* Claude subscriptions simultaneously (hit limits, signed up for a second account at 4am with jet lag), calls the subscription "a crazy bargain," and complains Anthropic won't let subscriptions stack cleanly — while noting Anthropic cut OpenCode off from subscriptions. His next Omarchy version ships multi-sub support tooling.
- **On refusals:** recounts a "HAL 9000 moment" — Claude refused to translate his own essay to Italian because it disagreed with the content.
- **On AI creativity:** his own creative moments feel like next-token prediction "with a bit of temperature sprinkled in," so he has no trouble believing AI's creative breakthroughs are real.

## Video Notes
- The "who is a programmer" argument: a CEO who hires programmers and ships software isn't called a programmer — so a vibe coder who never reads the implementation shouldn't be either. Programming implies understanding primitives (loops, conditions, variables), not just creating programs.
- Drudgery defense: of ~2,000 annual work hours, a programmer spent maybe 100–200 in flow state; the rest was drudgery that machines should take. He cites David Graeber's "bullshit jobs" for the claim that much replaceable work already was fake.
- Language note: "The language now is English" — natural language as the programming interface.
- Open-weights angle: uses Fireworks-style pay-per-token for open-weight models, but keeps coming back to the Claude subscription as the best value.

## Related Entries
- [[dictionary-of-ai-coding]] ([Dictionary of AI Coding](../tools/dictionary-of-ai-coding.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[claude-code-usage-reset-may-2026]] ([Claude Code Usage Reset](../news/claude-code-usage-reset-may-2026.md))

---
<!-- RU -->

## Краткое описание
Дэвид Хайнемайер Ханссон (DHH), создатель Ruby on Rails, рассказывает о своём переходе в конце 2025 года от скептика AI-кодинга к одному из самых плодовитых агентных инженеров — теперь ИИ пишет 80–100% его кода. В разговоре: почему он отвергает термины «agentic engineering» и «vibe coding», как работа с агентами заменила однопоточное программирование в состоянии потока параллельной оркестрацией, и его «агентная ОС» Omarchy.

## Ключевые идеи
- **От скептика автодополнения к агентному обращению:** год назад DHH принимал чат-ботов как репетиторов, но отвергал автодополнение; агенты «начались как диковинки на пять минут, а потом стали удивительными». Теперь ИИ пишет 80% кода — или 100% для непубличных продуктов.
- **Терминология:** он ненавидит «agentic engineering» («нужно слово столь же простое, как *программирование*») и отвергает «vibe coding» для реальной работы — это «пахнет скрипт-кидди начала 2000-х». Его граница: vibe coding = сказать агенту собрать софт и *не смотреть реализацию*; если ревьюишь код — это agent-accelerated development, то есть всё ещё программирование.
- **Сдвиг состояния потока:** ручной кодинг был однопоточным — глубокое погружение в одну задачу было «порталом в поток». С агентами — параллельная обработка: оркестрация множества агентов требует другого инструментария и другого внимания.
- **Omarchy — агентная ОС:** его Arch-based Linux-дистрибутив поставляется с полным агентским цехом (Neovim, терминал, OBS, Kden Live и его собственный клавиатурный «Cut» для клипов). Часть раннего движения «агентных ОС / податливых компьютеров».
- **Экономика подписок:** он держит *несколько* подписок Claude одновременно, называет подписку «безумно выгодной», жалуется, что подписки не стакаются — и отмечает, что Anthropic отрезала OpenCode от подписок. Следующая версия Omarchy получит multi-sub поддержку.
- **Об отказах:** вспоминает «момент HAL 9000» — Claude отказалась переводить его эссе на итальянский, поскольку не согласна с содержанием.
- **О креативности ИИ:** его собственные творческие моменты ощущаются как next-token prediction «с щепоткой temperature», поэтому он легко верит в творческие прорывы ИИ.

## Заметки по видео
- Аргумент «кто программист»: CEO, нанимающий программистов, не называется программистом — значит и vibe-кодер, не читающий реализацию, тоже. Программирование подразумевает понимание примитивов, а не просто создание программ.
- Защита от рутины: из ~2000 рабочих часов в год программист проводил в потоке 100–200; остальное — рутина для машин. Ссылается на «bullshit jobs» Гребера.
- «Язык теперь — английский» — естественный язык как интерфейс программирования.
- Открытые веса: использует повременную оплату токенов (Fireworks), но возвращается к подписке Claude как лучшей ценности.

## Связанные записи
- [[dictionary-of-ai-coding]] ([Dictionary of AI Coding](../tools/dictionary-of-ai-coding.md))
- [[expensive-model-not-smart-agent]] ([Expensive Model ≠ Smart Agent](../agents/expensive-model-not-smart-agent.md))
- [[opencode]] ([OpenCode](../tools/opencode.md))
- [[claude-code-usage-reset-may-2026]] ([Claude Code Usage Reset](../news/claude-code-usage-reset-may-2026.md))
