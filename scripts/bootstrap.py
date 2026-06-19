from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_step(args: list[str]) -> None:
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prepare Engineering Solver Agent Kit for a new technical course."
    )
    parser.add_argument("--subject-path", help="Create a course folder at this path")
    parser.add_argument("--subject-name", default="", help="Readable course name")
    parser.add_argument("--codex-home", help="Optional Codex home folder for skill installation")
    parser.add_argument("--force-skills", action="store_true", help="Replace existing same-name Codex skills")
    args = parser.parse_args()

    print("1. Checking local tools")
    run_step(["scripts/check_environment.py"])

    if args.subject_path:
        print()
        print("2. Creating course folder")
        create_args = ["scripts/create_subject.py", args.subject_path]
        if args.subject_name:
            create_args.extend(["--name", args.subject_name])
        run_step(create_args)

    if args.codex_home:
        print()
        print("3. Installing Codex skills")
        skill_args = ["scripts/install_codex_skills.py", "--codex-home", args.codex_home]
        if args.force_skills:
            skill_args.append("--force")
        run_step(skill_args)

    print()
    print("Done. Next step: copy course materials into 01_Course_Materials and run onboarding.")


if __name__ == "__main__":
    main()
