# Claude Code IDE Integrations

Claude Code supports integrations with two major IDE families:
1. Visual Studio Code (including forks like Cursor and Windsurf)
2. JetBrains IDEs (PyCharm, WebStorm, IntelliJ, GoLand)

## Key Features:
- Quick launch with `Cmd+Esc` (Mac) or `Ctrl+Esc` (Windows/Linux)
- Diff viewing directly in the IDE
- Automatic sharing of current selection/tab context
- File reference shortcuts (`Cmd+Option+K` on Mac, `Alt+Ctrl+K` on Linux/Windows)
- Automatic sharing of diagnostic errors from the IDE

## Installation:
- VS Code: Run `claude` in the integrated terminal
- JetBrains: Install plugin from marketplace and restart IDE

## Configuration:
- Connect Claude Code to IDE by running `claude`
- Use `/config` command
- Set diff tool to `auto` for automatic IDE detection

Troubleshooting tips are provided for common installation and plugin issues, with recommendations to check terminal, permissions, and IDE settings.

The documentation emphasizes seamless integration to enhance coding workflow by leveraging Claude's capabilities directly within development environments.