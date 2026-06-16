# Submission Attack Log

## Attack: weak or misdirected physical probes

Result: Addressed by v3 coverage calibration. The calibrated portfolio gates certification when coverage is weak and maintains low false certification across aligned, partial, misdirected, and unknown coverage regimes.

Decision impact: keep coverage recall and certification gating central to the paper.

## Attack: synthetic shortcut families

Result: Partly sustained. V3 expands the suite across six shortcut-channel families and twelve task families, but the paper still identifies the benchmark as deterministic and simulated.

Decision impact: do not claim real-robot safety.

## Attack: false rejection tradeoff

Result: Addressed by reporting false rejection, robust pass, cost, and utility. The calibrated portfolio reaches false rejection 0.036 and utility 0.775.

Decision impact: keep the multi-metric table in the main paper.

## Attack: oracle deployment should dominate

Result: Passed. The oracle deployment test remains best overall with utility 0.886, while the calibrated portfolio is best non-oracle with utility 0.775.

Decision impact: present calibrated evaluation as the practical non-oracle protocol, not as an oracle replacement.
