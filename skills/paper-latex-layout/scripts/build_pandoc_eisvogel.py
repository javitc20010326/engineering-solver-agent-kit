import subprocess
import sys
from pathlib import Path


ROOT = Path.home() / ".codex" / "tools" / "paper-latex-layout"
BIN = ROOT / "bin"
MIKTEX = Path.home() / ".codex" / "tools" / "miktex"
SKILL = Path(__file__).resolve().parents[1]
PANDOC = BIN / "pandoc.exe"
TECTONIC = BIN / "tectonic.exe"
EISVOGEL = SKILL / "assets" / "eisvogel.latex"


def resolve_engine():
    pdflatex_hits = sorted(MIKTEX.glob("**/pdflatex.exe"))
    if pdflatex_hits:
        return pdflatex_hits[0]
    if TECTONIC.exists():
        return TECTONIC
    raise SystemExit(f"No LaTeX engine found. Expected pdflatex under {MIKTEX} or Tectonic at {TECTONIC}")


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python build_pandoc_eisvogel.py input.md output.pdf")
    inp = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]).resolve()
    if not inp.exists():
        raise SystemExit(f"Input not found: {inp}")
    if not PANDOC.exists():
        raise SystemExit(f"Pandoc not found: {PANDOC}")
    if not EISVOGEL.exists():
        raise SystemExit(f"Eisvogel template not found: {EISVOGEL}")
    engine = resolve_engine()
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(PANDOC),
        str(inp),
        "--from",
        "markdown+tex_math_dollars+tex_math_single_backslash+raw_tex",
        "--template",
        str(EISVOGEL),
        "--pdf-engine",
        str(engine),
        "--number-sections",
        "--toc=false",
        "-o",
        str(out),
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
