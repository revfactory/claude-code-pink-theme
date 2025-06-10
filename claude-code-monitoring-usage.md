# Claude Code Monitoring Usage

## Key Points:
- OpenTelemetry support is currently in beta
- Enables metrics and events tracking for Claude Code usage
- Configurable through environment variables

## Quick Configuration Example:
```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
```

## Main Metrics Tracked:
1. Session count
2. Lines of code modified
3. Pull requests created
4. Git commits created
5. Cost of usage
6. Token usage
7. Code editing tool decisions

## Event Types:
- User prompt events
- Tool result events
- API request events
- API error events
- Tool decision events

## Configuration Options:
- Multiple export protocols (gRPC, HTTP)
- Configurable export intervals
- Optional authentication
- Cardinality control for metrics attributes

## Key Benefits:
- Monitor usage patterns
- Track productivity
- Analyze development workflows
- Manage costs
- Troubleshoot API interactions

## Important Notes:
- Telemetry is opt-in
- Sensitive information is not logged
- Cost metrics are approximations

Administrators can centrally configure settings via a managed settings file on macOS and Linux systems.