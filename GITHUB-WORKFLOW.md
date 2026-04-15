# GitHub Workflow

## 1. System of Record

GitHub is the system of record for this repository. Issues, pull requests, reviews, and merge history are the authoritative collaboration trail.

## 2. Branching Model

- `main` is the protected default branch.
- Short-lived branches are used for all changes.
- Branch names should describe the change type and topic, for example `artifact/sdlc-package` or `governance/review-gates`.

## 3. Issue Flow

Use an issue when the change needs discussion, staging, or accountability.

Issue guidance:

- state the problem in one sentence
- identify the affected artifact
- mark the change class as `C0`, `C1`, `C2`, or `C3`
- list the expected outcome
- note any downstream repos that may need a mirror update

## 4. Pull Request Flow

Use one PR per coherent change.

PR guidance:

- keep the diff focused
- link the issue if one exists
- describe what changed and why
- document validation
- call out downstream effects
- disclose AI involvement and human accountability when AI assistance was used

## 5. Review Rules

- Small editorial changes need one maintainer approval.
- `C1` local behavior changes need one maintainer or steward approval.
- `C2` shared contract or policy changes need steward approval plus one additional authorized reviewer.
- `C3` constitutional changes need two human steward approvals, one of which must be a core maintainer.
- Automation-generated changes do not self-approve.

## 6. Merge Rules

Merge only when:

- the review path is complete
- validation has been run
- the PR description matches the actual change
- any downstream mirror implications are stated

Prefer squash merges for discrete process changes so the history stays readable.

## 7. Labels

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
- `type:downstream`
- `status:draft`
- `status:blocked`
- `needs:review`
- `needs:steward`

## 8. Templates

Repository templates should make the expected shape of work obvious. The templates in `.github/` are intentionally short and opinionated.

## 9. Releases and Publishing

This repository is published on GitHub as versioned source artifacts rather than as a deployed runtime.

- Tag releases when a coherent set of prompt-native source changes is ready for downstream use.
- Use the release workflow to publish a GitHub Release that summarizes the change set and points to the tagged source snapshot.
- Treat the release as the public handoff point for downstream consumers, documentation readers, and mirror repositories.

## 10. CI/CD

Continuous integration runs repository validation on pushes and pull requests.

Continuous delivery runs on tagged releases and publishes the versioned source snapshot plus release notes.

The baseline expectation is that CI fails fast on missing process files, missing required headings, or malformed templates, while CD remains lightweight enough to work for a source-artifact repository before any product runtime exists.
