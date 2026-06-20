from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FOLDERS = [
    "00_Context",
    "01_Course_Materials",
    "02_Statements",
    "03_Solution_Sources",
    "04_Solution_PDFs",
    "05_Attachments",
    "06_Formula_Sheets",
    "07_Progress_And_Feedback",
    "08_Calculation_Scripts",
    "09_Figures",
    "10_Mock_Exams",
    "11_Assignments",
]


def copy_template(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not dst.exists():
        shutil.copy2(src, dst)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new Engineering Solver Agent Kit course folder.")
    parser.add_argument("target", help="Target course folder")
    parser.add_argument("--name", default="", help="Course name")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)
    for folder in FOLDERS:
        (target / folder).mkdir(exist_ok=True)

    copy_template(
        ROOT / "templates" / "subject" / "00_COURSE_ONBOARDING.md",
        target / "00_Context" / "00_COURSE_ONBOARDING.md",
    )
    for name in [
        "STUDENT_PROFILE.md",
        "COURSE_CONTEXT.md",
        "TOPIC_EQUATION_SUMMARY.md",
        "EXAM_PROBLEM_PATTERNS.md",
        "SOLUTION_PROTOCOL.md",
        "NEW_SOLUTION_CHECKLIST.md",
    ]:
        copy_template(ROOT / "templates" / "context" / name, target / "00_Context" / name)
    copy_template(
        ROOT / "templates" / "context" / "STUDENT_PROGRESS_LOG.md",
        target / "07_Progress_And_Feedback" / "STUDENT_PROGRESS_LOG.md",
    )

    readme = target / "README_COURSE.md"
    if not readme.exists():
        readme.write_text(
            f"# {args.name or target.name}\n\n"
            "Course workspace created with Engineering Solver Agent Kit.\n\n"
            "Start with `00_Context/00_COURSE_ONBOARDING.md`.\n",
            encoding="utf-8",
        )

    print(f"Created course folder: {target}")


if __name__ == "__main__":
    main()
