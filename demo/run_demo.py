from pathlib import Path

from agentic_use_cases import load_use_cases, rank_use_cases

if __name__ == "__main__":
    rows = rank_use_cases(load_use_cases(Path("data/enterprise_agentic_use_cases.csv")))
    print("Enterprise Agentic AI Use-Case Portfolio")
    print("========================================")
    for item in rows:
        print(
            f"{item['net_score']:.2f} | {item['posture']:<22} | "
            f"{item['recommended_autonomy']:<24} | {item['use_case']}"
        )