---
title: "Free API Tiers for Coding Agents — Half of Them Now Want a Card"
title_ru: "Бесплатные API-тиры для кодинг-агентов — половина теперь требует карту"
category: research
tags: [free-tier, api, groq, cerebras, github-models, aider, cline, benchmark]
aliases: [free api tiers, free llm api benchmark, coding agent free tier]
confidence: medium
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/ChatGPTCoding/comments/1w34m6p/benchmarked_the_free_api_tiers_you_can_point_a/
---

## Summary
A practitioner benchmark (aider + Cline run against free tiers) found that roughly **half of the commonly recommended free LLM API tiers no longer work without payment**: DeepSeek → 402 Insufficient Balance, SambaNova → 402 PAYMENT_METHOD_REQUIRED, Together → read-only until deposit, Cerebras and xAI → card required before anything runs, GitHub Models → 410 (retired July 30). The remaining truly-free-no-card tiers were measured with identical prompts (500-token cap, temp 0.3, one streaming request each) from a US GitHub Actions runner.

## Key Ideas
- **The "free tier guide rot" problem:** setup guides written earlier in 2026 point at options that have since evaporated — the free-API landscape shifts monthly.
- **Confirmed dead/dying for cardless use:** DeepSeek, SambaNova, Together, Cerebras, xAI, GitHub Models (retired Jul 30).
- **Methodology:** same prompt, 500-token cap, temp 0.3, single streaming request, US runner to control for distance; throughput from each API's own usage token counts.
- **Relevance:** free tiers matter for the "agent on a budget" pattern ([[cli-proxy-api]], [[9router-free-ai-coding]]) and for anyone testing harnesses before committing to a subscription.
- Practical lesson: don't build a workflow on a free tier without a fallback provider — model IDs disappear under you (the author's setup broke twice in one month).

## Details
The broader signal: the free-API era is closing as providers monetize agent workloads. What remains cardless (Groq and a few others per the post) is now the scarce resource, and any guide older than a quarter is unreliable. For wiki purposes this is a snapshot with a short shelf life — dated deliberately.

## Related Entries
- [[cli-proxy-api]] ([CLIProxyAPI](cli-proxy-api.md))
- [[9router-free-ai-coding]] ([9router](9router-free-ai-coding.md))
- [[kimi-code-quota-audit]] ([Kimi Code Quota Audit](../news/kimi-code-quota-audit.md))

---
<!-- RU -->

## Краткое описание
Бенчмарк практика (aider + Cline против бесплатных тиров) показал, что примерно **половина обычно рекомендуемых бесплатных LLM API-тиров больше не работает без оплаты**: DeepSeek → 402, SambaNova → нужна карта, Together → read-only до депозита, Cerebras и xAI → карта до любых запросов, GitHub Models → 410 (закрыт 30 июля). Оставшиеся действительно-бесплатные-без-карты тиры измерены одинаковыми промптами (500 токенов, temp 0.3, один streaming-запрос) с US GitHub Actions-раннера.

## Ключевые идеи
- **Проблема «гниения гайдов»:** инструкции начала 2026 указывают на уже исчезнувшие опции — ландшафт бесплатных API меняется ежемесячно.
- **Мертвы/умирают для cardless-использования:** DeepSeek, SambaNova, Together, Cerebras, xAI, GitHub Models.
- **Методология:** одинаковый промпт, лимит 500 токенов, temp 0.3, один запрос, US-раннер; throughput из собственных счётчиков API.
- **Значимость:** бесплатные тиры важны для паттерна «агент на бюджете» и для тестирования харнесов до покупки подписки.
- **Урок:** не стройте воркфлоу на бесплатном тире без запасного провайдера — ID моделей исчезают (сетап автора ломался дважды за месяц).

## Подробнее
Общий сигнал: эра бесплатных API закрывается по мере монетизации агентных нагрузок. Оставшиеся cardless-опции — дефицитный ресурс, а любой гайд старше квартала ненадёжен. Это снимок с коротким сроком годности — специально датирован.

## Связанные записи
- [[cli-proxy-api]] ([CLIProxyAPI](cli-proxy-api.md))
- [[9router-free-ai-coding]] ([9router](9router-free-ai-coding.md))
- [[kimi-code-quota-audit]] ([Kimi Code Quota Audit](../news/kimi-code-quota-audit.md))
