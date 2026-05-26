---
title: "Millie Policies & Compliance"
last_reviewed: 2026-05-24
owner: "Privacy Officer + Security Officer (joint)"
---

# Millie Policies & Compliance

This repository is the source of truth for Millie's HIPAA and information security policies.

- **`New Policy Docs/`** — current canonical policies in Markdown. Edit these. 10 thematic policies + 3 reference files + 1 TODO + 1 `forms/` subfolder.
- **`New Policy Docs/_archive/`** — the 20 single-topic policy files from the May 2026 consolidation. Historical reference only; don't edit.
- **`policy_docs_word/`** — Word (.docx) renderings of every active policy + this README, generated from the Markdown sources. **For execs / non-engineering reviewers** — open directly in Word, or drag the folder into Google Drive and each file auto-converts to a native Google Doc. Regenerate after editing any policy with `./scripts/build-word-docs.sh`. Do NOT edit these directly — your changes will be overwritten on the next rebuild.
- **`scripts/build-word-docs.sh`** — re-runnable converter (Markdown → .docx via pandoc). Installs pandoc on first run if missing.
- **`Policy Docs/`** — original `.docx` / `.pdf` / `.xlsx` source files from the pre-Markdown era. Don't edit.
- **`ECH Security Assessment Questions - Questions.csv`** — third-party vendor questionnaire Millie completes (AWS / ISD / OWASP / PCI / SIG Lite / Insurance / Security Audits).
- **`CONSOLIDATION-PROPOSAL.md`** + **`POLICY-VS-QUESTIONNAIRE-MAPPING.md`** — working documents that drove the consolidation; useful for understanding why files are structured as they are.
- **`TODO.md`** — outstanding compliance action items surfaced by the ECH assessment.
- **This README** — operating playbook: policy index, compliance calendar, and responsibility matrix. Reviewed by the **Privacy Officer** and **Security Officer** at the start of each quarter.

**How to use this document:**

1. **§1 Policy Index** — confirm every active policy is current. If a policy is out of date, open the file and update it.
2. **§2 Compliance Calendar** — work the recurring tasks for the current month/quarter/year. Tick off each row as it's done; if a task isn't done by its target date, escalate to the policy owner.
3. **§3 Responsibility Matrix** — when something happens (incident, audit, vendor change), use this table to find who is Responsible, Accountable, Consulted, and Informed.

Owner names are listed by **role** (Privacy Officer, Security Officer, CTO, CEO, Practice Manager). Fill in real names alongside each role the first time you use this document.

---

## §1 — Policy Index

10 thematic policies + 3 reference files. Active files live at the top level of `New Policy Docs/`; older single-topic files are in `New Policy Docs/_archive/` for historical reference.

| Policy | Purpose | Owner |
|---|---|---|
| [governance-and-risk-management.md](New%20Policy%20Docs/governance-and-risk-management.md) | Master security & data-governance framework, annual risk assessment, ERM, records retention, HR/sanctions anchor, assurance program. The landing policy. | Security Officer + Privacy Officer |
| [phi-use-and-disclosure.md](New%20Policy%20Docs/phi-use-and-disclosure.md) | Minimum Necessary Rule, permitted PHI uses & disclosures, de-identification (Safe Harbor), Limited Data Sets, Marketing & Patient Communications. | Privacy Officer |
| [patient-rights.md](New%20Policy%20Docs/patient-rights.md) | Patient rights to access (30-day), amendment (60-day), and accounting of disclosures (6-year window). | Privacy Officer |
| [technical-safeguards.md](New%20Policy%20Docs/technical-safeguards.md) | Access control, MFA, password storage, encryption (FIPS 140-2 / NIST SP 800-111), workstation use, remote access, device & media management, session/token, logging cadence. | Security Officer + CTO |
| [operational-safeguards.md](New%20Policy%20Docs/operational-safeguards.md) | Admin & physical safeguards (oral/fax/email/text/voicemail), paper documents, contingency planning, DR testing, pandemic plan, multi-vendor resiliency. | Security Officer |
| [incident-and-breach-response.md](New%20Policy%20Docs/incident-and-breach-response.md) | Security incident detection (24h Security Officer investigation), tamper-evident log, breach determination (48h internal report), patient/HHS notification (60-day rule). | Security Officer + Privacy Officer |
| [vendor-and-business-associates.md](New%20Policy%20Docs/vendor-and-business-associates.md) | Vendor risk management, BAA identification & execution, subcontractor/Nth-party flow-down, Cybersecurity Supply Chain Risk Management (C-SCRM). | Privacy Officer |
| [acceptable-use-and-byod.md](New%20Policy%20Docs/acceptable-use-and-byod.md) | Acceptable use, BYOD eligibility & registration, Mobile Device Management (MDM) enrollment, lost/stolen device protocol, offboarding wipe. | Security Officer |
| [network-and-cloud-security.md](New%20Policy%20Docs/network-and-cloud-security.md) | Network architecture (Aptible/AWS/Cloudflare), IAM & SSO posture, secrets management, VPC/subnet design, wireless, S3 posture, GuardDuty/Detection, IaC, AWS-specific IR. | Security Officer + CTO |
| [ai-and-ml-governance.md](New%20Policy%20Docs/ai-and-ml-governance.md) | AI tool approval & inventory, prohibited use of public LLMs with PHI, clinical AI validation, engineering AI guardrails, patient transparency. | Security Officer + CTO + Privacy Officer |
| [sdlc-and-asset-lifecycle.md](New%20Policy%20Docs/sdlc-and-asset-lifecycle.md) | Secure SDLC, change management, patch SLA (7d Critical / 30d High), code integrity, secure coding standards (OWASP ASVS). | CTO + Security Officer |
| [hipaa-definitions.md](New%20Policy%20Docs/hipaa-definitions.md) | Glossary of HIPAA terms (PHI, ePHI, Business Associate, Designated Record Set, etc.) referenced by all other policies. | Privacy Officer |
| [platform-and-access-matrix.md](New%20Policy%20Docs/platform-and-access-matrix.md) | Inventory of every platform / SaaS subscription, who has access, BAA status. The xlsx in `Policy Docs/` is the easier editable source. | Security Officer |

**Plus 1 TODO** — [PATIENT-NOTICE-TODO.md](New%20Policy%20Docs/PATIENT-NOTICE-TODO.md): a patient-facing Notice of Privacy Practices is missing from this repo and needs to be authored (45 CFR §164.520).

**Plus 1 `forms/` subfolder** — fillable templates extracted from the old breach notification policy: individual notification letter, media notification (≥500 residents), HHS breach report.

---

## §2 — HIPAA Compliance Calendar

Each row: **Task · Source policy · Owner · Notes / target window.** Use this as a checklist.

### Annual

| Task | Source | Owner |
|---|---|---|
| Conduct full HIPAA security risk assessment; document threats, vulnerabilities, likelihood, impact; produce mitigation plan; present to Risk Review Committee (and Board if material). | [governance-and-risk-management.md](New%20Policy%20Docs/governance-and-risk-management.md) §4 | Security Officer |
| Review and refresh every policy in `New Policy Docs/`; update `last_reviewed:` frontmatter; re-sign. | All policies | Privacy Officer + Security Officer |
| Workforce HIPAA training refresh for all personnel. | [governance-and-risk-management.md](New%20Policy%20Docs/governance-and-risk-management.md) §IV | Privacy Officer |
| Prepare annual privacy & security report and submit to the CEO. | [incident-and-breach-response.md](New%20Policy%20Docs/incident-and-breach-response.md) | Security Officer + Privacy Officer |
| Test the contingency plan end-to-end (failover, restoration, emergency operations) and document results. | [operational-safeguards.md](New%20Policy%20Docs/operational-safeguards.md) §4 | Security Officer |
| Review every active Business Associate Agreement: vendor still in scope, renewal date current, subcontractor list accurate. | [vendor-and-business-associates.md](New%20Policy%20Docs/vendor-and-business-associates.md) | Privacy Officer |
| Refresh the platform & access matrix end-to-end: every listed app still in use, every role's access still correct, every BAA-required vendor still has one signed. | [platform-and-access-matrix.md](New%20Policy%20Docs/platform-and-access-matrix.md) | Security Officer |
| External penetration test or equivalent assurance activity. | [governance-and-risk-management.md](New%20Policy%20Docs/governance-and-risk-management.md) §8 Assurance | Security Officer |
| Deeper AI inventory review including bias / fairness assessment for clinical AI. | [ai-and-ml-governance.md](New%20Policy%20Docs/ai-and-ml-governance.md) §3(e) | Security Officer + clinical lead |

### Quarterly

| Task | Source | Owner |
|---|---|---|
| Review backup procedure documentation and update if procedures or vendors have changed. | [operational-safeguards.md](New%20Policy%20Docs/operational-safeguards.md) §4 | Security Officer |
| User access review: walk the platform matrix, confirm every account is still needed; revoke stale access. | [governance-and-risk-management.md](New%20Policy%20Docs/governance-and-risk-management.md), [platform-and-access-matrix.md](New%20Policy%20Docs/platform-and-access-matrix.md) | Security Officer |
| Vulnerability scan / patch review across infrastructure and endpoints. | [sdlc-and-asset-lifecycle.md](New%20Policy%20Docs/sdlc-and-asset-lifecycle.md) §6.3 | Security Officer + CTO |
| Tabletop drill of an incident-response scenario (e.g., ransomware, lost laptop, phishing). | [incident-and-breach-response.md](New%20Policy%20Docs/incident-and-breach-response.md) | Security Officer |
| AI tool inventory review — confirm every AI tool listed in platform matrix is still in use; retire unused tools. | [ai-and-ml-governance.md](New%20Policy%20Docs/ai-and-ml-governance.md) §3(e) | Security Officer + CTO |

### Monthly

| Task | Source | Owner |
|---|---|---|
| Spot-check audit logs (Aptible, AWS CloudWatch, admin console) for anomalies. | [technical-safeguards.md](New%20Policy%20Docs/technical-safeguards.md) §7 Logging | Security Officer |
| Verify a recent backup is restorable (test restore in non-production environment). | [operational-safeguards.md](New%20Policy%20Docs/operational-safeguards.md) §4 | Security Officer + CTO |
| Confirm no terminated employees still have active credentials in any system on the platform matrix. | [technical-safeguards.md](New%20Policy%20Docs/technical-safeguards.md) §6 Termination Checklist | Security Officer |

### Event-driven

These are deadlines triggered by a specific event — not on a schedule, but missing them is a compliance failure.

| Trigger | Action | Deadline | Source |
|---|---|---|---|
| Personnel becomes aware of a suspected breach | Report to Privacy Officer | **≤ 48 hours** | [incident-and-breach-response.md](New%20Policy%20Docs/incident-and-breach-response.md) |
| Confirmed breach of unsecured PHI | Notify affected individuals and applicable agencies | **≤ 60 days from Date of Discovery** | [incident-and-breach-response.md](New%20Policy%20Docs/incident-and-breach-response.md) |
| Patient submits request for accounting of disclosures | Transmit request to Privacy Officer | **≤ 24 hours of receipt** | [patient-rights.md](New%20Policy%20Docs/patient-rights.md) |
| Patient submits request for accounting of disclosures | Provide accounting (or written denial) | **≤ 60 days** (30-day extension allowed) | [patient-rights.md](New%20Policy%20Docs/patient-rights.md) |
| Patient submits records access request | Provide access / copies (or written denial) | **≤ 30 days** (30-day extension allowed) | [patient-rights.md](New%20Policy%20Docs/patient-rights.md) |
| Patient submits amendment request | Act on request (amend or deny in writing) | **≤ 60 days** (30-day extension allowed) | [patient-rights.md](New%20Policy%20Docs/patient-rights.md) |
| Security incident reported | Preliminary investigation by Security Officer | **≤ 24 hours of report** | [incident-and-breach-response.md](New%20Policy%20Docs/incident-and-breach-response.md) |
| New hire / contractor starts | HIPAA training and policy attestation before PHI access | Before access granted | [governance-and-risk-management.md](New%20Policy%20Docs/governance-and-risk-management.md) §IV, [acceptable-use-and-byod.md](New%20Policy%20Docs/acceptable-use-and-byod.md) |
| New device touches PHI | MDM enrollment + signed BYOD agreement | Before access granted | [acceptable-use-and-byod.md](New%20Policy%20Docs/acceptable-use-and-byod.md) |
| New vendor / Business Associate engaged | Execute signed BAA before PHI access | Before access granted | [vendor-and-business-associates.md](New%20Policy%20Docs/vendor-and-business-associates.md) |
| New vendor / Business Associate engaged | Complete ECH-style security assessment | Before contract signature | [`ECH Security Assessment Questions - Questions.csv`](ECH%20Security%20Assessment%20Questions%20-%20Questions.csv) |
| New AI tool proposed | Security + clinical/ops approval; add to platform matrix | Before any Company-data use | [ai-and-ml-governance.md](New%20Policy%20Docs/ai-and-ml-governance.md) §3(a) |
| Employee termination / role change removing access | Deactivate password, terminate remote access, archive encryption keys, recover Company hardware, MDM-wipe BYOD | **Immediately** | [technical-safeguards.md](New%20Policy%20Docs/technical-safeguards.md) §6 |
| Lost / stolen device | Report to Security Officer; authorize remote wipe; breach assessment | **≤ 24 hours** | [acceptable-use-and-byod.md](New%20Policy%20Docs/acceptable-use-and-byod.md) §5 |
| Material change to production system | Change request, security review, deployment plan, rollback plan, approval | Before deploy | [sdlc-and-asset-lifecycle.md](New%20Policy%20Docs/sdlc-and-asset-lifecycle.md) §5 |
| Critical security patch (CVSS 9.0+ or KEV-listed) | Apply per patch SLA | **≤ 7 calendar days** | [sdlc-and-asset-lifecycle.md](New%20Policy%20Docs/sdlc-and-asset-lifecycle.md) §6.2 |

---

## §3 — Responsibility Matrix

Roles: **PrO** = Privacy Officer · **SO** = Security Officer · **CTO** · **CEO** · **PM** = Practice Manager.

Codes: **R** = Responsible (does the work) · **A** = Accountable (owns the outcome, signs off) · **C** = Consulted · **I** = Informed.

| Policy | PrO | SO | CTO | CEO | PM |
|---|---|---|---|---|---|
| [governance-and-risk-management.md](New%20Policy%20Docs/governance-and-risk-management.md) | C | A/R | C | I | I |
| [phi-use-and-disclosure.md](New%20Policy%20Docs/phi-use-and-disclosure.md) | A/R | C | C | I | C |
| [patient-rights.md](New%20Policy%20Docs/patient-rights.md) | A/R | I | — | I | C |
| [technical-safeguards.md](New%20Policy%20Docs/technical-safeguards.md) | I | A/R | R | I | — |
| [operational-safeguards.md](New%20Policy%20Docs/operational-safeguards.md) | C | A/R | C | I | R |
| [incident-and-breach-response.md](New%20Policy%20Docs/incident-and-breach-response.md) | A/R | A/R | R | I | C |
| [vendor-and-business-associates.md](New%20Policy%20Docs/vendor-and-business-associates.md) | A/R | C | C | I | I |
| [acceptable-use-and-byod.md](New%20Policy%20Docs/acceptable-use-and-byod.md) | C | A/R | C | I | C |
| [network-and-cloud-security.md](New%20Policy%20Docs/network-and-cloud-security.md) | I | A/R | A/R | I | — |
| [ai-and-ml-governance.md](New%20Policy%20Docs/ai-and-ml-governance.md) | C | A/R | A/R | I | C |
| [sdlc-and-asset-lifecycle.md](New%20Policy%20Docs/sdlc-and-asset-lifecycle.md) | I | C | A/R | I | — |
| [platform-and-access-matrix.md](New%20Policy%20Docs/platform-and-access-matrix.md) | I | A/R | C | I | C |
| **Annual report to CEO** | R | R | C | A | I |
| **ECH submission (vendor security questionnaire response)** | C | A/R | R | I | — |

### Signature & sign-off

At the end of each annual review cycle, both officers should sign off:

| Role | Name | Date | Signature |
|---|---|---|---|
| Privacy Officer | _______________ | _______________ | _______________ |
| Security Officer | _______________ | _______________ | _______________ |
| Chief Executive Officer | _______________ | _______________ | _______________ |

---

## Migration notes & timeline

**May 24, 2026** — Consolidated 24 single-topic files into 10 thematic files. The 20 archived originals are in [`New Policy Docs/_archive/`](New%20Policy%20Docs/_archive/) for historical reference. Three originals stayed at the top level: `hipaa-definitions.md` (glossary), `platform-and-access-matrix.md` (reference table), `sdlc-and-asset-lifecycle.md` (expanded with change management, patch SLA, and secure coding rather than merged).

**May 24, 2026** — Integrated the Millie Clinic COVID Policy into [operational-safeguards.md §A.9](New%20Policy%20Docs/operational-safeguards.md) as the live implementation example of the generic pandemic plan in Appendix A. The COVID source had a "GUIDANCE FOR STAFF: To Do…" placeholder that was never filled in — that gap is logged in [TODO.md](TODO.md).

### Key findings from the May 2026 work

- **`privacy-policy.md` was a misnamed bundle**, not a patient-facing Notice of Privacy Practices. Substantive content (including the Device & Media Management Policy IT-004 that existed nowhere else) was rescued into [technical-safeguards.md](New%20Policy%20Docs/technical-safeguards.md). A real NPP still needs to be authored — see [PATIENT-NOTICE-TODO.md](New%20Policy%20Docs/PATIENT-NOTICE-TODO.md).
- **The ECH Security Assessment surfaced critical gaps**: MDM/BYOD, OWASP A02/A06/A07 remediations, pandemic plan, multi-vendor resiliency. Outstanding action items live in [TODO.md](TODO.md). Three new policy areas were authored during consolidation to close compliance gaps: Acceptable Use & BYOD, Network & Cloud Security, AI & ML Governance.
- **`Policy Docs/AWS and Aptible Security Incident Management Policy.docx`** was added late in the process and was not integrated during the May 2026 pass. Logged in [TODO.md](TODO.md) for the next consolidation cycle.

### Working documents

- [POLICY-VS-QUESTIONNAIRE-MAPPING.md](POLICY-VS-QUESTIONNAIRE-MAPPING.md) — **the current authoritative coverage matrix.** For each of the 182 ECH/SIG/OWASP/AWS questionnaire rows, lists which policy file and section covers it, the coverage rating, and any remaining gaps. Refresh whenever a policy changes or a new questionnaire arrives.
- [CONSOLIDATION-PROPOSAL.md](CONSOLIDATION-PROPOSAL.md) — historical rationale for the 24→10 consolidation. Status: EXECUTED. Keep for the "why," but day-to-day questions go to the mapping doc above.
- [TODO.md](TODO.md) — open compliance action items.

These working documents can be deleted (or moved to `_archive/`) once the first ECH submission is complete and no longer needs the supporting analysis.
