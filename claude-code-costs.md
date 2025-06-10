# Claude Code Costs

The page focuses on managing and reducing token usage costs for Claude Code. Key points include:

## Cost Tracking Methods:
- Use `/cost` command to see current session usage
- Anthropic Console users can:
  - Check historical usage 
  - Set workspace spend limits
- Pro and Max plan users have usage included in subscription

## Cost Reduction Strategies:
- Use auto-compact feature when context exceeds 95% capacity
- Toggle auto-compact via `/config`
- Manually compact with `/compact` command
- Write specific, focused queries
- Break down complex tasks
- Clear conversation history between tasks

## Factors Affecting Costs:
- Codebase size
- Query complexity
- Number of files searched/modified
- Conversation history length
- Compaction frequency
- Background processes

## Background Token Usage:
- Haiku generation (≈1 cent/day)
- Conversation summarization
- Command processing

## Average Cost:
- $6 per developer per day
- 90% of users stay below $12 daily

Recommendation for team deployments: Start with a small pilot group to establish usage patterns.