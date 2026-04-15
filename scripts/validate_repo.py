#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = {
    "README.md": [],
    "SPEC.md": [
        "## 1. Project Identity",
        "## 2. Mission",
        "## 9. Core Domain Model",
    ],
    "SDLC.md": [
        "## 1. Purpose",
        "## 4. Change Classes",
        "## 5. Lifecycle Stages",
        "## 7. Human and AI Contribution Rules",
        "## 8. Definition of Done",
        "## 9. Continuous Improvement Review",
    ],
    "CONTRIBUTING.md": [
        "## 1. Before You Start",
        "## 2. Contributor Workflow",
        "## 9. Validation",
    ],
    "GOVERNANCE.md": [
        "## 1. Governance Objective",
        "## 3. Decision Rights",
        "## 5. Escalation Path",
        "## 9. Amendment Rules",
    ],
    "GITHUB-WORKFLOW.md": [
        "## 1. System of Record",
        "## 4. Pull Request Flow",
        "## 6. Merge Rules",
        "## 8. Internal Review Loop",
    ],
    "CODE_OF_CONDUCT.md": [],
    "SECURITY.md": [],
    ".github/PULL_REQUEST_TEMPLATE.md": [],
    ".github/ISSUE_TEMPLATE/artifact-proposal.md": [],
    ".github/ISSUE_TEMPLATE/governance-change.md": [],
    ".github/ISSUE_TEMPLATE/eval-failure.md": [],
    ".github/ISSUE_TEMPLATE/internal-review.md": [],
    ".github/workflows/validate.yml": [],
    ".github/workflows/release.yml": [],
    ".github/workflows/internal-review.yml": [],
    "decisions/README.md": [],
}


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_required_files() -> list[str]:
    failures: list[str] = []
    for relative_path, required_headings in REQUIRED_FILES.items():
        path = ROOT / relative_path
        if not path.exists():
            failures.append(f"missing required file: {relative_path}")
            continue
        text = load_text(path)
        for heading in required_headings:
            if heading not in text:
                failures.append(f"missing heading in {relative_path}: {heading}")
    return failures


def validate_pr_template() -> list[str]:
    path = ROOT / ".github/PULL_REQUEST_TEMPLATE.md"
    text = load_text(path)
    required_phrases = [
        "Change class",
        "Artifact class",
        "Evidence",
        "AI involvement",
        "Risks",
    ]
    return [
        f"missing PR template field: {phrase}"
        for phrase in required_phrases
        if phrase not in text
    ]


def validate_issue_templates() -> list[str]:
    failures: list[str] = []
    issue_dir = ROOT / ".github/ISSUE_TEMPLATE"
    templates = sorted(issue_dir.glob("*.md"))
    if len(templates) < 4:
        failures.append("expected at least 4 markdown issue templates")
    for path in templates:
        text = load_text(path)
        if "name:" not in text or "about:" not in text:
            failures.append(
                f"issue template missing front matter fields: {path.relative_to(ROOT)}"
            )
    return failures


def validate_workflow() -> list[str]:
    failures: list[str] = []

    validate_text = load_text(ROOT / ".github/workflows/validate.yml")
    for pattern in [r"make test", r"pull_request:", r"push:"]:
        if not re.search(pattern, validate_text):
            failures.append(f"validate workflow missing pattern: {pattern}")

    release_text = load_text(ROOT / ".github/workflows/release.yml")
    for pattern in [r"push:", r"tags:", r"actions/create-release@"]:
        if not re.search(pattern, release_text):
            failures.append(f"release workflow missing pattern: {pattern}")

    review_text = load_text(ROOT / ".github/workflows/internal-review.yml")
    for pattern in [r"schedule:", r"workflow_dispatch:", r"cron:"]:
        if not re.search(pattern, review_text):
            failures.append(f"internal review workflow missing pattern: {pattern}")

    return failures


def main() -> int:
    failures = []
    failures.extend(validate_required_files())
    failures.extend(validate_pr_template())
    failures.extend(validate_issue_templates())
    failures.extend(validate_workflow())

    if failures:
        print("Repository validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
