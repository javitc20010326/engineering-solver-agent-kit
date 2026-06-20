---
name: "engineering-calculation-verifier"
description: "Verify engineering calculations, numerical results, assumptions, units, signs, limiting cases, and alternative derivations. Use before final answers, before LaTeX/PDF generation, when reviewing a student's attempt, or when a result seems suspicious."
---

# Engineering Calculation Verifier

Use this skill whenever correctness matters more than speed.

## Verification Targets

Check:

- input data copied correctly;
- units and base quantities;
- sign conventions;
- complex conjugates;
- matrix dimensions;
- boundary conditions;
- physical plausibility;
- active constraints and limits;
- numerical precision;
- final units and rounding.

## Standard Pass

1. Rebuild the problem model from the statement.
2. Recompute the key result independently.
3. Compare against the working solution.
4. Check one alternative route when practical:
   - direct formula vs matrix;
   - phasor vs rectangular form;
   - power balance vs current balance;
   - analytical expression vs Python/numerical script;
   - limiting case vs expected behavior.
5. Mark each result as:
   - `verified`;
   - `likely correct, residual risk`;
   - `inconsistent`;
   - `requires clarification`.

## Engineering Checks

Use domain checks when available:

- **Circuits/power systems:** conservation of complex power, voltage/current direction, base conversion.
- **Optimization/dispatch:** incremental costs, active limits, demand plus losses, penalty factors.
- **Transient stability:** pre-fault/fault/post-fault networks, `P_m`, `P_e(delta)`, angle units, equal-area criterion.
- **Frequency control:** sign of tie-line deviations, beta coefficients, ACE convention.
- **Transmission lines:** sending/receiving-end convention, ABCD consistency, charging terms.

## Error Localization

When reviewing an attempt:

1. State the last line that is still correct.
2. State the first line that becomes wrong.
3. Explain the exact mathematical reason.
4. Continue the solution from the correct point.

## Output Format

Use a compact verification block:

```text
Verification:
- Data copied correctly: yes/no
- Method valid: yes/no
- Numerical check: result and residual
- Units/signs: ok/issues
- Final status: verified / inconsistent / needs clarification
```

Do not generate the polished PDF until this block is stable.
