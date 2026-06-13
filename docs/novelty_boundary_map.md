# Novelty Boundary Map

## What Survives

Deception-resistant embodied evaluation is useful as a diagnostic contract: the evaluator should state suspected shortcut channels, perturb them physically, verify that the probe couples to the shortcut, and report false certification.

## What V2 Breaks

The embodied audit is not automatically robust. In the v2 probe-coverage stress:

- Probe coupling 1.00: false certification 0.004, shortcut pass 0.003.
- Probe coupling 0.25: false certification 0.105, shortcut pass 0.114.
- Probe coupling 0.00: false certification 0.238, shortcut pass 0.264.

This means the audit is only as good as the shortcut hypothesis and intervention coverage.

## Workshop-Safe Framing

- Present static scoring and randomized scoring as failure cases.
- Present embodied audit as a diagnostic that requires calibrated probes.
- Emphasize false certification and false rejection reporting.
- Treat unknown shortcut discovery and real-robot validation as future work.

## Unsafe Framing

- "This benchmark is deception-proof."
- "The audit catches arbitrary shortcut policies."
- "The result proves real-world robot evaluation safety."
- "Domain randomization is obsolete."
