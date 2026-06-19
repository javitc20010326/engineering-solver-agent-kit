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
- personal weak points.

## Required behavior

1. Inspect the local course folder.
2. Identify available materials.
3. Create or update the standard folder structure.
4. Create initial context files.
5. Explain to the student how the agent will work.
6. Explain how the student should ask for tasks.
7. Ask only for missing information that is truly needed.

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

## Output

At the end, provide:

- what was found;
- what was created;
- what is missing;
- recommended next action.

Do not solve problems during onboarding unless the student explicitly asks after the setup is complete.
