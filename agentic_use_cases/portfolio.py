from __future__ import annotations

import csv
from pathlib import Path


def _int(row: dict, key: str) -> int:
    return int(row[key])


def score_use_case(row: dict) -> dict:
    value = _int(row, "business_value")
    workflow = _int(row, "workflow_leverage")
    context = _int(row, "context_readiness")
    evaluation = _int(row, "evaluation_readiness")
    adoption = _int(row, "adoption_feasibility")
    reuse = _int(row, "reuse_potential")
    risk = _int(row, "risk_exposure")
    reversibility = _int(row, "reversibility")

    value_score = (0.28 * value) + (0.18 * workflow) + (0.16 * context) + (0.14 * evaluation) + (0.10 * adoption) + (0.14 * reuse)
    risk_penalty = (0.65 * risk) + (0.35 * (6 - reversibility))
    net_score = round(value_score - (0.30 * risk_penalty), 2)

    if risk >= 5 and reversibility <= 2:
        posture = "decision-support-only"
        autonomy = "L1 recommend"
    elif net_score >= 3.6 and risk <= 3:
        posture = "scale-candidate"
        autonomy = "L3 reversible execution"
    elif net_score >= 3.0:
        posture = "priority-pilot"
        autonomy = "L2 prepare with approval"
    elif context < 3 or evaluation < 3:
        posture = "incubate-foundation"
        autonomy = "L1 recommend"
    else:
        posture = "defer"
        autonomy = "L0 observe"

    return {
        **row,
        "net_score": net_score,
        "posture": posture,
        "recommended_autonomy": autonomy,
        "governance_control": governance_control(risk, reversibility),
    }


def governance_control(risk: int, reversibility: int) -> str:
    if risk >= 5 or reversibility <= 2:
        return "executive approval, audit trail, rollback/compensation plan, human execution"
    if risk >= 4:
        return "business owner approval, audit trail, post-action review"
    if risk >= 3:
        return "human approval or override, monitoring, sampled QA"
    return "standard monitoring and feedback loop"


def load_use_cases(path: str | Path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def rank_use_cases(rows: list[dict]) -> list[dict]:
    return sorted([score_use_case(row) for row in rows], key=lambda item: item["net_score"], reverse=True)