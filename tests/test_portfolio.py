from pathlib import Path

from agentic_use_cases import load_use_cases, rank_use_cases, score_use_case


def test_portfolio_ranking_returns_scale_candidate():
    rows = rank_use_cases(load_use_cases(Path("data/enterprise_agentic_use_cases.csv")))
    assert rows[0]["posture"] in {"scale-candidate", "priority-pilot"}
    assert rows[0]["net_score"] >= rows[-1]["net_score"]


def test_high_risk_low_reversibility_limits_autonomy():
    row = {
        "use_case": "Material action",
        "domain": "Finance",
        "business_value": "5",
        "workflow_leverage": "5",
        "context_readiness": "5",
        "evaluation_readiness": "5",
        "adoption_feasibility": "5",
        "reuse_potential": "5",
        "risk_exposure": "5",
        "reversibility": "1",
    }
    result = score_use_case(row)
    assert result["posture"] == "decision-support-only"
    assert result["recommended_autonomy"] == "L1 recommend"