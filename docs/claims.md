# Claims

## Core Claim

Robot evaluation should treat embodied shortcut probes as coverage-limited physical instruments. A benchmark that certifies robots under possible deceptive or shortcut behavior should estimate probe coverage, gate certification when coverage is weak, and report false certification, false rejection, shortcut pass, robust pass, coverage recall, cost, and utility.

## Supported After V3

- Static scoring falsely certifies shortcut policies at a high rate in the full-scale suite: false certification 0.486 and shortcut pass 0.264.
- Appearance randomization improves over static scoring but still leaves false certification 0.371 and shortcut pass 0.196.
- A single embodied probe is insufficient under weak coverage: aggregate false certification 0.398 and shortcut pass 0.212.
- A coverage-unaware portfolio improves utility but remains fragile: false certification 0.315 and utility 0.098.
- The coverage-calibrated portfolio is the best non-oracle protocol: certification accuracy 0.933, false certification 0.032, shortcut pass 0.003, coverage recall 0.680, and utility 0.775.
- The oracle deployment test remains best overall: certification accuracy 0.942, false certification 0.032, coverage recall 0.931, and utility 0.886.
- Under unknown low coverage, the calibrated portfolio maintains false certification 0.029 and shortcut pass 0.003 by gating certification instead of over-trusting missed probes.

## Claims To Avoid

- Do not claim real-robot safety validation.
- Do not claim the benchmark catches every unknown shortcut without discovery instrumentation.
- Do not claim domain randomization is useless; the supported claim is that randomization alone can miss physical shortcut channels.
- Do not claim the oracle deployment test is unnecessary; it remains the upper-bound protocol.

## Current Boundary

The supported contribution is a deterministic full-scale benchmark and reporting contract for coverage-calibrated embodied evaluation. It expands the earlier diagnostic into a 302,400-row suite representing 23,030,784,000 policy evaluations and 2,210,955,264,000 frame decisions, while keeping the central limitation explicit: certification is only justified to the extent that probe coverage is estimated and reported.
