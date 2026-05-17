---
title: "The New Prompting Era: Claude 4.7 Literal vs GPT-5.5 Autonomous"
title_ru: "Новая эра промптинга: Claude 4.7 буквален, GPT-5.5 автономен"
category: tips
tags: [prompting, claude-opus, gpt-5, prompt-engineering, llm-behavior]
updated: 2026-05-15
sources:
  - https://x.com/alex_prompter/status/2049596193282375831
---

## Summary
Claude Opus 4.7 became significantly more literal — it does exactly what you type, no guessing — while GPT-5.5 became more autonomous, punishing over-specified prompts. Both changes mean the prompt writer is now the bottleneck, not the model.

## Key Ideas
- **Claude Opus 4.7 changed:** It stopped compensating for vague instructions. Vague prompts that worked on 4.6 now produce narrow, literal, sometimes worse results — not because the model regressed, but because it no longer fills in blanks.
- **GPT-5.5 changed the opposite way:** OpenAI's official guide says "don't carry over instructions from older prompt stacks." Legacy prompts that over-specified process now create noise and produce mechanical output.
- **Two philosophies, one conclusion:** Anthropic says be surgically specific; OpenAI says use "outcome-first prompting" (describe success criteria, get out of the way). Both punish prompts written without clear thinking.
- **The prompting skill is now the gap:** One developer on Reddit found that precise prompts got reliably better results on 4.7, vague prompts reliably worse — tracking almost perfectly with the complaints in the community.
- **Even Boris Cherny adjusted:** The engineer who built Claude Code said on launch day that even he needed a few days to recalibrate his prompting approach (that post got 936 likes).
- **Token cost penalizes lazy prompting:** Anthropic increased rate limits partly because the new tokenizer uses up to 35% more tokens on the same input. Precise prompts are cheaper to run than vague ones.

## Details
Anthropic's framework for Claude Opus 4.7: be surgically specific about what you want, because the model won't fill in your blanks. It takes instructions at face value.

OpenAI's framework for GPT-5.5 ("outcome-first prompting"): describe what good looks like, define success criteria, set constraints — then get out of the way. The model picks the path.

The practical implication: **the 2 minutes of structured thinking before typing** is now where results diverge. Both model families converge in capability; the gap between good and bad output now tracks almost entirely with prompt quality, not model choice.

For Claude Code specifically, this means: explicit task scoping, clear success criteria, and well-structured CLAUDE.md files matter more than ever. The model no longer compensates for ambiguous instructions by making charitable assumptions.

## Notable Quotes
> "The models are converging in capability. The gap between good and bad output is no longer about which model you pick. It's about the 2 minutes of structured thinking you do before you type anything." — @alex_prompter

> "Claude got more literal. GPT got more autonomous. Both now punish the same thing: prompts written without clear thinking behind them."

## Related Entries
- [[llm-wiki-setup-guide]] ([LLM Wiki: Practical Setup Guide](../tips/llm-wiki-setup-guide.md))
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide to the Top 36](../tips/claude-code-plugins-guide.md))

---
<!-- RU -->

## Краткое описание
Claude Opus 4.7 стал значительно буквальнее — выполняет ровно то, что написано, без угадывания — тогда как GPT-5.5 стал более автономным, наказывая за избыточную детализацию промптов. Оба изменения означают, что узким местом теперь является автор промпта, а не модель.

## Ключевые идеи
- **Claude Opus 4.7 изменился:** Он перестал компенсировать расплывчатые инструкции. Нечёткие промпты, работавшие на 4.6, теперь дают узкие, буквальные, порой худшие результаты — не потому что модель деградировала, а потому что она больше не додумывает.
- **GPT-5.5 изменился в противоположную сторону:** Официальное руководство OpenAI гласит: «не переносите инструкции из старых стеков промптов». Устаревшие промпты с избыточной детализацией процесса теперь создают шум и дают механические результаты.
- **Две философии, один вывод:** Anthropic советует быть хирургически точными; OpenAI продвигает «outcome-first prompting» (описывайте критерии успеха, уходите в сторону). Оба подхода наказывают за промпты, написанные без чёткого мышления.
- **Навык написания промптов — теперь узкое место:** Один разработчик на Reddit обнаружил, что точные промпты стабильно дают лучшие результаты на 4.7, а расплывчатые — стабильно хуже.
- **Токенные затраты наказывают за небрежность:** Новый токенизатор Anthropic использует до 35% больше токенов на тот же ввод. Точные промпты дешевле в запуске, чем расплывчатые.

## Подробнее
Фреймворк Anthropic для Claude Opus 4.7: будьте хирургически точны в том, что хотите, потому что модель не будет додумывать. Она принимает инструкции буквально.

Фреймворк OpenAI для GPT-5.5 («outcome-first prompting»): опишите, как выглядит хороший результат, определите критерии успеха, задайте ограничения — затем отойдите в сторону.

Практический вывод: **2 минуты структурированного мышления перед тем, как что-то напечатать** — вот где теперь расходятся результаты. Обе модели сближаются по возможностям; разрыв между хорошим и плохим выводом теперь почти полностью определяется качеством промпта, а не выбором модели.

## Примечательные цитаты
> «Модели сближаются по возможностям. Разрыв между хорошим и плохим результатом больше не в том, какую модель выбрать. Это 2 минуты структурированного мышления до того, как напечатать что-либо.» — @alex_prompter

## Связанные записи
- [[llm-wiki-setup-guide]] ([LLM Wiki: Practical Setup Guide](../tips/llm-wiki-setup-guide.md))
- [[claude-code-plugins-guide]] ([Claude Code Plugins: Curated Guide to the Top 36](../tips/claude-code-plugins-guide.md))
