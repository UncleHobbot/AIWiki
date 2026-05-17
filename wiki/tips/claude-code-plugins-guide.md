---
title: "Claude Code Plugins: Curated Guide to the Top 36"
title_ru: "Плагины Claude Code: путеводитель по 36 лучшим"
category: tips
tags: [claude-code, plugins, skills, mcp, productivity, extensions]
updated: 2026-05-15
sources:
  - https://x.com/zodchiii/status/2042529018260656555
---

## Summary
A curated ranking of the most useful Claude Code plugins across official marketplace, community, and partner categories — with install instructions and the practical sweet spot of 3–5 active plugins.

## Key Ideas
- **Install any plugin in 3 steps:** `/plugin` → Discover tab → find by name → select scope (user or project). Community plugins require adding the community marketplace first.
- **3–5 active plugins is the sweet spot:** Each plugin consumes context tokens. More plugins = more overhead before your first prompt. Disable unused plugins with `/plugin disable <name>`.
- **Top official picks by install count:** Frontend Design (400k+ installs, polished UI code), Superpowers (290k+, 20+ battle-tested skills), Context7 (live docs from source repos — stops hallucinated API calls).
- **LSP plugins give Claude VS Code-level code intelligence:** TypeScript, Python, Rust, and Ruby LSP plugins provide jump-to-definition, find-references, and type error awareness.
- **Automation standouts:** Ralph Loop (autonomous coding sessions with clean git history), Chrome DevTools (debug live pages via existing Chrome session), Playwright (real browser control for UI testing).
- **SaaS integrations worth having:** GitHub, Vercel, Sentry, Linear, Supabase — each turns Claude Code into a control plane for that service.

## Details

### Official Marketplace — Core Skills
| # | Plugin | What it does |
|---|---|---|
| 01 | **Frontend Design** | Polished UI code with real design systems. 400k+ installs. |
| 02 | **Superpowers** | 20+ skills: TDD, debugging, plan-to-code, brainstorming. 290k+ installs. |
| 03 | **Context7** | Live API docs from source repos — prevents hallucinated library code. |
| 04 | **Code Review** | Structured reviews: bugs, security, performance, style. |
| 05 | **Security Guidance** | OWASP Top 10, auth flaws, injection, hardcoded secrets. |
| 06 | **Commit Commands** | Smart commits, PR creation, changelog generation. |
| 07 | **Feature Dev** | Spec → plan → implement → test → PR workflow. |
| 08 | **Plugin Toolkit** | 7 skills for building your own plugins. |

### Language Server Protocol (Code Intelligence)
| # | Plugin | What it does |
|---|---|---|
| 09 | TypeScript LSP | Pyright-style type checking and navigation. |
| 10 | Python LSP | Type checking and code navigation. |
| 11 | Rust LSP | rust-analyzer integration. |
| 12 | Ruby LSP | Ruby language server. |

### Automation & Browser
| # | Plugin | What it does |
|---|---|---|
| 13 | **Ralph Loop** | Autonomous sessions: Claude works tasks, commits, keeps going. Leave it running. |
| 14 | Chrome DevTools | Inspect network, console errors, debug live pages. |
| 15 | **Playwright** | Real browser control — clicks, fills forms, screenshots, UI tests. |
| 16 | Firecrawl | Scrape URLs, crawl sites, autonomous research. |
| 17 | Sourcegraph | Cross-codebase search, reference tracing, refactor impact analysis. |

### Data & Cloud
| # | Plugin | Category |
|---|---|---|
| 18 | SQL Analytics | SQL, datasets, visualizations. |
| 19 | Data Engineering | Warehouse, pipelines, Airflow. |
| 20 | Amplitude | Analytics tracking plan from codebase. |
| 21 | **Vercel** | Deployments, builds, logs, domains, debug failures. |
| 22 | AWS Deploy | Architecture recommendations, cost estimates, IaC. |
| 23 | PagerDuty Risk Score | Pre-commit diff scoring against incident history. |
| 24 | Mintlify | Documentation from code, MDX conversion. |

### Service Integrations
| # | Plugin | What it does |
|---|---|---|
| 25 | GitHub | PRs, issues, code search, CI/CD. |
| 26 | Slack | Draft messages, surface channel insights. |
| 27 | Sentry | Production error stack traces + fix recommendations. |
| 28 | Linear | Issue tracking, sprints, tickets. |
| 29 | Supabase | Database, auth, storage via prompts. |
| 30 | Stripe | Payments, subscriptions, customer data. |

### Knowledge-Work Plugins (community marketplace)
Add first: `npx skills add anthropic/knowledge-work-plugins`

| # | Plugin | Category |
|---|---|---|
| 31 | Brand Voice | Enforces consistent tone from your style guide. |
| 32 | Marketing | SEO, content strategy, campaigns, competitive analysis. |
| 33 | Sales | Prospecting, email sequences, pipeline. |
| 34 | Legal | Contract review, compliance, risk (first pass only). |
| 35 | Finance | Analysis, reporting, budgets, forecasts. |
| 36 | Productivity | Meeting summaries, tasks, email drafting. |

## Notable Quotes
> "Each plugin uses context tokens. More plugins = more overhead. 3-5 active plugins is the sweet spot." — @zodchiii

## Related Entries
- [[claude-code-handoff-prototype-skills]]
- [[llm-wiki-setup-guide]]
- [[han-claude-code-plugin]]
- [[react-doctor]]
- [[visual-explainer]]
- [[package-hallucination-mcp]]
- [[matt-pocock-aihero]]

---
<!-- RU -->

## Краткое описание
Кураторский рейтинг наиболее полезных плагинов Claude Code из официального маркетплейса, сообщества и партнёров — с инструкциями по установке и оптимальным количеством 3–5 активных плагинов.

## Ключевые идеи
- **Установка плагина в 3 шага:** `/plugin` → вкладка Discover → найти по имени → выбрать область (user или project). Плагины сообщества требуют предварительного добавления маркетплейса.
- **Оптимально 3–5 активных плагинов:** Каждый плагин потребляет токены контекста. Чем больше плагинов — тем выше накладные расходы до первого промпта. Отключайте неиспользуемые через `/plugin disable <name>`.
- **Топ официальных по числу установок:** Frontend Design (400k+, качественный UI-код), Superpowers (290k+, 20+ навыков), Context7 (живая документация из исходников — исключает галлюцинации API).
- **LSP-плагины дают Claude уровень VS Code:** TypeScript, Python, Rust и Ruby LSP обеспечивают переход к определениям, поиск ссылок и осведомлённость об ошибках типов.
- **Выдающиеся инструменты автоматизации:** Ralph Loop (автономные сессии с чистой историей git), Chrome DevTools (отладка живых страниц через существующую сессию Chrome), Playwright (управление реальным браузером).

## Подробнее

Плагины Claude Code — это пакеты навыков, команд, хуков и MCP-серверов, устанавливаемые одной командой. Они расширяют возможности Claude Code без ручной настройки конфигурации.

Для плагинов сообщества, которых нет в официальном маркетплейсе, сначала добавьте источник:
`npx skills add anthropic/knowledge-work-plugins`

После этого плагины из этого репозитория появятся на вкладке Discover.

## Связанные записи
- [[claude-code-handoff-prototype-skills]]
- [[llm-wiki-setup-guide]]
- [[han-claude-code-plugin]]
- [[react-doctor]]
- [[visual-explainer]]
- [[package-hallucination-mcp]]
- [[matt-pocock-aihero]]
