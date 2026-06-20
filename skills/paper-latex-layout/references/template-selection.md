# Template Selection

Use this reference only when choosing between rendering engines.

## Candidates Reviewed

- `Wandmalfarbe/pandoc-latex-template` / Eisvogel: best practical GitHub base for polished Pandoc-to-LaTeX PDFs. Strong for reports, exercises, manuals, and academic notes.
- `dialoa/pandokoma`: strong KOMA-script control if Pandoc and LaTeX are installed.
- `Pseudomanifold/latex-mimosis`: clean thesis template, better for long monographs than short problem solutions.
- Lecture-notes templates: visually attractive but often too opinionated or heavy for repeated exam solutions.

## Default Decision

- If Pandoc + LaTeX engine exists: use Eisvogel or a local derivative of it.
- If no TeX stack exists: use `scripts/build_academic_pdf.py`, which renders formulas via matplotlib mathtext and composes PDF with ReportLab.

## Style Target

Professional single-column technical note:

- A4 portrait.
- Blue section headings.
- Compact but readable 9.5-10 pt body.
- Display equations slightly larger than body.
- Light grey table headers.
- No decorative cover unless requested.
