---
title: "Supply Chain Attacks Explicitly Targeting AI Coding Tools (May 2026 Wave)"
title_ru: "Атаки на цепочку поставок, целенаправленно атакующие AI-инструменты кодирования (волна мая 2026)"
category: news
tags: [supply-chain, security, claude-code, vs-code, cursor, npm, credential-theft, mini-shai-hulud, nx-console, developer-security]
aliases: [Nx Console attack, Mini Shai-Hulud npm, supply chain Claude Code, AI tool supply chain]
confidence: high
date: 2026-05-19
updated: 2026-05-19
sources:
  - https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
  - https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html
---

## Summary

Two related supply chain attacks disclosed on May 19, 2026, mark an escalation in attacker targeting of AI coding tools: the compromised Nx Console VS Code extension (18.95.0) explicitly harvests **Anthropic Claude Code configurations**, while the broader Mini Shai-Hulud npm campaign now includes "AI tool persistence hooks" and a Sigstore provenance-forging technique that makes malicious packages appear as legitimate signed builds.

## Key Ideas

- **Nx Console 18.95.0 specifically steals Claude Code secrets.** The compromised VS Code extension (2.2M installs) executed a multi-stage credential stealer that targeted 1Password vaults, npm/GitHub/AWS tokens — and explicitly Anthropic Claude Code configuration files.
- **Five npm packages backdoor Claude Code sessions directly.** Separately, packages `iceberg-javascript`, `supabase-javascript`, `auth-javascript`, `microsoft-applicationinsights-common`, and `ms-graph-types` were found to contain hidden ELF binaries that backdoor active Claude Code sessions to exfiltrate developer credentials.
- **Mini Shai-Hulud campaign now open-source.** TeamPCP released the full source code of their supply chain worm on BreachForums, dramatically lowering the barrier for copycat attacks. Over 2,500 GitHub repos contain the "Shai-Hulud marker" — a lower bound on compromised environments.
- **Sigstore provenance forgery is the new escalation.** Both attacks use stolen OIDC tokens to generate legitimate Sigstore attestations, making malicious package versions cryptographically indistinguishable from authorized builds — breaking the assumption that signed provenance = safe.
- **AI tool persistence hooks added to worm framework.** The Mini Shai-Hulud source code release explicitly includes hooks for persisting in AI coding tool environments (VS Code extensions, Cursor, Claude Code), signalling intent to target the AI developer toolchain at scale.
- **LLM proxy hijacking observed.** npm packages `k8s-pod-checker`, `dev-env-setup`, and `node-perf-utils` install a local LLM proxy service on victim machines, routing the victim's LLM traffic (including prompts and responses) through attacker-controlled infrastructure.

## Details

### The Nx Console Incident

On May 18, 2026, threat actors pushed `rwl.angular-console` version 18.95.0 to the VS Code Marketplace via a compromised developer credential. Within seconds of a developer opening any workspace:

1. An obfuscated 498KB payload was fetched from an orphaned commit in the official `nrwl/nx` GitHub repository.
2. The Bun JavaScript runtime was installed silently.
3. A multi-stage credential stealer executed as a detached background process.
4. Secrets were exfiltrated via HTTPS, GitHub API, and DNS tunneling.
5. On macOS, a Python backdoor was installed that used the GitHub Search API as a dead-drop command resolver.

**Targets explicitly listed in the payload:** 1Password vaults, npm tokens, GitHub credentials, AWS credentials — and Anthropic Claude Code configuration files. The exposure window was 11 minutes (2:36 PM–2:47 PM CEST on May 18). Users who had the extension installed during that window and opened any workspace are considered compromised.

**IOCs:**
- Files: `~/.local/share/kitty/cat.py`, `~/Library/LaunchAgents/com.user.kitty-monitor.plist`, `/var/tmp/.gh_update_state`
- Processes: python running `cat.py`, any process with `__DAEMONIZED=1`

**Remediation:** Update to Nx Console ≥ 18.100.0, terminate the above processes, delete artifacts, and rotate all credentials — particularly Claude Code API keys, GitHub tokens, npm tokens, and AWS credentials.

### Mini Shai-Hulud: npm Campaign Escalation

The same underlying campaign (Mini Shai-Hulud / TeamPCP) compromised 323 unique npm packages (639 malicious versions) in the @antv ecosystem and related packages including `echarts-for-react` (~1.1M weekly downloads). The payload harvests 20+ credential types and has a self-replication mechanism: it uses stolen npm OIDC tokens to inject itself into every package maintained by the compromised account.

The critical escalation: TeamPCP released the full worm source code on BreachForums. Copycat variants have already appeared. The framework now explicitly includes:
- **Sigstore attestation pipeline** — forges SLSA provenance using legitimate OIDC tokens from CI runners, making malicious packages appear as verified, authorized builds
- **AI tool persistence hooks** — designed to survive inside VS Code, Cursor, and Claude Code environments after initial infection

### What This Means for AI Coding Tool Users

AI coding agents like Claude Code operate with broad file-system access and often store credentials in configuration files. A compromised VS Code extension or npm package can silently harvest these credentials before any agent session begins. The fact that attackers are now *specifically* naming Claude Code as a target — and writing persistence hooks for AI tool environments — signals that developer tooling has become a primary supply chain attack surface.

**Recommended hygiene:**
- Audit VS Code extensions: remove any not from verified publishers, check version history for unexpected updates
- Use npm `--ignore-scripts` or `--no-optional` for untrusted packages; audit `preinstall`/`postinstall` hooks
- Rotate Claude Code API keys if any npm package was installed from affected ecosystems in May 2026
- Enable GitHub token alerts; audit for repositories with "Shai-Hulud" markers

## Notable Quotes

> "One capability that stands out: the payload contains full Sigstore integration, including Fulcio certificate issuance and SLSA provenance generation. Combined with stolen npm OIDC tokens, this means the attacker could publish downstream npm packages with valid, cryptographically signed provenance attestations, making the malicious packages appear as legitimate, verified builds." — StepSecurity

> "AI tool persistence hooks" — TeamPCP Mini Shai-Hulud source code release description, BreachForums, May 2026

## Related Entries

- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[mythos-cybersecurity-agent]] ([Mythos Cybersecurity Agent](../agents/mythos-cybersecurity-agent.md))
- [[github-copilot-app]] ([GitHub Copilot App](../news/github-copilot-app.md))

---
<!-- RU -->

## Краткое описание

Две связанные атаки на цепочку поставок, раскрытые 19 мая 2026 года, знаменуют эскалацию целенаправленной атаки злоумышленников на инструменты AI-кодирования: скомпрометированное расширение VS Code Nx Console (18.95.0) явно похищает **конфигурации Anthropic Claude Code**, а более широкая npm-кампания Mini Shai-Hulud теперь включает «хуки персистентности AI-инструментов» и технику подделки происхождения Sigstore, делающую вредоносные пакеты неотличимыми от легитимных подписанных сборок.

## Ключевые идеи

- **Nx Console 18.95.0 целенаправленно крадёт секреты Claude Code.** Скомпрометированное расширение VS Code (2,2 млн установок) запускало многоступенчатый похититель учётных данных, нацеленный на хранилища 1Password, токены npm/GitHub/AWS — и явно на файлы конфигурации Anthropic Claude Code.
- **Пять npm-пакетов создают бэкдор в сессиях Claude Code.** Пакеты `iceberg-javascript`, `supabase-javascript`, `auth-javascript`, `microsoft-applicationinsights-common` и `ms-graph-types` содержали скрытые ELF-бинарники, создающие бэкдор в активных сессиях Claude Code.
- **Кампания Mini Shai-Hulud стала открытым исходным кодом.** TeamPCP опубликовала исходный код своего червя на BreachForums, резко снизив барьер для атак-подражателей. Более 2500 репозиториев на GitHub содержат маркер «Shai-Hulud» — нижняя граница числа скомпрометированных сред.
- **Подделка происхождения Sigstore — новая эскалация.** Обе атаки используют украденные OIDC-токены для генерации легитимных аттестаций Sigstore, делая вредоносные версии пакетов криптографически неотличимыми от авторизованных сборок.
- **Хуки персистентности AI-инструментов добавлены в фреймворк червя.** Опубликованный исходный код явно включает хуки для выживания в средах VS Code, Cursor и Claude Code — сигнал о намерении атаковать инструментальный стек AI-разработчиков в масштабе.
- **Угон LLM-прокси.** npm-пакеты `k8s-pod-checker`, `dev-env-setup` и `node-perf-utils` устанавливают на машины жертв локальный LLM-прокси-сервис, перенаправляя LLM-трафик (включая промпты и ответы) через инфраструктуру злоумышленников.

## Подробнее

### Инцидент с Nx Console

18 мая 2026 года злоумышленники через скомпрометированные учётные данные разработчика опубликовали `rwl.angular-console` версии 18.95.0 в VS Code Marketplace. В течение секунд с момента открытия любого рабочего пространства запускался обфусцированный пейлоад 498 КБ из сиротского коммита в официальном GitHub-репозитории `nrwl/nx`. Он устанавливал среду выполнения Bun, запускал многоступенчатый похититель учётных данных как фоновый процесс и на macOS устанавливал Python-бэкдор.

**Явные цели в пейлоаде:** хранилища 1Password, токены npm, учётные данные GitHub, AWS — и файлы конфигурации Anthropic Claude Code. Окно воздействия: 11 минут 18 мая 2026 года.

**Рекомендации:** обновиться до Nx Console ≥ 18.100.0, остановить процессы `cat.py` и `__DAEMONIZED=1`, удалить артефакты, ротировать все учётные данные — особенно API-ключи Claude Code, токены GitHub и npm, учётные данные AWS.

### Эскалация npm-кампании Mini Shai-Hulud

Та же кампания скомпрометировала 323 уникальных npm-пакета (639 вредоносных версий) в экосистеме @antv и связанных пакетах, включая `echarts-for-react` (~1,1 млн загрузок в неделю). Ключевая эскалация: TeamPCP опубликовала полный исходный код червя на BreachForums. Фреймворк теперь включает конвейер аттестации Sigstore (подделка SLSA-происхождения) и хуки персистентности AI-инструментов.

### Что это означает для пользователей AI-инструментов кодирования

AI-агенты вроде Claude Code работают с широким доступом к файловой системе и часто хранят учётные данные в конфигурационных файлах. Злоумышленники теперь *явно* называют Claude Code в качестве цели и пишут хуки персистентности для AI-инструментов — сигнал о том, что инструментарий разработчиков стал основной поверхностью атаки цепочки поставок.

## Примечательные цитаты

> «Одна возможность особенно выделяется: пейлоад содержит полную интеграцию Sigstore, включая выпуск сертификатов Fulcio и генерацию SLSA-происхождения. В сочетании с украденными npm OIDC-токенами это означает, что злоумышленник мог публиковать нижестоящие npm-пакеты с валидными криптографически подписанными аттестациями происхождения, делая вредоносные пакеты похожими на легитимные, верифицированные сборки.» — StepSecurity

## Связанные записи

- [[agent-harness-engineering]] ([Agent Harness Engineering](../concepts/agent-harness-engineering.md))
- [[mythos-cybersecurity-agent]] ([Mythos Cybersecurity Agent](../agents/mythos-cybersecurity-agent.md))
