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
  - numpy;
  - reportlab.

The repository includes the full `paper-latex-layout` skill under:

```text
skills/paper-latex-layout/
```

That skill contains the PDF build scripts, Windows wrappers, Eisvogel LaTeX template, DOCX export helper, and PDF rendering utilities. It does not bundle heavy binaries such as a full TeX distribution or Pandoc executable; those should be installed on the student's machine or provided by the agent runtime.

Install Python packages:

```text
python -m pip install -r requirements.txt
```

Check the environment:

```text
python scripts/check_environment.py
```

Print the first-run onboarding message:

```text
python scripts/first_run_message.py --lang en
```

Spanish version:

```text
python scripts/first_run_message.py --lang es
```

Guided setup:

```text
python scripts/bootstrap.py --subject-path "Courses/Circuits_I" --subject-name "Circuits I"
```

Guided setup can also print the first-run message in Spanish:

```text
python scripts/bootstrap.py --subject-path "Courses/Circuits_I" --subject-name "Circuits I" --onboarding-lang es
```

Install Codex skills:

```text
python scripts/install_codex_skills.py --codex-home PATH_TO_CODEX_HOME
```

For Spanish onboarding output:

```text
python scripts/install_codex_skills.py --codex-home PATH_TO_CODEX_HOME --onboarding-lang es
```

This installs all included skills, including:

```text
engineering-ocr-intake
engineering-calculation-verifier
formula-sheet-builder
student-model-tracker
study-onboarding
study-problem-solver
study-latex-pdf
paper-latex-layout
```

By default, existing skills with the same name are not overwritten. To replace them:

```text
python scripts/install_codex_skills.py --codex-home PATH_TO_CODEX_HOME --force
```

## Important Rule

Create one workspace per course. Do not mix materials from multiple courses in the same folder.
