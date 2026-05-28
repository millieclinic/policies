# Changes — Final Markdown vs Original Converted Markdown

`3. Final Word/3.a Final Markdown/` started as an exact copy of `1. Original Docs (Word)/1.a Original Converted to MD/` (37 files, no edits). This document is the **comprehensive log of every change applied on top**: deletions, content additions, file merges, and renames. The full diff is visible per-file in git history; this is the executive-readable summary.

**Net change: 37 → 19 active policy files** (+ `CHANGES.md` = 20 files in the folder).
- 9 superseded duplicate files removed (§1)
- 3 short ECH-required clauses added to existing policies (§2)
- 4 thematic merges consolidated 14 source files into 4 new files (§4)
- 16 remaining files renamed with category prefixes for browsability (§5)
- 1 file (Medical Waste Management Plan) added later from a previously-overlooked source

No original content was rewritten. Every merge preserves its source policies verbatim as named sub-sections.

---

## 1. Deletions — superseded duplicate versions (9 files removed)

The originals included pairs / quadruplets of the same policy at different revision dates. We keep the newest of each and remove the rest. The originals remain untouched in `1. Original Docs (Word)/1.a Original Converted to MD/` for full audit history.

| Removed | Kept | Why |
|---|---|---|
| `03d HIPAA - Contingency Planning Policy.md` | `03d HIPAA - Contingency Planning Policy (1).md` | The `(1)` version is the May 7 revision; un-suffixed is the older May 1 baseline. |
| `03l HIPAA - Millie_BAA (for BA Use with Subcontractor).md` (legacy `.doc`) | `HIPAA - Millie_BAA (for BA Use with Subcontractor).md` (modern `.docx`) | Modern `.docx` supersedes the legacy `.doc`; same BAA template content. |
| `03q HIPAA - Risk Management Policy.md` | `03q HIPAA - Risk Management Policy (1).md` | Both converted to byte-identical Markdown. Kept the `(1)`. |
| `03s HIPAA - Security Incident Management Policy (1).md` (May 14 `.pdf`) | `03s HIPAA - Security Incident Management Policy (2).md` (May 18 `.docx`) | Four versions existed (two `.pdf`, two `.docx`). `(2).docx` is newest. |
| `03s HIPAA - Security Incident Management Policy.docx.md` (May 1 `.docx`) | same as above | Oldest of the four. |
| `03s HIPAA - Security Incident Management Policy.pdf.md` (May 6 `.pdf`) | same as above | Superseded by the May 14 PDF and the May 18 DOCX. |
| `03w HIPAA - Workstation Use Policy.md` | `03w HIPAA - Workstation Use Policy (1).md` | `(1)` is May 4; un-suffixed is May 1. |
| `Millie Information Security & Data Governance Framework.md` | `Millie Information Security & Data Governance Framework (1).md` | `(1)` is May 23; un-suffixed is May 5. |
| `Millie Privacy Policy.md` | `Millie Privacy Policy (1).md` | Byte-identical. Kept `(1)`. |

---

## 2. Additions — three short ECH-required clauses

Driven by `2. Gaps/2.a Gaps Markdown/GAPS.md`. Each was appended to an existing policy in its native voice (numbered list, italic sub-section header, formal "Company shall…" tone) so it reads as part of the original rather than a bolted-on extension.

### 2.1 — Email Authentication & Anti-Malware Exclusions

- **Now in:** `01a. Information Security Framework.md` §6 Data Transmission & Sharing
- **ECH driver:** ISD IT Risk Assessment / Additional Cybersecurity Questions, CSV rows 50, 51, 55 (DMARC + AV-exclusion + vuln-scan-exclusion stance).
- **What it says:** Google Workspace anti-malware with no custom exclusions; SPF / DKIM / DMARC at policy = quarantine or stricter on Millie-owned sending domains; vuln scanning has no application-side exclusions and any exception requires Chief Security Officer approval.

### 2.2 — BYOD & Mobile Device Management

- **Now in:** `03a. Technical Safeguards — Encryption, Passwords, Remote Access & Workstations.md` (Workstation Use sub-section)
- **ECH driver:** SIG Lite §M.1.3 / §M.1.5 / §M.1.6 (CSV rows 132–134, all flagged "FOLLOW UP").
- **What it says:** BYOD permitted for email / messaging / approved SaaS; PHI not stored locally on personal devices; any device touching PHI must be enrolled in MDM with passcode / encryption / remote-wipe; un-enrolled personal devices restricted to web SaaS via SSO + MFA.

### 2.3 — Pandemic Operations & Multi-Vendor Risk

- **Now in:** `04a. Contingency Planning Policy.md`
- **ECH driver:** SIG Lite §K.4 (pandemic plan, currently NO) and §K.30 (multi-vendor resiliency, currently NO).
- **What it says:** Pandemic patient operations governed by the COVID Policy; operational continuity may shift to telehealth-first / essential-on-site; cloud-first stack with single-vendor dependencies on Aptible / AWS / Cloudflare / Google Workspace is a documented accepted risk reviewed annually.

---

## 3. Items intentionally NOT changed

Per the gap analysis, the following questionnaire-surfaced items did **not** drive a policy edit:

- **Cyber-liability certificate + pentest / audit attestation** (Insurances row 181; Security Audits rows 182–183) — these are evidence attachments for the ECH submission package, not policy text.
- **Operational AWS judgment calls** (IAM users with console access, wildcard admin, AWS Config off, public subnet residue) — covered by honest answers in the ECH CSV; no policy edit warranted at Millie's size.
- **PCI DSS, ESG, IoMT, GLBA, antitrust, fraud-prevention program, standalone HR security policy, AI policy** — all marked N/A. Answer N/A on the submission with the one-line justifications in `2. Gaps/2.a Gaps Markdown/NA-justifications.md`.

---

## 4. Thematic merges (14 source files → 4 merged files)

Each merged file has (a) a brief blended intro at the top describing the topic, and (b) the source policies preserved verbatim as `## I. <Section>`, `## II. <Section>`, … sub-sections. Auditors with a checklist still find each original policy by name. The merged file's top metadata table lists the source Policy # codes.

### 4.1 — `02b. Patient Rights — Access, Amendment & Accounting of Disclosures.md`

Merges (preserving each verbatim as a sub-section):

| Original source | Policy # | New sub-section |
|---|---|---|
| `03k HIPAA - Individual Rights to Access Their Records Policy.md` | L-009 | I. Right to Access PHI |
| `03j HIPAA - Individual Right to Request Amendments to PHI Policy.md` | L-008 | II. Right to Request Amendments to PHI |
| `03a HIPAA- Accounting of Disclosures Policy.md` | L-003 | III. Accounting of Disclosures |

### 4.2 — `02c. PHI Use, Disclosure, Minimum Necessary & De-Identification.md`

| Original source | Policy # | New sub-section |
|---|---|---|
| `03v HIPAA - Use and Disclosure of PHI for Various Legal, Public Health and Regulatory Purposes Policy.md` | L-002 | I. Use & Disclosure of PHI for Legal, Public Health & Regulatory Purposes |
| `03m HIPAA - Minimum Necessary Rule Policy.md` | L-010 | II. Minimum Necessary Rule |
| `03e HIPAA - De-Identifying and Re-Identifying PHI and Creation of Limited Data Sets Policy.md` | L-005 | III. De-Identifying & Re-Identifying PHI + Limited Data Sets |
| `03h HIPAA and Marketing Policy.md` | L-006 | IV. Marketing & Patient Communications |

### 4.3 — `03a. Technical Safeguards — Encryption, Passwords, Remote Access & Workstations.md`

| Original source | Policy # | New sub-section |
|---|---|---|
| `03g HIPAA - Encryption Policy.md` | IT-005 | I. Encryption |
| `03o HIPAA - Password Management Policy.md` | IT-001 | II. Password Management |
| `03p HIPAA - Remote Access Policy.md` | IT-006 | III. Remote Access |
| `03w HIPAA - Workstation Use Policy (1).md` | IT-002 | IV. Workstation Use (including BYOD & Mobile Device Management) |

Note: the Workstation Use sub-section retains the BYOD/MDM clause (§2.2 above).

### 4.4 — `05a. Incident & Breach Response.md`

| Original source | Policy # | New sub-section |
|---|---|---|
| `03s HIPAA - Security Incident Management Policy (2).md` | IT-009 | I. Security Incident Management |
| `03b HIPAA - Breach Notification Policy.md` | L-004 | II. HIPAA Breach Notification |
| `AWS and Aptible Security Incident Management Policy.md` | (no original #) | III. AWS & Aptible Cloud Incident Playbook |

---

## 5. Renames (16 files renumbered with category prefixes)

No content changed; only the filenames. Done with `git mv` so per-file history is preserved.

| Old filename | New filename |
|---|---|
| `Millie Information Security & Data Governance Framework (1).md` | `01a. Information Security Framework.md` |
| `03i HIPAA Definitions Policy.md` | `01b. HIPAA Definitions.md` |
| `03q HIPAA - Risk Management Policy (1).md` | `01c. Risk Management Policy.md` |
| `03r HIPAA - Safeguards Policy.md` | `01d. Safeguards Policy.md` |
| `Millie Privacy Policy (1).md` | `02a. Privacy Policy.md` |
| `03d HIPAA - Contingency Planning Policy (1).md` | `04a. Contingency Planning Policy.md` |
| `03n HIPAA - Paper Document Management Policy.md` | `04b. Paper Document Management Policy.md` |
| `Millie Clinic COVID Policy.md` | `04c. COVID Policy.md` |
| `Medical Waste Management Plan.md` | `04d. Medical Waste Management Plan.md` |
| `03c HIPAA - Business Associate Agreement Policy.md` | `06a. Business Associate Agreement Policy.md` |
| `System Development Life Cycle (SDLC) & Asset Lifecycle Policy.md` | `06b. SDLC & Asset Lifecycle Policy.md` |
| `HIPAA - Millie_BAA (for BA Use with Subcontractor).md` | `06c. BAA Template (Subcontractor).md` |
| `Millie Matrix of Platforms, Software Subscriptions, and Access (1).md` | `07a. Platform & Subscription Matrix.md` |
| `03u HIPAA - TEMPLATE - Insurance Authorization and Assignment of Benefits (002).md` | `07b. Insurance Authorization Form Template.md` |
| `ECH Security Assessment Questions (1).md` | `07c. ECH Security Assessment Snapshot.md` |

Category numbering:

| Prefix | Category | Files |
|---|---|---|
| `01.` | Foundational & Governance | 01a–01d (4 files) |
| `02.` | Privacy & Patient Rights | 02a–02c (3 files; 02b and 02c are merges) |
| `03.` | Technical Safeguards | 03a (1 file; merge) |
| `04.` | Operations & Continuity | 04a–04d (4 files) |
| `05.` | Incident & Breach Response | 05a (1 file; merge) |
| `06.` | Vendor & Software | 06a–06c (3 files) |
| `07.` | Reference | 07a–07c (3 files) |

---

## 6. Inventory after all changes (19 active policies + CHANGES.md)

```
01a. Information Security Framework.md           ← +ECH email auth clause
01b. HIPAA Definitions.md
01c. Risk Management Policy.md
01d. Safeguards Policy.md
02a. Privacy Policy.md                           (Note: misnamed bundle of HIPAA staff policies, not a patient-facing NPP)
02b. Patient Rights — Access, Amendment & Accounting of Disclosures.md    ← MERGE of 3 files
02c. PHI Use, Disclosure, Minimum Necessary & De-Identification.md        ← MERGE of 4 files
03a. Technical Safeguards — Encryption, Passwords, Remote Access & Workstations.md  ← MERGE of 4 files (+BYOD/MDM clause)
04a. Contingency Planning Policy.md              ← +pandemic/multi-vendor clause
04b. Paper Document Management Policy.md
04c. COVID Policy.md
04d. Medical Waste Management Plan.md
05a. Incident & Breach Response.md               ← MERGE of 3 files
06a. Business Associate Agreement Policy.md
06b. SDLC & Asset Lifecycle Policy.md
06c. BAA Template (Subcontractor).md
07a. Platform & Subscription Matrix.md
07b. Insurance Authorization Form Template.md
07c. ECH Security Assessment Snapshot.md
CHANGES.md                                       (this file)
```

---

## 7. How to maintain this folder

1. **When ECH changes** (new vendor questionnaire, regulator update): start in `2. Gaps/2.a Gaps Markdown/`. Re-evaluate the row-level coverage matrix. Default to N/A unless ECH explicitly asks for new policy text.
2. **When a real gap appears**: append the smallest possible clause to an *existing* file here. Don't create a new file unless the gap is genuinely orthogonal to every existing policy.
3. **When a policy is materially revised**: edit the file here directly. The diff against `1. Original Docs (Word)/1.a Original Converted to MD/` shows total drift from the original; the per-file git history shows what changed when.
4. **After any edit**, run `./scripts/build-word-docs.py` to regenerate `3. Final Word/*.docx` and `2. Gaps/*.docx` / `*.xlsx`.
5. **Quarterly / annual review burden** is sized by file count. Keep this folder lean. 19 files today.
