# study-onboarding

Use this skill when a student starts a new university course folder and wants the agent to organize materials, create context files, explain the workflow, and prepare the study system.

## Goal

Transform raw course documentation into a structured study workspace.

## Inputs

The student may provide:

- a complete package of course materials exported from the learning platform;
- course name;
- degree/university;
- exam date;
- evaluation structure;
- course documents;
- problem sheets;
- previous exams;
- official solutions;
- practical assignments;
- student profile answers;
- personal weak points.

## Required behavior

1. Inspect the local course folder.
2. Identify available materials.
3. Create or update the standard folder structure.
4. Run a short student interview and write `00_Context/STUDENT_PROFILE.md`.
5. Create initial context files.
6. Explain to the student how the agent will work.
7. Explain how the student should ask for tasks.
8. Ask only for missing information that is truly needed.

Tell the student to keep one course per folder/project. Do not mix different courses in the same workspace.

## Standard folders

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

## Standard context files

```text
00_Context/00_COURSE_ONBOARDING.md
00_Context/STUDENT_PROFILE.md
00_Context/COURSE_CONTEXT.md
00_Context/TOPIC_EQUATION_SUMMARY.md
00_Context/EXAM_PROBLEM_PATTERNS.md
00_Context/SOLUTION_PROTOCOL.md
07_Progress_And_Feedback/STUDENT_PROGRESS_LOG.md
```

## Explain modes to the student

The onboarding must explain these modes:

- resolution mode;
- learning mode;
- correction mode;
- formula sheet mode;
- exam mode;
- turbo mode.

## Student interview

Prefer multiple-choice questions when possible so the student does not need to invent long answers.

Ask for:

- preferred name;
- university and degree;
- course/year;
- exam or assessment target;
- current level: very weak, basic, intermediate, or strong;
- preferred explanation style: very step-by-step, balanced, concise exam style, or conceptual first;
- cognitive preference: mathematical, visual/spatial, verbal/conceptual, procedural, or mixed;
- typical difficulty: method selection, algebra/numerics, exam writing, signs/units/conventions, or speed;
- preferred outputs: PDFs, chat explanations, formula sheets, attempt corrections, mock exams, or all.

Store the result in `00_Context/STUDENT_PROFILE.md` and use it to adapt future explanations.

## Output

At the end, provide:

- what was found;
- what was created;
- what is missing;
- recommended next action.

Do not solve problems during onboarding unless the student explicitly asks after the setup is complete.
