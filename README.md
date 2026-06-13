# Enterprise Agentic AI Use Cases

An executive-grade agentic AI use-case atlas for selecting, scoring, governing, and sequencing enterprise agent workflows.

## One-line value proposition

This repository helps AI leaders move from random agent ideas to a governed portfolio of high-value, risk-aware agentic AI opportunities.

## Business problem

Enterprises are excited about agentic AI, but many teams still select use cases based on novelty or executive enthusiasm. That creates fragmented pilots, uncontrolled tool access, weak governance, and unclear business outcomes. Senior leaders need a structured way to decide which agentic workflows deserve funding, which should remain decision support, and which should not be automated.

## Enterprise relevance

Agentic AI changes the risk profile of AI because systems can plan, call tools, and influence operational workflows. This repo frames agentic AI as an enterprise delivery portfolio: value, workflow leverage, autonomy level, context readiness, risk controls, and operating ownership must be evaluated together.

## Solution overview

The repository provides:

- A curated enterprise agentic AI use-case atlas
- A scoring model for value, readiness, risk, and reuse
- Risk-tier and autonomy recommendations
- Example portfolio data across operations, sales, procurement, IT, finance, and risk
- A small Python ranking engine to make the framework executable
- Documentation for architecture, governance, context, evaluation, and operating model choices

## Architecture / approach

```text
Use-case inventory -> Value/readiness/risk scoring -> Autonomy recommendation -> Governance controls -> Sequencing roadmap
```

The goal is not to prove agents can do everything. The goal is to show how a senior AI leader decides where agents should act, assist, or stay out of the workflow.

## Repository structure

```text
agentic_use_cases/       Scoring and portfolio ranking logic
data/                    Sample enterprise use-case portfolio
demo/                    Runnable ranking demo
docs/                    POV, architecture, business case, governance, roadmap
tests/                   Contract tests
.github/workflows/       CI workflow
```

## Setup and usage

```bash
python -m venv .venv
pip install -r requirements.txt
pytest -q
python demo/run_demo.py
```

Run the demo to see a ranked portfolio with recommended delivery posture: scale, pilot, incubate, or avoid automation.

## Featured guidance

- [Enterprise Agentic AI Adoption Playbook](docs/ENTERPRISE-AGENTIC-AI-ADOPTION-PLAYBOOK.md): 90-day model for moving agentic AI from pilot to governed adoption.

## Roadmap

- Add industry-specific agentic AI use-case packs
- Add HTML/Markdown portfolio report generation
- Add a decision matrix for autonomy levels L0-L5
- Add benchmark links to `agent-eval-harness`
- Add implementation patterns linked to `enterprise-agent-forge`