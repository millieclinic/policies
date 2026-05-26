---
title: "Incident & Breach Response"
sources: ["hipaa-security-incidents.md", "hipaa-breach-notification.md"]
supersedes: ["IT-009", "L-004"]
last_reviewed: 2026-05-24
owner: "Security Officer (Privacy Officer for breach notification)"
status: "active"
---

# Incident & Breach Response

> **Sources.** Consolidated from: `hipaa-security-incidents.md` (IT-009 Security Incident Management Policy) and `hipaa-breach-notification.md` (L-004 Breach Notification Policy). Originals archived in `New Policy Docs/_archive/`.

## I. Scope

This Policy applies to all facilities and locations owned, operated, or managed by Millie, Inc. ("Company") and all Company personnel, and to any security incident, suspected security incident, or suspected/confirmed breach of Protected Health Information regardless of where the incident originates (Company systems, personal devices used for Company work, third parties, or paper records).

## II. Policy

It is Company's policy to ensure the prompt identification, reporting, investigation, containment, and resolution of security incidents in order to safeguard Protected Health Information ("PHI"), prevent the recurrence of similar events, and meet all legal obligations to notify affected individuals and regulators when a Breach of Unsecured PHI is determined to have occurred. The Security Officer is responsible for technical incident response. The Privacy Officer is responsible for breach determination, individual notification, and regulator notification under the HITECH Act and applicable state law. Personnel must report any observed or suspected security incident or potential Breach promptly and must not attempt to resolve incidents on their own. All response actions, evidence, and decisions are recorded in a tamper-evident incident log retained per the Information Security Framework retention schedule. Failure to report an incident within the timelines stated in this Policy is subject to sanctions under Section V.

## III. Procedure

### 1. Security Incident Identification & Reporting

All personnel shall promptly report to the Security Officer (or designee) any observed or suspected (i) security weaknesses or threats to the IT System, (ii) violations of Company's security policies, and (iii) events that could compromise the integrity, confidentiality, or availability of PHI. If the security incident could be considered a Breach of HIPAA, the Security Officer shall immediately notify the Privacy Officer. The following non-exhaustive list of incidents are to be reported to the Security Officer or designee:

- Actual or suspected loss or unauthorized disclosure of PHI;
- Unauthorized access to or modification of PHI;
- Unusual behavior of the IT System (e.g., missing files, frequent crashes, misrouted messages);
- Unauthorized use of the IT System;
- Loss, theft, or disclosure of a password or other access control mechanism;
- Theft or loss of, or material damage to, Company property;
- Inability to log on to the IT System or any denial of service to a Company account; or
- Threatened or actual introduction of a virus.

Any personnel member uncertain whether a particular event is reportable should contact their supervisor. **The Security Officer shall investigate all reports within 24 hours of receipt.**

### 2. Incident Triage & Classification

Upon learning of a reported event, the Security Officer (or designee) performs an initial triage to determine whether a bona fide security event has occurred and, if so, to classify it. The Security Officer assigns each verified incident one of the following severity tiers and confirms whether it potentially involves PHI:

- **Low** — isolated event, no PHI exposure, no service impact (e.g., single failed phishing attempt blocked at the gateway).
- **Medium** — limited internal impact or near-miss involving PHI; containment expected within the business day.
- **High** — confirmed unauthorized access, malware, or service disruption affecting systems that store or transmit PHI; immediate escalation to the Privacy Officer and Risk Review Committee.
- **Critical** — known or strongly suspected Breach of Unsecured PHI, ransomware, or active intrusion; immediate engagement of executive leadership, legal counsel, and (if applicable) the cyber liability insurance carrier.

Any incident classified Medium or higher that potentially involves PHI is concurrently reported to the Privacy Officer to begin the parallel Breach Determination workflow in §7 below.

### 3. Incident Investigation & Containment

The Security Officer, in conjunction with the Privacy Officer, is responsible for managing Company's response to all reported security incidents. Upon learning of a security incident, the Security Officer shall conduct a preliminary investigation within 24 hours of the reported incident to ascertain whether a bona fide security event has occurred. If a security incident is verified, the Security Officer shall promptly determine its nature and scope and shall promptly report the matter to the Privacy Officer, who shall report the incident to the Chief Executive Officer and others as appropriate and required. The Security Officer shall then designate any additional personnel, third parties, and resources necessary to respond, obtaining any required approvals from the Privacy Officer or Chief Executive Officer.

Regardless of the nature and scope of the incident, Company's response shall follow this order of priorities, as applicable: (1) protection of human life and safety; (2) protection of PHI against unauthorized disclosure, destruction, or modification; (3) prevention or mitigation of damage to Company's assets; (4) notification of any third parties that may be adversely affected (only with legal counsel approval); (5) minimizing disruption of Company's computing resources and processes; and (6) reporting the incident to law enforcement and insurance carriers (only with legal counsel approval).

Personnel shall not discuss specific security incidents with other individuals (including other personnel) except as permitted under this Policy, and shall not attempt to resolve a suspected security incident without authorization from the Security Officer and Privacy Officer. All personnel shall cooperate with the Security Officer and Privacy Officer throughout the incident response process.

**AWS / cloud-specific playbook.** For incidents involving Company workloads hosted on AWS or other cloud infrastructure (compromised IAM credentials, suspicious GuardDuty findings, anomalous CloudTrail events, S3 exposure, etc.), the Security Officer shall follow the cloud-specific incident response procedures documented in [network-and-cloud-security.md](network-and-cloud-security.md), which include credential rotation, snapshot preservation, account isolation, and CloudTrail evidence collection steps. The cloud playbook supplements — it does not replace — the priorities and authorities in this Section.

### 4. Tamper-Evident Incident Log

The Security Officer shall maintain a written record of all reported incidents and the details of the response, including, as applicable: type of incident; date of incident; date reported to the Security Officer; date reported to Company by a Business Associate (if applicable); how the incident was identified; all internal and external discussions (parties, dates, times, content — except privileged content, which is logged without substance); copies of security audit logs and records; all remedial actions implemented and their dates and results; containment actions (e.g., third-party notifications, accounting of any PHI disclosures per [patient-rights.md](patient-rights.md)); law enforcement agencies notified and dates of notification; correspondence with insurance carriers; and date the incident was closed.

**Tamper-evident requirement.** All actions taken during an incident investigation shall be recorded in a tamper-evident log (write-once, signed, or version-controlled). Logs are retained per the Information Security Framework retention schedule and shall not be modified after closure. Acceptable implementations include a version-controlled repository with signed commits, an append-only ticketing system with immutable audit history, or a write-once object store with cryptographic integrity verification. Any post-closure correction must be made as a new dated entry referencing the original, never by overwriting the prior record.

### 5. Post-Incident Analysis & Annual Report to CEO

**Post-incident analysis.** After an incident is resolved or contained, the Security Officer shall prepare a written report for the Privacy Officer covering: a detailed description of the incident and how it occurred; the vulnerabilities exploited; how the incident was resolved or contained; whether existing security policies were adequate or require updating; any unresolved vulnerabilities; an inventory update for loss/damage to Company property; and any law enforcement agencies notified. The Privacy Officer shall forward the report to the Chief Executive Officer, as appropriate.

**Annual report.** The Security Officer and the Privacy Officer will endeavor to prepare an annual privacy and security report for submission to the Chief Executive Officer, which shall include: all incidents reported and responded to during the prior year (including breaches); security vulnerabilities that were corrected; the costs associated with each security incident; identification of any existing security weaknesses; and recommendations to improve Company's security defenses and limit the frequency, damage, and cost of future occurrences.

### 6. MSSP / Outsourced Incident Response

Millie does **not** currently outsource its incident response function to a Managed Security Service Provider ("MSSP") or third-party incident response retainer. Incident response is performed in-house by the Security Officer, with support from the Privacy Officer, the engineering team, legal counsel, and (where applicable) the cyber liability insurance carrier's pre-approved forensics vendors. If and when Millie engages an MSSP or executes an external incident response retainer, this Section will be updated to identify the provider, the scope of services, the activation procedure, and the Business Associate Agreement reference governing PHI handling.

### 7. Breach Determination & Notification

#### 7.1 Discovery of a Breach

**Reporting Breaches.** All personnel must immediately inform Company's Privacy Officer of any potential Breach as soon as possible, but **in no event later than 48 hours** after he or she becomes aware of the Breach. While investigating any potential Breach, the Privacy Officer shall fill out the internal Breach Report Form (see [forms/breach-notification-hhs-template.md](forms/breach-notification-hhs-template.md)). Business Associates of Company shall report all potential Breaches in accordance with their Business Associate Agreements. Company shall require additional follow-up by its Business Associates as necessary and appropriate and directed by the Privacy Officer.

**Date of Discovery.** A Breach is considered to have occurred at the time of the impermissible access, use, or disclosure of Unsecured PHI (the "Date of Discovery"). A Breach is not, however, considered to have been discovered, for the purposes of the HITECH Act, until:

- The first day the Breach is known to Company or its personnel; or
- The first day that Company, by exercising reasonable diligence, should have known of the Breach.

#### 7.2 Investigation & Breach Determination

After receiving a report of a potential Breach, the Privacy Officer will promptly investigate the circumstances and will involve the Security Officer and any other Company representatives necessary. The Privacy Officer will, to the extent possible: determine whether there was an impermissible access, use, or disclosure of PHI; identify who impermissibly accessed, used, or received PHI and to whom it was potentially disclosed; determine whether the PHI was Unsecured PHI; identify the type and amount of PHI involved; and determine what steps have been or should be taken to mitigate risk (e.g., confidentiality agreement with the recipient, obtaining return of the PHI, reporting to police).

In some situations in which it is apparent that a Breach has occurred, initial individual notifications may need to be sent prior to the completion of the investigation. The Privacy Officer is responsible for determining the appropriate timing of notification based on the requirements of HITECH.

**Breach determination.** Whenever a potential Breach is reported, a Breach is presumed to have occurred, unless it is demonstrated through a documented risk assessment that there is a **low probability** that the PHI has been compromised. The risk assessment must consider, at minimum: (i) the nature and extent of the PHI involved, including types of identifiers and likelihood of re-identification; (ii) the unauthorized person who used the PHI or to whom the disclosure was made; (iii) whether the PHI was actually acquired or viewed; and (iv) the extent to which the risk to the PHI has been mitigated. If the assessment supports a low-probability conclusion, the Privacy Officer documents the determination and notification is not required. Otherwise, individuals will be notified as described below. State-specific notification thresholds (see Section 8) are reviewed in parallel with the federal determination.

**Exceptions.** The following do not constitute a Breach that requires notifications to individuals under HITECH:

- The unintentional acquisition, access, or use of PHI by an authorized personnel member or another individual acting under Company's authority if the acquisition, access, or use was made in good faith, within the scope of such individual's authority, and does not result in further unauthorized Use or Disclosure.
- The inadvertent disclosure of PHI from one person to another person, if both persons were authorized to access the PHI at the same covered entity, organized health care arrangement, or Business Associate, so long as the PHI is not further acquired, accessed, used, or disclosed in an unauthorized manner.
- The unauthorized disclosure of PHI when Company or a Business Associate has a good faith belief that the person to whom disclosure was made would not reasonably have been able to retain the information.

#### 7.3 Notification of Affected Individuals

**Time frame for notification.** If it is determined that notification is required, such notification shall be made **without unreasonable delay, but in no event more than 60 days from the Date of Discovery of the Breach.** Company may delay Breach notifications if a law enforcement official requests a delay, subject to the following:

- If the request is in writing, the delay may be for as long as requested.
- If it is an oral request, the delay may be for up to 30 days unless a further delay is requested in writing. All oral requests shall be documented by Company including the name of the official making, and the date of, the request.

**Content of the notification.** The Privacy Officer will be responsible for arranging the preparation of the required notices of Breaches to individuals using the template at [forms/breach-notification-individual-letter.md](forms/breach-notification-individual-letter.md). Such notifications must be written in plain language, at an appropriate reading level, using clear language and syntax, and must include the following information:

- A brief description of what happened, including the date of the Breach and Date of Discovery of the Breach, if known;
- A description of the types of Unsecured PHI involved in the Breach;
- Any steps individuals should take to protect themselves from potential harm resulting from the Breach;
- A brief description of Company's efforts to investigate the Breach, mitigate harm to individuals, and protect against further Breaches; and
- Contact information for individuals to ask questions or learn about the Breach, which must include a toll-free number, an email address, website, or postal address.

**General method of notification.** Notice must be provided in written form by certified mail or hand-delivered to the last known address. For a minor or an individual who lacks legal capacity, notice may go to the parent or personal representative. If the individual is deceased and Company has the address of the next of kin or personal representative, notice must be sent to them (substitute notice to next of kin is not required if contact information is missing or out of date). When the Privacy Officer determines there is a possibility of imminent misuse of Unsecured PHI, urgent notice may be given by telephone, e-mail, or other means in addition to written notice.

**Substitute notice.** Substitute notice is provided when Company has insufficient or out-of-date contact information. For fewer than 10 affected individuals, an alternative form (telephone, e-mail, newspaper, or website) is used. For 10 or more, Company provides both: (a) conspicuous posting for 90 days on the website homepage (or noticeable hyperlink) **or** conspicuous notice in major print or broadcast media in geographic areas where affected individuals likely reside; **and** (b) a toll-free number, active for 90 days, through which individuals can learn whether their Unsecured PHI was involved.

#### 7.4 Notifications to Authorities

**Annual notification to the Secretary.** The Privacy Officer will maintain documentation of Breaches involving less than 500 individuals. The Privacy Officer will submit to the Secretary of the U.S. Department of Health and Human Services, on an annual basis, information regarding Breaches that occurred during the preceding year, no later than 60 days after the end of each calendar year in which the Breach is discovered. The information included in the Breach log will include all of the information included in the Breach notices to individuals.

**Notification to DHHS and the media when 500 or more affected individuals are involved.** If the Breach involves 500 or more individuals of a State, notice must be given to the Secretary of DHHS at the same time that notices are given to individuals. Notice must also be provided to prominent media outlets in the State through a press release, using the template at [forms/breach-notification-media-template.md](forms/breach-notification-media-template.md).

- Notification to the media must include the same information included in written notices to individuals.
- Notification to the media will be made without unreasonable delay, and in no case later than 60 calendar days following the Date of Discovery of the Breach.

**Notification to insurance company.** The Privacy Officer shall determine whether Company's cyber liability insurance provider shall be notified of any Breach, and shall engage them to assist with any notifications, investigations and mitigation activities, as appropriate.

#### 7.5 Mitigation, Complaints, Sanctions, and Accounting

- **Mitigation.** Company will make reasonable efforts to mitigate the effects of a Breach and to reduce harm to individuals in accordance with its privacy and security policies, which may include as appropriate: providing credit monitoring services to individuals, retraining personnel on privacy policies, or implementing new technical or physical safeguards to protect the privacy of PHI.
- **Complaints.** If the Breach resulted from a complaint, the complaint must also be listed on Company's complaint log and the Internal Investigations & Corrective Action Policy will be followed.
- **Security incident overlap.** To the extent that a Breach involves a security incident, the Security Officer will be immediately informed and the procedures in Sections 1–5 of this Policy will be followed in parallel.
- **Sanctions.** If sanctions against a workforce member result from a Breach, the Internal Investigations & Corrective Action Policy will be followed (see also Section V below).
- **Accounting.** If the Breach resulted from a disclosure, such Breach must be listed on Company's accounting of disclosures log for each individual affected by the Breach. See [patient-rights.md](patient-rights.md).

### 8. State-Specific Breach Notification Supplements

In addition to the federal HITECH requirements above, the Privacy Officer reviews state breach notification laws applicable to each affected individual's state of residence before issuing notifications. State laws may impose shorter timelines, different content requirements, attorney-general notification thresholds, or media notification triggers different from the federal rule. The Privacy Officer applies the **most stringent** applicable requirement.

**California (illustrative; representative of states where Millie operates).**

California law requires a business or state agency to notify any California resident whose unencrypted personal information, as defined, was acquired, or reasonably believed to have been acquired, by an unauthorized person. ([California Civil Code s. 1798.29(a)](http://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.29) [agency] and [California Civ. Code s. 1798.82(a)](http://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.82) [person or business].)

Any person or business that is required to issue a security breach notification to more than 500 California residents as a result of a single breach of the security system shall electronically submit a single sample copy of that security breach notification, excluding any personally identifiable information, to the Attorney General. ([California Civil Code s. 1798.29(e)](http://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.29) [agency] and [California Civ. Code s. 1798.82(f)](http://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.82) [person or business].)

Source: <https://oag.ca.gov/privacy/databreach/reporting>

For breaches affecting residents of states other than California, the Privacy Officer consults the current state-by-state matrix maintained by legal counsel (or an equivalent commercial reference) and documents the applicable trigger, timeline, content, and regulator-notification requirements in the incident file before notice is issued.

## IV. Training & Awareness

All personnel shall receive incident-recognition and reporting training at the time of employment or engagement, with annual updates thereafter, including a tabletop exercise at least quarterly for those in incident-response roles, in accordance with the [governance-and-risk-management.md](governance-and-risk-management.md) Training Program.

## V. Sanctions

Any personnel member who fails to report a known or suspected security incident or breach within the timelines stated in this Policy will be subject to disciplinary action, up to and including termination. Severity is assessed based on the magnitude of the incident and any aggravating factors (e.g., concealment, retaliation against reporters). Sanctions are documented and tracked by the Privacy Officer.

## VI. References

- 45 C.F.R. § 164.308(a)(6) — Security incident procedures
- 45 C.F.R. § 164.404 — Notification to individuals
- 45 C.F.R. § 164.406 — Notification to the media
- 45 C.F.R. § 164.408 — Notification to the Secretary
- 45 C.F.R. § 164.410 — Notification by a business associate
- 45 C.F.R. § 164.412 — Law enforcement delay
- 45 C.F.R. § 164.414 — Administrative requirements and burden of proof
- HITECH Act, Subtitle D — Privacy (Pub. L. 111-5, §§ 13400–13424)
- California Civil Code §§ 1798.29, 1798.82
- [governance-and-risk-management.md](governance-and-risk-management.md)
- [network-and-cloud-security.md](network-and-cloud-security.md)
- [patient-rights.md](patient-rights.md)
- [vendor-and-business-associates.md](vendor-and-business-associates.md)
- [hipaa-definitions.md](hipaa-definitions.md)

## VII. Definitions used in this Policy

Capitalized terms not defined here are defined in [hipaa-definitions.md](hipaa-definitions.md), including: **Breach**, **Disclosure**, **Date of Discovery**, **DHHS**, **PHI / Protected Health Information**, **Unsecured PHI**, and **Use**.

New terms used in this Policy:

- **Tamper-evident log.** A record of incident-response actions and evidence kept in a manner that prevents undetected alteration after the fact. Acceptable mechanisms include a version-controlled repository with signed commits, an append-only ticketing system with immutable audit history, or a write-once object store with cryptographic integrity verification. Corrections after log closure are recorded as new dated entries that reference, but do not overwrite, the prior record.
- **MSSP (Managed Security Service Provider).** A third-party provider that delivers outsourced monitoring, detection, and/or incident-response services on behalf of Company. Millie does not currently engage an MSSP for incident response (see Section III.6).

## VIII. Revision history

| Date | Version | Author | Change |
|---|---|---|---|
| 2022-05-18 | 1.0 | Privacy Officer | Original L-004 Breach Notification Policy. |
| 2022-07-01 | 1.1 | Privacy Officer | L-004 revised. |
| 2022-07-05 | 1.0 | Security Officer | Original IT-009 Security Incident Management Policy. |
| 2026-05-18 | 1.1 | Security Officer | IT-009 revised. |
| 2026-05-24 | 2.0 | Security + Privacy Officers | Consolidated IT-009 and L-004. Added Incident Triage & Classification (§III.2), AWS playbook pointer (§III.3), Tamper-Evident Log (§III.4, SIG J.14), MSSP statement (§III.6, SIG J.11), state-specific supplements (§III.8). Moved Exhibits B/C/D to `forms/`. Standardized officer titles. |

## Appendix A — Breach Notification Forms

Notification templates are maintained in `New Policy Docs/forms/` for editability. See:

- [forms/breach-notification-individual-letter.md](forms/breach-notification-individual-letter.md) — Sample letter to affected individuals (formerly Exhibit C).
- [forms/breach-notification-media-template.md](forms/breach-notification-media-template.md) — Media press-release template for breaches affecting 500+ individuals in a State (new; derived from §III.7.4 content requirements).
- [forms/breach-notification-hhs-template.md](forms/breach-notification-hhs-template.md) — Internal Breach Report Form / HHS submission worksheet (formerly Exhibit D, with Exhibit B Risk Assessment Form folded in).
