---
name: "paper-latex-layout"
description: "Create polished single-column academic/professional PDFs with homogeneous typography, structured explanatory text, rendered LaTeX-style formulas, clean tables, and visual QA. Use for university problem solutions, technical notes, reports, or paper-like documents that should not be two-column."
---

# Paper LaTeX Layout

Use this skill when the user wants a clean, professional, paper-like PDF or source document with well-rendered formulas and consistent academic layout.

## Output Standard

- Single-column A4 unless the user asks otherwise.
- Clear hierarchy: title, short subtitle, numbered sections, short paragraphs, display equations, compact tables.
- Explanatory text must read like a professor writing for students: what is being done, why, what formula applies, what is substituted, and how to interpret signs/units.
- Equations must be rendered visually, not left as raw LaTeX text.
- Figures, plots, screenshots, and user-supplied images may be included with Pandoc captions. Prefer generated plots from user data/calculations when that clarifies the result.
- Tables should be used only for compact data/result summaries.
- Use fast QA by default. Render/inspect only a representative sample unless the document is public/final, layout-risky, or the user asks for full visual QA.

## Preferred Workflow

1. Draft a structured spec with title, subtitle, sections, paragraphs, equations, and tables.
2. Run `scripts/check_environment.py` if tool availability is uncertain.
3. Prefer Pandoc + LaTeX for Markdown sources.
4. Use `classic` style for university notes, solved exercises, formula summaries, and material that should look like traditional LaTeX/Computer Modern.
5. Use `eisvogel` style for modern reports, manuals, or documents that benefit from stronger headings and report styling.
6. Use the Python generator when Pandoc/TeX fails or when deterministic programmatic composition is better.
7. Run fast QA: verify compilation succeeded and, when layout risk exists, render first/last page only.
8. Run full visual QA only for public/final documents, template changes, dense tables, long equations, page-break-sensitive work, or explicit user request.
9. Iterate if QA reveals clipped formulas, raw LaTeX, bad table breaks, or large blank gaps.

## Primary Script: Pandoc + LaTeX

Use this for polished Markdown/LaTeX documents:

```bash
python scripts/build_latex_pdf.py input.md output.pdf --style classic --engine auto
```

On Windows, prefer the `.cmd` wrapper when `python` is not guaranteed to be on PATH or PowerShell script execution is restricted:

```cmd
scripts\build_latex_pdf.cmd input.md output.pdf --style classic --engine auto
```

Installed portable tools:

```text
%USERPROFILE%\.codex\tools\paper-latex-layout\bin\pandoc.exe
%USERPROFILE%\.codex\tools\paper-latex-layout\bin\tectonic.exe
%USERPROFILE%\.codex\tools\miktex\miktex\bin\x64\pdflatex.exe
%USERPROFILE%\.codex\tools\paper-latex-layout\pydeps
```

The skill folder includes the Eisvogel LaTeX template as `assets/eisvogel.latex`, but the heavy binaries are external global tools under `%USERPROFILE%\.codex\tools`.

Tool roles:

- Pandoc converts Markdown with LaTeX math to LaTeX/PDF.
- MiKTeX/pdflatex is the preferred engine for `classic` output.
- Tectonic is the portable fallback engine.
- Eisvogel is the modern report template for `--style eisvogel`.
- PyMuPDF renders PDF pages to PNG for QA.
- ReportLab/matplotlib provide the programmatic fallback renderer.

### Figures And Captions

Use Pandoc image syntax:

```markdown
![Caption text.](figures/example.png){#fig:example width=75%}
```

Use figures for:

- plots generated from user data,
- graphs from calculations performed by Codex,
- screenshots/photos supplied by the user,
- cleaned diagrams or visual explanations.

Keep images in a folder relative to the Markdown source, usually `figures/`. The builder sets the Markdown folder as Pandoc resource path.

Recommended Markdown metadata:

```yaml
---
title: "Document title"
subtitle: "Short subtitle"
author: ""
date: ""
lang: es
geometry: "margin=2.2cm"
fontsize: 11pt
---
```

### Style Selection

- `--style classic`: default for exam solutions, math summaries, university notes, and documents where the body text should look like LaTeX text rather than a modern sans report.
- `--style eisvogel`: use for polished reports/manuals with stronger visual hierarchy.

### Engine Selection

- `--engine auto`: prefer `pdflatex` from the local MiKTeX installation, then fall back to Tectonic.
- `--engine pdflatex`: require real `pdflatex`; use when the user explicitly asks for pdflatex.
- `--engine tectonic`: use the portable Tectonic engine.

When using MiKTeX/pdflatex for the first time, ensure MiKTeX has completed setup and automatic package installation is enabled:

```bash
initexmf --set-config-value=[MPM]AutoInstall=yes
```

In restricted sandboxed shells, MiKTeX may need an unsandboxed/escalated run because it writes user config/cache files under AppData.

Before concluding that a tool is missing, run:

```bash
python scripts/check_environment.py
```

or on Windows:

```cmd
scripts\check_environment.cmd
```

Do not assume `python`, `pandoc`, or `pdflatex` are on PATH; use explicit executable paths if needed.

## Legacy Script: Pandoc + Eisvogel

This remains available for compatibility:

```bash
python scripts/build_pandoc_eisvogel.py input.md output.pdf
```

## Fallback Script: Programmatic PDF

Use when Pandoc/TeX is unavailable or too slow:

```bash
python scripts/build_academic_pdf.py input.json output.pdf
```

The script expects JSON:

```json
{
  "title": "Problem title",
  "subtitle": "Short context",
  "sections": [
    {
      "heading": "1. Section",
      "blocks": [
        {"type": "paragraph", "text": "Explanatory text with <b>basic HTML</b>."},
        {"type": "equation", "latex": "$P=VI\\cos\\varphi$", "width_cm": 12},
        {"type": "table", "headers": ["A", "B"], "rows": [["x", "y"]]}
      ]
    }
  ]
}
```

Supported block types: `paragraph`, `step`, `equation`, `table`, `pagebreak`, `spacer`.

## Optional DOCX Export

Use when the user wants an editable Word-compatible draft alongside the PDF:

```bash
python scripts/build_docx.py input.md output.docx
```

or on Windows:

```cmd
scripts\build_docx.cmd input.md output.docx
```

## Dependency Path

The script first tries bundled/runtime Python packages, then:

```text
%USERPROFILE%\.codex\tools\paper-latex-layout\pydeps
```

Install or refresh dependencies there if needed:

```bash
python -m pip install matplotlib pillow reportlab pymupdf --target "%USERPROFILE%\.codex\tools\paper-latex-layout\pydeps"
```

## GitHub Template Reference

The skill includes `assets/eisvogel.latex` when available. It comes from `Wandmalfarbe/pandoc-latex-template`, a strong Pandoc LaTeX template for polished PDFs.

Use Eisvogel when `pandoc.exe` and `tectonic.exe` are available in the portable tool directory. Otherwise use the Python generator.

## Layout Rules

- Keep formulas close to the text that explains them.
- For repeated mechanical calculations, show one or two representative substitutions, then summarize the rest.
- Use result boxes/tables at the end, but do not let the document become result-only.
- Avoid giant formulas; split into formula, substitution, result.
- Units and sign conventions must be stated near the first use.
- If a table splits awkwardly across pages, use a page break or simplify the table.

## QA Policy

Default behavior is fast because full page-by-page visual inspection slows routine PDF generation.

Fast QA is enough when:

- The source follows the established template.
- The document has ordinary paragraphs, equations, and small tables.
- The PDF compiles without LaTeX errors.
- The output is for study/internal use.

Full visual QA is required when:

- The user asks for a publication/submission/final handout.
- The template, geometry, fonts, or rendering scripts changed.
- The document contains wide tables, long aligned formulas, images, code blocks, or many manual page breaks.
- A previous build showed layout problems.

Fast render:

```bash
python scripts/render_pdf_pages.py output.pdf render_dir --mode quick
```

or on Windows:

```cmd
scripts\render_pdf_pages.cmd output.pdf render_dir --mode quick
```

Full render:

```bash
python scripts/render_pdf_pages.py output.pdf render_dir --mode full
```

or on Windows:

```cmd
scripts\render_pdf_pages.cmd output.pdf render_dir --mode full
```

- Equations are visually rendered.
- No raw LaTeX remains in the final PDF body unless intentionally shown as source.
- Headings, body text, formulas, and tables are visually consistent.
- No clipped formulas.
- No table split that makes reading harder.
- No page with a large blank region caused by a bad manual break.
- Final answer links only the PDF and relevant source/spec files.
