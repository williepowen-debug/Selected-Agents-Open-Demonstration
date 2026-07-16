# NEXUS Example State

> Demonstration only. The labels and observations below are fictional.

## Candidate convergence `DEMO-C01`

| Input | Observation | Immediate source | Causal antecedent |
|---|---|---|---|
| Agent A | Sensor X rose | Dataset 1 | Event Q |
| Agent B | Transport delay widened | Dataset 2 | Event Q |
| Agent C | Financing cost rose | Dataset 3 | Policy R |

## Synthesis

Agents A and B describe different transmission paths from the same shock. They count as two observations but one causal leg. Agent C is independent of Event Q and supplies a second leg.

| Field | Example value |
|---|---|
| Shared antecedents | `Event Q` |
| Independent legs | `2` |
| Mechanism grade | `SUPPORTED` |
| Threshold grade | `NOT YET SATISFIED` |
| Confidence | `MEDIUM` |
| Flip condition | A separately sourced threshold observation or failure of Policy R transmission |

## Route

NEXUS sends the threshold gap to the domain owner and asks RED to challenge the claimed independence of Agent C. No operational action is routed to PROME until that review closes.
