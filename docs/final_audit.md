# Final Audit

Paper-readiness judgment: final v3 full-scale submission artifact.

Submission-hardening version: v3.

## Final Experiment

- Compact condition rows: 302400.
- Represented policy evaluations: 23030784000.
- Represented frame decisions: 2210955264000.
- Factors: 12 task families, 5 robot embodiments, 6 shortcut channels, 5 deployment shifts, 4 probe-coverage regimes, 6 policy families, and 7 evaluation protocols.
- Each compact row represents 17 seeds, 8 policy instances, 5 physical probe variants, 4 deployment replicates, 28 trials, and 96 control frames.

## Main Results

- Static score: certification accuracy 0.475, false certification 0.486, shortcut pass 0.264, utility -0.252.
- Appearance randomization: certification accuracy 0.587, false certification 0.371, shortcut pass 0.196, utility -0.014.
- Single embodied probe: certification accuracy 0.560, false certification 0.398, shortcut pass 0.212, utility -0.083.
- Coverage-unaware portfolio: certification accuracy 0.645, false certification 0.315, shortcut pass 0.162, utility 0.098.
- Coverage-calibrated portfolio: certification accuracy 0.933, false certification 0.032, false rejection 0.036, shortcut pass 0.003, robust pass 0.077, coverage recall 0.680, utility 0.775.
- Adaptive adversarial search: certification accuracy 0.862, false certification 0.089, shortcut pass 0.029, utility 0.570.
- Oracle deployment test: certification accuracy 0.942, false certification 0.032, false rejection 0.027, shortcut pass 0.003, robust pass 0.085, coverage recall 0.931, utility 0.886.

## Coverage Stress

The calibrated portfolio remains the best non-oracle protocol across coverage regimes:

- Aligned high coverage: false certification 0.035, shortcut pass 0.004, coverage recall 0.997, utility 0.867.
- Partial coverage: false certification 0.032, shortcut pass 0.003, coverage recall 0.758, utility 0.805.
- Misdirected coverage: false certification 0.030, shortcut pass 0.003, coverage recall 0.490, utility 0.729.
- Unknown low coverage: false certification 0.029, shortcut pass 0.003, coverage recall 0.475, utility 0.699.

## Decision

The final paper is ready as a v3 full-scale submission artifact. It does not claim real-robot safety or guaranteed unknown-shortcut discovery. Its central supported claim is that embodied robot evaluation should calibrate probe coverage before certifying behavior, because uncalibrated probes can recreate the false-certification failure that the benchmark is meant to expose.

## Artifact Audit

- Canonical PDF: `C:/Users/wangz/Downloads/51.pdf`
- Pages: 25.
- File size: 276127 bytes.
- SHA256: `120D7C07C1868E2BB24B4E9060E09688D4D13746A664A5E5C9DDBCAE08C6F02B`.
- Visual QA pages: 1, 6, 8, 21, and 25.
- Local tracked/generated PDF policy: `paper/main.pdf` is ignored and removed after build.
- Desktop copy: absent.
- Build script: `scripts/build_pdf.ps1`
