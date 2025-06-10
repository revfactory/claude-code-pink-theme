# Claude Code Getting Started

## System Requirements:
- Operating Systems: macOS 10.15+, Ubuntu 20.04+/Debian 10+, Windows via WSL
- Hardware: Minimum 4GB RAM
- Software: 
  - Node.js 18+
  - Optional: git 2.23+, GitHub/GitLab CLI, ripgrep
- Requires internet connection
- Available only in supported countries

## Installation Steps:
1. Install NodeJS 18+
2. Run: `npm install -g @anthropic-ai/claude-code`
3. Navigate to project directory
4. Start Claude Code by running `claude`
5. Complete authentication through:
   - Anthropic Console (default)
   - Claude App (Pro/Max plan)
   - Enterprise platforms like Amazon Bedrock or Google Vertex AI

## First-Time User Recommendations:
1. Start Claude Code
2. Run a simple command like `summarize this project`
3. Generate a CLAUDE.md project guide using `/init`
4. Commit the generated CLAUDE.md file

The documentation includes troubleshooting tips for WSL installation and emphasizes not using `sudo` during installation to avoid permission issues.