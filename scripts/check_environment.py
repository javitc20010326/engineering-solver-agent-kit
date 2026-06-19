from __future__ import annotations

import importlib.util
import shutil
import sys


COMMANDS = [
    ("git", "Git"),
    ("pandoc", "Pandoc"),
    ("pdflatex", "LaTeX pdflatex"),
    ("xelatex", "LaTeX xelatex"),
]

PYTHON_PACKAGES = [
    ("PIL", "Pillow"),
    ("fitz", "PyMuPDF"),
    ("matplotlib", "matplotlib"),
    ("numpy", "numpy"),
]


def status(ok: bool) -> str:
    return "OK" if ok else "MISSING"


def main() -> None:
    print("Engineering Solver Agent Kit - environment check")
    print()
    print(f"Python: {sys.version.split()[0]} ({sys.executable})")
    print()
    print("Commands:")
    for command, label in COMMANDS:
        found = shutil.which(command)
        print(f"- {label}: {status(found is not None)}" + (f" -> {found}" if found else ""))

    print()
    print("Python packages:")
    for module, label in PYTHON_PACKAGES:
        ok = importlib.util.find_spec(module) is not None
        print(f"- {label}: {status(ok)}")

    print()
    print("Minimum useful setup: Python + agent app.")
    print("Recommended PDF setup: pandoc + pdflatex/xelatex + Pillow + PyMuPDF + matplotlib + numpy.")


if __name__ == "__main__":
    main()
