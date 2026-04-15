# Constellation Prompt-Native SDLC

## 1. Purpose

Constellation treats prompts, skills, policies, schemas, workflows, and evaluation artifacts as first-class source code. This SDLC defines how those artifacts are proposed, authored, reviewed, validated, released, and improved in GitHub.

This lifecycle applies to:

- mission and values documents
- prompt and skill artifacts
- policy and moderation artifacts
- schemas and interface contracts
- evaluations, test cases, benchmark suites, and example transcripts
- contributor instructions, decision records, and incident reports

## 2. Source Artifact Model

Every change must identify which artifact class it modifies.

### 2.1 Charter Artifacts

Examples:

- `SPEC.md`
- `VALUES.md`
- global rules
- governance rules

Use when defining mission, hard constraints, or constitutional behavior.

### 2.2 Contract Artifacts

Examples:

- schemas
- interface definitions
- prompt input and output contracts
- extension permission models

Use when defining stable boundaries that other artifacts depend on.

### 2.3 Operational Artifacts

Examples:

- prompts
- skills
- workflows
- moderation playbooks
- ranking logic descriptions

Use when defining executable behavior.

### 2.4 Evidence Artifacts

Examples:

- eval suites
- golden examples
- transcript fixtures
- benchmark summaries
- incident analyses

Use when proving whether an operational or policy change is good enough to ship.

### 2.5 Governance Artifacts

Examples:

- decision records
- proposals
- release notes
- contributor rules
- appeals and incident procedures

Use when defining how the project changes itself.

## 3. Lifecycle Principles

- Review the artifact, not just the prose. Prompt wording, examples, and constraints are executable behavior.
- Prefer small, composable changes over broad rewrites.
- Require provenance. Humans and AIs must be attributable in issues, commits, and pull requests.
- Require evidence proportional to risk.
- Preserve public legibility. Major behavior changes must be explainable from repository artifacts.
- Keep constitutional changes harder than local behavior tweaks.
- Humans retain final accountability for legal, safety, and constitutional decisions.

## 4. Change Classes

Each pull request must declare exactly one primary change class.

### Class C0: Editorial

Scope:

- grammar
- formatting
- broken links
- non-semantic clarifications

Requirements:

- linked issue optional
- no new eval evidence required
- one reviewer

### Class C1: Local Behavior

Scope:

- a prompt, skill, workflow, or contributor instruction with limited blast radius
- local examples or fixtures
- repo-local automation

Requirements:

- linked issue required
- updated examples or targeted eval evidence
- one maintainer approval

### Class C2: Shared Contract or Policy

Scope:

- schemas
- shared prompt contracts
- moderation policies
- evaluation standards
- contributor process changes that affect multiple artifact families

Requirements:

- linked issue required
- rationale section in PR
- backward-compatibility note or migration note
- updated evals and affected documentation
- two approvals, including the relevant artifact steward

### Class C3: Constitutional

Scope:

- mission
- values
- global rules
- governance model
- contributor rights and restrictions
- anything that changes what the project is for

Requirements:

- governance issue required
- explicit alternatives considered
- explicit risk analysis
- minimum public comment window of 72 hours before merge
- two human steward approvals, one of which must be a core maintainer

## 5. Lifecycle Stages

## 5.1 Intake

All non-editorial work starts with a GitHub issue.

Issue types:

- artifact proposal
- governance change
- evaluation failure
- incident or rollback follow-up

Each issue must state:

- problem
- desired outcome
- affected artifact class
- likely change class
- risks if unchanged

## 5.2 Triage

Maintainers or artifact stewards triage issues within GitHub using labels.

Required triage outputs:

- owner
- change class
- affected artifacts
- required evidence level
- whether AI-generated content is allowed, useful, or prohibited for this change

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
- `blocked`

## 5.3 Design

Before editing, the author must inspect existing artifact patterns and dependencies.

Required design questions:

- What behavior changes if this merges?
- Which artifacts must stay consistent with this change?
- How will the project know the new version is better?
- What failure modes or abuse paths could this introduce?
- What human accountability is required?

For C2 and C3 changes, these answers must be recorded in the PR description or linked issue.

## 5.4 Authoring

Authoring rules:

- keep diffs narrow
- preserve historical records unless the issue explicitly authorizes revision
- update examples, schemas, and eval fixtures alongside behavior changes
- separate normative changes from cleanup when possible

Every substantive artifact change must include:

- the changed source artifact
- supporting examples or fixtures when behavior is affected
- updated guidance where contributors would otherwise make the old assumption

## 5.5 Evidence Generation

Prompt-native projects do not get to skip testing. The tests are different, but they are still tests.

Evidence may include:

- golden example diffs
- transcript comparisons
- benchmark or eval summaries
- policy decision tables
- schema validation results
- manual review notes for non-automatable behavior
- incident replay results

Evidence expectations by class:

- C0: none beyond reviewer judgment
- C1: targeted examples or targeted evals
- C2: regression coverage for all affected contracts or policies
- C3: explicit comparison of old vs. new governance behavior and expected consequences

If evidence is manual, the PR must say:

- who performed it
- what was reviewed
- what passed or failed
- what remains uncertain

## 5.6 Pull Request Review

All changes merge through pull requests. Direct pushes to the default branch are not allowed.

Branch protection expectations in GitHub:

- require pull requests
- require status checks
- require conversation resolution
- block force-pushes to the default branch

Review dimensions:

- mission fit
- artifact correctness
- safety and abuse resistance
- internal consistency
- clarity for future contributors
- eval adequacy
- provenance completeness

AI review is allowed for analysis and drafting. Human review is mandatory for:

- C2 and C3 changes
- policy changes
- moderation logic
- incident closure
- release approval

## 5.7 Merge and Release

Merge policy:

- squash merge by default for artifact work
- keep commit messages descriptive and issue-linked
- merge only after required evidence and approvals are present

Release policy:

- tag releases when a coherent set of artifact changes is ready for downstream use
- publish release notes summarizing changed behaviors, affected artifacts, known risks, and required follow-up
- call out any migration expectations for dependent repos or agent runtimes

## 5.8 Operate and Observe

After merge, maintainers watch for:

- eval regressions
- contributor confusion
- policy ambiguity
- contradictory artifacts
- abuse opportunities created by the change

If a prompt, policy, or workflow behaves worse than intended, open an `eval failure` or `incident` issue immediately.

## 5.9 Incident, Rollback, and Correction

Rollback triggers:

- safety regression
- constitutional conflict
- broken contract
- materially misleading contributor guidance
- abuse-enabling prompt behavior

Rollback rules:

- prefer revert PRs over silent force-push correction
- document what failed and why
- open a follow-up issue before or immediately after rollback
- add or strengthen eval coverage before reattempting the change

## 6. Roles in the Lifecycle

Detailed authority lives in `GOVERNANCE.md`. Operationally, the lifecycle assumes these roles exist:

- contributor: authors or updates artifacts
- reviewer: evaluates correctness and clarity
- artifact steward: owns coherence for an artifact family
- eval owner: defines or approves evaluation adequacy
- release steward: packages and announces releases
- incident lead: coordinates urgent rollback or correction

One person may hold multiple roles for low-risk changes, but no one should unilaterally approve their own C2 or C3 PR.

## 7. Human and AI Contribution Rules

### 7.1 Human Contributors

Humans may propose, author, review, approve, merge, and govern according to their repository role.

Humans are accountable for:

- constitutional interpretation
- legal and safety judgment
- moderation policy approval
- release approval
- incident closure

### 7.2 AI Contributors

AIs may:

- draft artifacts
- propose diffs
- summarize issues
- run or assist with eval analysis
- review for consistency, coverage, and risk

AIs must not:

- hide their participation
- invent test evidence
- silently rewrite historical records
- serve as the only approval for C2 or C3 work

Every PR with AI involvement must disclose:

- model or agent identity when known
- major tasks performed by the AI
- which outputs were accepted without major rewrite
- human accountable reviewer

## 8. Definition of Done

A change is done only when all of the following are true:

- the issue is linked and still accurately describes the change
- the artifact class and change class are declared
- all impacted source artifacts are updated
- required evidence is attached
- required approvals are present
- `make test` passes
- any residual risk is documented

## 9. Repository Conventions

When this process is applied to a prompt-native repository, use these structural defaults unless that repository defines stricter ones:

- `prompts/` for prompt artifacts
- `skills/` for reusable workflows or operator knowledge
- `policy/` for governance and moderation rules
- `schemas/` for contracts
- `evals/` for evidence artifacts
- `decisions/` for ADRs and governance decisions
- `.github/` for templates and automation

## 10. Required GitHub Settings

Repository administrators should configure:

- protected default branch
- required PR reviews
- required status check for the repository validation workflow
- issue templates enabled
- pull request template enabled
- release tagging enabled

## 11. Minimum Operating Cadence

- triage new issues within 2 business days
- review C1 pull requests within 3 business days
- review C2 and C3 pull requests within 5 business days
- publish release notes for tagged releases on the day of release
- open incident issues within 24 hours of a confirmed regression

## 12. Internal Review and Continuous Improvement

The SDLC itself is a living artifact. The project must periodically inspect whether the process still serves the mission instead of assuming the initial design will remain adequate.

Review cadence:

- perform an internal SDLC review at least once per quarter
- perform an ad hoc review after any major incident, governance dispute, or contributor-experience failure

Review inputs:

- issue backlog shape and age
- PR cycle time
- validation failures
- incident count and severity
- contributor friction points
- release quality and downstream confusion

Review outcomes:

- update the SDLC or governance docs when the current process is creating avoidable drag or blind spots
- adjust template questions, evidence thresholds, or review roles when the work has outgrown the original baseline
- record the decision and rationale in a follow-up issue or decision record when the change has lasting impact
