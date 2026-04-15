#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = {
    "README.md": [],
    "SDLC.md": [
        "## 1. Purpose",
        "## 4. Change Classes",
        "## 5. Lifecycle Stages",
        "## 7. Human and AI Contribution Rules",
        "## 8. Definition of Done",
        "## 12. Internal Review and Continuous Improvement",
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
        "## 9. Internal Review and Continuous Improvement",
        "## 10. Amendment Rules",
    ],
    "GITHUB-WORKFLOW.md": [
        "## 1. System of Record",
        "## 4. Pull Request Flow",
        "## 6. Merge Rules",
        "## 9. Releases and Publishing",
        "## 10. CI/CD",
    ],
    ".github/PULL_REQUEST_TEMPLATE.md": [],
    ".github/ISSUE_TEMPLATE/artifact-proposal.md": [],
    ".github/ISSUE_TEMPLATE/governance-change.md": [],
    ".github/ISSUE_TEMPLATE/eval-failure.md": [],
    ".github/workflows/validate.yml": [],
    ".github/workflows/release.yml": [],
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
    if len(templates) < 3:
        failures.append("expected at least 3 markdown issue templates")
    for path in templates:
        text = load_text(path)
        if "name:" not in text or "about:" not in text:
            failures.append(f"issue template missing front matter fields: {path.relative_to(ROOT)}")
    return failures


def validate_workflow() -> list[str]:
    validate_path = ROOT / ".github/workflows/validate.yml"
    release_path = ROOT / ".github/workflows/release.yml"

    validate_text = load_text(validate_path)
    release_text = load_text(release_path)

    required_patterns = [
        (validate_text, r"make test"),
        (validate_text, r"pull_request:"),
        (validate_text, r"push:"),
        (release_text, r"workflow_dispatch:"),
        (release_text, r"tags:"),
        (release_text, r"make test"),
    ]
    failures = []
    for text, pattern in required_patterns:
        if not re.search(pattern, text):
            failures.append(f"workflow missing pattern: {pattern}")
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
