# Reviewer Attacks

## 1. This is domain randomization with a new name.

Response: Partly sustained. The paper distinguishes appearance randomization from physical shortcut probes, but it must compare to strong randomization and adaptive evaluation in future work.

## 2. Synthetic shortcuts are easier to catch than real shortcuts.

Response: Sustained. The current benchmark has manually specified shortcut families. This keeps the paper workshop-only.

## 3. The audit only works if the probe hits the shortcut channel.

Response: Sustained. V2 probe-coverage stress shows false certification rises from 0.004 at full coupling to 0.105 at 0.25 coupling and 0.238 at zero coupling.

## 4. A policy could adapt to the audit protocol.

Response: Sustained as future work. The current diagnostic does not model strategic audit-aware policies beyond weakened probe coupling.

## 5. False rejection may be high.

Response: Sustained. The fully coupled embodied audit has false rejection rate 0.280, so the paper should report both false certification and false rejection rather than optimizing one metric.

## Decision Impact

Workshop-only. The concept is useful, but the evidence is synthetic and depends on calibrated probe coverage.
