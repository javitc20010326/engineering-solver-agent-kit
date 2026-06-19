from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="List solution PDFs in a course folder.")
    parser.add_argument("course", help="Course folder")
    parser.add_argument("--solutions", default="04_Solution_PDFs")
    args = parser.parse_args()

    course = Path(args.course).resolve()
    folder = course / args.solutions
    for i, pdf in enumerate(sorted(folder.glob("*.pdf")), start=1):
        print(f"{i}. {pdf.name}")


if __name__ == "__main__":
    main()
