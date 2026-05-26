---
title: "Policy vs. ECH Questionnaire Coverage Matrix"
last_reviewed: 2026-05-24
owner: "Security Officer + Privacy Officer (joint)"
status: "current"
source_questionnaire: "ECH Security Assessment Questions - Questions.csv (182 rows, 7 questionnaires)"
---

# Policy vs. ECH Questionnaire Coverage Matrix

This is the post-consolidation coverage matrix. It **supersedes** the prior version of this document, which was written against the legacy 24-file `New Policy Docs/` layout. The repository now contains **10 thematic policies + 3 reference files** (glossary, platform matrix, patient-notice placeholder) plus the form templates under `New Policy Docs/forms/`. All 182 CSV rows are covered below, mapped against the active files only. Originals are preserved in `New Policy Docs/_archive/` and are not cited here.

Conventions:

- **Coverage rating** is policy-document coverage only (does the org have a written, current policy on this?). Operational state is captured in the CSV `Answer` and `Status` columns.
- **Open Action** means the topic is intentionally tracked as a TODO in [TODO.md](TODO.md) rather than "covered" by a policy clause; the rating distinguishes these from raw `None` gaps.
- **Out-of-scope** = the questionnaire item is N/A to Millie (e.g., PCI for a SAQ-A merchant, ESG for a women's-health clinic) and the assessor will be answered N/A rather than receiving a policy.
- Row numbers reference the CSV (1-indexed; row 1 is the header).
- File paths are relative to the repo root unless prefixed `New Policy Docs/`.
- Section references use the headings as written in each policy (e.g., `§III.2`, `§4.7`); section numbering is per the active file.

---

## §1 — Coverage matrix

### 1.1 AWS Questionnaire (rows 2–33)

| CSV | Q ref | Question (abbrev) | Covering policy + section | Rating | Notes |
|---|---|---|---|---|---|
| 2 | Acct.1 | AWS Organizations used? | `network-and-cloud-security.md` §1; CSV answer No | Partial | Architecture documented (single-account, no Orgs). Decision-of-record; not a remediation TODO. |
| 3 | Acct.2 | Separate accounts Dev/Stg/Prod? | `network-and-cloud-security.md` §1 | Partial | Single AWS account stance documented; no separation requirement codified. |
| 4 | Acct.3 | Dedicated audit/logging account? | `network-and-cloud-security.md` §5 (S3 dedicated backup account = Not in place) | Partial | Single-account posture stated as accepted risk. |
| 5 | Acct.4 | Shared root email alias? | `network-and-cloud-security.md` §2 (Q5) | Full | Documented. |
| 6 | Acct.5 | Root MFA on, no access keys? | `network-and-cloud-security.md` §2 (Q6); `technical-safeguards.md` §III.1.b | Full | Previously Partial; now explicitly stated for the root account. |
| 7 | Acct.6 | Root used in last 7 days? | `network-and-cloud-security.md` §2 (Q7) | Full | Use-case (GuardDuty enablement) documented. |
| 8 | Acct.7 | SCPs in place? | `network-and-cloud-security.md` §1 | Partial | Stated N/A because Orgs not used. |
| 9 | Enc.1 | Encryption at rest for RDS/data stores? | `technical-safeguards.md` §III.2.c (NIST SP 800-111); `network-and-cloud-security.md` §6 | Full | At-rest standard now rescued into technical-safeguards. |
| 10 | Enc.2 | EC2 volume/snapshot encryption? | `technical-safeguards.md` §III.2.c; `network-and-cloud-security.md` §6 | Full | Volume encryption clause + small EC2 footprint statement. |
| 11 | IAM.1 | SAML SSO for IAM? | `network-and-cloud-security.md` §2 (TODO #12) | Open Action | Migration to SSO tracked in TODO #12. |
| 12 | IAM.2 | Console IAM users exist? | `network-and-cloud-security.md` §2; `technical-safeguards.md` §III.1.a | Partial | Acknowledged deviation; tracked TODO #12. |
| 13 | IAM.3 | Programmatic access keys exist? | `network-and-cloud-security.md` §2 (Q13) | Full | Use-case and rotation cadence documented. |
| 14 | IAM.4 | Keys unused >90 days? | `network-and-cloud-security.md` §2 (Q14); TODO #17 | Open Action | One staging key tracked. |
| 15 | IAM.5 | Keys not rotated >90 days? | `network-and-cloud-security.md` §2 (Q15) | Full | 90-day rotation policy stated. |
| 16 | IAM.6 | Roles unused >90 days? | `network-and-cloud-security.md` §2 (Q16); TODO #18 | Open Action | Snowflake-role review tracked. |
| 17 | IAM.7 | Wildcard admin / S3 / IAM access? | `network-and-cloud-security.md` §2 (Q17); `technical-safeguards.md` §III.1.a; TODO #14 | Open Action | Least-privilege principle stated; deviation acknowledged + quarterly review. |
| 18 | IAM.8 | RDS IAM auth? | `network-and-cloud-security.md` §6 | Out-of-scope | N/A — RDS reached through Aptible integration. |
| 19 | IAM.9 | Secrets Manager / SSM in use? | `network-and-cloud-security.md` §3 | Partial | Aptible env vars + 1Password documented as approved stores; AWS-native stores noted as future-state. |
| 20 | Net.1 | SGs restrict non-HTTP inbound? | `network-and-cloud-security.md` §4 (Q20) | Full | |
| 21 | Net.2 | Private subnets? | `network-and-cloud-security.md` §4 (Q21); TODO #15 | Open Action | Public route table residue tracked. |
| 22 | Net.3 | RDS in private subnets? | `network-and-cloud-security.md` §4 (Q22) | Full | |
| 23 | Net.4 | Outbound SGs per VPC? | `network-and-cloud-security.md` §4 (Q23) | Full | |
| 24 | Net.5 | Open S3 buckets? | `network-and-cloud-security.md` §5 (Q24) | Full | No buckets open / no any-authenticated grants. |
| 25 | Net.6 | S3 block public access enabled? | `network-and-cloud-security.md` §5 (Q25) | Full | |
| 26 | Det.1 | AWS Config in all regions? | `network-and-cloud-security.md` §7 (Q26); TODO #16 | Open Action | Accepted risk pending assessor feedback. |
| 27 | Det.2 | CloudTrail data events on S3? | `network-and-cloud-security.md` §5 (Q27); §7 | Full | |
| 28 | Det.3 | GuardDuty / IDS enabled? | `network-and-cloud-security.md` §7 (Q28) | Full | |
| 29 | Proc.1 | IaC (Terraform/CFN)? | `network-and-cloud-security.md` §12; `sdlc-and-asset-lifecycle.md` §6.1 | Full | Terraform standard stated. |
| 30 | Proc.2 | Custom AMIs maintained via pipeline? | none | Out-of-scope | Millie does not maintain custom AMIs (Aptible-managed compute). Answer N/A to assessor; no policy needed. |
| 31 | Proc.3 | AWS-specific IR plan tested? | `incident-and-breach-response.md` §III.3 (AWS/cloud playbook); `network-and-cloud-security.md` §13–14 | Full | AWS playbook pointer + DR/IR cadence. Pre-existing `AWS and Aptible Security Incident Management Policy.docx` not yet integrated — TODO. |
| 32 | Proc.4 | Backups in dedicated AWS acct? | `network-and-cloud-security.md` §5 (Q32); `operational-safeguards.md` §4.7 | Partial | Single-account posture documented as accepted risk; multi-vendor resiliency clause covers backup vendor concentration. |
| 33 | Proc.5 | Secure remote access to servers/DBs? | `technical-safeguards.md` §III.4 (Remote Access); `network-and-cloud-security.md` (whole) | Full | |

### 1.2 ISD IT Risk Assessment (rows 34–71)

Project-intake questionnaire — most rows are project-context fields completed at intake. Rated `Out-of-scope` where no policy is expected.

| CSV | Q ref | Question (abbrev) | Covering policy + section | Rating | Notes |
|---|---|---|---|---|---|
| 34–41 | Req.1–8 | Project context (objective, end-user, conversion, archive, training) | `sdlc-and-asset-lifecycle.md` §1 (Planning & Acquisition) | Out-of-scope | Project intake form, not a policy gap. Planning section covers the umbrella. |
| 42 | Svr.1 | Server infrastructure type? | `network-and-cloud-security.md` §1 | Full | Architecture overview answers this. |
| 43 | Net.1 | New port required? | `sdlc-and-asset-lifecycle.md` §5 (Change Management); `network-and-cloud-security.md` §4 | Full | Change-mgmt process now exists; covered. |
| 44 | Net.2 | New WAN circuit? | `network-and-cloud-security.md` §1 | Out-of-scope | Cloud-native; no WAN circuits. |
| 45 | Net.3 | Site-to-site VPN? | `technical-safeguards.md` §III.4 (Remote Access) | Partial | Policy covers user remote access via VPN; no site-to-site VPN in current architecture. |
| 46 | IAM.1 | Authentication method? | `technical-safeguards.md` §III.1; `network-and-cloud-security.md` §2 | Full | |
| 47 | IAM.2 | MFA available? | `technical-safeguards.md` §III.1.b; `governance-and-risk-management.md` §III.1.b | Full | |
| 48 | IAM.3 | Vendor remote access? | `technical-safeguards.md` §III.4; `vendor-and-business-associates.md` §5 | Full | |
| 49 | Cyb.1 | Internet-accessible? | `network-and-cloud-security.md` §1 | Full | |
| 50 | Cyb.2 | AV/security exclusions? | `acceptable-use-and-byod.md` §III.B.3 (anti-malware required); `technical-safeguards.md` §III.4.b (up-to-date AV) | Partial | Anti-malware standard stated; no formal "exclusions" policy. |
| 51 | Cyb.3 | Vuln-scan exclusions? | `sdlc-and-asset-lifecycle.md` §6.3 | Partial | Scope of scanning defined; "exclusions" not enumerated. |
| 52 | Cyb.4 | Vendor doing vuln scan/remediation? | `vendor-and-business-associates.md` §4.2; `sdlc-and-asset-lifecycle.md` §6.3 | Full | Dependency scanning + vendor patch SLA. |
| 53 | Cyb.5 | Transactional emails? | `acceptable-use-and-byod.md` §III.A.2; `phi-use-and-disclosure.md` §6 (Marketing) | Partial | Email standards exist; transactional-email infra (Sendgrid) listed in platform matrix. |
| 54 | Cyb.6 | Dedicated host/IP vs shared? | none | Out-of-scope | Operational config; assessor answered from platform matrix (Sendgrid/Twilio). |
| 55 | Cyb.7 | DMARC configured? | none | Open Action | Not addressed in any policy; suggest adding a TODO for email-auth standards. |
| 56 | Int.1 | API/interface changes? | `sdlc-and-asset-lifecycle.md` §5 (Change Management) | Full | |
| 57–63 | EUC.1–7 | End-user compute | `acceptable-use-and-byod.md` (whole); `technical-safeguards.md` §III.3 (Workstation Use) | Full | AUP + BYOD + Workstation Use now cover the EUC questions. |
| 64 | CE.1 | IoMT? | none | Out-of-scope | Not applicable to Millie. |
| 65 | Tel.1 | Telecom? | `operational-safeguards.md` §III.1.3 (telephone protocols) | Partial | Voice/voicemail protocols only; no broader telecom standard. |
| 66–68 | TE.1–3 | Timeline | none | Out-of-scope | Project intake. |
| 69 | VS.1 | Existing ECH engagements? | none | Out-of-scope | Project intake. |
| 70–71 | Oth.1–2 | Outstanding issues / resolution | none | Out-of-scope | Project intake. |

### 1.3 OWASP Top 10 (rows 72–81)

| CSV | Q ref | Question (abbrev) | Covering policy + section | Rating | Notes |
|---|---|---|---|---|---|
| 72 | A01 | Access control enforcement | `technical-safeguards.md` §III.1 (Access Control); `governance-and-risk-management.md` §III.1.b | Full | RBAC, least privilege, unique IDs, MFA. |
| 73 | A02 | Sensitive data extra protection | `technical-safeguards.md` §III.2.c (at-rest); §III.2.d (password storage hashing — argon2id/bcrypt) | Full | Previously Partial; now Full. Operational implementation tracked in TODO #1 (Critical). |
| 74 | A03 | Injection defenses | `sdlc-and-asset-lifecycle.md` §2.1 (Secure Coding Standard — OWASP ASVS; parameterized queries) | Full | |
| 75 | A04 | Secure SDLC w/ AppSec | `sdlc-and-asset-lifecycle.md` §2.2 (AppSec Role); §2 generally | Full | AppSec role formalized; TODO #6 covers any expansion decision. |
| 76 | A05 | Hardening process | `network-and-cloud-security.md` §11 (Hardening Baseline); `technical-safeguards.md` §III.1.h (default-creds) | Full | CIS Benchmarks referenced; hardened base images. |
| 77 | A06 | Vuln scanning / patch mgmt | `sdlc-and-asset-lifecycle.md` §6.2 (Patch SLA Critical=7d/High=30d); §6.3 (Scanning); `network-and-cloud-security.md` §9 | Full | Policy in place; GitHub upgrade operational item tracked in TODO #2 (Critical). |
| 78 | A07 | Auth / session token protection | `technical-safeguards.md` §III.1.g (Session & Token Management) | Full | Previously Partial; now Full. Operational implementation tracked in TODO #3 (Critical). |
| 79 | A08 | Code & infra integrity | `sdlc-and-asset-lifecycle.md` §2.3 (Code Integrity & Signed Artifacts); §6.1 (IaC) | Full | |
| 80 | A09 | Logging/monitoring failures | `technical-safeguards.md` §III.7 (Logging, Monitoring & Alert Cadence); `network-and-cloud-security.md` §7 | Full | Operational fine-tuning tracked in TODO #7 (High). |
| 81 | A10 | SSRF defenses | `network-and-cloud-security.md` §10 (SSRF & Outbound Network Defenses) | Full | Operational hardening tracked in TODO #8 (High). |

### 1.4 PCI DSS Assessment Form (rows 82–91)

Millie does not process, store, or transmit cardholder data — payment processing is outsourced. Answer the whole questionnaire as "Out-of-scope per SAQ-A" rather than authoring PCI policies.

| CSV | Q ref | Question (abbrev) | Covering policy + section | Rating | Notes |
|---|---|---|---|---|---|
| 82 | Gen.1 | Process/store/transmit card data? | none | Out-of-scope | Assessor answer: No (SAQ-A merchant; payments outsourced). Verify with Finance. |
| 83 | Gen.2 | PCI DSS assessment in 12 mo? | none | Out-of-scope | N/A (SAQ-A). |
| 84 | Gen.3 | Passing grade? | none | Out-of-scope | N/A (SAQ-A). |
| 85 | Gen.4 | Card data encrypted? | none | Out-of-scope | N/A; no card data stored. |
| 86 | Gen.5 | Restricted access to card data? | none | Out-of-scope | N/A. |
| 87 | Gen.6 | Access control to card data? | none | Out-of-scope | N/A. |
| 88 | Gen.7 | Patches up to date? | `sdlc-and-asset-lifecycle.md` §6.2 (Patch SLA) | Full | Not PCI-scoped but the patch SLA does cover Company systems. |
| 89 | Gen.8 | Firewall? | `network-and-cloud-security.md` §4 (Cloudflare WAF + cloud SGs) | Full | Cloud-native firewalling documented. |
| 90 | Gen.9 | Periodic password changes? | `technical-safeguards.md` §III.1 (no forced rotation; NIST 800-63B aligned) | Partial | Intentional policy choice; documented but does not match PCI's periodic-rotation expectation. |
| 91 | Gen.10 | Complex & unique passwords | `technical-safeguards.md` §III.1.c | Full | |

### 1.5 SIG Lite 2025 (rows 92–180)

| CSV | Q ref | Question (abbrev) | Covering policy + section | Rating | Notes |
|---|---|---|---|---|---|
| 92 | A.1 | ERM policy | `governance-and-risk-management.md` §III.3 (Enterprise Risk Management) | Full | Previously None; ERM framing now explicit. |
| 93 | B.1 | TPRM incl 4th/Nth parties | `vendor-and-business-associates.md` §1; §3 | Full | Previously Partial. |
| 94 | B.2 | Contractual flow-down to subs | `vendor-and-business-associates.md` §3 | Full | |
| 95 | C.1 | Cyber risk mgmt policy | `governance-and-risk-management.md` (whole) | Full | |
| 96 | C.4 | Risk assessment process | `governance-and-risk-management.md` §III.4 | Full | |
| 97 | D.1 | Asset mgmt program | `technical-safeguards.md` §III.5 (Device & Media — IT-004 rescued); `network-and-cloud-security.md` §11 | Full | Previously Partial (buried in privacy-policy). |
| 98 | D.2 | Acceptable Use Policy | `acceptable-use-and-byod.md` §III.A | Full | Previously Partial; new file closes the gap. |
| 99 | D.3 | Records retention schedule | `governance-and-risk-management.md` §III.6 (Records Retention Schedule table) | Full | Previously Partial; schedule by record type now in place. Email retention still "TBD". |
| 100 | E.1 | HR policies | `governance-and-risk-management.md` §III.7 (HR Security and Sanctions Anchor) | Partial | Anchor section + canonical sanctions clause; standalone HR security policies still under development per §III.7. |
| 101 | E.3 | Employee performance process | none | Out-of-scope | HR operational; not a security-repo policy. |
| 102 | F.1 | Physical security program | `operational-safeguards.md` §III.2 | Full | CSV task owner Terese — facility-specific implementation tracked separately. |
| 103 | G.1 | IT Ops policies aligned | `governance-and-risk-management.md` §III.1; `network-and-cloud-security.md` (whole); `sdlc-and-asset-lifecycle.md` (whole) | Full | |
| 104 | G.2 | Change Management policy | `sdlc-and-asset-lifecycle.md` §5 (Change Management) | Full | Previously None. |
| 105 | G.3 | Security req's for new systems | `sdlc-and-asset-lifecycle.md` §1, §2, §3 | Full | |
| 106 | H.1 | Access Control policy | `technical-safeguards.md` §III.1; `governance-and-risk-management.md` §III.1.b | Full | |
| 107 | H.2 | Password policy approved | `technical-safeguards.md` §III.1.c–g (construction, mobile passcodes, lockout, sessions, storage) | Full | |
| 108 | I.1 | Apps process scoped data | n/a | Out-of-scope | Affirmative question; no policy needed. |
| 109 | I.2 | App development performed | `sdlc-and-asset-lifecycle.md` (whole) | Full | |
| 110 | I.3 | Web site/app hosted | n/a | Out-of-scope | Affirmative question. |
| 111 | J.1 | Cybersecurity IR program | `incident-and-breach-response.md` (whole) | Full | |
| 112 | J.4 | IR plan w/ escalation | `incident-and-breach-response.md` §III.1, §III.2 (severity tiers) | Full | |
| 113 | J.5 | Event review methodology | `technical-safeguards.md` §III.7 (cadence + thresholds); `network-and-cloud-security.md` §7 | Full | Previously Partial. |
| 114 | J.11 | Outsourced IR (MSSP) | `incident-and-breach-response.md` §III.6 | Full | Explicit "no MSSP" statement now on the record. |
| 115 | J.14 | Incident docs tamper-protected | `incident-and-breach-response.md` §III.4 (Tamper-Evident Incident Log) | Full | Previously Partial. |
| 116 | K.1 | Business Resilience policy | `operational-safeguards.md` §III.4 (Contingency Planning) | Full | |
| 117 | K.2 | DR exercise/testing program | `operational-safeguards.md` §III.4.6 (DR Testing Program) | Full | Cadence + last-test-date tracking. Operational test execution tracked in TODO #9 (High). |
| 118 | K.3 | Critical 3P dependencies? | n/a | Out-of-scope | Affirmative question. |
| 119 | K.4 | Pandemic plan? | `operational-safeguards.md` Appendix A (Pandemic/Infectious Disease Plan, with A.9 = active COVID-19 implementation) | Full | Previously None. CSV-marked NO is now superseded. Staff-guidance sub-gap tracked in TODO Other Outstanding Follow-ups. |
| 120 | K.5 | Offsite backups? | `operational-safeguards.md` §III.4.2 | Full | |
| 121 | K.6 | Operational risk assessment | `governance-and-risk-management.md` §III.3 (ERM) + §III.4 | Full | Previously Partial; ERM scope extends beyond HIPAA. |
| 122 | K.7 | BCP procedures | `operational-safeguards.md` §III.4 (4.4 DR procedures; 4.5 Emergency Operations) | Full | |
| 123 | K.11 | Data retention policy/schedule | `governance-and-risk-management.md` §III.6 | Full | Same source as D.3 row 99. |
| 124 | K.30 | Multi-vendor resiliency | `operational-safeguards.md` §III.4.7 (Multi-Vendor Resiliency and Single-Vendor Risk Acceptance) | Full | Previously None. Risk-acceptance documented for Aptible/AWS/Cloudflare. |
| 125 | L.1 | Regulatory compliance procedures | `governance-and-risk-management.md` §III.1, §III.9 (Compliance & Ethics) | Full | |
| 126 | L.2 | Customer-facing website | n/a | Out-of-scope | Affirmative question. |
| 127 | L.3 | Antitrust policy | none | Out-of-scope | N/A for Millie. |
| 128 | L.4 | Compliance & ethics program | `governance-and-risk-management.md` §III.9 | Partial | Pointer/anchor exists; standalone Code of Conduct flagged TBD within §III.9. |
| 129 | L.5 | Cyber compliance procedures | `governance-and-risk-management.md` (whole); `incident-and-breach-response.md` §III.7 | Full | |
| 130 | L.6 | Fraud detection/prevention | `governance-and-risk-management.md` §III.9 (fraud reporting channel) | Partial | Channel exists; no standalone fraud-prevention program documented. |
| 131 | M.1 | Endpoints handle scoped data | n/a | Out-of-scope | Affirmative question. |
| 132 | M.1.3 | MDM program | `acceptable-use-and-byod.md` §III.C (MDM) | Full | Previously None. MDM vendor selection tracked in TODO #4 (Critical). |
| 133 | M.1.5 | Non-company devices on network | `acceptable-use-and-byod.md` §III.B (BYOD) | Full | Previously Partial. |
| 134 | M.1.6 | BYOD mobile w/ scoped data | `acceptable-use-and-byod.md` §III.B; §III.D (Personal-vs-Company separation); §III.E (Lost/Stolen) | Full | Previously Partial. |
| 135 | M.3 | (blank) | n/a | Out-of-scope | CSV row empty. |
| 136 | N.1 | Secure network build | `network-and-cloud-security.md` (whole) | Full | Previously Partial. |
| 137 | N.2 | Network Security Program | `network-and-cloud-security.md` (whole) | Full | Previously None. |
| 138 | N.3 | External connections terminate at firewall | `network-and-cloud-security.md` §4 (Cloudflare + cloud SGs) | Full | Previously None. |
| 139 | N.4 | Network device patching | `network-and-cloud-security.md` §8, §9; `sdlc-and-asset-lifecycle.md` §6.2 | Full | Previously None. |
| 140 | N.5 | Remote access policy approved | `technical-safeguards.md` §III.4 | Full | |
| 141 | N.7 | NIDS/NIPS | `network-and-cloud-security.md` §7 (GuardDuty stance) | Full | Previously None. |
| 142 | N.8 | DMZ environment | `network-and-cloud-security.md` §4 (cloud-native DMZ equivalent) | Full | Previously None. |
| 143 | N.9 | Wireless policy | `network-and-cloud-security.md` §8 (Wireless) | Full | Previously None. |
| 144 | N.11 | Network device baselines | `network-and-cloud-security.md` §8, §11 | Full | Previously None. |
| 145 | N.12 | Default passwords changed | `technical-safeguards.md` §III.1.h; `network-and-cloud-security.md` §8 | Full | Previously Partial. |
| 146–158 | O.1–13 | ESG: env, hazards, biodiversity, modern slavery, ethics, H&S, community, DEI | none | Out-of-scope | Per CONSOLIDATION §7.4: answer "Not formally documented." |
| 159 | O.14 | Ethical sourcing | none | Out-of-scope | Same as 146–158. |
| 160 | P.1 | PII collection | n/a | Out-of-scope | Affirmative question. |
| 161 | P.2 | PII privacy policy (NPP) | `New Policy Docs/PATIENT-NOTICE-TODO.md` | Open Action | Patient-facing NPP still TBD. Internal `phi-use-and-disclosure.md` exists but is NOT a §164.520 NPP. |
| 162 | P.3 | Formal privacy program | `phi-use-and-disclosure.md` (whole); `patient-rights.md` (whole); `governance-and-risk-management.md` | Full | |
| 163 | P.4 | Privacy training program | `governance-and-risk-management.md` §IV (canonical Training & Awareness Program) | Full | |
| 164 | P.5 | Minimum necessary / need-to-know | `phi-use-and-disclosure.md` §III.1 | Full | |
| 165 | P.6 | Internet-facing app collecting client data | n/a | Out-of-scope | Affirmative question. |
| 166 | P.8 | Data governance program | `governance-and-risk-management.md` (whole) | Full | |
| 167 | P.9 | Privacy incident detection/reporting (GLBA) | `incident-and-breach-response.md` (whole) | Partial | HIPAA breach covered; GLBA is N/A for Millie (not a financial institution). |
| 168 | P.10 | 4th/Nth-party access | `vendor-and-business-associates.md` §3 | Full | |
| 169 | P.11 | Privacy role w/ accountability | `governance-and-risk-management.md` §III.2.a (Privacy Officer); `hipaa-definitions.md` | Full | |
| 170 | P.12 | Registration info accuracy | none | Out-of-scope | Likely N/A (terminology aligns with EU regulatory authority registration). |
| 171 | R.1 | AI legal/regulatory awareness | `ai-and-ml-governance.md` §III.a; §VI (references HHS OCR AI guidance) | Full | Previously None. |
| 172 | R.2 | Trustworthy AI characteristics | `ai-and-ml-governance.md` §III.c (clinical AI), §III.f (prohibited uses), §III.g (transparency) | Full | Previously None. |
| 173 | R.4 | AI risk mgmt review | `ai-and-ml-governance.md` §III.e (review cadence — quarterly + annual) | Full | Previously None. |
| 174 | R.5 | AI system inventory policy | `ai-and-ml-governance.md` §III.a, §III.e; `platform-and-access-matrix.md` (AI Platforms section) | Full | Previously None. |
| 175 | S.1 | Supplier access control flow-down | `vendor-and-business-associates.md` §3, §4 | Full | Previously Partial. |
| 176 | S.32 | C-SCRM policy | `vendor-and-business-associates.md` §4 (C-SCRM) | Full | Previously None. |
| 177 | S.57 | Media protection in SDLC supply chain | `vendor-and-business-associates.md` §4.1, §4.3 (SBOM); `sdlc-and-asset-lifecycle.md` §7 (NIST SP 800-88) | Full | Previously Partial. |
| 178 | S.61 | C-SCRM integrated in security planning | `vendor-and-business-associates.md` §4; `governance-and-risk-management.md` §III.1.i | Full | Previously None. |
| 179 | S.80 | Personnel responsibilities for SCRM | `vendor-and-business-associates.md` §4 (Security Officer owns C-SCRM); §III.7 in Governance | Full | Previously None. |
| 180 | S.100 | System/comms protection in SCRM | `vendor-and-business-associates.md` §4; `network-and-cloud-security.md` (whole) | Full | Previously None. |

### 1.6 Insurances (row 181)

| CSV | Q ref | Question (abbrev) | Covering policy + section | Rating | Notes |
|---|---|---|---|---|---|
| 181 | Ins.1 | Cyber Liability / Data Privacy doc | `governance-and-risk-management.md` §III.8 (Assurance Program — cyber liability); `incident-and-breach-response.md` §III.7.4; `operational-safeguards.md` §III.4.4 | Partial | Policies reference carrier; the actual insurance certificate must still be attached to the ECH submission as evidence (no policy clause can supply that). |

### 1.7 Security Audits (rows 182–183)

| CSV | Q ref | Question (abbrev) | Covering policy + section | Rating | Notes |
|---|---|---|---|---|---|
| 182 | Aud.1 | Penetration Testing doc | `governance-and-risk-management.md` §III.8 (annual external pentest commitment) | Partial | Policy commits to annual pentest; actual report must be in `assurance/` folder before submission. |
| 183 | Aud.2 | General Security Audit doc | `governance-and-risk-management.md` §III.8 (internal audit + SOC 2/HITRUST stance TBD) | Partial | SOC 2/HITRUST status documented as TBD; internal control assessment cadence stated. |

---

## §2 — Coverage summary

### 2.1 Overall counts (182 rows)

| Rating | Count | % |
|---|---|---|
| Full | 104 | 57% |
| Partial | 20 | 11% |
| None | 0 | 0% |
| Open Action (tracked in TODO.md / PATIENT-NOTICE-TODO.md) | 8 | 4% |
| Out-of-scope | 50 | 28% |
| **Total** | **182** | **100%** |

No rows are rated `None`. The closest things to an unaddressed gap are: **CSV row 55 (DMARC configured)** — rated `Open Action` here because no current policy addresses it, but it is not yet in TODO.md and should be added; and the operational follow-ups already enumerated in TODO.md (rows 73, 77, 78, 132–134, etc., which are policy-Full but operationally open).

### 2.2 Per-questionnaire breakdown

| Questionnaire | Rows | Full | Partial | None | Open Action | Out-of-scope |
|---|---|---|---|---|---|---|
| AWS Questionnaire | 32 (rows 2–33) | 19 | 7 | 0 | 5 | 1 |
| ISD IT Risk Assessment | 38 (rows 34–71) | 13 | 4 | 0 | 1 | 20 |
| OWASP Top 10 | 10 (rows 72–81) | 10 | 0 | 0 | 0 | 0 |
| PCI DSS | 10 (rows 82–91) | 2 | 1 | 0 | 0 | 7 |
| SIG Lite 2025 | 89 (rows 92–180) | 67 | 6 | 0 | 3 | 13 |
| Insurances | 1 (row 181) | 0 | 1 | 0 | 0 | 0 |
| Security Audits | 2 (rows 182–183) | 0 | 2 | 0 | 0 | 0 |
| Wireless/Misc | (none) | | | | | |

### 2.3 Movement vs the prior mapping

The previous mapping was authored against the 24-file pre-consolidation layout. Net swings on this pass (selected highlights):

- **AWS Questionnaire** — 7 rows promoted from Partial/None to Full (Q5, Q6, Q9, Q10, Q20, Q22–25), the rest absorbed into the new `network-and-cloud-security.md`.
- **SIG Lite §N (Network Security)** — every previously-None row (N.1, N.2, N.3, N.7, N.8, N.9, N.11) is now Full via `network-and-cloud-security.md`.
- **SIG Lite §M (Endpoint Security)** — M.1.3 / M.1.5 / M.1.6 (the Critical BYOD/MDM gaps) moved from None/Partial to Full via `acceptable-use-and-byod.md`. Operational MDM vendor selection still tracked in TODO #4.
- **SIG Lite §R (Artificial Intelligence)** — all four rows (R.1, R.2, R.4, R.5) moved from None to Full via `ai-and-ml-governance.md`.
- **SIG Lite §S (Supply Chain)** — all six rows (S.1, S.32, S.57, S.61, S.80, S.100) moved from None/Partial to Full via `vendor-and-business-associates.md` §4.
- **SIG K.2/K.4/K.30** — DR testing program, pandemic plan, and multi-vendor resiliency moved from None to Full in `operational-safeguards.md` §III.4.6–4.8 + Appendix A.
- **OWASP A02/A07** (both `Remediate=Yes`) moved from Partial to Full via `technical-safeguards.md` §III.1.g (sessions/tokens) and §III.2.d (password hashing).
- **NPP (P.2)** remains an Open Action; the rest of the patient-rights row set (P.3, P.4, P.5) is Full.

---

## §3 — Remaining gaps

Listed below in severity order. A "gap" here means anything not rated Full *and* not Out-of-scope.

| Sev | CSV row(s) | Item | Recommended next step |
|---|---|---|---|
| Critical | 73 | OWASP A02 — operational password-storage implementation | Policy is Full. Engineering must confirm production hashes meet `technical-safeguards.md` §III.2.d (argon2id/bcrypt + 16-byte salt + work factor ≥250 ms). Tracked in TODO #1. |
| Critical | 77 | OWASP A06 — operational patch backlog / GitHub upgrade | Policy is Full. Complete GitHub plan upgrade; confirm patch-SLA compliance for current open CVEs. Tracked in TODO #2. |
| Critical | 78 | OWASP A07 — operational session/token implementation | Policy is Full. Engineering must confirm session expiry, refresh-token rotation, logout-on-password-change against `technical-safeguards.md` §III.1.g. Tracked in TODO #3. |
| Critical | 132–134 | MDM vendor selection + BYOD enrollment rollout | Policy is Full. Select MDM vendor and run the enrollment process documented in `acceptable-use-and-byod.md` §III.C.3. Tracked in TODO #4 and #5. |
| High | 117 | DR test execution | Policy is Full. Execute the annual end-to-end DR exercise and capture last-test-date per `operational-safeguards.md` §III.4.6. Tracked in TODO #9. |
| High | 100 | Standalone HR security policies | Policy anchor exists in `governance-and-risk-management.md` §III.7. Author standalone background-check / NDA / full sanctions-schedule policies when bandwidth allows. |
| High | 161 | Patient-facing Notice of Privacy Practices (NPP) | Tracked in `New Policy Docs/PATIENT-NOTICE-TODO.md`. Draft a real §164.520 NPP; ensure intake-packet, posted, and website distribution. |
| High | 80 | OWASP A09 — log review tuning | Policy is Full. Tune log review cadence + alert thresholds per `technical-safeguards.md` §III.7. TODO #7. |
| High | 81 | OWASP A10 — SSRF operational hardening | Policy is Full. Implement IMDSv2-only + URL allowlisting per `network-and-cloud-security.md` §10. TODO #8. |
| High | 182, 183 | Pentest report + general security-audit attestation | Policy commits in `governance-and-risk-management.md` §III.8. Procure annual pentest + decide on SOC 2/HITRUST direction; attach reports to ECH submission. |
| Medium | 128 | Code of Conduct | Pointer exists in `governance-and-risk-management.md` §III.9; full Code of Conduct still TBD per §VII Definitions. |
| Medium | 130 | Standalone fraud-prevention program | Reporting channel exists in §III.9; standalone program not documented. |
| Medium | 181 | Cyber liability certificate evidence | Policy references exist; certificate must be attached to the ECH submission package (cannot be supplied by policy text). |
| Medium | 99 | Records retention — Email row TBD | `governance-and-risk-management.md` §III.6 table marks Email as "TBD". Decide retention period and update. |
| Medium | 55 | DMARC configured (email auth) | Not addressed in any policy. Add an email-auth standards row to `network-and-cloud-security.md` §1 or to a future "Email Security" subsection; verify operational DMARC posture. |
| Medium | 100, 124 | Multi-vendor resiliency — periodic review of risk acceptance | `operational-safeguards.md` §III.4.7 commits to annual review by Risk Review Committee. Ensure first review is scheduled. |
| Medium | 21, 26 | AWS Config + public-subnet residue | TODOs #15, #16 cover the operational remediation; assessor-facing answer is "accepted risk." |
| Low | 11, 12, 13, 14, 16, 17 | AWS IAM judgment calls (console users, programmatic keys, unused keys/roles, wildcard admin) | Operational items per TODO §🟡 Operational. Each is acknowledged in `network-and-cloud-security.md` §2 and accepted; no policy change required. |
| Low | 65 | Telecom requirements scope | `operational-safeguards.md` §III.1.3 covers patient telephony; no broader policy needed at Millie's size. |
| Low | 50, 51 | AV/security exclusions, vuln-scan exclusions | Partial — exclusions are typically defined operationally per ticket. No policy change required unless the assessor pushes back. |
| Info | 167 (P.9 GLBA) | GLBA scope | Out-of-scope for Millie (not a financial institution); answer N/A. |

---

## §4 — Delivery verification vs CONSOLIDATION-PROPOSAL §7

CONSOLIDATION-PROPOSAL §7.2 promised specific content additions to specific consolidated files. Each promised item is verified below against the active file.

### 4.1 To `acceptable-use-and-byod.md` (NEW)

| §7.2 promise | Where landed | Delivered? |
|---|---|---|
| MDM section addressing rows 132–134 | §III.C (full MDM section with vendor TBD, capabilities, enrollment, privacy notice, work container) | ✅ Yes |
| AI Use clause (SIG R.1/R.2/R.5 minimum viable) | §III.A.5 (prohibits PHI to unapproved AI/LLM); full AI policy authored separately as `ai-and-ml-governance.md` | ✅ Yes — and exceeded scope (separate AI policy) |
| Acceptable use (internet, email, social, personal use, prohibited, sanctions) | §III.A.1 through §III.A.7 | ✅ Yes |

### 4.2 To `technical-safeguards.md`

| §7.2 promise | Where landed | Delivered? |
|---|---|---|
| Session & token management subsection (OWASP A07) | §III.1.g | ✅ Yes |
| Password storage / app secret hashing standard (OWASP A02) | §III.2.d | ✅ Yes |
| Default-password change requirement (SIG N.12) | §III.1.h | ✅ Yes |
| Logging/alerting cadence (OWASP A09 / SIG J.5) — new §8 | Landed as §III.7 ("Logging, Monitoring & Alert Cadence") — numbering different than §7.2 said but content delivered | ✅ Yes |

### 4.3 To `network-and-cloud-security.md` (NEW)

| §7.2 promise | Where landed | Delivered? |
|---|---|---|
| All AWS Questionnaire policy-relevant items (rows 2–33) | §§1–7, 12, 13, 14, 15 (per-row Q-refs cited) | ✅ Yes |
| SIG N.1, N.2, N.3, N.4, N.7, N.8, N.11, N.12 | §§4, 7, 8, 9, 11 | ✅ Yes |
| Wireless policy section (N.9) | §8 | ✅ Yes |
| Hardening baseline reference (OWASP A05) | §11 | ✅ Yes |
| Patch SLA for network devices (OWASP A06 / SIG N.4) | §9 | ✅ Yes (also duplicated in `sdlc-and-asset-lifecycle.md` §6.2 — consistent) |
| SSRF defenses (OWASP A10) | §10 | ✅ Yes |

### 4.4 To `operational-safeguards.md` §5 (Contingency Planning)

> Note: §7.2 references "§5 Contingency Planning"; the active file renumbers this as **§III.4**. Content delivered there.

| §7.2 promise | Where landed | Delivered? |
|---|---|---|
| Pandemic / infectious disease appendix (SIG K.4) | Appendix A — full plan, including activation criteria, remote work, communication chain, return-to-office; A.9 = active COVID-19 implementation | ✅ Yes |
| DR testing program subsection (SIG K.2) | §III.4.6 (annual end-to-end + monthly restore-test) | ✅ Yes |
| Multi-vendor resiliency / single-vendor risk acceptance (SIG K.30) | §III.4.7 (Aptible/AWS/Cloudflare inventory + accepted-risk + monitoring + exit considerations) | ✅ Yes |

### 4.5 To `governance-and-risk-management.md`

| §7.2 promise | Where landed | Delivered? |
|---|---|---|
| Records Retention schedule (SIG D.3 / K.11) | §III.6 (full table by record type) | ✅ Yes — Email row marked "TBD" |
| Enterprise Risk Management framing (SIG A.1) | §III.3 | ✅ Yes |
| HR security pointer + sanctions clause (SIG E.1 + CONSOLIDATION §5c) | §III.7 (anchor) + §V (canonical Sanctions clause) | ✅ Yes |
| Assurance Program section (rows 182, 183 + Insurance row 181) | §III.8 (pentest, internal audit, SOC 2/HITRUST stance TBD, cyber insurance) | ✅ Yes |
| Compliance & ethics / fraud prevention pointer (SIG L.4 / L.6) | §III.9 (Code of Conduct TBD, whistleblower channel, fraud reporting channel) | ✅ Yes |
| Sanctions clause closing 45 CFR §164.530(e) gap | §V | ✅ Yes |
| Canonical Training & Awareness Program | §IV | ✅ Yes (referenced from every other policy) |

### 4.6 To `vendor-and-business-associates.md`

| §7.2 promise | Where landed | Delivered? |
|---|---|---|
| C-SCRM section (SIG S.32/S.57/S.61/S.80/S.100) | §4 (Cybersecurity Supply Chain Risk Management, with SBOM + dependency vulnerability mgmt + assurance-cadence table) | ✅ Yes |
| Nth-party flow-down language migrated verbatim | §3 (full Subcontractor and Nth-Party Flow-Down Requirements section) | ✅ Yes |

### 4.7 To `sdlc-and-asset-lifecycle.md`

| §7.2 promise | Where landed | Delivered? |
|---|---|---|
| Change Management subsection (SIG G.2) | §5 (Change Management with Standard/Normal/Emergency categories, artifacts, audit trail) | ✅ Yes |
| Patch management SLA — Critical=7d / High=30d (OWASP A06 / SIG N.4) | §6.2 (full SLA table) | ✅ Yes |
| Code integrity / signed artifacts (OWASP A08) | §2.3 | ✅ Yes |
| Secure coding standard pointer (OWASP A03/A04/A10) | §2.1 (OWASP ASVS) + §2.2 (AppSec Role) | ✅ Yes |
| Fix the SDLC header bug (was mis-stamped IT-026) | Source quote in header section + Revision history correction; Policy # restored to IT-009 | ✅ Yes |

### 4.8 To `incident-and-breach-response.md`

| §7.2 promise | Where landed | Delivered? |
|---|---|---|
| Tamper-evident incident log (SIG J.14) | §III.4 | ✅ Yes |
| MSSP / outsourced IR statement (SIG J.11) | §III.6 | ✅ Yes |
| AWS-specific incident playbook pointer | §III.3 (cross-reference to `network-and-cloud-security.md`) | ✅ Yes |

### 4.9 Cuts promised in CONSOLIDATION §7.3

| §7.3 promise | Verified in current file |
|---|---|
| Collapse 8 L-002 disclosure-permission subsections to a single paragraph | `phi-use-and-disclosure.md` §III.2.4 (single Privacy-Officer-approval paragraph) ✅ |
| Foreign-country encryption export controls (cut) | Not present in `technical-safeguards.md` §III.2 ✅ |
| Per-page paper-copy fee supply itemization (cut to flat fee) | `patient-rights.md` §III.1.7 — flat $6.50 + "no patient denied for inability to pay" ✅ |
| Breach notification fill-in-the-blank forms (move to `forms/`) | `New Policy Docs/forms/breach-notification-{individual-letter,media-template,hhs-template}.md` ✅ |
| Information Blocking Compliance Policy cross-references (inline EHI def, drop refs) | `patient-rights.md` §VII inlines EHI; original broken refs gone ✅ |

### 4.10 Promised-but-not-delivered

None found in §7.2 or §7.3. **All content additions and cuts called out in CONSOLIDATION §7 appear in the active files.** Caveats:

- The Records Retention Schedule has an explicit "TBD — policy under development" entry for Email retention. Delivered as a row, but the value is incomplete.
- MDM vendor selection in `acceptable-use-and-byod.md` §III.C.1 is marked "TBD pending vendor selection." Policy is delivered; operational vendor choice is not.
- Code of Conduct location (governance §III.9) is marked "TBD — under development."
- SOC 2 / HITRUST direction in governance §III.8 is "under evaluation."

These are flagged in §3 above and tracked in TODO.md where appropriate.

---

## §5 — Net new findings since the prior mapping

### 5.1 Substantive coverage changes

| Area | Prior status | Now | Notes |
|---|---|---|---|
| COVID-19 / pandemic plan (K.4) | None (CSV NO) | Full | `operational-safeguards.md` Appendix A.9 holds the active COVID-19 clinical protocol drawn from `Policy Docs/Millie Clinic COVID Policy.docx`. Patient-facing CDPH isolation logic, exposure protocol, and prevention rules are complete. Staff-facing operational protocols (return-to-work, sick-leave, PPE, exposure-reporting) remain a `To Do` placeholder per the source docx and are tracked in [TODO.md](TODO.md). |
| BYOD / MDM (rows 132–134) | None/Partial | Full | New `acceptable-use-and-byod.md` closes the policy gap; MDM vendor selection remains operational TODO. |
| Network security suite (SIG §N) | Mostly None | Full | New `network-and-cloud-security.md` covers N.1–N.12 plus AWS Questionnaire rows 2–33 in one file. |
| AI governance (SIG §R) | None | Full | New `ai-and-ml-governance.md` covers R.1/R.2/R.4/R.5; AI inventory anchored to `platform-and-access-matrix.md`. |
| Supply chain (SIG §S) | None/Partial | Full | `vendor-and-business-associates.md` §4 adds C-SCRM. |
| Records retention (D.3 / K.11) | Partial ("indefinite") | Full | `governance-and-risk-management.md` §III.6 table. |
| ERM framing (A.1) | None | Full | `governance-and-risk-management.md` §III.3. |
| OWASP A02, A07, A09 (sessions, password storage, logging) | Partial | Full | `technical-safeguards.md` §III.1.g, §III.2.d, §III.7. |
| Tamper-evident incident log (J.14) | Partial | Full | `incident-and-breach-response.md` §III.4. |
| Outsourced IR statement (J.11) | None | Full | `incident-and-breach-response.md` §III.6. |
| Patient-facing NPP (P.2) | Partial (mis-titled file) | Open Action | `PATIENT-NOTICE-TODO.md` makes the gap explicit. |

### 5.2 New gaps surfaced on this pass

- **CSV row 55 — DMARC.** Not addressed in any active policy. Suggest adding an email-authentication standards bullet under `network-and-cloud-security.md` §1 (or a new §1.x) and creating an operational TODO to verify DMARC posture. **This is the only `None` rating in the entire matrix.**

### 5.3 Cross-reference health check

Broken or stale links found in the active policy set. **None of these affect coverage**; they're cleanup items.

| File | Line(s) | Broken/stale ref | Should be | Severity |
|---|---|---|---|---|
| `technical-safeguards.md` | 203, 240 | `[hipaa-security-incidents.md](hipaa-security-incidents.md)` (archived) | `[incident-and-breach-response.md](incident-and-breach-response.md)` | Medium |
| `technical-safeguards.md` | 241 | `[hipaa-safeguards.md](hipaa-safeguards.md)` (archived) | `[operational-safeguards.md](operational-safeguards.md)` | Medium |
| `technical-safeguards.md` | 242 | `[hipaa-risk-management.md](hipaa-risk-management.md)` (archived) | `[governance-and-risk-management.md](governance-and-risk-management.md)` | Medium |
| `acceptable-use-and-byod.md` | 32, 160 | `[hipaa-business-associate-agreement.md](hipaa-business-associate-agreement.md)` (archived) | `[vendor-and-business-associates.md](vendor-and-business-associates.md)` | Medium |
| `acceptable-use-and-byod.md` | 124, 160 | `[hipaa-security-incidents.md](hipaa-security-incidents.md)` (archived) | `[incident-and-breach-response.md](incident-and-breach-response.md)` | Medium |
| `network-and-cloud-security.md` | 94, 192 | `[information-security-framework.md](information-security-framework.md)` (archived; merged into governance) | `[governance-and-risk-management.md](governance-and-risk-management.md)` | Medium |
| `governance-and-risk-management.md` | 219 | Note that `hipaa-definitions.md` §II(r) "will be updated separately to reflect this reconciliation" — definitions file still references `Risk Management Team` and `Chief Privacy/Security Officer`; the planned reconciliation update has not landed in `hipaa-definitions.md` | — | Low (cosmetic; reconciliation is described in governance §III.2 anyway) |
| `hipaa-definitions.md` | (whole) | File still uses pre-consolidation metadata table + numbered list with "Companypersonnel" docx typo + footnote artifacts | Apply the CONSOLIDATION §5d / §6 janitorial cleanup | Low |

### 5.4 Content/coverage observations

- **`AWS and Aptible Security Incident Management Policy.docx`** (sitting in `Policy Docs/`, dated 2026-05-24) has **not** been integrated into any active markdown policy. The new `incident-and-breach-response.md` §III.3 promises an "AWS / cloud-specific playbook" but the cited content lives in `network-and-cloud-security.md` §13, which itself **points back** to incident-and-breach-response §III.3. The substantive cloud-specific runbook from the AWS/Aptible docx has not been migrated. Tracked in [TODO.md](TODO.md) "Other outstanding follow-ups."
- **`ECH Security Assessment Questions - Questions.csv` link paths.** The 2 fixes already applied (per user) are confirmed in `vendor-and-business-associates.md` §5 and `sdlc-and-asset-lifecycle.md` §1 — both now point to `../ECH Security Assessment Questions - Questions.csv` at repo root. **No additional references found in the active policy set.**
- **AI policy double-coverage (not a regression).** Both `acceptable-use-and-byod.md` §III.A.5 and `ai-and-ml-governance.md` constrain submission of PHI to AI tools. This is intentional layering (AUP-level guardrail + governance-level program). Both reference `platform-and-access-matrix.md` as the source of truth for the approved-tool list.
- **`hipaa-definitions.md` is the only active policy file that still has the old docx-derived format** (numbered list, broken Scope heading, no consolidated frontmatter, "Companypersonnel" typo, footnote markers). Functionally adequate as a glossary; cosmetic only.
- **`platform-and-access-matrix.md` and `hipaa-definitions.md` deviate from the 3-file reference pattern in the README and PATIENT-NOTICE-TODO.md.** Each new policy points back to `hipaa-definitions.md` for shared terms — no breakage, but the README narrative speaks of "10 thematic + 3 reference files" and these are the 3 (platform matrix, definitions glossary, NPP placeholder).

---

## §6 — Quick reference: 24 → 10 + 3 file mapping (for audit cross-reference)

Where each historical Policy # lives now in the active set. Mirrors the supersedes lists in the active files' frontmatter.

| Old file (archived) | Old Policy # | Current home |
|---|---|---|
| hipaa-accounting-of-disclosures.md | L-003 | `patient-rights.md` §III.3 |
| hipaa-breach-notification.md | L-004 | `incident-and-breach-response.md` §III.7 |
| hipaa-business-associate-agreement.md | L-001 | `vendor-and-business-associates.md` §2 |
| hipaa-contingency-planning.md | IT-003 | `operational-safeguards.md` §III.4 |
| hipaa-de-identifying-phi.md | L-005 | `phi-use-and-disclosure.md` §§3–5 |
| hipaa-definitions.md | L-007 | unchanged (reference glossary) |
| hipaa-encryption.md | IT-005 | `technical-safeguards.md` §III.2 |
| hipaa-marketing.md | L-006 | `phi-use-and-disclosure.md` §III.6 |
| hipaa-minimum-necessary.md | L-010 | `phi-use-and-disclosure.md` §III.1 |
| hipaa-paper-documents.md | L-011 | `operational-safeguards.md` §III.3 |
| hipaa-passwords.md | IT-001 | `technical-safeguards.md` §III.1 |
| hipaa-phi-use-and-disclosure.md | L-002 | `phi-use-and-disclosure.md` §III.2 |
| hipaa-remote-access.md | IT-006 | `technical-safeguards.md` §III.4 |
| hipaa-right-to-access.md | L-009 | `patient-rights.md` §III.1 |
| hipaa-right-to-amend.md | L-008 | `patient-rights.md` §III.2 |
| hipaa-risk-management.md | IT-007 | `governance-and-risk-management.md` §§III.4–5 |
| hipaa-safeguards.md | IT-008 | `operational-safeguards.md` §§III.1–2 (admin + physical); technical bits → `technical-safeguards.md` |
| hipaa-security-incidents.md | IT-009 (old) | `incident-and-breach-response.md` §§III.1–6 |
| hipaa-workstation-use.md | IT-002 | `technical-safeguards.md` §III.3 |
| information-security-framework.md | IT-026 | `governance-and-risk-management.md` §III.1 + `vendor-and-business-associates.md` §1 |
| privacy-policy.md (mis-titled bundle) | (mixed) | Content rescued: IT-004 Device & Media → `technical-safeguards.md` §III.5. Patient-facing NPP → still TODO (`PATIENT-NOTICE-TODO.md`). |
| sdlc-and-asset-lifecycle.md | IT-009 (corrected) | unchanged (CTO-owned standalone) |
| platform-and-access-matrix.md | (xlsx snapshot) | unchanged (reference matrix) |
| ech-security-assessment.md | (xlsx snapshot) | replaced by `../ECH Security Assessment Questions - Questions.csv` at repo root |

New active files with no pre-consolidation predecessor:

| New file | Drives | Source |
|---|---|---|
| `acceptable-use-and-byod.md` | SIG D.2, M.1.3, M.1.5, M.1.6 | Authored 2026-05-24 |
| `network-and-cloud-security.md` | AWS Q rows 2–33; SIG N.1–N.12; OWASP A05/A06/A10 | Authored 2026-05-24 |
| `ai-and-ml-governance.md` | SIG R.1, R.2, R.4, R.5 | Authored 2026-05-24 |
| `New Policy Docs/PATIENT-NOTICE-TODO.md` | SIG P.2 (NPP) | Placeholder authored 2026-05-24 |
| `New Policy Docs/forms/breach-notification-individual-letter.md` | 45 CFR §164.404 | Migrated from L-004 Exhibit C |
| `New Policy Docs/forms/breach-notification-media-template.md` | 45 CFR §164.406 | New (derived from L-004 content requirements) |
| `New Policy Docs/forms/breach-notification-hhs-template.md` | 45 CFR §§164.408, 164.414 | Migrated from L-004 Exhibits B + D |
