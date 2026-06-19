from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Index local course materials.")
    parser.add_argument("course", help="Course folder")
    parser.add_argument("--output", default="00_Context/MATERIAL_INDEX.md")
    args = parser.parse_args()

    course = Path(args.course).resolve()
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in course.rglob("*"):
        if path.is_file():
            if any(part.startswith(".") for part in path.relative_to(course).parts):
                continue
            groups[path.suffix.lower() or "[sin_extension]"].append(path)

    lines = ["# Indice de material\n"]
    for ext in sorted(groups):
        lines.append(f"\n## {ext}\n")
        for path in sorted(groups[ext]):
            lines.append(f"- `{path.relative_to(course)}`")

    out = course / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
