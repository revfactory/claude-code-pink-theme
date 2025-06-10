# Claude Code GitHub Actions

## Claude Code GitHub Actions Overview:
- Enables AI-powered automation in GitHub workflows
- Allows using `@claude` mentions in PRs and issues to:
  - Create pull requests
  - Implement features
  - Fix bugs
  - Follow project standards

## Key Features:
- Instant PR creation
- Automated code implementation
- Respects project guidelines via `CLAUDE.md`
- Simple setup
- Secure execution on GitHub runners

## Setup Methods:
### 1. Quick Terminal Setup:
- Run `/install-github-app` command
- Requires repository admin access

### 2. Manual Setup:
- Install Claude GitHub App
- Add `ANTHROPIC_API_KEY` to repository secrets
- Copy workflow configuration file

## Use Cases:
- Turn issues into PRs
- Get implementation guidance
- Quickly fix bugs

## Best Practices:
- Create `CLAUDE.md` for project standards
- Use GitHub Secrets for API keys
- Review suggestions before merging
- Optimize performance with issue templates

## Cloud Provider Integration:
- Supports AWS Bedrock and Google Vertex AI
- Requires specific authentication configurations
- Enables enterprise-level control and security

## Costs Considerations:
- Consumes GitHub Actions minutes
- API token usage varies by task complexity
- Recommended to use specific commands and set iteration limits

The documentation provides detailed, step-by-step guidance for implementing Claude Code GitHub Actions across different environments and use cases.