---
title: "Policy ↔ ECH Questionnaire Coverage Mapping"
last_reviewed: 2026-05-24
owner: "Privacy Officer + Security Officer (joint)"
status: "DRAFT — companion to CONSOLIDATION-PROPOSAL.md"
source_questionnaire: "ECH Security Assessment Questions - Questions.csv (182 rows, 7 questionnaires)"
---

# Policy ↔ ECH Questionnaire Coverage Mapping

Cross-references every item in `ECH Security Assessment Questions - Questions.csv` against the 24 Markdown files in `New Policy Docs/`. Drives §7 of `CONSOLIDATION-PROPOSAL.md`.

- **Coverage rating** is policy-document coverage only (does the org have written policy on this?), not the operational state of the control. Operational state is captured in the CSV's `Answer` and `Status` columns.
- Row numbers reference the CSV (1-indexed; row 1 is the header).
- File paths are relative to `New Policy Docs/` unless otherwise noted.

---

## §1 — Coverage matrix

### 1.1 AWS Questionnaire (rows 2–33)

| CSV row | Q ref | Question (abbrev) | Policy file(s) | Coverage | Notes |
|---|---|---|---|---|---|
| 2 | Acct.1 | AWS Organizations used? | none | None | Operational config; no written policy says we must/mustn't use Orgs. |
| 3 | Acct.2 | Separate AWS accounts for Dev/Stg/Prod? | `sdlc-and-asset-lifecycle.md` §III(b) (implied) | Partial | SDLC mentions secure deployment but no env-separation requirement. |
| 4 | Acct.3 | Dedicated audit/logging account? | none | None | |
| 5 | Acct.4 | Shared root email alias? | none | None | |
| 6 | Acct.5 | Root MFA enabled, no access keys? | `hipaa-passwords.md` §III (general MFA); `information-security-framework.md` §4 | Partial | "MFA wherever possible" — not root-specific. |
| 7 | Acct.6 | Root used in last 7 days? | none | None | Operational metric. |
| 8 | Acct.7 | SCPs in place? | none | None | |
| 9 | Enc.1 | Encryption at rest for RDS/data stores? | `information-security-framework.md` §5; `privacy-policy.md` IT-004 §III(c) (NIST SP 800-111) | Full | At-rest standard ONLY in buried IT-004. |
| 10 | Enc.2 | EC2 volume/snapshot encryption? | same as Enc.1 | Partial | Generic at-rest covers it implicitly. |
| 11 | IAM.1 | SAML SSO for IAM? | none | None | |
| 12 | IAM.2 | Console IAM users exist? | `hipaa-passwords.md` §III(a) (unique IDs, MFA) | Partial | Policy requires unique IDs but doesn't forbid console users. |
| 13 | IAM.3 | Programmatic access keys exist? | none | None | |
| 14 | IAM.4 | Keys unused >90 days? | none | None | No key-rotation/usage policy. |
| 15 | IAM.5 | Keys not rotated >90 days? | none | None | |
| 16 | IAM.6 | Roles unused >90 days? | none | None | |
| 17 | IAM.7 | Wildcard admin / S3 / IAM access? | `information-security-framework.md` §4 (RBAC/least privilege) | Partial | Principle stated; no AWS-specific guardrail. |
| 18 | IAM.8 | RDS IAM auth? | none | None | N/A per answer (Aptible). |
| 19 | IAM.9 | Secrets Manager / SSM use? | none | None | |
| 20 | Net.1 | Security groups restrict non-HTTP inbound? | none | None | |
| 21 | Net.2 | Private subnets for internal resources? | none | None | |
| 22 | Net.3 | RDS in private subnets? | none | None | |
| 23 | Net.4 | Outbound SGs per VPC? | none | None | |
| 24 | Net.5 | Open S3 buckets? | none | None | |
| 25 | Net.6 | S3 block public access enabled? | none | None | |
| 26 | Det.1 | AWS Config in all regions? | none | None | |
| 27 | Det.2 | CloudTrail data events on S3? | `information-security-framework.md` §7 (logging) | Partial | Logging mentioned generically. |
| 28 | Det.3 | GuardDuty / IDS enabled? | none | None | |
| 29 | Proc.1 | IaC (Terraform/CFN)? | `sdlc-and-asset-lifecycle.md` §III (general) | Partial | SDLC doesn't mandate IaC. |
| 30 | Proc.2 | Custom AMIs maintained? | none | None | |
| 31 | Proc.3 | AWS-specific IR plan tested? | `hipaa-security-incidents.md` (general IR) | Partial | Not AWS-specific or tested cadence. |
| 32 | Proc.4 | Backups in dedicated account? | `hipaa-contingency-planning.md` §III(b) (offsite encrypted backup) | Partial | "Offsite" satisfied by Aptible; "dedicated account" not specified. |
| 33 | Proc.5 | Secure remote access to servers/DBs? | `hipaa-remote-access.md` (entire) | Full | |

### 1.2 ISD IT Risk Assessment (rows 34–71)

Project-intake questionnaire. Most items are project-context fields, not policy-relevant; rated `Project intake` where no policy is expected.

| CSV row | Q ref | Question (abbrev) | Policy file(s) | Coverage | Notes |
|---|---|---|---|---|---|
| 34–41 | Req.1–8 | Project context (objective, end-user, conversion, training) | none | Project intake | Belongs in change-mgmt/intake form; not a policy gap. |
| 42 | Svr.1 | Server infrastructure type? | `information-security-framework.md` §5 (Aptible, AWS) | Partial | |
| 43 | Net.1 | New port required? | none | None | Implies need for Change Mgmt / Network Sec policy. |
| 44 | Net.2 | New WAN circuit? | none | None | |
| 45 | Net.3 | Site-to-site VPN? | `hipaa-remote-access.md` (vague) | Partial | |
| 46 | IAM.1 | Authentication method? | `hipaa-passwords.md` §III; `information-security-framework.md` §4 | Full | |
| 47 | IAM.2 | MFA available? | `information-security-framework.md` §4 | Full | |
| 48 | IAM.3 | Vendor remote access? | `hipaa-remote-access.md` §III(a) | Full | |
| 49 | Cyb.1 | Internet-accessible? | none | None | |
| 50 | Cyb.2 | AV/security exclusions needed? | none | None | No AV policy. |
| 51 | Cyb.3 | Vuln-scan exclusions? | none | None | No vuln-mgmt policy. |
| 52 | Cyb.4 | Vendor doing vuln scanning/remediation? | none | None | |
| 53 | Cyb.5 | Transactional emails? | none | None | |
| 54 | Cyb.6 | Dedicated host/IP/shared mail? | none | None | |
| 55 | Cyb.7 | DMARC configured? | none | None | |
| 56 | Int.1 | API/interface changes? | `sdlc-and-asset-lifecycle.md` (general) | Partial | No formal change-control policy. |
| 57–63 | EUC.1–7 | End-user compute (mods, browser, OS, peripherals, equipment, VDI, local install) | `hipaa-workstation-use.md` (partial) | Partial | Workstation policy covers use; not provisioning/standards. |
| 64 | CE.1 | IoMT? | none | Project intake | Out of scope for Millie. |
| 65 | Tel.1 | Telecom? | none | Project intake | |
| 66–68 | TE.1–3 | Timeline | none | Project intake | |
| 69 | VS.1 | Existing ECH engagements? | none | Project intake | |
| 70–71 | Oth.1–2 | Outstanding issues / resolution | none | Project intake | |

### 1.3 OWASP Top 10 (rows 72–81)

| CSV row | Q ref | Question (abbrev) | Policy file(s) | Coverage | Notes |
|---|---|---|---|---|---|
| 72 | A01 | Access control enforcement | `information-security-framework.md` §4; `hipaa-safeguards.md` §III(b) | Full | |
| 73 | A02 | Sensitive data extra protection | `hipaa-encryption.md`; `privacy-policy.md` IT-004 §III(c) | Partial | Password storage gap flagged. |
| 74 | A03 | Injection defenses | `sdlc-and-asset-lifecycle.md` §III(c) (testing) | Partial | No secure-coding standard. |
| 75 | A04 | Secure SDLC w/ AppSec | `sdlc-and-asset-lifecycle.md` (whole file) | Partial | SDLC exists but lightweight; no AppSec role. |
| 76 | A05 | Hardening process | none | None | No hardening baseline policy. |
| 77 | A06 | Vuln scanning / patch mgmt | `sdlc-and-asset-lifecycle.md` §III(d) bullet 1 | Partial | "Security updates and patching" listed; no cadence/SLA. |
| 78 | A07 | Auth / session token protection | `hipaa-passwords.md` (whole) | Partial | Passwords covered; sessions/tokens not. |
| 79 | A08 | Code & infra integrity | `sdlc-and-asset-lifecycle.md` §III(b)(c) | Partial | No signed-artifact / supply-chain integrity policy. |
| 80 | A09 | Logging/monitoring failures | `information-security-framework.md` §7 | Partial | Logging stated; failure-detection/alerting not. |
| 81 | A10 | SSRF defenses | none | None | No app-sec policy detail. |

### 1.4 PCI DSS Assessment Form (rows 82–91)

| CSV row | Q ref | Question (abbrev) | Policy file(s) | Coverage | Notes |
|---|---|---|---|---|---|
| 82 | Gen.1 | Process/store/transmit card data? | none | None | Likely "No" for Millie — verify with Finance/Stripe. |
| 83 | Gen.2 | PCI DSS assessment in 12 mo? | none | None | |
| 84 | Gen.3 | Passing grade? | none | None | |
| 85 | Gen.4 | Card data encrypted? | none | None | |
| 86 | Gen.5 | Restricted access to card data? | none | None | |
| 87 | Gen.6 | Access control to card data? | none | None | |
| 88 | Gen.7 | Patches up to date? | `sdlc-and-asset-lifecycle.md` §III(d) | Partial | Not PCI-specific. |
| 89 | Gen.8 | Firewall? | none | None | |
| 90 | Gen.9 | Periodic password changes? | `hipaa-passwords.md` (no rotation requirement) | Partial | Policy intentionally omits forced rotation (NIST 800-63B aligned). |
| 91 | Gen.10 | Complex & unique passwords | `hipaa-passwords.md` §III(a) | Full | |

### 1.5 SIG Lite 2025 (rows 92–179)

| CSV row | Q ref | Question (abbrev) | Policy file(s) | Coverage | Notes |
|---|---|---|---|---|---|
| 92 | A.1 | ERM policy | none | None | No Enterprise Risk Mgmt program. `hipaa-risk-management.md` is HIPAA-scoped only. |
| 93 | B.1 | TPRM incl 4th/Nth parties | `information-security-framework.md` §11; `hipaa-business-associate-agreement.md` | Partial | Nth-party flow-down stated; no formal program doc. |
| 94 | B.2 | Contractual flow-down to subs | `information-security-framework.md` §11 | Full | |
| 95 | C.1 | Cyber risk mgmt policy | `information-security-framework.md`; `hipaa-risk-management.md` | Full | |
| 96 | C.4 | Risk assessment process | `hipaa-risk-management.md` §III | Full | |
| 97 | D.1 | Asset mgmt program | `privacy-policy.md` IT-004 §III(a); `hipaa-contingency-planning.md` §III(c) | Partial | Only in buried IT-004 + brief inventory mention. |
| 98 | D.2 | Acceptable Use policy | `hipaa-workstation-use.md` (partial) | Partial | No standalone AUP. Workstation Use is closest. |
| 99 | D.3 | Records retention policy w/ schedule | `information-security-framework.md` §9 (1 paragraph) | Partial | No retention schedule; "indefinite" is not a schedule. |
| 100 | E.1 | HR policies | none | None | Not in repo. |
| 101 | E.3 | Employee performance process | none | None | Not in repo. |
| 102 | F.1 | Physical security program | `hipaa-safeguards.md` §III(c); `hipaa-paper-documents.md` | Partial | Owner = "Terese" per CSV — physical/facility specifics needed. |
| 103 | G.1 | IT Ops policies aligned with strategy | `information-security-framework.md` | Partial | No formal "IT Operations" policy. |
| 104 | G.2 | Change Management policy | none | None | No formal change-control policy. |
| 105 | G.3 | Security requirements for new systems | `sdlc-and-asset-lifecycle.md` §III(a)(b) | Full | |
| 106 | H.1 | Access Control policy | `information-security-framework.md` §4; `hipaa-safeguards.md` §III(b) | Full | |
| 107 | H.2 | Password policy approved & enforced | `hipaa-passwords.md` (whole) | Full | |
| 108 | I.1 | Apps process scoped data | n/a | n/a | Affirmative answer; no policy needed. |
| 109 | I.2 | App development performed | `sdlc-and-asset-lifecycle.md` | Full | |
| 110 | I.3 | Web site/app hosted | n/a | n/a | |
| 111 | J.1 | Cybersecurity IR program | `hipaa-security-incidents.md` (whole) | Full | |
| 112 | J.4 | IR plan w/ escalation | `hipaa-security-incidents.md` §III(b) | Full | |
| 113 | J.5 | Event review methodology | `information-security-framework.md` §7 | Partial | "Reviewed as needed" — no defined cadence. |
| 114 | J.11 | Outsourced IR | none | None | Policy silent on MSSP use. |
| 115 | J.14 | Incident docs protected from tampering | `hipaa-security-incidents.md` §III(c) (log requirement) | Partial | Log exists; tamper-protection not specified. |
| 116 | K.1 | Business Resilience policy | `hipaa-contingency-planning.md` (whole) | Full | |
| 117 | K.2 | DR exercise/testing program | `hipaa-contingency-planning.md` §III(d) | Partial | DR plan referenced; testing cadence undefined. **FOLLOW UP**. |
| 118 | K.3 | Critical 3P dependencies? | n/a | n/a | Affirmative q. |
| 119 | K.4 | Pandemic plan? | none | None | **Answered NO; FOLLOW UP**. |
| 120 | K.5 | Offsite backups? | `hipaa-contingency-planning.md` §III(b) | Full | |
| 121 | K.6 | Operational risk assessment | `hipaa-risk-management.md` | Partial | HIPAA-scoped; doesn't cover non-PHI operational risk. |
| 122 | K.7 | BCP procedures | `hipaa-contingency-planning.md` | Full | |
| 123 | K.11 | Data retention policy/schedule | `information-security-framework.md` §9 | Partial | See row 99. |
| 124 | K.30 | Multi-vendor resiliency | none | None | **Answered NO; FOLLOW UP**. |
| 125 | L.1 | Regulatory compliance procedures | `information-security-framework.md` (general) | Partial | |
| 126 | L.2 | Customer-facing website | n/a | n/a | |
| 127 | L.3 | Antitrust policy | none | None | Likely out of scope. |
| 128 | L.4 | Compliance & ethics program | none | None | Not in repo. |
| 129 | L.5 | Cyber compliance procedures | `information-security-framework.md` | Partial | |
| 130 | L.6 | Fraud detection/prevention | none | None | Not in repo. |
| 131 | M.1 | Endpoints handle scoped data | n/a | n/a | Affirmative q. |
| 132 | M.1.3 | MDM program | none | None | **Answered NO; FOLLOW UP**. Closest is `hipaa-workstation-use.md` §III (mobile rules) but not MDM. |
| 133 | M.1.5 | Non-company devices on network | `hipaa-remote-access.md` §III(b)(c) | Partial | Allowed per answer YES; policy doesn't formally authorize BYOD. **FOLLOW UP**. |
| 134 | M.1.6 | BYOD mobile w/ scoped data | `hipaa-workstation-use.md` §II(b); `hipaa-passwords.md` §III(b) (mobile passcode) | Partial | Mobile passcode rule exists, but no BYOD enrollment/wipe policy. **FOLLOW UP**. |
| 135 | M.3 | (blank) | n/a | n/a | CSV row is empty. |
| 136 | N.1 | Secure network build | `information-security-framework.md` §4–5 | Partial | |
| 137 | N.2 | Network Security Program | none | None | No formal network security policy. |
| 138 | N.3 | External connections terminated at firewall | none | None | Implicit via cloud provider; not documented. |
| 139 | N.4 | Network device patching | none | None | |
| 140 | N.5 | Remote access policy approved | `hipaa-remote-access.md` (whole) | Full | |
| 141 | N.7 | NIDS/NIPS | none | None | |
| 142 | N.8 | DMZ environment | none | None | N/A (cloud-native); not documented. |
| 143 | N.9 | Wireless policy | none | None | No wireless policy. |
| 144 | N.11 | Device security standards / baselines | none | None | |
| 145 | N.12 | Default passwords changed | `hipaa-passwords.md` (general) | Partial | No explicit default-password requirement. |
| 146–158 | O.1–13 | ESG: env, hazards, biodiversity, modern slavery, ethics, health & safety, community, DEI | none | None | Out of scope for HIPAA repo. Low priority for women's-health clinic. |
| 159 | O.14 | Ethical sourcing | none | None | |
| 160 | P.1 | PII collection | n/a | n/a | Affirmative. |
| 161 | P.2 | PII privacy policy | `privacy-policy.md` (mis-titled per CONSOLIDATION) | Partial | Patient-facing NPP does NOT exist. |
| 162 | P.3 | Formal privacy program | `hipaa-phi-use-and-disclosure.md`; etc. | Full | |
| 163 | P.4 | Privacy training program | `hipaa-safeguards.md` §III(c)(iv); README annual training | Full | |
| 164 | P.5 | Minimum necessary / need-to-know | `hipaa-minimum-necessary.md` (whole) | Full | |
| 165 | P.6 | Internet-facing app collecting client data | n/a | n/a | Affirmative q. |
| 166 | P.8 | Data governance program | `information-security-framework.md` (whole) | Full | |
| 167 | P.9 | Privacy incident detection/reporting (GLBA) | `hipaa-breach-notification.md` (whole) | Partial | HIPAA breach covered; GLBA not (likely N/A). |
| 168 | P.10 | 4th/Nth-party access | `information-security-framework.md` §11 | Full | |
| 169 | P.11 | Privacy role w/ accountability | `hipaa-definitions.md` §II (CPO referenced everywhere) | Full | |
| 170 | P.12 | Registration info accuracy | none | None | Likely N/A. |
| 171 | R.1 | AI legal/regulatory awareness | none | None | No AI policy. |
| 172 | R.2 | Trustworthy AI in policies | none | None | |
| 173 | R.4 | AI risk mgmt review | none | None | |
| 174 | R.5 | AI system inventory policy | none | None | |
| 175 | S.1 | Supplier access control flow-down | `information-security-framework.md` §11 | Partial | High level; not full C-SCRM. |
| 176 | S.32 | C-SCRM policy | none | None | |
| 177 | S.57 | Media protection in SDLC supply chain | `sdlc-and-asset-lifecycle.md`; `privacy-policy.md` IT-004 | Partial | |
| 178 | S.61 | C-SCRM integrated in security planning | none | None | |
| 179 | S.80 | Personnel responsibilities for SCRM | none | None | |
| 180 | S.100 | System/comms protection in SCRM | none | None | |

### 1.6 Insurances (row 181)

| CSV row | Q ref | Question (abbrev) | Policy file(s) | Coverage | Notes |
|---|---|---|---|---|---|
| 181 | Ins.1 | Cyber Liability / Data Privacy insurance doc | `hipaa-contingency-planning.md` §III(g); `hipaa-breach-notification.md` §IV(f) | Partial | Policies reference insurance carrier; no insurance certificate stored in repo. |

### 1.7 Security Audits (rows 182–183)

| CSV row | Q ref | Question (abbrev) | Policy file(s) | Coverage | Notes |
|---|---|---|---|---|---|
| 182 | Aud.1 | Penetration Testing doc | none | None | No pentest policy or report referenced. |
| 183 | Aud.2 | General Security Audit doc | `hipaa-safeguards.md` §III(b)(xi) (periodic audits); `hipaa-risk-management.md` §III(a) | Partial | Audit mentioned but no formal audit program / report. |

---

## §2 — Gaps (items rated None or critical Partial)

Grouped by topic. Severity legend:
- **Critical** = `Remediate before submitting = Yes` in CSV, or compliance gap likely to block ECH submission.
- **High** = SIG Lite asks with no Millie policy coverage and the assessor will mark as "deficient."
- **Medium** = nice-to-have, common ask, but Millie can answer "controls compensate."
- **Low** = irrelevant to Millie's business model (e.g., PCI, modern slavery, IoMT).

### 2.1 Endpoint & device management — Critical

- **MDM program** (row 132, M.1.3, NO + FOLLOW UP). Severity: **Critical**. Millie allows BYOD (rows 133–134 YES) but has no Mobile Device Management program. Closest existing: `hipaa-workstation-use.md` mobile rules and `hipaa-passwords.md` §III(b) mobile passcode. Needs an enforceable MDM/BYOD policy with enrollment, remote-wipe, app-allowlist, and OS-version minimums.
- **BYOD policy** (rows 133, 134; M.1.5/M.1.6 YES + FOLLOW UP). Severity: **Critical**. BYOD is permitted in practice but never authorized in writing. Need explicit BYOD policy with acceptance-form, separation of personal/Company data, and offboarding wipe.

### 2.2 Acceptable Use / IT operations — High

- **Acceptable Use Policy** (row 98, D.2). Severity: **High**. SIG Lite explicitly asks for an AUP with owner & review cadence. Existing `hipaa-workstation-use.md` is workstation-only and doesn't cover internet/email/social-media/AI/personal-use.
- **Change Management policy** (row 104, G.2). Severity: **High**. No formal change-control policy exists. SDLC mentions "testing & validation" but no approvals/rollback procedure.
- **IT Operations policy** (row 103, G.1). Severity: **Medium**. The Framework partially covers, but no formal IT-Ops doc.

### 2.3 Records retention & data lifecycle — High

- **Records Retention policy with schedule** (rows 99, 123; D.3, K.11). Severity: **High**. Framework §9 says "indefinitely" which is a non-answer to the question; assessor wants a retention schedule by record type (PHI, email, logs, financial, HR).

### 2.4 HR & people security — High

- **HR Security policies** (row 100, E.1). Severity: **High**. SIG asks for management-approved HR policies (onboarding, background check, sanctions, termination). Not in repo.
- **Employee performance process** (row 101, E.3). Severity: **Medium**. Operational HR; out of scope for security repo but should be acknowledged.
- **Sanctions clause** (already flagged in CONSOLIDATION §1.4). Severity: **High**. Only `hipaa-risk-management.md` §II(d) has an explicit sanctions clause. SIG H.1/H.2 implicitly require it.

### 2.5 Network security — High

- **Network Security Policy / program** (rows 137, 138, 141, 142, 143, 144). Severity: **High**. SIG asks for a formal network security policy w/ baselines, firewalls, IDS/IPS, DMZ documentation. Millie's cloud-native posture answers most of these via Aptible/AWS — but there's no written policy that says so. A short "Network & Cloud Security" document is the smallest credible answer.
- **Wireless Policy** (row 143, N.9). Severity: **Medium**. Office wireless. If Millie offices use guest WiFi separation, a 1-page policy suffices.

### 2.6 AWS-specific operational hardening — Critical / High

Multiple AWS Questionnaire items (rows 2–8, 11–19, 26–32) are operational issues without policy backing. Severity per item is operational, not policy. **Policy-relevant gap**: there is no "Cloud Configuration Standard" anywhere in the repo. Severity: **High**. A standards doc that prescribes: AWS Orgs structure, IAM auth method (SSO vs IAM users), secrets management, key rotation cadence, VPC design rules, S3 public-access, GuardDuty/Config required, IaC required.

### 2.7 OWASP / AppSec — Critical (for items with FOLLOW UP)

- **A02 Cryptographic Failures — password storage** (row 73, FOLLOW UP, **Remediate=Yes**). Severity: **Critical**. Needs documented password hashing standard + key management for app secrets.
- **A06 Vuln/Outdated Components — Upgrade GitHub** (row 77, FOLLOW UP, **Remediate=Yes**). Severity: **Critical**. Needs documented patch/upgrade SLA; SDLC policy is too thin.
- **A07 Auth/Session** (row 78, FOLLOW UP, **Remediate=Yes**). Severity: **Critical**. Sessions/tokens not in `hipaa-passwords.md`.
- **A04, A09, A10** (rows 75, 80, 81, FOLLOW UP). Severity: **High**. Need an AppSec / Secure Coding standard.
- **A05 Hardening process** (row 76). Severity: **High**. No hardening baseline.

### 2.8 Resiliency & business continuity — Critical

- **Pandemic plan** (row 119, K.4, NO + FOLLOW UP). Severity: **Critical**. A 1-page pandemic appendix to Contingency Planning satisfies this.
- **Multi-vendor resiliency strategy** (row 124, K.30, NO + FOLLOW UP). Severity: **Critical** by virtue of explicit NO answer. Document the current single-vendor dependencies (Aptible, AWS, Cloudflare) and risk-acceptance rationale.
- **DR testing program** (row 117, K.2, FOLLOW UP). Severity: **High**. Existing policy mentions plan; needs cadence + test results.

### 2.9 AI governance — High (and rising)

- **AI policy / Trustworthy AI / AI inventory / AI risk review** (rows 171–174, R.1/R.2/R.4/R.5). Severity: **High**. SIG Lite added an entire R section in 2025 — assessors will start failing orgs without something. Need a brief AI Use & Governance policy covering: approved AI tools, prohibited inputs (PHI to public LLMs), AI inventory, periodic review.

### 2.10 Supply chain risk — Medium

- **C-SCRM policy** (rows 175, 176, 178, 179, 180; S.32/S.61/S.80/S.100). Severity: **Medium**. Existing BAA + Vendor Mgmt covers most operational substance; SIG wants a formally-named C-SCRM document. A small addendum to the consolidated vendor doc likely suffices.

### 2.11 Compliance & ethics — Medium

- **Compliance & ethics program / fraud prevention** (rows 128, 130; L.4/L.6). Severity: **Medium**. Standard ask; light document with Code of Conduct + whistleblower channel.

### 2.12 Audit & assurance — High

- **Penetration testing** (row 182). Severity: **High**. ECH wants a pentest report. No policy or report exists in repo.
- **General Security Audit report** (row 183). Severity: **High**. No SOC2 or equivalent.

### 2.13 Insurance — Medium

- **Cyber Liability certificate** (row 181). Severity: **Medium**. Policies reference it; certificate needs to be attached to ECH submission.

### 2.14 PCI / Out-of-scope items — Low

- **PCI DSS** (rows 82–91). Severity: **Low** if Millie's payment processing is fully outsourced to a SAQ-A provider (Stripe etc.). Document the answer as "Out of scope per SAQ-A" rather than creating PCI policy.
- **ESG/DEI** (rows 146–159). Severity: **Low** for Millie. Answer "Not formally documented" or point to public-facing values.
- **IoMT** (row 64). Severity: **Low** — N/A.
- **Antitrust / modern slavery** (rows 127, 152, 153). Severity: **Low**.

### 2.15 Patient-facing Notice of Privacy Practices — High

- **NPP** (row 161, P.2 partial; also flagged in CONSOLIDATION §3.10). Severity: **High**. The `privacy-policy.md` file is mis-titled (it's an internal policy concat). A patient-facing §164.520 NPP does not exist.

---

## §3 — Cruft / over-engineered (cuttable when consolidating)

Content in the 24 files that no ECH/SIG item asks about. Candidates for deletion or massive reduction in the consolidated set.

### 3.1 PHI use & disclosure exhibits with no questionnaire counterpart

`hipaa-phi-use-and-disclosure.md` contains 8 detailed disclosure-permission sections that are policy-required by 45 CFR §164.512 but read like a federal-agency manual. The ECH questionnaire never asks about any of these:

- **§III(c)** Disclosures to law enforcement (warrants, subpoenas, suspect identification, location of fugitives). ~50 lines.
- **§III(d/e)** Coroner / funeral director disclosures. ~15 lines.
- **§III(f)** Workers' compensation disclosures. ~10 lines.
- **§III(h)** Cadaveric organ/eye/tissue donation. ~10 lines.
- **§III(j)** Military and veteran activities. ~10 lines.
- **§III(k)** National security and intelligence activities. ~10 lines.
- **§III(l)** Protective services for the President. ~10 lines.
- **§III(m)** Correctional institutions. ~15 lines.

**Recommendation:** keep §III(b) (public health, including communicable diseases and child abuse — relevant to women's health) and §III(g) (threat to health/safety — clinically relevant). Collapse the rest to a single paragraph: *"Disclosures permitted under 45 CFR §164.512 for law enforcement, judicial proceedings, coroners, organ donation, workers' compensation, military, national security, and correctional institutions are permitted only with prior Chief Privacy Officer approval. Personnel must consult the CPO before responding to any such request."* Saves ~130 lines.

### 3.2 Paper-document procedures beyond the basics

`hipaa-paper-documents.md` reads as if Millie has a large paper-records operation. ECH questionnaire never asks about paper records other than implicitly via SIG D.3 records retention.

- **§III(c)(iv)** Selection process for off-site document shredding services with BAA, insurance, certificate of destruction. ~10 lines.
- Detailed mailing precautions in §III(a) bullet 5.

**Recommendation:** keep a brief paragraph: "Paper PHI is minimized. If created, it is shredded on-site at end of day; off-site shredding requires a BAA." Saves ~15 lines.

### 3.3 Encryption policy boilerplate duplicating Device & Media

`hipaa-encryption.md` is data-in-motion only and disclaims data-at-rest ("This Policy does not cover 'at rest' data… which is subject to other applicable Company policies"). It then says key recovery archives, "import/export to foreign countries," and key length determination — content that reads like a 2010-era enterprise standard.

- **§III(c)(iii)** Foreign-country encryption export controls. Largely irrelevant for Millie's stack.
- Manual key-archival in a "secure environment" (§III(c)(iii) end).

**Recommendation:** trim to the substantive standards (FIPS 140-2, NIST SP 800-52/77/111/113), MFA requirement, and termination key deactivation. Drop foreign-export language. Saves ~15 lines.

### 3.4 Right-to-access fee mechanics & paper-mail procedures

`hipaa-right-to-access.md` §III(a)(vii) includes detailed per-page paper-copy fees ($0.75/page) and CD/USB-flash-drive supply costs. Millie's patient portal handles this digitally; ECH/SIG never asks about per-page copy fees.

**Recommendation:** keep the flat-fee statement and the "no patient denied access for inability to pay" line; cut the supply-cost itemization. Saves ~10 lines.

### 3.5 Breach notification exhibits — paper forms

`hipaa-breach-notification.md` Exhibits B (Risk Assessment Form), C (Sample Letter), D (Report Form) are extensive `_______` fill-in-the-blank paper forms. Useful for an auditor but bloated for a markdown policy.

**Recommendation:** keep Exhibit A (state law) inline; move Exhibits B, C, D to a separate `forms/` folder or convert to a 1-page "use the template in Google Workspace > Compliance > Breach Forms" pointer. Saves ~100 lines from the consolidated file.

### 3.6 De-identification 18-identifier list duplication

The 18-identifier Safe Harbor list appears once in `hipaa-de-identifying-phi.md` §III(a)(ii) and again (slightly different — 16 items, no zip-code carve-out) in §III(c)(ii) for Limited Data Sets. The duplication is functional (different rules apply) but visually noisy.

**Recommendation:** preserve both lists but format as side-by-side table or shared list with `* (LDS only)` annotations. Cuts ~20 lines and reduces drift risk.

### 3.7 SDLC policy header has wrong title

`sdlc-and-asset-lifecycle.md` lines 8–11 read "Title: Security Incident Management Policy / Policy #: IT-026" — a copy-paste bug. (`information-security-framework.md` also has Policy # IT-026, so the SDLC doc collides.) Not cruft, but a fix-during-consolidation item.

### 3.8 "Information Blocking Compliance Policy" cross-reference

Already flagged in CONSOLIDATION §1.13. Two references in `hipaa-right-to-access.md` to a policy that doesn't exist. ECH never asks about the Information Blocking Rule. **Recommendation:** inline the EHI definition and drop both references entirely. Saves ~5 lines and removes a dangling link.

### 3.9 Privacy-policy.md DICOM/image base64 artifacts

The mis-titled `privacy-policy.md` contains numerous `![](data:image/png;base64...)` and `400989884.1` page-footer artifacts from the docx import. ECH never asks for any of this. Already part of the cleanup plan.

---

## §4 — Action items (CSV-surfaced TODOs for ECH submission)

Every CSV row where `Status = FOLLOW UP` or `Remediate before submitting = Yes`. Owners pulled from CSV; "—" where blank.

| # | CSV row | Q ref | Question (abbrev) | Current answer | Status | Remediate? | Owner | What needs to happen |
|---|---|---|---|---|---|---|---|---|
| 1 | 73 | OWASP A02 | Sensitive data extra protection | (blank) | FOLLOW UP | **Yes** | — | Document password storage approach (hash algo, salt, iterations); add to AppSec/SDLC. |
| 2 | 75 | OWASP A04 | Secure SDLC w/ AppSec | (blank) | FOLLOW UP | (blank) | — | Decide whether current SDLC answer is sufficient; if not, expand SDLC doc with AppSec role. |
| 3 | 77 | OWASP A06 | Vuln scanning + patch mgmt | (blank) | FOLLOW UP | **Yes** | — | Complete the GitHub upgrade; document patch-mgmt SLA. |
| 4 | 78 | OWASP A07 | Auth / session tokens | (blank) | FOLLOW UP | **Yes** | — | Document session-token handling, expiry, rotation; add to consolidated technical safeguards. |
| 5 | 80 | OWASP A09 | Logging & monitoring | (blank) | FOLLOW UP | (blank) | — | Document log review cadence, alert thresholds, retention. |
| 6 | 81 | OWASP A10 | SSRF defenses | (blank) | FOLLOW UP | (blank) | — | Document URL allowlisting / metadata-endpoint blocks for outbound calls. |
| 7 | 117 | SIG K.2 | DR testing program | (blank) | FOLLOW UP | (blank) | — | Define annual DR test cadence; capture last test date. |
| 8 | 119 | SIG K.4 | Pandemic plan | **NO** | FOLLOW UP | (blank) | — | Add pandemic-plan section to Contingency Planning (remote-work activation, supply continuity). |
| 9 | 124 | SIG K.30 | Multi-vendor resiliency | **NO** | FOLLOW UP | (blank) | — | Document accepted single-vendor risk on Aptible/AWS/Cloudflare and any mitigations. |
| 10 | 132 | SIG M.1.3 | MDM program | **NO** | FOLLOW UP | (blank) | — | Stand up MDM (or document why N/A) + write BYOD policy. |
| 11 | 133 | SIG M.1.5 | Non-company devices on network | YES | FOLLOW UP | (blank) | — | Pair with #10; needs BYOD authorization document. |
| 12 | 134 | SIG M.1.6 | BYOD mobile w/ scoped data | YES | FOLLOW UP | (blank) | — | Pair with #10/#11; needs enrollment + acceptance form. |

Other AWS-questionnaire items have `No` answers but are not flagged FOLLOW UP — owner `zoe.h@millieclinic.com` should review for whether each warrants pre-submission remediation. The notable judgment calls are:
- Row 21 (private subnets): noted "maybe fix, but not confident."
- Row 26 (AWS Config): "might be ok to wait."
- Rows 11, 12, 13, 17 (IAM users w/ console access, programmatic keys, wildcard admin): these are common red flags for assessors even when intentionally accepted.

---

## §5 — How this drives consolidation

See `CONSOLIDATION-PROPOSAL.md` §7 for the proposed structural changes that follow from §2 (gaps) and §3 (cruft) above.
