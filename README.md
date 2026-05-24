---
title: "Millie Policies & Compliance"
last_reviewed: 2026-05-24
owner: "Privacy Officer + Security Officer (joint)"
---

# Millie Policies & Compliance

This repository is the source of truth for Millie's HIPAA and information security policies.

- **`New Policy Docs/`** — current canonical policies in Markdown. Edit these.
- **`Policy Docs/`** — historical archive of the original `.docx` / `.pdf` / `.xlsx` source files. Do not edit.
- **This README** — the operating playbook: policy index, compliance calendar, and responsibility matrix. Reviewed by the **Privacy Officer** and **Security Officer** at the start of each quarter.

**How to use this document:**

1. **§1 Policy Index** — confirm every active policy is current. If a policy is out of date, open the file and update it.
2. **§2 Compliance Calendar** — work the recurring tasks for the current month/quarter/year. Tick off each row as it's done; if a task isn't done by its target date, escalate to the policy owner.
3. **§3 Responsibility Matrix** — when something happens (incident, audit, vendor change), use this table to find who is Responsible, Accountable, Consulted, and Informed.

Owner names are listed by **role** (Privacy Officer, Security Officer, CTO, CEO, Practice Manager). Fill in real names alongside each role the first time you use this document.

---

## §1 — Policy Index

All policies live as Markdown files in `New Policy Docs/`. Original `.docx` / `.pdf` source files are preserved in `Policy Docs/` for the historical record. Templates (BAA, Insurance Authorization) and training decks were intentionally not migrated; they remain in `Policy Docs/`.

| Policy | Purpose | Owner |
|---|---|---|
| [information-security-framework.md](New Policy Docs/information-security-framework.md) | Master security and data-governance framework. Anchors all other policies; covers governance, data classification, access control, encryption, logging, incident response, retention, BCP, vendor management. | Security Officer |
| [privacy-policy.md](New Policy Docs/privacy-policy.md) | Patient-facing privacy notice describing how Millie collects, uses, and discloses personal information. | Privacy Officer |
| [sdlc-and-asset-lifecycle.md](New Policy Docs/sdlc-and-asset-lifecycle.md) | System Development Lifecycle and IT asset lifecycle controls — secure design, deployment, maintenance, retirement. | CTO |
| [hipaa-accounting-of-disclosures.md](New Policy Docs/hipaa-accounting-of-disclosures.md) | Procedure for tracking and responding to patient requests for an accounting of PHI disclosures. | Privacy Officer |
| [hipaa-breach-notification.md](New Policy Docs/hipaa-breach-notification.md) | Breach detection, internal reporting, and notification to patients / HHS / state regulators. | Privacy Officer |
| [hipaa-business-associate-agreement.md](New Policy Docs/hipaa-business-associate-agreement.md) | Requirements for identifying Business Associates and executing BAAs before granting PHI access. | Privacy Officer |
| [hipaa-contingency-planning.md](New Policy Docs/hipaa-contingency-planning.md) | Backup, disaster recovery, and emergency operations procedures. | Security Officer |
| [hipaa-de-identifying-phi.md](New Policy Docs/hipaa-de-identifying-phi.md) | Approved methods for de-identifying PHI and creating Limited Data Sets. | Privacy Officer |
| [hipaa-definitions.md](New Policy Docs/hipaa-definitions.md) | Glossary of HIPAA terms used across the rest of the policy suite. | Privacy Officer |
| [hipaa-encryption.md](New Policy Docs/hipaa-encryption.md) | Encryption standards for PHI at rest and in transit, plus key management. | Security Officer |
| [hipaa-marketing.md](New Policy Docs/hipaa-marketing.md) | When patient communications count as Marketing and when authorization is required. | Privacy Officer |
| [hipaa-minimum-necessary.md](New Policy Docs/hipaa-minimum-necessary.md) | Limiting PHI use, disclosure, and request to the minimum necessary for the task. | Privacy Officer |
| [hipaa-paper-documents.md](New Policy Docs/hipaa-paper-documents.md) | Physical handling, storage, and destruction of paper PHI. | Security Officer |
| [hipaa-passwords.md](New Policy Docs/hipaa-passwords.md) | Password complexity, rotation, lockout, and deactivation upon termination. | Security Officer |
| [hipaa-phi-use-and-disclosure.md](New Policy Docs/hipaa-phi-use-and-disclosure.md) | Permitted uses and disclosures of PHI for legal, public health, and regulatory purposes. | Privacy Officer |
| [hipaa-remote-access.md](New Policy Docs/hipaa-remote-access.md) | VPN, MFA, and controls for accessing the IT System from outside the office. | Security Officer |
| [hipaa-right-to-access.md](New Policy Docs/hipaa-right-to-access.md) | Patient right to inspect and obtain copies of their own PHI. 30-day response window. | Privacy Officer |
| [hipaa-right-to-amend.md](New Policy Docs/hipaa-right-to-amend.md) | Patient right to request amendment of their PHI. 60-day response window. | Privacy Officer |
| [hipaa-risk-management.md](New Policy Docs/hipaa-risk-management.md) | Annual security risk assessment, risk mitigation, and reporting to the Risk Review Committee. | Security Officer |
| [hipaa-safeguards.md](New Policy Docs/hipaa-safeguards.md) | Administrative, physical, and technical safeguards required by the HIPAA Security Rule. | Security Officer |
| [hipaa-security-incidents.md](New Policy Docs/hipaa-security-incidents.md) | Detection, investigation, escalation, and annual reporting of security incidents. | Security Officer |
| [hipaa-workstation-use.md](New Policy Docs/hipaa-workstation-use.md) | Acceptable use of workstations (including iPads and personal mobile devices) accessing the IT System. | Security Officer |
| [platform-and-access-matrix.md](New Policy Docs/platform-and-access-matrix.md) | Inventory of every platform / SaaS subscription, who has access, and BAA status. | Security Officer |
| [ech-security-assessment.md](New Policy Docs/ech-security-assessment.md) | Standard security-assessment questions used when evaluating new health-tech vendors. | Security Officer |

---

## §2 — HIPAA Compliance Calendar

Each row: **Task · Source policy · Owner · Notes / target window.** Use this as a checklist.

### Annual

| Task | Source | Owner |
|---|---|---|
| Conduct full HIPAA security risk assessment; document threats, vulnerabilities, likelihood, impact; produce mitigation plan; present to Risk Review Committee (and Board if material risks). | [hipaa-risk-management.md](New Policy Docs/hipaa-risk-management.md) | Security Officer |
| Review and refresh every policy in this folder; update `last_reviewed:` in frontmatter; re-sign if required. | All policies | Privacy Officer + Security Officer |
| Workforce HIPAA training refresh for all personnel (initial training is on hire — see Event-driven section). | [hipaa-safeguards.md](New Policy Docs/hipaa-safeguards.md) | Privacy Officer |
| Prepare annual privacy & security report and submit to the CEO. | [hipaa-security-incidents.md](New Policy Docs/hipaa-security-incidents.md) | Security Officer + Privacy Officer |
| Test the contingency plan end-to-end (failover, restoration, emergency operations) and document results. | [hipaa-contingency-planning.md](New Policy Docs/hipaa-contingency-planning.md) | Security Officer |
| Review every active Business Associate Agreement: confirm vendor is still in scope, renewal date current, subcontractor list accurate. | [hipaa-business-associate-agreement.md](New Policy Docs/hipaa-business-associate-agreement.md) | Privacy Officer |
| Refresh the platform & access matrix end-to-end: confirm every listed app is still in use, every role's access is still correct, every BAA-required vendor still has one signed. | [platform-and-access-matrix.md](New Policy Docs/platform-and-access-matrix.md) | Security Officer |

### Quarterly

| Task | Source | Owner |
|---|---|---|
| Review backup procedure documentation and update if procedures or vendors have changed. | [hipaa-contingency-planning.md](New Policy Docs/hipaa-contingency-planning.md) | Security Officer |
| User access review: walk the platform matrix, confirm every account is still needed; revoke stale access. | [hipaa-minimum-necessary.md](New Policy Docs/hipaa-minimum-necessary.md), [platform-and-access-matrix.md](New Policy Docs/platform-and-access-matrix.md) | Security Officer |
| Vulnerability scan / patch review across infrastructure and endpoints. | [hipaa-safeguards.md](New Policy Docs/hipaa-safeguards.md) | Security Officer + CTO |
| Tabletop drill of an incident-response scenario (e.g., ransomware, lost laptop, phishing). Document findings. | [hipaa-security-incidents.md](New Policy Docs/hipaa-security-incidents.md) | Security Officer |

### Monthly

| Task | Source | Owner |
|---|---|---|
| Spot-check audit logs (Aptible, AWS CloudWatch, admin console) for anomalies. | [information-security-framework.md](New Policy Docs/information-security-framework.md) | Security Officer |
| Verify a recent backup is restorable (test restore in a non-production environment). | [hipaa-contingency-planning.md](New Policy Docs/hipaa-contingency-planning.md) | Security Officer / CTO |
| Confirm no terminated employees still have active credentials in any system on the platform matrix. | [hipaa-passwords.md](New Policy Docs/hipaa-passwords.md), [hipaa-remote-access.md](New Policy Docs/hipaa-remote-access.md) | Security Officer |

### Event-driven

These are deadlines triggered by a specific event — they are not on a schedule but missing them is a compliance failure.

| Trigger | Action | Deadline | Source |
|---|---|---|---|
| Personnel becomes aware of a suspected breach | Report to Chief Privacy Officer | **≤ 48 hours** | [hipaa-breach-notification.md](New Policy Docs/hipaa-breach-notification.md) |
| Confirmed breach of unsecured PHI | Notify affected individuals and applicable agencies | **≤ 60 days from Date of Discovery** | [hipaa-breach-notification.md](New Policy Docs/hipaa-breach-notification.md) |
| Patient submits request for accounting of disclosures | Transmit request to Privacy Officer | **≤ 24 hours of receipt** | [hipaa-accounting-of-disclosures.md](New Policy Docs/hipaa-accounting-of-disclosures.md) |
| Patient submits request for accounting of disclosures | Provide accounting (or written denial) | **≤ 60 days** (30-day extension allowed) | [hipaa-accounting-of-disclosures.md](New Policy Docs/hipaa-accounting-of-disclosures.md) |
| Patient submits records access request | Provide access / copies (or written denial) | **≤ 30 days** (30-day extension allowed) | [hipaa-right-to-access.md](New Policy Docs/hipaa-right-to-access.md) |
| Patient submits amendment request | Act on request (amend or deny in writing) | **≤ 60 days** (30-day extension allowed) | [hipaa-right-to-amend.md](New Policy Docs/hipaa-right-to-amend.md) |
| Security incident reported | Preliminary investigation by Security Officer | **≤ 24 hours of report** | [hipaa-security-incidents.md](New Policy Docs/hipaa-security-incidents.md) |
| New hire / contractor starts | HIPAA training and policy attestation before PHI access | Before access granted | [hipaa-safeguards.md](New Policy Docs/hipaa-safeguards.md), [hipaa-paper-documents.md](New Policy Docs/hipaa-paper-documents.md) |
| New vendor / Business Associate engaged | Execute signed BAA before PHI access | Before access granted | [hipaa-business-associate-agreement.md](New Policy Docs/hipaa-business-associate-agreement.md) |
| New vendor / Business Associate engaged | Complete ECH-style security assessment | Before contract signature | [ech-security-assessment.md](New Policy Docs/ech-security-assessment.md) |
| Employee termination or role change removing access | Deactivate password / disable account | **Immediately** | [hipaa-passwords.md](New Policy Docs/hipaa-passwords.md) |
| Employee termination or role change removing access | Terminate remote access; recover Company hardware | **Immediately** | [hipaa-remote-access.md](New Policy Docs/hipaa-remote-access.md) |
| Employee termination | Deactivate and archive encryption keys | **Immediately** on HR notice | [hipaa-encryption.md](New Policy Docs/hipaa-encryption.md) |
| Marketing communication uses PHI in a non-routine way | Privacy Officer reviews before send | Before communication | [hipaa-marketing.md](New Policy Docs/hipaa-marketing.md) |
| New software / system in design phase | Apply SDLC controls (security review, threat model, sign-off) | Before deployment | [sdlc-and-asset-lifecycle.md](New Policy Docs/sdlc-and-asset-lifecycle.md) |

---

## §3 — Responsibility Matrix

Roles: **PrO** = Privacy Officer · **SO** = Security Officer · **CTO** · **CEO** · **PM** = Practice Manager.

Codes: **R** = Responsible (does the work) · **A** = Accountable (owns the outcome, signs off) · **C** = Consulted · **I** = Informed.

| Policy / Area | PrO | SO | CTO | CEO | PM |
|---|---|---|---|---|---|
| Information Security Framework | C | A/R | C | I | I |
| Privacy Policy (patient-facing) | A/R | C | I | I | C |
| SDLC & Asset Lifecycle | I | C | A/R | I | — |
| Accounting of Disclosures | A/R | I | — | I | C |
| Breach Notification | A/R | R | C | I | C |
| Business Associate Agreements | A/R | C | C | I | I |
| Contingency Planning | I | A/R | R | I | C |
| De-Identifying PHI | A/R | C | C | I | — |
| Definitions | A/R | I | I | I | I |
| Encryption | I | A/R | R | I | — |
| Marketing & PHI | A/R | C | I | I | C |
| Minimum Necessary Rule | A/R | C | C | I | C |
| Paper Document Management | C | A/R | — | I | R |
| Password Management | I | A/R | R | I | C |
| PHI Use & Disclosure | A/R | C | C | I | C |
| Remote Access | I | A/R | R | I | C |
| Right to Access Records | A/R | I | C | I | C |
| Right to Amend Records | A/R | I | — | I | C |
| Risk Management | C | A/R | C | I | I |
| Safeguards | C | A/R | C | I | C |
| Security Incident Management | C | A/R | R | I | C |
| Workstation Use | I | A/R | R | I | C |
| Platform & Access Matrix | I | A/R | C | I | C |
| ECH Security Assessment (vendor evals) | C | A/R | C | I | — |
| **Annual report to CEO** | R | R | C | A | I |

### Signature & sign-off

At the end of each annual review cycle, both officers should sign off:

| Role | Name | Date | Signature |
|---|---|---|---|
| Chief Privacy Officer | _______________ | _______________ | _______________ |
| Chief Security Officer | _______________ | _______________ | _______________ |
| Chief Executive Officer | _______________ | _______________ | _______________ |

---

## Notes on the migration

- This folder (`New Policy Docs/`) is now the canonical source for Millie policies. Edit the Markdown files directly and let `git` track changes.
- The original `Policy Docs/` folder is preserved as a historical record. Older dated versions of policies (e.g., the May 1 versions superseded by May 7 / May 13 / May 18 / May 23) were not migrated — only the latest of each was carried forward.
- Templates (Insurance Authorization, BAA template) and the March 2025 training deck were intentionally not migrated — they are forms / training material, not policy text.
- The platform-and-access matrix and ECH security assessment were converted from `.xlsx` and contain wide tables with `NaN` placeholders for empty cells. The original spreadsheets in `Policy Docs/` remain the easier-to-edit source for those two; treat the Markdown versions as read-only snapshots.
- **Next step (deferred):** Several policies overlap heavily (e.g., Encryption + Password + Remote Access + Workstation Use all describe technical safeguards). A follow-up task will merge related policies into fewer thematic documents.
