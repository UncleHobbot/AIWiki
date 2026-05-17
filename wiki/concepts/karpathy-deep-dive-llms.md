---
title: "Karpathy: Deep Dive into LLMs like ChatGPT"
title_ru: "Карпаты: глубокое погружение в LLM вроде ChatGPT"
category: concepts
tags: [llm, pre-training, rlhf, sft, transformer, karpathy, chatgpt, education]
updated: 2026-05-15
sources:
  - https://www.youtube.com/watch?v=7xTGNNLPyMI
---

## Summary
Andrej Karpathy's comprehensive, general-audience deep dive into how large language models like ChatGPT are built — covering the full training pipeline from internet data collection through pre-training and post-training (RLHF/SFT), along with practical mental models for using LLMs effectively.

## Key Ideas
- **LLMs as probabilistic knowledge stores:** Everything the model "knows" is vague, probabilistic, and statistical — not precise or exact. Things that occur frequently in training data are more reliably remembered.
- **Two-stage training pipeline:** (1) Pre-training on ~10T+ tokens of internet text teaches next-token prediction; (2) Post-training (SFT + RLHF) aligns the base model to follow instructions and be helpful.
- **Base model = "dream internet simulator":** The raw pre-trained model doesn't know how to answer questions — it has absorbed statistical patterns from the internet and will complete any text in the style of what might appear there.
- **Context window beats memory:** When relevant information is in the context window, the model has direct access to it and doesn't need to "recall" from weights — quality improves dramatically. Always paste reference material directly in the prompt rather than relying on model memory.
- **Hallucination is structural, not a bug to patch:** Models hallucinate because they predict probable continuations — they don't have a truth oracle. Check their work; don't trust outputs uncritically.
- **RLHF shapes assistant behavior:** Reinforcement Learning from Human Feedback converts a base model (which just completes text) into a helpful assistant (which follows instructions). Human raters compare outputs and the model is trained toward preferred responses.

## Details
Published February 5, 2025 on the Andrej Karpathy YouTube channel. Runtime: ~3 hours 15 minutes. One of the most-watched technical LLM explainers available.

**Pre-training stage:**
The model is trained on a massive corpus (e.g. FineWeb from Common Crawl) via next-token prediction. At each position in text, the model outputs a probability distribution over ~100k tokens; the loss is how surprised the model was by the actual next token. After billions of iterations across trillions of tokens, the model "compresses" the internet's statistical patterns into its weights. Training frontier models costs millions of dollars and requires thousands of GPUs.

**Tokenization (BPE):** Text is converted to integer token IDs using Byte Pair Encoding before the model ever sees it. A typical vocabulary is ~100k tokens. This means the model "sees" tokens, not characters — which explains some counting/spelling failures.

**Post-training (SFT + RLHF):**
- *SFT (Supervised Fine-Tuning):* Human contractors write ideal question-answer pairs; the model is fine-tuned on these to learn the assistant format.
- *RLHF (Reinforcement Learning from Human Feedback):* Human raters compare two model outputs; a reward model learns to predict human preference; the main model is optimized toward higher reward via RL. Modern variants use AI feedback (RLAIF) to scale this.

**Practical tips from the video:**
- Provide context explicitly in the prompt — pasting the relevant text is better than hoping the model recalls it.
- Use for inspiration and first drafts; verify the output.
- Models can't reliably count or do exact arithmetic — those failures are expected.
- Don't trust models as truth oracles for factual claims without verification.

## Video Notes
- [~0:00] Introduction — goals of the video: mental models for thinking about LLMs
- [~15:00] Pre-training: downloading the internet, data processing
- [~30:00] Tokenization (BPE) — why models struggle with character counting
- [~55:00] Neural network architecture — transformer; attention mechanism
- [~1:40:00] Post-training begins: SFT with human demonstrations
- [~2:10:00] RLHF pipeline — reward model, policy optimization
- [~2:50:00] Practical usage: how to prompt, what to expect, where LLMs fail
- [~3:10:00] Closing: "use them as tools in the toolbox, check their work"

## Notable Quotes
> "The kinds of things that occur often are the kinds of things that are more likely to be remembered in the model." — Andrej Karpathy

> "When it's in the context window the model has direct access to it... doesn't have to recall it." — Andrej Karpathy

> "Use them as tools in the toolbox, check their work and own the product of your work." — Andrej Karpathy

## Related Entries
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[claude-code-prompting-era]] ([The New Prompting Era: Claude 4.7 Literal vs GPT-5.5 Autonomous](../tips/claude-code-prompting-era.md))
- [[self-guided-self-play]] ([Self-Guided Self-Play (SGS) for LLMs](../concepts/self-guided-self-play.md))
- [[agi-impossibility-proof-debunked]] ([Barriers to Complexity-Theoretic Proofs That AGI Is Impossible](../concepts/agi-impossibility-proof-debunked.md))
- [[andrej-karpathy]] ([Andrej Karpathy](../people/andrej-karpathy.md))
- [[llm-fundamentals-tokens-to-production]] ([Critical LLM Knowledge Base for Developers: Tokens to Production AI Agents](../concepts/llm-fundamentals-tokens-to-production.md))
- [[yandex-agents-week-2026-intro]] ([Yandex Agents Week 2026: Intro to AI Agents and LLMs](../concepts/yandex-agents-week-2026-intro.md))

---
<!-- RU -->

## Краткое описание
Полное введение в LLM для широкой аудитории от Андрея Карпатого — весь цикл обучения от сбора интернет-данных через пре-тренировку и пост-тренировку (RLHF/SFT), а также практические модели для эффективного использования LLM.

## Ключевые идеи
- **LLM как вероятностное хранилище знаний:** Всё, что «знает» модель, расплывчато, вероятностно и статистично — не точно. То, что часто встречается в обучающих данных, запоминается надёжнее.
- **Двухэтапный цикл обучения:** (1) Пре-тренировка на 10T+ токенах интернет-текста (предсказание следующего токена); (2) Пост-тренировка (SFT + RLHF) выравнивает базовую модель для следования инструкциям.
- **Базовая модель = "симулятор интернета":** Сырая пре-обученная модель не умеет отвечать на вопросы — она поглотила статистические паттерны интернета и будет продолжать любой текст в стиле того, что могло бы там появиться.
- **Контекстное окно важнее памяти:** Когда релевантная информация находится в контекстном окне, модель имеет к ней прямой доступ — качество резко улучшается. Всегда вставляйте справочный материал прямо в промпт.
- **Галлюцинации структурны, это не баг:** Модели галлюцинируют, потому что предсказывают вероятные продолжения — у них нет оракула истины. Проверяйте выводы.
- **RLHF формирует поведение ассистента:** Reinforcement Learning from Human Feedback превращает базовую модель (завершает текст) в полезного ассистента (следует инструкциям). Эксперты сравнивают варианты ответов, модель обучается в направлении предпочтительных.

## Заметки по видео
- [~0:00] Введение — цели видео: ментальные модели для понимания LLM
- [~15:00] Пре-тренировка: загрузка интернета, обработка данных
- [~30:00] Токенизация (BPE) — почему модели плохо считают символы
- [~55:00] Архитектура — transformer, механизм внимания
- [~1:40:00] Пост-тренировка: SFT с демонстрациями людей
- [~2:10:00] RLHF: модель награды, оптимизация политики
- [~2:50:00] Практическое использование: как писать промпты, чего ожидать
- [~3:10:00] Итог: «используйте как инструменты, проверяйте результат»

## Примечательные цитаты
> «То, что часто встречается, с большей вероятностью запомнится моделью.» — Андрей Карпаты

> «Когда это в контекстном окне, модель имеет к этому прямой доступ... ей не нужно это вспоминать.» — Андрей Карпаты

## Связанные записи
- [[llm-wiki-pattern]] ([LLM Wiki Pattern](../concepts/llm-wiki-pattern.md))
- [[claude-code-prompting-era]] ([The New Prompting Era: Claude 4.7 Literal vs GPT-5.5 Autonomous](../tips/claude-code-prompting-era.md))
- [[self-guided-self-play]] ([Self-Guided Self-Play (SGS) for LLMs](../concepts/self-guided-self-play.md))
- [[agi-impossibility-proof-debunked]] ([Barriers to Complexity-Theoretic Proofs That AGI Is Impossible](../concepts/agi-impossibility-proof-debunked.md))
- [[andrej-karpathy]] ([Andrej Karpathy](../people/andrej-karpathy.md))
- [[llm-fundamentals-tokens-to-production]] ([Critical LLM Knowledge Base for Developers: Tokens to Production AI Agents](../concepts/llm-fundamentals-tokens-to-production.md))
- [[yandex-agents-week-2026-intro]] ([Yandex Agents Week 2026: Intro to AI Agents and LLMs](../concepts/yandex-agents-week-2026-intro.md))
