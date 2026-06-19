# Live Files Map

Live files are persistent memory files that the agent updates during the course.

## Live Context Files

| File | Created by | Updated by | Purpose |
| --- | --- | --- | --- |
| `00_Context/COURSE_CONTEXT.md` | Agent | Agent | Global course state |
| `00_Context/TOPIC_EQUATION_SUMMARY.md` | Agent | Agent | Operational equation summary |
| `00_Context/EXAM_PROBLEM_PATTERNS.md` | Agent | Agent | Common exercise and exam patterns |
| `00_Context/SOLUTION_PROTOCOL.md` | Agent | Agent | Course-specific solution rules |
| `07_Progress_And_Feedback/STUDENT_PROGRESS_LOG.md` | Agent | Agent | Student level, mistakes, progress |

## Input Files

| Folder | Content |
| --- | --- |
| `01_Course_Materials/` | Theory, slides, exams, assignments, official solutions |
| `05_Attachments/` | Raw photos and captures from the student |

## Output Files

| Folder | Content |
| --- | --- |
| `02_Statements/` | Clean problem statements |
| `03_Solution_Sources/` | Editable solved-problem sources |
| `04_Solution_PDFs/` | Final PDF solutions |
| `06_Formula_Sheets/` | Formula sheets and summaries |
| `08_Calculation_Scripts/` | Verification scripts |
| `09_Figures/` | Diagrams and plots |
| `10_Mock_Exams/` | Practice exams |
| `11_Assignments/` | Assignment-style work |

## Relationship

```text
Course material -> live context -> formulas/patterns -> solved problems -> progress log
```

Formal solutions should usually produce:

```text
02_Statements/base_name_statement.pdf
03_Solution_Sources/base_name_solution.md
04_Solution_PDFs/base_name.pdf
08_Calculation_Scripts/base_name_calculations.py
09_Figures/base_name_fig01.png
```
