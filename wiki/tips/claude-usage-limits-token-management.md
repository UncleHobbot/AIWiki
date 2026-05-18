---
title: "10 Ways to Stop Hitting Claude's Usage Limits"
title_ru: "10 способов перестать упираться в лимиты Claude"
category: tips
tags: [claude, usage-limits, token-management, context-management, claude-pro, workflow, prompting]
aliases: [Claude usage limits, Claude token limits, stop hitting Claude limits, Claude rate limits]
confidence: medium
updated: 2026-05-18
sources:
  - https://x.com/0x_kaize/status/2038286026284667239
  - https://support.claude.ai/en/articles/11647753-how-do-usage-and-length-limits-work
---

## Summary
Claude counts tokens, not messages. Most users hit usage limits because they unknowingly burn tokens on repeated context loads, correction messages, and redundant document uploads. Ten targeted workflow changes can dramatically extend usable session time without upgrading plans.

## Key Ideas
- **Edit, don't correct**: sending a follow-up "No, I meant..." adds that message to history and forces Claude to re-read the entire thread — burning tokens on context that did not help. Click the pencil icon to rewrite your original prompt instead.
- **Merge prompts**: three separate prompts = three full context loads; one prompt with three tasks = one context load. Combining related questions always saves tokens.
- **Use Projects for recurring docs**: uploading the same PDF to multiple chats re-tokenizes it each time. Upload once to a Project and every conversation inside it references the cached version at no extra token cost.
- **Start fresh every 15–20 messages**: long threads compound token cost quadratically — a 100-message chat at ~500 tokens each burns over 2.5 million tokens mostly on re-reading old history. Summarize, copy, open new chat, paste as first message.
- **The 5-hour rolling window**: Claude uses a rolling 5-hour window, not midnight resets. Spacing usage into 2–3 sessions per day recycles earlier usage before the next session starts.

## Details

### The 10 Practices

**1. Rewrite, don't follow up**
When Claude misses your intent, click Edit on the original message, rewrite it, and regenerate. The bad exchange is replaced rather than stacked. Every correction message you avoid is a full context re-read you skip.

**2. Start new chats regularly**
Begin a new conversation every 15–20 messages. Ask Claude to summarize the key points first, copy the summary, open a new chat, paste as the opening message. Context cost grows as S × N(N+1)/2 — it compounds fast.

**3. Merge your prompts**
Batch related questions into one message. Three separate prompts = three context loads. One prompt with three tasks = one context load. The multi-task prompt also gets better results because Claude sees all constraints simultaneously.

**4. Use Projects to cache documents**
Instead of re-uploading a recurring PDF or spec to every new chat, add it once to a Claude Project. Every conversation inside that Project references the cached file. The token cost is paid once, not on every conversation.

**5. Set default User Memory**
Go to Settings → Memory. Add persistent context about your role, writing style, output preferences, and recurring constraints. Claude applies this automatically to every new chat — no re-explaining at the start of each session.

**6. Turn off unused features**
Web Search, Connectors, and Explore mode add tokens to every response even when you do not need them. Disable "Search and Tools" when you are writing, coding, or working from your own documents.

**7. Route easy tasks to smaller models**
Not every task needs Claude Sonnet or Opus. Simple rewrites, formatting, and classification work well with Haiku. Routing appropriately extends your Sonnet/Opus quota for tasks that actually need it.

**8. Use the 5-hour rolling window**
Claude resets usage on a rolling 5-hour basis, not at midnight. If you hit a limit at 9 AM, capacity begins freeing up at 2 PM. Structuring work into two or three sessions spaced 4–5 hours apart ensures earlier usage has expired by the next session.

**9. Avoid peak hours for heavy tasks**
As of March 2026, Anthropic applies tighter throttling during peak usage hours (weekday mornings, approximately 8 AM–2 PM Eastern). Scheduling resource-intensive work for evenings or weekends stretches the same plan further.

**10. Avoid Extended Thinking for routine tasks**
The Extended Thinking (Advanced Reasoning) feature consumes significantly more tokens per response. Reserve it for genuinely hard problems — architecture decisions, debugging complex failures, multi-step reasoning — and turn it off for everyday questions.

### The Underlying Principle

Claude charges tokens on everything in the context window at every turn, not just the new message. A long conversation where every turn includes the full history is the single biggest source of unexpected limit hits. The practices above all reduce how much history Claude re-reads per turn.

## Notable Quotes
> "Claude doesn't count the number of messages — it counts tokens. Not everyone knows how to use them wisely." — @0x_kaize

## Related Entries
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[claude-code-12-setup-tricks]] ([12 Claude Code Setup Tricks](../tips/claude-code-12-setup-tricks.md))
- [[context-engineering-ai-agents-pipeline]] ([Context Engineering for AI Agent Pipelines](../tips/context-engineering-ai-agents-pipeline.md))

---
<!-- RU -->

## Краткое описание
Claude считает токены, а не сообщения. Большинство пользователей упирается в лимиты из-за повторных загрузок контекста, сообщений-поправок и дублирования документов. Десять изменений в рабочем процессе могут значительно увеличить доступное время сессии без смены тарифа.

## Ключевые идеи
- **Редактируй, не поправляй**: отправка «Нет, я имел в виду...» добавляет сообщение в историю и заставляет Claude перечитывать весь тред — сжигая токены на контекст, который не помог. Нажми на карандаш и перепиши исходный промпт.
- **Объединяй промпты**: три отдельных промпта = три полных загрузки контекста; один промпт с тремя задачами = одна загрузка контекста. Группировка вопросов всегда экономит токены.
- **Используй Projects для постоянных документов**: загрузка одного и того же PDF в разные чаты токенизирует его каждый раз. Загрузи один раз в Project — все беседы внутри него ссылаются на кеш.
- **Начинай новый чат каждые 15–20 сообщений**: длинные треды дают квадратичный рост стоимости. Попроси Claude подвести итог, скопируй, открой новый чат, вставь как первое сообщение.
- **Скользящее окно 5 часов**: Claude использует скользящее пятичасовое окно, а не сброс в полночь. Разбивка дня на 2–3 сессии с интервалом позволяет использованию «протухнуть» до следующей.

## Подробнее

### 10 практик

**1. Переписывай, не поправляй**
Если Claude понял неверно, нажми Edit на исходном сообщении, перепиши и пересгенерируй. Неудачный обмен заменяется, а не складывается поверх.

**2. Начинай новые чаты регулярно**
Новый чат каждые 15–20 сообщений. Попроси Claude резюмировать ключевые моменты, скопируй, открой новый чат, вставь как первое сообщение. Стоимость растёт по формуле S × N(N+1)/2 — очень быстро.

**3. Объединяй промпты**
Группируй связанные вопросы в одно сообщение. Три отдельных промпта = три загрузки контекста. Один промпт с тремя задачами = одна загрузка. Результаты тоже лучше: Claude видит все ограничения сразу.

**4. Используй Projects для кеширования документов**
Вместо повторной загрузки одного PDF в каждый новый чат добавь его один раз в Claude Project. Все беседы внутри проекта ссылаются на кешированный файл. Токенная стоимость платится один раз.

**5. Настрой постоянную User Memory**
Настройки → Memory. Добавь контекст о своей роли, стиле письма, предпочтениях к выводу, постоянных ограничениях. Claude применяет это автоматически в каждом новом чате — не нужно объяснять заново.

**6. Отключи неиспользуемые функции**
Web Search, Connectors и режим Explore добавляют токены в каждый ответ, даже если они не нужны. Отключай «Search and Tools», когда пишешь, кодишь или работаешь со своими документами.

**7. Маршрутизируй простые задачи на меньшие модели**
Не каждая задача требует Sonnet или Opus. Простые переписывания, форматирование и классификация хорошо работают с Haiku. Разумная маршрутизация сохраняет квоту Sonnet/Opus для задач, которым она действительно нужна.

**8. Используй скользящее окно 5 часов**
Claude сбрасывает использование по скользящим 5 часам, а не в полночь. Если упёрся в лимит в 9:00 — к 14:00 начинает освобождаться. Структурируй работу в две-три сессии с интервалом 4–5 часов.

**9. Избегай пиковых часов для тяжёлых задач**
С марта 2026 Anthropic применяет более жёсткое ограничение в часы пик (будние утра, примерно 8:00–14:00 по EST). Тяжёлые задачи вечером или в выходные дни растягивают тот же тариф.

**10. Отключай Extended Thinking для рутинных задач**
Функция Extended Thinking (расширенное рассуждение) потребляет значительно больше токенов на ответ. Оставь её для по-настоящему сложных проблем — архитектурных решений, сложной отладки, многошаговых рассуждений.

### Главный принцип

Claude тратит токены на всё в окне контекста при каждом ходу, а не только на новое сообщение. Длинная беседа, где каждый ход включает полную историю — главный источник неожиданных лимитов. Все практики выше сводятся к одному: сократить, сколько истории Claude перечитывает на каждом ходу.

## Примечательные цитаты
> «Claude не считает количество сообщений — он считает токены. Не все знают, как использовать их разумно.» — @0x_kaize

## Связанные записи
- [[claude-code-workflows-best-practices]] ([Claude Code Workflows and Best Practices](../tips/claude-code-workflows-best-practices.md))
- [[claude-code-12-setup-tricks]] ([12 Claude Code Setup Tricks](../tips/claude-code-12-setup-tricks.md))
- [[context-engineering-ai-agents-pipeline]] ([Context Engineering for AI Agent Pipelines](../tips/context-engineering-ai-agents-pipeline.md))
