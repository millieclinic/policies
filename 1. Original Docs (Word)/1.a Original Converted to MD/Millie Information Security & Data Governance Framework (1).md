| **![](data:image/jpeg;base64...)** | |
| --- | --- |
| **Title**: Millie Information Security & Data Governance Framework | **Policy #**: IT-026 |
| **Effective Date**: April 22, 2026 | **Last Revised**: May 23, 2026 |

Millie Information Security & Data Governance Framework

# 1. Overview

Millie, Inc. maintains a comprehensive set of administrative, technical, and physical safeguards to ensure the confidentiality, integrity, and availability of sensitive personal and corporate information, including Protected Health Information (PHI) as defined under HIPAA.

This framework governs how sensitive data is stored, accessed and secured, transmitted, monitored, retained and archived, and protected in the event of a breach. It applies to Protected Health Information (PHI), personally identifiable information (PII), and other confidential business information maintained by the Company.

This framework is supported by formal policies including Encryption, Remote Access, Device & Media Management, Minimum Necessary Rule, De-Identification, Business Associate Agreements, Breach Notification, and Risk Management policies.

# 2. Governance & Risk Management

Millie maintains a risk-based approach to data protection through formal risk assessments conducted at least annually and as needed. A designated Risk Management Team evaluates threats, vulnerabilities, likelihood, and impact, and defines mitigation strategies.

Results are reviewed by leadership and used to prioritize controls and investments.

# 3. Data Classification & Handling

Millie defines PHI in accordance with HIPAA and applies strict handling controls. Data use is governed by the Minimum Necessary Rule and formal processes for de-identification, re-identification, and limited data sets.

These controls minimize unnecessary exposure and ensure compliant data usage.

# 4. Access Control & Identity Management

Access is governed by role-based access control (RBAC) and least privilege principles.

All systems require multi-factor authentication (2FA). AWS access is managed via IAM users, and root access is not used for routine operations.

Access is granted based on role and business need and is revoked promptly upon role change or termination. Administrative access is restricted and monitored. Periodic reviews of access permissions are conducted as part of ongoing security practices.

# 5. Data Storage & Protection

All PHI transmitted over open networks is encrypted. Databases hosted via Aptible are encrypted at rest.

Devices storing PHI are inventoried, encrypted, and securely wiped prior to reuse or disposal. Paper records are minimized, securely stored, and shredded when no longer needed.

# 6. Data Transmission & Sharing

All PHI transmitted externally must be encrypted. Data sharing is governed by the Minimum Necessary Rule, Data Use Agreements, and Business Associate Agreements.

Secure channels are required for all remote access and data transmission.

# 7. Logging, Monitoring & Audit Controls

Millie maintains logs across systems including Aptible, AWS CloudWatch, and internal admin dashboards.

Logs track user activity, including updates to patient data, capturing who made changes, what fields were changed, and when. These logs are used to support security monitoring, incident investigation, and audit activities. Relevant logs are reviewed as needed in response to security events or anomalies.

# 8. Incident Response & Breach Management

Millie maintains a Breach Notification Policy aligned with HIPAA. Suspected breaches must be reported within 48 hours and are investigated promptly.

If confirmed, affected individuals are notified within 60 days and mitigation actions are taken.

# 9. Data Retention & Lifecycle Management

Application data is retained in accordance with business and regulatory requirements. At present, core application data is retained indefinitely to support clinical, operational, and compliance needs.

Logs are retained for 6 months in the database and then archived to AWS S3 for long-term storage.

Daily backups are performed via Aptible, including point-in-time recovery capabilities.

# 10. Business Continuity & Data Availability

Databases are backed up daily with redundancy and recovery capabilities via Aptible.

These controls ensure resilience and recovery in case of system failure.

# 11. Third-Party & Vendor Management

Millie maintains a risk-based third-party risk management process for vendors, contractors, subcontractors, service providers, and other third parties that create, receive, maintain, transmit, access, or otherwise process PHI, PII, or other confidential Millie information. The process is owned by the Security Officer in coordination with the Chief Privacy Officer, Legal, Operations, and relevant business owners.

Prior to granting access to PHI or other sensitive data, Millie evaluates the vendor’s business purpose, data access, system access, criticality, security controls, and contractual obligations. Vendors that create, receive, maintain, or transmit PHI on Millie’s behalf must execute a Business Associate Agreement or other appropriate contractual terms before access is granted.

Millie maintains a vendor inventory or tracker identifying vendor owner, business purpose, data type, access level, criticality/risk tier, BAA or contractual status, renewal/review date, and known subcontractor/subprocessor considerations where applicable.

For vendors that use subcontractors, subprocessors, fourth parties, or Nth parties to handle PHI or sensitive Millie data, Millie requires contractual flow-down obligations or other written assurances that such parties are bound to materially similar privacy and security obligations. Millie reviews vendor and subcontractor risk based on data sensitivity, criticality, access, and applicable legal or contractual requirements.

Vendor risk is reviewed at onboarding, upon material changes in vendor services or data access, at renewal or periodic review, and as needed in response to incidents, changes in legal requirements, security events, or changes in business operations. Material third-party risks are escalated through Millie’s risk management process and reviewed by leadership as appropriate.

#

# Referenced Policies:

* [Encryption Policy.docx](https://docs.google.com/document/u/0/d/1lmBS4UQI9wFgY4ZGenFfUc_UfcMWEwRa/edit)
* [Paper Document Management Policy.docx](https://docs.google.com/document/u/0/d/1FKJhjIzIBBR4IEaWBuL7hM7Eh2EuofWa/edit)
* [Remote Access Policy.docx](https://docs.google.com/document/u/0/d/1TjOZIuwV3l8-fNDInz1eqWVjXZQvf_ve/edit)
* [Device Management and Media Management Inventory Policy.docx](https://docs.google.com/document/u/0/d/1R89XNhHysdKotPbuMyKsG1J8tmKiWveO/edit)
* [Minimum Necessary Rule Policy.docx](https://docs.google.com/document/u/0/d/1QGpQ6TzlImTfCD4TQ5-uJcDEkyRwWymB/edit)
* [De-Identifying and Re-Identifying PHI and Creation of Limited Data Sets Policy.docx](https://docs.google.com/document/d/1grONvs_akg_VCkimfNDamIRLVSCbegtQ/edit?usp=drive_link&ouid=112729554834993473893&rtpof=true&sd=true)
* [Business Associate Agreement Policy.docx](https://docs.google.com/document/u/0/d/1Ow91SFKBpFzdVAIiQKFH6fjzzQ9UG3Og/edit)
* [Breach Notification Policy.docx](https://docs.google.com/document/u/0/d/13teSJdPEC4P_LDvisQZZ43OxrZ1eZSh7/edit)
* [Risk Management Policy.docx](https://docs.google.com/document/d/1-QYmzbvMLir_SmAijhq_ZTGDyCuRisjL/edit?usp=drive_link&ouid=112729554834993473893&rtpof=true&sd=true)
* [HIPAA Definitions Policy.docx](https://docs.google.com/document/u/0/d/1rX2ftSIFO24Z3xM2cUf_oVvTzieA8ad1/edit)

# Additional Resources:

Aptible:

* <https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-encryption/overview>
* <https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-backups> ![](data:image/png;base64...)
