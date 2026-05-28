# UCSF Security Review — Coverage Summary

Analyzed all **39 questions** from `UCSF Docs/UCSF Security Review Questions.xlsx` against the current consolidated policy set in `Current Policies (… Generated)/3.a Final Markdown/` and the evidence files in `Supporting Sources/`.

## Coverage counts

| Coverage | Count |
|---|---|
| Full | 28 |
| Partial | 11 |
| None | 0 |
| N/A | 0 |
| Evidence-only | 0 |

## Flag Risk counts (if submitted as-is)

| Flag Risk | Count |
|---|---|
| High | 0 |
| Medium | 11 |
| Low | 28 |
| None | 0 |

## Per-section breakdown

| Section | Questions |
|---|---|
| Risk Management | 5 |
| Business Continuity | 4 |
| Access Control | 3 |
| Asset Management | 3 |
| Configuration Management | 3 |
| Data Protection | 3 |
| Incident Response | 3 |
| Network Security | 3 |
| Physical Security | 3 |
| Roles & Responsibilities | 3 |
| Data Mapping | 1 |
| HR Security | 1 |
| Legal & Regulatory | 1 |
| Security Program | 1 |
| Training | 1 |
| Vendor Management | 1 |

## Remediation effort

- **Total `Required Fix - Text` word count across all rows:** 361
- **Policy files needing additions** (2):
  - `01c. Risk Management Policy`
  - `06b. SDLC & Asset Lifecycle Policy`

Everything else is either Full (policy answers it) or needs a **supporting doc** (HR / Tenisi / operational SOP), not a policy edit. See `SUPPORTING-DOCS-NEEDED.md` for the consolidated evidence checklist.

The per-row analysis is in `coverage_matrix_UCSF.csv` (renders to `coverage_matrix_UCSF.xlsx` after the build).
