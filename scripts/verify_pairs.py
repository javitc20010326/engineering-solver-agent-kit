from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify that each solution PDF has a matching statement PDF.")
    parser.add_argument("course", help="Course folder")
    parser.add_argument("--statements", default="02_Statements")
    parser.add_argument("--solutions", default="04_Solution_PDFs")
    args = parser.parse_args()

    course = Path(args.course).resolve()
    statements = course / args.statements
    solutions = course / args.solutions

    missing = []
    for solution in sorted(solutions.glob("*.pdf")):
        expected = statements / f"{solution.stem}_statement.pdf"
        if not expected.exists():
            missing.append((solution.name, expected.name))

    if not missing:
        print("OK: every solution has a matching statement.")
        return

    print("Missing statement PDFs:")
    for solution, expected in missing:
        print(f"- {solution} -> expected {expected}")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
