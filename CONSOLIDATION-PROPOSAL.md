---
title: "Policy Consolidation Proposal"
last_reviewed: 2026-05-24
owner: "Privacy Officer + Security Officer (joint)"
status: "DRAFT — pending approval"
---

# Policy Consolidation Proposal

Reducing the 24 Markdown files in `New Policy Docs/` to a recommended **6 thematic policy documents** (plus 2 read-only reference matrices and 1 patient-facing notice that still needs to be written from scratch).

> **Important framing finding — read this first.**
> The file currently called [`privacy-policy.md`](New Policy Docs/privacy-policy.md) is **not** a patient-facing privacy notice (despite what the README claims on line 32). It is a concatenated dump of 9 HIPAA policies (Accounting of Disclosures, Breach Notification, **Device Management & Media Management/Inventory**, Minimum Necessary, Paper Documents, Passwords, Remote Access, Safeguards, Workstation Use), all mis-stamped under one "Accounting of Disclosures Policy" header (line 10) and inheriting Policy # L-003. Every section is duplicated word-for-word from the individual files — **except** for the "Device Management and Media Management/Inventory Policy" (Policy # IT-004) at lines 564–609. That policy text **does not exist as a standalone file** in `New Policy Docs/`. The README also does not list it. Either the standalone file was lost in the docx migration, or it was deliberately rolled up, but it is currently only preserved inside `privacy-policy.md`. Any consolidation plan **must rescue the Device & Media Management content** before deleting `privacy-policy.md`. See §1 and §6 below.

---

## §1 — Duplication map

Each entry: the snippet (quoted or paraphrased) followed by the files in which it appears. All file paths are relative to `New Policy Docs/`.

### 1.1 The standard Scope boilerplate (verbatim, 19 files)

Quote:
> "This Policy applies to all facilities and locations owned, operated, or managed by Millie, Inc.("Company"), and all Companypersonnel. For purposes of this Policy, the term "personnel" includes all licensed professionals and staff who perform services on behalf of Company."

(Note the missing space between "Company" and "personnel" — a docx→md migration artifact present in nearly every file.)

Appears in:
- `hipaa-accounting-of-disclosures.md` (§1)
- `hipaa-breach-notification.md` (§1)
- `hipaa-business-associate-agreement.md` (§1)
- `hipaa-contingency-planning.md` (§1)
- `hipaa-de-identifying-phi.md` (§1)
- `hipaa-definitions.md` (§1)
- `hipaa-encryption.md` (§1)
- `hipaa-marketing.md` (§1)
- `hipaa-minimum-necessary.md` (§1)
- `hipaa-paper-documents.md` (§1)
- `hipaa-passwords.md` (§1)
- `hipaa-phi-use-and-disclosure.md` (§1)
- `hipaa-remote-access.md` (§1)
- `hipaa-right-to-access.md` (§1)
- `hipaa-right-to-amend.md` (§1)
- `hipaa-risk-management.md` (§1)
- `hipaa-safeguards.md` (§1)
- `hipaa-security-incidents.md` (§1)
- `hipaa-workstation-use.md` (§1)
- `privacy-policy.md` (repeats it 9 times, once per embedded policy)

The SDLC policy uses a slightly broader scope statement covering "Company information systems, software platforms, cloud services, endpoints, mobile devices, and hardware assets that are used to create, receive, maintain, or transmit Company data or Protected Health Information ('PHI')" — it is the only file with a non-standard scope.

### 1.2 The metadata table header (verbatim, 19 files)

Every HIPAA-numbered policy opens with the same 2x2 markdown table:
```
| **Title**: <name> | **Policy #**: <code> |
| **Effective Date**: <date> | **Last Revised**: <date> |
```
Combined with the new YAML frontmatter (`title:`, `last_reviewed:`, `owner:`) at the top of every file, **the document title is repeated 3 times** in each file (frontmatter title, table title, and often a markdown `#` header).

### 1.3 Training requirement (4+ files, varying wording)

- `hipaa-safeguards.md` §III(c)(iv): *"All personnel shall receive training at the time of employment or engagement, with annual updates thereafter or as otherwise needed, regarding Company's HIPAA compliance program and the safeguards discussed in this Policy."*
- `hipaa-contingency-planning.md` §III(a)(i): *"All personnel shall receive regular training regarding this Policy."*
- `hipaa-paper-documents.md` §III(a) bullet: *"Prior to gaining access to Protected Documents, all personnel must receive training in the use and disclosure of PHI, and Company must obtain evidence of such training."*
- `hipaa-encryption.md` §III(a)(iii): *"The Chief Security Officer will be responsible for training all applicable personnel in the use of encryption…"*
- `README.md` Annual section: *"Workforce HIPAA training refresh for all personnel…"*

### 1.4 Disciplinary action sentence (only explicit in 1 file, implied in many)

The only file that contains an explicit "violations will result in disciplinary action" clause is `hipaa-risk-management.md` §II(d):
> *"Any personnel member who violates this Policy will be subject to disciplinary action based on the severity of the violation."*

This is a notable gap — most HIPAA policies should contain a sanctions/discipline clause for 45 C.F.R. § 164.530(e) compliance. The Breach Notification policy alludes to it (§IV(g)(iii) "Sanctions … the Company Internal Investigations & Corrective Action Policy will be followed"), but that referenced policy is not in the repo.

### 1.5 References to a Chief Privacy Officer / Chief Security Officer (nearly every file)

- "Chief Privacy Officer" appears in: `hipaa-accounting-of-disclosures.md`, `hipaa-breach-notification.md`, `hipaa-business-associate-agreement.md`, `hipaa-de-identifying-phi.md`, `hipaa-marketing.md`, `hipaa-paper-documents.md`, `hipaa-phi-use-and-disclosure.md`, `hipaa-right-to-access.md`, `hipaa-right-to-amend.md`, `hipaa-risk-management.md`, `hipaa-safeguards.md`, `hipaa-security-incidents.md`, `hipaa-remote-access.md`, `hipaa-breach-notification.md`, `privacy-policy.md`.
- "Chief Security Officer" appears in: `hipaa-contingency-planning.md`, `hipaa-encryption.md`, `hipaa-passwords.md`, `hipaa-remote-access.md`, `hipaa-risk-management.md`, `hipaa-safeguards.md`, `hipaa-security-incidents.md`, `hipaa-workstation-use.md`, `sdlc-and-asset-lifecycle.md`, `information-security-framework.md`, `privacy-policy.md`.
- "Risk Review Committee" / "Risk Committee": `hipaa-risk-management.md` (multiple), `README.md`. The term **"Risk Management Team"** is also defined in `hipaa-definitions.md` §II(r) — these may or may not refer to the same body and should be reconciled.

### 1.6 Definitions repeated across files

The same defined terms appear in multiple files (sometimes with subtle wording differences):

| Term | Defined in |
|---|---|
| `PHI` / `Protected Health Information` | `hipaa-definitions.md`, used by all 20+ HIPAA files; effectively re-defined in `information-security-framework.md` §1 |
| `ePHI` | `hipaa-encryption.md` §II, `hipaa-risk-management.md` §II, `information-security-framework.md` §1 |
| `Business Associate` | `hipaa-definitions.md`, `hipaa-business-associate-agreement.md` (uses but does not re-define) |
| `Breach` | `hipaa-definitions.md`, `hipaa-breach-notification.md` (uses), `privacy-policy.md` |
| `Disclosure` | `hipaa-definitions.md` (implied), `hipaa-breach-notification.md` §II(b), `privacy-policy.md` |
| `Use` | `hipaa-breach-notification.md` §II(d), `privacy-policy.md` |
| `Unsecured PHI` | `hipaa-breach-notification.md` §II(c), `privacy-policy.md` |
| `Designated Record Set` | `hipaa-definitions.md`, `hipaa-right-to-access.md` §II, `hipaa-right-to-amend.md` §II |
| `Health Care Operations` | `hipaa-definitions.md`, `hipaa-marketing.md`, `hipaa-de-identifying-phi.md`, `hipaa-phi-use-and-disclosure.md` |
| `Treatment` | `hipaa-definitions.md`, `hipaa-marketing.md`, `hipaa-minimum-necessary.md`, `hipaa-phi-use-and-disclosure.md` |
| `Workstation` | `hipaa-definitions.md`, `hipaa-workstation-use.md` (implicit), `hipaa-safeguards.md` |
| `IT System` | `hipaa-definitions.md`, `hipaa-remote-access.md` (~22 references), `hipaa-contingency-planning.md`, `hipaa-encryption.md`, `hipaa-security-incidents.md`, `hipaa-workstation-use.md`, `hipaa-risk-management.md` |
| `Marketing` | `hipaa-definitions.md` (NOT defined), `hipaa-marketing.md` §II(a) (full def) |
| `Financial Remuneration` | `hipaa-marketing.md` §II(b) only |
| `Company Computer Network` | `hipaa-definitions.md`, `hipaa-passwords.md`, `hipaa-safeguards.md`, `privacy-policy.md` Device section |

### 1.7 NIST / FIPS encryption standard reference (3 files — and material drift)

- `hipaa-encryption.md` §III(c)(i) — covers **data in motion** only (FIPS 140-2, NIST SP 800-52, 800-77, 800-113).
- `privacy-policy.md` Device Management section (lines ~599–602) — covers **both data at rest** (NIST SP 800-111) **and data in motion** (same set as above).
- `information-security-framework.md` §5 — says "All PHI transmitted over open networks is encrypted. Databases hosted via Aptible are encrypted at rest." (no NIST citation).

**Critical:** the standalone Encryption policy is silent on data-at-rest standards. The only documented NIST 800-111 reference is inside `privacy-policy.md`. This is exactly the kind of content that must not be lost in consolidation.

### 1.8 The "Workstations / iPads / iPhones" device-list (4 files)

Nearly identical lists of which device types are in scope:
- `hipaa-workstation-use.md` §II(b)
- `hipaa-remote-access.md` §II(a)
- `hipaa-passwords.md` §III(b) ("Mobile Passcode Construction")
- `hipaa-safeguards.md` §III(b)(xi)

### 1.9 Password / access-control cross-references (5 files)

The phrase "must comply with the Company Password Management Policy" or equivalent:
- `hipaa-workstation-use.md` §III(c)(iii)
- `hipaa-remote-access.md` §III(b)(ii) — "See Workstation Use, Encryption, and Password Management policies."
- `hipaa-safeguards.md` §III(b)(x) bullet 3
- `hipaa-encryption.md` §III(a)(i) — "the same precautions in protecting encryption keys from disclosure as is required for passwords"
- `sdlc-and-asset-lifecycle.md` §III(b)

### 1.10 Termination → deactivate access (4 files, parallel timing)

- `hipaa-passwords.md` §III(d)(ii) — "immediately deactivated … upon … termination"
- `hipaa-remote-access.md` §III(d) — "immediately terminated … upon termination of employment"
- `hipaa-encryption.md` §III(b)(ii) — "immediately deactivate and archive encryption keys upon notification by Human Resources of the termination"
- `README.md` Event-driven section has 3 separate rows for the same trigger

### 1.11 Annual report to CEO (3 files)

- `hipaa-security-incidents.md` §III(e) ("Annual Report")
- `hipaa-risk-management.md` §II(c) (report to Risk Review Committee / Board)
- `README.md` Annual section + Responsibility Matrix "Annual report to CEO" row

### 1.12 BAA cross-references (5 files)

The requirement to execute a BAA before granting PHI access:
- `hipaa-business-associate-agreement.md` (the canonical source)
- `hipaa-paper-documents.md` §III(c)(iv) bullet 1 (for shredding vendors)
- `hipaa-marketing.md` §IV(b) note (for marketing vendors)
- `information-security-framework.md` §11
- `sdlc-and-asset-lifecycle.md` §III(a)
- `README.md` Event-driven section

### 1.13 Reference to "Information Blocking Compliance Policy" (broken)

- `hipaa-right-to-access.md` §III(a)(iv) and elsewhere references "Information Blocking Compliance Policy" and the term `Electronic Health Information` / `EHI` as if defined elsewhere.
- `hipaa-definitions.md` §II(j) defines `Information Blocking Rule` but not `EHI`.
- **No "Information Blocking Compliance Policy" exists in this repo** — this is a dangling reference that will need to be either resolved (write the policy) or rewritten (inline the relevant content) during consolidation.

### 1.14 Other dangling cross-references

- "Company Internal Investigations & Corrective Action Policy" — referenced in `hipaa-breach-notification.md` §IV(g)(i) and (iii). **Not in repo.**
- "Company Device Management and Media Management/Inventory Policy" — referenced in `hipaa-remote-access.md` §III(c) and `hipaa-safeguards.md` §III(a)(vii). **Only exists embedded in `privacy-policy.md` lines 564–609.**

---

## §2 — Overlap by topic

Six natural clusters emerge.

### Cluster A — Technical safeguards for endpoints (4 files + 1 buried file)

- `hipaa-encryption.md`
- `hipaa-passwords.md`
- `hipaa-remote-access.md`
- `hipaa-workstation-use.md`
- (Embedded) Device & Media Management policy inside `privacy-policy.md`

**Redundant:** all five describe how a user protects an endpoint that may touch PHI — they share the "workstation/iPad/iPhone" device list, the termination/deactivation procedure, mutual cross-references, and the same Chief Security Officer authority.

**Genuinely distinct:** Encryption is a control standard (FIPS 140-2, NIST SP 800-52/77/111/113, key management) — auditable as a separate artifact. Passwords cover specific construction rules (length, character classes, lockout). Remote Access covers VPN and off-network connectivity. Workstation Use covers the physical/screen-lock behavior. Device & Media covers inventory and disposal — the only place that specifies the NIST SP 800-111 *at-rest* encryption standard.

**Options:**
- *(a) Merge all 5 into one "Technical Safeguards" policy with subsections.* Pro: a single auditable artifact for the HIPAA Security Rule §164.310/§164.312 technical+physical safeguards. Pro: kills ~80% of the boilerplate. Con: a single ~30KB file; auditors who specifically ask for "the Encryption Policy" need a section anchor instead of a separate doc.
- *(b) Keep Encryption standalone (because OCR/HHS commonly request it by name) and merge the other four.* Pro: preserves audit-friendly file. Con: still leaves overlap between Encryption and Device & Media at-rest standard.
- *(c) Status quo.* Heaviest duplication, easiest to find any one rule.

**Tradeoff to note:** the existing `hipaa-safeguards.md` already partially does this — it has its own "Workstation Use" subsection that duplicates `hipaa-workstation-use.md`, its own "Access Controls" that points back to Passwords, its own "Remote Work Areas" that overlaps with Remote Access. Safeguards is the natural anchor for option (a) or (b).

### Cluster B — Administrative + physical safeguards (3 files)

- `hipaa-safeguards.md` (administrative + physical + some technical)
- `hipaa-paper-documents.md` (physical, paper-only)
- `hipaa-contingency-planning.md` (administrative, BCP/DR)

**Redundant:** `hipaa-safeguards.md` already contains a "Disposal" subsection (§III(a)(vi)) that overlaps with `hipaa-paper-documents.md` shredding rules. Both reference the same BAA requirement for shredding vendors.

**Genuinely distinct:** Contingency Planning is a separate HIPAA Security Rule requirement (§164.308(a)(7)) that auditors look for by name — backup, DR, emergency operations. It barely overlaps in content with the others; the overlap is just the standard scope/training boilerplate.

**Options:**
- *(a) Fold Paper Documents into Safeguards as a subsection; keep Contingency Planning standalone.*
- *(b) Keep all three separate but explicitly cross-link the shredding rules.*
- *(c) Merge all into one "Operational Safeguards" doc.* Risk: Contingency Planning loses its distinct identity, and auditors won't find a "Disaster Recovery / BCP" policy by name.

### Cluster C — Patient rights (3 files)

- `hipaa-right-to-access.md`
- `hipaa-right-to-amend.md`
- `hipaa-accounting-of-disclosures.md`

**Redundant:** identical procedural pattern — patient submits written request → Chief Privacy Officer responds within N days → response template letters in attachments. All three have nearly identical "30-day extension allowed" mechanics.

**Genuinely distinct:** different statutory clocks (30, 60, 60 days), different denial grounds, different sample letter templates. All three are HIPAA-required individual rights under different CFR sections (164.524, 164.526, 164.528).

**Options:**
- *(a) Merge into one "Patient Rights Policy" with three top-level sections.* Pro: each section can still be referenced by name; sample letter templates can sit together. Pro: kills 2x scope/training boilerplate.
- *(b) Keep all three separate.* They are already small (4–22KB).

### Cluster D — Use & disclosure of PHI (3 files)

- `hipaa-phi-use-and-disclosure.md` (legal, public health, regulatory)
- `hipaa-minimum-necessary.md`
- `hipaa-de-identifying-phi.md` (also includes Limited Data Sets and Data Use Agreements)
- `hipaa-marketing.md`

**Redundant:** all four govern when/how PHI may be used or disclosed. Minimum Necessary is referenced inside De-Identifying (§III(d)(v) bullet) and is foundational to all of them.

**Genuinely distinct:** each is a distinct HIPAA decision: do you need authorization (Marketing), can you de-identify instead (De-Identifying), is this disclosure exempt (Use & Disclosure for Legal/Public Health), and how much do you disclose (Minimum Necessary).

**Options:**
- *(a) Merge all four into one "PHI Use & Disclosure Policy" with subsections.* Pro: a single answer to "may we use/share this PHI?" Pro: kills shared scope/training boilerplate. Con: ~35KB doc.
- *(b) Keep Marketing standalone (it has very specific authorization mechanics and a definition unique to it) and merge the other three.*

### Cluster E — Governance, risk, vendor management, incidents (4 files)

- `information-security-framework.md` (master framework)
- `hipaa-risk-management.md`
- `hipaa-security-incidents.md`
- `hipaa-breach-notification.md`
- `hipaa-business-associate-agreement.md`

**Redundant:** `information-security-framework.md` is structurally a summary of all the other policies — it has sections on encryption, access control, incident response, breach notification, vendor management that all duplicate (in summary form) what those individual policies say.

**Genuinely distinct:** Risk Management has the formal annual risk-assessment process. Security Incidents has the IT incident-response procedure. Breach Notification has the *legal* 48-hour / 60-day notification cascade and exhibits (Risk Assessment form, sample letter, breach reporting form) — auditors absolutely look for this one by name. BAA has the vendor-onboarding procedure.

**Options:**
- *(a) Keep all 5 separate but treat the framework as the table-of-contents/landing page that points into them.*
- *(b) Merge framework + Risk Management into "Governance & Risk Management"; merge Security Incidents + Breach Notification into "Incident & Breach Response"; keep BAA standalone (or fold into Governance as Vendor Management section).* This is the cleanest 3-file outcome for this cluster.
- *(c) Merge Security Incidents into Breach Notification.* Risky — they have different audiences (Security Officer vs Privacy Officer) and different statutory triggers.

### Cluster F — Patient-facing notice + SDLC + Reference inventories (3 + 2 files)

- `privacy-policy.md` — currently mis-titled (see top of doc); needs to be rebuilt as an actual Notice of Privacy Practices, OR deleted after content rescue.
- `sdlc-and-asset-lifecycle.md` — separate concern (CTO-owned, developer-facing).
- `hipaa-definitions.md` — glossary; standalone or absorbed.
- `platform-and-access-matrix.md` — pure inventory (xlsx-derived).
- `ech-security-assessment.md` — vendor questionnaire (xlsx-derived).

The two xlsx-derived files are noted in the README as "read-only snapshots" of the canonical spreadsheets. They should stay as-is and not be merged with anything.

---

## §3 — Proposed consolidated structure

Recommended target: **6 thematic policies + 2 reference matrices + 1 patient-facing notice (TBD)** = 9 files total, down from 24.

Estimated sizes are rough character counts assuming each section keeps only the substantive content (one shared scope + one training section + the policy-specific procedures), with boilerplate factored out per §5.

---

### 3.1 `governance-and-risk-management.md`

- **Purpose:** Master security & data governance framework, annual risk assessment process, and the Risk Review Committee charter. The "landing" policy that frames everything else.
- **Source files merged:**
  - `information-security-framework.md`
  - `hipaa-risk-management.md`
  - (The "Governance" parts of) `hipaa-definitions.md` §II(r) (Risk Management Team definition — reconcile with Risk Committee in Risk Management policy)
- **Outline:**
  1. Scope & applicability
  2. Roles: Chief Privacy Officer, Chief Security Officer, Risk Review Committee, CTO, CEO
  3. Information security & data governance framework (data classification, access control, encryption-at-a-glance, transmission, logging, retention) — narrative-level only, with pointers to the technical-safeguards doc for the specifics
  4. Annual risk assessment process (universe of ePHI → threat → vulnerability → control analysis → likelihood → impact → risk determination → recommendations → documentation)
  5. Risk mitigation process (prioritize → evaluate controls → cost-benefit → select → assign → implement → monitor)
  6. Risk management schedule (annual / ongoing / as-needed)
  7. Reporting (Risk Review Committee + Board if material; annual report to CEO)
  8. References (45 CFR §164.308(a)(1), NIST SP 800-30)
- **Estimated final size:** ~15–18 KB
- **Risks / what gets lost:** The framework's "Referenced Policies" list with Google Doc hyperlinks should be replaced with relative links to the new consolidated files. Nothing substantive lost.

---

### 3.2 `phi-use-and-disclosure.md`

- **Purpose:** All rules governing when and how Millie may use, disclose, request, de-identify, or market with PHI. The "may I send this?" policy.
- **Source files merged:**
  - `hipaa-phi-use-and-disclosure.md`
  - `hipaa-minimum-necessary.md`
  - `hipaa-de-identifying-phi.md` (including Data Use Agreement exhibit)
  - `hipaa-marketing.md`
- **Outline:**
  1. Scope & applicability
  2. Minimum Necessary Rule (uses, routine vs nonroutine disclosures, exceptions for Treatment)
  3. Permitted uses & disclosures for legal, public health & regulatory purposes (health oversight, public health, law enforcement, judicial proceedings, military, national security, correctional institutions, workers' compensation, organ donation, threat-to-safety)
  4. De-identification of PHI (Expert Determination + Safe Harbor 18-identifier list)
  5. Re-identification controls
  6. Limited Data Sets & Data Use Agreement requirements (with sample DUA in Appendix A)
  7. Marketing — definition, Financial Remuneration, when authorization is required, exceptions
  8. References (45 CFR §§164.501, 164.502, 164.508, 164.512, 164.514)
  9. Appendix A — Data Use Agreement template
- **Estimated final size:** ~38–45 KB
- **Risks / what gets lost:** Need to preserve the verbatim 18-identifier list in §4 (auditors check it). Marketing has a specific definitional structure (Financial Remuneration test) that must be preserved.
- **Auditor-finding note:** even though Marketing collapses into a subsection, the section should be titled exactly "**Marketing & Patient Communications**" so a `Ctrl-F` for "Marketing" in an audit lands on it.

---

### 3.3 `patient-rights.md`

- **Purpose:** Patient rights to access, amend, and request an accounting of disclosures of their own PHI. Includes response timelines, denial grounds, and sample letter templates.
- **Source files merged:**
  - `hipaa-right-to-access.md`
  - `hipaa-right-to-amend.md`
  - `hipaa-accounting-of-disclosures.md`
- **Outline:**
  1. Scope & applicability
  2. Right to inspect & obtain copies of PHI (30-day rule, manner of access, fees, electronic format requirements, patient portal)
     - Denial grounds (reviewable vs non-reviewable)
     - Personal representatives, parents/guardians
  3. Right to request amendment of PHI (60-day rule, acceptance/denial mechanics, statement of disagreement, amendments by other covered entities)
  4. Right to accounting of disclosures (6-year window, what's in vs excluded, tracking process, fees)
  5. References (45 CFR §§164.524, 164.526, 164.528)
  6. Appendix A — Sample letter templates (access denial, access acceptance, amendment denial, amendment acceptance, amendment rebuttal, extension)
- **Estimated final size:** ~38–42 KB
- **Risks / what gets lost:** The reference to a missing "Information Blocking Compliance Policy" (in current `hipaa-right-to-access.md`) needs to be either written or inlined. Recommend inlining the EHI definition and removing the broken cross-reference.

---

### 3.4 `technical-safeguards.md`

- **Purpose:** All technical and endpoint controls that protect PHI: encryption, passwords/auth, remote access, workstation use, device & media management.
- **Source files merged:**
  - `hipaa-encryption.md`
  - `hipaa-passwords.md`
  - `hipaa-remote-access.md`
  - `hipaa-workstation-use.md`
  - The Device & Media Management content currently buried in `privacy-policy.md` lines 564–609 ⚠️ MUST RESCUE
- **Outline:**
  1. Scope & applicability
  2. Access control & authentication (unique user IDs, RBAC, least privilege, MFA, password construction rules, mobile passcode rules, prohibited behaviors, password manager guidance, deactivation)
  3. Encryption (data in transit — FIPS 140-2, NIST SP 800-52/77/113; data at rest — NIST SP 800-111; key management; deactivation of keys on termination)
  4. Workstation use (lock timers, screen savers, mobile phones & iPads, prohibited configurations, data storage locations)
  5. Remote access (authorization, VPN, MFA, equipment handling, termination of privileges, monitoring)
  6. Device & media management (inventory, receipt/removal logs, disposal, reuse, NIST sanitization standards)
  7. Termination & role change (immediate revocation across passwords, remote access, encryption keys, device inventory) — single consolidated checklist
  8. References (45 CFR §§164.308(a)(5), 164.310(b), 164.310(d), 164.312)
- **Estimated final size:** ~32–38 KB
- **Risks / what gets lost:** This is the highest-risk merge because it pulls together 4 separately-numbered HIPAA policies (IT-001, IT-002, IT-005, IT-006) plus the orphaned IT-004. Auditors looking for "Password Policy" by name will need to land on section 2; "Encryption Policy" on section 3; etc. Preserve the original Policy # numbers in section headers so an audit reference like "IT-005" still resolves.
- **MUST PRESERVE verbatim:**
  - The 8-character + character-class password construction rules
  - The FIPS 140-2 / NIST SP 800-52/77/111/113 encryption standards
  - The "no PHI on hard drives" rule
  - The mobile passcode 6/8-digit rule

---

### 3.5 `operational-safeguards.md`

- **Purpose:** Administrative + physical safeguards that don't fit the technical bucket: oral/fax/email/text/voicemail protocols, paper document handling, facility security, and business continuity.
- **Source files merged:**
  - `hipaa-safeguards.md` (administrative + physical sections; the technical parts move to §3.4 above)
  - `hipaa-paper-documents.md`
  - `hipaa-contingency-planning.md`
- **Outline:**
  1. Scope & applicability
  2. Administrative safeguards
     - Oral communications
     - Facsimile transmissions
     - Telephone protocols (including voicemail/appointment reminders)
     - Email protocols
     - Texting
     - Social media
     - Disposal of PHI (general principle)
  3. Physical safeguards
     - Facility security plan
     - Access control & visitor validation
     - PHI storage (locked cabinets, public-area precautions)
  4. Paper document management
     - Handling (clean-desk, printers/copiers, mailing)
     - Storage (locked cabinets, key control)
     - Destruction (in-house shredding, third-party shredding via BAA, certificates of destruction)
  5. Contingency planning
     - Personnel safety priority
     - Data & software backup (encrypted, offsite, quarterly review)
     - IT system inventory
     - Disaster recovery plan
     - Emergency operations
     - Confidentiality of the plan
     - Insurance
  6. Training (annual + on-hire)
  7. References (45 CFR §§164.308(a)(7), 164.310, 164.316(b)(1), 164.530)
- **Estimated final size:** ~25–30 KB
- **Risks / what gets lost:** Contingency Planning is a HIPAA Security Rule requirement that auditors look for by name (§164.308(a)(7)). Make sure section 5 has a clear top-level anchor and that the README + Compliance Calendar references it correctly.

---

### 3.6 `incident-and-breach-response.md`

- **Purpose:** Detection, triage, internal response, and external notification when PHI is (or might be) compromised. Covers both the technical "security incident" track and the regulatory "breach notification" track.
- **Source files merged:**
  - `hipaa-security-incidents.md`
  - `hipaa-breach-notification.md` (including all 4 exhibits)
- **Outline:**
  1. Scope & applicability
  2. Definitions (Breach, Unsecured PHI, Date of Discovery, Disclosure, Use — pulled in from the embedded breach-notification definitions and from `hipaa-definitions.md`)
  3. Security incident reporting (any personnel → CSO within 24h)
  4. Security incident investigation, response, and post-incident analysis
  5. Security incident log (required fields)
  6. Breach determination (presumption + low-probability rebuttal + risk assessment form)
  7. Breach exceptions (good-faith access, inadvertent disclosure within authorized scope, unretainable disclosure)
  8. Notification of affected individuals (60-day rule, content, method, substitute notice)
  9. Notification to authorities (annual HHS report for <500, immediate HHS + media for ≥500)
  10. Notification to insurance carrier
  11. Mitigation, sanctions, complaints, accounting cross-references
  12. Annual privacy & security report to CEO
  13. Policy review cadence
  14. References (45 CFR §§164.308(a)(6), 164.400–164.414)
  15. Appendix A — State Breach Notification Requirements (California)
  16. Appendix B — Risk Assessment Form
  17. Appendix C — Sample patient breach notification letter
  18. Appendix D — Internal breach report form
- **Estimated final size:** ~32–35 KB
- **Risks / what gets lost:** **Critical that "Breach Notification" remain findable by name** — HHS/OCR audits explicitly request it. Use that phrase as the top-level heading for sections 6–11 so it appears in the table of contents and in any text search.
- **Auditor-finding note:** consider linking this policy under TWO file paths (or noting in the README) so both "Breach Notification" and "Security Incident Management" remain navigable concepts.

---

### 3.7 `vendor-and-business-associates.md`

- **Purpose:** Identifying Business Associates, executing BAAs, vendor risk assessment, and ongoing oversight.
- **Source files merged:**
  - `hipaa-business-associate-agreement.md`
  - The "Third-Party & Vendor Management" section of `information-security-framework.md` (§11)
- **Outline:**
  1. Scope & applicability
  2. Determining whether a vendor is a Business Associate
  3. Pre-engagement: security assessment (cross-reference `ech-security-assessment.md`)
  4. BAA execution requirements (template, modifications, storage in Google Workspace Contracts > BAAs)
  5. Subcontractor / subprocessor / Nth-party flow-down obligations
  6. Annual BAA review (cross-reference Compliance Calendar)
  7. Breach of a BAA
  8. References (45 CFR §164.308(b)(1))
- **Estimated final size:** ~6–8 KB
- **Risks / what gets lost:** Small file — but BAA is one auditors look for by name, so keeping it separate is worth the small overhead. Could alternatively become a subsection of §3.1 (Governance) — judgment call for the reviewer.

---

### 3.8 `sdlc-and-asset-lifecycle.md` (UNCHANGED)

Keep as a standalone CTO-owned policy. It is the only developer-facing policy and naturally lives separately from the HIPAA officer-owned set.

- **Estimated final size:** ~4 KB (no change)
- **Risks / what gets lost:** None.

---

### 3.9 Reference matrices (UNCHANGED, read-only snapshots)

- `platform-and-access-matrix.md` — keep as-is (read-only xlsx snapshot per README)
- `ech-security-assessment.md` — keep as-is (read-only xlsx snapshot per README)

---

### 3.10 What to do about `privacy-policy.md`

Two scenarios; pick one before deletion:

- **Scenario A — Repurpose:** Rewrite as an actual patient-facing **Notice of Privacy Practices** (which is what the README expects). This is a different beast from the internal HIPAA operating policies — it is the §164.520 NPP that is given to every patient and posted on the website. This needs to be drafted fresh; the current file does not contain a patient-facing notice.
- **Scenario B — Delete:** Drop the file entirely (after rescuing the Device & Media Management content into `technical-safeguards.md` per §3.4) and remove the row from the README §1 Policy Index. Add a new TODO in the README for "Patient-facing Notice of Privacy Practices — to be drafted."

**Recommendation:** Scenario B + add a TODO. The patient NPP is a separate compliance artifact and should not be drafted as part of this consolidation pass.

---

### 3.11 What to do about `hipaa-definitions.md`

See §4 below — recommendation is to keep it as a standalone glossary.

---

## §4 — Definitions strategy

**Recommendation: Keep `hipaa-definitions.md` as a centralized glossary, and remove duplicate inline definitions from the other files (replace with "as defined in `hipaa-definitions.md`").**

Rationale:
- 13+ terms are reused across 3+ files (see §1.6). Centralizing eliminates drift risk (e.g., `ePHI` defined slightly differently in Encryption vs Risk Management vs Framework).
- The glossary is short (~7KB) and easy to scan.
- HIPAA auditors are comfortable with a "Definitions" annex; this is a standard convention.

Tweaks:
- **Add** `Marketing`, `Financial Remuneration`, `Unsecured PHI`, `Date of Discovery`, `Disclosure`, `Use`, `Designated Record Set`, `Electronic Health Information (EHI)`, `Limited Data Set` — these are currently scattered.
- **Reconcile** `Risk Management Team` (in `hipaa-definitions.md`) vs `Risk Review Committee` / `Risk Committee` (used in `hipaa-risk-management.md` and `README.md`). These appear to refer to different bodies (the Risk Management Team is the standing operational group; the Risk Review Committee is the governance body that receives reports). Clarify.
- **Add** `Risk Review Committee` as a distinct defined term.
- **Add** `Chief Privacy Officer`, `Chief Security Officer`, `Risk Committee` as defined terms (currently used everywhere but never formally defined as Millie roles).
- **Remove** the "Scope" header from `hipaa-definitions.md` (it doesn't need one; it's a glossary), and remove the boilerplate Scope paragraph. Just leave a 1-line "These definitions apply to all Millie policies."

Definitions to centralize (from the files where they currently live):

| Term | Currently defined in (delete after centralizing) |
|---|---|
| `Breach` | `hipaa-definitions.md` (keep); also implicitly in `hipaa-breach-notification.md` `privacy-policy.md` |
| `Unsecured PHI` | `hipaa-breach-notification.md` §II(c) → move to definitions |
| `Disclosure` | `hipaa-breach-notification.md` §II(b) → move to definitions |
| `Use` | `hipaa-breach-notification.md` §II(d) → move to definitions |
| `Date of Discovery` | `hipaa-breach-notification.md` §IV(a)(ii) → move to definitions |
| `Marketing` | `hipaa-marketing.md` §II(a) → move to definitions |
| `Financial Remuneration` | `hipaa-marketing.md` §II(b) → move to definitions |
| `Limited Data Set` | `hipaa-de-identifying-phi.md` §III(c)(ii) → move to definitions |

---

## §5 — Boilerplate strategy

Three categories of boilerplate need different treatment.

### 5a — Scope statement (the "applies to all facilities and locations…" paragraph)

**Recommendation: Extract once to a shared preamble at the top of each consolidated policy, OR drop it entirely in favor of a one-line statement at the top of the README + each policy.**

Currently this 60-word paragraph appears 19 times in the policy folder + 9 more times inside `privacy-policy.md`. After consolidation to 6 policies, it would still repeat 6 times — which is fine for standalone readability. Suggested unified wording (fixes the missing-space typo):

> **Scope.** This policy applies to all facilities and locations owned, operated, or managed by Millie, Inc. ("Company"), and all Company personnel. For purposes of this policy, the term "personnel" includes all licensed professionals and staff who perform services on behalf of Company.

Variant for `sdlc-and-asset-lifecycle.md` keeps its broader systems/contractors scope.

### 5b — Training requirement

**Recommendation: Single canonical statement in `operational-safeguards.md` §6 (Training).** Other policies that currently embed training language (`hipaa-encryption.md`, `hipaa-paper-documents.md`, `hipaa-contingency-planning.md`) replace it with: *"All personnel receive HIPAA training on hire and annually — see `operational-safeguards.md` §6."*

The README's Annual section already correctly anchors training to `hipaa-safeguards.md` — update that link to the new file.

### 5c — Disciplinary action / sanctions

**Recommendation: Add a single sanctions clause to `governance-and-risk-management.md`** that covers all policies, modeled on the existing language in `hipaa-risk-management.md` §II(d):

> **Sanctions.** Any personnel member who violates this Policy or any other Millie information privacy or security policy will be subject to disciplinary action up to and including termination, based on the severity of the violation, in accordance with Millie's Corrective Action Policy.

This closes the gap noted in §1.4 and satisfies 45 CFR §164.530(e) at a single location. (Note: the Corrective Action Policy is referenced in `hipaa-breach-notification.md` but does not exist in this repo — flag for separate authoring.)

### 5d — Frontmatter & metadata table

**Recommendation: Pick ONE.** Currently every file has both YAML frontmatter (`title:`, `last_reviewed:`, `owner:`) AND a 2-row markdown metadata table (Title, Policy #, Effective Date, Last Revised). This is triple-redundant with the file's H1.

Suggest: keep YAML frontmatter and add `policy_number:`, `effective_date:`, and `last_revised:` fields to it. Delete the markdown metadata table from every file. This is a separate, easy janitorial pass.

### 5e — Review cadence

Only `hipaa-security-incidents.md` currently has explicit "Last Reviewed / Review Cadence" rows. The README's Annual section says "Review and refresh every policy in this folder" — so the cadence is consistent (annual). Recommend adding `review_cadence: annual` to the frontmatter of all 6 consolidated policies rather than embedding it in each document body.

---

## §6 — Migration steps

Suggested ordering. Each step is independently shippable so the repo never has broken cross-references at HEAD.

### Step 0 — Preparation (no file moves)

1. **Rescue the Device & Media Management content** from `privacy-policy.md` lines 564–609 to a temporary working file. This is the only place where IT-004 lives.
2. **Verify no other file references** any of the 24 file names except via README. Run `grep -r '\.md' "New Policy Docs/"`. The current cross-references are mostly prose ("See Workstation Use, Encryption…") rather than file links, so URL breakage is minimal, but worth confirming.
3. **Decide Scenario A vs B for `privacy-policy.md`** (§3.10). Default to B.
4. **Decide whether to keep BAA standalone or fold into Governance** (§3.7).
5. **Confirm definition reconciliation for `Risk Management Team` vs `Risk Review Committee`** with the policy owners.

### Step 1 — Definitions consolidation (low-risk warm-up)

Update `hipaa-definitions.md` to add the centralized terms listed in §4. This file gets touched but does not yet rename or delete anything. Run a search for each newly-centralized term in the rest of the policies; replace inline definitions with cross-references.

### Step 2 — Create the 6 new thematic files

In a single PR (or 6 small ones if review bandwidth is tight), create:

1. `governance-and-risk-management.md` (merges `information-security-framework.md` + `hipaa-risk-management.md`)
2. `phi-use-and-disclosure.md` (merges `hipaa-phi-use-and-disclosure.md` + `hipaa-minimum-necessary.md` + `hipaa-de-identifying-phi.md` + `hipaa-marketing.md`)
3. `patient-rights.md` (merges `hipaa-right-to-access.md` + `hipaa-right-to-amend.md` + `hipaa-accounting-of-disclosures.md`)
4. `technical-safeguards.md` (merges `hipaa-encryption.md` + `hipaa-passwords.md` + `hipaa-remote-access.md` + `hipaa-workstation-use.md` + **rescued IT-004 Device & Media Management content**)
5. `operational-safeguards.md` (merges `hipaa-safeguards.md` + `hipaa-paper-documents.md` + `hipaa-contingency-planning.md`)
6. `incident-and-breach-response.md` (merges `hipaa-security-incidents.md` + `hipaa-breach-notification.md` with all 4 exhibits)
7. `vendor-and-business-associates.md` (if kept separate per §3.7)

In each new file, include a one-line "Supersedes" note in the frontmatter listing the old Policy # numbers it absorbs — auditors who arrive expecting "L-006 Marketing Policy" can confirm it is now §7 of `phi-use-and-disclosure.md`.

### Step 3 — Delete the old single-topic files

Once the 6 new files are merged, delete (don't redirect — this is a git repo, history is preserved):

- `hipaa-accounting-of-disclosures.md`
- `hipaa-breach-notification.md`
- `hipaa-business-associate-agreement.md` (if folded into Governance)
- `hipaa-contingency-planning.md`
- `hipaa-de-identifying-phi.md`
- `hipaa-encryption.md`
- `hipaa-marketing.md`
- `hipaa-minimum-necessary.md`
- `hipaa-paper-documents.md`
- `hipaa-passwords.md`
- `hipaa-phi-use-and-disclosure.md`
- `hipaa-remote-access.md`
- `hipaa-right-to-access.md`
- `hipaa-right-to-amend.md`
- `hipaa-risk-management.md`
- `hipaa-safeguards.md`
- `hipaa-security-incidents.md`
- `hipaa-workstation-use.md`
- `information-security-framework.md`
- `privacy-policy.md` (after Device & Media rescue)

Keep:
- `sdlc-and-asset-lifecycle.md`
- `platform-and-access-matrix.md`
- `ech-security-assessment.md`
- `hipaa-definitions.md`

Final count: **4 unchanged + 6 new + 0 leftover = 10 files** (or 9 if BAA is folded into Governance).

### Step 4 — Update [README.md](README.md)

In a single commit alongside Step 3:

- **§1 Policy Index** — rewrite the table. 24 rows → 9 rows. Add a "Supersedes" column for the first migration cycle so anyone with bookmarks can find what they're looking for; remove the column after a quarter.
- **§2 Compliance Calendar** — update every "Source" link to point to the new file. Most rows currently point to deprecated files.
- **§3 Responsibility Matrix** — collapse the rows. 25 → ~10 rows. Owners should not change.
- **Add to "Notes on the migration"** a paragraph documenting the consolidation and pointing readers to this proposal document as the migration record.

### Step 5 — Address dangling cross-references (separate task)

These are real holes that consolidation surfaces but does not fix — list them in a follow-up issue:

- "Company Internal Investigations & Corrective Action Policy" (referenced in breach notification) — does not exist.
- "Information Blocking Compliance Policy" (referenced in right-to-access) — does not exist. Decision: inline the EHI definition in `patient-rights.md` §2 and drop the cross-reference.
- "Company Device Management and Media Management/Inventory Policy" (referenced in remote-access and safeguards) — resolved by the IT-004 rescue in Step 0.
- Patient-facing Notice of Privacy Practices — does not exist. Decision: TODO in README.

### Step 6 — Janitorial (lowest-priority, optional)

- Fix the missing-space typo "Companypersonnel" → "Company personnel" throughout (sed pass).
- Strip the redundant markdown metadata table from every file's header; move the metadata into YAML frontmatter (see §5d).
- Strip the `400989...1` page-number artifacts and `![](data:image/png;base64...)` image placeholders from the (now-deleted) `privacy-policy.md` and from any retained files.

---

## Appendix — Quick reference: 24 → 9 mapping

| Old file | New home |
|---|---|
| hipaa-accounting-of-disclosures.md | patient-rights.md §4 |
| hipaa-breach-notification.md | incident-and-breach-response.md §§6–11 |
| hipaa-business-associate-agreement.md | vendor-and-business-associates.md (or governance §X) |
| hipaa-contingency-planning.md | operational-safeguards.md §5 |
| hipaa-de-identifying-phi.md | phi-use-and-disclosure.md §§4–6 |
| hipaa-definitions.md | unchanged (expanded per §4) |
| hipaa-encryption.md | technical-safeguards.md §3 |
| hipaa-marketing.md | phi-use-and-disclosure.md §7 |
| hipaa-minimum-necessary.md | phi-use-and-disclosure.md §2 |
| hipaa-paper-documents.md | operational-safeguards.md §4 |
| hipaa-passwords.md | technical-safeguards.md §2 |
| hipaa-phi-use-and-disclosure.md | phi-use-and-disclosure.md §3 |
| hipaa-remote-access.md | technical-safeguards.md §5 |
| hipaa-right-to-access.md | patient-rights.md §2 |
| hipaa-right-to-amend.md | patient-rights.md §3 |
| hipaa-risk-management.md | governance-and-risk-management.md §§4–6 |
| hipaa-safeguards.md | operational-safeguards.md §§2–3 (technical bits → technical-safeguards.md) |
| hipaa-security-incidents.md | incident-and-breach-response.md §§3–5 + §12 |
| hipaa-workstation-use.md | technical-safeguards.md §4 |
| information-security-framework.md | governance-and-risk-management.md §3 + vendor §X |
| privacy-policy.md | DELETE (after rescuing IT-004 Device & Media to technical-safeguards.md §6); TODO for new NPP |
| sdlc-and-asset-lifecycle.md | unchanged |
| platform-and-access-matrix.md | unchanged |
| ech-security-assessment.md | unchanged |
