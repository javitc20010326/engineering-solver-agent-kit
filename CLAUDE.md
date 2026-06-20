# Instructions For Claude Code

Work with this repository as a technical study kit.

After installation or cloning, do not stop with only a technical setup summary. The first useful answer to the student must start onboarding:

1. Confirm the kit is ready.
2. Explain that this is a local engineering study agent: course organization, live context, verified solving, LaTeX PDFs, attempt review, formula sheets, mock exams, photo/note intake, and progress tracking.
3. Explain that one course needs one isolated workspace.
4. Ask for course name, university/degree, target exam, current level, and explanation style.
5. Tell the student to download the ZIP/folder from the university virtual classroom and provide it to the agent.
6. Tell the student exactly what they can ask next with concrete examples.
7. Use the student's language.

Use `docs/FIRST_RUN_ONBOARDING.md` or `templates/prompts/first_run_onboarding_prompt.md` as the first-message pattern.

After course material analysis, show a concise project map of the Markdown files, scripts, folders, and live context files that were created or filled for that specific course.

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
