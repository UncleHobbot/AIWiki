---
title: "Vibe Coding Security Checklist: What AI Skips by Default"
title_ru: "Чек-лист безопасности для vibe coding: что AI пропускает по умолчанию"
category: tips
tags: [vibe-coding, security, appsec, claude-code, code-review]
aliases: [vibe coding appsec checklist]
confidence: low
updated: 2026-06-14
sources:
  - https://www.reddit.com/r/vibecoding/comments/1u5hp7k/vibe_coders_without_a_security_background_how_are/
---

## Summary
An application-security professional who also vibe codes shares a checklist of security gaps that AI coding assistants reliably skip unless explicitly prompted — access control, the "negative path," and money/business logic — and recommends hardening `CLAUDE.md` to catch them by default.

## Key Ideas
- AI models aren't "dumb" about security — they write confident, plausible-looking code, but security simply isn't something they volunteer unless asked.
- **Access control**: AI often writes an "is this yours?" ownership check, but frequently checks the wrong field, allowing one user to load another user's data by changing an ID (classic IDOR/BOLA).
- **The negative path**: AI tests the happy path by default. Hostile/malformed input — the path real attackers use — is rarely handled unless explicitly requested.
- **Money/business logic**: validation of refunds, discounts, and similar financial flows is often missing or superficial, leaving room for abuse.
- The author's mitigation: heavily harden `CLAUDE.md` (or equivalent agent instructions) with these checks baked in, since the gaps are otherwise invisible unless you already know to look for them.

## Details
The post comes from someone working in application security professionally who also relies on AI coding tools personally — giving the observation more weight than a typical "AI writes insecure code" complaint. The core insight is that the failure mode isn't incompetence but omission: models produce code that *looks* secure (an ownership check exists, a refund function validates *something*) but doesn't hold up under adversarial review, because adversarial thinking isn't the model's default frame.

The practical takeaway for anyone vibe coding production or semi-production systems is to treat security checks as part of the explicit spec, not something to review for afterward. Concretely: for every endpoint, ask "can a different user hit this with a different ID and get data that isn't theirs?"; for every input, ask "what happens if this is hostile rather than cooperative?"; and for every monetary operation, ask "does this validation actually constrain the attacker, or just check that a field is present?" Baking these three questions into project-level agent instructions (CLAUDE.md, system prompts, custom rules) is a low-cost way to get the AI to surface these issues proactively rather than only on request.

## Related Entries
- [[vibe-coding-bundling-what-already-exists]] ([Vibe Coding Failure Mode: Bundling What Already Exists](../tips/vibe-coding-bundling-what-already-exists.md))
- [[claude-security-plugin-code-review]] ([Claude Security Plugin: Built-in Vulnerability Review for Agent Code](../news/claude-security-plugin-code-review.md))

---
<!-- RU -->

## Краткое описание
Специалист по application security, который также занимается vibe coding, делится чек-листом из пробелов безопасности, которые AI-coding-ассистенты систематически пропускают без явного запроса — контроль доступа, "негативный путь" и денежная/бизнес-логика — и рекомендует усилить `CLAUDE.md`, чтобы ловить их по умолчанию.

## Ключевые идеи
- AI-модели не "глупые" в вопросах безопасности — они пишут уверенный, правдоподобный код, но безопасность просто не входит в то, что модель предлагает сама, если её не попросить.
- **Контроль доступа**: AI часто пишет проверку "это твоё?", но нередко проверяет неправильное поле, что позволяет одному пользователю получить данные другого, просто изменив ID (классический IDOR/BOLA).
- **Негативный путь**: AI по умолчанию тестирует только "счастливый путь". Враждебный или некорректный ввод — путь, которым пользуются настоящие атакующие — обрабатывается редко, если не указано явно.
- **Денежная/бизнес-логика**: проверка возвратов, скидок и аналогичных финансовых операций часто отсутствует или поверхностна, оставляя возможность для злоупотреблений.
- Решение автора: серьёзно усилить `CLAUDE.md` (или аналогичные инструкции агенту), встроив эти проверки по умолчанию, поскольку без этого пробелы невидимы, если не знать, где искать.

## Подробнее
Пост написан человеком, который профессионально занимается application security и при этом сам активно использует AI-coding-инструменты — это придаёт наблюдению больше веса, чем типичной жалобе "AI пишет небезопасный код". Главная мысль в том, что проблема не в некомпетентности, а в упущении: модели выдают код, который *выглядит* безопасным (проверка владения есть, функция возврата средств что-то проверяет), но не выдерживает враждебного анализа, потому что враждебное мышление не является базовой рамкой модели.

Практический вывод для тех, кто занимается vibe coding production или полу-production систем: относиться к проверкам безопасности как к части явной спецификации, а не как к тому, что проверяется потом. Конкретно: для каждого эндпоинта спрашивать "может ли другой пользователь обратиться сюда с другим ID и получить чужие данные?"; для каждого ввода — "что произойдёт, если он враждебный, а не дружелюбный?"; для каждой денежной операции — "эта проверка реально ограничивает атакующего, или просто проверяет, что поле заполнено?". Встраивание этих трёх вопросов в проектные инструкции агента (CLAUDE.md, системные промпты, кастомные правила) — дешёвый способ заставить AI поднимать эти проблемы проактивно, а не только по запросу.

## Связанные записи
- [[vibe-coding-bundling-what-already-exists]] ([Vibe Coding Failure Mode: Bundling What Already Exists](../tips/vibe-coding-bundling-what-already-exists.md))
- [[claude-security-plugin-code-review]] ([Claude Security Plugin: Built-in Vulnerability Review for Agent Code](../news/claude-security-plugin-code-review.md))
