import argparse
import shutil
import subprocess
import sys
from pathlib import Path


TOOL_ROOT = Path.home() / ".codex" / "tools" / "paper-latex-layout"
MIKTEX_ROOT = Path.home() / ".codex" / "tools" / "miktex"
SKILL_ROOT = Path(__file__).resolve().parents[1]
EISVOGEL = SKILL_ROOT / "assets" / "eisvogel.latex"


def first_existing(paths):
    for path in paths:
        if path and Path(path).exists():
            return Path(path)
    return None


def resolve_tool(name):
    if name == "pandoc":
        hit = first_existing([TOOL_ROOT / "bin" / "pandoc.exe", shutil.which("pandoc")])
    elif name == "tectonic":
        hit = first_existing([TOOL_ROOT / "bin" / "tectonic.exe", shutil.which("tectonic")])
    elif name == "pdflatex":
        miktex_hits = sorted(MIKTEX_ROOT.glob("**/pdflatex.exe"))
        hit = first_existing([*(miktex_hits[:1]), shutil.which("pdflatex")])
    else:
        hit = first_existing([shutil.which(name)])
    if not hit:
        raise SystemExit(f"{name} not found. Run scripts/check_environment.py and install the missing tool.")
    return hit


def choose_engine(requested):
    if requested != "auto":
        return resolve_tool(requested)
    try:
        return resolve_tool("pdflatex")
    except SystemExit:
        return resolve_tool("tectonic")


def pandoc_base(inp, out, engine):
    cmd = [
        str(resolve_tool("pandoc")),
        str(inp),
        "--from",
        "markdown+tex_math_dollars+tex_math_single_backslash+implicit_figures+raw_tex",
        "--resource-path",
        str(inp.parent),
        "--pdf-engine",
        str(engine),
        "--number-sections",
        "--toc=false",
        "-o",
        str(out),
    ]
    if engine.name.lower() == "pdflatex.exe":
        cmd.extend(
            [
                "--pdf-engine-opt=-interaction=nonstopmode",
                "--pdf-engine-opt=-halt-on-error",
                "--pdf-engine-opt=-file-line-error",
            ]
        )
    return cmd


def add_classic_style(cmd):
    cmd.extend(
        [
            "-V",
            "documentclass=article",
            "-V",
            "papersize=a4",
            "-V",
            "geometry=margin=2.05cm",
            "-V",
            "fontsize=11pt",
            "-V",
            "linestretch=1.04",
            "-V",
            "colorlinks=true",
            "-V",
            "linkcolor=black",
            "-V",
            "urlcolor=black",
        ]
    )


def add_eisvogel_style(cmd):
    if not EISVOGEL.exists():
        raise SystemExit(f"Eisvogel template not found: {EISVOGEL}")
    cmd.extend(["--template", str(EISVOGEL)])


def main():
    parser = argparse.ArgumentParser(description="Build a polished LaTeX PDF from Markdown.")
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument("output", help="Output PDF file")
    parser.add_argument("--style", choices=["classic", "eisvogel"], default="classic")
    parser.add_argument("--engine", choices=["auto", "pdflatex", "tectonic"], default="auto")
    args = parser.parse_args()

    inp = Path(args.input).resolve()
    out = Path(args.output).resolve()
    if not inp.exists():
        raise SystemExit(f"Input not found: {inp}")
    out.parent.mkdir(parents=True, exist_ok=True)

    engine = choose_engine(args.engine)
    cmd = pandoc_base(inp, out, engine)
    if args.style == "classic":
        add_classic_style(cmd)
    else:
        add_eisvogel_style(cmd)

    result = subprocess.run(cmd, check=False, timeout=240)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    sys.exit(main())
