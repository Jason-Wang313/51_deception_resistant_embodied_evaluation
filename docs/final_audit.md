# Final Audit

Paper-readiness judgment: workshop-only.

Submission-hardening version: v2.

## Original Diagnostic

- 720 synthetic policy-case evaluations.
- Static score: certification accuracy 0.410, false certification 0.639, shortcut pass 0.806.
- Randomized score: certification accuracy 0.610, false certification 0.116, shortcut pass 0.172.
- Embodied audit: certification accuracy 0.901, false certification 0.004, shortcut pass 0.003.

## V2 Probe-Coverage Stress

The hardening pass adds `scripts/v2_probe_coverage_stress.py`, which weakens the coupling between the physical probe and the shortcut channel.

- Probe coupling 1.00: false certification 0.004, shortcut pass 0.003.
- Probe coupling 0.75: false certification 0.013, shortcut pass 0.019.
- Probe coupling 0.50: false certification 0.027, shortcut pass 0.039.
- Probe coupling 0.25: false certification 0.105, shortcut pass 0.114.
- Probe coupling 0.00: false certification 0.238, shortcut pass 0.264.

## Decision

Workshop-only. The paper is honest as a diagnostic and reporting-contract note for false certification in robot benchmarks. It is not submit-ready as a full conference paper because the evidence is synthetic, shortcut families are manually specified, and v2 shows probe coverage is a fragile central assumption.

## Required Future Work

- Real robot or high-fidelity benchmark traces.
- Unknown-shortcut discovery machinery.
- Stronger domain-randomization and adaptive-evaluation baselines.
- Probe coverage metrics and false-rejection tradeoff analysis.

## Artifact Audit

- Canonical PDF: `C:/Users/wangz/Downloads/51.pdf`
- Local tracked/generated PDF policy: `paper/main.pdf` is ignored and removed after build.
- Desktop copy: absent.
- Build script: `scripts/build_pdf.ps1`
