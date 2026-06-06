---
title: "Awesome Agent Vault"
title_ru: "Awesome Agent Vault"
category: tools
tags: [security, credentials, agent-security, mcp, oauth, secrets-management]
aliases: [Agent Vault, awesome-agent-vault, agent credential management]
confidence: medium
updated: 2026-06-06
sources:
  - https://github.com/zriyansh/awesome-agent-vault
---

## Summary
A curated directory mapping how to give AI agents credentials safely. Organized into five reader-intent buckets covering products, integrations, service-specific recipes, security patterns, and threat models.

## Key Ideas
- Five-bucket structure: Products (35+ tools), Integrations (20+ agent platforms), Services (per-API credential recipes), Patterns (named solutions to recurring problems), Threat Models (attack surfaces with mitigations)
- Products include 1Password CLI, HashiCorp Vault, Infisical Agent Vault, Docker MCP Gateway, Microsoft Agent Governance Toolkit and others
- Integrations cover Claude Code, Codex CLI, Cursor, Cline, OpenCode, LangChain, LangGraph, Vercel AI SDK, and more
- Compatibility matrix shows products x platforms with status indicators
- Curated by Authsome, neutral and CTA-free

## Details
Awesome Agent Vault fills a gap in the agent ecosystem: the lack of a canonical reference for credential management. As agents gain autonomy to call APIs, write files, and execute shell commands, the question of how to scope, store, and rotate their credentials becomes critical.

The **Products** section catalogs 35+ tools ranging from enterprise secret managers (HashiCorp Vault, AWS Secrets Manager) to agent-specific solutions (Docker MCP Gateway, Microsoft Agent Governance Toolkit). Each entry links to the tool and notes its approach to credential injection.

The **Integrations** section lists 20+ agent platforms with notes on how each handles secrets — from environment variable injection to OAuth flows to MCP-based credential passing.

The **Services** section provides per-API recipes: how to safely hand a Stripe key, GitHub token, Slack bot token, Anthropic API key, or Google Workspace credential to an agent, with minimal scope and rotation guidance.

The **Patterns** section names recurring solutions (e.g., "ephemeral token per task", "scoped OAuth per agent session") and cites projects that implement them well.

The **Threat Models** section documents known attack surfaces — credential leakage in logs, supply-chain injection via MCP servers, privilege escalation through agent tool use — with concrete mitigations.

## Related Entries
- [[microsoft-agent-governance-toolkit]] ([Microsoft Agent Governance Toolkit](../tools/microsoft-agent-governance-toolkit.md))
- [[ai-agent-identity-iam-risks]] ([AI Agent Identity and IAM Risks](../concepts/ai-agent-identity-iam-risks.md))
- [[claude-code-permission-modes]] ([Claude Code Permission Modes](../tools/claude-code-permission-modes.md))

---
<!-- RU -->

## Краткое описание
Курированный каталог, описывающий, как безопасно передавать AI-агентам учётные данные. Организован в пять разделов по намерению читателя: продукты, интеграции, рецепты для сервисов, паттерны безопасности и модели угроз.

## Ключевые идеи
- Пять разделов: Products (35+ инструментов), Integrations (20+ агентных платформ), Services (рецепты для каждого API), Patterns (именованные решения типовых проблем), Threat Models (поверхности атак с мерами защиты)
- Продукты включают 1Password CLI, HashiCorp Vault, Infisical Agent Vault, Docker MCP Gateway, Microsoft Agent Governance Toolkit и другие
- Интеграции охватывают Claude Code, Codex CLI, Cursor, Cline, OpenCode, LangChain, LangGraph, Vercel AI SDK и другие
- Матрица совместимости показывает статус поддержки продуктов на разных платформах
- Поддерживается Authsome — нейтральный каталог без рекламы

## Подробнее
Awesome Agent Vault заполняет пробел в экосистеме агентов: отсутствие канонического справочника по управлению учётными данными. По мере того как агенты получают автономность вызывать API, записывать файлы и выполнять команды оболочки, вопрос о том, как ограничить, хранить и ротировать их учётные данные, становится критическим.

Раздел **Products** каталогизирует 35+ инструментов — от корпоративных хранилищ секретов (HashiCorp Vault, AWS Secrets Manager) до специализированных агентных решений (Docker MCP Gateway, Microsoft Agent Governance Toolkit).

Раздел **Integrations** перечисляет 20+ агентных платформ с описанием подхода каждой к работе с секретами — от инъекции через переменные окружения до OAuth-потоков и передачи учётных данных через MCP.

Раздел **Services** содержит рецепты для каждого API: как безопасно передать агенту Stripe-ключ, GitHub-токен, Slack bot token, Anthropic API key или Google Workspace credential с минимальными правами и рекомендациями по ротации.

Раздел **Patterns** даёт имена типовым решениям (например, «эphemeral-токен на задачу», «scoped OAuth на сессию агента») и ссылается на проекты, которые их хорошо реализуют.

Раздел **Threat Models** документирует известные поверхности атак — утечку учётных данных в логах, атаки через цепочку поставок MCP-серверов, повышение привилегий через использование агентских инструментов — с конкретными мерами защиты.

## Связанные записи
- [[microsoft-agent-governance-toolkit]] ([Microsoft Agent Governance Toolkit](../tools/microsoft-agent-governance-toolkit.md))
- [[ai-agent-identity-iam-risks]] ([AI Agent Identity and IAM Risks](../concepts/ai-agent-identity-iam-risks.md))
- [[claude-code-permission-modes]] ([Claude Code Permission Modes](../tools/claude-code-permission-modes.md))
