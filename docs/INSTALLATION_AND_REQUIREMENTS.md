# Installation And Requirements

This kit is local-first. It works best when the machine can calculate, render figures, and compile LaTeX PDFs.

## Minimum Requirements

- Codex or Claude Code.
- Python 3.10 or newer.
- Git.
- Terminal:
  - PowerShell on Windows;
  - shell equivalent on Linux/macOS.

## Recommended PDF Stack

- LaTeX distribution:
  - MiKTeX on Windows;
  - TeX Live on Linux/macOS;
  - TinyTeX as a lightweight alternative.
- `pdflatex` and/or `xelatex`.
- Pandoc.
- Python packages:
  - Pillow;
  - PyMuPDF;
  - matplotlib;
  - numpy.

Install Python packages:

```text
python -m pip install -r requirements.txt
```

Check the environment:

```text
python scripts/check_environment.py
```

Guided setup:

```text
python scripts/bootstrap.py --subject-path "Courses/Circuits_I" --subject-name "Circuits I"
```

Install Codex skills:

```text
python scripts/install_codex_skills.py --codex-home PATH_TO_CODEX_HOME
```

By default, existing skills with the same name are not overwritten. To replace them:

```text
python scripts/install_codex_skills.py --codex-home PATH_TO_CODEX_HOME --force
```

## Important Rule

Create one workspace per course. Do not mix materials from multiple courses in the same folder.
