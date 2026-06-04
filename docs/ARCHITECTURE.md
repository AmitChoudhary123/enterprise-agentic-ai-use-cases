# Architecture

This repository models agentic AI use-case selection as a portfolio architecture problem.

```text
Use-case data -> Scoring model -> Risk/autonomy rules -> Governance controls -> Portfolio roadmap
```

## Components

- `data/enterprise_agentic_use_cases.csv`: sample enterprise use-case inventory
- `agentic_use_cases/portfolio.py`: scoring and governance recommendation logic
- `demo/run_demo.py`: ranked portfolio demo
- `docs/`: executive guidance for architecture, governance, operating model, and evaluation

## Design principle

Autonomy is an architectural decision. It should be based on business value, workflow leverage, context readiness, evaluation readiness, risk exposure, and reversibility.