# Claude Code SDK

The Claude Code SDK allows developers to programmatically integrate Claude Code into applications, enabling AI-powered coding assistance through command-line usage. Key features include:

## Authentication:
- Create an API key in the Anthropic Console
- Set the `ANTHROPIC_API_KEY` environment variable

## Basic Usage Examples:
```bash
# Run a single prompt
$ claude -p "Write a function to calculate Fibonacci numbers"

# Pipe input
$ echo "Explain this code" | claude -p

# Output in JSON format
$ claude -p "Generate a hello world function" --output-format json
```

## Advanced Capabilities:
- Multi-turn conversations
- Custom system prompts
- MCP (Model Context Protocol) configuration
- Flexible tool permissions
- Multiple output formats (text, JSON, streaming JSON)

## Key CLI Options:
- `--print/-p`: Non-interactive mode
- `--output-format`: Specify response format
- `--resume/-r`: Resume specific conversation
- `--continue/-c`: Continue most recent conversation
- `--system-prompt`: Override default system instructions
- `--mcp-config`: Load external tool configurations

The SDK supports programmatic integration, allowing developers to build sophisticated AI coding assistants with fine-grained control over Claude's behavior.