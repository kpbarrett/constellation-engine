# GitHub Workflow

## 1. System of Record

GitHub is the system of record for this repository. Issues, pull requests, reviews, releases, and merge history are the authoritative collaboration trail.

## 2. Branching Model

- `main` is the protected default branch.
- All work lands through short-lived branches.
- Branch names should describe the change type and topic, for example `artifact/participant-contracts` or `governance/review-cadence`.

## 3. Issue Flow

Use an issue when the change needs discussion, staging, or accountability.

Issue guidance:

- state the problem in one sentence
- identify the affected artifact
- mark the proposed change class as `C0`, `C1`, `C2`, or `C3`
- list the expected outcome
- note downstream systems or repositories that may be affected

## 4. Pull Request Flow

Use one pull request per coherent change.

PR guidance:

- keep the diff focused
- link the issue when one exists
- describe what changed and why
- document validation
- call out downstream effects
- disclose AI involvement and human accountability when AI assistance was used

## 5. Review Rules

- C0 editorial changes need one authorized reviewer.
- C1 local behavior changes need one maintainer or steward approval.
- C2 shared contract or policy changes need steward approval plus one additional authorized reviewer.
- C3 constitutional changes need two human steward approvals, one of which must be a core maintainer.
- Automation-generated changes do not self-approve.

## 6. Merge Rules

Merge only when:

- the review path is complete
- `make test` has passed
- the PR description matches the actual change
- downstream and release implications are documented

Prefer squash merges for discrete process and artifact changes so history stays readable.

## 7. Release Flow

- tag releases from `main`
- let GitHub Actions publish the GitHub release from the tag
- summarize notable changes, risks, and migration notes in release notes
- link any open follow-up incident or governance issues when relevant

## 8. Internal Review Loop

- GitHub Actions opens an internal SDLC review issue every 30 days
- maintainers use that issue to record where the process is helping, where it is slowing work down, and what should change next
- concrete process changes should spin out into normal issues and pull requests rather than being handled informally

## 9. Labels

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
- `needs:review`
- `needs:steward`
- `needs-evals`
- `status:blocked`
- `status:draft`

## 10. Templates

Repository templates should make expected workflow obvious. The templates under `.github/` are intentionally short and opinionated so contributors can classify work quickly.
