# Claude Code Settings

## Key Highlights:
- Claude Code uses a `settings.json` file for configuration
- Settings can be configured at user, project, and enterprise levels
- Supports hierarchical settings with specific precedence order

## Settings File Locations:
- User settings: `~/.claude/settings.json`
- Project settings: 
  - Shared: `.claude/settings.json`
  - Local: `.claude/settings.local.json`
- Enterprise policies: 
  - macOS: `/Library/Application Support/ClaudeCode/policies.json`
  - Linux/Windows: `/etc/claude-code/policies.json`

## Example Settings Configuration:
```json
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl:*)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1"
  }
}
```

## Key Configuration Options:
- `apiKeyHelper`: Custom script for generating authentication
- `cleanupPeriodDays`: Retention period for chat transcripts
- `env`: Environment variables for sessions
- `includeCoAuthoredBy`: Toggle Claude byline in git commits
- `permissions`: Allow/deny rules for tool usage

## Permissions Support:
- Tool-specific permission rules
- Support for Bash, Read/Edit, WebFetch, and MCP tools
- Granular control over tool execution

## Environment Variables:
- Extensive list of configurable variables
- Control API keys, model selection, timeouts, and telemetry
- Options to disable auto-updates, error reporting, and more

## Terminal Optimization:
- Supports Bash, Zsh, and Fish shells
- Configurable line breaks and notifications
- Optional Vim mode keybindings

The documentation provides comprehensive guidance for configuring Claude Code to suit individual and organizational needs.