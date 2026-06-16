# Reviewer Attacks

## 1. This is domain randomization with a new name.

Response: Not sustained after v3. The benchmark separately models appearance randomization and embodied physical shortcut probes. Appearance randomization has false certification 0.371, while the calibrated portfolio has false certification 0.032 and shortcut pass 0.003.

## 2. Synthetic shortcuts are easier to catch than real shortcuts.

Response: Partly sustained. The benchmark is deterministic and simulated, so the paper must not claim real-robot safety. The full-scale suite nevertheless expands the earlier diagnostic across task, embodiment, shortcut, deployment, coverage, policy, and protocol factors.

## 3. The audit only works if the probe hits the shortcut channel.

Response: Sustained and addressed directly. V3 makes coverage estimation the central mechanism. Certification is gated when coverage is partial, misdirected, or unknown.

## 4. A policy could adapt to the audit protocol.

Response: Partly sustained. The suite includes an adversarial adaptive shortcut policy family and adaptive search baseline, but it still does not prove security against arbitrary strategic policies.

## 5. False rejection may be high.

Response: Addressed by reporting false rejection, robust pass, and utility. The calibrated portfolio has false rejection 0.036 and robust pass 0.077, while the oracle has false rejection 0.027 and robust pass 0.085.

## Decision Impact

The final framing is submission-ready as a full-scale simulated benchmark with explicit limits. The paper should keep the oracle upper bound and the absence of real-robot validation visible.
