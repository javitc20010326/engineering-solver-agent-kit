# Engineering Solver Agent Kit

![Engineering Solver Agent Kit cover](assets/cover.png)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)
![LaTeX](https://img.shields.io/badge/LaTeX-pdflatex%20%7C%20xelatex-008080)
![Pandoc](https://img.shields.io/badge/Pandoc-recommended-555555)
![Codex](https://img.shields.io/badge/Agent-Codex%20%7C%20Claude%20Code-111827)
![License](https://img.shields.io/badge/license-MIT-green)

**Engineering Solver Agent Kit** is a local agentic study framework for university engineering courses. It turns Codex or Claude Code into a structured technical tutor that can onboard a course, index teaching material, solve problems step by step, verify calculations, generate LaTeX-rendered PDFs, keep editable solution sources, and maintain a live record of the student's progress.

The core idea is simple:

```text
one course -> one local workspace -> one agent memory -> verified solved problems
```

This kit is designed for technical subjects where the student needs more than final answers: formulas, assumptions, unit conversions, sign conventions, numerical checks, diagrams, plots, and professionally formatted solution PDFs.

## What This Repository Contains

This is not a single prompt or a simple notes template. It is a complete local study system composed of several coordinated parts:

1. **Agent instructions**
   - `AGENTS.md` for Codex-like agents.
   - `CLAUDE.md` for Claude Code.
   - Shared behavioral rules for technical tutoring, calculation-first solving, and local artifact management.

2. **Reusable agent skills**
   - `study-onboarding`: course setup, material inspection, and live context initialization.
   - `study-problem-solver`: engineering problem solving, verification, and attempt review.
   - `study-latex-pdf`: formal solution writing, LaTeX math rendering, PDF generation, and visual QA.

3. **Course workspace architecture**
   - A complete folder structure for one technical course.
   - Separate areas for course material, statements, editable solutions, PDFs, attachments, formula sheets, scripts, figures, mock exams, and assignments.

4. **Live memory files**
   - Course context.
   - Topic and equation summary.
   - Exam problem patterns.
   - Solution protocol.
   - Student progress and feedback log.

5. **Engineering solution protocols**
   - Data extraction.
   - Unit and sign-convention checks.
   - Formula selection.
   - Step-by-step substitution.
   - Numerical verification.
   - Final answer formatting.
   - Error prevention checklist.

6. **LaTeX/PDF production workflow**
   - Markdown/LaTeX source files.
   - Rendered equations.
   - Tables for repeated calculations.
   - Figures and plots when useful.
   - PDF compilation workflow using local tools.

7. **Local automation scripts**
   - Environment checker.
   - Course workspace creator.
   - Guided bootstrap script.
   - Image-to-PDF converter.
   - Material indexer.
   - Solution listing utility.
   - Statement/solution pairing checker.
   - PDF build helper.
   - Codex skill installer.

8. **Software/tooling assumptions**
   - Python runtime.
   - PowerShell or equivalent terminal.
   - LaTeX engine such as `pdflatex` or `xelatex`.
   - Optional Pandoc workflow.
   - Optional Python packages for images, PDF processing, plotting, and numerical checks.

9. **Student interaction patterns**
   - Solved problem mode.
   - Attempt review mode.
   - Formula sheet mode.
   - Learning/explanation mode.
   - Mock exam mode.
   - Fast revision mode.

10. **Templates and examples**
    - Course onboarding templates.
    - Context templates.
    - Problem solution templates.
    - Attempt review templates.
    - Formula sheet entries.
    - A minimal demo engineering course.

## What It Does

- Builds a local course workspace from teaching material.
- Maintains live context files for topics, equations, exam patterns, and student progress.
- Solves engineering problems with explicit assumptions, formulas, substitutions, and verification.
- Produces editable Markdown/LaTeX sources and final PDF solutions.
- Stores statements, attached images, scripts, figures, and solved outputs in predictable folders.
- Supports attempt review: the agent can compare the student's handwritten or typed solution against the correct procedure.
- Supports formula sheets, mock exams, assignment-style problems, and fast revision workflows.
- Provides reusable Codex skills for onboarding, problem solving, and LaTeX/PDF generation.

## Target Users

This repository is intended for engineering students who want to study a technical subject with an AI agent while keeping a rigorous local archive:

- solved exercises;
- exam problems;
- assignment problems;
- formula sheets;
- derivations;
- calculation scripts;
- figures and plots;
- progress tracking.

It is especially useful for subjects such as electrical power systems, circuits, control, signals, mechanics, thermodynamics, structures, numerical methods, and similar calculation-heavy courses.

## What This Is Not

- It is not a repository of notes for a specific university course.
- It does not include copyrighted teaching material.
- It does not replace the student's own reasoning or teacher feedback.
- It does not guarantee correctness without verification.

The agent must calculate first, verify second, and only then write the final explanation.

## Quick Start

1. Copy or clone this repository.
2. Open the repository with Codex or Claude Code.
3. Ask the agent:

```text
Read this repository, inspect README.md, AGENTS.md, and docs/INSTALLATION_AND_REQUIREMENTS.md.
Prepare a new engineering course workspace with this kit and tell me what course material I should provide.
```

4. Put the course material for one subject only into the generated workspace.
5. Ask for solved problems, attempt reviews, formula sheets, or mock exams.

## Recommended Tooling

Minimum:

- Codex or Claude Code.
- Python 3.10 or newer.
- A terminal: PowerShell on Windows or an equivalent shell on Linux/macOS.
- Git.

Recommended for professional PDFs and visual verification:

- A LaTeX distribution: MiKTeX, TeX Live, or TinyTeX.
- `pdflatex` and/or `xelatex`.
- Pandoc.
- Python packages: Pillow, PyMuPDF, matplotlib, numpy.

Install recommended Python packages:

```text
python -m pip install -r requirements.txt
```

Check the local environment:

```text
python scripts/check_environment.py
```

Guided preparation:

```text
python scripts/bootstrap.py --subject-path "Courses/Circuits_I" --subject-name "Circuits I"
```

Create only the course workspace:

```text
python scripts/create_subject.py "Courses/Circuits_I" --name "Circuits I"
```

Install the included Codex skills:

```text
python scripts/install_codex_skills.py --codex-home PATH_TO_CODEX_HOME
```

## Course Workspace Layout

Each subject must have its own workspace. Do not mix courses.

```text
00_Context/                 live course memory
01_Course_Materials/        theory, slides, assignments, exams, solutions
02_Statements/              clean problem statements
03_Solution_Sources/        editable Markdown/LaTeX sources
04_Solution_PDFs/           final PDF solutions
05_Attachments/             original student images and captures
06_Formula_Sheets/          compact formula sheets and summaries
07_Progress_And_Feedback/   live student level, mistakes, corrections
08_Calculation_Scripts/     Python/MATLAB/etc. verification scripts
09_Figures/                 plots and diagrams used in PDFs
10_Mock_Exams/              generated practice exams
11_Assignments/             assignment-style exercises and deliverables
```

## Agent Workflow

For a formal problem solution, the agent should follow this sequence:

1. Read the statement and classify the topic.
2. Extract data, units, known variables, and unknowns.
3. State assumptions and sign conventions.
4. Choose the governing equations.
5. Compute the result independently before writing the solution.
6. Verify by dimensional checks, limiting cases, alternative formulas, or scripts.
7. Write the explanation in a university-level but readable style.
8. Generate figures when they clarify the method.
9. Produce a polished PDF with rendered LaTeX math.
10. Save statement, source, PDF, figures, scripts, and progress notes locally.

The priority is not just getting the numerical answer. The priority is making the method reproducible.

## Key Documents

```text
docs/HOW_TO_WORK_WITH_THE_AGENT.md
docs/COURSE_ONBOARDING_GUIDE.md
docs/INSTALLATION_AND_REQUIREMENTS.md
docs/COURSE_WORKSPACE_STRUCTURE.md
docs/LIVE_FILES_MAP.md
docs/LATEX_PDF_WORKFLOW.md
docs/ERROR_PREVENTION_PROTOCOL.md
docs/SOLUTION_PROTOCOL.md
docs/QA_CHECKLIST.md
```

## Included Skills

```text
skills/study-onboarding/
skills/study-problem-solver/
skills/study-latex-pdf/
```

These skills define the core behavior:

- course onboarding;
- rigorous engineering problem solving;
- LaTeX/PDF production with calculation-first verification.

## License

MIT. See `LICENSE`.
