---
title: "Shardflow — LLM Inference Split Across Cloud Regions over Public WAN"
title_ru: "Shardflow — инференс LLM, разрезанный по облачным регионам через публичный WAN"
category: research
tags: [distributed-inference, speculative-decoding, pipeline-parallelism, kaggle, qwen, wan]
aliases: [Shardflow, distributed inference free gpus, shard llm across regions]
confidence: medium
updated: 2026-09-01
sources:
  - https://github.com/rautaditya2606/Shardflow
---

## Summary
Shardflow is a Python/PyTorch framework that partitions any Hugging Face transformer layer-wise across heterogeneous GPU machines — free Kaggle/Colab notebooks, rented cloud GPUs, local rigs — and fights wide-area latency with neural speculative decoding, zero-copy tensor serialization, and a high-throughput TCP relay. Demo: Qwen2.5-7B (FP16) split across two free Kaggle T4s in different GCP regions via a $3/month EC2 relay, at **28.1 TPS peak vs 4.9 baseline (5.7×)**.

## Key Ideas
- **The trick — speculative decoding as latency mask:** a small drafter (Qwen2.5-0.5B, K=8) generates draft tokens locally while the next shard is busy, hiding WAN round-trips (4.07 tokens per round-trip, 65% peak draft acceptance).
- **Measured results:** peak 28.10 TPS (5.71× vs 4.92 baseline; 12.4× vs project v1); average 20.31 TPS; also benchmarked at 14B (Qwen2.5-14B, 4-bit NF4, 20.17 TPS peak).
- **Zero-copy engineering:** exact KV-cache sync and rollback across nodes, meta-device model slicing (zero RAM at load), length-prefixed binary TCP framing.
- **OpenAI-compatible API** exposed; reproducible on 2 free Kaggle instances; 37 passing tests.
- **Honest caveats:** no LICENSE file despite an MIT badge in the README; 3 stars; single-author engineering experiment — the numbers are self-reported.

## Details
Shardflow's thesis: free/cheap disjointed GPUs + a smart protocol can beat paying for a single big GPU. The speculative-decoding-as-WAN-mask is the genuinely transferable idea — it decouples token production from network latency in any pipeline-parallel setup. Practical caveats: public-WAN inference of proprietary weights raises exfiltration concerns, and the ~86ms RTT envelope is why the drafter does the heavy lifting.

## Related Entries
- [[hillock-neurosymbolic-memory]] ([Hillock](../tools/hillock-neurosymbolic-memory.md)) — local single-node alternative
- [[orthrus-qwen3-acceleration]] ([Orthrus-Qwen3 Acceleration](orthrus-qwen3-acceleration.md))
- [[dual-dgx-spark-deepseek-v4-flash]] ([Dual DGX Spark DeepSeek V4 Flash](../tips/dual-dgx-spark-deepseek-v4-flash.md))
- [[ollama]] ([Ollama](ollama.md))

---
<!-- RU -->

## Краткое описание
Shardflow — Python/PyTorch фреймворк, разрезающий любой Hugging Face трансформер послойно между разнородными GPU-машинами — бесплатными Kaggle/Colab, облачными GPU, локальными ригами — и компенсирующий WAN-латентность нейроспекулятивным декодированием, zero-copy сериализацией тензоров и производительным TCP-релеем. Демо: Qwen2.5-7B (FP16) на двух бесплатных Kaggle T4 в разных регионах GCP через релей на EC2 — **28.1 TPS пик против 4.9 базовых (5.7×)**.

## Ключевые идеи
- **Трюк — спекулятивное декодирование как маска латентности:** малый драфтер (Qwen2.5-0.5B, K=8) генерирует черновики локально, пока следующий шард занят, скрывая WAN-тайм-ауты (4.07 токена за round-trip, 65% принятия).
- **Измеренные результаты:** пик 28.10 TPS (5.71×; в 12.4× против v1 проекта); среднее 20.31 TPS; также 14B (NF4, 20.17 TPS).
- **Zero-copy инженерия:** точная синхронизация и откат KV-кэша между нодами, meta-device нарезка (ноль RAM при загрузке), бинарный TCP-фрейминг.
- **OpenAI-совместимый API**; воспроизводимо на 2 бесплатных Kaggle; 37 проходящих тестов.
- **Честные оговорки:** нет файла LICENSE (несмотря на бейдж MIT); 3 звезды; эксперимент одного автора — числа самопровозглашённые.

## Подробнее
Тезис Shardflow: бесплатные/дешёвые разрозненные GPU + умный протокол могут победить один большой GPU. Спекулятивное декодирование как маска WAN — по-настоящему переносимая идея для любого pipeline-parallel сетапа. Практические оговорки: инференс проприетарных весов через публичный WAN поднимает вопросы эксфильтрации, а конверт ~86 мс RTT — причина, по которой драфтер делает тяжёлую работу.

## Связанные записи
- [[hillock-neurosymbolic-memory]] ([Hillock](hillock-neurosymbolic-memory.md))
- [[orthrus-qwen3-acceleration]] ([Orthrus-Qwen3 Acceleration](orthrus-qwen3-acceleration.md))
- [[dual-dgx-spark-deepseek-v4-flash]] ([Dual DGX Spark DeepSeek V4 Flash](../tips/dual-dgx-spark-deepseek-v4-flash.md))
- [[ollama]] ([Ollama](ollama.md))
