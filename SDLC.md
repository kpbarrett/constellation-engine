# Constellation Engine SDLC

## 1. Purpose

Constellation Engine treats prompts, skills, policies, schemas, workflows, evaluation artifacts, and governance records as first-class source code. This SDLC defines how those artifacts are proposed, authored, reviewed, validated, released, and improved over time.

The lifecycle must help the project ship useful work while protecting mission fit, transparency, contributor accountability, and public legibility.

## 2. Source Artifact Model

Every change must identify the primary artifact class it modifies.

### 2.1 Charter Artifacts

Examples:

- `SPEC.md`
- values statements
- mission-defining rules

Use when defining what Constellation is for and what must remain true.

### 2.2 Contract Artifacts

Examples:

- schemas
- interface definitions
- participant, content, reputation, or moderation contracts
- extension boundaries

Use when defining stable interfaces that other artifacts depend on.

### 2.3 Operational Artifacts

Examples:

- prompts
- skills
- workflows
- ranking descriptions
- moderation playbooks

Use when defining executable engine behavior.

### 2.4 Evidence Artifacts

Examples:

- eval suites
- fixtures
- golden transcripts
- benchmarks
- incident analyses

Use when proving whether a behavior or policy change should ship.

### 2.5 Governance Artifacts

Examples:

- decision records
- contributor rules
- review and release procedures
- incident reports

Use when defining how the project changes itself.

## 3. Lifecycle Principles

- Review the behavior encoded in artifacts, not just the prose quality.
- Prefer narrow, composable changes over wide rewrites.
- Require provenance for human and AI contribution.
- Match evidence to risk.
- Keep constitutional changes harder than local behavior changes.
- Preserve historical integrity. Correct history by appending clarification unless a correction path explicitly authorizes revision.
- Build the SDLC to improve itself through periodic review, not only during crises.

## 4. Change Classes

Each pull request must declare exactly one primary change class.

### C0: Editorial

Scope:

- grammar
- formatting
- broken links
- non-semantic clarification

Requirements:

- linked issue optional
- no new eval evidence required
- one reviewer

### C1: Local Behavior

Scope:

- a prompt, workflow, schema, doc, or automation change with limited blast radius
- local examples or fixtures
- repository-local tooling

Requirements:

- linked issue required
- targeted examples, fixtures, or validation notes
- one maintainer or steward approval

### C2: Shared Contract or Policy

Scope:

- shared schemas
- participant or content contracts
- moderation policies
- evaluation standards
- process changes that affect multiple artifact families

Requirements:

- linked issue required
- rationale section in the PR
- migration note or backward-compatibility note
- updated evidence and affected documentation
- two approvals, including the relevant steward

### C3: Constitutional

Scope:

- mission
- values
- governance model
- contributor rights and restrictions
- identity or transparency rules
- anything that changes what the project is for

Requirements:

- governance issue required
- explicit alternatives considered
- explicit risk analysis
- minimum 72-hour comment window before merge
- two human steward approvals, one of which must be a core maintainer

## 5. Lifecycle Stages

### 5.1 Intake

All non-editorial work starts with a GitHub issue.

Issue types:

- feature or artifact proposal
- governance change
- eval failure
- internal review follow-up
- incident follow-up

Each issue must state:

- problem
- desired outcome
- affected artifact class
- likely change class
- risks if unchanged

### 5.2 Triage

Maintainers or stewards triage issues using labels and ownership.

Required triage outputs:

- owner
- change class
- affected artifacts
- required evidence level
- whether AI-generated content is allowed, useful, or prohibited

Suggested labels:

- `artifact:charter`
- `artifact:contract`
- `artifact:operational`
- `artifact:evidence`
- `artifact:governance`
- `class:C0`
- `class:C1`
- `class:C2`
- `class:C3`
- `needs-evals`
- `needs-human-review`
- `status:blocked`

### 5.3 Design

Before editing, the author must inspect existing patterns and dependencies.

Required design questions:

- What user-visible or operator-visible behavior changes if this merges?
- Which artifacts must remain consistent with the change?
- What evidence will show the new version is better or safer?
- What failure modes or abuse paths could this introduce?
- What human accountability is required?

For C2 and C3 changes, record these answers in the PR description or linked issue.

### 5.4 Authoring

Authoring rules:

- keep diffs narrow
- preserve historical records unless the issue explicitly authorizes revision
- update examples, fixtures, schemas, or docs alongside substantive behavior changes
- separate normative changes from cleanup when possible

Every substantive change should include:

- the changed source artifact
- supporting examples, fixtures, or release notes when behavior is affected
- updated guidance where contributors would otherwise make the old assumption

### 5.5 Evidence Generation

Constellation Engine does not skip testing because some artifacts are human-readable.

Evidence may include:

- schema validation
- transcript comparisons
- before and after examples
- benchmark or eval summaries
- manual review notes for non-automatable behavior
- incident replay results

Evidence expectations by class:

- C0: reviewer judgment only
- C1: targeted examples or validation notes
- C2: regression coverage for affected shared behavior
- C3: explicit comparison of old vs. new governance or constitutional behavior

If evidence is manual, the PR must state:

- who performed it
- what they reviewed
- what passed or failed
- what remains uncertain

### 5.6 Review

Reviewers must assess:

- mission fit
- clarity
- behavioral impact
- evidence sufficiency
- consistency with `SPEC.md`
- whether declared change class matches the real blast radius

Blocking review feedback should be explicit.

### 5.7 Release

Releases mark stable artifact sets for downstream engine work.

Each release should include:

- summary of behavior and process changes
- contract or migration notes
- known risks
- incident follow-ups still open

Prefer small, frequent releases over infrequent bundles that obscure provenance.

### 5.8 Incident and Rollback

If a merged artifact creates harm, confusion, or a governance breach:

1. contain the issue
2. open or link an incident issue
3. rollback or patch with human approval appropriate to the risk
4. record the cause, impact, and follow-up actions

Incident rollback may bypass normal timing, but it must be documented afterward.

## 6. CI/CD Baseline

The initial CI/CD baseline for this repository is:

- `make test` as the required local and CI validation entrypoint
- GitHub Actions validation on pushes and pull requests
- tagged release publication through GitHub Actions
- scheduled internal SDLC review issue generation

As runnable engine components arrive, extend CI to cover them through `make test` rather than creating fragmented entrypoints.

## 7. Human and AI Contribution Rules

- Humans remain accountable for acceptance and merge decisions.
- AI assistance must be disclosed in pull requests when used for drafting, analysis, review, or evaluation.
- AI systems may propose, summarize, and help validate, but may not be the sole approving authority for C2 or C3 changes.
- Unverifiable AI-authored evidence is not sufficient for merge.
- Sensitive or safety-relevant policy changes require human review even when AI generated the draft.

## 8. Definition of Done

A change is done when:

- the issue and change class are clear
- required artifacts are updated
- evidence is attached and proportionate to risk
- `make test` passes
- the review path is complete
- downstream or release implications are documented

## 9. Continuous Improvement Review

The SDLC itself must be reviewed on a regular cadence.

Cadence:

- open an internal review issue every 30 days
- additionally trigger review after any critical incident or repeated process failure

Each internal review should answer:

- Is the current SDLC helping the project meet the goals in `SPEC.md`?
- Which steps create clarity and which create drag?
- Where did contributor confusion, review delay, or weak evidence appear?
- Which automation or templates should be added, tightened, or removed?
- Are release, rollback, and incident procedures still proportionate to the project stage?

Outputs:

- a short written assessment in the review issue
- follow-up issues for concrete process changes
- reclassification of any policy now too weak or too heavy for the actual project risk

This section is normative. Process drift should be corrected through ordinary governance rather than ignored.
