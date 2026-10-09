"""Validate skills/finch against the Agent Skills spec and repo conventions.

Usage: uv run python scripts/validate.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "finch"
ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.index("\n---\n", 4)
    raw, body = text[4:end], text[end + 5 :]
    fields: dict = {}
    current = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            if current is None:
                raise ValueError(f"indented line outside a mapping: {line!r}")
            key, _, value = line.strip().partition(":")
            fields[current][key.strip()] = value.strip().strip('"')
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value:
            fields[key] = value
            current = None
        else:
            fields[key] = {}
            current = key
    return fields, body


def main() -> int:
    errors: list[str] = []
    skill_md = SKILL_DIR / "SKILL.md"
    text = skill_md.read_text()
    fields, body = parse_frontmatter(text)

    extra = set(fields) - ALLOWED_FIELDS
    if extra:
        errors.append(f"non-standard frontmatter fields: {sorted(extra)}")
    name = fields.get("name", "")
    if not (1 <= len(name) <= 64 and NAME_RE.match(name)):
        errors.append(f"invalid name: {name!r}")
    if name != SKILL_DIR.name:
        errors.append(f"name {name!r} does not match directory {SKILL_DIR.name!r}")
    desc = fields.get("description", "")
    if not (1 <= len(desc) <= 1024):
        errors.append(f"description length {len(desc)} not in 1..1024")
    if "compatibility" in fields and len(fields["compatibility"]) > 500:
        errors.append("compatibility longer than 500 chars")

    n_lines = text.count("\n") + 1
    if n_lines > 500:
        errors.append(f"SKILL.md has {n_lines} lines (> 500)")

    # Check portable resource paths regardless of backticks, Markdown links, or fences.
    resources = set(re.findall(r"(?:references|scripts)/[\w./-]+\.(?:md|py)", body))
    for ref in sorted(resources):
        target = (SKILL_DIR / ref).resolve()
        if not target.is_relative_to(SKILL_DIR.resolve()) or not target.is_file():
            errors.append(f"broken or non-portable resource: {ref}")
    for resource in (SKILL_DIR / "references").rglob("*.md"):
        relative = resource.relative_to(SKILL_DIR).as_posix()
        if resource.parent != SKILL_DIR / "references":
            errors.append(f"reference must be one level deep: {relative}")
        if relative not in resources:
            errors.append(f"reference has no route from SKILL.md: {relative}")
    for script in (SKILL_DIR / "scripts").glob("*.py"):
        if script.relative_to(SKILL_DIR).as_posix() not in resources:
            errors.append(f"script has no route from SKILL.md: {script.name}")
    license_file = SKILL_DIR / "LICENSE"
    if not license_file.is_file() or license_file.read_text() != (ROOT / "LICENSE").read_text():
        errors.append("installable skill must carry the repository LICENSE")

    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    version = fields.get("metadata", {}).get("version")
    if plugin.get("version") != version:
        errors.append(f"version mismatch: SKILL.md {version} vs plugin.json {plugin.get('version')}")
    json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    json.loads((ROOT / "evals" / "evals.json").read_text())

    words = len(body.split())
    print(f"SKILL.md: {n_lines} lines, ~{words} words in body, description {len(desc)} chars")
    for ref in sorted((SKILL_DIR / "references").glob("*.md")):
        print(f"  {ref.relative_to(SKILL_DIR)}: {ref.read_text().count(chr(10)) + 1} lines")
    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
