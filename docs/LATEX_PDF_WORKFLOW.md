# LaTeX PDF Workflow

Use this workflow when the student requests a formal solved problem.

This repository includes two complementary PDF layers:

- `skills/study-latex-pdf/`: study protocol for calculation-first engineering solutions.
- `skills/paper-latex-layout/`: full production skill with Pandoc/LaTeX wrappers, a classic academic layout, optional Eisvogel report style, DOCX export, PDF page rendering, and visual QA scripts.

For serious solved problems, use both: solve and verify through `study-latex-pdf`, then render and inspect through `paper-latex-layout`.

## Sequence

1. Solve and verify calculations first.
2. Draft the explanation in Markdown or LaTeX.
3. Use displayed equations for important formulas and substitutions.
4. Add figures only when they clarify the method.
5. Compile to PDF with `pdflatex`, `xelatex`, or Pandoc.
6. Inspect the PDF visually if layout quality matters.
7. Save source and final PDF in the course workspace.

## Preferred Build Route

Use the vendored `paper-latex-layout` skill when available:

```text
python skills/paper-latex-layout/scripts/build_latex_pdf.py 03_Solution_Sources/base_name_solution.md 04_Solution_PDFs/base_name.pdf --style classic --engine auto
```

On Windows, the command wrapper can be used:

```text
skills\paper-latex-layout\scripts\build_latex_pdf.cmd 03_Solution_Sources\base_name_solution.md 04_Solution_PDFs\base_name.pdf --style classic --engine auto
```

Recommended style selection:

- `classic`: solved exercises, exam resolutions, formula sheets, and traditional university notes.
- `eisvogel`: polished reports, manuals, or documents that need stronger visual hierarchy.

Recommended engine selection:

- `auto`: try the available local LaTeX/PDF stack automatically.
- `pdflatex`: require real `pdflatex`.
- `xelatex`: use when Unicode/font handling matters.
- `tectonic`: use the portable fallback when available.

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

## Visual QA

For routine study material, a fast QA pass is enough:

```text
python skills/paper-latex-layout/scripts/render_pdf_pages.py 04_Solution_PDFs/base_name.pdf 09_Figures/base_name_pdf_qa --mode quick
```

Use full visual QA when the document is public, final, long, image-heavy, table-heavy, or when a previous render showed layout issues:

```text
python skills/paper-latex-layout/scripts/render_pdf_pages.py 04_Solution_PDFs/base_name.pdf 09_Figures/base_name_pdf_qa --mode full
```
