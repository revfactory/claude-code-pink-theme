# Claude Code Security

Claude Code uses a tiered permission system to manage security and access to various tools. The key security features include:

## Permission Levels:
- Read-only tools (like file reads, LS, Grep) require no approval
- Bash commands and file modifications require explicit approval
- Some tools like WebFetch and WebSearch need permission before use

## Prompt Injection Protection:
- Implements a multi-layered security approach including:
  - Permission system requiring explicit approvals
  - Context-aware analysis of requests
  - Input sanitization
  - Command blocklist to prevent risky web fetches

## Network Access:
- Requires access to specific domains:
  - api.anthropic.com
  - statsig.anthropic.com
  - sentry.io

## Development Container Security:
- Provides a secure container configuration with:
  - Precise network access control
  - Default-deny network policy
  - Startup verification of firewall rules
  - Isolation from main system

## Best Practices Recommended:
- Review suggested commands before approval
- Avoid piping untrusted content
- Verify proposed file changes
- Report suspicious behavior

The documentation emphasizes that while these protections significantly reduce risks, "no system is completely immune to all attacks."