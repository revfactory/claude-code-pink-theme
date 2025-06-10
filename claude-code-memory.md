# Claude Code Memory Management

Claude Code offers three types of memory locations:

## 1. Project Memory (`./CLAUDE.md`):
- Team-shared instructions for the project
- Examples: Project architecture, coding standards, workflows

## 2. User Memory (`~/.claude/CLAUDE.md`):
- Personal preferences across all projects
- Examples: Code styling preferences, tooling shortcuts

## 3. Project Memory (Local) - Deprecated:
- Previously for personal project-specific preferences

## Key Features:
- Memory files are automatically loaded when Claude Code launches
- Supports file imports using `@path/to/import` syntax
- Recursive memory lookup from current working directory up to root
- Maximum import depth of 5 hops

## Memory Management Methods:
- Quick memory addition using `#` prefix
- Use `/memory` command to edit memory files in system editor

## Best Practices:
- Be specific in memory instructions
- Use structured markdown
- Periodically review and update memories

The documentation provides guidance on effectively using and managing Claude Code's memory across different project and personal contexts.