---
name: "engineering-ocr-intake"
description: "Prepare engineering problem statements from student-provided photos, screenshots, scans, PDFs, or messy attachments. Use when the user uploads enunciados, exam photos, handwritten captures, or asks the agent to save, clean, transcribe, OCR, crop, combine, name, or archive problem statements before solving."
---

# Engineering OCR Intake

Use this skill before solving when the input is an image, scan, screenshot, or mixed attachment set.

## Objective

Turn raw student attachments into reliable local statement artifacts:

```text
05_Attachments/raw files
02_Statements/clean statement PDF or Markdown
00_Context/COURSE_CONTEXT.md updated when useful
```

## Workflow

1. Identify whether the attachment is a statement, theory page, solution, rubric, or unrelated material.
2. Preserve the raw file in `05_Attachments/` when the local environment exposes it.
3. Produce a clean statement artifact in `02_Statements/`:
   - one PDF for multi-image statements;
   - one Markdown file when transcription is enough;
   - both when OCR/transcription is important.
4. Extract the problem metadata:
   - course;
   - exam or source;
   - year;
   - problem/question number;
   - topic;
   - visible data;
   - ambiguous or unreadable data.
5. If any symbol, decimal, sign, unit, or line value is uncertain, ask before solving.
6. Name files consistently.

## Naming

Use explicit names:

```text
C1_EX_2P_2026_T6_Transactions_statement.pdf
P2_PROP_T8_TransientStability_statement.pdf
P1_ASSIGNMENT4_T8_TransientStability_statement.pdf
```

Prefer:

```text
{C|P}{number}_{EX|REC|PROP|ASSIGNMENT}_{period_or_source}_{year_if_any}_{topic}_statement
```

## OCR Discipline

- Never silently guess unreadable numeric data.
- Distinguish printed data from handwritten annotations.
- Ignore irrelevant handwritten notes unless the user asks to analyze them.
- Preserve original sign conventions from the statement.
- Normalize decimal commas only in the working solution, not in quoted statement data.

## Useful Local Scripts

Use these when relevant:

```text
scripts/image_to_pdf.py
scripts/index_materials.py
```

For several photos of one problem, combine them in the correct order into one statement PDF.

## Output

End with:

- saved statement path;
- extracted data summary;
- unclear items, if any;
- recommended next action: solve, classify, or request clarification.
