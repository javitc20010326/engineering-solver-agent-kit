# First Run Onboarding Protocol

This document defines what the agent must do immediately after the kit is installed.

The student should not be left with only a technical installation report. The first response must convert the installation into a concrete study workflow.

## Mandatory First Response

After installation, cloning, or bootstrap verification, the agent must:

1. Confirm that the kit is ready.
2. Briefly explain the practical value of the kit: course organization, live context, verified problem solving, LaTeX PDFs, attempt review, formula sheets, mock exams, note transcription, and progress tracking.
3. State that the system works with one isolated workspace per course.
4. Ask the student to answer the short setup questionnaire.
5. Tell the student to download a ZIP/folder from the university virtual classroom for that course and provide it to the agent.
6. Explain what the agent will create next.
7. Give concrete examples of messages the student can send after onboarding.
8. Keep the message actionable, not merely technical.

## First Message Template

Use the student's language.

```text
Installed and ready.

This kit turns Codex/Claude into a local engineering study agent for one university course. It can organize course material, build live context files, solve problems step by step, verify calculations, generate LaTeX PDFs, review attempts, create formula sheets, prepare mock exams, transcribe notes from photos, and track progress.

Important rule: one workspace per course. Do not mix different subjects.

First, send me:

1. Course name:
2. University and degree/program:
3. Target exam or assessment:
4. Current level:
   A. Very weak
   B. Basic
   C. Intermediate
   D. Strong but needs exam polish
5. Preferred explanation style:
   A. Very step-by-step
   B. Balanced
   C. Concise exam style
   D. Conceptual first, equations second
Then go to your university virtual classroom, download the ZIP/folder for this course, and provide it to me: slides, notes, problem sheets, exams, official solutions, assignments, rubrics, photos, or screenshots.

After analyzing it, I will create the course workspace, organize and connect the files, build the live context files, and show you a project map of the Markdown files, scripts, folders, and what each one contains for this specific course.

Then you can ask:

- "Solve this problem step by step and generate a LaTeX PDF."
- "Review my attempt and identify the first error."
- "Build a formula sheet for this topic."
- "Create a mock exam with this teacher's style."
- "Explain only this calculation step."
- "Transcribe these handwritten notes and connect them with the theory."
```

## After Material Analysis

Once the course ZIP/folder has been analyzed, the agent must give the student a concise project map. This is not a raw list of every file in the ZIP. It is a list of the kit/project files the agent will maintain, for example:

- `00_Context/STUDENT_PROFILE.md`: student profile, preferences, goals, level.
- `00_Context/COURSE_CONTEXT.md`: global course map and exam objective.
- `00_Context/TOPIC_EQUATION_SUMMARY.md`: operational equation/method summary.
- `00_Context/EXAM_PROBLEM_PATTERNS.md`: recurring exam and problem types.
- `07_Progress_And_Feedback/STUDENT_PROGRESS_LOG.md`: mistakes, improvements, practice history.
- `03_Solution_Sources/`: editable Markdown/LaTeX sources.
- `04_Solution_PDFs/`: final PDF solutions.
- `08_Calculation_Scripts/`: numerical verification scripts.

## If The Student Gives Only A Course Name

Create the course workspace, then ask for material and the student profile.

## If The Student Uploads Material First

Store the material in the new course workspace once the course name is known. If the course name is not known, ask for it before mixing files into a generic folder.

## If The Student Wants To Start Solving Immediately

Accept the problem, but still create the minimum workspace and save:

- the original statement;
- the clean statement;
- editable solution source;
- final PDF, if requested;
- progress notes when useful.
