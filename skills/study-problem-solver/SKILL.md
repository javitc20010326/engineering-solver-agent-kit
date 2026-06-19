# study-problem-solver

Use this skill when the student asks to solve, explain, verify, or correct a university technical problem.

## Goal

Produce a correct, teachable, verifiable solution.

## Workflow

1. Read the active course context.
2. Read the problem statement.
3. Identify topic and problem type.
4. Extract data into a table.
5. Define assumptions, signs, and units.
6. Choose formulas.
7. Solve.
8. Verify.
9. Explain step by step.
10. Save outputs if a formal solution is requested.

## Verification

Always check relevant items:

- units;
- signs;
- limits;
- physical intuition;
- conservation/balance equations;
- numerical order of magnitude;
- consistency with official solution if available.

## Teaching style

Default:

- concise but complete;
- explain formulas before substituting;
- show where each important value comes from;
- develop one representative repetitive calculation;
- summarize repeated operations in tables.

If the student is confused:

- stop advancing;
- explain the blocking step;
- use full formula;
- substitute values explicitly;
- avoid algebraic jumps.

## Formal solution outputs

If the student asks for a formal solution or PDF, the agent must create:

```text
02_Statements/base_name_statement.pdf
03_Solution_Sources/base_name_solution.md
04_Solution_PDFs/base_name.pdf
08_Calculation_Scripts/base_name_calculations.py
09_Figures/base_name_fig01.png
```

Adapt folder names if the course template uses equivalent directories.

## Naming

Use a stable base name:

```text
[C/P][number]_[EX/PROP/ENT]_[exam_or_source]_[topic]_[short_description]
```

Examples:

```text
C1_EX_2026_TOPIC2_Lines
P2_PROP_TOPIC4_LoadFlow
ASSIGNMENT3_P1_TOPIC6_Markets
```

## Do not

- do not invent missing data;
- do not mix problems;
- do not create a polished PDF before verifying calculations;
- do not hide uncertainty;
- do not omit units in final results.
