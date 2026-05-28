# Changes — Final Markdown vs Original Converted Markdown

`3. Final Word/3.a Final Markdown/` started as an exact copy of `1. Original Docs (Word)/1.a Original Converted to MD/` (37 files, no edits). This document lists every change applied on top, and why. The full diff is visible per-file in git history; this is the executive-readable summary.

**Net change: 37 → 28 files, with 3 short clauses added to existing policies.** No new files were authored. No content was rewritten.

---

## 1. Deletions — superseded duplicate versions (9 files removed)

The originals included pairs / quadruplets of the same policy at different revision dates. We keep the newest of each and remove the rest. The originals remain untouched in `1. Original Docs (Word)/1.a Original Converted to MD/` for full audit history.

| Removed | Kept | Why |
|---|---|---|
| `03d HIPAA - Contingency Planning Policy.md` | `03d HIPAA - Contingency Planning Policy (1).md` | The `(1)` version is the May 7 revision; the un-suffixed version is the older May 1 baseline. |
| `03l HIPAA - Millie_BAA (for BA Use with Subcontractor).md` (legacy `.doc`) | `HIPAA - Millie_BAA (for BA Use with Subcontractor).md` (modern `.docx`) | Modern `.docx` supersedes the legacy `.doc`; content is the same BAA template. |
| `03q HIPAA - Risk Management Policy.md` | `03q HIPAA - Risk Management Policy (1).md` | Both converted to byte-identical Markdown. Kept the `(1)` per filename convention. |
| `03s HIPAA - Security Incident Management Policy (1).md` (May 14 `.pdf`) | `03s HIPAA - Security Incident Management Policy (2).md` (May 18 `.docx`) | Four versions of this file existed (two `.pdf`, two `.docx`). `(2).docx` is the newest. |
| `03s HIPAA - Security Incident Management Policy.docx.md` (May 1 `.docx`) | same as above | Oldest of the four. |
| `03s HIPAA - Security Incident Management Policy.pdf.md` (May 6 `.pdf`) | same as above | Superseded by the May 14 PDF and the May 18 DOCX. |
| `03w HIPAA - Workstation Use Policy.md` | `03w HIPAA - Workstation Use Policy (1).md` | `(1)` is May 4; un-suffixed is May 1. |
| `Millie Information Security & Data Governance Framework.md` | `Millie Information Security & Data Governance Framework (1).md` | `(1)` is May 23; un-suffixed is May 5. |
| `Millie Privacy Policy.md` | `Millie Privacy Policy (1).md` | Byte-identical. Kept `(1)`. |

These nine deletions reduce the policy set to 28 files without losing any content.

---

## 2. Additions — three short ECH-required clauses

Driven by `2. Gaps/2.a Gaps Markdown/GAPS.md`. Each was appended to an existing policy in its native voice (numbered list, italic sub-section header, formal "Company shall…" tone) so it reads as part of the original rather than a bolted-on extension.

### 2.1 — Email Authentication & Anti-Malware Exclusions

- **File:** `Millie Information Security & Data Governance Framework (1).md`
- **Location:** Appended one paragraph to §6 Data Transmission & Sharing.
- **ECH driver:** ISD IT Risk Assessment / Additional Cybersecurity Questions, CSV rows 50, 51, 55 (DMARC + AV-exclusion + vuln-scan-exclusion stance).
- **What it says:** Google Workspace anti-malware with no custom exclusions; SPF / DKIM / DMARC at policy = quarantine or stricter on Millie-owned sending domains; vuln scanning has no application-side exclusions and any exception requires Chief Security Officer approval.

### 2.2 — BYOD & Mobile Device Management

- **File:** `03w HIPAA - Workstation Use Policy (1).md`
- **Location:** Appended as new numbered sub-section `*BYOD & Mobile Device Management*.` immediately before the References section.
- **ECH driver:** SIG Lite §M.1.3 / §M.1.5 / §M.1.6 (CSV rows 132–134, all flagged "FOLLOW UP").
- **What it says:** BYOD permitted for email / messaging / approved SaaS; PHI not stored locally on personal devices; any device touching PHI must be enrolled in MDM with passcode / encryption / remote-wipe; un-enrolled personal devices restricted to web SaaS via SSO + MFA.

### 2.3 — Pandemic Operations & Multi-Vendor Risk

- **File:** `03d HIPAA - Contingency Planning Policy (1).md`
- **Location:** Appended as new numbered sub-section `*Pandemic Operations & Multi-Vendor Risk*.` immediately before the References section.
- **ECH driver:** SIG Lite §K.4 (pandemic plan, currently NO) and §K.30 (multi-vendor resiliency, currently NO).
- **What it says:** Pandemic patient operations governed by the COVID Policy; operational continuity may shift to telehealth-first / essential-on-site; cloud-first stack with single-vendor dependencies on Aptible / AWS / Cloudflare / Google Workspace is a documented accepted risk reviewed annually.

---

## 3. Items intentionally NOT changed

Per the gap analysis, the following questionnaire-surfaced items did **not** drive a policy edit:

- **Cyber-liability certificate + pentest / audit attestation** (Insurances row 181; Security Audits rows 182–183) — these are evidence attachments for the ECH submission package, not policy text. The Contingency Planning Policy already commits to obtaining cyber-liability insurance; the actual certificate lives in business records.
- **Operational AWS judgment calls** (IAM users with console access, wildcard admin, AWS Config off, public subnet residue) — covered by honest answers in the ECH CSV; no policy edit warranted at Millie's size.
- **PCI DSS, ESG, IoMT, GLBA, antitrust, fraud-prevention program, standalone HR security policy, AI policy** — all marked N/A in the gap analysis. Answer N/A on the submission with the one-line justifications in `2. Gaps/2.a Gaps Markdown/NA-justifications.md`.

---

## 4. Inventory after changes

29 files remain in `3. Final Word/3.a Final Markdown/`:

- **Privacy / patient-rights HIPAA suite (10):** Accounting of Disclosures, Breach Notification, BAA Policy, De-Identifying PHI, Definitions, Marketing, Min Necessary Rule, Paper Document Mgmt, Right to Access, Right to Amend, Use & Disclosure of PHI, Privacy Policy *(L-series + standalone)*
- **Security / technical HIPAA suite (5):** Contingency Planning *(+ pandemic / multi-vendor clause)*, Encryption, Password Mgmt, Remote Access, Risk Mgmt, Safeguards, Security Incident Mgmt, Workstation Use *(+ BYOD / MDM clause)* *(IT-series)*
- **Frameworks & lifecycle (3):** Information Security & Data Governance Framework *(+ email auth clause)*, SDLC & Asset Lifecycle Policy, AWS and Aptible Security Incident Management Policy
- **Templates (2):** BAA-for-Subcontractor template, Insurance Authorization template
- **Operational (3):** Millie Clinic COVID Policy, Medical Waste Management Plan, Platform Matrix
- **Reference (1):** ECH Security Assessment Questions snapshot

## 4a. Later additions

- **2026-05-26 — Medical Waste Management Plan.** Existing Millie document that wasn't in the original inventory. Converted via markitdown and added to both folders 1 and 3 unchanged. Covers California Medical Waste Management Act compliance (HSC §§ 117935, 117960) for small-quantity-generator status. Authored by Patricia Bevitz (Director of Clinical Operations). Not driven by ECH; added for completeness. Net effect on gap analysis: 2 SIG ESG rows moved from N/A to Partial — **O.4** (hazardous/toxic chemical handling, storage, disposal) and **O.9** (Health & Safety policy) — because the Waste Plan plus the COVID Policy and Safeguards Policy together substantively address them. Neither requires a Required Fix; the Waste Plan itself is the answer.

---

## 5. How to maintain this folder

1. **When ECH changes** (new vendor questionnaire, regulator update): start in `2. Gaps/2.a Gaps Markdown/`. Re-run the section-level analysis. Default to N/A unless ECH explicitly asks for new policy text.
2. **When a real gap appears**: append the smallest possible clause to an *existing* file here. Don't create a new file unless the gap is genuinely orthogonal to every existing policy.
3. **When a policy is materially revised**: edit the file here directly. The diff against `1. Original Docs (Word)/1.a Original Converted to MD/` shows total drift from the original; the per-file git history shows what changed when.
4. **Quarterly / annual review burden** is sized by file count. Keep this folder lean.
