# Course Workspace Structure

Each university subject must have an isolated workspace.

## Standard Layout

```text
Course_Name/
  README_COURSE.md

  00_Context/
    00_COURSE_ONBOARDING.md
    STUDENT_PROFILE.md
    COURSE_CONTEXT.md
    TOPIC_EQUATION_SUMMARY.md
    EXAM_PROBLEM_PATTERNS.md
    SOLUTION_PROTOCOL.md
    NEW_SOLUTION_CHECKLIST.md

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

## Student Inputs

The student provides source material in `01_Course_Materials/` and raw images/captures in `05_Attachments/`.

## Agent Outputs

The agent creates:

- context files;
- equation summaries;
- solved problem sources;
- final PDFs;
- verification scripts;
- diagrams and plots;
- mock exams;
- feedback and progress notes.

## Naming Rule

Use descriptive, searchable names:

```text
P1_EX_2025_TOPIC4_LoadFlow.pdf
C2_PROP_TOPIC8_TransientStability.pdf
Assignment3_TOPIC6_MarketTransactions.pdf
```
