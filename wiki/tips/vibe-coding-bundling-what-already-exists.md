---
title: "Vibe Coding Failure Mode: Bundling What Already Exists"
title_ru: "Паттерн провала вайб-кодинга: включение в проект того, что уже существует"
category: tips
tags: [vibe-coding, code-review, llm-mistakes, android, fonts, bloat, junior-dev, ai-agents]
aliases: [vibe coding font bundling, AI bundles system files, LLM unnecessary dependencies]
confidence: high
date: 2026-05-19
updated: 2026-05-19
sources:
  - https://www.reddit.com/r/vibecoding/comments/1tfxxx/pr_rejected_vibe_coding_just_cost_a_junior_dev/
---

## Summary

A viral r/vibecoding post (362 pts, 220 comments) captures a recurring failure pattern: AI-assisted code bundles resources that already exist in the target environment — in this case, Roboto font files in an Android app, where Roboto is the OS default and costs 500KB of unnecessary APK weight.

## Key Ideas

- **LLMs don't know what's already there.** When an AI writes code to load a font, it adds the file. It has no model of what's already installed in the target runtime, OS, or framework.
- **The root cause is LLM statelesness.** The model has no persistent knowledge of the deployment environment; it generates self-contained solutions by default.
- **The failure mode generalises.** Not just fonts: common patterns include bundling certificates already in the trust store, shipping polyfills for features the target browser supports natively, copying utility code from a library already in the dependency tree.
- **The senior engineer's role shifts.** Rather than writing code, the senior's job becomes "deleting what the AI added that didn't need to exist." This is the new code review skill.
- **Human panic reinforces the problem.** In the story, the junior developer panicked when asked to remove the files — "The code will break!" — because they had no mental model of where the font actually came from.

## Details

The post describes a junior developer using AI assistance to build a PDF generator for an Android app. To get formatting right, the AI bundled `Roboto-Regular.ttf` and `Roboto-Bold.ttf` directly into the source code. The senior engineer rejected the PR, deleted the font assets, and changed the load path to the system font location — with no breakage.

The story resonated widely because it captures something structural about how LLMs generate code: they produce self-contained artifacts. A model generating font-loading code will include the font file because that's how you ship font-loading code as a standalone module. The model has no way to know it is running inside Android, whose OS already ships Roboto as a system font.

**Generalised checklist for AI-generated code review:**

- Does it ship a certificate that the OS trust store already has?
- Does it bundle a polyfill for a feature the min-SDK/browser-target supports natively?
- Does it copy a utility function from a library that's already in `package.json`?
- Does it vendor a font that's a system default on the target platform?
- Does it include a compiled binary that the runtime already provides?

## Notable Quotes

> "He panicked. 'I can't remove it! The code will break! We need those files!' I walked over to his desk, deleted the font assets, and changed his load function to point to the native path." — r/vibecoding OP

## Related Entries

- [[spec-driven-development-bmad]] ([Spec-Driven Development](../tips/spec-driven-development-bmad.md))
- [[matt-pocock-aihero]] ([Matt Pocock: AI Hero and Claude Code Skills Author](../people/matt-pocock-aihero.md))

---
<!-- RU -->

## Краткое описание

Вирусный пост на r/vibecoding (362 балла, 220 комментариев) фиксирует повторяющийся паттерн провала: AI-ассистированный код включает ресурсы, которые уже существуют в целевой среде — в данном случае файлы шрифта Roboto в Android-приложении, где Roboto является шрифтом по умолчанию ОС и создаёт 500 КБ ненужного веса APK.

## Ключевые идеи

- **LLM не знает, что уже есть.** Когда ИИ пишет код для загрузки шрифта, он добавляет файл. У него нет модели того, что уже установлено в целевой среде выполнения, ОС или фреймворке.
- **Причина — отсутствие состояния у LLM.** Модель не имеет постоянного знания о среде развёртывания; по умолчанию она генерирует самодостаточные решения.
- **Паттерн сбоя обобщается:** не только шрифты — также сертификаты (уже в хранилище доверия), полифиллы (для уже поддерживаемых функций), утилитарный код (из уже подключённой библиотеки).
- **Роль опытного разработчика смещается.** Вместо написания кода задача старшего — «удалять то, что добавил ИИ, но чего не должно было существовать».
- **Паника джуниора усугубляет проблему.** В истории джуниор запаниковал при просьбе убрать файлы — «Код сломается!» — потому что у него не было ментальной модели происхождения шрифта.

## Подробнее

Пост описывает джуниора, использующего AI-ассистента для создания PDF-генератора в Android-приложении. ИИ включил `Roboto-Regular.ttf` и `Roboto-Bold.ttf` прямо в исходный код. Опытный разработчик отклонил PR, удалил файлы шрифтов и изменил путь загрузки на системный — без каких-либо поломок.

**Обобщённый чеклист для ревью AI-сгенерированного кода:**
- Включает ли он сертификат, который уже есть в хранилище доверия ОС?
- Добавляет ли полифилл для функции, уже поддерживаемой целевой платформой?
- Копирует ли утилитарную функцию из библиотеки, уже есть в зависимостях?
- Поставляет ли шрифт, являющийся системным по умолчанию на целевой платформе?

## Примечательные цитаты

> «Он запаниковал. "Я не могу убрать это! Код сломается! Нам нужны эти файлы!" Я подошёл к его столу, удалил файлы шрифтов и изменил функцию загрузки на системный путь.» — автор поста на r/vibecoding

## Связанные записи

- [[spec-driven-development-bmad]] ([Spec-Driven Development](../tips/spec-driven-development-bmad.md))
- [[matt-pocock-aihero]] ([Matt Pocock: AI Hero and Claude Code Skills Author](../people/matt-pocock-aihero.md))
