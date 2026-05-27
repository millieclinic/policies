# ECH Gap Analysis — Row-Level Verification

Re-checked every row inside each previously-rated **No Gap** section (15 sections, ~75 rows) against the actual text of the 28 originals in `3. final_policies/`. The section-level pass was directionally right but coarse — it hid real row-level gaps in **SIG S (SCRM)**, **SIG K (Resilience)**, **SIG G (IT Ops / Change Mgmt)**, and **SIG J (Incident review methodology / evidence integrity)**. Findings below.

---

## §1 — Newly-found gaps (rows inside "No Gap" sections that are actually gaps)

| CSV row | Q ref | Question (abbrev) | Why the section-level "No Gap" was wrong | Severity | Recommended fix |
|---|---|---|---|---|---|
| 117 | SIG K.2 | Formal, documented IT DR exercise/testing program | Contingency Planning Policy §III(b)–(d) describes backups, DR plan, third-party coordination, but is silent on **exercising / testing** the DR plan on a cadence. CSV already flagged "FOLLOW UP." Section-level pass treated K-block as covered. | Standard | `03d HIPAA - Contingency Planning Policy.md` — add 1 sentence to §III(d) "Other Protective Measures": "The Chief Security Officer shall coordinate at least an annual tabletop or walk-through exercise of the disaster recovery plan, document the outcome, and feed material findings into the risk management process." |
| 104 | SIG G.2 | Operational Change Management / Change Control policy with owner & review | SDLC Policy §III(c) covers "testing & validation prior to deployment," but never names a Change Management program, approval gates, change log, or rollback. ECH assessor expecting a discrete CM clause will not find one. | Standard | `System Development Life Cycle (SDLC) & Asset Lifecycle Policy.md` — append to §III(c): "Changes to production systems require peer review and approval through Company's source-control and deployment pipeline (currently GitHub pull-request review + Aptible deploys). The Chief Security Officer is the owner of this change-control process, which is reviewed at least annually. A record of production changes is retained via Git history and Aptible deploy logs." |
| 176 | SIG S.32 | Documented, approved C-SCRM policy (strategy, objectives, supplier adoption, contingency) | Info Sec Framework §11 covers vendor onboarding / BAA / flow-down — that answers S.1, not S.32. There is no document titled or framed as a **Cybersecurity Supply Chain Risk Management** policy with strategy/objectives. Section-level pass conflated the two. | Standard | `Millie Information Security & Data Governance Framework (1).md` — append to §11: "Millie's third-party risk management process functions as Company's Cybersecurity Supply Chain Risk Management (C-SCRM) program. Its strategy is to limit supply-chain exposure through BAA-gated PHI access, vendor concentration disclosed and reviewed in the Contingency Planning Policy, and contractual flow-down to subcontractors. Its objectives are reviewed annually by the Chief Security Officer alongside the risk assessment." (Terminology mismatch note for assessor: Millie's "third-party risk management" = ECH's "C-SCRM.") |
| 177 | SIG S.57 | Media protection policies cover supply-chain concerns through the SDLC | SDLC Policy §III(e) covers media sanitization / disposal but not media handled *within the supply chain* (vendor-returned drives, third-party-furnished hardware). At Millie's scale this is largely N/A (cloud-only, no shipped media), but it is not stated anywhere. | Low | `System Development Life Cycle (SDLC) & Asset Lifecycle Policy.md` — append 1 sentence to §III(e): "Where vendors or contractors handle physical media on Company's behalf, the vendor's media-protection controls are reviewed during BAA / vendor onboarding; Company's cloud-first posture limits supply-chain media exposure to vendor-owned infrastructure." |
| 178 | SIG S.61 | Integrate C-SCRM when developing security planning policy | No document explicitly ties supply-chain risk into the security-planning process. Addressed by the same Framework §11 addition above; a single sentence cross-referencing risk-management cycle closes this. | Low | Same edit as S.32 above also closes S.61 (one combined sentence noting C-SCRM is integrated into the annual security planning / risk-assessment cycle). |
| 179 | SIG S.80 | Security plans clearly define personnel responsibilities for supply chain security risk management | No clause names the **owner** of supply-chain security responsibilities. Implicit (Chief Security Officer + Chief Privacy Officer), but never stated. | Low | Closed by the same Framework §11 addition — explicitly name the Chief Security Officer (in coordination with Chief Privacy Officer and Legal) as owner of the C-SCRM function. |
| 180 | SIG S.100 | System & communications protection policies address cybersecurity risks throughout the supply chain | Encryption Policy + AWS/Aptible IR Policy address sys/comm protection internally but not "throughout the supply chain." | Low | Closed by the same Framework §11 addition — note that encryption-in-transit and network protections are required of all subcontractors/subprocessors via BAA flow-down. |
| 113 | SIG J.5 | Specific methodology to regularly review events on scoped systems to uncover potential incidents | Incident Mgmt Policy + AWS/Aptible IR cover *response to reported incidents* but not the proactive **review methodology** (cadence, who, what they look at). Info Sec Framework §7 mentions "Relevant logs are reviewed as needed in response to security events" — but "as needed" is not a methodology. | Standard | `Millie Information Security & Data Governance Framework (1).md` — replace the "as needed" sentence in §7 with: "The Chief Security Officer (or designee) reviews GuardDuty findings, CloudTrail anomalies, and Aptible application audit logs on at least a monthly cadence to identify potential incidents, in addition to event-driven review. Findings are logged and escalated through the Security Incident Management Policy." |
| 115 | SIG J.14 | Incident-investigation actions formally documented and protected from unauthorized changes | Incident Mgmt Policy §III(c) Log + AWS/Aptible IR §VII Log describe **what** is logged, not that the log is **protected from unauthorized changes** (write-once, access-restricted, retained). | Low | `03s HIPAA - Security Incident Management Policy.md` — add 1 sentence to §III(c) Log: "The incident log is maintained in a restricted-access Company system, edits are auditable, and the log is retained for at least 6 years consistent with HIPAA documentation requirements." |
| 73 | OWASP A02 | Sensitive data protection — extra protection for financial / healthcare / PII | CSV already flagged "FOLLOW UP — Need update to password storage" with `Remediate before submitting = Yes`. Password Mgmt Policy describes **user** password rules, not server-side **password storage** (hashing algorithm, salting). Encryption Policy covers data in transit, not credential at-rest hashing. | Standard | `03o HIPAA - Password Management Policy.md` — add 1 sentence to §III: "User account passwords are stored using an industry-standard one-way hash with per-user salt (bcrypt or equivalent); plaintext passwords are never stored or logged." |
| 77 | OWASP A06 | Regular vuln scanning + patch management process | Info Sec Framework now mentions vuln scanning (post-Gap-1 edit); SDLC mentions "security updates and patching" as a bullet. Neither states **cadence, scanner used, or SLA for patching severity-rated vulns**. CSV flagged "FOLLOW UP — Upgrade Github, Yes (remediate)." | Standard | `Millie Information Security & Data Governance Framework (1).md` — append to §6 (after the DMARC sentence): "Dependency vulnerabilities are surfaced via GitHub Dependabot and triaged at least weekly; Critical/High findings are remediated within 30 days, Medium within 90 days, subject to the risk-management exception process." |
| 78 | OWASP A07 | Protect against attackers compromising passwords, keys, session tokens | Password Mgmt Policy covers password hygiene; Encryption Policy covers key custody. No explicit session-token / MFA-bypass / brute-force-protection stance. CSV flagged "FOLLOW UP, Yes (remediate)." | Standard | `03o HIPAA - Password Management Policy.md` — add 1 sentence: "Application sessions are protected by signed, short-lived tokens; failed-login attempts are rate-limited and monitored; and session invalidation occurs on logout, password change, or role revocation." |

**Total newly-found gaps:** 12 (0 Critical, 6 Standard, 4 Low — note S.32/S.57/S.61/S.80/S.100 collapse into ONE Framework §11 addition; J.5 and OWASP A06 both collapse into ONE Framework §6/§7 addition).

---

## §2 — Confirmed No Gap rows (the easy ones)

- **AWS / AWS Account Management:** 7/7 confirmed (operational answers; no policy text required).
- **AWS / Encryption:** 2/2 confirmed (Encryption Policy + Aptible reference).
- **AWS / Identity & Access Mgmt:** 9/9 confirmed (Password Mgmt + Safeguards §III(b) + Info Sec §4; CSV operational answers).
- **AWS / Network Security:** 6/6 confirmed.
- **AWS / Detection & Monitoring:** 3/3 confirmed.
- **AWS / Processes:** 5/5 confirmed (SDLC + AWS/Aptible IR cover IaC, IR plan, backups).
- **ISD / Identity & Access Management:** 3/3 confirmed.
- **ISD / Integration Requirements:** 1/1 confirmed.
- **ISD / End-user Compute Requirements:** 7/7 confirmed.
- **OWASP Top 10:** 7/10 confirmed (A01, A03, A04, A05, A08, A09, A10) — A02/A06/A07 newly flagged in §1.
- **SIG A. Enterprise Risk Mgmt:** 1/1 confirmed.
- **SIG B. Nth Party Mgmt:** 2/2 confirmed.
- **SIG C. Information Assurance:** 2/2 confirmed.
- **SIG D. Asset & Info Mgmt:** 3/3 confirmed (note: D.3 retention "schedule" is terminologically thin — Info Sec §9 says "indefinitely" — but substantively answers the question; flag as terminology mismatch for assessor, not a gap).
- **SIG F. Physical & Environmental:** 1/1 confirmed.
- **SIG G. IT Ops Mgmt:** 2/3 confirmed (G.1, G.3); G.2 newly flagged.
- **SIG H. Access Control:** 2/2 confirmed.
- **SIG I. Application Mgmt:** 3/3 confirmed (affirmative-fact questions).
- **SIG J. Cybersecurity Incident Mgmt:** 3/5 confirmed (J.1, J.4, J.11); J.5 and J.14 newly flagged.
- **SIG K. Operational Resilience:** 6/8 confirmed (K.1, K.3, K.5, K.6, K.7, K.11); K.2 newly flagged (K.4 and K.30 already in GAPS.md).
- **SIG N. Network Security:** 10/10 confirmed (no on-prem network, no wireless infra in scope, no DMZ — answered via posture not policy text).
- **SIG P. Privacy Management:** 8/8 in-scope rows confirmed (P.9 and P.12 stay N/A per existing justifications).
- **SIG S. SCRM:** 1/6 confirmed (S.1 only); S.32/S.57/S.61/S.80/S.100 newly flagged.

---

## §3 — Recommended updates to SUMMARY.md

| Section | Current | Proposed | Reason |
|---|---|---|---|
| SIG S. Supply Chain Risk Management (SCRM) | No Gap | **Partial** | S.32 (Standard) + S.57/S.61/S.80/S.100 (Low) — one combined Framework §11 sentence closes all five. |
| SIG K. Operational Resilience | Gap (K.4, K.30) | **Gap** — also add K.2 | K.2 DR-exercise/testing cadence missing; add 1 sentence to Contingency Planning. |
| SIG G. IT Operations Mgmt | No Gap | **Partial** | G.2 Change Management not discretely named — add 1 sentence to SDLC §III(c). |
| SIG J. Cybersecurity Incident Mgmt | No Gap | **Partial** | J.5 (proactive review methodology) + J.14 (log integrity protection) need short clauses. |
| OWASP Top 10 | No Gap | **Partial** | A02 (password storage), A06 (vuln-scan cadence/SLA), A07 (session tokens) need 1-sentence each. |

All other "No Gap" sections remain **No Gap**.

---

## §4 — Recommended updates to GAPS.md

### Gap 5 — DR Exercise Testing Cadence (SIG K.2)

- **Section:** SIG Lite 2025 / K. Operational Resilience
- **CSV rows:** 117 (K.2 — flagged FOLLOW UP)
- **What ECH expects:** Evidence that the DR plan is actually exercised/tested, with cadence and documentation.
- **What originals say:** `Contingency Planning Policy` §III(b)–(d) describes backups and a DR plan but never says it is exercised.
- **What to add:** "The Chief Security Officer shall coordinate at least an annual tabletop or walk-through exercise of the disaster recovery plan, document the outcome, and feed material findings into the risk management process."
- **Where to add it:** `03d HIPAA - Contingency Planning Policy.md` — append to §III(d) Other Protective Measures.

### Gap 6 — Change Management (SIG G.2)

- **Section:** SIG Lite 2025 / G. IT Operations Management
- **CSV rows:** 104 (G.2)
- **What ECH expects:** A named Change Management / Change Control program with owner and review cadence.
- **What originals say:** `SDLC & Asset Lifecycle Policy` §III(c) covers pre-deploy validation but does not name a change-control program.
- **What to add:** "Changes to production systems require peer review and approval through Company's source-control and deployment pipeline (currently GitHub pull-request review + Aptible deploys). The Chief Security Officer is the owner of this change-control process, which is reviewed at least annually. A record of production changes is retained via Git history and Aptible deploy logs."
- **Where to add it:** `System Development Life Cycle (SDLC) & Asset Lifecycle Policy.md` — append to §III(c) Testing & Implementation.

### Gap 7 — C-SCRM Framing (SIG S.32 / S.57 / S.61 / S.80 / S.100)

- **Section:** SIG Lite 2025 / S. Supply Chain Risk Management
- **CSV rows:** 176, 177, 178, 179, 180
- **What ECH expects:** A document explicitly framed as Cybersecurity Supply Chain Risk Management — strategy, objectives, supplier adoption, contingency planning, named owner, integration with security planning, and system/communications protection across the supply chain.
- **What originals say:** Info Sec Framework §11 covers third-party / vendor risk management with BAA flow-down, but never uses the "C-SCRM" framing nor names an owner of supply-chain security specifically.
- **What to add:** A 3-sentence paragraph appended to §11: (1) Millie's third-party risk management process functions as the Company's C-SCRM program, with the Chief Security Officer (in coordination with the Chief Privacy Officer and Legal) as the named owner. (2) C-SCRM objectives are reviewed annually alongside the security risk assessment, and supplier-related cybersecurity controls (encryption in transit, access management, incident notification) are required of subcontractors and subprocessors via BAA flow-down. (3) Vendor-furnished or vendor-returned physical media is addressed via the vendor onboarding / BAA review; Millie's cloud-first posture limits supply-chain media exposure to vendor-owned infrastructure.
- **Where to add it:** `Millie Information Security & Data Governance Framework (1).md` — append to §11.

### Gap 8 — Incident-Review Methodology + Log Integrity (SIG J.5 / J.14) + OWASP A06

- **Section:** SIG Lite 2025 / J. Cybersecurity Incident Mgmt + OWASP A06
- **CSV rows:** 77 (A06), 113 (J.5), 115 (J.14)
- **What ECH expects:** A stated methodology + cadence for proactive log/event review; assurance the incident log is tamper-resistant; a stated vuln-scanning cadence and patching SLA.
- **What originals say:** Reactive incident response is well documented; proactive review and tamper-resistance are not stated; vuln-scan cadence and patch SLAs are not stated.
- **What to add:** (a) Info Sec Framework §7 — replace "as needed" with monthly GuardDuty/CloudTrail/Aptible-audit-log review cadence. (b) Info Sec Framework §6 — add Dependabot weekly triage + 30/90-day patch SLAs for Critical/High/Medium. (c) Security Incident Mgmt Policy §III(c) — add 1 sentence on restricted-access, auditable, 6-year retention of the incident log.
- **Where to add it:** `Millie Information Security & Data Governance Framework (1).md` (§6 and §7) + `03s HIPAA - Security Incident Management Policy.md` (§III(c)).

### Gap 9 — Password Storage + Session/Token Protection (OWASP A02 / A07)

- **Section:** OWASP Top 10 / A02 + A07
- **CSV rows:** 73 (A02), 78 (A07)
- **What ECH expects:** A stated stance on how user credentials are stored (hashing) and how session tokens are protected.
- **What originals say:** Password Mgmt Policy covers user password hygiene but not server-side storage; nothing on session tokens.
- **What to add:** Two 1-sentence additions to `03o HIPAA - Password Management Policy.md`: (1) "User account passwords are stored using an industry-standard one-way hash with per-user salt (bcrypt or equivalent); plaintext passwords are never stored or logged." (2) "Application sessions are protected by signed, short-lived tokens; failed-login attempts are rate-limited and monitored; and session invalidation occurs on logout, password change, or role revocation."
- **Where to add it:** `03o HIPAA - Password Management Policy.md` — append to §III.
