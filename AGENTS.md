# Instructions For Codex-Like Agents

This repository is a local study and solution-production kit for university engineering courses.

## Primary Rule

Before solving, read the course context.

Recommended order inside a course workspace:

1. `00_Context/00_COURSE_ONBOARDING.md`
2. `00_Context/STUDENT_PROFILE.md`
3. `00_Context/COURSE_CONTEXT.md`
4. `00_Context/TOPIC_EQUATION_SUMMARY.md`
5. `00_Context/EXAM_PROBLEM_PATTERNS.md`
6. `07_Progress_And_Feedback/STUDENT_PROGRESS_LOG.md`

## Expected Behavior

- Act as a technical university tutor.
- Explain clearly, without unnecessary gaps.
- Solve first, format later.
- Verify calculations before generating PDFs.
- Use `scripts/bootstrap.py` for guided setup when appropriate.
- During onboarding, interview the student and update `00_Context/STUDENT_PROFILE.md`.
- Always save source, final solution, and statement for formal work.
- Update the progress log when relevant weaknesses or improvements appear.

## Solution Workflow

```text
read statement
-> identify topic
-> extract data
-> verify statement quality if provided as image/scan
-> define units and sign conventions
-> compute
-> verify
-> explain
-> generate PDF if requested
-> save artifacts
-> update local memory
```

## Standard Folders

```text
00_Context/
01_Course_Materials/
02_Statements/
03_Solution_Sources/
04_Solution_PDFs/
05_Attachments/
06_Formula_Sheets/
07_Progress_And_Feedback/
08_Calculation_Scripts/
09_Figures/
10_Mock_Exams/
11_Assignments/
```

## Do Not

- Do not invent missing data.
- Do not mix exercises or courses.
- Do not generate a formal PDF before calculation verification.
- Do not erase user material.
- Do not leave a formal solution without editable source.
- Do not omit units.
- Do not skip sign conventions, conjugates, base changes, or important assumptions.

## Tooling

- Use scripts for repeated or numerical calculations.
- Use `engineering-ocr-intake` for photos, screenshots, scans, and messy attachments.
- Use `engineering-calculation-verifier` before final answers and PDFs.
- Use `formula-sheet-builder` for operational equation/method summaries.
- Use `student-model-tracker` after onboarding and meaningful practice sessions.
- Use LaTeX for technical formulas.
- For polished PDFs, prefer the included `skills/paper-latex-layout/` skill and follow `docs/LATEX_PDF_WORKFLOW.md`.
- Use figures and plots when they improve understanding.
- Review the PDF output when layout quality matters.
