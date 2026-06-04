---
title: "HTTP/2 Bomb: Novel DoS Vulnerability Discovered by OpenAI Codex"
title_ru: "HTTP/2 Bomb: новая DoS-уязвимость, обнаруженная OpenAI Codex"
category: news
tags: [openai, codex, vulnerability-discovery, security, http2, nginx, apache, dos, ai-security-research]
aliases: [HTTP/2 Bomb, HPACK bomb variant, Codex vulnerability discovery]
confidence: high
date: 2026-06-03
updated: 2026-06-04
sources:
  - https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html
---

## Summary
OpenAI Codex discovered a novel remote denial-of-service vulnerability in major web servers (NGINX, Apache, IIS, Envoy, Cloudflare Pingora) by chaining two known techniques — HPACK header compression bombs and Slowloris connection holds — in a way that bypasses existing header-size limits, demonstrating AI-assisted offensive security research at the protocol level.

## Key Ideas
- **AI-discovered chain**: Codex chained an HPACK compression bomb variant with a Slowloris-style zero-byte flow-control hold, bypassing server defenses that cap decoded header size by targeting *per-entry bookkeeping* rather than decoded content size.
- **Novel bypass mechanism**: classic HPACK bombs stuff large values into the compression table. HTTP/2 Bomb flips this — headers are nearly empty, but the server allocates bookkeeping overhead for each entry. The decoded-size limit never triggers because there's almost nothing to decode.
- **Scale of impact**: a home computer on a 100 Mbps connection can render a vulnerable server inaccessible in seconds; a single client can exhaust 32 GB of server memory against Apache HTTPD and Envoy in ~20 seconds.
- **Broad exposure**: NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora — all in their *default HTTP/2 configuration*.
- **Patches**: NGINX fixed in 1.29.8+ (adds `max_headers` directive). Apache HTTPD fixed in mod_http2 v2.0.41. IIS, Envoy, Cloudflare Pingora had no patch at time of reporting.

## Details
The HTTP/2 Bomb was discovered by researchers at Calif using OpenAI Codex to chain two independently known techniques. This is a notable case of AI-assisted vulnerability research that reached beyond what prior human analysis had surfaced — the specific combination of HPACK amplification via bookkeeping overhead plus indefinite connection holding was not previously documented.

### Why Existing Defenses Failed
HTTP/2 servers learned to defend against classic HPACK bombs by capping total decoded header size. HTTP/2 Bomb evades this: the attacker sends headers with almost no decodable content, but forces the server to allocate bookkeeping memory for each entry. The decoded-size cap never fires because each header is tiny — only the accumulated metadata overhead kills the server.

The Slowloris component keeps connections open with a zero-byte flow-control window, preventing the server from freeing any allocated memory for as long as the attacker holds the connection. The spec frames memory risk purely as an amplification ratio — but ratio is only half the equation. Memory freed at request completion is harmless; memory pinned indefinitely is an attack.

### Significance for AI Security Research
This continues a pattern established by Anthropic's Project Glasswing (10,000+ vulnerabilities discovered in open-source software) and OpenAI Daybreak (GPT-5.5-Cyber for authorized red teaming): frontier AI models are now capable of discovering genuine, novel security vulnerabilities by reasoning across protocol specifications and chaining known weaknesses in new combinations.

## Related Entries
- [[openai-daybreak-cyber-defense]] ([OpenAI Daybreak: Frontier AI for Cyber Defense](../news/openai-daybreak-cyber-defense.md))
- [[project-glasswing-anthropic-vulnerability-discovery]] ([Project Glasswing: AI Vulnerability Discovery](../news/project-glasswing-anthropic-vulnerability-discovery.md))
- [[mythos-aisi-cyber-capability-2026]] ([Mythos AISI Cyber Capability 2026](../news/mythos-aisi-cyber-capability-2026.md))

---
<!-- RU -->

## Краткое описание
OpenAI Codex обнаружил новую DoS-уязвимость в крупных веб-серверах (NGINX, Apache, IIS, Envoy, Cloudflare Pingora), объединив два известных метода — HPACK-бомбу и Slowloris-удержание — способом, обходящим существующие ограничения размера заголовков.

## Ключевые идеи
- **Цепочка, найденная ИИ**: Codex объединил вариант HPACK-бомбы со Slowloris-удержанием (нулевое flow-control окно), обходя защиты на основе размера заголовков через атаку на *накладные расходы учёта записей*.
- **Новый механизм обхода**: классические HPACK-бомбы используют большие значения в таблице сжатия. HTTP/2 Bomb делает наоборот — заголовки почти пусты, но сервер выделяет память под учётные структуры для каждой записи. Лимит decoded-size никогда не срабатывает, потому что декодировать почти нечего.
- **Масштаб**: домашний компьютер на 100 Мбит/с может вывести уязвимый сервер из строя за секунды; один клиент способен занять 32 ГБ памяти Apache HTTPD или Envoy примерно за 20 секунд.
- **Широкий охват**: NGINX, Apache HTTPD, Microsoft IIS, Envoy, Cloudflare Pingora — все в *конфигурации HTTP/2 по умолчанию*.
- **Патчи**: NGINX исправлен в 1.29.8+ (директива `max_headers`). Apache HTTPD — в mod_http2 v2.0.41. IIS, Envoy, Cloudflare — патча не было на момент публикации.

## Подробнее
Уязвимость обнаружена исследователями Calif с помощью OpenAI Codex путём объединения двух независимо известных техник. Это показательный случай AI-assisted vulnerability research, вышедшего за пределы того, что ранее находили люди: конкретная комбинация HPACK-усиления через bookkeeping overhead и indefinite connection hold не была задокументирована ранее.

Этот случай продолжает паттерн, заложенный Project Glasswing от Anthropic и Daybreak от OpenAI: frontier AI модели способны обнаруживать подлинные новые уязвимости, рассуждая о протокольных спецификациях и объединяя известные слабости в новые комбинации.

## Связанные записи
- [[openai-daybreak-cyber-defense]] ([OpenAI Daybreak: Frontier AI for Cyber Defense](../news/openai-daybreak-cyber-defense.md))
- [[project-glasswing-anthropic-vulnerability-discovery]] ([Project Glasswing: AI Vulnerability Discovery](../news/project-glasswing-anthropic-vulnerability-discovery.md))
- [[mythos-aisi-cyber-capability-2026]] ([Mythos AISI Cyber Capability 2026](../news/mythos-aisi-cyber-capability-2026.md))
