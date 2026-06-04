# Context Engineering for Agentic AI Use Cases

Agents need workflow context, not just documents.

## Required context types

- User role and authority
- Current workflow state
- Available tools
- Policy constraints
- Customer, vendor, employee, or asset context
- Approval threshold
- Prior actions and audit history

## Checklist

- Is the source of truth named?
- Is the agent allowed to access this context?
- Is context fresh enough for action?
- What happens when context conflicts?
- Which context must be cited in the final recommendation?
- Which context should never enter model prompts?