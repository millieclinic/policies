# Coverage CSV — Summary

This summary describes the row-by-row coverage matrix at `coverage_matrix.csv` in the same directory. The CSV is the authoritative per-row analysis; `SUMMARY.md` and `GAPS.md` remain useful for exec-readable structure.

The matrix is generated against the 29-policy `3. final_policies/` set. The CSV's **Plain English** column is a layman's translation of each questionnaire item for non-security readers.

**Source CSV:** `ECH Security Assessment Questions - Sheet2.csv` (repo root) — the expanded 212-row × 16-column workbook supersedes the prior 182-row `Questions.csv`. New columns include `Additional Info Added` (col 7), which carries user-authoritative answers and overrides the AI-provided coverage where populated.

**Total rows:** 212 (expected 212; previously 182)

## Coverage counts

| Coverage | Count |
|---|---|
| Full | 119 |
| Partial | 40 |
| None | 0 |
| N/A | 49 |
| Evidence-only | 4 |

## Flag Risk counts

| Flag Risk | Count |
|---|---|
| High | 19 |
| Medium | 23 |
| Low | 121 |
| None | 49 |

## Required Fix totals

**Total word count of all `Required Fix - Text` values:** 750

### Files needing additions (cumulative words)

| File | Cumulative words |
|---|---|
| `Millie Information Security & Data Governance Framework (1).md` | 543 |
| `System Development Life Cycle (SDLC) & Asset Lifecycle Policy.md` | 92 |
| `03o HIPAA - Password Management Policy.md` | 53 |
| `03s HIPAA - Security Incident Management Policy (2).md` | 31 |
| `03d HIPAA - Contingency Planning Policy (1).md` | 31 |

The SDLC file's cumulative word count rose from 57 to 92 because the new SIG Lite I.3.1 row (web-server configuration standards) appends a hardening-baseline clause.

## Top High-risk rows (Flag Risk = High)

19 rows are High-risk. Submission-evidence rows (Insurances, Security Audits) and Supply Chain Risk Management (S.32, S.57, S.61, S.80, S.100) dominate. The full list is in the CSV — filter `Flag Risk = High`.

Notable groupings:

| Group | Items | Driver |
|---|---|---|
| Submission-evidence artifacts | Insurances 1, Security Audits 1 & 2 | Documents must be attached to the ECH submission; no policy edit. |
| Endpoint / MDM operationalization | M.1.3, M.1.5, M.1.6 | Workstation Use §III(d) documents the BYOD/MDM stance; vendor implementation pending. |
| Supply Chain Risk (NIST SP 800-161) | S.32, S.57, S.61, S.80, S.100 | C-SCRM program not adopted at Millie's scale; defensible but assessor may push back. |
| Operational resilience | K.2, K.4, K.30 | DR exercise, pandemic plan, multi-vendor resiliency strategy require explicit articulation. |
| OWASP / app-security framing | A02, A06, A07 | Password Management Policy lacks server-side hashing / scanner-cadence / session-token language. |
| Monitoring methodology | G.2, J.5 | Change control + log-review cadence not documented at required specificity. |

## Per-questionnaire breakdown

| Questionnaire | Total | Full | Partial | None | N/A | Evidence-only |
|---|---|---|---|---|---|---|
| AWS Questionnaire | 32 | 17 | 12 | 0 | 3 | 0 |
| ISD IT Risk Assessment | 50 | 45 | 0 | 0 | 4 | 1 |
| OWASP Top 10 | 10 | 4 | 6 | 0 | 0 | 0 |
| PCI DSS Assessment Form | 10 | 0 | 0 | 0 | 10 | 0 |
| SIG Lite 2025 | 107 | 53 | 22 | 0 | 32 | 0 |
| Insurances | 1 | 0 | 0 | 0 | 0 | 1 |
| Security Audits | 2 | 0 | 0 | 0 | 0 | 2 |

ISD grew by 12 rows (mostly Additional Cybersecurity 5.x SMTP/email subqueries plus End-user / Telecom / Server sub-detail). SIG Lite grew by 18 rows (mostly P.2.x privacy classifications, M.1.x endpoint subqueries, H.2.1 password confidentiality, I.3.x web/API hardening, J.5.1 malware monitoring, P.3.1 / P.5.1 / P.5.3 privacy documentation).

## User-authoritative overrides

10 rows have user-populated `Additional Info Added`. In each case the authoritative text is prepended to the Proposed Answer, Coverage is upgraded where warranted (Partial → Full, Evidence-only → Full), and Flag Risk is lowered one step (Medium → Low, High → Medium). The 10 rows are: Request Details Q1, Q2, Q8; Identity & Access Management Q1; Additional Cybersecurity 5.6; SIG Lite A.1, B.1, B.2, C.1, C.4.

---

*The CSV is the authoritative per-row analysis. `SUMMARY.md` and `GAPS.md` remain useful for exec-readable structure but reflect section-level / actionable-subset framing rather than per-row grades.*
