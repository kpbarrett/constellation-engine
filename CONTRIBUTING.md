# Contributing to Constellation Engine

## 1. Before You Start

- Read `SPEC.md`, `SDLC.md`, and `GOVERNANCE.md`.
- Search for existing terms, patterns, and related artifacts before inventing a new structure.
- Open or claim a GitHub issue unless the change is clearly C0 editorial.
- Keep the change as small as possible while still solving the actual problem.

## 2. Contributor Workflow

1. Open or claim an issue.
2. Declare the change class: `C0`, `C1`, `C2`, or `C3`.
3. State the primary artifact class being changed.
4. Create a short-lived branch from `main`.
5. Make the smallest coherent change that solves the issue.
6. Add evidence proportional to risk.
7. Run `make test`.
8. Open a pull request using the repository template.

## 3. Branch and PR Expectations

Suggested branch prefixes:

- `editorial/`
- `artifact/`
- `contract/`
- `policy/`
- `governance/`
- `eval/`
- `incident/`

Each PR should address one primary concern. Split the work when:

- policy and implementation can be reviewed independently
- a schema change and migration notes would obscure each other
- a constitutional debate would block local engine progress

## 4. Evidence Expectations

Use evidence that matches the artifact:

- prompt or workflow change: before and after examples, transcript fixtures, or targeted evals
- schema change: contract examples and migration notes
- policy change: decision tables, edge cases, and enforcement examples
- governance change: explicit explanation of authority shifts and failure modes

When evidence is manual, write down:

- scenario reviewed
- reviewer identity
- outcome
- unresolved uncertainty

## 5. Provenance Requirements

All contributors must preserve attribution.

If AI assisted:

- disclose the model or agent when known
- describe what it produced
- identify the human accountable reviewer

If multiple humans contributed:

- identify the final accountable author in the PR
- credit subject matter reviewers when relevant

## 6. Review Etiquette

- Review for mission fit and operational consequences, not just sentence quality.
- Challenge vague wording in prompts, policies, and contracts.
- Prefer concrete counterexamples over abstract disagreement.
- Mark blocking feedback clearly.
- Resolve threads only when the artifact or rationale changed accordingly.

## 7. Historical Integrity

Do not silently rewrite project history, incident records, decision logs, or review outcomes. If history was wrong, correct it through an explicit follow-up that preserves the original trail.

## 8. Community Standards

By participating, you agree to follow `CODE_OF_CONDUCT.md`. Report unacceptable behavior or security-sensitive concerns through the channels in `CODE_OF_CONDUCT.md` and `SECURITY.md` rather than in public issues when disclosure would create harm.

## 9. Validation

Run:

```sh
make test
```

Do not merge a PR that fails repository validation.
