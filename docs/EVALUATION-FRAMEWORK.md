# Evaluation Framework

Agentic AI use cases should be evaluated beyond answer quality.

## Metrics

| Dimension | Metric |
| --- | --- |
| Task success | Workflow completed or recommendation accepted |
| Evidence quality | Decision supported by correct context |
| Approval compliance | Required human approval followed |
| Tool safety | Tool calls within authority and scope |
| Latency | Fits workflow time tolerance |
| Cost | Unit economics acceptable |
| Rework | Human correction effort reduced |
| Incident risk | Failure detectable and reversible |

## Hard gates

- Tool call outside authority
- Missing approval for high-risk action
- Sensitive data exposure
- Unsupported material recommendation
- No rollback path for executed action