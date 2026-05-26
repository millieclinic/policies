# Real Gaps — Actionable Subset

Four sections have genuine gaps. Three need a one-paragraph clause added to an existing original; one is evidence-only and needs an attachment, not a policy edit.

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
