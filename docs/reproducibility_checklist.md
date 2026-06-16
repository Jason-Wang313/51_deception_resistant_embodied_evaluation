# Reproducibility Checklist

- Full-scale generator: `scripts/run_full_scale_deception_resistant_suite.py`.
- Full-scale outputs: `results/full_scale/condition_metrics.csv`, `protocol_summary.csv`, `coverage_protocol_summary.csv`, `shortcut_protocol_summary.csv`, `task_protocol_summary.csv`, `experiment_summary.json`, `experiment_validation.json`, and `validation.json`.
- Generated tables: `results/full_scale/table_scale.tex`, `table_main_performance.tex`, `table_coverage_stress.tex`, `table_shortcut_boundary.tex`, and `table_task_summary.tex`.
- Generated figures: `paper/figures/full_scale/protocol_false_cert_utility.pdf`, `coverage_stress_curve.pdf`, `shortcut_pass_tradeoff.pdf`, and `task_utility.pdf`.
- Historical diagnostic generator: `scripts/recover_paper51.py`.
- Historical v2 hardening generator: `scripts/v2_probe_coverage_stress.py`.
- Manuscript source: `paper/main.tex`.
- Build command: `powershell -ExecutionPolicy Bypass -File scripts\build_pdf.ps1`.
- Canonical PDF: `C:/Users/wangz/Downloads/51.pdf`.
- Canonical PDF pages: 25.
- Canonical PDF SHA256: `120D7C07C1868E2BB24B4E9060E09688D4D13746A664A5E5C9DDBCAE08C6F02B`.
- Local generated PDF policy: `paper/main.pdf` is ignored and removed after build.
- Desktop PDF copy: absent.
- Visual QA pages: 1, 6, 8, 21, and 25.
