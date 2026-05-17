---
title: "Agentic AI Development with GitHub Copilot: Lessons Learned"
title_ru: "Агентная разработка с GitHub Copilot: уроки из практики"
category: tips
tags: [github-copilot, agentic-ai, tdd, cli, open-source, lessons-learned, junior-developer-analogy]
updated: 2026-05-16
sources:
  - https://www.youtube.com/watch?v=Y5xXDA4tQlk
---

## Summary
A practitioner's account of real-world agentic AI-assisted development using GitHub Copilot CLI on an open-source Rust project, distilling five concrete lessons about where the tool helps, where it over-reaches, and how to stay in control.

## Key Ideas
- **Treat the AI like an eager junior developer:** It never gets tired, will run as long as you want, and follows instructions diligently — but needs oversight, not blind trust. You are still the senior engineer making architectural calls.
- **TDD becomes even more critical:** Asking AI to write tests AND implementation in one pass produces tests that pass but don't test the right thing. The correct workflow: ask AI to write the test only → verify it fails yourself → then ask AI to implement the code that makes it pass.
- **Be a seasoned developer to evaluate AI suggestions:** AI will find real issues (deprecated APIs, legitimate refactors) but also spurious "improvements" that add complexity without real value. You need domain knowledge to tell them apart.
- **Control your commits:** AI tools will happily commit broken or off-direction code. Disable auto-commit and treat each commit as a developer decision, not a Copilot action.
- **Develop locally for tight feedback loops:** The local CLI workflow beats the cloud-based "assign issue to Copilot" workflow for most tasks. Local lets you switch between AI and manual edits, revert changes instantly, and run your own tests. Cloud is clunky when you need small iterative corrections.
- **Run multiple sessions in parallel:** Each analysis session can take 5+ minutes. For independent tasks, start them in parallel to recover the wait time.

## Video Notes
- [0:00] Speaker intro — using Copilot CLI on "mei" (a Rust CLI tool for tracking files/directories) as worked example
- [~5:00] Demo: `copilot "identify five ways I can improve the codebase"` — Copilot autonomously runs `cat`, `ls`, reads Rust files, thinks aloud, then outputs 5 suggestions
- [~8:00] Key lesson: one suggestion (caching a git-ignore object) is technically correct but pointless — the function is only ever called once per invocation. A naive developer blindly acting on it adds complexity for zero gain
- [~10:00] Another suggestion (deprecated `std::env::home_dir`) is more valid — but still requires external verification before acting
- [~14:00] TDD lesson illustrated: asked Copilot to "build a test for Zoxide backwards compatibility" — Copilot misinterpreted and built the test AND the implementation, then ran `cargo test` autonomously, then debugged failures — all unsolicited. Burned tokens and went off in wrong direction
- [~20:00] Auto-commit disabled deliberately — Copilot will commit for you by default, including broken code
- [~22:00] Cloud vs. local comparison: assigning a GitHub issue to Copilot is useful for simple discrete tasks (adding an alias command), but for subtle bugs requiring iterative back-and-forth, it becomes tedious — you end up checking out the PR locally anyway
- [~28:00] Parallel sessions tip: since analysis runs take minutes, start multiple sessions on different tasks simultaneously
- Tool use is the key differentiator of agentic AI: `cat`, `cargo test`, `clippy` run autonomously — the AI self-steers based on actual output, not prompts alone

## Details
The video is grounded in a real open-source project (Rust, ~30 minutes runtime) and avoids hype. The central tension is that agentic AI development requires you to have *less* need to do routine work but *more* need for senior judgment — the AI amplifies both good and bad decisions.

The TDD lesson is particularly counterintuitive: you might expect AI to be better at writing tests, but when it writes tests alongside implementation, it satisfies the stated goal (passing tests) without guaranteeing the tests are meaningful. Splitting the request — test first, implementation second — preserves the TDD invariant and gives you a checkpoint to verify the test's correctness before the implementation obscures it.

## Related Entries
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[github-copilot-cli-best-practices]] ([GitHub Copilot CLI: Best Practices and Workflows](../tips/github-copilot-cli-best-practices.md))
- [[test-driven-agentic-behaviours]] ([Test-Driven Agentic Behaviours](../tips/test-driven-agentic-behaviours.md))

---
<!-- RU -->

## Краткое описание
Практический разбор агентной AI-разработки с GitHub Copilot CLI на реальном open-source проекте на Rust: пять конкретных уроков о том, где инструмент помогает, где выходит за рамки и как сохранить контроль.

## Ключевые идеи
- **Воспринимайте AI как старательного джуниора:** Он никогда не устаёт, будет работать столько, сколько нужно, и добросовестно выполняет инструкции — но требует надзора, а не слепого доверия. Вы по-прежнему остаётесь старшим разработчиком, принимающим архитектурные решения.
- **TDD становится ещё важнее:** Если попросить AI написать тесты И реализацию за один проход — он напишет тесты, которые проходят, но проверяют не то, что нужно. Правильный workflow: попросить AI написать только тест → самостоятельно убедиться, что он падает → попросить AI реализовать код, который делает тест проходящим.
- **Нужно быть опытным разработчиком, чтобы оценивать советы AI:** Инструмент найдёт реальные проблемы (устаревшие API, обоснованные рефакторинги), но также и мнимые «улучшения», добавляющие сложность без реальной ценности. Чтобы их различить, нужны предметные знания.
- **Контролируйте коммиты:** AI-инструменты охотно закоммитят сломанный или «уехавший» код. Отключите авто-коммит и воспринимайте каждый коммит как решение разработчика, а не действие Copilot.
- **Разрабатывайте локально для быстрой обратной связи:** Локальный CLI-workflow превосходит облачный («назначить задачу Copilot») для большинства задач. Локально можно мгновенно переключаться между AI и ручной правкой, откатывать изменения и запускать собственные тесты. Облако неудобно при необходимости мелких итеративных корректировок.
- **Запускайте несколько сессий параллельно:** Каждая аналитическая сессия может занимать 5+ минут. Для независимых задач запускайте их параллельно, чтобы не терять время.

## Заметки по видео
- [0:00] Введение — автор использует Copilot CLI на проекте «mei» (CLI-инструмент на Rust для отслеживания файлов и директорий)
- [~5:00] Демо: `copilot "identify five ways I can improve the codebase"` — Copilot автономно запускает `cat`, `ls`, читает Rust-файлы, «думает вслух» и выдаёт 5 предложений
- [~8:00] Ключевой урок: одно предложение (кэшировать git-ignore объект) технически верно, но бессмысленно — функция вызывается лишь раз за запуск. Слепое следование добавляет сложность без выигрыша
- [~14:00] Урок про TDD: автор попросил «написать тест для совместимости с Zoxide» — Copilot неверно понял и написал тест И реализацию, затем автономно запустил `cargo test` и начал отлаживать ошибки — всё это не было запрошено
- [~20:00] Авто-коммит намеренно отключён — по умолчанию Copilot коммитит сам, включая сломанный код
- [~22:00] Сравнение облака и локального режима: назначение задачи Copilot через GitHub Issues удобно для простых дискретных задач, но для сложных итеративных багов оказывается громоздким
- [~28:00] Совет о параллельных сессиях: поскольку анализ занимает минуты, запускайте несколько сессий одновременно на разных задачах
- Использование внешних инструментов — ключевое отличие агентного AI: `cat`, `cargo test`, `clippy` запускаются автономно

## Подробнее
Видео основано на реальном open-source проекте и избегает хайпа. Центральное противоречие: агентная AI-разработка требует меньше рутинного труда, но больше экспертных решений — AI усиливает как хорошие, так и плохие решения.

Урок про TDD особенно контринтуитивен: когда AI пишет тесты вместе с реализацией, он достигает заявленной цели (проходящие тесты), не гарантируя их содержательности. Разделение запроса — тест отдельно, реализация отдельно — сохраняет инвариант TDD и даёт точку проверки до того, как реализация «замутит воду».

## Связанные записи
- [[github-copilot-cli]] ([GitHub Copilot CLI](../tools/github-copilot-cli.md))
- [[github-copilot-cli-best-practices]] ([GitHub Copilot CLI: Best Practices and Workflows](../tips/github-copilot-cli-best-practices.md))
- [[test-driven-agentic-behaviours]] ([Test-Driven Agentic Behaviours](../tips/test-driven-agentic-behaviours.md))
