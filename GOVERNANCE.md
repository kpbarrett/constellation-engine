# Constellation Engine Governance

## 1. Governance Objective

Governance exists to keep the project mission-aligned, inspectable, and resistant to drift while still allowing fast iteration on prompts, skills, policies, and evaluation methods.

## 2. Role Definitions

### 2.1 Contributors

May:

- open issues
- propose changes
- author pull requests
- supply examples and evaluations

Must:

- declare change class and artifact class
- preserve provenance
- link changes to evidence

### 2.2 Reviewers

May:

- review pull requests
- request changes
- approve C0 and C1 changes if authorized

Must:

- review for correctness, clarity, risk, and consistency
- refuse approval when evidence is weak for the declared change class

### 2.3 Artifact Stewards

Artifact stewards own coherence for a given area such as prompts, policy, schemas, or evals.

May:

- set local conventions for their artifact family
- require migration notes
- reject changes that create inconsistency or hidden behavior shifts

Must:

- keep their artifact family internally consistent
- ensure dependent artifacts are updated together

### 2.4 Core Maintainers

Core maintainers are the human operators with final responsibility for repository integrity.

May:

- approve or reject any change
- merge pull requests
- manage repository settings
- initiate rollback

Must:

- guard mission fit
- protect constitutional and safety boundaries
- ensure GitHub protections remain active

### 2.5 Eval Owners

Eval owners define what evidence is sufficient for a given artifact family.

May:

- require new or stronger eval coverage
- block merges when evidence does not support the claim being made

Must:

- keep evidence criteria legible
- avoid performative testing that does not meaningfully reduce uncertainty

### 2.6 Incident Lead

The incident lead coordinates urgent response to regressions or governance failures.

May:

- declare an incident
- request immediate rollback
- require post-incident documentation

Must:

- prioritize containment and clarity
- leave an auditable record of decisions

## 3. Decision Rights

### 3.1 Who Can Decide What

- C0 editorial: one authorized reviewer
- C1 local behavior: one maintainer or steward approval
- C2 shared contract or policy: steward plus one additional authorized reviewer
- C3 constitutional: two human steward approvals, including one core maintainer

### 3.2 Human Reserved Authority

The following decisions must be approved by humans:

- constitutional changes
- moderation policy changes
- incident closure
- release approval
- repository access changes

AI systems may advise on these decisions but may not serve as the sole approving authority.

## 4. Governance Mechanisms

### 4.1 Issues

Issues are the default intake surface for new work, disputes, and failures.

### 4.2 Pull Requests

Pull requests are the only route to merge artifact changes.

### 4.3 Decision Records

For C2 and C3 changes with lasting impact, create or update a decision record in `decisions/` in the target repository when that repository supports them.

Decision records should capture:

- context
- decision
- alternatives considered
- consequences

### 4.4 Releases

Releases communicate stable artifact sets to downstream consumers. A release should summarize behavior changes, policy shifts, open risks, and migration notes.

## 5. Escalation Path

Escalate when:

- reviewers disagree on mission fit
- a change appears to conflict with `SPEC.md` or values
- evidence is disputed
- a merged change causes harm or confusion

Escalation order:

1. pull request discussion
2. linked governance issue
3. maintainer decision
4. rollback or constitutional review if needed

## 6. Governance Standards

- No silent constitutional drift.
- No unreviewed policy changes.
- No unverifiable AI-authored evidence.
- No hidden overrides that bypass declared process.
- No rewriting historical governance records without explicit correction procedure.

## 7. Quorum and Timing

- C2 changes should remain open for review long enough for the relevant steward to see them.
- C3 changes require a 72-hour comment window before merge.
- Incident rollback decisions may bypass normal timing but must be documented afterward.

## 8. Repository Administration Standards

Core maintainers should keep the GitHub repository configured with:

- protected default branch
- required pull request reviews
- required status checks
- signed or attributable commits when available
- force-push protection on the default branch

## 9. Internal Review and Continuous Improvement

The process should be audited periodically to make sure it still supports the project goals instead of ossifying into ceremony.

At minimum, core maintainers should run a quarterly internal review that checks:

- whether contributors can still understand the repo entry points quickly
- whether the current templates ask for the right evidence
- whether review latency is blocking useful work
- whether the release and issue flow still match actual contribution patterns
- whether any repeated confusion suggests the SDLC docs need adjustment

If the review identifies a gap, update the relevant SDLC, workflow, or template document and capture the rationale in a follow-up issue or decision record.

## 10. Amendment Rules

This governance document is itself a C3 constitutional artifact. Amend it only through the C3 path defined in `SDLC.md`.
