# Roadmap

Implemented core extensions:

1. **OCR / statement intake skill**
   - `skills/engineering-ocr-intake/`
   - Handles photos, scans, screenshots, naming, archiving, and ambiguity flags.

2. **Calculation verifier skill**
   - `skills/engineering-calculation-verifier/`
   - Checks units, signs, constraints, residuals, alternative derivations, and first-error localization.

3. **Student model tracker skill**
   - `skills/student-model-tracker/`
   - Maintains `STUDENT_PROFILE.md` and progress evidence.

4. **Formula sheet builder skill**
   - `skills/formula-sheet-builder/`
   - Creates agent-facing equation maps and method sheets.

5. **Professional PDF layout skill**
   - `skills/paper-latex-layout/`
   - Provides Pandoc/LaTeX wrappers, Eisvogel support, DOCX export, page rendering, and visual QA.

Potential next high-impact extensions:

1. **Understanding debugger skill**
   - Handle questions such as "where does this equation come from?"
   - Explain derivations, physical meaning, and dimensional consistency.

2. **Mock exam generator skill**
   - Build practice exams from topic weights and difficulty.
   - Include timed and untimed variants.
   - Generate correction rubrics and model answers.

3. **Rubric-based review skill**
   - Grade student attempts using course-specific rubrics.
   - Separate conceptual, algebraic, notation, and exam-format errors.

4. **Mistake bank generator**
   - Store recurring mistakes.
   - Generate targeted drills from weak areas.

5. **Subject family templates**
   - Electrical circuits.
   - Power systems.
   - Control systems.
   - Signals and systems.
   - Mechanics.
   - Thermodynamics.
   - Numerical methods.

6. **Installer improvements**
   - Detect missing PDF tooling.
   - Recommend exact installation steps per operating system.
   - Validate Codex/Claude skill installation.

7. **Workspace audit dashboard**
   - Report missing statements, sources, PDFs, figures, scripts, and context files.
   - Produce a course readiness score.
