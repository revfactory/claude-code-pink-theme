# Claude Code CLI Usage and Controls

## Key Sections:

### 1. Getting Started
- Two main interaction modes:
  - Interactive mode: Run `claude`
  - One-shot mode: Use `claude -p "query"`

### 2. CLI Commands
- Basic commands include:
  - `claude`: Start interactive REPL
  - `claude -p "query"`: Run one-off query
  - `claude -c`: Continue most recent conversation
  - `claude update`: Update to latest version

### 3. CLI Flags
Important flags include:
- `--print` or `-p`: Print response without interactive mode
- `--output-format`: Specify response format (text, json, stream-json)
- `--verbose`: Enable detailed logging
- `--model`: Set specific AI model
- `--max-turns`: Limit agentic turns

### 4. Slash Commands
Useful interactive session commands:
- `/bug`: Report bugs
- `/clear`: Clear conversation history
- `/config`: View/modify configuration
- `/help`: Get usage help
- `/memory`: Edit memory files
- `/model`: Change AI model
- `/review`: Request code review

### 5. Special Shortcuts
- Quick memory with `#`
- Multiline input using `\` or Option/Shift+Enter
- Vim mode with `/vim`

The documentation provides comprehensive guidance for developers using Claude Code's command-line interface.