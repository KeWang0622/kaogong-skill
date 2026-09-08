#!/usr/bin/env python3
"""Validate this repository against the Agent Skills specification.

Checks every skills/*/SKILL.md and commands/*.md for spec compliance, plus the
Claude Code plugin manifests. Exits non-zero on any error so CI can gate merges.

Spec: https://agentskills.io/specification
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_COMPATIBILITY = 500
RECOMMENDED_MAX_LINES = 500

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []
warnings: list[str] = []


def error(path: Path, msg: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def warn(path: Path, msg: str) -> None:
    warnings.append(f"{path.relative_to(ROOT)}: {msg}")


def split_frontmatter(path: Path) -> tuple[dict[str, str], str] | None:
    """Return (frontmatter, body). Minimal parser: no external deps in CI."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        error(path, "must begin with '---' on the very first line (YAML frontmatter)")
        return None
    end = text.find("\n---\n", 3)
    if end == -1:
        error(path, "frontmatter is not closed with '---'")
        return None

    fm: dict[str, str] = {}
    key = None
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")):  # nested value, e.g. under metadata:
            continue
        if ":" in raw:
            key, _, value = raw.partition(":")
            fm[key.strip()] = value.strip().strip("\"'")
    return fm, text[end + 5 :]


def check_skill(skill_md: Path) -> None:
    parsed = split_frontmatter(skill_md)
    if not parsed:
        return
    fm, body = parsed
    directory = skill_md.parent.name

    name = fm.get("name")
    if not name:
        error(skill_md, "missing required field 'name'")
    else:
        if len(name) > MAX_NAME:
            error(skill_md, f"'name' is {len(name)} chars, max {MAX_NAME}")
        if not NAME_RE.match(name):
            error(skill_md, f"'name' must be lowercase a-z0-9 and single hyphens: {name!r}")
        if name != directory:
            error(skill_md, f"'name' ({name!r}) must match its directory ({directory!r})")

    description = fm.get("description")
    if not description:
        error(skill_md, "missing required field 'description'")
    elif len(description) > MAX_DESCRIPTION:
        error(skill_md, f"'description' is {len(description)} chars, max {MAX_DESCRIPTION}")

    compatibility = fm.get("compatibility")
    if compatibility and len(compatibility) > MAX_COMPATIBILITY:
        error(skill_md, f"'compatibility' is {len(compatibility)} chars, max {MAX_COMPATIBILITY}")

    lines = len(skill_md.read_text(encoding="utf-8").splitlines())
    if lines > RECOMMENDED_MAX_LINES:
        warn(skill_md, f"{lines} lines; spec recommends keeping SKILL.md under {RECOMMENDED_MAX_LINES}")

    check_links(skill_md, body)


def check_links(path: Path, body: str) -> None:
    """Every relative markdown link must resolve to a real file."""
    for target in re.findall(r"\]\(([^)#][^)]*)\)", body):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        resolved = (path.parent / target.split("#")[0]).resolve()
        if not resolved.exists():
            error(path, f"broken relative link: {target}")


def check_json(path: Path, required: list[str]) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        error(path, f"invalid JSON: {exc}")
        return None
    for field in required:
        if field not in data:
            error(path, f"missing required field {field!r}")
    return data


def main() -> int:
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("no skills/*/SKILL.md found")
    for skill in skills:
        check_skill(skill)

    for command in sorted((ROOT / "commands").glob("*.md")):
        parsed = split_frontmatter(command)
        if parsed:
            fm, body = parsed
            if not fm.get("description"):
                error(command, "missing required field 'description'")
            check_links(command, body)

    for reference in sorted((ROOT / "skills").glob("*/references/*.md")):
        check_links(reference, reference.read_text(encoding="utf-8"))

    plugin = ROOT / ".claude-plugin" / "plugin.json"
    if plugin.exists():
        check_json(plugin, ["name"])
    else:
        error(plugin, "missing")

    marketplace = ROOT / ".claude-plugin" / "marketplace.json"
    if marketplace.exists():
        check_json(marketplace, ["name", "owner", "plugins"])

    for line in warnings:
        print(f"WARN  {line}")
    for line in errors:
        print(f"ERROR {line}")

    checked = len(skills) + len(list((ROOT / "commands").glob("*.md")))
    if errors:
        print(f"\n✗ {len(errors)} error(s) across {checked} file(s)")
        return 1
    print(f"\n✓ {checked} skill/command file(s) valid — {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
