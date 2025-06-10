# Claude Code Team Setup

## Key Sections:

### 1. User Management
- Three ways to set up Claude Code access:
  - Anthropic API via Anthropic Console
  - Amazon Bedrock
  - Google Vertex AI

### 2. Security Approach
- Strict read-only permissions by default
- Requires user approval for additional actions
- Supports fine-grained permissions configurable by organizations
- Protections against prompt injection and prompt fatigue

### 3. Data Flow and Dependencies
- Runs locally
- Sends data over network encrypted via TLS
- Supports authentication via multiple methods
- Connects to Statsig and Sentry for metrics/error logging
- Configurable telemetry and error reporting

### 4. Cost Management
- Charges by API token consumption
- Average cost ~$50-60/developer per month
- Can limit workspace spend

### 5. Best Practices for Organizations
- Create documentation (e.g. CLAUDE.md)
- Develop "one-click" installation
- Encourage gradual adoption
- Configure managed permissions
- Use Model Context Protocol (MCP)

### 6. FAQ Highlights
- Existing commercial agreements apply
- Does not train on user content by default
- Supports zero data retention keys

The documentation provides comprehensive guidance for teams implementing Claude Code, with a strong emphasis on security, flexibility, and controlled AI assistance.