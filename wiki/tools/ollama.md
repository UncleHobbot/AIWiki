---
title: "Ollama"
title_ru: "Ollama"
category: tools
tags: [ollama, local-llm, inference, open-source]
aliases: [Ollama, ollama CLI]
confidence: high
updated: 2026-06-14
sources:
  - https://ollama.com/
  - https://github.com/ollama/ollama
---

## Summary

Ollama is an open-source tool for running large language models locally. It bundles model weights, configuration, and a chat template into a single managed package, exposing a simple CLI (`ollama run`, `ollama pull`) and a local REST API for integration with agents and apps.

## Key Ideas

- Run open-weight models (Llama, Gemma, Qwen, DeepSeek, Mistral, and more) on consumer hardware with one command — no Python environment or manual weight downloads required.
- Each model is packaged as a "Modelfile" artifact that bundles weights, a chat template, generation parameters, and system prompt, making versions reproducible.
- Ships a local HTTP API (default `localhost:11434`) compatible with many agent frameworks, so apps can talk to Ollama as if it were an OpenAI-style endpoint.
- Supports quantization (GGUF, QAT) and accelerator backends (CUDA, Metal/Apple Silicon) so models fit in available VRAM and run efficiently.
- Recent versions add speculative-decoding / Multi-Token Prediction (MTP) support, though speedups are highly hardware-dependent.

## Details

Ollama's appeal is simplicity: `ollama run llama3.1` pulls a quantized model and drops you into a chat REPL. The same binary serves an API that tools and coding agents connect to for fully offline inference, which matters for privacy, cost, and latency-sensitive workflows.

Because it manages the full model lifecycle (download, versioning, prompt template, context window), Ollama has become the default local-inference layer for community agents and self-hosted setups. Its quantization support lets large models run on a single GPU or even CPU-only machines at usable speeds. Advanced features like MTP can roughly double throughput on fast CUDA cards but can regress on unified-memory architectures like Apple Silicon — always benchmark on real hardware before assuming a speedup.

## Related Entries

- [[opencoderag-rag-plugin]] ([OpenCodeRAG RAG Plugin](opencoderag-rag-plugin.md))
- [[mtp-hardware-dependent-speedup]] ([MTP Hardware-Dependent Speedup](../tips/mtp-hardware-dependent-speedup.md))
- [[small-models-clean-architecture]] ([Small Models, Clean Architecture](../tips/small-models-clean-architecture.md))

---
<!-- RU -->

## Краткое описание

Ollama — инструмент с открытым исходным кодом для локального запуска больших языковых моделей. Он упаковывает веса модели, конфигурацию и chat-шаблон в единый управляемый артефакт, предоставляя простой CLI (`ollama run`, `ollama pull`) и локальный REST API для интеграции с агентами и приложениями.

## Ключевые идеи

- Запуск моделей с открытыми весами (Llama, Gemma, Qwen, DeepSeek, Mistral и др.) на потребительском оборудовании одной командой — без Python-окружения и ручной загрузки весов.
- Каждая модель упакована как артефакт «Modelfile», объединяющий веса, chat-шаблон, параметры генерации и системный промпт, что делает версии воспроизводимыми.
- Поставляется с локальным HTTP API (по умолчанию `localhost:11434`), совместимым со многими агент-фреймворками — приложения общаются с Ollama как с OpenAI-совместимым эндпоинтом.
- Поддерживает квантование (GGUF, QAT) и ускорители (CUDA, Metal/Apple Silicon), чтобы модели помещались в доступную VRAM и работали эффективно.
- Недавние версии добавили поддержку спекулятивного декодирования / Multi-Token Prediction (MTP), но прирост сильно зависит от оборудования.

## Подробнее

Привлекательность Ollama — в простоте: `ollama run llama3.1` скачивает квантованную модель и открывает chat-REPL. Тот же бинарник обслуживает API, к которому подключаются инструменты и кодинговые агенты для полностью офлайн-инференса, что важно для приватности, стоимости и задач, чувствительных к задержкам.

Поскольку Ollama управляет полным жизненным циклом модели (загрузка, версионирование, шаблон промпта, контекстное окно), он стал дефолтным слоем локального инференса для community-агентов и self-hosted-решений. Поддержка квантования позволяет запускать крупные модели на одной GPU или даже на машинах только с CPU на приемлемой скорости. Продвинутые функции вроде MTP могут примерно удвоить пропускную способность на быстрых CUDA-картах, но на архитектурах с унифицированной памятью (Apple Silicon) возможна регрессия — всегда делайте бенчмарк на реальном оборудовании, прежде чем рассчитывать на ускорение.

## Связанные записи

- [[opencoderag-rag-plugin]] ([OpenCodeRAG RAG Plugin](opencoderag-rag-plugin.md))
- [[mtp-hardware-dependent-speedup]] ([MTP Hardware-Dependent Speedup](../tips/mtp-hardware-dependent-speedup.md))
- [[small-models-clean-architecture]] ([Small Models, Clean Architecture](../tips/small-models-clean-architecture.md))
