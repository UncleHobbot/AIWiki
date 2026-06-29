---
title: "oxideLLM: Rust Gateway That Stops Ollama Wasting GPU on Closed Tabs"
title_ru: "oxideLLM: Rust-шлюз, останавливающий пустую трату GPU Ollama на закрытых вкладках"
category: tools
tags: [ollama, rust, gpu, proxy, load-balancing, inference]
aliases: [oxideLLM, oxide LLM, ollama gpu leak proxy]
confidence: medium
updated: 2026-06-29
sources:
  - https://github.com/lugga1s/oxideLLM
  - https://www.reddit.com/r/ollama/comments/1uizg46/i_built_a_10mb_rust_gateway_that_stops_ollama/
---

## Summary
oxideLLM is a lightweight (~10 MB) Rust proxy gateway that sits between a frontend (Open WebUI, custom apps) and an Ollama backend, instantly aborting generation the moment a client closes its tab — fixing the "GPU leak" where Ollama keeps burning VRAM and compute to finish responses no one will read. It also adds load balancing across multiple Ollama instances.

## Key Ideas
- **The GPU-leak problem**: when a user closes a browser tab or clicks stop mid-generation, Ollama often keeps the model loaded and the GPU hot in the background to finish generating the full response — visible via `ollama ps` as a model still active and hogging VRAM for tokens that will be discarded.
- **Instant abort via Rust's `Drop` trait**: the gateway wraps the streaming connection in a guard implementing `Drop`. The exact millisecond the client closes the TCP socket (closing the window, navigating away), the guard drops and aborts the upstream request, telling Ollama to halt generation instantly.
- **Load balancing**: routes requests across multiple Ollama backends.
- **Tiny footprint**: ~10 MB single binary, Rust, no heavy runtime.
- **Why it matters for shared/local deployments**: anyone running Ollama behind a shared web UI (multiple users, long generations) bleeds GPU time on abandoned requests.

## Details
The underlying issue is a mismatch between client intent ("I left") and backend behavior ("keep generating to completion"). Ollama's default streaming doesn't tightly couple generation lifecycle to client connection state, so an abandoned request keeps occupying a GPU slot — costly on hardware with limited VRAM or when serving several users.

oxideLLM closes that gap at the proxy layer by tying upstream generation lifetime to the downstream TCP socket lifetime. Because the abort is driven by the socket `Drop` (a deterministic destructor), there's no polling latency — the stop is near-instantaneous.

## Related Entries
- [[product-ollama]] ([Ollama Cloud](product-ollama.md))
- [[shrimp-coding-agent]] ([Shrimp: Coding Agent for Ollama](shrimp-coding-agent.md))
- [[turbo-llm-launcher]] ([Turbo-LLM: Run Any llama.cpp Fork](turbo-llm-launcher.md))

---
<!-- RU -->

## Краткое описание
oxideLLM — лёгкий (~10 МБ) Rust-прокси-шлюз между фронтендом (Open WebUI, кастомные приложения) и бэкендом Ollama, мгновенно прерывающий генерацию, как только клиент закрывает вкладку. Это устраняет «утечку GPU», когда Ollama продолжает жечь VRAM и вычисления, чтобы дописать ответ, который никто не прочитает. Также добавляет балансировку нагрузки между инстансами Ollama.

## Ключевые идеи
- **Проблема утечки GPU**: когда пользователь закрывает вкладку или жмёт «стоп» во время генерации, Ollama часто продолжает держать модель загруженной и GPU горячим, чтобы дописать полный ответ — через `ollama ps` видно, что модель активна и занимает VRAM под выбрасываемые токены.
- **Мгновенный abort через `Drop` Rust**: шлюз оборачивает стриминг-соединение в guard, реализующий `Drop`. В ту же миллисекунду, когда клиент закрывает TCP-сокет, guard дропается и прерывает upstream-запрос, приказывая Ollama немедленно остановить генерацию.
- **Балансировка нагрузки**: маршрутизация запросов между несколькими бэкендами Ollama.
- **Крошечный footprint**: ~10 МБ, один бинарник на Rust, без тяжёлого рантайма.
- **Зачем это для shared/local-деплоев**: любой, кто крутит Ollama за общим веб-UI, теряет GPU-время на брошенных запросах.

## Подробнее
Корень проблемы — рассогласование намерения клиента («я ушёл») и поведения бэкенда («дописать до конца»). Стриминг Ollama по умолчанию не связывает жёстко жизненный цикл генерации с состоянием клиентского соединения, поэтому брошенный запрос продолжает занимать GPU-слот.

oxideLLM закрывает этот разрыв на уровне прокси, привязывая время жизни upstream-генерации к времени жизни downstream TCP-сокета. Поскольку abort управляется `Drop` сокета (детерминированный деструктор), нет задержки на поллинг — остановка почти мгновенна.

## Связанные записи
- [[product-ollama]] ([Ollama Cloud](product-ollama.md))
- [[shrimp-coding-agent]] ([Shrimp: Coding Agent for Ollama](shrimp-coding-agent.md))
- [[turbo-llm-launcher]] ([Turbo-LLM: Run Any llama.cpp Fork](turbo-llm-launcher.md))
