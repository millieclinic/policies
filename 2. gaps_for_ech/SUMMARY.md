# ECH Gap Analysis — Section-Level Summary

Across 7 questionnaires and 36 sections (covering 182 CSV rows), Millie's existing originals — primarily the HIPAA Safeguards Policy, Risk Management Policy, Security Incident Management Policy, AWS/Aptible Incident Management Policy, Encryption Policy, Remote Access Policy, Password Management Policy, Breach Notification Policy, BAA Policy, Contingency Planning Policy, SDLC & Asset Lifecycle Policy, and the Information Security & Data Governance Framework — already give us enough written policy to answer ECH.

**Counts: 15 No Gap, 17 N/A, 4 Gap.**

Recommended action set:

1. Add a one-paragraph email-authentication / DMARC clause to the Information Security Framework.
2. Add a one-paragraph BYOD / MDM clause to the Workstation Use Policy.
3. Add a one-paragraph pandemic-operations + multi-vendor-resiliency clause to the Contingency Planning Policy.
4. Attach a cyber-liability certificate and a pentest / security-audit attestation to the submission (or honestly answer "none on file") — this is evidence, not policy text.

Everything else is either already covered by an existing original or is honestly answered "N/A — not in scope for our business."

| Questionnaire | Section | Category | Rationale (≤2 sentences) | Recommended action |
|---|---|---|---|---|
| AWS Questionnaire | AWS Account Management | No Gap | Operational answers already in CSV; AWS/Aptible Incident Mgmt Policy + Info Sec Framework cover the policy posture (single-account, root MFA, etc.). | — |
| AWS Questionnaire | Encryption | No Gap | Encryption Policy + Info Sec Framework §5 cover at-rest/in-transit; Aptible-managed encryption referenced. | — |
| AWS Questionnaire | Identity and Access Management | No Gap | Password Mgmt + Safeguards §III(b) Access Controls + Info Sec §4 cover RBAC / least-privilege / MFA; specific AWS deviations honestly answered in CSV. | — |
| AWS Questionnaire | Network Security | No Gap | AWS/Aptible Incident Mgmt Policy + CSV operational answers cover security groups, private subnets, S3 public-access posture. | — |
| AWS Questionnaire | Detection and Monitoring | No Gap | Info Sec Framework §7 (Logging/Monitoring) + AWS/Aptible Incident Mgmt §III.2 cover CloudTrail / GuardDuty. | — |
| AWS Questionnaire | Processes | No Gap | SDLC Policy + AWS/Aptible Incident Mgmt Policy cover IaC, IR plan, backups; remaining items (dedicated backup account, custom AMIs) are operational answers, not policy gaps. | — |
| ISD IT Risk Assessment | Request Details | N/A | Project-intake form fields, not policy questions. | Answer in-form at submission |
| ISD IT Risk Assessment | Server & Storage Requirements | N/A | Project-intake field. | Answer in-form |
| ISD IT Risk Assessment | Network Requirements | N/A | Cloud-native — no new ports / WAN / site-VPN. | Answer in-form |
| ISD IT Risk Assessment | Identity & Access Management | No Gap | Password Mgmt + Remote Access + Safeguards cover MFA, auth, vendor remote access. | — |
| ISD IT Risk Assessment | Additional Cybersecurity Questions | **Gap** | DMARC / email-authentication (row 55) and AV-exclusion / vuln-scan-exclusion stance (rows 50–52) not in any original. | Add 1-paragraph "Email Authentication & Anti-Malware Exclusions" clause to the Info Sec & Data Governance Framework |
| ISD IT Risk Assessment | Integration Requirements | No Gap | SDLC Policy covers API / interface change considerations. | — |
| ISD IT Risk Assessment | End-user Compute Requirements | No Gap | Workstation Use Policy + Remote Access Policy cover EUC posture. | — |
| ISD IT Risk Assessment | Clinical Engineering | N/A | No Internet of Medical Things (IoMT) — clinic uses standard endpoints + cloud services. | Answer N/A in submission |
| ISD IT Risk Assessment | Telecommunications Requirements | N/A | Standard SaaS telephony (RingCentral); no special telecom requirements. | Answer N/A in submission |
| ISD IT Risk Assessment | Timeline / Vendor Support / Other | N/A | Project-intake fields. | Answer in-form |
| OWASP Top 10 | A01–A10 (all 10 items) | No Gap | Each is "do you do X, please explain" — narrative answers from existing originals (Safeguards, Encryption, Password Mgmt, Remote Access, SDLC, AWS/Aptible IR) plus operational details already in CSV "FOLLOW UP" notes. No new policy text needed. | — |
| PCI DSS Assessment Form | General (all 10) | N/A | Millie does not process, store, or transmit cardholder data — payments outsourced. | Answer "N/A — payments outsourced; no cardholder data in scope" in submission |
| SIG Lite 2025 | A. Enterprise Risk Management | No Gap | Risk Mgmt Policy + Info Sec Framework §2 cover ERM framing. | — |
| SIG Lite 2025 | B. Nth Party Management | No Gap | BAA Policy + Info Sec Framework (1).md §11 (Nth-party flow-down clause) cover it. | — |
| SIG Lite 2025 | C. Information Assurance | No Gap | Info Sec Framework + Risk Mgmt Policy answer C.1 and C.4. | — |
| SIG Lite 2025 | D. Asset and Info Management | No Gap | SDLC / Asset Lifecycle Policy, Workstation Use, and Info Sec §9 (Retention) cover D.1 / D.2 / D.3; the Platform Matrix is the IT asset inventory. | — |
| SIG Lite 2025 | E. Human Resources Security | N/A | HR policies owned by HR / Gusto; not a security-policy gap. | Answer "HR policies maintained in Gusto / People Ops" |
| SIG Lite 2025 | F. Physical and Environmental Security | No Gap | Safeguards Policy §III(c) Facility Security Plan + Paper Document Mgmt cover physical security. | — |
| SIG Lite 2025 | G. IT Operations Management | No Gap | SDLC / Asset Lifecycle Policy + Info Sec Framework cover G.1 / G.2 / G.3. | — |
| SIG Lite 2025 | H. Access Control | No Gap | Password Mgmt Policy + Safeguards §III(b) cover both H.1 and H.2. | — |
| SIG Lite 2025 | I. Application Management | No Gap | Affirmative-fact questions; SDLC Policy covers the underlying program. | — |
| SIG Lite 2025 | J. Cybersecurity Incident Mgmt. | No Gap | Security Incident Mgmt + AWS/Aptible Incident Mgmt + Breach Notification cover all J-rows. | — |
| SIG Lite 2025 | K. Operational Resilience | **Gap** | K.4 (pandemic) is partially covered by the COVID Policy (patient-facing only); staff-facing pandemic operations and K.30 (multi-vendor resiliency) are not addressed. | Add 1-paragraph "Pandemic Operations & Multi-Vendor Risk Acceptance" clause to the Contingency Planning Policy |
| SIG Lite 2025 | L. Compliance Management | N/A | L.3 (antitrust), L.4 (compliance & ethics program), L.6 (fraud) not required for a 30-person clinic; handled via legal counsel + Gusto. | Answer "handled via outside legal counsel and HR processes; no standalone program" |
| SIG Lite 2025 | M. Endpoint Security | **Gap** | M.1.3 (MDM), M.1.5 (non-company devices), M.1.6 (BYOD) flagged "FOLLOW UP" in CSV. Workstation Use mentions personal devices but no BYOD / MDM stance is documented. | Add 1-paragraph "BYOD & Mobile Device Management" clause to the Workstation Use Policy |
| SIG Lite 2025 | N. Network Security | No Gap | AWS/Aptible Incident Mgmt + Info Sec Framework + Encryption Policy cover N.1–N.12; no on-prem network exists. | — |
| SIG Lite 2025 | O. Environmental, Social and Governance (ESG) | N/A | All 14 ESG rows not in scope for a 30-person women's-health clinic. | Answer "not formally documented — not applicable to Millie's scope" |
| SIG Lite 2025 | P. Privacy Management | No Gap | HIPAA suite (Privacy Policy, Use & Disclosure, Accounting, Right to Access / Amend, Min Necessary, De-ID, BAA) + Info Sec Framework cover P.2 / P.3 / P.4 / P.5 / P.8 / P.10 / P.11. P.9 GLBA + P.12 EU-registration are N/A. | — |
| SIG Lite 2025 | R. Artificial Intelligence | N/A | AI use limited to listed AI platforms in Platform Matrix (BAA-covered); no AI-system policy required at Millie's size. | Answer "AI vendors reviewed under BAA process; no separate AI policy" |
| SIG Lite 2025 | S. Supply Chain Risk Management (SCRM) | No Gap | BAA Policy + Info Sec Framework (1).md §11 + SDLC §III(a) Planning & Acquisition cover SCRM at this scale. | — |
| Insurances | Cyber Liability / Data Privacy | **Gap** | Evidence question, not policy. We need to attach the actual cyber-liability certificate to the submission. | Attach cyber-liability certificate to ECH submission (no policy change needed) |
| Security Audits | Penetration Testing + General Security Audit | **Gap** | Evidence questions. Millie has no recent third-party pentest or SOC 2 / HITRUST attestation. | Answer "none on file" or commission a pentest |
