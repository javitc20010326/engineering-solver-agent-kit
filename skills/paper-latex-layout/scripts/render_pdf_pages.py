import sys
import shutil
import argparse
from pathlib import Path


def add_dependency_paths():
    dep = Path.home() / ".codex" / "tools" / "paper-latex-layout" / "pydeps"
    if dep.exists():
        sys.path.insert(0, str(dep))


try:
    import fitz
except (ImportError, PermissionError):
    add_dependency_paths()
    import fitz


def main():
    parser = argparse.ArgumentParser(description="Render PDF pages to PNG for visual QA.")
    parser.add_argument("input_pdf")
    parser.add_argument("output_dir")
    parser.add_argument(
        "--mode",
        choices=["quick", "full"],
        default="quick",
        help="quick renders first and last page; full renders every page.",
    )
    args = parser.parse_args()

    pdf = Path(args.input_pdf).resolve()
    out = Path(args.output_dir).resolve()
    if not pdf.exists():
        raise SystemExit(f"PDF not found: {pdf}")
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf)
    if args.mode == "quick":
        indexes = sorted(set([0, doc.page_count - 1]))
    else:
        indexes = list(range(doc.page_count))
    for i in indexes:
        page = doc[i]
        pix = page.get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False)
        pix.save(out / f"page_{i+1}.png")
    print(f"Rendered {len(indexes)} of {doc.page_count} pages to {out}")


if __name__ == "__main__":
    main()
