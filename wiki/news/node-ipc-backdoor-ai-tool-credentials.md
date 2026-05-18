---
title: "node-ipc Supply Chain Attack Targets Claude AI and Developer Credentials"
title_ru: "Атака на цепочку поставок node-ipc целится в учётные данные Claude AI и разработчиков"
category: news
tags: [supply-chain, npm, claude-code, ai-coding-tools, credential-theft, developer-security, node-ipc]
aliases: [node-ipc backdoor, node-ipc stealer, npm supply chain AI credentials]
confidence: high
date: 2026-05-14
updated: 2026-05-18
sources:
  - https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html
---

## Summary

Three versions of the popular npm package `node-ipc` (9.1.6, 9.2.3, 12.0.1) were found to contain an obfuscated credential-stealing backdoor published by a compromised maintainer account. The malware explicitly targets 90 credential categories including **Claude AI settings**, Kiro IDE configs, GitHub CLI, AWS/GCP/Azure keys, SSH keys, and Kubernetes tokens — making this a targeted attack on the AI coding tool developer population.

## Key Ideas

- **AI-specific targeting:** The credential list explicitly includes Claude AI configuration files and Kiro IDE settings alongside cloud credentials. This is among the first supply chain attacks documented as specifically harvesting AI coding assistant credentials.
- **Maintainer account takeover via expired domain:** The `atiertant` maintainer account's email was hosted on `atlantis-software[.]net`, which expired 2025-01-10 and was re-registered 2026-05-07 — one week before the attack. The attacker triggered a standard npm password reset to gain publish rights without compromising any of the maintainer's own infrastructure.
- **Payload evasion:** The malware uses no npm lifecycle hooks (no `preinstall`/`postinstall`). Instead it appends an IIFE to `node-ipc.cjs` that fires unconditionally on every `require('node-ipc')`. Version 12.0.1 adds a SHA-256 fingerprint check — it is inert unless the target module's entry point matches a pre-computed hash, indicating a targeted delivery for a specific developer or project.
- **Dual exfiltration:** Data goes via HTTPS POST to a fake Azure domain (`sh.azurestaticprovider[.]net`) AND via DNS TXT records after overriding the system resolver to bypass corporate DNS logging.
- **Detection gap:** The DNS exfiltration channel routes directly to the C2 IP, bypassing public resolvers — organizations relying solely on corporate DNS logging would not see this traffic.

## Details

The three malicious versions were published by an account named `atiertant` with no prior publish history for this package (previous legitimate update: August 2024). The 21-month gap before compromise is consistent with a dormant maintainer account targeted specifically for its publish rights.

**Malware behavior:**
1. Fingerprints the host environment and enumerates local files
2. Harvests 90 credential categories (AI tool configs, cloud keys, SSH, Git, database passwords, shell history)
3. Compresses into GZIP archive
4. Primary exfil: HTTPS POST to `sh.azurestaticprovider[.]net`
5. Secondary exfil: DNS TXT chunks using Google Public DNS (`1.1.1.1` / `8.8.8.8`) to bypass local DNS controls
6. Forks a detached background process to continue exfiltration after parent app terminates

**Affected versions:** node-ipc@9.1.6, node-ipc@9.2.3, node-ipc@12.0.1
**Clean versions:** node-ipc@9.2.1, node-ipc@12.0.0

**Remediation:**
1. Remove compromised versions; reinstall 9.2.1 or 12.0.0
2. Assume compromise — rotate all credentials (especially AI API keys, cloud keys, SSH, GitHub tokens)
3. Audit npm publish logs and cloud IAM activity during the compromised window
4. Block egress to `sh.azurestaticprovider[.]net`
5. If using Claude Code or Kiro IDE: rotate API keys and review API usage logs for unauthorized activity

## Notable Quotes

> "This campaign reflects how software supply chain attacks are evolving beyond simple malicious packages into infrastructure-aware credential harvesting operations. Attackers are increasingly targeting the identities and automation systems powering modern software delivery pipelines." — Avital Harel, Upwind

## Related Entries

- [[ai-agent-security]] ([AI Agent Security](../agents/ai-agent-security.md))
- [[claude-code]] ([Claude Code](../tools/claude-code.md))
- [[supply-chain-security]] ([Supply Chain Security](../concepts/supply-chain-security.md))

---
<!-- RU -->

## Краткое описание

Три версии популярного npm-пакета `node-ipc` (9.1.6, 9.2.3, 12.0.1) содержали обфусцированный бэкдор для кражи учётных данных, опубликованный через скомпрометированный аккаунт мейнтейнера. Вредонос явно нацелен на **настройки Claude AI**, конфиги Kiro IDE, GitHub CLI, ключи AWS/GCP/Azure, SSH, токены Kubernetes — это одна из первых задокументированных атак на цепочку поставок, специально нацеленных на учётные данные AI-инструментов разработчиков.

## Ключевые идеи

- **AI-специфичное таргетирование:** В списке 90 категорий учётных данных явно упомянуты файлы конфигурации Claude AI и Kiro IDE — наряду с облачными ключами.
- **Захват аккаунта через истёкший домен:** Email аккаунта мейнтейнера `atiertant` был привязан к домену `atlantis-software[.]net`, истёкшему 10 января 2025 и перерегистрированному 7 мая 2026 — за неделю до атаки. Злоумышленник сбросил пароль npm через стандартный механизм восстановления.
- **Обход хуков:** Вредонос не использует npm lifecycle hooks, а добавляет IIFE в `node-ipc.cjs`, срабатывающий при каждом `require('node-ipc')`. Версия 12.0.1 содержит SHA-256-проверку — неактивна, если хэш точки входа не совпадает с предварительно вычисленным значением (целевая атака на конкретного разработчика).
- **Двойная экфильтрация:** HTTPS POST на фиктивный Azure-домен + DNS TXT-записи после подмены системного DNS-резолвера — для обхода корпоративного DNS-логирования.

## Подробнее

Вредоносные версии опубликованы аккаунтом `atiertant` без истории публикаций для этого пакета (последнее легитимное обновление — август 2024). 21-месячный перерыв перед компрометацией соответствует паттерну целенаправленного захвата спящего аккаунта с правами публикации.

**Скомпрометированные версии:** node-ipc@9.1.6, node-ipc@9.2.3, node-ipc@12.0.1  
**Чистые версии:** node-ipc@9.2.1, node-ipc@12.0.0

**Меры реагирования:** удалить скомпрометированные версии; ротировать все учётные данные (особенно API-ключи AI-инструментов, облачные ключи, SSH, GitHub-токены); проверить логи cloud IAM и npm publish в период компрометации; заблокировать исходящий трафик к `sh.azurestaticprovider[.]net`.

## Примечательные цитаты

> «Эта кампания отражает, как атаки на цепочку поставок ПО эволюционируют от простых вредоносных пакетов к инфраструктурно-осведомлённым операциям кражи учётных данных.» — Avital Harel, Upwind

## Связанные записи

- [[ai-agent-security]] ([AI Agent Security](../agents/ai-agent-security.md))
- [[claude-code]] ([Claude Code](../tools/claude-code.md))
- [[supply-chain-security]] ([Supply Chain Security](../concepts/supply-chain-security.md))
