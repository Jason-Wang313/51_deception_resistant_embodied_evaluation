# Claims

## Core Claim

Robot evaluation should report false certification and physically perturb suspected shortcut channels, rather than relying only on static score or appearance randomization.

## Supported After V2

- Static scoring falsely certifies shortcut policies in the synthetic diagnostic: false certification rate 0.639.
- Randomized scoring helps but still has false certification rate 0.116.
- Fully coupled embodied probing reduces false certification to 0.004.
- Probe coverage is the key assumption: at probe coupling 0.25, false certification rises to 0.105; at 0.00, it rises to 0.238.

## Claims To Avoid

- Do not claim a universal benchmark.
- Do not claim real-robot safety.
- Do not claim the audit catches unknown shortcut channels without discovery machinery.
- Do not claim domain randomization is useless; the claim is that randomization alone can miss physical shortcuts.

## Current Boundary

The supported contribution is a diagnostic/reporting contract: identify shortcut hypotheses, physically perturb them, verify probe coverage, and report false certification.
