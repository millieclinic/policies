# Real Gaps — Actionable Subset

Eight sections have genuine gaps after the row-level verification (see [ROW-LEVEL-VERIFICATION.md](ROW-LEVEL-VERIFICATION.md)). All eight collapse into short clauses appended to **existing** files — no new policy documents required. One is evidence-only and needs an attachment rather than a policy edit.

Gaps 1–4 surfaced in the initial section-level pass. Gaps 5–9 surfaced in the row-level verification that followed (the section pass was too coarse and hid these inside sections it called "No Gap" — notably the C-SCRM gap inside SIG S).

---

## Gap 1 — Email Authentication & Anti-Malware Exclusions

- **Section:** ISD IT Risk Assessment / Additional Cybersecurity Questions
- **CSV rows:** 50, 51, 55
- **What ECH expects:** Stance on AV / security exclusions, vuln-scan exclusions, and whether the third-party adopts DMARC.
- **What originals say:** Nothing. No active original addresses DMARC / SPF / DKIM or anti-malware exclusion handling.
- **What to add:** A one-paragraph clause stating: Millie uses Google Workspace's built-in anti-malware (no custom exclusions); transactional email is sent via SendGrid with SPF, DKIM, and DMARC configured at policy = quarantine or reject; vulnerability scanning is performed against in-scope hosted services (Aptible / AWS) with no application-side exclusions, and any one-off operational exclusion requires Chief Security Officer approval.
- **Where to add it:** `Millie Information Security & Data Governance Framework.md` — append to §6 Data Transmission & Sharing.

---

## Gap 2 — BYOD & Mobile Device Management

- **Section:** SIG Lite 2025 / M. Endpoint Security
- **CSV rows:** 132 (M.1.3), 133 (M.1.5), 134 (M.1.6) — all flagged "FOLLOW UP"
- **What ECH expects:** A documented MDM program; a stance on non-company devices touching the network; a stance on BYOD with scoped data.
- **What originals say:** `Workstation Use Policy` references mobile phones / iPads and locking timeouts, and `Remote Access Policy` covers Users on personal devices, but no BYOD / MDM stance is documented.
- **What to add:** A one-paragraph clause stating: BYOD is permitted for email, Slack, and approved SaaS only — no PHI may be stored locally on personal devices. Company-issued devices and personal devices that access PHI must be enrolled in Millie's MDM (vendor selection pending; tracked operationally), require device passcode + auto-lock + disk encryption + remote-wipe capability, and may be remotely wiped on termination or loss. Non-managed personal devices are restricted to web-based SaaS via SSO / MFA and may not store PHI.
- **Where to add it:** `03w HIPAA - Workstation Use Policy.md` — append as new procedure section "BYOD & Mobile Device Management."

---

## Gap 3 — Pandemic Operations & Multi-Vendor Resiliency

- **Section:** SIG Lite 2025 / K. Operational Resilience
- **CSV rows:** 119 (K.4 — answered NO), 124 (K.30 — answered NO)
- **What ECH expects:** A pandemic / infectious-disease outbreak plan, and a resiliency strategy with multi-vendor risk mitigation.
- **What originals say:** `Millie Clinic COVID Policy.md` covers patient-facing isolation / exposure logic but is silent on staff-facing operational continuity. `Contingency Planning Policy` covers data backup, IT contingency, and disaster recovery but not pandemic operations or single-vendor concentration risk.
- **What to add:** A one-paragraph clause stating: For pandemic / infectious-disease events, Millie's COVID Policy (or its successor) governs patient interactions; clinical operations may shift to telehealth-first scheduling, on-site staffing reduces to essential personnel, and PPE protocols follow current CDPH / CDC guidance. Millie operates a cloud-first stack with single-vendor dependencies on Aptible (compute / databases), AWS (storage / logging), Cloudflare (DNS / CDN), and Google Workspace (collaboration); this concentration is a documented accepted risk reviewed annually by the Chief Security Officer, with exit considerations (data portability, vendor lock-in) factored into the BAA review for each.
- **Where to add it:** `03d HIPAA - Contingency Planning Policy.md` — append as new section "Pandemic Operations & Multi-Vendor Risk."

---

## Gap 4 — Insurance Certificate + Audit Attestations (Evidence, not Policy)

- **Section:** Insurances + Security Audits
- **CSV rows:** 181, 182, 183
- **What ECH expects:** Attached documents — cyber-liability certificate; pentest report; general security audit (SOC 2 / HITRUST / etc.).
- **What originals say:** `Contingency Planning Policy.md` §III(h) commits to obtaining cyber-liability insurance but does not substitute for the certificate.
- **What to add:** **No policy change.** Attach the actual cyber-liability certificate to the ECH submission package. For pentest + general audit: either commission a third-party pentest (recommended for credibility) or answer truthfully "none currently on file; will share when commissioned."
- **Where to add it:** N/A — submission package, not policy text.

---

## Gap 5 — DR Exercise / Testing Cadence

- **Section:** SIG Lite 2025 / K. Operational Resilience
- **CSV rows:** 117 (K.2 — flagged FOLLOW UP)
- **What ECH expects:** Evidence that the DR plan is actually exercised / tested, with cadence and documentation.
- **What originals say:** `Contingency Planning Policy.md` §III(b)–(d) describes backups, the DR plan, and third-party coordination, but is silent on **exercising** the plan.
- **What to add:** One sentence: "The Chief Security Officer shall coordinate at least an annual tabletop or walk-through exercise of the disaster recovery plan, document the outcome, and feed material findings into the risk management process."
- **Where to add it:** `03d HIPAA - Contingency Planning Policy (1).md` — append to §III(d) Other Protective Measures.

---

## Gap 6 — Change Management

- **Section:** SIG Lite 2025 / G. IT Operations Management
- **CSV rows:** 104 (G.2)
- **What ECH expects:** A named Change Management / Change Control program with owner and review cadence.
- **What originals say:** `SDLC & Asset Lifecycle Policy` §III(c) covers pre-deploy validation but never names a change-control program.
- **What to add:** "Changes to production systems require peer review and approval through Company's source-control and deployment pipeline (currently GitHub pull-request review + Aptible deploys). The Chief Security Officer is the owner of this change-control process, which is reviewed at least annually. A record of production changes is retained via Git history and Aptible deploy logs."
- **Where to add it:** `System Development Life Cycle (SDLC) & Asset Lifecycle Policy.md` — append to §III(c) Testing & Implementation.

---

## Gap 7 — C-SCRM Framing (one paragraph closes S.32 + S.57 + S.61 + S.80 + S.100)

- **Section:** SIG Lite 2025 / S. Supply Chain Risk Management (SCRM)
- **CSV rows:** 176 (S.32), 177 (S.57), 178 (S.61), 179 (S.80), 180 (S.100)
- **What ECH expects:** A document explicitly framed as **Cybersecurity Supply Chain Risk Management** — strategy, objectives, supplier adoption, contingency planning, named owner, integration with security planning, and system / communications protection across the supply chain.
- **What originals say:** `Millie Information Security & Data Governance Framework (1).md` §11 covers third-party / vendor risk management with BAA flow-down — that's a substantive answer to S.1 (sub-tier flow-down), but it never uses the "C-SCRM" framing nor names an owner of supply-chain security specifically. Without the C-SCRM framing, an assessor running a SIG checklist will not find S.32 / S.57 / S.61 / S.80 / S.100 even though the underlying controls are largely in place.
- **What to add:** A 3-sentence paragraph appended to §11: (1) Millie's third-party risk management process functions as the Company's Cybersecurity Supply Chain Risk Management (C-SCRM) program, with the Chief Security Officer (in coordination with the Chief Privacy Officer and Legal) as the named owner. (2) C-SCRM objectives are reviewed annually alongside the security risk assessment, and supplier-related cybersecurity controls — encryption in transit, access management, and incident notification — are required of subcontractors and subprocessors via BAA flow-down. (3) Vendor-furnished or vendor-returned physical media is addressed during vendor onboarding / BAA review; Millie's cloud-first posture limits supply-chain media exposure to vendor-owned infrastructure.
- **Where to add it:** `Millie Information Security & Data Governance Framework (1).md` — append to §11.

---

## Gap 8 — Proactive Log Review + Patch SLA + Tamper-Resistant Incident Log (J.5 + A06 + J.14)

- **Section:** SIG Lite 2025 / J. Cybersecurity Incident Mgmt + OWASP A06
- **CSV rows:** 77 (OWASP A06 — flagged Remediate), 113 (J.5), 115 (J.14)
- **What ECH expects:** A stated methodology + cadence for proactive log / event review; assurance the incident log is tamper-resistant; a stated vuln-scanning cadence and patching SLA.
- **What originals say:** Reactive incident response is well documented. Proactive review is described as "as needed" (Framework §7), vuln scanning has no cadence or SLA stated anywhere, and the incident log is described as a Log but not as tamper-resistant.
- **What to add (three small edits):**
  1. **Framework §7** — replace "as needed" with: "The Chief Security Officer (or designee) reviews GuardDuty findings, CloudTrail anomalies, and Aptible application audit logs on at least a monthly cadence to identify potential incidents, in addition to event-driven review. Findings are logged and escalated through the Security Incident Management Policy."
  2. **Framework §6** — append: "Dependency vulnerabilities are surfaced via GitHub Dependabot and triaged at least weekly; Critical / High findings are remediated within 30 days, Medium within 90 days, subject to the risk-management exception process."
  3. **Security Incident Management §III(c)** — append to the Log paragraph: "The incident log is maintained in a restricted-access Company system, edits are auditable, and the log is retained for at least 6 years consistent with HIPAA documentation requirements."
- **Where to add it:** `Millie Information Security & Data Governance Framework (1).md` §6 and §7; `03s HIPAA - Security Incident Management Policy (2).md` §III(c).

---

## Gap 9 — Password Storage + Session / Token Protection (OWASP A02 + A07)

- **Section:** OWASP Top 10 / A02 + A07
- **CSV rows:** 73 (A02 — flagged Remediate), 78 (A07 — flagged Remediate)
- **What ECH expects:** A stated stance on how user credentials are stored (hashing) and how session tokens are protected.
- **What originals say:** `03o HIPAA - Password Management Policy.md` covers user password hygiene (length, rotation, lockout) but not server-side credential storage; nothing on session tokens.
- **What to add:** Two 1-sentence additions to §III: (1) "User account passwords are stored using an industry-standard one-way hash with per-user salt (bcrypt or equivalent); plaintext passwords are never stored or logged." (2) "Application sessions are protected by signed, short-lived tokens; failed-login attempts are rate-limited and monitored; and session invalidation occurs on logout, password change, or role revocation."
- **Where to add it:** `03o HIPAA - Password Management Policy.md` — append to §III.
