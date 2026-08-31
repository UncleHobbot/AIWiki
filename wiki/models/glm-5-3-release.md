---
title: "GLM-5.3: Post-Training Only, 50% Coding Gain and Emergent Cyber Capability"
title_ru: "GLM-5.3: только пост-обучение, +50% в кодинге и эмерджентные кибервозможности"
category: models
tags: [glm, zai, open-weights, moe, post-training, coding, cybersecurity, terminal-bench, reasoning-effort, agentic]
aliases: [GLM 5.3, GLM-5.3, zai-org/GLM-5.3, GLM 5.3 flash]
confidence: high
date: 2026-08-31
updated: 2026-08-31
sources:
  - https://huggingface.co/zai-org/GLM-5.3
  - https://www.reddit.com/r/ZaiGLM/comments/1w0u5un/
---

## Summary
GLM-5.3 is Z.ai's open-weights 753B MoE-DSA release that keeps GLM-5.2's base model entirely unchanged — every gain comes from post-training, including a 50% coding improvement on Z.ai's internal benchmark and a more than doubling of exploitation-benchmark scores.

## Key Ideas
- **Same base model, post-training only**: an unusually clean demonstration that substantial capability gains remain available from post-training alone, with no pretraining run. 753B parameters, MoE-DSA architecture, BF16/F8_E4M3/F32 tensor types.
- **50% coding improvement over GLM-5.2** on Z.ai's in-house Code Bench, plus stated SOTA on Terminal Bench 3.0 (28.3) and Agents' Last Exam.
- **Emergent cyber capability**: vulnerability discovery described as emergent, with exploitation-benchmark scores "more than double" GLM-5.2 — ExploitGym (6h) 130, CyberGym 84.5.
- **`reasoning_effort` parameter**: inference is controllable across low / high / max, defaulting to `max`. This mirrors the effort-control pattern now appearing across frontier models.
- **Context**: 300K tokens for evaluation, with 1M available on specific benchmarks.
- **Config gotcha**: the chat template defaults `clear_thinking` to **false** — you must explicitly enable it for conversational use, or reasoning traces leak into responses.

## Details

### The Post-Training-Only Result
The most interesting claim is methodological. GLM-5.3 shares GLM-5.2's base model exactly; the delta is post-training. A 50% coding gain and a doubling of exploitation performance from post-training alone suggests the field is still far from extracting everything a given pretrained base can do — relevant to anyone weighing the cost of a fresh pretraining run against further post-training investment.

### Cyber Capability in an Open-Weights Model
The emergent vulnerability-discovery capability deserves attention because GLM-5.3 ships with **open weights**. Anthropic (Mythos/Glasswing) and OpenAI (Daybreak) gate comparable capability behind verified access tiers and account-level controls. An open-weights model scoring 130 on ExploitGym and 84.5 on CyberGym has no such gate — the capability is downloadable. This is the sharpest instance yet of the open-weights/frontier-safety tension in cyber specifically.

### Practical Notes
Community benchmarking on r/ZaiGLM compared GLM 5.3 Flash against GPT 5.6 Luna on browsing tasks, with GLM 5.3 Flash reported as competitive. Note that Z.ai's headline coding figure comes from an in-house benchmark, so treat the 50% as vendor-reported rather than independently verified; the Terminal Bench 3.0 number is externally comparable.

## Related Entries
- [[glm-5-2-release]] ([GLM-5.2 Release](../models/glm-5-2-release.md))
- [[product-zai-glm]] ([Z.ai GLM](../models/product-zai-glm.md))
- [[qwen-3-8-flash-next]] ([Qwen 3.8 Flash Next](../models/qwen-3-8-flash-next.md))
- [[openai-daybreak-cyber-defense]] ([OpenAI Daybreak: Frontier AI for Cyber Defense](../news/openai-daybreak-cyber-defense.md))
- [[mythos-aisi-cyber-capability-2026]] ([Mythos AISI Cyber Capability](../news/mythos-aisi-cyber-capability-2026.md))

---
<!-- RU -->

## Краткое описание
GLM-5.3 — открытый релиз Z.ai на 753B параметров с архитектурой MoE-DSA, полностью сохраняющий базовую модель GLM-5.2: все улучшения получены только за счёт пост-обучения, включая рост на 50% в кодинге по внутреннему бенчмарку и более чем двукратный рост на бенчмарках эксплуатации уязвимостей.

## Ключевые идеи
- **Та же базовая модель, только пост-обучение**: необычно чистая демонстрация того, что существенный прирост возможностей всё ещё доступен за счёт одного лишь пост-обучения, без нового прогона предобучения.
- **+50% в кодинге относительно GLM-5.2** по внутреннему Code Bench, плюс заявленный SOTA на Terminal Bench 3.0 (28.3) и Agents' Last Exam.
- **Эмерджентные кибервозможности**: обнаружение уязвимостей описано как эмерджентное, показатели на бенчмарках эксплуатации «более чем вдвое» выше GLM-5.2 — ExploitGym (6ч) 130, CyberGym 84.5.
- **Параметр `reasoning_effort`**: инференс управляется на уровнях low / high / max, по умолчанию `max`.
- **Контекст**: 300K токенов для оценки, 1M на отдельных бенчмарках.
- **Подводный камень конфигурации**: в шаблоне чата `clear_thinking` по умолчанию **false** — для диалогового использования его нужно включать явно, иначе следы рассуждений попадают в ответы.

## Подробнее

**Результат «только пост-обучение».** Самое интересное заявление — методологическое. GLM-5.3 использует ту же базовую модель, что и GLM-5.2; вся разница в пост-обучении. Прирост 50% в кодинге и удвоение показателей эксплуатации только за счёт пост-обучения говорят о том, что отрасль всё ещё далека от извлечения всего, на что способна данная предобученная база.

**Кибервозможности в модели с открытыми весами.** Эмерджентная способность к поиску уязвимостей заслуживает внимания, потому что GLM-5.3 поставляется с **открытыми весами**. Anthropic (Mythos/Glasswing) и OpenAI (Daybreak) ограничивают сопоставимые возможности верифицированными уровнями доступа и контролем на уровне аккаунта. У модели с открытыми весами такого барьера нет — возможность просто скачивается.

**Практические заметки.** Заявленный показатель по кодингу получен на внутреннем бенчмарке Z.ai, поэтому 50% следует считать заявлением вендора, а не независимо подтверждённым результатом; цифра Terminal Bench 3.0 сопоставима внешне.

## Связанные записи
- [[glm-5-2-release]] ([Релиз GLM-5.2](../models/glm-5-2-release.md))
- [[product-zai-glm]] ([Z.ai GLM](../models/product-zai-glm.md))
- [[qwen-3-8-flash-next]] ([Qwen 3.8 Flash Next](../models/qwen-3-8-flash-next.md))
- [[openai-daybreak-cyber-defense]] ([OpenAI Daybreak](../news/openai-daybreak-cyber-defense.md))
- [[mythos-aisi-cyber-capability-2026]] ([Mythos AISI Cyber Capability](../news/mythos-aisi-cyber-capability-2026.md))
