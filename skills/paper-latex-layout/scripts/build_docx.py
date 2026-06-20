import argparse
import shutil
import subprocess
from pathlib import Path


TOOL_ROOT = Path.home() / ".codex" / "tools" / "paper-latex-layout"


def resolve_pandoc():
    local = TOOL_ROOT / "bin" / "pandoc.exe"
    if local.exists():
        return local
    hit = shutil.which("pandoc")
    if hit:
        return Path(hit)
    raise SystemExit("pandoc not found. Install Pandoc or run scripts/check_environment.py.")


def main():
    parser = argparse.ArgumentParser(description="Build a DOCX from Markdown via Pandoc.")
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument("output", help="Output DOCX file")
    args = parser.parse_args()

    inp = Path(args.input).resolve()
    out = Path(args.output).resolve()
    if not inp.exists():
        raise SystemExit(f"Input not found: {inp}")
    out.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        str(resolve_pandoc()),
        str(inp),
        "--from",
        "markdown+tex_math_dollars+tex_math_single_backslash+implicit_figures+raw_tex",
        "--resource-path",
        str(inp.parent),
        "-o",
        str(out),
    ]
    raise SystemExit(subprocess.run(cmd, check=False, timeout=180).returncode)


if __name__ == "__main__":
    main()
