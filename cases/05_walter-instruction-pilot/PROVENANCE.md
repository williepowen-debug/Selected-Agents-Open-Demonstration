# Provenance — WALTER instruction pilot

Prepared September 6, 2026. This package presents a recorded, limited pilot; it does not run new agent sessions or modify WALTER's operating instructions.

## Source anchors

The committed inputs, fixture files, and execution-record extractions are pinned to private commit **`ddd3713aea3251cadf8eaa2ae7cc820dbf5a9cb2`**, under `AGENTS/WALTER/design/pilot_runs/`. The core rubric excerpt comes from **`269fa140f2ff325c2c7fea2db866a76dafa24521`**, under `AGENTS/WALTER/design/PILOT_STEP_FORM_2026-09-06.md`. The bounded closeout is at **`1bd4dab90abf475f6fbcf6e301e94852f0442374`** in that same document.

The [manifest](evidence/manifest.json) records full source commit IDs, relative source paths, private-file hashes, public-file hashes, and selected metadata from the two original session JSONL files. Hashes support checking local artifact consistency; because the manifest and artifacts ship together, they do not independently authenticate the private origin.

## Preserved versus edited

- **Instruction files:** exact UTF-8 contents preserved, including original names, historical incident references, and the revised preamble wrapper. They are archived test inputs, not current instructions or claims that those historical references were re-researched here.
- **Execution records:** copied from the committed Markdown extractions, with a new editorial wrapper. All numbered turns, prompts, tool calls/results, and final answers in those extractions remain in order. This is not an export of all original runner context or internal metadata.
- **Privacy substitutions throughout records:** historical temporary root → `/fixture`; local username → `operator`; original JSONL filenames → `CONTROL_SESSION.jsonl` / `REVISED_SESSION.jsonl`.
- **Fixture sanitization throughout records and files:** the registry metric → `DEMO-METRIC`, and its numeric band → `EXAMPLE-BAND`. Neither value determines the A/B/C grading. Agent names, signal identifiers, missing-recipient condition, and missing-file condition are retained for consistent references.
- **Formatting:** terminal newlines added to text artifacts where absent. Instruction-file bytes were separately checked against the pinned originals and match exactly.
- **Editorial additions:** README, evidence guide, this provenance, manifest, and artifact checker were prepared by Codex under Will's direction. They are not contemporaneous trial outputs.

The original records' internal headings calling themselves raw/verbatim refer to their private extraction. The outer public wrapper governs here: **the published copies are sanitized**, not byte-verbatim original transcripts. The original models' abbreviated self-reports remain visible rather than being silently repaired.

## Checks and their limits

During preparation, the source history, archived tool calls/results, final replies, and original session metadata were inspected. Both session records report `claude-sonnet-5`, with five original-arm and six revised-arm tool calls. Full hidden/system context, immutable provider build identity, sampling settings, and a controlled cost record are not supplied by this package. Do not infer those from a model name or elapsed timestamps.

The instruction-file byte counts are **1,724 → 1,537**, a difference of **187**. The original full prompts have different surrounding text; this byte comparison does not measure their complete transmitted inputs, token counts, or billed cost.

`check_artifacts.py` checks public-file hashes, exact instruction sizes, selected fixture properties, tool-call counts, and the archived timing relationship. It does not judge model reasoning, estimate an effect, reconstruct private inputs, or prove historical isolation. The behavior grades are inspectable editorial judgments against the recorded evidence, not the output of that checker.

The original session JSONL files remain private. Their hashes and limited metadata are included; the public reader can inspect the sanitized tool records but cannot independently authenticate those JSONL files from this bundle. Private artifacts remain available for review on request under the repository's existing policy.

## Claims deliberately excluded

No claim of general behavioral equivalence, superiority, maintenance savings, reference independence, statistical significance, or fleet-wide adoption. The core rubric predates execution, but a later addendum was committed during it; see [chronology](EVIDENCE.md#chronology). The pilot's final interpretation was a post-review correction, not its author's first conclusion.

Will authorized the work and selected the public case. WALTER authored the candidate and managed the original exercise. The two subagents generated the recorded behavior. Codex advised on the protocol and reviewed its interpretation, then prepared this public account. Neither this role separation nor two model sessions constitutes independent experimental replication.
