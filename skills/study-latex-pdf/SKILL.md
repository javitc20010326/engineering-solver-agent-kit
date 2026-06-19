# study-latex-pdf

Use this skill when the student asks for a polished PDF solution, formula sheet, exam solution, or written technical document with rendered formulas.

## Goal

Create readable university-style PDFs from verified calculations.

## Required order

```text
verified calculations
-> Markdown/LaTeX source
-> PDF compilation
-> visual review
-> final saved files
```

Never start with the final PDF before calculations are verified.

## Recommended document structure

1. Title.
2. Problem statement summary or reference.
3. Data table.
4. Model and assumptions.
5. Formulas used.
6. Step-by-step solution.
7. Verification.
8. Final results.

## Formatting rules

- Use LaTeX display equations for formulas.
- Use boxes for final key results.
- Use tables for repeated calculations.
- Use figures only when they clarify.
- Avoid duplicated numbering.
- Avoid oversized pages or cut tables.
- Keep language clear and technical.

## File outputs

For a formal solution:

```text
03_Solution_Sources/base_name_solution.md
04_Solution_PDFs/base_name.pdf
```

If there is a statement:

```text
02_Statements/base_name_statement.pdf
```

If there are scripts or plots:

```text
08_Calculation_Scripts/base_name_calculations.py
09_Figures/base_name_fig01.png
```

## Compilation

Use the best available local route:

1. Existing PDF/LaTeX skill if available.
2. `pandoc` with a LaTeX engine if available.
3. `pdflatex` if using a `.tex` source.
4. A local script provided by the course/project.

## Visual QA

Check:

- formulas render;
- tables fit;
- figures load;
- no placeholders remain;
- final results are visible;
- page breaks are acceptable.

If visual QA fails, fix the source and regenerate.
