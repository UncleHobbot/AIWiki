---
title: "US Export-Control Order Suspends Anthropic's Fable 5 and Mythos 5 Worldwide"
title_ru: "Экспортный контроль США приостанавливает доступ к Fable 5 и Mythos 5 Anthropic по всему миру"
category: news
tags: [anthropic, claude, fable, mythos, export-control, ai-policy, ai-safety, government]
aliases: [Fable 5 ban, Mythos 5 suspension, AI export ban]
confidence: low
date: 2026-06-13
updated: 2026-07-01
sources:
  - https://www.christianfindlay.com/blog/ai-export-ban
  - https://www.reddit.com/r/singularity/comments/1u55r4m/the_us_government_switched_off_anthropics_most/
  - https://www.reddit.com/r/singularity/comments/1u54qco/anthropics_fablemythos_suspension_they_plan_to/
  - https://www.reddit.com/r/singularity/comments/1u4y3kc/david_sacks_explains_the_sequence_of_events/
  - https://www.reddit.com/r/singularity/comments/1u4wrxb/amazon_ceos_talks_with_us_officials_triggered/
  - https://x.com/DavidSacks/status/2065853007619588171
  - https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html
---

## Summary
Within ~72 hours of Anthropic's public launch of Claude Fable 5 / Mythos 5, the US government issued an export-control-based order suspending access to both models for all customers worldwide. Reporting traces the trigger to discussions between Amazon's CEO and Trump administration officials over the cyber-capability risks of the "Mythos" class models that Fable 5 is built on.

## Key Ideas
- Fable 5 and Mythos 5 were both disabled for every customer globally within roughly 72 hours of launch, following a federal directive citing export-control authority.
- Reporting (via a blog post syndicated to r/singularity, and commentary attributed to David Sacks) claims Amazon CEO Andy Jassy held talks with senior US officials about security risks in Anthropic's most advanced models, and that this was a catalyst for the crackdown.
- The framing in "Fable is Mythos with guardrails" — Fable 5 is the public, safeguarded commercial release of the same underlying model as Mythos 5 (vetted-access-only, safeguards lifted for cybersecurity research). If Fable's guardrails were considered insufficient, that exposes the more capable Mythos capabilities to the same restriction.
- The triggering "threat" example cited was the model's ability to read a codebase and fix bugs autonomously — a capability also present in GPT-5.5, raising questions about why this specific model was singled out.
- Commentators note this sets a precedent: a government can retroactively suspend a lawful, days-old commercial AI product worldwide, with no apparent appeal process, drawing comparisons to earlier chip export-control fights (where demand simply shifted to alternative suppliers, e.g., China).
- Anthropic said it would "share more details" within 24 hours of the suspension; community discussion (r/singularity) was split between treating this as a serious AI-safety/export-control story and treating it as politically charged speculation.

## Details
This event follows directly from the earlier Fable 5 "silent nerfing" controversy (see [[claude-fable-5-ai-research-restrictions]]) and the Fable 5 / Mythos 5 dual release itself (see [[claude-fable-5-mythos-5-release]]). Mythos 5 was released as the safeguard-lifted variant of the same underlying model, restricted to vetted cybersecurity partners (cf. Project Glasswing). Fable 5 is the public-facing commercial product with cyber safeguards applied.

According to the linked reporting, the suspension was driven by an export-control directive from US officials, reportedly catalyzed by conversations between Amazon's CEO and the administration about the risk that Mythos-class capabilities (autonomous codebase analysis and bug-fixing, with associated cyber-offense potential as documented in the AISI cyber-capability findings — see [[mythos-aisi-cyber-capability-2026]]) could proliferate if Fable 5's guardrails were bypassed.

Multiple r/singularity threads from the same window discuss this from different angles: a "what's the actual play here" thread speculating about whether Anthropic would build US-only verification infrastructure or fight the order publicly; a thread relaying David Sacks' account of the sequence of events; and a thread specifically attributing the catalyst to Amazon CEO Andy Jassy's conversations with officials. As with all rapidly-developing political/regulatory stories sourced primarily from social media and a single blog writeup, this should be treated as a developing story (confidence: low) pending official statements from Anthropic and US government sources — but the underlying premise (worldwide suspension of a just-launched frontier model via export-control authority) appears to be corroborated across multiple independent posts in the same time window.

## Resolution (July 1, 2026) — Export Controls Lifted, Fable 5 Restored

The U.S. lifted the jailbreak-linked export controls, and Anthropic restored Claude Fable 5 to customers. The suspension therefore proved temporary — the export-control mechanism was used as a short-term brake rather than a permanent ban, though it still set the precedent noted above. See also [[gpt-5-6-sol-preview]] for how OpenAI is now staging frontier cyber-capable models (restricted access by design) in the wake of this episode.

## Related Entries
- [[claude-fable-5-mythos-5-release]] ([Claude Fable 5 / Mythos 5 Dual Release](claude-fable-5-mythos-5-release.md))
- [[claude-fable-5-ai-research-restrictions]] ([Claude Fable 5 AI Research Restrictions](claude-fable-5-ai-research-restrictions.md))
- [[mythos-aisi-cyber-capability-2026]] ([Mythos Cyber Capability: 20-Hour Network Attacks](mythos-aisi-cyber-capability-2026.md))
- [[project-glasswing-anthropic-vulnerability-discovery]] ([Project Glasswing](project-glasswing-anthropic-vulnerability-discovery.md))
- [[gpt-5-6-sol-preview]] ([GPT-5.6 Sol Preview](gpt-5-6-sol-preview.md))

---
<!-- RU -->

## Краткое описание
В течение ~72 часов после публичного запуска Claude Fable 5 / Mythos 5 правительство США издало распоряжение на основе экспортного контроля, приостановившее доступ к обеим моделям для всех клиентов по всему миру. По сообщениям, причиной стали переговоры между CEO Amazon и представителями администрации Трампа об угрозах кибербезопасности, связанных с моделями класса «Mythos», на которых построен Fable 5.

## Ключевые идеи
- Fable 5 и Mythos 5 были отключены для всех клиентов по всему миру в течение примерно 72 часов после запуска, в результате федерального распоряжения, ссылающегося на полномочия экспортного контроля.
- По сообщениям (блог-пост, распространённый через r/singularity, и комментарии, приписываемые Дэвиду Саксу), CEO Amazon Энди Джасси провёл переговоры с высокопоставленными чиновниками США о рисках безопасности самых продвинутых моделей Anthropic, и это стало катализатором ограничительных мер.
- Формулировка «Fable — это Mythos с защитными механизмами»: Fable 5 — это публичный коммерческий релиз с защитой той же базовой модели, что и Mythos 5 (доступ только для проверенных партнёров, защита снята для исследований кибербезопасности). Если защитные механизмы Fable считались недостаточными, это подвергает риску те же возможности Mythos.
- В качестве «угрозы», вызвавшей реакцию, приводится способность модели автономно читать кодовую базу и исправлять ошибки — возможность, присутствующая и в GPT-5.5, что вызывает вопросы, почему именно эта модель оказалась под прицелом.
- Комментаторы отмечают, что это создаёт прецедент: государство может ретроактивно приостановить законный, всего несколько дней как выпущенный коммерческий AI-продукт по всему миру без видимого процесса апелляции — проводятся параллели с более ранними спорами по экспортному контролю чипов (где спрос просто переместился к альтернативным поставщикам, например, в Китай).
- Anthropic заявила, что «поделится подробностями» в течение 24 часов после приостановки; обсуждение в сообществе (r/singularity) разделилось между восприятием этого как серьёзной истории о AI-safety/экспортном контроле и как политически окрашенных спекуляций.

## Подробнее
Это событие напрямую следует за более ранним скандалом с «незаметным урезанием» Fable 5 (см. [[claude-fable-5-ai-research-restrictions]]) и самим релизом Fable 5 / Mythos 5 (см. [[claude-fable-5-mythos-5-release]]). Mythos 5 был выпущен как вариант той же базовой модели со снятой защитой, доступный только проверенным партнёрам по кибербезопасности (см. Project Glasswing). Fable 5 — публичный коммерческий продукт с применёнными кибер-защитными механизмами.

Согласно приведённым источникам, приостановка была вызвана распоряжением американских властей на основе экспортного контроля, по сообщениям — катализированным переговорами CEO Amazon с администрацией об угрозе того, что возможности класса Mythos (автономный анализ кодовой базы и исправление ошибок, с соответствующим потенциалом для кибератак, как документировано в результатах AISI по киберспособностям — см. [[mythos-aisi-cyber-capability-2026]]) могут распространиться, если защитные механизмы Fable 5 будут преодолены.

Несколько тредов r/singularity того же периода обсуждают это с разных сторон: тред «в чём реальный план» со спекуляциями о том, построит ли Anthropic инфраструктуру верификации только для США или будет публично оспаривать решение; тред, пересказывающий версию событий от Дэвида Сакса; и тред, конкретно связывающий катализатор с переговорами CEO Amazon Энди Джасси с чиновниками. Как и для всех быстро развивающихся политических/регуляторных историй, основанных в первую очередь на соцсетях и одном блог-посте, это следует считать развивающейся историей (confidence: low) до официальных заявлений Anthropic и властей США — но базовая предпосылка (приостановка только что запущенной frontier-модели по всему миру через экспортный контроль) подтверждается несколькими независимыми постами в один и тот же период времени.

## Развязка (1 июля 2026) — экспортный контроль снят, Fable 5 восстановлен

США сняли экспортный контроль, привязанный к jailbreak, и Anthropic восстановила Claude Fable 5 для клиентов. Приостановка оказалась временной — механизм экспортного контроля сработал как краткосрочный тормоз, а не постоянный запрет, хотя прецедент (см. выше) сохраняется. См. также [[gpt-5-6-sol-preview]] — как OpenAI теперь staging'ует frontier киберспособные модели (ограниченный доступ by design) по следам этого эпизода.

## Связанные записи
- [[claude-fable-5-mythos-5-release]] ([Claude Fable 5 / Mythos 5 Dual Release](claude-fable-5-mythos-5-release.md))
- [[claude-fable-5-ai-research-restrictions]] ([Claude Fable 5 AI Research Restrictions](claude-fable-5-ai-research-restrictions.md))
- [[mythos-aisi-cyber-capability-2026]] ([Mythos Cyber Capability: 20-Hour Network Attacks](mythos-aisi-cyber-capability-2026.md))
- [[project-glasswing-anthropic-vulnerability-discovery]] ([Project Glasswing](project-glasswing-anthropic-vulnerability-discovery.md))
- [[gpt-5-6-sol-preview]] ([GPT-5.6 Sol Preview](gpt-5-6-sol-preview.md))
