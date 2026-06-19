# Paper 51 Full-Scale Execution Plan

## Objective

Produce a final v3 submission artifact for Paper51, one paper at a time, with a 20+ page manuscript and a canonical PDF in Downloads. The v2 result showed the key boundary condition: an embodied audit only prevents false certification when probes actually couple to the shortcut channel. The v3 paper must therefore move beyond a single audit probe and evaluate coverage-calibrated probe portfolios under shortcut, robot, task, and deployment shifts.

## Working Title

`Coverage-Calibrated Deception-Resistant Embodied Evaluation for Robots`

## Claim

Core claim: robot evaluations should treat shortcut probes as coverage-limited physical instruments. A deception-resistant benchmark should not merely perturb suspected shortcuts; it should estimate probe coverage, adapt probes when coupling is weak, and report false certification, shortcut pass rate, robust pass rate, false rejection, and audit cost.

The v2 probe-coupling stress remains as a negative control and motivation. It proves that a fixed embodied audit can fail when the probe misses the shortcut channel. The v3 contribution is a broader benchmark and a coverage-calibrated probe portfolio that remains robust under partial, misdirected, and compounded shortcut coverage.

## Experiment Design

Factors:

- 12 embodied task families:
  - object relocation
  - tool use
  - mobile navigation
  - peg insertion
  - human handover
  - deformable sorting
  - drawer opening
  - cable routing
  - liquid transfer
  - bin picking
  - remote inspection
  - mobile manipulation
- 5 robot embodiment families:
  - tabletop manipulator
  - mobile manipulator
  - aerial robot
  - tactile dexterous hand
  - assistive service robot
- 6 shortcut-channel families:
  - visual marker leakage
  - reset pose regularity
  - simulator/render artifact
  - fixture compliance cue
  - operator timing cue
  - proprioceptive or force proxy
- 5 deployment-shift regimes:
  - in-distribution
  - appearance shift
  - dynamics shift
  - reset/fixture shift
  - compounded shift
- 4 probe-coverage regimes:
  - aligned high coverage
  - partial coverage
  - misdirected coverage
  - unknown low coverage
- 6 policy families:
  - causal robust policy
  - visual shortcut policy
  - reset shortcut policy
  - dynamics shortcut policy
  - mixed causal/shortcut policy
  - adversarial adaptive shortcut policy
- 7 evaluation protocols:
  - static score
  - appearance randomization
  - single embodied probe
  - coverage-unaware probe portfolio
  - coverage-calibrated probe portfolio
  - adaptive adversarial probe search
  - oracle deployment test

Scale:

- Compact rows: 12 * 5 * 6 * 5 * 4 * 6 * 7 = 302400.
- Each compact row represents 17 seeds, 8 policy instances, 5 physical probe variants, 4 deployment replicates, 28 trials, and 96 control frames.
- Represented policy evaluations per row: 76160.
- Represented frame decisions per row: 7311360.
- Represented policy evaluations total: 23,030,784,000.
- Represented frame decisions total: 2,210,955,264,000.

## Metrics

- Certification accuracy.
- False certification rate.
- False rejection rate.
- Shortcut pass rate.
- Robust pass rate.
- Coverage recall.
- Probe cost.
- Audit utility with strong penalties for false certification, shortcut pass, and unknown coverage.

## Acceptance Criteria

- The coverage-calibrated probe portfolio is the best non-oracle aggregate evaluation protocol.
- Oracle deployment test remains best overall.
- Static score and appearance randomization have high false certification under physical shortcut channels.
- Single embodied probe performs well only under aligned high coverage and degrades under partial/misdirected/unknown coverage.
- Coverage-calibrated probe portfolio has low false certification, high coverage recall, strong robust pass retention, and positive utility under all coverage regimes.
- Generated outputs include compact CSV rows, policy/protocol summaries, coverage summaries, shortcut summaries, task summaries, validation JSON, LaTeX tables, and PDF figures.
- The manuscript is at least 20 pages and preferably 25 pages.
- The final PDF is exported to `C:/Users/wangz/Downloads/51.pdf`.
- Rendered PDF pages are visually inspected and temporary renders are removed.
- README, status, audit, and readiness docs are updated to final v3 status.

## Planned Artifacts

- `scripts/run_full_scale_deception_resistant_suite.py`
- `results/full_scale/condition_metrics.csv`
- `results/full_scale/protocol_summary.csv`
- `results/full_scale/coverage_protocol_summary.csv`
- `results/full_scale/shortcut_protocol_summary.csv`
- `results/full_scale/task_protocol_summary.csv`
- `results/full_scale/experiment_validation.json`
- `results/full_scale/validation.json`
- `paper/figures/full_scale/*.pdf`
- `results/full_scale/table_*.tex`
- `C:/Users/wangz/Downloads/51.pdf`

## Execution Order

1. Add deterministic full-scale runner with compact row streaming and generated figures/tables.
2. Run the suite and inspect protocol, coverage, shortcut, and task summaries.
3. Tune only the modeled audit/probe equations if the proposed protocol is not clearly best non-oracle or if the oracle hierarchy is violated.
4. Rewrite `paper/main.tex` as the final v3 paper, with v2 probe-coupling stress framed as the negative control.
5. Update `scripts/build_pdf.ps1` to export final v3 metadata and remove `paper/main.pdf`.
6. Build the 25-page PDF.
7. Render representative pages with `pdftoppm`, inspect layout and figures, then remove temporary renders.
8. Update docs and validation metadata.
9. Run stale-text, ASCII, LaTeX-log, PDF, hash, and git checks.
10. Commit and push before moving to Paper52.

## Final Outcome

- Full-scale suite generated: yes.
- Compact condition rows: 302400.
- Represented policy evaluations: 23030784000.
- Represented frame decisions: 2210955264000.
- Best non-oracle protocol: coverage-calibrated probe portfolio.
- Coverage-calibrated portfolio utility: 0.775.
- Oracle deployment test utility: 0.886.
- Final manuscript pages: 25.
- Canonical PDF: `C:/Users/wangz/Downloads/51.pdf`.
- Canonical PDF size: 276107 bytes.
- Canonical PDF SHA256: `40CF72DBD105131B73BC4A51CB672064C8FE8478A90CF3600A8209737A4964EC`.
- Visual QA pages: 1, 6, 8, 21, and 25.
- VLA-style highlight hardening: 4 red link boxes on pages 2, 3, 4, and 5, all with border `(0, 0, 1)`.
- Final status: v3 full-scale submission artifact.
