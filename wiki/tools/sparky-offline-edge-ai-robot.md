---
title: "Sparky: Fully Offline Edge AI Robot"
title_ru: "Sparky: полностью офлайн-робот на базе ИИ"
category: tools
tags: [edge-ai, jetson, local-llm, robotics, llama-cpp, gemma, offline]
aliases: [Sparky robot, Jetson Orin AI robot, offline AI companion]
confidence: medium
updated: 2026-05-18
sources:
  - https://www.reddit.com/r/LocalLLaMA/comments/1tebfni/built_a_fully_offline_suitcase_robot_around_a/
  - https://www.tomshardware.com/
---

## Summary

Sparky is a fully offline AI companion robot built inside a suitcase, powered by an NVIDIA Jetson Orin NX Super 16GB and running Gemma 4 E4B via llama.cpp. With 30+ integrated sensors and ~200ms cached TTFT, it demonstrates that real-time conversational AI is achievable entirely on edge hardware, with zero cloud dependency.

## Key Ideas

- **Hardware**: NVIDIA Jetson Orin NX Super 16GB — a single-board embedded AI computer designed for robotics and edge inference.
- **Model**: Gemma 4 E4B (4-bit quantized) running via llama.cpp — small enough to fit in unified memory, good enough for natural conversation.
- **Latency**: ~200ms cached Time to First Token — achieves near-conversational responsiveness without any network round-trips.
- **Sensor fusion**: 30+ sensors (environmental, proximity, motion, etc.) inject live context into every prompt, giving the model situational awareness.
- **Fully air-gapped**: no WiFi, no Bluetooth, no cellular — operates indefinitely offline; no API keys, no subscription, no cloud costs after purchase.
- **Covered by Tom's Hardware** as a notable demonstration of consumer-accessible edge AI for robotics.

## Details

Sparky shows the practical ceiling of current edge AI for embodied agents. The Jetson Orin NX Super (16GB unified memory) is enough to run a capable 4-bit quantized model at conversation speed. The builder designed the system around the constraint that every sensor reading feeds into the LLM's context, making the robot aware of its physical environment without separate perception pipelines.

The project is notable for what it *doesn't* use: no cloud inference, no internet, no external API. This makes it relevant for privacy-sensitive deployments, unstable-network environments, and cost-sensitive applications where per-token API fees would be prohibitive at scale.

The 200ms TTFT figure is for cached prompts (shared system-level context re-used across turns). Cold first-token latency would be higher, but for ongoing conversation the cached figure is what matters.

## Related Entries

- [[orthrus-qwen3-acceleration]] ([Orthrus: Hybrid Diffusion+AR Speedup for Qwen3](./orthrus-qwen3-acceleration.md))
- [[dynamic-compute-budget-local-llm]] ([Dynamic Compute Budget for Local LLMs](../tips/dynamic-compute-budget-local-llm.md))

---
<!-- RU -->

## Краткое описание

Sparky — полностью автономный ИИ-робот-компаньон в чемодане, построенный на NVIDIA Jetson Orin NX Super 16GB с моделью Gemma 4 E4B через llama.cpp. Имея более 30 датчиков и задержку ~200 мс, он доказывает, что разговорный ИИ в реальном времени возможен без какого-либо облака.

## Ключевые идеи

- **Железо**: NVIDIA Jetson Orin NX Super 16GB — одноплатный embedded AI-компьютер для робототехники и инференса на устройстве.
- **Модель**: Gemma 4 E4B (4-битное квантование) через llama.cpp — достаточно маленькая для размещения в унифицированной памяти и достаточно умная для разговора.
- **Задержка**: ~200 мс кэшированного TTFT (время до первого токена) — близко к разговорной скорости без сетевых запросов.
- **Слияние данных с датчиков**: 30+ датчиков (окружение, близость, движение и др.) добавляют живой контекст в каждый промпт.
- **Полностью изолирован**: нет Wi-Fi, Bluetooth, мобильной связи — работает бесконечно без интернета, API-ключей и подписок.
- **Освещён Tom's Hardware** как заметная демонстрация доступного edge AI для робототехники.

## Подробнее

Sparky показывает практический потолок современного edge AI для воплощённых агентов. Jetson Orin NX Super (16 ГБ унифицированной памяти) достаточно для запуска 4-битно квантованной модели на разговорной скорости. Архитектура позволяет каждому показанию датчика попадать в контекст LLM, давая роботу ситуационную осведомлённость без отдельных перцептивных пайплайнов.

## Связанные записи

- [[orthrus-qwen3-acceleration]] ([Orthrus: Hybrid Diffusion+AR Speedup for Qwen3](./orthrus-qwen3-acceleration.md))
- [[dynamic-compute-budget-local-llm]] ([Dynamic Compute Budget for Local LLMs](../tips/dynamic-compute-budget-local-llm.md))
