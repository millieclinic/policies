# Coverage CSV — Summary

This summary describes the row-by-row coverage matrix at `coverage_matrix.csv` in the same directory. The CSV is the authoritative per-row analysis; `SUMMARY.md` and `GAPS.md` remain useful for exec-readable structure.

The matrix is generated against the 29-policy `3. final_policies/` set. Column 5 of the CSV is **Plain English** — a layman's translation of each questionnaire item for non-security readers.

**Total rows:** 182 (expected 182)

## Coverage counts

| Coverage | Count |
|---|---|
| Full | 102 |
| Partial | 36 |
| None | 0 |
| N/A | 41 |
| Evidence-only | 3 |

## Flag Risk counts

| Flag Risk | Count |
|---|---|
| High | 19 |
| Medium | 18 |
| Low | 104 |
| None | 41 |

## Required Fix totals

**Total word count of all `Required Fix - Text` values:** 715

### Files needing additions (cumulative words)

| File | Cumulative words |
|---|---|
| `Millie Information Security & Data Governance Framework (1).md` | 543 |
| `System Development Life Cycle (SDLC) & Asset Lifecycle Policy.md` | 57 |
| `03o HIPAA - Password Management Policy.md` | 53 |
| `03s HIPAA - Security Incident Management Policy (2).md` | 31 |
| `03d HIPAA - Contingency Planning Policy (1).md` | 31 |

## Top 10 highest-priority rows (Flag Risk = High)

Ordered by which assessor red-flag they represent (missing-control rows first, then evidence-only, then terminology / framing gaps).

| # | Questionnaire | Section | Item | Question (abbrev) | Gap |
|---|---|---|---|---|---|
| 1 | Insurances | Insurances | 1 | Do you have document "Cyber Liability / Data Privacy"? | Contingency Planning Policy commits to obtaining the coverage but the actual certificate is the deliverable; submission must include the certificate as an attachment. |
| 2 | Security Audits | Security Audits | 1 | Do you have document "Penetration Testing"? | No pentest evidence exists; either commission a third-party pentest (recommended) or answer truthfully that none is on file. Submission impact depends on ECH appetite. |
| 3 | Security Audits | Security Audits | 2 | Do you have document "General Security Audit"? | No external audit attestation; provide the annual internal HIPAA risk assessment as a compensating artifact and disclose plans for a third-party audit if planned. |
| 4 | SIG Lite 2025 | K. Operational Resilience | K.2 | Is there a formal, documented information technology disaster recovery exercise … | Source CSV flagged FOLLOW UP. Contingency Planning Policy currently describes backups, DR plan, and third-party coordination but does not require periodic exercise/testing of the DR plan. |
| 5 | SIG Lite 2025 | M. Endpoint Security | M.1.3 | M.1.3 Is there a mobile device management program in place that has been approve… | Source CSV answered NO and flagged FOLLOW UP. Workstation Use §III(d) now contains the documented program, but MDM tooling implementation is operationally pending and the assessor may want vendor confirmation. |
| 6 | SIG Lite 2025 | M. Endpoint Security | M.1.5 | M.1.5 Are non-company managed computing devices used to connect to the company n… | Source CSV answered YES and flagged FOLLOW UP. Workstation Use §III(d) now contains the restriction; assessor may still want network-segmentation evidence. |
| 7 | SIG Lite 2025 | M. Endpoint Security | M.1.5 | M.1.6 Are any mobile devices with access to scoped data Constituent owned (BYOD)… | Source CSV answered YES and flagged FOLLOW UP. Workstation Use §III(d) now contains the BYOD posture; assessor may want MDM enrollment evidence. |
| 8 | OWASP Top 10 | A02:2021 - Cryptographic Failures | 1 | Do you protect sensitive data, such as financial, healthcare, and PII through ex… | Source CSV explicitly flagged 'Need update to password storage' with Remediate=Yes; Password Management Policy currently covers user password hygiene but lacks an explicit server-side hashing clause. |
| 9 | OWASP Top 10 | A06:2021 - Vulnerable and Outdated Components | 1 | Do you regularly scan for vulnerabilities and is there a patch management proces… | Source CSV flagged 'Upgrade Github, Remediate=Yes'; current policy lacks an explicit scanner-cadence-and-patch-SLA clause. |
| 10 | OWASP Top 10 | A07:2021 - Identification and Authentication Failures | 1 | Do you protect against attackers compromising passwords, keys, or session tokens… | Source CSV flagged Remediate=Yes; Password Management Policy currently covers user password hygiene but lacks explicit session-token / brute-force language. |

## Per-questionnaire breakdown

| Questionnaire | Total | Full | Partial | None | N/A | Evidence-only |
|---|---|---|---|---|---|---|
| AWS Questionnaire | 32 | 17 | 12 | 0 | 3 | 0 |
| ISD IT Risk Assessment | 38 | 36 | 0 | 0 | 2 | 0 |
| OWASP Top 10 | 10 | 4 | 6 | 0 | 0 | 0 |
| PCI DSS Assessment Form | 10 | 0 | 0 | 0 | 10 | 0 |
| SIG Lite 2025 | 89 | 45 | 18 | 0 | 26 | 0 |
| Insurances | 1 | 0 | 0 | 0 | 0 | 1 |
| Security Audits | 2 | 0 | 0 | 0 | 0 | 2 |

---

*The CSV is the authoritative per-row analysis. `SUMMARY.md` and `GAPS.md` remain useful for exec-readable structure but reflect section-level / actionable-subset framing rather than per-row grades.*