# Coverage-Calibrated Deception-Resistant Embodied Evaluation for Robots

Submission-hardening version: v3 full-scale.

Decision: final submission artifact.

The paper now evaluates deception-resistant robot certification as a coverage-calibrated embodied benchmark rather than a single fixed probe. The v2 probe-coupling failure is retained as the negative control: a probe only works when it reaches the shortcut channel. The v3 contribution is a deterministic full-scale suite showing that coverage-calibrated probe portfolios keep false certification low under aligned, partial, misdirected, and unknown coverage regimes.

## Key Artifacts

- `paper/main.tex`: final v3 anonymous review manuscript.
- `scripts/run_full_scale_deception_resistant_suite.py`: deterministic full-scale experiment runner.
- `results/full_scale/condition_metrics.csv`: 302,400 compact condition rows.
- `results/full_scale/protocol_summary.csv`: protocol-level certification, shortcut, coverage, cost, and utility summary.
- `results/full_scale/coverage_protocol_summary.csv`: coverage-regime stress results.
- `results/full_scale/shortcut_protocol_summary.csv`: shortcut-channel boundary results.
- `results/full_scale/task_protocol_summary.csv`: task-family utility results.
- `results/full_scale/validation.json`: canonical PDF and experiment validation record.
- `paper/figures/full_scale/*.pdf`: generated manuscript figures.
- `docs/final_audit.md`: final submission-hardening audit.
- `docs/full_scale_execution_plan.md`: pre-edit execution plan and final outcome.

## Main Result

The coverage-calibrated portfolio is the best non-oracle protocol by utility. It reaches certification accuracy 0.933, false certification 0.032, shortcut pass 0.003, robust pass 0.077, coverage recall 0.680, and utility 0.775. The oracle deployment test remains best overall with utility 0.886. Static scoring, appearance randomization, a single probe, and a coverage-unaware portfolio all leave substantially higher false certification.

Scale: 302,400 compact condition rows representing 23,030,784,000 policy evaluations and 2,210,955,264,000 frame decisions.

## Canonical PDF

The canonical built PDF is `C:/Users/wangz/Downloads/51.pdf`.

- Pages: 25.
- Size: 276,127 bytes.
- SHA256: `120D7C07C1868E2BB24B4E9060E09688D4D13746A664A5E5C9DDBCAE08C6F02B`.
- Visual QA: rendered pages 1, 6, 8, 21, and 25.

Local generated PDFs are not tracked. The build script copies the generated PDF to the canonical Downloads path and removes `paper/main.pdf`.

```powershell
python scripts\run_full_scale_deception_resistant_suite.py
powershell -ExecutionPolicy Bypass -File scripts\build_pdf.ps1
```
