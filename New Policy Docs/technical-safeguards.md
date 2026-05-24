---
title: "Technical Safeguards — Access, Encryption, Endpoints, Remote Access, Device & Media"
sources: ["hipaa-encryption.md", "hipaa-passwords.md", "hipaa-remote-access.md", "hipaa-workstation-use.md", "privacy-policy.md (IT-004 content, lines 564–609 only)"]
supersedes: ["IT-001 Password Management", "IT-002 Workstation Use", "IT-004 Device & Media Management", "IT-005 Encryption", "IT-006 Remote Access"]
last_reviewed: 2026-05-24
owner: "Security Officer (CTO co-owner)"
status: "active"
---

# Technical Safeguards — Access, Encryption, Endpoints, Remote Access, Device & Media

> **Sources.** Consolidated from: `hipaa-passwords.md` (IT-001 Password Management), `hipaa-workstation-use.md` (IT-002 Workstation Use), `hipaa-encryption.md` (IT-005 Encryption), `hipaa-remote-access.md` (IT-006 Remote Access). Includes the rescued Device & Media Management content (Policy # IT-004) that previously existed only inside `privacy-policy.md`. Originals archived in `New Policy Docs/_archive/`.

## I. Scope

This Policy applies to all facilities and locations owned, operated, or managed by Millie, Inc. ("Company"), all Company personnel, and all information systems, software, hardware, and electronic media that create, receive, maintain, or transmit Protected Health Information (PHI), confidential Company information, or related credentials.

For purposes of this Policy, the term "personnel" includes all licensed professionals and staff who perform services on behalf of Company. The term "User" includes any personnel member or authorized third party with access to the Company IT System ("Company Computer Network" or "IT System").

## II. Policy

It is Company's policy to safeguard the confidentiality, integrity, and availability of PHI and other confidential information through layered technical safeguards: strong authentication, role-based access control, FIPS-validated encryption in transit and at rest, hardened endpoints and workstations, controlled remote access, and disciplined device and media management.

Access to the Company IT System is granted on a least-privilege basis and is conditioned on unique user identification, strong password or passcode construction, and multi-factor authentication wherever technologically feasible. All ePHI transmitted over open networks must be encrypted. All Company workstations, mobile devices, and electronic media — whether issued by Company or personally owned and used for Company business — must be configured, inventoried, and disposed of in accordance with this Policy. Remote access is permitted only with explicit authorization and is continuously monitored. All personnel must comply with this Policy as a condition of access; violations are subject to sanction under §V.

## III. Procedure

### 1. Access Control & Authentication (originally IT-001 Password Management; technical portions of IT-008 Safeguards)

**a. Unique user identification and role-based access.** All components of the Company Computer Network will be password protected. Such password protection may consist of "single-sign-on" technology. Any PHI residing on the Company Computer Network will not be accessible without the use of a unique personnel member identifier and password created in accordance with this Policy, though nothing in this Policy shall prevent the use of single-sign-on technology or processes to enable personnel to log onto one program with the login or password issued under another program. Access rights are granted on a least-privilege basis aligned to role; provisioning and de-provisioning are tracked per [platform-and-access-matrix.md](platform-and-access-matrix.md).

**b. Multi-factor authentication.** Two-factor authentication will be required wherever possible.

**c. Password construction (PRESERVED VERBATIM from IT-001).** All personnel are responsible for creating strong passwords consisting of certain attributes that are designed to improve security by thwarting attempts to guess or crack passwords. Each personnel member will construct passwords of at least eight characters in length and consist of a combinations of upper and lowercase letters, numbers and characters. Passwords may not include any of the following:

* Proper names or words in the English or a foreign dictionary;
* The personnel member's initials or his or her first, middle, or last name;
* Any personal information of the personnel member (e.g., license plate, Social Security number, street address);
* All numerical digits or all letters;
* Obvious patterns or keyboard sequences (e.g., AlB2C3D4, qwertyui);
* The personnel member's login name, in any form (e.g., as is, reversed, capitalized, doubled); or
* Any of the above elements in inverse order or followed or preceded by a single digit.

**d. Mobile passcode construction (PRESERVED VERBATIM from IT-001).** All personnel using mobile phones to access Company data are responsible for creating and using strong passcodes consisting of certain attributes that are designed to improve security by thwarting attempts to guess or crack passcodes. Each personnel member will construct passcodes of at least six digits in length (eight digits if the device may access PHI) and consisting of a combinations of upper and lowercase letters, numbers and characters. Passcodes may not consist of obvious patterns or sequences (e.g., 12345678, 55555555).

**e. General personnel password responsibilities.** Passwords are to be chosen by and known only to the personnel responsible for its creation. All personnel are responsible for safeguarding the integrity of their unique passwords. To this end, personnel are prohibited from engaging in the following conduct:

* Sharing a password with anyone, including administrative assistants, secretaries, temporary personnel of Company, or family members;
* Keying in their password for others to use or permitting others to observe their password as it is entered on a computer;
* Attempting to learn or use the password of another personnel member;
* Posting a password in a work area or other easily discovered place (e.g., taped to a wall, under a keyboard);
* Creating a "hot key" for purposes of automatically entering a password;
* Transmitting a password through electronic mail over the Internet or storing it without encryption in a file on any computer (including iPads or similar devices); or
* Using the same password for any other purpose, particularly in connection with a World Wide Web site where someone outside the organization could have access to the password.

All passwords should be memorized and not written down, with two exceptions: (1) Use of a password manager approved by the Security Officer is highly recommended. The master password should be memorized and not written down. (2) If memorization is not possible, personnel may write down his or her password as long as the password is not identified as a password and is stored in a secure, non-public location, such as a wallet.

**f. Account lockout.** Production systems and identity providers must enforce automated lockout after a reasonable number of consecutive failed authentication attempts, with lockout duration and re-enablement procedures approved by the Security Officer. Lockout events generate audit log entries reviewed under §7.

**g. Session & token management (OWASP A07).** All Company applications and services that issue authenticated sessions or API tokens must comply with the following:

* **Session expiration.** Web and application sessions expire after a defined idle period appropriate to the data sensitivity (default 30 minutes for PHI-bearing surfaces), and after an absolute maximum session lifetime not to exceed 12 hours without re-authentication.
* **Token rotation.** Access tokens are short-lived (target ≤1 hour) and rotated on each refresh.
* **Refresh-token handling.** Refresh tokens are stored only in secure, HTTP-only, same-site cookies or platform secure-storage equivalents; refresh tokens are single-use (rotated on redemption) and revoked on logout, password change, or detected reuse.
* **Logout-on-password-change.** A successful password change or forced password reset invalidates all outstanding sessions and refresh tokens for the affected user.
* **Session binding.** Where feasible, sessions are bound to client characteristics (e.g., IP/device fingerprint) and anomalous re-use triggers re-authentication.

**h. Default-credential change requirement (SIG N.12).** All default credentials (vendor-supplied admin passwords, factory keys, default API tokens) must be changed before any device, appliance, virtual image, SaaS tenant, or service is placed into production. Verification of default-credential change is a required step in the production-readiness checklist maintained by the Security Officer.

**i. Deactivation of passwords.** If a personnel member suspects that someone else has access to his or her password, or that the security of the password has otherwise been compromised, the personnel member must immediately report the occurrence to the Security Officer. Immediate steps will be taken to change the password. A personnel member's password will be immediately deactivated by the Security Officer or his or her designee upon a security incident that the Security Officer determines requires a forced password reset, termination of the personnel member's employment, or a change in the personnel member's role with Company in which access to Company's network is no longer authorized. (See §6 for the consolidated termination checklist.)

### 2. Encryption (originally IT-005)

**a. Coverage and authority.** This section requires the encryption of ePHI transmitted over open networks such as the Internet, and provides for the secure administration of Company's encryption protocols. All ePHI will be encrypted before it is emailed or otherwise transmitted over open networks such as the Internet. To ensure that ePHI is transmitted only to authorized third parties, personnel must comply with all protocols established by Company for confirming that the intended recipient of any encrypted data is identified and authenticated. Any encryption of data not required under this Policy must be approved in writing by the Security Officer.

**b. Encryption in transit (PRESERVED VERBATIM standard citations from IT-005).** To ensure consistency within the Company Computer Network and interoperability between the Company Computer Network and third-party systems, all algorithms and products used by Company in connection with encryption must be approved by the Security Officer. The encryption system must provide a sufficient level of security to safeguard against the unauthorized access to or modification of ePHI. For data in motion, encryption must be in accordance with Federal Information Processing Standards (FIPS) 140-2. These include, as appropriate, standards described in NIST Special Publications 800-52, *Guidelines for the Selection and Use of Transport Layer Security (TLS) Implementations*; 800-77, *Guide to IPsec VPNs*; or 800-113, *Guide to SSL VPNs*, and may include others which are FIPS 140-2 validated.

**c. Encryption at rest (PRESERVED VERBATIM standard citation, rescued from IT-004).** All PHI maintained on portable devices and media, including mobile phones and iPads, must be encrypted in accordance with standards approved by the Security Officer. For data in storage, encryption must be in accordance with NIST Special Publication 800-111, *Guide to Storage Encryption Technologies for End User Devices*. This requirement applies to laptops, desktops, mobile devices, removable media, server volumes, database storage, and backup media that contain or may contain ePHI.

**d. Password storage / application secret hashing standard (OWASP A02).** Application-layer storage of user passwords and authentication secrets must comply with the following:

* **Approved hash algorithms.** User passwords must be stored using `argon2id` (preferred) or `bcrypt` (acceptable). Plain SHA family hashes, MD5, and reversible encryption are prohibited for password storage.
* **Salt strategy.** Each password hash uses a unique, cryptographically random per-user salt of at least 16 bytes generated by a CSPRNG; salts are stored alongside the hash.
* **Work-factor / iteration count.** Tuned so that a single hash operation takes ≥250 ms on production-class hardware, reviewed annually by the Security Officer as compute capacity increases. For `argon2id`, baseline parameters are `memory ≥ 64 MiB`, `iterations ≥ 3`, `parallelism = 1`. For `bcrypt`, baseline `cost ≥ 12`.
* **Pepper (optional).** Where used, the pepper is stored in a dedicated secrets manager separate from the credential database.
* **Application secret rotation.** API keys, signing keys, OAuth client secrets, database credentials, and other application secrets are rotated at least every 12 months and immediately upon suspected compromise or personnel role change with access to those secrets. Secrets are stored in an approved secrets manager — never in source control, ticket systems, or chat.

**e. Encryption keys.** Personnel must exercise the same precautions in protecting encryption keys from disclosure as is required for passwords under §1. Encryption keys must not be sent by electronic mail over the Internet or any other open network, unless such information is encrypted using keys that have been previously exchanged using secure means. In the event that this is not possible, encryption keys should be mailed to the authorized recipient in an envelope clearly marked as confidential or disclosed to the recipient by phone. Personnel must not attempt to break encryption codes used by Company, or modify, destroy or otherwise compromise the efficacy of Company's encryption system or related keys.

Access to Company's encryption protocols will be restricted to authorized third parties and those personnel requiring such access to perform their job responsibilities. The Security Officer will maintain a list of all authorized encryption users issued encryption keys. The Security Officer will be responsible for training all applicable personnel in the use of encryption, identification and authentication protocols, as well as the manner in which personnel will instruct recipients with respect to the decryption of any encrypted data transmitted by Company.

**f. Key generation, length, and lifecycle.** Encryption keys will be developed through mechanisms that are not easily reproducible by third parties (e.g., computerized random number generation). The Security Officer will be responsible for reviewing and determining (a) the length of the keys, (b) the quality of the encryption and (c) the frequency of modifications to the key configurations. Any increase in the length of the encryption keys, upgrades to the applicable technology or routine changes to key configurations will be performed in accordance with applicable standards published by government agencies, or if such standards are not available, in accordance with industry standards and guidelines.

**g. Key recovery and archival.** Because data that has been encrypted may be irretrievable in the event an encryption key is lost or damaged, all encryption products used by Company must support a technology that will make keys available to authorized individuals and include key recovery capabilities. Any use of encryption without such technology must be approved in writing by the Security Officer. In addition, the Security Officer or his or her designee will maintain, in a secure environment, an archive of all encryption keys used by Company. In no event will such keys be stored on the same media as that which is used for ePHI.

**h. Deactivation of keys.** Personnel will promptly report to the Security Officer any instance in which they believe that an unauthorized party has had access to an encryption key, or circumstances in which the security of Company's encryption system has been otherwise compromised. In such instances, immediate steps will be taken by the Security Officer to deactivate the compromised key and remedy the specific security breach, as applicable. The Security Officer must immediately deactivate and archive encryption keys upon notification by Human Resources of the termination of an individual's employment with Company. (See §6.)

### 3. Workstation Use (originally IT-002)

This section applies to all Users accessing the IT System using individual Workstations, including iPads, owned and maintained by Company as well as iPhones and other mobile devices owned and maintained by personnel, but which are used in the performance of personnel members' job functions. Because one of the greatest security risks to Company's data and PHI is use of Workstations, Users must take all necessary steps to prevent the improper use of or damage to their individual Workstations.

**a. Physical safeguards.**

* Users must always lock their Workstations, if possible, or sign off the Workstation when not using it or when leaving the work area for breaks. Workstations should be locked after 5 minutes of inactivity.
* Users must sign off at their Workstations at the end of the day. When using mobile phones or iPads, Users should lock their devices after two minutes when not in use.
* To prevent damage to any equipment, users should take care when eating or drinking in the vicinity of a Workstation.
* Users must never log on to their Workstation for, or share their passwords with, another party (including but not limited to temporary personnel of Company) or permit unauthorized parties to use a Workstation.
* Passwords and user IDs should not be stored on or near a Workstation.
* Users must not remove monitor privacy shields if such shields have been installed on their Workstations by Company.

**b. Technical security.**

* Workstations may not be configured to automatically enter log-on information or passwords.
* Users must comply with all Company directives pertaining to Workstation security and maintenance issued from time to time, as applicable (e.g., virus notices, corrective actions to be implemented by Users, system upgrades).
* Workstation configuration shall only be performed by a personnel member or agent authorized by Company unless such configuration is being performed by the personnel member to a personnel member's mobile phone or iPad. Users must never modify system configuration files or access control lists for such files or files belonging to other users.
* If not locked, all Workstations, excluding mobile phones and iPads, shall run activated screen savers that operate in accordance with Company's requirements. Users may use only those screen savers that are authorized by Company and may not modify the timing of any authorized screen saver or download any screen saver from an Internet source.

**c. Protection of work-related documents and data storage location (PRESERVED VERBATIM — "no PHI on hard drives" rule).** Unless authorized or otherwise directed by Company, work-related data and files must be stored on the external hosting platform with which Company contracts, in the Company app or on the network server of the IT System, and not on a computer C drive, CD or thumb drive nor directly on a mobile phone or iPad. PHI shall not be stored on the hard drives of computers, laptops, or other mobile devices.

Users shall secure media (e.g., hard copy or CDs but not mobile phones) that contains PHI in a locked desk, cabinet or room. Users must comply with any other applicable Company policies when using Workstations, including the password rules in §1 above.

### 4. Remote Access (originally IT-006)

This section establishes the terms under which personnel may access the IT System through a non-Company-controlled network, device, or medium, including, but not limited to, personal mobile devices such as iPhones and iPads, dial-in and cable modems, wireless networks, frame relays, and digital subscriber lines, and to protect the security and confidentiality of the data residing on the IT System. Nothing in this section shall prevent field-based personnel from connecting to the Company IT System using laptops, mobile phones, or other mobile devices.

**a. Authorization.** Access to the IT System from remote locations by any User shall be overseen by the Security Officer and will be limited to those individuals and entities requiring such access in order to perform their duties and responsibilities for Company.

**b. General security procedures.** Users are accountable for their actions with respect to any remote access to the IT System and are responsible for taking every reasonable measure to protect the IT System from unauthorized access. In order to minimize breaches of security, all Users with remote access privileges are required to comply with the following rules:

* All computers and networks (including laptops and other mobile devices) remotely connected to the IT System must (a) use up-to-date virus protection software, and (b) be configured to comply with Company's security program. See §1 (Access Control), §2 (Encryption), and §3 (Workstation Use).
* To the extent Company employs any technical controls and schemes designed to safeguard the IT System from unauthorized access (e.g., "automatic disconnect" features, firewalls, encryption tools), Users are not permitted to utilize any artificial processes for purposes of overriding or circumventing such controls.
* Users must not provide access information, including, but not limited to executable files, user IDs, passwords, and VPN access, to any other individual (including family members).
* Users must promptly log off the IT System when a work session has been completed and take reasonable steps to confirm that the connection has been terminated. If other individuals have physical access to the User's computer or mobile device, the User must log off whenever he or she temporarily leaves the computer workstation or mobile device.
* Users are not permitted to use non-Company-authorized electronic mail accounts or other unauthorized external resources to conduct Company business.
* Users may not transmit PHI from a remote location to the IT System through the Internet or any other open line unless the transmission is encrypted.

**c. VPN and multi-factor authentication.** All remote access to internal Company resources containing or capable of accessing PHI must traverse a Company-approved VPN or zero-trust access broker and is conditioned on multi-factor authentication. All Users shall be required to take any additional authentication steps required by Company when remotely accessing the IT System.

**d. Equipment and technology.** Because laptops and other portable technology present special security risks when used to access the IT System, the use of such technology for purposes of remote access shall require that the User adhere to the additional security procedures described below.

* Users must comply with Company's procedures for removing any equipment owned by Company from Company's offices and not otherwise issued to the User, which includes recording: the User's name, date of pickup and return, where the equipment will be used, and the condition of the equipment at the time of removal and upon return.
* All laptops and other mobile devices used for Company business purposes must be prepared and/or approved by the Security Officer or his or her designee in accordance with §5 (Device & Media Management).
* All PHI maintained on laptops and other mobile devices must be encrypted in accordance with §2.
* Users may not install any software applications on Company-owned equipment without the approval of Company.
* Where appropriate, equipment must be plugged into a surge protection device and, if available, kept in a locked protective carrying case when not in use. If possible, the equipment should be placed in a locked file or supply cabinet when not in use.
* PHI shall not be stored on the hard drives of computers, laptops, or other mobile devices.
* Computers must be carried as hand baggage on public carriers and never be stored in luggage or cargo areas, unless prohibited by the carrier's policies.
* Users should be observant of their surroundings when using mobile equipment off-site to access the IT System.
* User passwords must not be stored or written on the computer or its carrying case.

**e. Termination of remote-access privilege.** A User's ability to remotely access the IT System shall be immediately terminated, and any hardware and equipment owned or software licensed by Company in the possession of User shall be promptly returned to Company, upon termination of employment or a change in User's role with or relationship to Company whereby remote access to the IT System is no longer authorized. (See §6.)

**f. Monitoring (PRESERVED VERBATIM timing language).** Company shall, as applicable, maintain or cause to be maintained a record of all inbound remote access to the IT System, which will be reviewed by the Security Officer as frequently as is technologically and administratively feasible. Any actual or suspected unauthorized access shall be immediately investigated by the Security Officer and promptly reported to the Privacy Officer of Company.

**g. Installation, costs, and no warranty.** Company will provide the specifications for appropriate software and hardware to be used by User for purposes of establishing the necessary connections to the IT System. Each User is responsible for selecting an Internet service provider, installing (or coordinating the installation) of any required components, and paying any fees and costs associated therewith. Software licensing fees within Millie's standard tech stack will be paid by Millie. All remote access of the IT System shall be at the User's risk; Company makes no warranty that the User's connection will be uninterrupted, error-free, or free of viruses.

### 5. Device & Media Management (originally IT-004 — RESCUED from privacy-policy.md)

This section regulates the receipt and removal of Company's hardware and electronic media as well as the movement of these items within and outside of Company's Facilities to ensure that PHI stored on the Company Computer Network is protected from unauthorized access and disclosure.

**a. Inventory controls.** The Security Officer will cause to be maintained a written inventory of all components of the Company Computer Network that includes a detailed list of all equipment, hardware, software and electronic media such as USBs, external hard drives and tapes that contain or maintain or may contain or maintain PHI. This will include Company-issued laptops as well as iPhones and other mobile devices owned by Company personnel, but used in their performance of their Company job functions. The list will include each item's name, serial number, date of acquisition, manufacturer, service provider, the date and type of any maintenance performed and the current location of such item, as applicable.

**b. Receipt and removal log.** With respect to components of the Company Computer Network that are issued by Company to its personnel (not including mobile phones and other devices that are owned directly by personnel, but utilized for Company business), the Security Officer or his or her designee will maintain a log of the receipt and removal of all such components of the Company Computer Network that includes the name of the party responsible for each item, the date of receipt and removal and the reason for any removal (e.g., repair, off-site storage, personnel home use). In addition, the log will include a record reflecting the relocation of such items within Company's Facilities. No personnel or other individual will be permitted to remove or relocate any item without notifying the Security Officer who shall record such action in the log. Any such component of the Company Computer Network not accounted for will be immediately reported to the Security Officer.

**c. Retrievable copy before relocation (PRESERVED VERBATIM requirement).** Prior to any relocation or removal of any such equipment, the Security Officer is responsible for ensuring that a retrievable copy of any PHI residing on the equipment is available.

**d. Disposal and reuse.** The disposal of Company's hardware, equipment or media that may contain ePHI, or the transfer of such items to a third party, must be approved by the Security Officer. All electronic data stored on any hardware or equipment must be completely deleted by the Facilities Resource Manager or his or her designee prior to the disposal or transfer of such items. For example, any data stored on the hard-drive of a Company-issued laptop computer must be erased before issuing to another personnel or the sale of the computer to a third party. In addition, any electronic media must be formatted so that the data residing on the media is no longer accessible to a potential user. To the extent that it is not possible to erase the data or format the media, as is the case with certain compact disks that are not rewritable, the media itself must be destroyed. The date and time of such deletion or destruction process, as well as the name of the personnel responsible for the process, will be recorded in a log maintained by the Facilities Resource Manager.

The Security Officer must approve making any equipment, hardware or media available for reuse for purposes other than processing PHI. Prior to recycling such items, the Security Officer or his or her designee will take all necessary steps to ensure that any electronic data residing on such equipment, hardware or media has been completely deleted or otherwise rendered inaccessible to a prospective user. The date and time of the deletion process, as well as the name of the personnel responsible for the process, will be recorded in a logbook maintained by the Security Officer.

**e. Encryption-at-rest cross-reference.** All PHI maintained on portable devices and media is encrypted per §2(c) (NIST SP 800-111).

### 6. Termination & Role-Change Checklist (consolidated)

This single checklist supersedes the per-policy termination clauses previously stated in IT-001 (passwords), IT-005 (encryption keys), and IT-006 (remote access). Upon notification by Human Resources of personnel termination, role change resulting in loss of authorization, or a security incident requiring forced re-credentialing, the Security Officer or designee shall execute the following — immediately:

1. **Password deactivation.** Disable all user accounts; force password reset for any shared service the user could have accessed; invalidate all active sessions and refresh tokens (see §1(g)).
2. **MFA factor revocation.** Remove all enrolled second-factor devices for the user.
3. **Remote access termination.** Revoke VPN credentials, zero-trust certificates, and any standing remote-access tokens.
4. **Encryption key archival.** Deactivate and archive any encryption keys issued to the user; rotate shared keys the user had access to.
5. **Application secret rotation.** Rotate any API keys, signing keys, or service-account credentials the user could have accessed.
6. **Device inventory return.** Recover all Company-issued laptops, mobile devices, removable media, and physical access tokens; reconcile against the §5 inventory and receipt-and-removal log; wipe per §5(d) before reuse or disposal.
7. **Audit log entry.** Record each completed step with timestamp and responsible personnel.

The Privacy Officer is notified upon completion.

### 7. Logging, Monitoring & Alert Cadence (OWASP A09 / SIG J.5)

**a. Events that must be logged.** At minimum, Company production systems generate audit log records for:

* Authentication events — successful logins, failed logins, lockouts, MFA challenges, password resets, session creation/destruction.
* PHI access events — read, write, export, print, and bulk-query operations against records containing PHI.
* Administrative actions — privilege grants and revocations, role changes, configuration changes, encryption key issuance and rotation, secrets-manager access.
* Network ingress/egress — VPN connections, firewall denies, anomalous outbound flows, and remote-access sessions (per §4(f)).
* Application-layer security events — input-validation rejections, authorization failures, anti-CSRF token failures, rate-limit trips.

Log records include actor identity, timestamp (UTC), source IP or device identifier, action, target resource, and outcome. Logs are protected from tampering and stored in accordance with the retention schedule in [governance-and-risk-management.md](governance-and-risk-management.md).

**b. Review cadence.** The Security Officer (or designee) performs a documented monthly spot-check of authentication, PHI-access, and administrative-action logs, and an on-alert investigation whenever an automated detection fires. Remote-access logs are reviewed as frequently as is technologically and administratively feasible per §4(f). Findings and any corrective actions are logged.

**c. Alert thresholds.** Automated alerts are configured for, at minimum: repeated authentication failures from a single source, MFA bypass attempts, privilege escalation outside the change-management window, anomalous PHI-export volume, encryption-key access by an unexpected principal, and detection of default credentials in production. Threshold tuning is reviewed quarterly.

**d. Cross-reference.** Log retention duration, breach-notification escalation paths, and risk-management integration are governed by [governance-and-risk-management.md](governance-and-risk-management.md) and [hipaa-security-incidents.md](hipaa-security-incidents.md).

## IV. Training & Awareness

All personnel with access to Company information systems shall receive technical-safeguards training at the time of employment or engagement, with annual updates thereafter, in accordance with the [governance-and-risk-management.md](governance-and-risk-management.md) Training Program.

## V. Sanctions

Any personnel member who violates this Policy will be subject to disciplinary action, up to and including termination of employment or engagement, in accordance with Company HR policy. Severity is assessed based on intent, the nature of the systems and PHI involved, and impact on Company information security. Sanctions are documented and tracked by the Privacy Officer.

## VI. References

**Regulatory.**

* 45 C.F.R. § 164.308(a)(5) — Security awareness and training (passwords, log-in monitoring).
* 45 C.F.R. § 164.310(b) — Workstation use.
* 45 C.F.R. § 164.310(d)(1) — Device and media controls.
* 45 C.F.R. § 164.312 — Technical safeguards (access control, audit controls, integrity, person/entity authentication, transmission security).
* 45 C.F.R. § 164.312(a)(1) — Access control standard.
* 45 C.F.R. § 164.530 — Administrative requirements (referenced in originating IT-005).

**Federal standards.**

* FIPS 140-2 — Security Requirements for Cryptographic Modules.
* NIST SP 800-52 — Guidelines for the Selection and Use of Transport Layer Security (TLS) Implementations.
* NIST SP 800-77 — Guide to IPsec VPNs.
* NIST SP 800-111 — Guide to Storage Encryption Technologies for End User Devices.
* NIST SP 800-113 — Guide to SSL VPNs.

**Industry frameworks.**

* OWASP Top 10 — particularly A02 (Cryptographic Failures / password storage), A07 (Identification and Authentication Failures / session and token management), A09 (Security Logging and Monitoring Failures).
* SIG (Shared Assessments Standardized Information Gathering) — N.12 (default-credential change), J.5 (logging and monitoring).

**Related Millie policies.**

* [governance-and-risk-management.md](governance-and-risk-management.md) — training program, log retention, risk management.
* [hipaa-security-incidents.md](hipaa-security-incidents.md) — incident response and escalation.
* [hipaa-safeguards.md](hipaa-safeguards.md) — administrative and physical safeguards.
* [hipaa-risk-management.md](hipaa-risk-management.md) — risk analysis methodology.
* [platform-and-access-matrix.md](platform-and-access-matrix.md) — system-by-system access provisioning.
* [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md) — secure development and asset lifecycle.
* [hipaa-definitions.md](hipaa-definitions.md) — glossary.

## VII. Definitions used in this Policy

Standard HIPAA and Millie glossary terms (PHI, ePHI, Workstation, IT System, Company Computer Network, User, personnel, Security Officer, Privacy Officer) are defined in [hipaa-definitions.md](hipaa-definitions.md). Terms used in this Policy that warrant additional clarification:

* **Refresh token** — a long-lived credential used to obtain new short-lived access tokens without requiring the user to re-authenticate. Subject to the rotation, storage, and revocation requirements in §1(g).
* **Default credential** — any vendor-supplied, factory-set, or installer-default password, key, token, or PIN shipped with a device, appliance, virtual image, or service. Must be changed before production deployment per §1(h).
* **Hardening baseline** — the documented set of configuration settings applied to a class of devices, operating systems, or services to reduce attack surface before placement into production (e.g., disabling unused services, enforcing logging, applying CIS or vendor-recommended controls).
* **Secrets manager** — an approved, access-controlled service for storing and rotating application secrets (API keys, signing keys, service credentials). Direct embedding of secrets in source control, ticketing systems, chat, or email is prohibited.
* **Work factor** — the computational cost parameter of a password-hashing algorithm (e.g., `bcrypt cost`, `argon2id memory/iterations`) tuned to make brute-force attack infeasible.
* **Session binding** — the practice of tying an authenticated session to one or more client characteristics (IP, device fingerprint, TLS channel) so that re-use from a different context triggers re-authentication.

## VIII. Revision history

| Date       | Version | Author           | Summary of change |
| ---------- | ------- | ---------------- | ----------------- |
| 2022-05-18 | 1.0     | Security Officer | Initial issuance of IT-001 (Passwords), IT-002 (Workstation Use), IT-004 (Device & Media), IT-005 (Encryption), IT-006 (Remote Access). |
| 2022-05-02 | 1.1     | Security Officer | Last revised dates per originating source documents. |
| 2025-05-04 | 1.2     | Security Officer | IT-002 Workstation Use last revised. |
| 2026-05-24 | 2.0     | Security Officer (CTO co-owner) | Consolidated IT-001, IT-002, IT-004, IT-005, IT-006 into single Technical Safeguards policy. Rescued IT-004 Device & Media content that previously existed only inside `privacy-policy.md`. Added: session & token management (OWASP A07), password-storage hashing standard (OWASP A02), default-credential change (SIG N.12), consolidated termination checklist, logging/monitoring section (OWASP A09 / SIG J.5). Cut: foreign-country encryption export-control clause (out of Millie threat model per CONSOLIDATION-PROPOSAL §7.3). Normalized "Chief Security Officer"/"Chief Privacy Officer" → "Security Officer"/"Privacy Officer". |
