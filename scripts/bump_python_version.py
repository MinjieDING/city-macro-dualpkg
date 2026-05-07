from __future__ import annotations

import re
import sys
from pathlib import Path


def bump_semver(version: str, part: str) -> str:
    major, minor, patch = map(int, version.split("."))
    if part == "patch":
        patch += 1
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "major":
        major += 1
        minor = 0
        patch = 0
    else:
        raise ValueError("part must be one of: patch, minor, major")
    return f"{major}.{minor}.{patch}"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/bump_python_version.py [patch|minor|major]")

    part = sys.argv[1].strip().lower()
    root = Path(__file__).resolve().parents[1]
    pyproject = root / "python-pkg" / "pyproject.toml"
    content = pyproject.read_text(encoding="utf-8")

    match = re.search(r'^version\s*=\s*"(\d+\.\d+\.\d+)"\s*$', content, flags=re.MULTILINE)
    if not match:
        raise SystemExit("Cannot find [project].version in pyproject.toml")

    old_version = match.group(1)
    new_version = bump_semver(old_version, part)
    updated = content.replace(f'version = "{old_version}"', f'version = "{new_version}"', 1)
    pyproject.write_text(updated, encoding="utf-8")
    print(f"Version bumped: {old_version} -> {new_version}")


if __name__ == "__main__":
    main()
