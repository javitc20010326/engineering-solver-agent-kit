from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from first_run_message import get_message


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def main() -> None:
    parser = argparse.ArgumentParser(description="Copy Engineering Solver Agent Kit skills into a Codex skills folder.")
    parser.add_argument("--codex-home", required=True, help="Codex home folder")
    parser.add_argument("--force", action="store_true", help="Replace existing skills with the same name")
    parser.add_argument("--onboarding-lang", choices=["en", "es"], default="en", help="Language for the first-run onboarding message")
    args = parser.parse_args()

    codex_home = Path(args.codex_home).expanduser().resolve()
    target = codex_home / "skills"
    target.mkdir(parents=True, exist_ok=True)

    copied = []
    for skill_dir in SKILLS.iterdir():
        if not skill_dir.is_dir():
            continue
        dst = target / skill_dir.name
        if dst.exists():
            if not args.force:
                print(f"Skipped existing skill: {dst}")
                continue
            shutil.rmtree(dst)
        shutil.copytree(skill_dir, dst)
        copied.append(skill_dir.name)

    print(f"Copied {len(copied)} skills to {target}")
    for name in copied:
        print(f"- {name}")
    print()
    print("First-run onboarding message:")
    print()
    print(get_message(args.onboarding_lang))


if __name__ == "__main__":
    main()
