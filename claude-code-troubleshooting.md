# Claude Code Troubleshooting

The page covers common issues developers might encounter when using Claude Code, organized into several key sections:

## 1. Common Installation Issues
- Focuses on Linux permission problems with npm global prefix
- Provides a recommended solution to create a user-writable npm directory
- Includes detailed recovery steps for system permission errors

## 2. Auto-Updater Issues
- Suggests fixing permission issues with npm global prefix
- Option to disable auto-updater by setting `DISABLE_AUTOUPDATER` environment variable

## 3. Permissions and Authentication
- Addresses repeated permission prompts
- Provides authentication troubleshooting steps like logging out and clearing authentication cache

## 4. Performance and Stability
- Offers guidance for high CPU/memory usage
- Recommends:
  - Using `/compact` to reduce context size
  - Restarting Claude Code between major tasks
  - Adding large build directories to `.gitignore`

## 5. Specific Technical Issues
- Troubleshooting command hangs/freezes
- Fixing ESC key issues in JetBrains IDEs

## 6. Getting More Help
- Use `/bug` command to report problems
- Check GitHub repository
- Run `/doctor` to check installation health

The documentation provides comprehensive, step-by-step guidance for resolving various technical challenges when using Claude Code.