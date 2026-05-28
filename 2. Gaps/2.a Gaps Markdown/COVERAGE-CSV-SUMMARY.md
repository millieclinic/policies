# Coverage CSV — Summary

This summary describes the row-by-row coverage matrix at `coverage_matrix.csv` in the same directory. The CSV is the authoritative per-row analysis; `SUMMARY.md` and `GAPS.md` remain useful for exec-readable structure.

The matrix is generated against the 17-policy `Current Policies (… Generated)/3.a Final Markdown/` set (post-consolidation). The CSV's **Plain English** column is a layman's translation of each questionnaire item for non-security readers.

**Source CSV:** `ECH Security Docs/ECH Security Assessment Questions - Sheet2.csv` — the user-maintained authoritative workbook. The user populates `Current Answer`, `Additional Info Added`, and `Flags/Notes` as new info arrives, and may add new questions / sections. Re-sync into `coverage_matrix.csv` via `python3 scripts/sync-ech-sheet2.py`.

**Total rows:** 217 (was 212; +5 user-added rows in the latest sync — see "Recent sync" below).

## Coverage counts

| Coverage | Count |
|---|---|
| Full | 121 |
| Partial | 40 |
| None | 0 |
| N/A | 52 |
| Evidence-only | 4 |

## Flag Risk counts

| Flag Risk | Count |
|---|---|
| High | 19 |
| Medium | 25 |
| Low | 121 |
| None | 52 |

## Recent sync (2026-05-28)

Pulled in user changes from Sheet2:

- **5 net-new rows** added by the user, all in SIG Lite 2025:
  - T.1 — Vulnerability Management Program Policy (Partial → recommends a one-paragraph addition to `01c. Risk Management Policy`)
  - T.2 — Cybersecurity supply-chain risk management (Partial → same C-SCRM addition already proposed for SIG S.32 closes this)
  - U.1 — Servers used for scoped data (Full — Millie has no on-prem servers; cloud-only)
  - V.1 — Cloud hosting services provided (N/A — Millie does not provide cloud hosting)
  - V.2 — Cloud hosting provider audit reports (N/A — follows from V.1)
- **14 rows** had their Proposed Answer regenerated because the user added new `Current Answer` or `Additional Info Added` content (notably A04/A06 OWASP rows with BreachLock + patch-system details, and Encryption row with "We don't use EC2").
- **12 rows** had user-input changes that didn't require a Proposed Answer rewrite (the user's content was already implied by the existing answer).
- **186 rows** carried over unchanged from the prior sync.

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

## User-authoritative input

The user populated 169 cells in the `Current Answer` column (137 of those are new vs the original ECH-provided answers) plus 10 in `Additional Info Added`. In every case the user's content is treated as authoritative and is the lead of the Proposed Answer; AI elaboration follows as supporting context, never as a contradiction.

| Source of user input | Rows populated | New vs original ECH | Treatment |
|---|---|---|---|
| `Current Answer` (user-modified or user-added) | 169 | 137 | Lead the Proposed Answer; upgrade Coverage where warranted; lower Flag Risk one step |
| `Additional Info Added` | 10 | 10 | Same treatment |

**Of the 137 user-modified `Current Answer` rows, 117 (85%) had the user's answer already integrated** by the initial generation pass. The remaining 20 were fixed manually in a follow-up pass — these were cases where the AI elaborated past or contradicted the user's literal input. Notable manual fixes:

- **ISD Additional Cybersecurity Q4 (vuln scanning)** — user said "No" (vendor Millie does not scan ECH's environment); AI had incorrectly said "Yes." Corrected.
- **SIG M.1.3 (MDM program)** — user said "NO" (no operational MDM vendor yet); AI had said "Yes" citing the Workstation Use Policy stance. Corrected — policy stance documented, operational deployment pending; Flag Risk stays High.
- **SIG O.4 (hazardous chemicals)** — user said "Yes"; AI had said "Partial." Promoted to Full per Medical Waste Management Plan.
- **SIG O.9 (Health & Safety policy)** — user said "N/A" (no standalone policy at Millie's headcount); AI had said "Partial." Demoted to N/A.
- **ISD Timeline rows** — user provided specific dates (2026-07-31 start, 45-day duration) and a detailed project-scope paragraph; AI had given generic "to be confirmed" placeholders. Replaced with user's actual values.
- **ISD Request Details Q3–Q5, IAM Q3, EUC Q2–Q3, Telecom Q1, Integration Q1, Additional Cyber Q6** — user provided concrete values where AI had reframed the question. Replaced with user's literal answers.

---

*The CSV is the authoritative per-row analysis. `SUMMARY.md` and `GAPS.md` remain useful for exec-readable structure but reflect section-level / actionable-subset framing rather than per-row grades.*
