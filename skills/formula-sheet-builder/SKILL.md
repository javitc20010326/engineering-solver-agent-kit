---
name: "formula-sheet-builder"
description: "Build operational formula sheets for Codex/Claude to use while solving engineering problems. Use when creating topic summaries, equation maps, method maps, formula indexes, or agent-facing cheat sheets that connect formulas to conditions, units, assumptions, and problem types."
---

# Formula Sheet Builder

Use this skill to create formula sheets for the agent, not just for the student.

## Goal

Produce operational formula files that help the agent solve future problems faster and more consistently.

Main output:

```text
00_Context/TOPIC_EQUATION_SUMMARY.md
06_Formula_Sheets/topic_formula_sheet.md
```

## Formula Entry Schema

For each formula, store:

```text
Name:
Topic:
Use when:
Do not use when:
Formula:
Variables:
Units:
Known inputs:
Unknowns solved:
Assumptions:
Sign convention:
Base/per-unit convention:
Typical substitutions:
Common mistakes:
Verification check:
Related problem types:
Source/reference:
```

## Agent-Facing Priority

The sheet must answer:

- What problem pattern triggers this formula?
- What data must be known?
- What hidden convention can break the result?
- What equation should be used before/after it?
- How can the result be checked?

## Structure

Use this order:

1. Topic overview.
2. Problem-type decision tree.
3. Core variables and units.
4. Formula blocks.
5. Method blocks.
6. Common mistakes.
7. Verification checks.
8. Links to solved examples.

## Decision Tree Format

Prefer compact routing:

```text
If the problem gives X and asks Y -> use method A.
If there are losses -> include penalty factors.
If one generator hits a limit -> fix it and recompute lambda with the remaining units.
```

## Maintenance

Update the sheet after:

- a new topic is onboarded;
- a recurring formula appears in several problems;
- the student makes a repeated formula-selection error;
- a professor-specific convention is discovered;
- an exam pattern is identified.

Do not turn the sheet into a textbook. Keep it operational.
