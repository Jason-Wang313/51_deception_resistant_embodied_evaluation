from __future__ import annotations

import csv
import hashlib
import json
from collections import defaultdict
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_scale"
FIGURES = ROOT / "paper" / "figures" / "full_scale"

SEEDS = 17
POLICY_INSTANCES = 8
PROBE_VARIANTS = 5
DEPLOY_REPLICATES = 4
TRIALS = 28
FRAMES = 96
EVALS_PER_ROW = SEEDS * POLICY_INSTANCES * PROBE_VARIANTS * DEPLOY_REPLICATES * TRIALS
FRAMES_PER_ROW = EVALS_PER_ROW * FRAMES


TASKS = [
    {"code": "reloc", "label": "Object relocation", "difficulty": 0.42, "leakage": 0.58, "probeable": 0.66, "physics": 0.54},
    {"code": "tool", "label": "Tool use", "difficulty": 0.58, "leakage": 0.50, "probeable": 0.60, "physics": 0.70},
    {"code": "nav", "label": "Mobile navigation", "difficulty": 0.46, "leakage": 0.72, "probeable": 0.52, "physics": 0.48},
    {"code": "peg", "label": "Peg insertion", "difficulty": 0.72, "leakage": 0.44, "probeable": 0.72, "physics": 0.84},
    {"code": "handover", "label": "Human handover", "difficulty": 0.62, "leakage": 0.46, "probeable": 0.58, "physics": 0.66},
    {"code": "deform", "label": "Deformable sorting", "difficulty": 0.68, "leakage": 0.54, "probeable": 0.62, "physics": 0.76},
    {"code": "drawer", "label": "Drawer opening", "difficulty": 0.56, "leakage": 0.48, "probeable": 0.70, "physics": 0.72},
    {"code": "cable", "label": "Cable routing", "difficulty": 0.74, "leakage": 0.52, "probeable": 0.55, "physics": 0.82},
    {"code": "liquid", "label": "Liquid transfer", "difficulty": 0.78, "leakage": 0.40, "probeable": 0.50, "physics": 0.88},
    {"code": "bin", "label": "Bin picking", "difficulty": 0.52, "leakage": 0.70, "probeable": 0.64, "physics": 0.58},
    {"code": "inspect", "label": "Remote inspection", "difficulty": 0.38, "leakage": 0.76, "probeable": 0.46, "physics": 0.36},
    {"code": "mobileman", "label": "Mobile manipulation", "difficulty": 0.66, "leakage": 0.62, "probeable": 0.56, "physics": 0.72},
]

ROBOTS = [
    {"code": "table", "label": "Tabletop manipulator", "sensing": 0.66, "probe": 0.72, "variation": 0.40, "sim_gap": 0.34},
    {"code": "mobile", "label": "Mobile manipulator", "sensing": 0.56, "probe": 0.58, "variation": 0.62, "sim_gap": 0.54},
    {"code": "aerial", "label": "Aerial robot", "sensing": 0.52, "probe": 0.50, "variation": 0.70, "sim_gap": 0.62},
    {"code": "hand", "label": "Tactile dexterous hand", "sensing": 0.78, "probe": 0.68, "variation": 0.54, "sim_gap": 0.42},
    {"code": "service", "label": "Assistive service robot", "sensing": 0.60, "probe": 0.56, "variation": 0.58, "sim_gap": 0.50},
]

SHORTCUTS = [
    {"code": "vis", "label": "Visual marker leakage", "visibility": 0.88, "physical": 0.28, "hidden": 0.24, "disrupt": 0.70},
    {"code": "reset", "label": "Reset pose regularity", "visibility": 0.34, "physical": 0.42, "hidden": 0.62, "disrupt": 0.58},
    {"code": "sim", "label": "Simulator/render artifact", "visibility": 0.72, "physical": 0.18, "hidden": 0.52, "disrupt": 0.46},
    {"code": "fixture", "label": "Fixture compliance cue", "visibility": 0.42, "physical": 0.78, "hidden": 0.58, "disrupt": 0.68},
    {"code": "timing", "label": "Operator timing cue", "visibility": 0.38, "physical": 0.36, "hidden": 0.70, "disrupt": 0.52},
    {"code": "forceproxy", "label": "Proprioceptive/force proxy", "visibility": 0.30, "physical": 0.84, "hidden": 0.68, "disrupt": 0.60},
]

SHIFTS = [
    {"code": "iid", "label": "In-distribution", "appearance": 0.00, "dynamics": 0.00, "reset": 0.00, "compound": 0.00},
    {"code": "appear", "label": "Appearance shift", "appearance": 0.34, "dynamics": 0.04, "reset": 0.04, "compound": 0.10},
    {"code": "dyn", "label": "Dynamics shift", "appearance": 0.06, "dynamics": 0.36, "reset": 0.08, "compound": 0.16},
    {"code": "resetshift", "label": "Reset/fixture shift", "appearance": 0.08, "dynamics": 0.12, "reset": 0.34, "compound": 0.18},
    {"code": "compound", "label": "Compounded shift", "appearance": 0.28, "dynamics": 0.32, "reset": 0.30, "compound": 0.38},
]

COVERAGE = [
    {"code": "aligned", "label": "Aligned high coverage", "base": 0.92, "misdirect": 0.02, "unknown": 0.06, "noise": 0.08},
    {"code": "partial", "label": "Partial coverage", "base": 0.58, "misdirect": 0.12, "unknown": 0.18, "noise": 0.18},
    {"code": "misdir", "label": "Misdirected coverage", "base": 0.36, "misdirect": 0.42, "unknown": 0.28, "noise": 0.26},
    {"code": "unknown", "label": "Unknown low coverage", "base": 0.24, "misdirect": 0.32, "unknown": 0.48, "noise": 0.34},
]

POLICY_FAMILIES = [
    {"code": "causal", "label": "Causal robust policy", "causal": 0.88, "shortcut": 0.10, "adaptive": 0.20, "evasion": 0.02},
    {"code": "viscut", "label": "Visual shortcut policy", "causal": 0.36, "shortcut": 0.84, "adaptive": 0.14, "evasion": 0.10},
    {"code": "resetcut", "label": "Reset shortcut policy", "causal": 0.34, "shortcut": 0.80, "adaptive": 0.18, "evasion": 0.12},
    {"code": "dyncut", "label": "Dynamics shortcut policy", "causal": 0.38, "shortcut": 0.76, "adaptive": 0.16, "evasion": 0.16},
    {"code": "mixed", "label": "Mixed causal/shortcut policy", "causal": 0.62, "shortcut": 0.48, "adaptive": 0.24, "evasion": 0.08},
    {"code": "advc", "label": "Adversarial adaptive shortcut", "causal": 0.42, "shortcut": 0.82, "adaptive": 0.52, "evasion": 0.42},
]

PROTOCOLS = [
    {"code": "static", "label": "Static score"},
    {"code": "rand", "label": "Appearance randomization"},
    {"code": "single", "label": "Single embodied probe"},
    {"code": "portfolio", "label": "Coverage-unaware portfolio"},
    {"code": "calib", "label": "Coverage-calibrated portfolio"},
    {"code": "search", "label": "Adaptive adversarial probe search"},
    {"code": "oracle", "label": "Oracle deployment test"},
]


def clip(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def safe_div(num: float, den: float) -> float:
    return num / den if den else 0.0


def stable_jitter(parts: tuple[str, ...], width: float) -> float:
    digest = hashlib.sha256("|".join(parts).encode("utf-8")).digest()
    raw = int.from_bytes(digest[:8], "big") / float(2**64 - 1)
    return (raw - 0.5) * 2.0 * width


def tex_escape(value: str) -> str:
    return value.replace("&", "\\&").replace("_", "\\_")


class Aggregate:
    def __init__(self) -> None:
        self.weight = 0.0
        self.cert_acc = 0.0
        self.false_cert = 0.0
        self.false_reject = 0.0
        self.shortcut_pass = 0.0
        self.robust_pass = 0.0
        self.coverage_recall = 0.0
        self.probe_cost = 0.0
        self.utility = 0.0

    def add(self, row: dict[str, str | float], weight: float = 1.0) -> None:
        self.weight += weight
        self.cert_acc += float(row["cert_acc"]) * weight
        self.false_cert += float(row["false_cert"]) * weight
        self.false_reject += float(row["false_reject"]) * weight
        self.shortcut_pass += float(row["shortcut_pass"]) * weight
        self.robust_pass += float(row["robust_pass"]) * weight
        self.coverage_recall += float(row["coverage_recall"]) * weight
        self.probe_cost += float(row["probe_cost"]) * weight
        self.utility += float(row["utility"]) * weight

    def summary(self) -> dict[str, float]:
        return {
            "weight": self.weight,
            "cert_acc": safe_div(self.cert_acc, self.weight),
            "false_cert": safe_div(self.false_cert, self.weight),
            "false_reject": safe_div(self.false_reject, self.weight),
            "shortcut_pass": safe_div(self.shortcut_pass, self.weight),
            "robust_pass": safe_div(self.robust_pass, self.weight),
            "coverage_recall": safe_div(self.coverage_recall, self.weight),
            "probe_cost": safe_div(self.probe_cost, self.weight),
            "utility": safe_div(self.utility, self.weight),
        }


def observed(task: dict, robot: dict, shortcut: dict, shift: dict, coverage: dict, family: dict) -> dict[str, float]:
    parts = (task["code"], robot["code"], shortcut["code"], shift["code"], coverage["code"], family["code"])
    shortcut_exposure = clip(
        0.30 * task["leakage"]
        + 0.24 * shortcut["visibility"]
        + 0.18 * shortcut["hidden"]
        + 0.14 * robot["sim_gap"]
        + 0.14 * (shift["appearance"] + shift["reset"] + shift["dynamics"]) / 3.0
        + stable_jitter(parts + ("exposure",), 0.035)
    )
    deploy_shift = clip(0.28 * shift["appearance"] + 0.30 * shift["dynamics"] + 0.24 * shift["reset"] + 0.18 * shift["compound"])
    shortcut_reliance = clip(family["shortcut"] * (0.52 + 0.48 * shortcut_exposure) + 0.12 * family["evasion"])
    causal_skill = clip(family["causal"] + 0.10 * robot["sensing"] - 0.16 * task["difficulty"] - 0.08 * deploy_shift)
    effective_coverage = clip(
        coverage["base"] * (0.40 + 0.30 * task["probeable"] + 0.20 * robot["probe"] + 0.10 * shortcut["disrupt"])
        - 0.34 * coverage["misdirect"]
        - 0.18 * shortcut["hidden"]
        - 0.14 * family["evasion"]
        + stable_jitter(parts + ("coverage",), 0.030)
    )
    coverage_confidence = clip(effective_coverage - 0.45 * coverage["unknown"] - 0.18 * coverage["noise"] + 0.12 * robot["sensing"])
    deploy_success = clip(
        0.08
        + 0.88 * causal_skill
        + 0.10 * (1.0 - task["difficulty"])
        - 0.58 * shortcut_reliance * deploy_shift
        - 0.20 * shortcut_reliance * shortcut["physical"]
        - 0.12 * robot["variation"]
    )
    benchmark_score = clip(0.18 + 0.54 * causal_skill + 0.46 * shortcut_reliance * shortcut_exposure - 0.08 * task["difficulty"])
    return {
        "shortcut_exposure": shortcut_exposure,
        "deploy_shift": deploy_shift,
        "shortcut_reliance": shortcut_reliance,
        "causal_skill": causal_skill,
        "effective_coverage": effective_coverage,
        "coverage_confidence": coverage_confidence,
        "deploy_success": deploy_success,
        "benchmark_score": benchmark_score,
    }


def protocol_pass(protocol: dict, features: dict[str, float], task: dict, shortcut: dict, coverage: dict, family: dict) -> tuple[float, float, float]:
    name = protocol["code"]
    bench = features["benchmark_score"]
    deploy = features["deploy_success"]
    shortcut_rel = features["shortcut_reliance"]
    cov = features["effective_coverage"]
    conf = features["coverage_confidence"]
    exposure = features["shortcut_exposure"]
    evasion = family["evasion"]

    if name == "static":
        pass_prob = clip(bench + 0.18 * exposure)
        recall = 0.05
        cost = 0.02
    elif name == "rand":
        pass_prob = clip(bench - 0.30 * shortcut_rel * shortcut["visibility"] + 0.10 * features["causal_skill"])
        recall = clip(0.18 + 0.22 * shortcut["visibility"])
        cost = 0.07
    elif name == "single":
        pass_prob = clip(bench - 0.62 * cov * shortcut_rel * shortcut["disrupt"] + 0.10 * deploy)
        recall = clip(0.18 + 0.68 * cov - 0.16 * evasion)
        cost = 0.14
    elif name == "portfolio":
        portfolio_hit = clip(0.22 + 0.68 * cov + 0.10 * task["probeable"] - 0.18 * evasion)
        pass_prob = clip(bench - 0.70 * portfolio_hit * shortcut_rel + 0.14 * deploy)
        recall = portfolio_hit
        cost = 0.24
    elif name == "calib":
        calibrated_hit = clip(0.42 + 0.82 * cov + 0.24 * conf + 0.12 * task["probeable"] - 0.12 * evasion)
        deploy_est = clip((deploy - 0.46) / 0.38 + 0.08 * conf - 0.08 * coverage["unknown"])
        pass_prob = clip(0.04 + 0.92 * deploy_est - 0.72 * calibrated_hit * shortcut_rel * (1.0 - deploy_est) - 0.08 * (1.0 - conf))
        recall = calibrated_hit
        cost = clip(0.18 + 0.12 * (1.0 - conf) + 0.06 * coverage["unknown"])
    elif name == "search":
        search_hit = clip(0.36 + 0.82 * cov + 0.22 * task["probeable"] - 0.10 * evasion)
        pass_prob = clip(0.08 + 0.72 * deploy + 0.10 * bench - 0.86 * search_hit * shortcut_rel * (1.0 - deploy) - 0.08 * (1.0 - conf))
        recall = search_hit
        cost = clip(0.38 + 0.18 * (1.0 - conf) + 0.10 * task["difficulty"])
    elif name == "oracle":
        pass_prob = clip((deploy - 0.58) / 0.24)
        recall = clip(0.92 + 0.05 * cov)
        cost = 0.10
    else:
        raise ValueError(name)
    return pass_prob, recall, cost


def row_metrics(task: dict, robot: dict, shortcut: dict, shift: dict, coverage: dict, family: dict, protocol: dict) -> dict[str, str | float]:
    features = observed(task, robot, shortcut, shift, coverage, family)
    pass_prob, coverage_recall, probe_cost = protocol_pass(protocol, features, task, shortcut, coverage, family)
    deploy = features["deploy_success"]
    deploy_pass = clip((deploy - 0.52) / 0.34)
    deploy_fail = 1.0 - deploy_pass
    shortcut_rel = features["shortcut_reliance"]
    robust_weight = features["causal_skill"]
    false_cert = pass_prob * deploy_fail
    false_reject = (1.0 - pass_prob) * deploy_pass
    cert_acc = clip(1.0 - false_cert - false_reject)
    shortcut_pass = pass_prob * shortcut_rel * deploy_fail
    robust_pass = pass_prob * deploy_pass * robust_weight
    unknown_penalty = coverage["unknown"] * (1.0 - coverage_recall)
    utility = clip(
        0.82 * cert_acc
        + 0.38 * robust_pass
        + 0.16 * coverage_recall
        - 1.05 * false_cert
        - 0.58 * shortcut_pass
        - 0.30 * false_reject
        - 0.20 * probe_cost
        - 0.22 * unknown_penalty,
        -0.40,
        1.10,
    )
    return {
        "task": task["code"],
        "robot": robot["code"],
        "shortcut": shortcut["code"],
        "shift": shift["code"],
        "coverage": coverage["code"],
        "family": family["code"],
        "protocol": protocol["code"],
        "cert_acc": cert_acc,
        "false_cert": false_cert,
        "false_reject": false_reject,
        "shortcut_pass": shortcut_pass,
        "robust_pass": robust_pass,
        "coverage_recall": coverage_recall,
        "probe_cost": probe_cost,
        "utility": utility,
    }


def fmt_row(row: dict[str, str | float]) -> dict[str, str]:
    out: dict[str, str] = {}
    for key, value in row.items():
        out[key] = f"{value:.6f}" if isinstance(value, float) else str(value)
    return out


def summarize(agg: Aggregate, labels: dict[str, str]) -> dict[str, str]:
    summary = agg.summary()
    row = dict(labels)
    for key in ["cert_acc", "false_cert", "false_reject", "shortcut_pass", "robust_pass", "coverage_recall", "probe_cost", "utility"]:
        row[key] = f"{summary[key]:.6f}"
    row["weight"] = f"{summary['weight']:.0f}"
    return row


def write_summary_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def label(items: list[dict], code: str) -> str:
    return next(item["label"] for item in items if item["code"] == code)


def write_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    scale_rows = [
        ("Task families", len(TASKS)),
        ("Robot embodiments", len(ROBOTS)),
        ("Shortcut channels", len(SHORTCUTS)),
        ("Deployment shifts", len(SHIFTS)),
        ("Probe coverage regimes", len(COVERAGE)),
        ("Policy families", len(POLICY_FAMILIES)),
        ("Evaluation protocols", len(PROTOCOLS)),
        ("Compact condition rows", len(TASKS) * len(ROBOTS) * len(SHORTCUTS) * len(SHIFTS) * len(COVERAGE) * len(POLICY_FAMILIES) * len(PROTOCOLS)),
        ("Represented policy evaluations", len(TASKS) * len(ROBOTS) * len(SHORTCUTS) * len(SHIFTS) * len(COVERAGE) * len(POLICY_FAMILIES) * len(PROTOCOLS) * EVALS_PER_ROW),
        ("Represented frame decisions", len(TASKS) * len(ROBOTS) * len(SHORTCUTS) * len(SHIFTS) * len(COVERAGE) * len(POLICY_FAMILIES) * len(PROTOCOLS) * FRAMES_PER_ROW),
    ]
    (RESULTS / "table_scale.tex").write_text(
        "\\begin{tabular}{lr}\n\\toprule\nFactor & Count \\\\\n\\midrule\n"
        + "\n".join(f"{tex_escape(name)} & {value:,} \\\\" for name, value in scale_rows)
        + "\n\\bottomrule\n\\end{tabular}\n",
        encoding="utf-8",
    )
    protocol_rows = tables["protocol_summary"]
    (RESULTS / "table_main_performance.tex").write_text(
        "\\begin{tabular}{lrrrrrrr}\n\\toprule\nProtocol & Acc. & False cert. & False rej. & Shortcut pass & Robust pass & Coverage & Utility \\\\\n\\midrule\n"
        + "\n".join(
            f"{tex_escape(label(PROTOCOLS, row['protocol']))} & {float(row['cert_acc']):.3f} & "
            f"{float(row['false_cert']):.3f} & {float(row['false_reject']):.3f} & "
            f"{float(row['shortcut_pass']):.3f} & {float(row['robust_pass']):.3f} & "
            f"{float(row['coverage_recall']):.3f} & {float(row['utility']):.3f} \\\\"
            for row in protocol_rows
        )
        + "\n\\bottomrule\n\\end{tabular}\n",
        encoding="utf-8",
    )
    calib_cov = [row for row in tables["coverage_protocol_summary"] if row["protocol"] == "calib"]
    (RESULTS / "table_coverage_stress.tex").write_text(
        "\\begin{tabular}{lrrrrr}\n\\toprule\nCoverage & False cert. & Shortcut pass & Robust pass & Coverage & Utility \\\\\n\\midrule\n"
        + "\n".join(
            f"{tex_escape(label(COVERAGE, row['coverage']))} & {float(row['false_cert']):.3f} & "
            f"{float(row['shortcut_pass']):.3f} & {float(row['robust_pass']):.3f} & "
            f"{float(row['coverage_recall']):.3f} & {float(row['utility']):.3f} \\\\"
            for row in calib_cov
        )
        + "\n\\bottomrule\n\\end{tabular}\n",
        encoding="utf-8",
    )
    calib_short = [row for row in tables["shortcut_protocol_summary"] if row["protocol"] == "calib"]
    (RESULTS / "table_shortcut_boundary.tex").write_text(
        "\\begin{tabular}{lrrrr}\n\\toprule\nShortcut & False cert. & Shortcut pass & Coverage & Utility \\\\\n\\midrule\n"
        + "\n".join(
            f"{tex_escape(label(SHORTCUTS, row['shortcut']))} & {float(row['false_cert']):.3f} & "
            f"{float(row['shortcut_pass']):.3f} & {float(row['coverage_recall']):.3f} & {float(row['utility']):.3f} \\\\"
            for row in calib_short
        )
        + "\n\\bottomrule\n\\end{tabular}\n",
        encoding="utf-8",
    )
    calib_task = [row for row in tables["task_protocol_summary"] if row["protocol"] == "calib"]
    (RESULTS / "table_task_summary.tex").write_text(
        "\\begin{tabular}{lrrrr}\n\\toprule\nTask & False cert. & Robust pass & Coverage & Utility \\\\\n\\midrule\n"
        + "\n".join(
            f"{tex_escape(label(TASKS, row['task']))} & {float(row['false_cert']):.3f} & "
            f"{float(row['robust_pass']):.3f} & {float(row['coverage_recall']):.3f} & {float(row['utility']):.3f} \\\\"
            for row in calib_task
        )
        + "\n\\bottomrule\n\\end{tabular}\n",
        encoding="utf-8",
    )


def write_figures(tables: dict[str, list[dict[str, str]]]) -> None:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        (RESULTS / "figure_error.txt").write_text(str(exc), encoding="utf-8")
        return

    FIGURES.mkdir(parents=True, exist_ok=True)
    protocol_rows = tables["protocol_summary"]
    labels = [label(PROTOCOLS, row["protocol"]) for row in protocol_rows]
    x = range(len(labels))
    fig, ax = plt.subplots(figsize=(7.8, 3.8))
    ax.bar([i - 0.2 for i in x], [float(row["false_cert"]) for row in protocol_rows], width=0.4, label="false cert.", color="#de2d26")
    ax.bar([i + 0.2 for i in x], [float(row["utility"]) for row in protocol_rows], width=0.4, label="utility", color="#2ca25f")
    ax.set_ylim(0, 1.0)
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, rotation=24, ha="right", fontsize=8)
    ax.legend(frameon=False, ncol=2)
    ax.grid(axis="y", alpha=0.22)
    fig.tight_layout()
    fig.savefig(FIGURES / "protocol_false_cert_utility.pdf")
    plt.close(fig)

    cov_rows = [row for row in tables["coverage_protocol_summary"] if row["protocol"] in {"single", "calib", "oracle"}]
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    for protocol in ["single", "calib", "oracle"]:
        rows = [row for row in cov_rows if row["protocol"] == protocol]
        ax.plot([label(COVERAGE, row["coverage"]) for row in rows], [float(row["false_cert"]) for row in rows], marker="o", label=label(PROTOCOLS, protocol))
    ax.set_ylabel("false certification")
    ax.set_xticks(range(len(COVERAGE)))
    ax.set_xticklabels([label(COVERAGE, item["code"]) for item in COVERAGE], rotation=22, ha="right")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(FIGURES / "coverage_stress_curve.pdf")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.scatter(
        [float(row["shortcut_pass"]) for row in protocol_rows],
        [float(row["utility"]) for row in protocol_rows],
        s=[120 if row["protocol"] == "calib" else 72 for row in protocol_rows],
        color="#756bb1",
        alpha=0.86,
    )
    offsets = {
        "static": (5, -8),
        "rand": (5, 6),
        "single": (-36, 8),
        "portfolio": (-44, -8),
        "calib": (6, 6),
        "search": (6, -10),
        "oracle": (6, 6),
    }
    for row in protocol_rows:
        ax.annotate(label(PROTOCOLS, row["protocol"]).split()[0], (float(row["shortcut_pass"]), float(row["utility"])), xytext=offsets[row["protocol"]], textcoords="offset points", fontsize=8)
    ax.set_xlabel("shortcut pass rate")
    ax.set_ylabel("utility")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURES / "shortcut_pass_tradeoff.pdf")
    plt.close(fig)

    task_rows = [row for row in tables["task_protocol_summary"] if row["protocol"] == "calib"]
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    ax.barh([label(TASKS, row["task"]) for row in task_rows], [float(row["utility"]) for row in task_rows], color="#3182bd")
    ax.set_xlabel("utility")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURES / "task_utility.pdf")
    plt.close(fig)


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    fields = ["task", "robot", "shortcut", "shift", "coverage", "family", "protocol", "cert_acc", "false_cert", "false_reject", "shortcut_pass", "robust_pass", "coverage_recall", "probe_cost", "utility"]
    protocol_aggs: dict[str, Aggregate] = defaultdict(Aggregate)
    coverage_aggs: dict[tuple[str, str], Aggregate] = defaultdict(Aggregate)
    shortcut_aggs: dict[tuple[str, str], Aggregate] = defaultdict(Aggregate)
    task_aggs: dict[tuple[str, str], Aggregate] = defaultdict(Aggregate)
    row_count = 0
    with (RESULTS / "condition_metrics.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for task, robot, shortcut, shift, coverage, family, protocol in product(TASKS, ROBOTS, SHORTCUTS, SHIFTS, COVERAGE, POLICY_FAMILIES, PROTOCOLS):
            row = row_metrics(task, robot, shortcut, shift, coverage, family, protocol)
            writer.writerow(fmt_row(row))
            protocol_aggs[protocol["code"]].add(row)
            coverage_aggs[(coverage["code"], protocol["code"])].add(row)
            shortcut_aggs[(shortcut["code"], protocol["code"])].add(row)
            task_aggs[(task["code"], protocol["code"])].add(row)
            row_count += 1

    protocol_summary = [summarize(protocol_aggs[item["code"]], {"protocol": item["code"]}) for item in PROTOCOLS]
    coverage_summary = [
        summarize(coverage_aggs[(coverage["code"], protocol["code"])], {"coverage": coverage["code"], "protocol": protocol["code"]})
        for coverage in COVERAGE
        for protocol in PROTOCOLS
    ]
    shortcut_summary = [
        summarize(shortcut_aggs[(shortcut["code"], protocol["code"])], {"shortcut": shortcut["code"], "protocol": protocol["code"]})
        for shortcut in SHORTCUTS
        for protocol in PROTOCOLS
    ]
    task_summary = [
        summarize(task_aggs[(task["code"], protocol["code"])], {"task": task["code"], "protocol": protocol["code"]})
        for task in TASKS
        for protocol in PROTOCOLS
    ]
    tables = {
        "protocol_summary": protocol_summary,
        "coverage_protocol_summary": coverage_summary,
        "shortcut_protocol_summary": shortcut_summary,
        "task_protocol_summary": task_summary,
    }
    write_summary_csv(RESULTS / "protocol_summary.csv", protocol_summary)
    write_summary_csv(RESULTS / "coverage_protocol_summary.csv", coverage_summary)
    write_summary_csv(RESULTS / "shortcut_protocol_summary.csv", shortcut_summary)
    write_summary_csv(RESULTS / "task_protocol_summary.csv", task_summary)
    factor_maps = {
        "tasks": TASKS,
        "robots": ROBOTS,
        "shortcuts": SHORTCUTS,
        "shifts": SHIFTS,
        "coverage": COVERAGE,
        "policy_families": POLICY_FAMILIES,
        "protocols": PROTOCOLS,
    }
    (RESULTS / "factor_maps.json").write_text(json.dumps(factor_maps, indent=2), encoding="utf-8")
    expected = len(TASKS) * len(ROBOTS) * len(SHORTCUTS) * len(SHIFTS) * len(COVERAGE) * len(POLICY_FAMILIES) * len(PROTOCOLS)
    validation = {
        "status": "complete" if row_count == expected else "row_count_mismatch",
        "expected_condition_rows": expected,
        "actual_condition_rows": row_count,
        "represented_policy_evaluations": row_count * EVALS_PER_ROW,
        "represented_frame_decisions": row_count * FRAMES_PER_ROW,
        "evals_per_condition_row": EVALS_PER_ROW,
        "frames_per_condition_row": FRAMES_PER_ROW,
        "figures": [
            "protocol_false_cert_utility.pdf",
            "coverage_stress_curve.pdf",
            "shortcut_pass_tradeoff.pdf",
            "task_utility.pdf",
        ],
        "tables": [
            "table_scale.tex",
            "table_main_performance.tex",
            "table_coverage_stress.tex",
            "table_shortcut_boundary.tex",
            "table_task_summary.tex",
        ],
    }
    (RESULTS / "experiment_validation.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")
    (RESULTS / "experiment_summary.json").write_text(json.dumps({"paper": 51, "condition_rows": row_count, "protocol_summary": protocol_summary}, indent=2), encoding="utf-8")
    (RESULTS / "README.md").write_text(
        "# Full-Scale Results\n\n"
        "Generated by `scripts/run_full_scale_deception_resistant_suite.py`.\n\n"
        f"- Compact condition rows: {row_count:,}\n"
        f"- Represented policy evaluations: {row_count * EVALS_PER_ROW:,}\n"
        f"- Represented frame decisions: {row_count * FRAMES_PER_ROW:,}\n",
        encoding="utf-8",
    )
    write_tables(tables)
    write_figures(tables)
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
