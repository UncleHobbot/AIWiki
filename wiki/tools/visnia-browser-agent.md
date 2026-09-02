---
title: "Visnia Browser Agent — Self-Hosted Browser Automation Benchmark Leader"
title_ru: "Visnia Browser Agent — самохостный агент автоматизации браузера"
category: tools
tags: [browser-agent, playwright, ocr, benchmark, self-hosted, typescript, mit]
aliases: [visnia, visnia browser agent, browser automation agent]
confidence: medium
updated: 2026-09-01
sources:
  - https://github.com/visnia-ai/browser-agent
---

## Summary
Visnia is an open-source (MIT) TypeScript browser-automation agent with a CLI and TypeScript/Python SDKs, built on Playwright with bundled OCR (Tesseract). Its self-reported benchmarks show it beating both a commercial framework (Browser-code) and the hosted Browser Use product on success rate and cost-efficiency for real web-app tasks.

## Key Ideas
- **Stack:** Playwright-driven; OCR via bundled Tesseract traineddata; `npm install @visnia/browser-agent-sdk`.
- **Self-reported results (all runs on gpt-5.6-luna xhigh):**
  - BrowserUse Bench success: **88%** vs Browser-code 78% vs Browser Use 31%.
  - Cost per full run: **$5.37** vs $8.34 (Browser-code) vs $6.31 (Browser Cloud v4).
  - Efficiency: **16.4 successful tasks per dollar** vs 9.35 / 12.37.
  - BrowseWebApp Bench: 76% vs 64%, at roughly half the cost ($3.73 vs $7.45).
- **Caveat:** these are the project's own benchmarks (Tier 3/vendor) — methodology not independently verified; treat as a strong signal, not a settled ranking.
- Fits the local/stealth browsing stack pattern alongside [[local-agentic-web-research-stack]] and [[cloakbrowser-stealth-chromium]].

## Details
The interesting claim is cost-efficiency rather than raw success rate: a self-hosted agent doing more successful tasks per dollar than a hosted product would flip the "hosted browser-agents are easier" assumption. Note: an earlier community mention framed this repo as containing a GLM-5.3-Flash vs GPT-5.6-Luna comparison — the README actually runs everything on gpt-5.6-luna; the GLM comparison lives in a separate r/ZaiGLM post.

## Related Entries
- [[local-agentic-web-research-stack]] ([Local Agentic Web Research Stack](../tips/local-agentic-web-research-stack.md))
- [[cloakbrowser-stealth-chromium]] ([CloakBrowser](cloakbrowser-stealth-chromium.md))
- [[ui-tars-desktop-multimodal-agent]] ([UI-TARS Desktop](../agents/ui-tars-desktop-multimodal-agent.md))

---
<!-- RU -->

## Краткое описание
Visnia — открытый (MIT) браузерный агент автоматизации на TypeScript с CLI и SDK (TypeScript/Python), построен на Playwright с встроенным OCR (Tesseract). Собственные бенчмарки показывают превосходство над коммерческим фреймворком (Browser-code) и хостед-продуктом Browser Use по успешности и экономической эффективности.

## Ключевые идеи
- **Стек:** Playwright; OCR через Tesseract; установка `npm install @visnia/browser-agent-sdk`.
- **Заявленные результаты (все на gpt-5.6-luna xhigh):**
  - Успех BrowserUse Bench: **88%** против 78% (Browser-code) и 31% (Browser Use).
  - Стоимость полного прогона: **$5.37** против $8.34 / $6.31.
  - Эффективность: **16.4 успешных задач на доллар** против 9.35 / 12.37.
  - BrowseWebApp Bench: 76% против 64% примерно вдвое дешевле.
- **Оговорка:** бенчмарки собственные (уровень 3) — методология независимо не верифицирована.

## Подробнее
Интересна именно экономическая эффективность: самохостный агент, выполняющий больше успешных задач на доллар, чем хостед-продукт, переворачивает предположение «хостед браузерные агенты проще». Примечание: более раннее упоминание в сообществе приписывало репо сравнение GLM-5.3-Flash vs GPT-5.6-Luna — на деле README гоняет всё на gpt-5.6-luna; сравнение GLM живёт в отдельном посте r/ZaiGLM.

## Связанные записи
- [[local-agentic-web-research-stack]] ([Local Agentic Web Research Stack](../tips/local-agentic-web-research-stack.md))
- [[cloakbrowser-stealth-chromium]] ([CloakBrowser](cloakbrowser-stealth-chromium.md))
- [[ui-tars-desktop-multimodal-agent]] ([UI-TARS Desktop](../agents/ui-tars-desktop-multimodal-agent.md))
