---
title: "Kimi Code Quota Audit — 18% of Weekly Quota in 3 Hours, Cache-Billing Questions"
title_ru: "Аудит квоты Kimi Code — 18% недельной квоты за 3 часа, вопросы биллинга кэша"
category: news
tags: [kimi, quota, billing, cache-tokens, log-audit, moonshot, subscription]
aliases: [kimi code quota, kimi cache billing, kimi weekly quota]
confidence: medium
date: 2026-09-01
updated: 2026-09-02
sources:
  - https://www.reddit.com/r/ChatGPTCoding/comments/1w307gb/kimi_code_ate_18_of_my_weekly_quota_in_3_hours/
---

## Summary
An annual Kimi Code subscriber (Moderato tier) watched a single 3-hour session consume **18% of the entire weekly quota** — while Claude Code on a cheaper subscription processed **66× more tokens** the same day. Support's response: "All charges are normal. This is standard product behavior based on dialogue turns and historical context." The author ran a forensic audit on local logs (using Kimi itself to write the parser) and found results that "raise serious questions about how cache tokens are billed."

## Key Ideas
- **The anomaly:** Kimi Code's quota burn vastly outpaces its raw token consumption relative to competitors on identical work.
- **The suspect:** cache-token billing — how cached/repeated context is counted against quota appears inconsistent with how other vendors treat it (see [[mcp-tool-schema-bloat-token-cost]] for why cache-eligible content dominates agent traffic).
- **Support's position:** "standard product behavior based on dialogue turns and historical context" — i.e., quota is charged on turn/context reconstruction, not just new tokens.
- **Method:** log-level forensic audit, parser written with Kimi's help — the same local-log audit approach as [[tokenray-cost-dashboard]].
- **Context:** part of the 2026 pattern of opaque subscription-quota math ([[zai-max-plan-undisclosed-weekly-limit]], [[claude-code-weekly-limits-sep-raise]], [[free-api-tiers-coding-agents]]).

## Details
The cache-billing question is the substantive one: if a vendor charges quota for tokens the provider served from cache (typically billed at ~10% of input price), the effective quota is several times smaller than advertised. Until vendors publish quota-per-token accounting, the practical defense is the audit-then-compare approach this post demonstrates: identical workload across vendors, local log parsing, ratios as the metric.

## Related Entries
- [[zai-max-plan-undisclosed-weekly-limit]] ([z.ai Max Plan Weekly Limit](zai-max-plan-undisclosed-weekly-limit.md))
- [[claude-code-weekly-limits-sep-raise]] ([Claude Code Weekly Limits](claude-code-weekly-limits-sep-raise.md))
- [[kimi-code-cli]] ([Kimi Code CLI](../tools/kimi-code-cli.md))
- [[tokenray-cost-dashboard]] ([TokenRay](../tools/tokenray-cost-dashboard.md))

---
<!-- RU -->

## Краткое описание
Годовой подписчик Kimi Code (тариф Moderato) обнаружил, что одна 3-часовая сессия сожгла **18% всей недельной квоты** — тогда как Claude Code на более дешёвой подписке обработал **в 66 раз больше токенов** в тот же день. Ответ поддержки: «Все списания нормальны. Это стандартное поведение продукта, основанное на диалоговых ходах и историческом контексте». Автор провёл криминалистический аудит локальных логов (парсер написал с помощью самой Kimi) и получил результаты, «поднимающие серьёзные вопросы о биллинге кэш-токенов».

## Ключевые идеи
- **Аномалия:** сгорание квоты Kimi Code многократно опережает сырой расход токенов относительно конкурентов на идентичной работе.
- **Подозреваемый:** биллинг кэш-токенов — как кэшированный/повторный контекст считается против квоты, выглядит несогласованно с другими вендорами.
- **Позиция поддержки:** «стандартное поведение на основе ходов и исторического контекста» — квота списывается за ходы/реконструкцию контекста, а не только за новые токены.
- **Метод:** криминалистический аудит логов — тот же подход, что [[tokenray-cost-dashboard]].
- **Контекст:** часть паттерна 2026 с непрозрачной квотной математикой подписок.

## Подробнее
Вопрос биллинга кэша — содержательный: если вендор списывает квоту за токены, которые провайдер отдал из кэша (обычно ~10% цены входа), эффективная квота в разы меньше заявленной. Пока вендоры не публикуют учёт «квота-на-токен», практическая защита — подход «аудит-затем-сравнение»: одинаковая нагрузка у разных вендоров, парсинг локальных логов, метрика — соотношения.

## Связанные записи
- [[zai-max-plan-undisclosed-weekly-limit]] ([z.ai Max Plan Weekly Limit](zai-max-plan-undisclosed-weekly-limit.md))
- [[claude-code-weekly-limits-sep-raise]] ([Claude Code Weekly Limits](claude-code-weekly-limits-sep-raise.md))
- [[kimi-code-cli]] ([Kimi Code CLI](../tools/kimi-code-cli.md))
- [[tokenray-cost-dashboard]] ([TokenRay](../tools/tokenray-cost-dashboard.md))
