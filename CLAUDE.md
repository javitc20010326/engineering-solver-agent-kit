# Instructions For Claude Code

Work with this repository as a technical study kit.

When creating or preparing a course workspace:

1. Use `scripts/bootstrap.py` or `scripts/create_subject.py` if the structure does not exist.
2. Read `00_Context/00_COURSE_ONBOARDING.md`.
3. Interview the student and update `00_Context/STUDENT_PROFILE.md`.
4. Inspect available course material.
5. Create or update live context files.
6. Explain to the student how to request solutions, reviews, formula sheets, and mock exams.

When solving:

1. Extract data.
2. If input is a photo/scan, prepare the statement using `engineering-ocr-intake`.
3. Identify the topic and method.
4. Calculate and verify with `engineering-calculation-verifier`.
5. Write the explanation step by step.
6. If a PDF is requested, follow `docs/LATEX_PDF_WORKFLOW.md` and prefer the included `skills/paper-latex-layout/` production skill.
7. Save statement, source, PDF, calculations, and figures when relevant.
8. Update the progress log if needed.

Maintain a technical tutor style: clear, concrete, verifiable.
