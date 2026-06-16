# Hostile Reviewer Response

The strongest criticism remains correct: an embodied audit only works when its physical probe actually reaches the shortcut channel. The v3 paper does not hide that weakness; it turns it into the evaluation target.

The full-scale revision adds coverage regimes, robot embodiments, task families, shortcut families, deployment shifts, policy families, and protocol comparisons. The decisive change is that certification is gated by estimated probe coverage. Under unknown low coverage, the calibrated portfolio keeps false certification at 0.029 and shortcut pass at 0.003, while single probes and coverage-unaware portfolios fail because they over-trust missed interventions.

The paper should still concede three limits. First, the benchmark is deterministic and simulated. Second, it does not provide a general unknown-shortcut discovery guarantee. Third, the oracle deployment test remains the upper-bound protocol. These limits are compatible with the submitted claim: robot evaluation should report and calibrate probe coverage before certifying a policy as robust.
