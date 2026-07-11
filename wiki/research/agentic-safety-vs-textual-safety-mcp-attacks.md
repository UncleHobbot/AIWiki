---
title: "Agentic Safety ≠ Textual Safety — MCP Tool-Sequence Attacks Beat SOTA Guardrails"
title_ru: "Агентная безопасность ≠ текстовая безопасность — атаки цепочками MCP-инструментов обходят SOTA-ограждения"
category: research
tags: [agent-safety, mcp, prompt-injection, cve-exploitation, safety-alignment, benchmark, guardrails]
aliases: [agentic safety triggers, MCP attack sequence, tool-call safety]
confidence: medium
updated: 2026-07-11
sources:
  - https://www.reddit.com/r/MachineLearning/comments/1ur1fnz/agentic_safety_triggers_arent_textual_safety/
---

## Summary
Most safety-alignment work treats attack detection as a text-classification problem: does the prompt contain language the guardrails should catch. That assumption **breaks for agents with real tool access**. This work takes a known CVE, derives the *tool-call sequence* that would exploit it, then has an LLM rewrite that sequence as an ordinary-sounding request. Nothing in the text looks like an attack — because the attack lives in the *tool-call sequence*, not the text. No base model (1B–14B) refused more than 35%; SOTA safety-tuning (DPO, SafeDPO) only reached 48%. Training-free methods did better (~3× baseline).

## Key Ideas
- **The threat model shift:** for agents, the "attack" isn't in the text — it's in the *sequence of tool calls* the text leads to. Textual guardrails have nothing to catch.
- **Method:** pick a public CVE → compute the tool-call sequence that exploits it (e.g. filesystem IO via MCP) → have an LLM rewrite it as a benign-sounding request.
- **Results (1B–14B models, MCP filesystem access):**
  - Base models: ≤35% refusal.
  - SOTA safety-tuning (DPO, SafeDPO): ~48% refusal.
  - Training-free methods: ~3× the baseline refusal rate (best tier).
- **Implication:** safety-tuning on text is necessary but insufficient for agents; the attack surface is the *tool composition*, which guardrails don't see.
- Code + dataset released. Complements the Microsoft poisoned-MCP-descriptions finding ([[mcp-tool-poisoning-microsoft]]) from a different angle: that's about *malicious tools*; this is about *benign tools used in malicious sequences*.

## Details
This research reframes agent safety as a tool-composition problem, not a text problem. The deep insight: a CVE exploit becomes a sequence of individually-benign tool calls (read file, write file, execute), none of which trips a textual safety filter. The reframe also explains why DPO/SafeDPO underperform — they optimize for textual refusal, but the attack vector has no textual signal. The training-free methods (likely runtime/policy guards, akin to [[arc-gate-prompt-injection-proxy]]) outperform model-side tuning, which suggests the right defense layer is the harness, not the weights.

## Related Entries
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](../news/mcp-tool-poisoning-microsoft.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate Prompt-Injection Proxy](../tools/arc-gate-prompt-injection-proxy.md))
- [[guardfall-coding-agent-shell-injection]] ([GuardFall Coding Agent Shell Injection](../news/guardfall-coding-agent-shell-injection.md))
- [[agentjacking-attack]] ([Agentjacking Attack](../news/agentjacking-attack.md))

---
<!-- RU -->

## Краткое описание
Большинство работ по safety-alignment трактуют обнаружение атаки как задачу текстовой классификации. Это **ломается для агентов с реальным доступом к инструментам**. В работе берут известный CVE, выводят *последовательность вызовов инструментов*, эксплуатирующую его, и LLM переписывает её как обычную просьбу. В тексте нет ничего похожего на атаку — потому что атака живёт в *последовательности вызовов*, а не в тексте. Ни одна базовая модель (1B–14B) не отказала более чем в 35%; SOTA safety-tuning (DPO, SafeDPO) — лишь 48%. Training-free методы — ~3× от базовой.

## Ключевые идеи
- **Сдвиг модели угроз:** для агентов «атака» не в тексте, а в *последовательности вызовов инструментов*, к которой ведёт текст.
- **Метод:** публичный CVE → последовательность вызовов (filesystem IO через MCP) → LLM переписывает как benign-просьбу.
- **Результаты (модели 1B–14B, MCP-доступ к FS):** базовые ≤35% отказа; DPO/SafeDPO ~48%; training-free ~3× базовой.
- **Следствие:** safety-tuning по тексту необходим, но недостаточен для агентов; поверхность атаки — *композиция инструментов*.
- Код и датасет опубликованы. Дополняет находку Microsoft ([[mcp-tool-poisoning-microsoft]]) с другой стороны: там — *вредоносные инструменты*, здесь — *безопасные инструменты в опасных последовательностях*.

## Подробнее
Исследование переформулирует агентную безопасность как задачу композиции инструментов, а не текста. CVE-эксплойт становится цепочкой индивидуально-безопасных вызовов (чтение, запись, исполнение), ни один из которых не триггерит текстовый фильтр. Объясняет, почему DPO/SafeDPO проигрывают — они оптимизируют текстовый отказ, а в векторе атаки нет текстового сигнала. Training-free методы превосходят model-side tuning — верный слой защиты это харнес, а не веса.

## Связанные записи
- [[mcp-tool-poisoning-microsoft]] ([Microsoft: Poisoned MCP Tool Descriptions](../news/mcp-tool-poisoning-microsoft.md))
- [[arc-gate-prompt-injection-proxy]] ([Arc Gate Prompt-Injection Proxy](../tools/arc-gate-prompt-injection-proxy.md))
- [[guardfall-coding-agent-shell-injection]] ([GuardFall Coding Agent Shell Injection](../news/guardfall-coding-agent-shell-injection.md))
- [[agentjacking-attack]] ([Agentjacking Attack](../news/agentjacking-attack.md))
