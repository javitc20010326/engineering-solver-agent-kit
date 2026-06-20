# How To Work With The Agent

The agent performs best when it receives complete course context and precise requests.

## First Message After Installation

After the kit is installed, the agent should not leave you with only a technical installation summary. It should ask for the course name, basic student/course context, your current level, your preferred explanation style, and the course material.

If it does not, send:

```text
Start the Engineering Solver Agent Kit onboarding. Ask me what you need and create one workspace for this course.
```

## What The Student Should Provide

Place all available material for one course in `01_Course_Materials/`:

- lecture notes;
- slides;
- problem sheets;
- exams;
- official solutions;
- rubrics;
- assignments;
- lab material;
- teacher-specific conventions.

If the student sends photos or captures, the agent must store them in `05_Attachments/` and create a clean statement in `02_Statements/` when the exercise becomes part of the formal study archive.

## One Course Per Workspace

Each course must have its own folder. Mixing subjects causes formula, notation, exam-pattern, and teacher-convention contamination.

## What The Agent Does

1. Reads the course structure.
2. Builds or updates live context files.
3. Extracts topics, equations, methods, and exam patterns.
4. Solves problems step by step.
5. Verifies numerical results before writing final explanations.
6. Generates LaTeX/PDF solutions when requested.
7. Reviews student attempts.
8. Uses OCR/attachment intake for photos and scans before solving.
9. Uses the student profile to adapt explanation depth, visual support, and practice recommendations.
10. Updates the progress log after meaningful mistakes or improvements.

## Request Patterns

Use precise requests:

```text
Solve this problem step by step, verify calculations first, then generate a LaTeX PDF.
```

```text
Review my attempt. Tell me exactly where the first error appears and continue from there correctly.
```

```text
Create a formula sheet for Topic 4 with equations, variable meanings, units, and when to use each formula.
```

## Output Rule

Formal work must leave a trace:

- statement;
- editable source;
- final PDF;
- calculation scripts when useful;
- figures when useful;
- progress notes when the student's level changes.
