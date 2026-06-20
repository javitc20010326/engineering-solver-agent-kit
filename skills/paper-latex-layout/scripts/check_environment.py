import shutil
import subprocess
from pathlib import Path


TOOL_ROOT = Path.home() / ".codex" / "tools" / "paper-latex-layout"
MIKTEX_ROOT = Path.home() / ".codex" / "tools" / "miktex"


def candidates(name):
    local = []
    if name == "pandoc":
        local.append(TOOL_ROOT / "bin" / "pandoc.exe")
    if name == "tectonic":
        local.append(TOOL_ROOT / "bin" / "tectonic.exe")
    if name == "pdflatex":
        local.extend(MIKTEX_ROOT.glob("**/pdflatex.exe"))
    path_hit = shutil.which(name)
    if path_hit:
        local.append(Path(path_hit))
    return [p for p in local if p.exists()]


def version(path):
    try:
        result = subprocess.run(
            [str(path), "--version"],
            check=False,
            capture_output=True,
            text=True,
            timeout=15,
        )
        first = (result.stdout or result.stderr).splitlines()[0]
        return first.strip()
    except Exception as exc:
        return f"version check failed: {exc}"


def main():
    for tool in ["pandoc", "pdflatex", "tectonic"]:
        found = candidates(tool)
        if not found:
            print(f"{tool}: NOT FOUND")
            continue
        print(f"{tool}: {found[0]}")
        print(f"  {version(found[0])}")


if __name__ == "__main__":
    main()
