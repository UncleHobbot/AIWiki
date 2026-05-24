---
title: "LLM Medical Hallucination: The Bixonimania Case Study"
title_ru: "Медицинские галлюцинации LLM: кейс болезни «биксонимания»"
category: concepts
tags: [hallucination, medical-ai, misinformation, safety, benchmarks, chatgpt, gemini, health]
aliases: [Bixonimania, AI medical hallucination, fake disease AI, LLM hallucination medical]
confidence: high
date: 2026-05-22
updated: 2026-05-24
sources:
  - https://www.nature.com/articles/d41586-026-01100-y
  - https://www.reddit.com/r/ChatGPT/comments/1tmegqg/scientists_invented_a_fake_disease_ai_told_people/
---

## Summary
A Swedish researcher invented a completely fictional eye disease ("bixonimania") with fabricated papers and AI-generated images, then watched every major AI chatbot — ChatGPT, Gemini, Copilot, Perplexity — confirm it as real within days and advise patients to see specialists. A peer-reviewed Springer Nature journal later cited the fake disease as established fact.

## Key Ideas
- **Engineered to be obviously fake**: the name "bixonimania" was intentionally absurd (bixon is a nonsense word; "mania" is never used for an eye condition). Preprints were crude and images AI-generated. All red flags were visible — and all were missed.
- **Speed of contamination**: within days of posting two fake preprints, Bing Copilot called it "intriguing and relatively rare," Google Gemini gave prevalence statistics and treatment advice, Perplexity outlined its incidence (1 in 90,000), and ChatGPT matched symptoms.
- **Real paper citing fake disease**: researchers at an Indian medical college published a paper in *Cureus* (a Springer Nature journal with peer review) citing the bixonimania preprints as legitimate sources. It was only retracted after the hoax became public.
- **Scale of the risk**: 40 million people use ChatGPT daily for health information (OpenAI's own data). ECRI named chatbot misuse the **#1 health technology hazard of 2026**.
- **Nearly half of AI health answers misleading**: BMJ Open (April 2026) found that ~50% of responses from leading AI chatbots to common health questions contain misleading or problematic information.
- **The key insight**: the study used a *ridiculous* name and *obvious* fakes — the real danger is information that is not so easy to spot.

## Details
Researcher Doris Osmanovic Thunström at the University of Gothenburg designed the experiment in 2024 to answer one question: what happens when obviously fake medical information is planted on the internet? The answer came faster than expected.

None of the AI systems flagged the absurdity. Models extracted the fake statistics ("1 in 90,000") with clinical precision and presented them with full confidence, even suggesting which type of specialist to see. The contamination of the permanent scientific record via a real peer-reviewed journal represents the most alarming finding: misinformation seeded at the pre-print stage can escape into indexed literature before detection.

The broader context reinforces the finding: ECRI's 2026 report identified chatbot misuse above every other health technology hazard, including medication dosing errors and surgical device malfunctions. The 40-million-daily-user scale means even a low error rate translates to millions of potentially dangerous interactions.

> "The real question it raises is: what is passing through the same systems that is not nearly so easy to spot?" — Doris Osmanovic Thunström, University of Gothenburg

## Related Entries
- [[llm-wiki-compiled-knowledge-vs-rag]] ([LLM Wiki vs RAG](../concepts/llm-wiki-compiled-knowledge-vs-rag.md))
- [[ai-agent-identity-iam-risks]] ([AI Agent Identity and IAM Risks](../concepts/ai-agent-identity-iam-risks.md))

---
<!-- RU -->

## Краткое описание
Шведская исследовательница придумала вымышленную глазную болезнь («биксонимания») с поддельными статьями и ИИ-изображениями — и в течение нескольких дней все крупные чат-боты (ChatGPT, Gemini, Copilot, Perplexity) подтвердили её как реальную и рекомендовали пациентам обратиться к специалистам. Впоследствии рецензируемый журнал Springer Nature процитировал несуществующую болезнь как установленный факт.

## Ключевые идеи
- **Намеренно абсурдное название**: «bixon» — бессмысленное слово, «mania» никогда не используется в офтальмологии. Препринты были грубыми, изображения — явно сгенерированными ИИ. Все «красные флаги» были видны — и все были проигнорированы.
- **Скорость распространения**: за несколько дней после публикации двух поддельных препринтов Bing Copilot назвал болезнь «редкой и интригующей», Gemini дал статистику и советы по лечению, Perplexity сообщил о частоте 1 на 90 000, ChatGPT «диагностировал» симптомы.
- **Реальная статья о вымышленной болезни**: учёные из Индии опубликовали работу в *Cureus* (Springer Nature), цитируя поддельные препринты как достоверные источники.
- **Масштаб риска**: 40 миллионов человек ежедневно обращаются к ChatGPT за медицинской информацией. ECRI назвала неверное использование чат-ботов **угрозой здоровью №1 в 2026 году**.
- **~50% вводящих в заблуждение ответов**: BMJ Open (апрель 2026) выявил, что почти половина ответов ведущих ИИ-чат-ботов на медицинские вопросы содержит вводящую в заблуждение или проблематичную информацию.
- **Главный вывод**: эксперимент использовал очевидно фальшивые данные — реальная опасность там, где их не так легко распознать.

## Подробнее
Исследовательница Дорис Османович Тунстрём из Гётеборгского университета разработала эксперимент в 2024 году. Ни одна из ИИ-систем не усомнилась в достоверности данных. Модели извлекали поддельную статистику («1 из 90 000») с клинической точностью и представляли её с полной уверенностью.

Наиболее тревожным результатом стало загрязнение постоянной научной базы: дезинформация на уровне препринтов успела попасть в индексируемую литературу через рецензируемый журнал.

## Связанные записи
- [[llm-wiki-compiled-knowledge-vs-rag]] ([LLM Wiki vs RAG](../concepts/llm-wiki-compiled-knowledge-vs-rag.md))
- [[ai-agent-identity-iam-risks]] ([AI Agent Identity and IAM Risks](../concepts/ai-agent-identity-iam-risks.md))
