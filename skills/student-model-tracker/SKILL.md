---
name: "student-model-tracker"
description: "Maintain a live learning model for an engineering student: profile, preferences, strengths, weak topics, recurring mistakes, practiced problems, progress, and recommended next actions. Use during onboarding, after attempt reviews, after solved problems, and when planning study sessions."
---

# Student Model Tracker

Use this skill to personalize the agent's teaching behavior across a course.

## Live Files

Maintain:

```text
00_Context/STUDENT_PROFILE.md
07_Progress_And_Feedback/STUDENT_PROGRESS_LOG.md
```

`STUDENT_PROFILE.md` changes rarely. It stores identity, preferences, learning style, constraints, and goals.

`STUDENT_PROGRESS_LOG.md` changes often. It stores actual evidence from solved problems and reviews.

## Initial Interview

During onboarding, ask a short interview. Prefer multiple-choice options when possible.

Required:

1. Name or preferred name.
2. University and degree.
3. Course/year.
4. Exam or assessment target.
5. Current level:
   - A. Very weak;
   - B. Basic;
   - C. Intermediate;
   - D. Strong but needs polish.
6. Preferred explanation style:
   - A. Very step-by-step;
   - B. Balanced;
   - C. Concise exam style;
   - D. Conceptual first, equations second.
7. Cognitive preference:
   - A. Mathematical-symbolic;
   - B. Visual/spatial;
   - C. Verbal/conceptual;
   - D. Procedural/algorithmic;
   - E. Mixed.
8. Preferred output:
   - A. PDF solutions;
   - B. Chat explanations;
   - C. Formula sheets;
   - D. Attempt corrections;
   - E. All of the above.
9. Weakness pattern:
   - A. I do not know which formula to use;
   - B. I make algebra/numeric mistakes;
   - C. I understand but write poorly in exams;
   - D. I miss signs/units/conventions;
   - E. I need more practice speed.
10. Time horizon and exam date if known.

Optional:

- age;
- city/country;
- language preference;
- accessibility needs;
- preferred notation;
- professor/exam style notes.

## Update Rules

After each meaningful session, update the progress log with evidence:

```text
- Date:
- Activity:
- Topic:
- What the student did well:
- Error or weakness observed:
- Correction:
- Next recommended practice:
```

Do not overfit to one mistake. Mark a recurring weakness only after repeated evidence.

## Personalization Rules

- If the student is visual/spatial, add diagrams, curves, tables, and network sketches more often.
- If the student is mathematical-symbolic, show derivations and formula transformations explicitly.
- If the student is procedural, emphasize algorithmic steps and checklists.
- If the student is exam-focused, include compact final-answer formatting and likely scoring points.
- If the student is weak, reduce jumps between equations.

## Privacy

Keep the profile local. Do not request sensitive personal data that is not useful for learning.
