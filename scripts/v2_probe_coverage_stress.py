from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PAPER = ROOT / "paper"
CASES = DOCS / "deception_resistant_cases.csv"

FLOAT_FIELDS = [
    "leakage",
    "physical_probe",
    "deployment_shift",
    "causal_skill",
    "shortcut_strength",
    "deploy_success",
]


def load_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with CASES.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            parsed: dict[str, object] = dict(row)
            for field in FLOAT_FIELDS:
                parsed[field] = float(row[field])
            rows.append(parsed)
    return rows


def embodied_audit_pass(row: dict[str, object], probe_coupling: float) -> int:
    score = (
        0.70 * float(row["causal_skill"])
        + 0.12 * float(row["leakage"])
        + 0.08 * float(row["shortcut_strength"])
        - 0.44 * probe_coupling * float(row["physical_probe"]) * float(row["shortcut_strength"])
    )
    return int(score > 0.42)


def metrics(rows: list[dict[str, object]], probe_coupling: float) -> dict[str, float]:
    correct = 0
    false_cert = 0
    false_reject = 0
    shortcut_pass = 0
    robust_pass = 0
    shortcut_rows = [row for row in rows if row["policy_type"] == "shortcut"]
    robust_rows = [row for row in rows if row["policy_type"] == "robust"]
    deploy_fail = sum(1 for row in rows if int(row["deploy_success"]) == 0)
    deploy_success = sum(1 for row in rows if int(row["deploy_success"]) == 1)

    for row in rows:
        pred = embodied_audit_pass(row, probe_coupling)
        deploy = int(row["deploy_success"])
        correct += int(pred == deploy)
        false_cert += int(pred == 1 and deploy == 0)
        false_reject += int(pred == 0 and deploy == 1)
    for row in shortcut_rows:
        shortcut_pass += embodied_audit_pass(row, probe_coupling)
    for row in robust_rows:
        robust_pass += embodied_audit_pass(row, probe_coupling)

    return {
        "probe_coupling": probe_coupling,
        "certification_accuracy": correct / len(rows),
        "false_certification_rate": false_cert / deploy_fail,
        "false_rejection_rate": false_reject / deploy_success,
        "shortcut_pass_rate": shortcut_pass / len(shortcut_rows),
        "robust_pass_rate": robust_pass / len(robust_rows),
        "false_certifications": float(false_cert),
        "false_rejections": float(false_reject),
    }


def write_outputs(rows: list[dict[str, float]]) -> None:
    csv_path = DOCS / "v2_probe_coverage_stress.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        fields = [
            "probe_coupling",
            "certification_accuracy",
            "false_certification_rate",
            "false_rejection_rate",
            "shortcut_pass_rate",
            "robust_pass_rate",
            "false_certifications",
            "false_rejections",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    json_path = DOCS / "v2_probe_coverage_stress.json"
    json_path.write_text(json.dumps({"rows": rows}, indent=2), encoding="utf-8")

    table_lines = [
        r"\begin{tabular}{lrrrr}",
        r"\toprule",
        r"Probe coupling & Cert. acc. & False cert. & Shortcut pass & Robust pass \\",
        r"\midrule",
    ]
    for row in rows:
        table_lines.append(
            f"{row['probe_coupling']:.2f} & "
            f"{row['certification_accuracy']:.3f} & "
            f"{row['false_certification_rate']:.3f} & "
            f"{row['shortcut_pass_rate']:.3f} & "
            f"{row['robust_pass_rate']:.3f} \\\\"
        )
    table_lines.extend([r"\bottomrule", r"\end{tabular}"])
    (PAPER / "v2_probe_coverage_table.tex").write_text("\n".join(table_lines) + "\n", encoding="utf-8")


def main() -> None:
    rows = load_rows()
    stress = [metrics(rows, coupling) for coupling in [1.0, 0.75, 0.5, 0.25, 0.0]]
    write_outputs(stress)
    print(json.dumps({"rows": stress}, indent=2))


if __name__ == "__main__":
    main()
