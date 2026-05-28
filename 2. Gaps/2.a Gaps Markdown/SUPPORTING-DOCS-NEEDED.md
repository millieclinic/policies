# Supporting Docs You Need to Create or Maintain

## What this is

This is the **evidence checklist**. The policies in `Current Policies (… Generated)/` describe what Millie *does*; this document tracks the actual records, logs, attestations, and reports the policies require you to keep on file.

**You manage policy-review cadence yourself** — nothing in here says "review your Risk Management Policy yearly." Everything here is a **document or record you need to produce or refresh**, driven by a specific clause in a specific policy.

**Sources cross-referenced:**

- `Current Policies (05-28-2026 Generated)/3.a Final Markdown/` — every active policy.
- `Supporting Sources/` — three evidence files already on file (annual risk letter, May 2026 DR review, platform matrix).
- ECH coverage matrix + UCSF coverage matrix in this folder — flagged the document-evidence gaps.

---

## ✅ What you already have on file (`Supporting Sources/`)

| File | Covers requirement from | Next refresh |
|---|---|---|
| `Copy of Annual Risk Letter _ Mitigations from 03q HIPAA - Risk Management Policy.docx` | `01c. Risk Management Policy` (annual risk assessment) | Annually — refresh before the date drifts past 12 months from the letter date. |
| `Disaster Recovery Review - May 2026.xlsx` | `04a. Contingency Planning Policy` (annual DR exercise + quarterly backup review) | Annually for full DR exercise; quarterly for the backup-procedure review portion. |
| `Millie Matrix of Platforms, Software Subscriptions, and Access (1).xlsx` | `06a. Business Associate Agreement Policy` (vendor inventory + BAA status) and `01a. Information Security Framework` (access matrix) | Quarterly user-access review; annual full refresh. |

---

## 🔴 Missing — high priority (assessor / auditor will flag)

These are documents an ECH or UCSF assessor will almost certainly ask for. Create as soon as bandwidth allows.

| # | Document to create | Required by | What it should contain | Why it's high priority |
|---|---|---|---|---|
| 1 | **Workforce training completion roster** (annual) | `01d. Safeguards Policy` §IV "Training & Awareness"; UCSF Q16 | Per-person record of: training assigned date, completion date, acknowledgement signature, score on knowledge check (if any), refresh date. Export from whatever LMS / Google Form / Gusto-module you use. | Both ECH and UCSF explicitly ask for evidence that training completion is tracked and measured. |
| 2 | **Tamper-evident incident log** | `05a. Incident & Breach Response` §III(c) (J.14 from ECH); UCSF Q33/Q37 | Restricted-access log of every security incident: date, reporter, classification (event vs incident vs breach), investigation steps, owners, root cause, remediation, closure date. Stored in a write-once or version-controlled system (e.g., locked Google Sheet with audit history, or a ticketing system). Retain ≥6 years. | ECH SIG J.14 and HIPAA documentation requirements. |
| 3 | **Annual privacy & security report to the CEO** | `05a. Incident & Breach Response` §I "Annual Report" | Once per year, the Chief Security Officer + Chief Privacy Officer compile: incidents this year, breach assessments, training completion %, risk-assessment results, open remediation items, and recommendations. Delivered in writing to the CEO. | Internal accountability requirement that auditors look for to confirm board/exec engagement. |
| 4 | **Critical Systems & Recovery Priority Matrix** | `04a. Contingency Planning Policy` "IT System Inventory" + UCSF Q3 | Table: every critical system × data sensitivity × business criticality × owner × RTO / RPO × dependency chain × restart order. User-stated software priority is: backend → mobile app → admin/frontend. Hardware/devices side: Tenisi. | UCSF explicitly asks; ECH expects via SIG K.2/K.5. |
| 5 | **Risk register / threat register** (refresh annually with the risk letter) | `01c. Risk Management Policy` §III; UCSF Q9 | Per-threat row: threat (internal/external, by category), vulnerability, controls in place, likelihood, impact, residual risk, owner, status, due date. Can be a tab in the Annual Risk Letter workbook. | UCSF Q9 specifically requires this. The Annual Risk Letter covers the assessment narrative; a threat-register tab makes the threats explicit. |
| 6 | **BYOD enrollment register + signed acceptance forms** | `03a. Technical Safeguards` §IV (Workstation Use — BYOD addition); ECH SIG M.1.3/M.1.5/M.1.6 | One row per personal device touching PHI: user, device make/model/OS, IMEI/serial, MDM enrollment date, signature on the BYOD acceptance form. Lives wherever MDM dashboard exports go. | ECH flagged this with `Remediate=Yes`. Three rows of the ECH matrix close when this exists. |
| 7 | **Vendor Risk Management Program SOP + vendor security questionnaire** | `06a. Business Associate Agreement Policy`; UCSF Q17 | Document: how new vendors are screened (security questionnaire — can be a short version of the ECH questionnaire pointed at vendors), risk-tiering criteria, BAA review workflow, periodic reassessment cadence. Plus an evidence folder per vendor (BAA, security questionnaire response, SOC2/HITRUST report if any). | Both ECH SIG S and UCSF Q17 ask for this. |
| 8 | **Sanctions log** | `01d. Safeguards Policy` / HIPAA §164.530(e) (sanctions clause); referenced from every consolidated policy's §V Sanctions section | Per-incident row: date, personnel involved (anonymized if needed), policy violated, sanction applied, follow-up. Even empty ("no sanctions issued this period") satisfies the audit; absence of any tracking is the gap. | Auditors look specifically for evidence the sanctions clause is operationalized. |
| 9 | **Cyber-liability insurance certificate** (current period) | `04a. Contingency Planning Policy` §III "Insurance"; ECH Insurance row 181 | A scanned / PDF copy of the current policy declarations page. Updated each renewal. | ECH explicitly asks for this as an attachment, not as policy text. |
| 10 | **Pentest report** or written "no pentest currently on file" decision memo | `01a. Information Security Framework` §7 / `06b. SDLC & Asset Lifecycle` §III(b); ECH Security Audits rows 182–183 | Most recent third-party penetration test report — OR a written decision documented in the Risk Register saying "no pentest commissioned this cycle; accepted risk; rationale". | ECH asks for this; either commission a test or document the acceptance. |
| 11 | **Patient PHI request log** | `02b. Patient Rights — Access, Amendment & Accounting of Disclosures` | Per request: date received, requester, request type (access / amendment / accounting), response date, outcome (granted / denied with reason), 6-year retention. | HIPAA requires evidence of compliance with the 30-day / 60-day response rules. |
| 12 | **HR: Background check & exit interview attestation** | UCSF Q29 (referenced by `01d. Safeguards Policy` workforce trust model) | One-paragraph HR-owned attestation: background checks are performed on every workforce member at hire (scope: criminal + reference); exit interviews include HIPAA confidentiality reminder. Plus a check-the-box exit checklist. | UCSF Q29 explicitly asks. |

---

## 🟡 Missing — standard priority (create when there's bandwidth)

These will strengthen a security review but aren't blockers if explained verbally.

| # | Document to create | Required by | What it should contain |
|---|---|---|---|
| 13 | **Access Provisioning & Deprovisioning SOP** | `03a. Technical Safeguards` §II/§III; UCSF Q30 | Cross-system process: request → approval → role mapping → least privilege → provisioning → periodic review → termination/offboarding SLAs → physical access. |
| 14 | **Internal/External Data Flow Map and Data Inventory** | UCSF Q32 | System inventory × PHI categories × source/destination × transfers × vendors × storage location × encryption × owner × retention × BAA status. Diagram + table. |
| 15 | **Network Security Monitoring / IDS-IPS Statement** | `network-and-cloud-security.md` (now in `_old_attempt/`; reflect in `01a. Framework`); UCSF Q35 | What's monitored (GuardDuty, CloudTrail, NinjaOne agent, etc.), Tenisi alerting workflow, review cadence, escalation, sample alert evidence. |
| 16 | **Data Leak Monitoring / DLP Statement** | UCSF Q22 | Per-platform audit logging coverage (Fivetran, Databricks, Hex, Aptible, AWS CloudTrail/CloudWatch), AWS User Notifications, review cadence, escalation. Can reuse the UCSF Q22 draft answer as the starting paragraph. |
| 17 | **Network Segmentation / Architecture Statement** | UCSF Q15 | Cloud-first; no physical server infrastructure; LAN separate from production; wireless split into guest + production. Include a simple diagram. |
| 18 | **Secure Configuration Baseline Standard** | UCSF Q23 | Endpoint / server / cloud / network baseline controls (NinjaOne policy, ConnectSecure agent, etc.), owner, review cadence, exceptions. |
| 19 | **Per-site Physical Security Monitoring Statement** | UCSF Q36 | Per clinic location: locks, cameras (or "none"), badge readers (or "none"), visitor logs, restricted areas, responsible owner, exceptions. |
| 20 | **Asset Lifecycle SOP + Tenisi hardware inventory export** | UCSF Q21 / `06b. SDLC` | Tenisi-managed device inventory (make/model/serial/user/status), acquisition/movement/transfer/disposal process, owner. |
| 21 | **Admin RBAC role matrix** (screenshot or export) | UCSF Q14 | Per-role × per-system permission grid, exported from admin dashboard. Supports the "Yes, RBAC enforced" answer with visual evidence. |
| 22 | **Pandemic plan activation playbook** | `04a. Contingency Planning Policy` §III(h) (pandemic addition) | Step-by-step activation steps for a future pandemic / infectious-disease event (the COVID Policy is the current implementation; this is the generic playbook for the next event). |
| 23 | **Multi-vendor risk acceptance memo** | `04a. Contingency Planning Policy` §III(h) (multi-vendor addition) | One-page memo: Aptible / AWS / Cloudflare / Google Workspace concentration documented; CSO + CEO sign-off; review cadence; exit considerations per vendor. |
| 24 | **Change Management log template** (and ongoing log) | `06b. SDLC & Asset Lifecycle Policy` §III(c); ECH SIG G.2; UCSF Q25 | Per-change row: change description, risk class (standard / normal / emergency), approver, testing performed, deployment date, rollback plan, evidence link (PR + Aptible deploy URL). |
| 25 | **Patch SLA compliance log** | `06b. SDLC & Asset Lifecycle Policy` §III(d) | Per CVE / dependency advisory: severity, advisory date, remediation deadline (per SLA: Critical=7d, High=30d, Medium=90d, Low=next cycle), remediation date, evidence link. |

---

## 🟢 Optional / nice-to-have

| # | Document | Why it's nice |
|---|---|---|
| 26 | Security & Privacy Roles / RACI addendum | UCSF Q5 — would strengthen the answer that role responsibilities are documented in writing. |
| 27 | Incident Severity & Escalation Matrix | UCSF Q34 — would make criticality tiers explicit in incident response. |
| 28 | Disposal Certificate folder | `04b. Paper Document Management Policy` requires vendor certificates of destruction for shredding services. Keep one per shred cycle. |

---

## 📋 How to use this list

1. **For each row marked 🔴 high-priority and not already in `Supporting Sources/`**: create the document. Doesn't need to be long — a one-page SOP or a tracked spreadsheet is often enough. Save to `Supporting Sources/` so the next gap-analysis run sees it.
2. **When you create one**, the next pass through this checklist should move it from 🔴/🟡 to the ✅ table.
3. **You don't need to do these all at once**. Prioritize what an actual assessor is likely to ask for next (ECH or UCSF).
4. **Refresh cadence**: the three docs in `Supporting Sources/` today have annual or quarterly refresh expectations. Put a calendar reminder.

---

*Generated by walking every active policy in `Current Policies (… Generated)/3.a Final Markdown/` and cross-referencing the `Supporting Sources/` folder + the ECH and UCSF coverage matrices in this folder. Re-run the analysis after any policy change or new evidence file lands in `Supporting Sources/`.*
