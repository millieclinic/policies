---
title: "Acceptable Use, Bring-Your-Own-Device, and Mobile Device Management"
sources: []
supersedes: []
last_reviewed: 2026-05-24
owner: "Security Officer"
status: "active"
---

# Acceptable Use, Bring-Your-Own-Device, and Mobile Device Management

> **New policy authored 2026-05-24** to address gaps in SIG Lite 2025 §M (Endpoint Security) and §D.2 (Acceptable Use). Closes the BYOD and MDM gaps surfaced by the ECH Security Assessment.

## I. Scope

This Policy applies to all Company personnel and all devices (Company-owned or personally-owned, mobile or non-mobile) used to access Company systems, Company data, or Protected Health Information (PHI). This Policy supplements (does not replace) the technical controls in [technical-safeguards.md](technical-safeguards.md).

## II. Policy

Company personnel are trusted with sensitive information — including PHI, patient records, financial data, and proprietary business information — and that trust comes with clear expectations. Personnel shall use Company systems and any device that touches Company data in a lawful, ethical, professional, and security-conscious manner. Personally-owned devices ("BYOD") may be used to access Company systems only when registered, enrolled in Company-managed Mobile Device Management (MDM), and configured to meet the minimum standards in this Policy. All devices that access PHI — whether Company-owned or BYOD — must be enrolled in MDM so Company can enforce encryption, screen-lock, and remote-wipe of Company data. Personnel retain ownership of personal data on BYOD devices; Company will not access, view, or wipe personal content. Violations may result in disciplinary action up to and including termination, and may trigger a breach assessment. This Policy is reviewed at least annually by the Security Officer.

## III. Procedure

### A. Acceptable Use of Company Systems

Acceptable Use applies to email, calendar, chat (Slack), file storage (Google Workspace, 1Password), the Millie application, the EMR(s), and every other platform listed in [platform-and-access-matrix.md](platform-and-access-matrix.md).

**1. Internet use.** Personnel may use Company internet access for legitimate business purposes. Incidental personal browsing (e.g., a news site at lunch) is permitted, provided it does not interfere with job duties, consume excessive bandwidth, or expose Company systems to risk. Personnel shall not access sites that distribute malware, host pirated content, or display sexually explicit, hateful, or otherwise unlawful material from any device connected to Company systems.

**2. Email.** Company email is for Company business. Personnel shall:
- Not auto-forward Company email to a personal account.
- Not send PHI to any address that is not a Company-issued account or a Business Associate's secured channel (see [hipaa-business-associate-agreement.md](hipaa-business-associate-agreement.md)).
- Treat unexpected attachments and links as suspicious; report suspected phishing to the Security Officer.
- Not use Company email to register for unrelated personal services.

**3. Social media.** Personnel are welcome to maintain personal social media presences. When doing so:
- Never post PHI, patient photos, or patient stories — even with names removed.
- Do not represent yourself as speaking for Company unless authorized in writing by the Privacy Officer or Company leadership.
- When discussing your role at Company on a personal account, include a "views are my own" disclaimer.
- Official Company channels are operated only by personnel designated by Company leadership.

**4. Personal use of Company systems.** Incidental personal use of Company laptops, email, and chat is permitted within reason (e.g., scheduling a personal appointment, paying a bill). The following are **prohibited** regardless of how "personal" the use feels:
- Storing personal media libraries (movies, music, large photo archives) on Company devices.
- Running a side business or personal commercial venture from Company systems.
- Cryptocurrency mining or any activity that consumes Company compute/network resources for personal gain.
- Installing games, streaming software, or other non-business applications without IT approval.

**5. Prohibited activities.** Personnel shall not:
- Engage in any illegal activity using Company systems or any device that accesses Company data.
- Harass, threaten, discriminate against, or bully colleagues, patients, vendors, or any third party (via email, chat, or any other channel).
- Violate intellectual property rights — no pirated software, no unlicensed media, no copying competitor materials without permission.
- Install unauthorized software, browser extensions, or AI plugins on Company devices or on BYOD devices used to access PHI. Approved software is listed in [platform-and-access-matrix.md](platform-and-access-matrix.md); requests go to the Security Officer.
- Circumvent, disable, or attempt to bypass any security control (antivirus, MDM, MFA, VPN, screen lock, audit logging, etc.).
- Share account credentials with any other person, including colleagues, family members, or contractors. Each personnel member is responsible for activity under their account.
- Submit PHI, patient identifiers, or proprietary Company information to any AI tool, public LLM, or external service that is not on the approved list and does not have a Business Associate Agreement on file. When in doubt, ask the Security Officer before pasting.

**6. Company monitoring rights.** Company reserves the right to monitor, log, and audit use of Company systems and Company-issued devices for security, compliance, and operational purposes. Personnel should have no expectation of privacy in Company-owned data, Company email, Company chat, or activity on Company-managed systems. For BYOD, monitoring is limited to the Company-managed work container and Company applications — see §III(C)(4).

**7. Confidentiality.** PHI and Company-confidential information remain confidential during and after employment. Personnel shall not disclose, copy, screenshot, photograph, or remove PHI or Company-confidential information except as required to perform assigned duties.

### B. Bring-Your-Own-Device (BYOD)

**1. Eligibility.** Personnel may request to use a personally-owned smartphone, tablet, or laptop to access Company systems or PHI only after: reviewing this Policy, submitting the BYOD Enrollment Form (Appendix A), and receiving written approval from the Security Officer. Personnel who do not wish to use a personal device for Company work may request a Company-issued device instead. No personnel member is required to enroll a personal device in MDM as a baseline employment condition; however, certain roles requiring mobile access (on-call clinicians, field staff) may require BYOD enrollment **or** acceptance of a Company-issued device.

**2. Registration and inventory.** Before any BYOD device touches PHI, the device must be enrolled in the Company MDM (see §III(C)), recorded in the Company device inventory (make, model, OS version, personnel member), and re-confirmed annually as still active and still meeting standards.

**3. Minimum device standards.** A personal device used for Company work must meet **all** of the following:
- **Operating system:** Apple iOS/iPadOS/macOS, Google Android, Microsoft Windows, or Chrome OS — currently supported by the vendor with security updates.
- **Version:** running an OS major version the vendor still supports (typically current or current-minus-one).
- **Full-disk encryption:** enabled (FileVault on macOS; BitLocker on Windows; default on iOS, modern Android, and Chrome OS).
- **Screen lock:** strong passcode, biometric, or password required; auto-lock within 5 minutes for laptops and 2 minutes for phones/tablets.
- **OS security updates:** installed within **14 days** of vendor release.
- **MFA:** enabled on all Company accounts accessed from the device.
- **No jailbreak / no root:** devices modified to remove vendor security boundaries are prohibited.
- **Anti-malware:** Company-approved endpoint protection installed on Windows and macOS laptops.

**4. Acceptable Use applies on BYOD.** Every rule in §III(A) — illegal activity, harassment, IP, unauthorized software, credential sharing, AI/LLM rules, confidentiality — applies to a personal device whenever it is being used for Company work or accessing Company data.

**5. Liability and reimbursement.** Personnel are responsible for the cost, maintenance, repair, and replacement of personally-owned devices. Company does not reimburse personal device or carrier plan costs unless specifically authorized in writing as part of a stipend program. Company is not liable for loss of personal data resulting from a remote wipe of Company data, theft, damage, or technical failure of a personal device. Personnel are strongly encouraged to maintain a personal backup of personal data; Company does not back up personal content on BYOD devices.

### C. Mobile Device Management (MDM)

MDM enrollment is **required** for any device — Company-owned or BYOD — that accesses PHI or is used to log in to Company systems that store PHI.

**1. MDM vendor.** The MDM platform is TBD pending vendor selection by the Security Officer. Until a vendor is in place, the Security Officer maintains a manual device register and enforces the standards in §III(B)(3) by attestation; full MDM enrollment is expected within 90 days of vendor go-live.

**2. MDM capabilities.** The MDM platform will, at minimum, be able to:
- Enforce device encryption and screen-lock configuration.
- Require minimum OS versions and block non-compliant devices from Company systems.
- Push Company-approved applications and revoke them on departure.
- **Remote-wipe Company data** from the device (selective wipe on BYOD; full wipe permitted on Company-owned).
- Report compliance status (encryption on/off, OS version, MFA enrollment) to the Security Officer.
- Detect jailbroken/rooted devices and block access.

**3. Enrollment process and timeline.**
- Company-owned devices are enrolled by IT at issuance, before the device is handed to the personnel member.
- BYOD devices must be enrolled **within 5 business days** of approval and before first PHI access.
- New hires must complete enrollment for any device that will access PHI within their first 7 calendar days, prior to PHI access being granted.

**4. Privacy notice — what MDM can and cannot see.** Personnel using BYOD have a right to understand what Company can and cannot observe. Through MDM, Company **can** see device make/model/OS/compliance status (encryption, screen lock, OS update level); push, update, and remove Company-approved applications and the work container; and remote-wipe Company data within the work container. Company **cannot**, through MDM, read personal email, personal SMS, personal photos, or personal browsing history; see personal contacts, personal calendar, or personal app data outside the work container; track device location outside an explicit "find my device" action triggered through the Security Officer when a device is lost; or listen to calls or read iMessages/SMS.

**5. Separate work container on BYOD.** Where the MDM platform supports it (e.g., iOS managed apps, Android Work Profile), Company will use a separate work container so personal and Company data are technically segregated. Company management actions are scoped to the work container.

### D. Personal-vs-Company Data Separation on BYOD

**1. Work data stays in Company-approved apps.** PHI and Company data may be accessed only through Company-approved applications and the work container (Gmail/Google Workspace via managed app, Slack, EMR mobile apps where applicable, the Millie application, 1Password, etc.). Approved apps are listed in [platform-and-access-matrix.md](platform-and-access-matrix.md).

**2. No PHI in personal channels.** PHI shall **never** be sent or stored in personal email accounts, personal cloud storage (personal iCloud Drive, personal Google Drive, Dropbox, OneDrive personal), personal messaging apps (iMessage, SMS, WhatsApp, Signal, Messenger, Telegram), or personal note-taking apps not on the approved list.

**3. No photos or screenshots of PHI.** Personnel shall not photograph PHI displayed on any screen, nor screenshot PHI to a personal photo library or personal cloud-backed camera roll. Screen captures for legitimate Company purposes must be stored only in Company-approved locations and deleted from personal libraries.

**4. No copy-paste of PHI into personal apps.** The MDM work container should prevent this where supported; where it cannot, personnel shall not manually copy PHI from a Company app into a personal app, including personal AI assistants.

### E. Lost / Stolen Device Protocol

A lost or stolen device that may have accessed PHI is treated as a potential breach.

**1. Report within 24 hours.** Personnel must report a lost, stolen, or unaccounted-for device to the Security Officer within **24 hours** of discovery, even if the personnel member believes encryption and screen-lock will protect the data. Off-hours reports may be made via Slack DM to the Security Officer or via the on-call Company contact.

**2. Remote wipe.** Upon a credible lost/stolen report, the Security Officer is authorized to trigger a remote wipe of Company data from the device immediately and suspend the personnel member's Company accounts pending recovery, password reset, and MFA re-enrollment from a known-good device. For BYOD, the wipe is scoped to Company data and the work container.

**3. Risk assessment for breach determination.** The Security Officer (with the Privacy Officer) shall complete a risk assessment under [incident-and-breach-response.md](incident-and-breach-response.md) to determine whether the loss constitutes a Breach of Unsecured PHI requiring notification under 45 CFR §§164.400–414. Factors include whether the device was encrypted, whether the screen was locked, what PHI was accessible, and whether a remote wipe completed successfully.

**4. Document.** The event, the assessment, and any corrective action are recorded in the Security Incident Log per [hipaa-security-incidents.md](hipaa-security-incidents.md).

### F. Offboarding

**1. Company-owned devices** must be returned to Company within 5 business days of the personnel member's last day, in working condition. IT performs a full wipe, re-images the device, and updates the inventory.

**2. BYOD remote wipe of Company data.** On the personnel member's last day, the Security Officer triggers a selective wipe of Company data, removes Company-managed applications, and revokes MDM enrollment. Personal data, personal apps, and personal accounts are not affected.

**3. Personal data preservation.** Personnel are responsible for any personal backup of personal data prior to offboarding. Company is not responsible for loss of personal data caused by an MDM action, an account revocation, or removal of a managed app, and is not obligated to provide a copy of any data from a BYOD device.

**4. Final attestation.** As part of offboarding, the personnel member signs an attestation confirming that all Company devices have been returned (Company-owned), all Company data has been removed from any BYOD device and from any personally-controlled storage location (personal cloud accounts, USB drives, personal email), and no PHI has been retained in personal possession in any form. The attestation is retained by HR and the Privacy Officer.

## IV. Training & Awareness

All personnel shall complete Acceptable Use and BYOD training at the time of employment or engagement, before any device is enrolled or any PHI is accessed, with annual updates thereafter, in accordance with the [governance-and-risk-management.md](governance-and-risk-management.md) Training Program.

## V. Sanctions

Any personnel member who violates this Policy will be subject to disciplinary action, up to and including termination of employment or engagement, in accordance with Company HR policy. Violations involving exposure of PHI on unmanaged or unauthorized devices may trigger a breach assessment under [incident-and-breach-response.md](incident-and-breach-response.md). Sanctions are documented and tracked by the Privacy Officer.

## VI. References

**Regulatory / standards:**
- 45 CFR §164.310(d) — HIPAA Security Rule, Device and Media Controls.
- 45 CFR §164.310(b) — HIPAA Security Rule, Workstation Use.
- 45 CFR §164.530(e) — HIPAA Privacy Rule, sanctions for personnel violations.
- NIST SP 800-124 Rev. 2 — Guidelines for Managing the Security of Mobile Devices in the Enterprise.
- NIST SP 800-114 Rev. 1 — User's Guide to Telework and Bring Your Own Device (BYOD) Security.

**Shared Assessments SIG Lite 2025 questions closed by this Policy:**
- §D.2 — Acceptable Use Policy.
- §M.1.3 — Mobile Device Management program.
- §M.1.5 — Non-company-managed computing devices.
- §M.1.6 — BYOD mobile devices with access to scoped data.

**Linked Millie policies:**
- [technical-safeguards.md](technical-safeguards.md), [hipaa-business-associate-agreement.md](hipaa-business-associate-agreement.md), [incident-and-breach-response.md](incident-and-breach-response.md), [hipaa-security-incidents.md](hipaa-security-incidents.md), [governance-and-risk-management.md](governance-and-risk-management.md), [platform-and-access-matrix.md](platform-and-access-matrix.md), [hipaa-definitions.md](hipaa-definitions.md).

## VII. Definitions used in this Policy

General defined terms (PHI, Workforce, Workstation, Business Associate, Breach, Unsecured PHI, etc.) follow the definitions in [hipaa-definitions.md](hipaa-definitions.md). The following terms are specific to this Policy:

- **BYOD (Bring-Your-Own-Device):** any smartphone, tablet, laptop, or other computing device owned by an individual personnel member (not Company) and used to access Company systems, Company data, or PHI.
- **MDM (Mobile Device Management):** a Company-administered platform that applies security configuration, enforces compliance, manages Company applications, and can remote-wipe Company data on enrolled devices.
- **Work Container:** the logically-segregated portion of a BYOD device — managed apps, managed email profile, work profile, or equivalent — within which Company data resides and to which Company management actions are limited.
- **Remote Wipe:** a Company-initiated action that removes Company data and Company-managed applications from a device. On Company-owned devices a full-device wipe is permitted; on BYOD the wipe is scoped to the Work Container.

## VIII. Revision history

| Date | Author | Change |
|---|---|---|
| 2026-05-24 | Security Officer | Initial draft authored to close ECH Security Assessment gaps surfaced in SIG Lite 2025 §D.2 (Acceptable Use), §M.1.3 (MDM), §M.1.5 (non-Company devices), and §M.1.6 (BYOD with scoped data). |

## Appendix A — BYOD Enrollment Form

Submit this form to the Security Officer before enrolling a personal device. The Security Officer countersigns once the device has been MDM-enrolled and recorded in the device inventory.

```
MILLIE, INC. — BYOD ENROLLMENT FORM

Personnel name:        ____________________________________
Role / title:          ____________________________________
Manager:               ____________________________________
Date of request:       ____________________________________

DEVICE INFORMATION
Device type (phone / tablet / laptop):   ______________________
Make:                                     ______________________
Model:                                    ______________________
Operating system and version:             ______________________
Serial number or IMEI:                    ______________________
Primary use case for Company work:        ______________________

ACKNOWLEDGEMENTS — initial each line

____  I have read the Acceptable Use, BYOD, and MDM Policy in full.
____  I agree to enroll this device in Company-managed MDM and keep
      it enrolled for as long as I use it for Company work.
____  I authorize Company to remote-wipe Company data from this
      device in the event of loss, theft, suspected compromise, or
      my separation from Company.
____  I understand Company will not access my personal data,
      personal email, personal photos, personal messages, personal
      contacts, personal location, or personal app data via MDM.
____  I will report a lost or stolen device to the Security Officer
      within 24 hours.
____  I will not store PHI in personal email, personal cloud
      storage, personal messaging apps, or my personal photo
      library, and I will not photograph or screenshot PHI to a
      personal device library.
____  I will keep this device's OS and security updates current
      (within 14 days of vendor release), keep encryption and
      screen lock enabled, and not jailbreak or root the device.
____  I understand Company is not responsible for the cost,
      maintenance, repair, or replacement of this device, or for
      personal data loss caused by an MDM action, device failure,
      or remote wipe.

SIGNATURES
Personnel signature:        _______________________  Date: __________
Security Officer signature: _______________________  Date: __________

MDM enrollment confirmed (Security Officer use only)
  Enrollment date:          __________
  Device inventory ID:      __________
  Initial compliance check: [ ] Pass   [ ] Fail (notes: _________ )
```
