---
title: "Information Security Governance, Risk Management, and Compliance Program"
sources: ["information-security-framework.md", "hipaa-risk-management.md"]
supersedes: ["IT-026 (Framework)", "IT-007 (Risk Management)"]
last_reviewed: 2026-05-24
owner: "Security Officer (Privacy Officer co-owner)"
status: "active"
---

# Information Security Governance, Risk Management, and Compliance Program

> **Sources.** Consolidated from: `information-security-framework.md` (IT-026), `hipaa-risk-management.md` (IT-007). Vendor Management & BAAs moved to [vendor-and-business-associates.md](vendor-and-business-associates.md). Originals archived in `New Policy Docs/_archive/`.

## I. Scope

This Policy applies to all facilities and locations owned, operated, or managed by Millie, Inc. ("Company"), all Company personnel, and all Company information assets including Protected Health Information, personally identifiable information, and confidential business information.

## II. Policy

Company maintains a comprehensive program of administrative, technical, and physical safeguards to ensure the confidentiality, integrity, and availability of sensitive personal and corporate information, including Protected Health Information ("PHI") as defined under HIPAA. This Policy is the landing document for Company's information security governance, risk management, and compliance program; it establishes the governance bodies, the annual risk assessment and mitigation cycle, the records retention schedule, the assurance program, and the canonical training and sanctions provisions that are referenced by every other Company information privacy and security policy.

It is the policy of Company to operate a risk-based information security program, to conduct thorough and timely risk assessments of the potential threats to and vulnerabilities of the confidentiality, integrity, and availability of its electronic PHI ("ePHI") and other confidential and proprietary electronic information, and to develop strategies to efficiently and effectively mitigate the risks identified in the assessment. A risk assessment shall be conducted no less frequently than once a year. The information security risk management process assesses compliance with the administrative, physical, and technical standards that govern ePHI that is received, created, maintained, or transmitted by Company.

The results of each risk assessment shall be presented to the Risk Review Committee, and if there are material risks, to the Board of Directors or any committee designated thereby. All Company personnel are expected to fully cooperate with all persons charged with doing risk management work. Any personnel member who violates this Policy will be subject to disciplinary action in accordance with §V (Sanctions) below.

## III. Procedure

### 1. Information Security & Data Governance Framework

Company maintains a written information security and data governance framework covering the lifecycle of sensitive data — how it is stored, accessed, transmitted, monitored, retained, archived, and protected in the event of a breach. The framework applies to PHI, PII, and other confidential business information maintained by Company. Operational and technical specifics are documented in [technical-safeguards.md](technical-safeguards.md) and [operational-safeguards.md](operational-safeguards.md); this section establishes the framework at the policy/narrative level.

**(a) Data classification & handling.** Company defines PHI in accordance with HIPAA and applies strict handling controls. Data use is governed by the Minimum Necessary Rule and by formal processes for de-identification, re-identification, and limited data sets (see [phi-use-and-disclosure.md](phi-use-and-disclosure.md)). These controls minimize unnecessary exposure and ensure compliant data usage.

**(b) Access control & identity management (principles).** Access is governed by role-based access control ("RBAC") and least-privilege principles. All systems require multi-factor authentication. AWS access is managed via IAM users, and root access is not used for routine operations. Access is granted based on role and business need and is revoked promptly upon role change or termination. Administrative access is restricted and monitored. Periodic reviews of access permissions are conducted as part of ongoing security practices. Detailed authentication, password, session, and provisioning standards are documented in [technical-safeguards.md](technical-safeguards.md).

**(c) Data storage & protection (principles).** All PHI transmitted over open networks is encrypted. Databases hosted via Aptible are encrypted at rest. Devices storing PHI are inventoried, encrypted, and securely wiped prior to reuse or disposal. Paper records are minimized, securely stored, and shredded when no longer needed. Detailed encryption standards (FIPS 140-2; NIST SP 800-52, 800-77, 800-111, 800-113), key management, and device/media controls are documented in [technical-safeguards.md](technical-safeguards.md).

**(d) Data transmission & sharing (principles).** All PHI transmitted externally must be encrypted. Data sharing is governed by the Minimum Necessary Rule, Data Use Agreements, and Business Associate Agreements. Secure channels are required for all remote access and data transmission. See [phi-use-and-disclosure.md](phi-use-and-disclosure.md) and [vendor-and-business-associates.md](vendor-and-business-associates.md).

**(e) Logging, monitoring & audit controls (principles).** Company maintains logs across systems including Aptible, AWS CloudWatch, and internal admin dashboards. Logs track user activity, including updates to patient data, capturing who made changes, what fields were changed, and when. These logs are used to support security monitoring, incident investigation, and audit activities. Relevant logs are reviewed as needed in response to security events or anomalies. Log review cadence, alerting thresholds, and protection of log integrity are detailed in [technical-safeguards.md](technical-safeguards.md). Retention of log records is governed by the Records Retention Schedule in §6 below.

**(f) Incident response & breach management (pointer).** Company maintains a Breach Notification Policy aligned with HIPAA. Suspected breaches must be reported promptly and are investigated under the procedures in [incident-and-breach-response.md](incident-and-breach-response.md). If confirmed, affected individuals are notified within 60 days and mitigation actions are taken.

**(g) Data retention & lifecycle management (pointer).** Application data, audit logs, backups, and other records are retained in accordance with the Records Retention Schedule in §6 below. Daily backups are performed via Aptible, including point-in-time recovery capabilities (see [operational-safeguards.md](operational-safeguards.md) §5 Contingency Planning).

**(h) Business continuity & data availability (pointer).** Databases are backed up daily with redundancy and recovery capabilities via Aptible. Detailed BCP/DR controls are documented in [operational-safeguards.md](operational-safeguards.md) §5.

**(i) Third-party & vendor management (pointer).** Vendor and Business Associate management — including BAA execution, subcontractor flow-down, and supply-chain risk — is documented in [vendor-and-business-associates.md](vendor-and-business-associates.md). Material third-party risks are escalated through Company's risk management process and reviewed by the Risk Review Committee.

### 2. Roles & Responsibilities

The following roles administer the information security governance, risk management, and compliance program. Where prior Company policy documents referred to a "Chief Privacy Officer," "Chief Security Officer," "Risk Committee," or "Risk Management Team," those references shall be read as the corresponding role defined below.

**(a) Privacy Officer.** The Privacy Officer (formerly referred to as the "Chief Privacy Officer") is accountable for Company's HIPAA privacy program and is the canonical authority for use and disclosure of PHI, patient rights, breach determination, and sanctions tracking. The Privacy Officer co-owns this Policy with the Security Officer and is responsible for the Training & Awareness Program (§IV) and for documenting and tracking sanctions (§V).

**(b) Security Officer.** The Security Officer (formerly referred to as the "Chief Security Officer") is accountable for Company's HIPAA security program and for the administrative, physical, and technical safeguards that protect ePHI. The Security Officer is the primary owner of this Policy, chairs the Risk Review Committee, owns the annual risk assessment, owns the assurance program (§8), and serves as the escalation point for security incidents.

**(c) Risk Review Committee.** The Risk Review Committee (formerly variously referred to as the "Risk Committee" or "Risk Management Team") is the standing governance body responsible for the risk management process and procedures outlined in this Policy. The Committee consists of the Privacy Officer, the Security Officer, the CTO, and other personnel with subject-matter expertise as appointed by the Security Officer (which may include Human Resources, Operations, Finance, and external advisors). The Committee receives the annual risk assessment, prioritizes mitigation, and escalates material risks to the CEO and Board.

**(d) CTO.** The CTO is accountable for technical implementation of safeguards, for the secure design and operation of Company's systems and infrastructure, and for the change management and SDLC controls documented in [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md). The CTO is a standing member of the Risk Review Committee.

**(e) CEO.** The CEO is the executive sponsor of the information security governance program, receives the annual privacy & security report (§10), and approves material risk acceptance and policy exceptions. The CEO is responsible for ensuring the program is appropriately resourced.

**(f) Practice Manager.** The Practice Manager is responsible for site-level operational implementation of safeguards, for facility security, and (jointly with the Privacy Officer) for HR security matters described in §7, including background checks, NDAs on hire, and termination access revocation coordination.

### 3. Enterprise Risk Management

Company's HIPAA-scoped risk management process described in §§4–5 is one component of a broader enterprise risk management ("ERM") program that addresses operational, strategic, financial, regulatory, clinical, and reputational risk. The Risk Review Committee maintains visibility into top enterprise risks beyond ePHI — including but not limited to clinical quality, vendor concentration, financial liquidity, legal/regulatory exposure, and people risk. The Committee reviews the top enterprise risk register at least annually and presents it to the Board of Directors (or a committee designated thereby) for review. Material risks identified through any pathway — risk assessment, audit, incident, regulator inquiry, vendor escalation — are escalated through this same governance channel.

### 4. Annual HIPAA Security Risk Assessment Process

*Risk Assessment.* The intent of completing a risk assessment is to determine potential threats and vulnerabilities related to the security of PHI and their likelihood, as well as the impact on Company should they occur. The output of this process helps identify appropriate controls for reducing or eliminating risk. Company may utilize the [risk assessment tool](https://www.healthit.gov/providers-professionals/security-risk-assessment-tool) developed by the Office for Civil Rights within the U.S. Department of Health & Human Services to perform its HIPAA risk assessment. This tool may be supplemented by additional risk assessment elements or by a more robust risk assessment performed by a third-party vendor.

In performing the risk assessment, Company shall appoint a committee consisting of the Privacy Officer, the Security Officer, and other personnel with subject matter expertise (the "Risk Review Committee") to do the following.

1. *Universe of ePHI*: Identify where ePHI is created, received, maintained, processed, or transmitted and document its findings, taking into consideration removable media and portable devices and third-party systems. Using information-gathering techniques, identify the IT System boundaries, as well as the resources and the information that constitute the IT System.
2. *Threat Identification*: Ensure potential threats to the IT Systems and ePHI are identified.
3. *Vulnerability Identification*: Develop a list of technical and nontechnical system vulnerabilities that could be exploited or triggered by the potential threat sources. Vulnerabilities can range from incomplete or conflicting policies that govern computer usage to insufficient safeguards to protect Company's equipment to any number of software, hardware, or other deficiencies that comprise the IT System.
4. *Control Analysis*: Document and assess the effectiveness of technical and nontechnical controls that have been or will be implemented to minimize or eliminate the likelihood of a threat source exploiting a system vulnerability.
5. *Likelihood Determination*: Determine the overall likelihood rating, which indicates the probability that a vulnerability could be exploited by a threat source given the existing or planned security controls.
6. *Impact Analysis*: Determine the level of adverse impact that would result from a threat source successfully exploiting a vulnerability.
7. *Risk Determination*: Establish a risk level. By multiplying the ratings from the likelihood determination and impact analysis, a risk level is determined. This represents the degree or level of risk to which an IT System, facility, or procedure might be exposed if a given vulnerability were exploited.
8. *Control Recommendations*: Identify controls that could eliminate or reduce to an acceptable level the identified risks, as appropriate to Company's operations.
9. *Results Documentation*: Results of the risk assessment are documented in an official report or briefing and provided to the Risk Review Committee to make decisions on policy, procedure, budget, and system operational and management changes. If significant risks are identified, the report should also be provided to the Board of Directors or committee designated by the Board of Directors.

**Risk management schedule.** The risk assessment process shall be carried out according to the following schedule:

- *Scheduled Basis*: An overall risk assessment of Company's IT System will be conducted annually. The assessment process should be completed in a timely fashion so that risk mitigation strategies can be determined and included in the corporate budgeting process.
- *Ongoing*: From the time that a need for a new information system is identified through the time it is disposed of, ongoing assessments of the potential threats to a system and its vulnerabilities should be undertaken as a part of the maintenance of the system.
- *As Needed*: The Security Officer (or other designated personnel member) or the Risk Review Committee may call for a full or partial risk assessment in response to changes in business strategies, information technology, information sensitivity, threats, legal liabilities, or other significant factors that affect Company's IT System.

### 5. Risk Mitigation Process

*Risk Mitigation.* Risk mitigation involves prioritizing, evaluating, and implementing the appropriate risk-reducing controls recommended from the risk assessment process to ensure the confidentiality, integrity, and availability of ePHI. Elimination of all risk is not practical. Depending on individual situations, implemented controls may lower a risk level, but not completely eliminate the risk.

- *Prioritize Actions*: Using results from Step 7 of the risk assessment, the Risk Review Committee shall sort the threat and vulnerability pairs according to their risk levels in descending order. This establishes a prioritized list of necessary actions, with the pairs at the top of the list getting/requiring the most immediate attention and top priority in allocating resources.
- *Evaluate Recommended Control Options*: Although possible controls for each threat and vulnerability pair are determined in Step 8 of the risk assessment, the Risk Review Committee shall review the recommended control(s) and alternative solutions for reasonableness and appropriateness. The feasibility (e.g., compatibility, user acceptance) and effectiveness (e.g., degree of protection, level of risk mitigation) of the recommended controls should be analyzed. In the end, select the most appropriate control option for each threat and vulnerability pair.
- *Conduct Cost-Benefit Analysis*: The Risk Review Committee shall determine the extent to which a control is cost-effective. Compare the benefit (e.g., risk reduction) of applying a control with its subsequent cost of application. Controls that are not cost-effective must also be identified during this step. Analyzing each control or set of controls in this manner, and prioritizing across all controls being considered, can greatly aid in the decision-making process.
- *Select Control(s)*: The Risk Review Committee shall take into account the information and results from previous steps, Company's mission, and other important criteria, and consult with senior management to determine the best control(s) for reducing risks to the IT Systems and to the confidentiality, integrity, and availability of ePHI. These controls may consist of a mix of administrative, physical, and/or technical safeguards.
- *Assign Responsibility*: The Risk Review Committee shall identify the individual(s) or team with the skills necessary to implement each of the specific controls outlined in the previous step, and formally assign to such individuals or teams their responsibilities.
- *Develop Safeguard Implementation Plan*: The Risk Review Committee, or its designee(s), shall be responsible for developing an overall implementation or action plan and individual project plans needed to implement the safeguards and controls identified. The implementation plan should contain the following information:
  - Each risk or vulnerability/threat pair and risk level;
  - Prioritized actions;
  - The recommended feasible control(s) for each identified risk;
  - Required resources for implementation of selected controls;
  - Personnel responsible for implementation of each control;
  - Start date for implementation;
  - Target date for completion of implementation; and
  - Maintenance requirements.

  The overall implementation plan provides a broad overview of the safeguard implementation, identifying important milestones and time frames, resource requirements (staff and other individuals' time, budget, etc.), interrelationships between projects, and any other relevant information. Regular status updates against plan, along with key metrics and success indicators, should be reported to the Risk Review Committee.

  Individual project plans for safeguard implementation may be developed and may contain detailed steps that assigned resources must carry out in order to meet implementation time frames and expectations (often referred to as a work breakdown structure). Additionally, consider including items in individual project plans such as a project scope, a list of deliverables, key assumptions, objectives, task completion dates, and project requirements.

- *Implement Selected Controls*: As controls are implemented, the Risk Review Committee must monitor the affected system(s) to verify that the implemented controls continue to meet expectations.
- *Addressing Unmet Risk Reduction Expectations*: If risk reduction expectations are not met, then repeat all or a part of the risk management process so that additional controls needed to lower risk to an acceptable level can be identified.

### 6. Records Retention Schedule

Company retains records in accordance with the following schedule. Retention obligations begin at the date specified in the "Retention" column. Records may be retained longer if required by litigation hold, audit, regulator inquiry, or other operational need. The Privacy Officer maintains the canonical retention schedule and reviews it at least annually.

| Record type | Retention | Authority |
|---|---|---|
| PHI (patient records) | Lifetime + 6 years after last patient interaction | HIPAA §164.530(j) + CA Bus. & Prof. Code |
| Audit logs | 6 months hot in database; archive to AWS S3 for long-term per Framework §1(e) | HIPAA §164.312(b) |
| Email | TBD — policy under development | — |
| HR records | Per state law (typically 4–7 years post-termination) | CA Labor Code |
| Financial records | 7 years | IRS |
| BAA and vendor contracts | 6 years past termination | HIPAA §164.530(j) |
| Incident & breach records | 6 years past close | HIPAA §164.530(j) |

Application data is retained in accordance with business and regulatory requirements. At present, core application data is retained indefinitely to support clinical, operational, and compliance needs, subject to the PHI retention floor above. Daily backups are performed via Aptible, including point-in-time recovery capabilities.

### 7. HR Security and Sanctions Anchor

HR-facing security policies — including pre-employment background checks, the Non-Disclosure Agreement / Confidentiality Agreement required on hire, sanctions for policy violations, access provisioning at hire, and access revocation at termination — are owned jointly by the Practice Manager and the Privacy Officer. The Practice Manager owns the operational execution (hiring paperwork, signed acknowledgments, exit checklist) and the Privacy Officer owns the privacy/security policy content and the sanctions register. Standalone HR security policies (background-check policy, NDA, full sanctions schedule) are under development; until they are formally adopted, this Policy and the canonical Sanctions clause in §V below govern.

Access provisioning at hire and revocation at termination are coordinated by the Practice Manager (notification), the Security Officer (system revocation), and the Privacy Officer (PHI access review). The standing requirement is that all system access be revoked promptly upon termination or role change; specific technical procedures (key deactivation, MFA token revocation, remote access termination, device retrieval) are documented in [technical-safeguards.md](technical-safeguards.md).

### 8. Assurance Program

Company maintains an assurance program that verifies the design and operating effectiveness of its security controls through a combination of internal and external assessments.

- **Penetration testing.** Company commissions an external penetration test at least annually, scoped to its internet-facing applications and infrastructure. Findings are tracked to remediation by the Security Officer and reported to the Risk Review Committee.
- **Internal audit / control assessment.** Company performs internal control assessments at least annually, focused on access reviews, change management, backup verification, and incident response readiness.
- **External attestation (SOC 2 / HITRUST).** Pursuit of SOC 2 Type II and/or HITRUST certification is under evaluation by the Security Officer and CEO; status is TBD. In the interim, Company relies on the assurance combination of annual penetration testing, internal control assessments, BAA-required attestations from subprocessors, and the annual HIPAA Security Risk Assessment described in §4.
- **Cyber liability insurance.** Company maintains cyber liability and data privacy insurance. The current carrier, coverage limits, and certificate are maintained by the Practice Manager / Finance and referenced in [incident-and-breach-response.md](incident-and-breach-response.md) and [operational-safeguards.md](operational-safeguards.md) §5.
- **Assurance reports repository.** Pentest reports, control assessment reports, attestations, and the cyber-insurance certificate are stored in the `assurance/` folder (and/or the corresponding Google Workspace location); pointers are listed in the repository [README.md](../README.md).

### 9. Compliance & Ethics

Company maintains a compliance and ethics posture covering its regulatory obligations (HIPAA, state privacy laws, employment law, clinical regulation) and its ethical commitments to patients, personnel, and partners.

- **Code of Conduct.** Company's Code of Conduct (location: TBD — under development) sets baseline expectations for honesty, integrity, conflict-of-interest disclosure, and respectful conduct. Until formally adopted, this Policy together with the HR onboarding materials governs.
- **Whistleblower / good-faith reporting channel.** Personnel may report suspected violations of law, policy, or ethical standards in good faith to the Privacy Officer or the CEO. Reports may be made anonymously. Retaliation against any personnel member for a good-faith report is prohibited and is itself subject to the Sanctions provisions in §V.
- **Fraud reporting channel.** Suspected financial fraud, billing fraud, or misappropriation may be reported to the CEO or, where the CEO is implicated, to the Board of Directors. Suspected billing fraud involving patient PHI is additionally a privacy matter and is handled jointly with the Privacy Officer.

### 10. Reporting & Cadence

- **Risk assessment results** are reported to the Risk Review Committee within 30 days of completion. If material risks are identified, the Risk Review Committee reports them to the Board of Directors (or a committee designated thereby).
- **Annual privacy & security report** is delivered to the CEO at least annually, summarizing the prior year's risk assessment results, incident summary, breach summary (if any), audit and pentest results, training completion, vendor risk highlights, and the coming year's priorities.
- **Quarterly cadence** for Risk Review Committee meetings, with topical agenda rotation across risk, incident review, vendor risk, and metrics. Cross-reference the compliance calendar in [README.md](../README.md).
- **Event-driven reporting** for material incidents, breaches, regulator inquiries, vendor compromises, or significant control failures is escalated to the CEO immediately and to the Board as warranted.

## IV. Training & Awareness Program

This section is the canonical Training & Awareness Program for Company information privacy and security. Other Company policies that reference training shall be read as pointing here.

**(a) Initial training on hire.** All personnel (employees, contractors, licensed professionals, and other workforce members) shall complete HIPAA privacy and security training prior to being granted access to PHI or to any system that creates, receives, maintains, or transmits PHI. Initial training covers, at minimum: the Notice of Privacy Practices; permitted uses and disclosures (including Minimum Necessary); patient rights; the Acceptable Use Policy; password and authentication standards; phishing and social-engineering awareness; incident and breach reporting; sanctions; and the location of Company's policies.

**(b) Annual refresh.** All personnel shall complete annual refresher training. The refresh updates personnel on policy changes, lessons learned from incidents, and current threats. Annual refresh completion is tracked by the Privacy Officer.

**(c) Role-specific training.** Personnel in roles with elevated access or responsibility shall complete additional, role-specific training, including:

- Incident-response tabletop exercises for designated incident-response personnel.
- Administrator / privileged-access training for personnel with administrative privileges.
- Developer / SDLC training for engineering personnel (see [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md)).
- BAA / vendor management training for personnel who onboard or oversee vendors (see [vendor-and-business-associates.md](vendor-and-business-associates.md)).

**(d) Event-driven training.** Following any material policy change, any reportable breach, or any significant control failure, the Privacy Officer may require targeted retraining for affected personnel or for the entire workforce.

**(e) Completion tracking & records.** The Privacy Officer owns the training register, tracks completion by personnel and by module, and follows up on overdue completion. Training records are retained per §6 (HR records / per state law).

## V. Sanctions

Any personnel member who violates a Company information security or privacy policy will be subject to disciplinary action, up to and including termination of employment or engagement, in accordance with Company HR policy. Severity is assessed based on intent, the nature of the data and systems involved, and impact on patient privacy and Company information security. Sanctions are documented and tracked by the Privacy Officer per 45 CFR §164.530(e).

## VI. References

- 45 C.F.R. § 164.308(a)(1) — Security management process (risk analysis, risk management, sanctions, information system activity review)
- 45 C.F.R. § 164.308(a)(2) — Assigned security responsibility (Security Officer designation)
- 45 C.F.R. § 164.308(a)(1)(ii)(A) — Risk analysis (required)
- 45 C.F.R. § 164.308(a)(1)(ii)(B) — Risk management (required)
- 45 C.F.R. § 164.308(a)(8) — Evaluation
- 45 C.F.R. § 164.530(b) — Training
- 45 C.F.R. § 164.530(e) — Sanctions
- 45 C.F.R. § 164.530(j) — Documentation and record retention
- NIST Risk Management Guide for Information Technology Systems, Special Publication 800-30
- NIST Security Self-Assessment Guide for Information Technology Systems 800-26

Linked Millie policies:

- [hipaa-definitions.md](hipaa-definitions.md)
- [technical-safeguards.md](technical-safeguards.md)
- [operational-safeguards.md](operational-safeguards.md)
- [phi-use-and-disclosure.md](phi-use-and-disclosure.md)
- [patient-rights.md](patient-rights.md)
- [incident-and-breach-response.md](incident-and-breach-response.md)
- [vendor-and-business-associates.md](vendor-and-business-associates.md)
- [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md)
- [README.md](../README.md) (compliance calendar and responsibility matrix)

## VII. Definitions used in this Policy

Defined terms used in this Policy, including PHI, ePHI, IT System, Business Associate, Breach, and Workforce, have the meanings given to them in [hipaa-definitions.md](hipaa-definitions.md). The following additional terms are introduced or reconciled by this Policy:

- **Privacy Officer** — the Company role accountable for the HIPAA privacy program. Formerly referred to in legacy Company policies as the "Chief Privacy Officer"; both terms refer to the same role.
- **Security Officer** — the Company role accountable for the HIPAA security program. Formerly referred to in legacy Company policies as the "Chief Security Officer"; both terms refer to the same role.
- **Risk Review Committee** — the standing governance body responsible for the risk management process and procedures outlined in this Policy. The Committee consists of the Privacy Officer, the Security Officer, the CTO, and other personnel with subject-matter expertise as appointed by the Security Officer. Legacy Company documents have variously referred to this body as the "Risk Committee" or the "Risk Management Team"; all three terms refer to the same body, which is hereinafter the **Risk Review Committee**. (Note: [hipaa-definitions.md](hipaa-definitions.md) §II(r) will be updated separately to reflect this reconciliation.)
- **Enterprise Risk Management (ERM)** — Company's broader program for identifying, assessing, mitigating, and reporting operational, strategic, financial, regulatory, clinical, and reputational risk, of which the HIPAA security risk management process is one component (see §3).
- **Records Retention Schedule** — the schedule of record types and minimum retention periods set forth in §6, maintained by the Privacy Officer.
- **Code of Conduct** — Company's published statement of expectations for ethical and lawful conduct by personnel, referenced in §9. Location: TBD — under development.

## VIII. Revision history

| Date | Version | Author | Change |
|---|---|---|---|
| 2026-05-24 | 1.0 | Security Officer (Privacy Officer co-owner) | Consolidated IT-026 (Information Security & Data Governance Framework) and IT-007 (Risk Management) into a single landing policy. Reconciled "Chief Privacy Officer" → "Privacy Officer", "Chief Security Officer" → "Security Officer", and "Risk Committee" / "Risk Management Team" → "Risk Review Committee". Added Enterprise Risk Management framing (§3), Records Retention Schedule (§6), HR Security and Sanctions Anchor (§7), Assurance Program (§8), Compliance & Ethics (§9), reporting cadence (§10), canonical Training & Awareness Program (§IV), and canonical Sanctions clause (§V). Vendor and BAA content migrated to [vendor-and-business-associates.md](vendor-and-business-associates.md). |
