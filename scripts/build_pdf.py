from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a PDF from Markdown using pandoc if available.")
    parser.add_argument("source", help="Markdown source")
    parser.add_argument("output", help="Output PDF")
    parser.add_argument("--pdf-engine", default="pdflatex")
    args = parser.parse_args()

    if shutil.which("pandoc") is None:
        raise SystemExit("pandoc not found. Install pandoc or use another PDF workflow.")

    source = Path(args.source)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "pandoc",
        str(source),
        "-o",
        str(output),
        "--pdf-engine",
        args.pdf_engine,
    ]
    subprocess.run(cmd, check=True)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
