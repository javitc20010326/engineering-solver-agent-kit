# LaTeX PDF Workflow

Use this workflow when the student requests a formal solved problem.

## Sequence

1. Solve and verify calculations first.
2. Draft the explanation in Markdown or LaTeX.
3. Use displayed equations for important formulas and substitutions.
4. Add figures only when they clarify the method.
5. Compile to PDF with `pdflatex`, `xelatex`, or Pandoc.
6. Inspect the PDF visually if layout quality matters.
7. Save source and final PDF in the course workspace.

## Standard Artifacts

```text
02_Statements/base_name_statement.pdf
03_Solution_Sources/base_name_solution.md
04_Solution_PDFs/base_name.pdf
08_Calculation_Scripts/base_name_calculations.py
09_Figures/base_name_fig01.png
```

## Quality Bar

- No overflowing equations.
- No unreadable tables.
- No unexplained sign convention.
- No final result without units.
- No PDF before calculation verification.
