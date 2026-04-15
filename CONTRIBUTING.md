# Contributing to Constellation Engine

## 1. Before You Start

- Read `SPEC.md`, `SDLC.md`, and `GOVERNANCE.md`.
- Read `GITHUB-WORKFLOW.md` before opening a pull request.
- Search for existing patterns before proposing a new structure or term.
- Open or claim a GitHub issue unless the change is clearly C0 editorial.

## 2. Contributor Workflow

1. Open an issue using the closest template.
2. Classify the change as `C0`, `C1`, `C2`, or `C3`.
3. State which artifact class is being changed.
4. Create a branch from the default branch.
5. Make the smallest coherent change that solves the issue.
6. Add evidence proportional to risk.
7. Run `make test`.
8. Open a pull request using the repository template.

## 3. Branch and PR Expectations

Suggested branch prefixes:

- `editorial/`
- `artifact/`
- `policy/`
- `governance/`
- `eval/`
- `incident/`

Each PR should change one primary concern. Split the work when:

- a policy change and a prompt rewrite can be reviewed independently
- a schema change and its migrations would obscure each other
- a constitutional debate would block operational improvements

## 4. Evidence Expectations

Use evidence that matches the artifact:

- prompt or skill change: before and after examples, transcript fixtures, or targeted evals
- policy change: decision tables, edge cases, and enforcement examples
- schema change: contract examples and migration notes
- governance change: explicit explanation of authority shifts and failure modes

When evidence is manual, write down:

- scenario reviewed
- reviewer identity
- outcome
- unresolved uncertainty

## 5. Provenance Requirements

All contributors must preserve attribution.

If AI assisted:

- disclose the model or agent if known
- describe what it produced
- identify the human who verified and accepted the content

If multiple humans contributed:

- identify the final accountable author in the PR
- credit subject matter reviewers where relevant

## 6. Review Etiquette

- Review for mission fit and operational consequences, not just sentence quality.
- Challenge vague wording in prompts, policies, and contracts.
- Prefer concrete counterexamples over abstract disagreement.
- Mark blocking feedback clearly.
- Resolve threads only when the artifact or rationale changed accordingly.

## 7. Historical Integrity

Do not revise status logs, decision records, or incident history unless the issue explicitly calls for a correction. If history was wrong, correct it by appending clarification, not by silently rewriting the past.

## 8. What Not to Submit

Do not submit changes that:

- optimize engagement while degrading meaning or truth-seeking
- obscure AI provenance
- weaken contributor accountability
- bypass review for policy or constitutional changes
- add process complexity without reducing ambiguity or risk

## 9. Validation

Run:

```sh
make test
```

Do not merge a PR that fails repository validation.
