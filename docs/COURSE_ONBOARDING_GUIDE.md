# Course Onboarding Guide

Onboarding converts a raw folder of course material into a structured agent-ready workspace.

## Required Initial Information

The agent should identify:

- student profile and learning preferences;
- course name;
- degree/program context;
- exam structure;
- assessment dates if relevant;
- official topic list;
- available theory files;
- problem sheets;
- past exams;
- student goals;
- weak topics;
- desired output format.

## Student Questions

First ask a short student interview and save it in `00_Context/STUDENT_PROFILE.md`.

Recommended interview:

1. Preferred name.
2. Age.
3. City/country.
4. University.
5. Degree/program.
6. Academic year/course.
7. Main objective.
8. Target exam/assessment and date.
9. Current level:
   - A. Very weak;
   - B. Basic;
   - C. Intermediate;
   - D. Strong but needs polish.
10. Preferred explanation style:
   - A. Very step-by-step;
   - B. Balanced;
   - C. Concise exam style;
   - D. Conceptual first, equations second.
11. Cognitive preference:
   - A. Mathematical-symbolic;
   - B. Visual/spatial;
   - C. Verbal/conceptual;
   - D. Procedural/algorithmic;
   - E. Mixed.
12. Typical difficulty:
   - A. Formula/method selection;
   - B. Algebra/numerical mistakes;
   - C. Exam writing;
   - D. Signs/units/conventions;
   - E. Speed.
13. Preferred outputs:
   - A. PDF solutions;
   - B. Chat explanations;
   - C. Formula sheets;
   - D. Attempt corrections;
   - E. Mock exams;
   - F. All of the above.

Then ask course-specific questions:

1. What is the course?
2. What exam or assessment are you preparing?
3. What material do you have?
4. What topics are included?
5. What topics are your weakest?
6. Do you want formal PDF solutions?
7. Do you want concise solutions, teaching-style solutions, or both?
8. Do you want the agent to maintain a progress log?

## Files Created During Onboarding

```text
00_Context/COURSE_CONTEXT.md
00_Context/STUDENT_PROFILE.md
00_Context/TOPIC_EQUATION_SUMMARY.md
00_Context/EXAM_PROBLEM_PATTERNS.md
00_Context/SOLUTION_PROTOCOL.md
07_Progress_And_Feedback/STUDENT_PROGRESS_LOG.md
```

## Completion Criteria

Onboarding is complete when the agent can answer:

- what topics exist;
- where theory and exercises are stored;
- what problem types are likely in exams;
- what formulas and methods are central;
- how future solved problems should be saved.
