---
title: "Vendor Management & Business Associate Agreements"
sources: ["hipaa-business-associate-agreement.md", "information-security-framework.md (§11 Third-Party & Vendor Management)"]
supersedes: ["L-001"]
last_reviewed: 2026-05-24
owner: "Privacy Officer"
status: "active"
---

# Vendor Management & Business Associate Agreements

> **Sources.** Consolidated from: `hipaa-business-associate-agreement.md` (Policy # L-001) and `information-security-framework.md` §11 (Third-Party & Vendor Management). Originals archived in `New Policy Docs/_archive/`.

## I. Scope

This Policy applies to all facilities and locations owned, operated, or managed by Millie, Inc. ("Company") and all Company personnel, and to all third parties (vendors, contractors, subcontractors, service providers, subprocessors, and any other party) that create, receive, maintain, transmit, access, or otherwise process PHI, PII, or other confidential Company information on behalf of Company.

## II. Policy

It is Company's policy to manage third-party relationships under a risk-based program that protects the confidentiality, integrity, and availability of Company data — including Protected Health Information (PHI). Company will (a) identify and evaluate vendors before granting access to sensitive data; (b) execute a Business Associate Agreement (BAA) with every Business Associate prior to that Business Associate creating, receiving, maintaining, or transmitting PHI on Company's behalf; (c) require contractual flow-down obligations to subcontractors, subprocessors, fourth parties, and other Nth-party participants in the supply chain; and (d) monitor third-party risk on a continuous basis, with escalation through Company's risk management process when material.

## III. Procedure

### 1. Vendor Risk Management

> *Migrated verbatim from `information-security-framework.md` §11.*

Millie maintains a risk-based third-party risk management process for vendors, contractors, subcontractors, service providers, and other third parties that create, receive, maintain, transmit, access, or otherwise process PHI, PII, or other confidential Millie information. The process is owned by the Security Officer in coordination with the Chief Privacy Officer, Legal, Operations, and relevant business owners.

Prior to granting access to PHI or other sensitive data, Millie evaluates the vendor's business purpose, data access, system access, criticality, security controls, and contractual obligations. Vendors that create, receive, maintain, or transmit PHI on Millie's behalf must execute a Business Associate Agreement or other appropriate contractual terms before access is granted.

Millie maintains a vendor inventory or tracker identifying vendor owner, business purpose, data type, access level, criticality/risk tier, BAA or contractual status, renewal/review date, and known subcontractor/subprocessor considerations where applicable.

For vendors that use subcontractors, subprocessors, fourth parties, or Nth parties to handle PHI or sensitive Millie data, Millie requires contractual flow-down obligations or other written assurances that such parties are bound to materially similar privacy and security obligations. Millie reviews vendor and subcontractor risk based on data sensitivity, criticality, access, and applicable legal or contractual requirements.

Vendor risk is reviewed at onboarding, upon material changes in vendor services or data access, at renewal or periodic review, and as needed in response to incidents, changes in legal requirements, security events, or changes in business operations. Material third-party risks are escalated through Millie's risk management process and reviewed by leadership as appropriate.

### 2. Business Associate Identification and BAA Execution

#### 2.1 Determining whether a person or entity is a Business Associate

To determine whether a person or entity is a Business Associate of Company, Company will evaluate whether the person or entity, on behalf of Company, creates, receives, maintains, or transmits PHI — including for claims processing or administration, data analysis, processing or administration, utilization review, quality assurance, certain patient safety activities, billing, benefit management, and practice management.

Persons or entities that receive PHI from Company solely for patient Treatment, or solely to enable Company to be paid for its services, are not Business Associates. The Privacy Officer must be contacted to confirm the determination of whether a person or entity is a Business Associate when there is any doubt.

#### 2.2 BAA execution requirements

- Every Business Associate must sign a Business Associate Agreement, in the form designated by the Privacy Officer, prior to creating, receiving, maintaining, or transmitting any PHI. No access to PHI will be allowed, no account will be set up, and no money will be paid for products or services until such agreement is signed or until the occurrence of a condition or event specified in the BAA or an addendum thereto.
- The Company Model Business Associate Agreement (see Appendix A) must be used without modification unless the Privacy Officer approves modifications or use of a different form (e.g., a vendor-paper BAA).
- Each executed BAA shall be maintained in the Millie Google Workspace `Contracts > BAAs` folder, with the vendor record in the vendor inventory updated to reflect execution date, counterparty, scope, and renewal date.
- Contract renewal will be monitored for continued HIPAA compliance by the Privacy Officer.

#### 2.3 Breach of a BAA

If a Business Associate improperly uses or discloses PHI, it has breached its obligations under the applicable BAA. In the event of such a breach the Privacy Officer shall be immediately notified, will consult with outside legal counsel as appropriate, and will coordinate with the Security Officer to invoke Company's incident-response and breach-notification procedures. Material breaches may result in contract termination and reporting to the Office for Civil Rights (OCR) as required by HIPAA.

### 3. Subcontractors and Nth-Party Flow-Down Requirements

Many vendors rely on their own subcontractors, subprocessors, fourth parties, or further-downstream Nth parties to deliver services to Company. Because PHI and other sensitive data may flow to those parties, Company requires contractual safeguards that follow the data wherever it goes.

- **Flow-down clauses.** Every BAA executed by Company must require the Business Associate to enter into a written agreement with each of its subcontractors that materially mirrors the privacy, security, breach-notification, and audit obligations the Business Associate owes to Company. This satisfies 45 CFR §164.308(b)(2) and §164.502(e)(1)(ii).
- **Subprocessor disclosure.** Where a vendor relies on named subprocessors (common for SaaS), the vendor must maintain a current subprocessor list and notify Company in advance of material additions or changes, with a reasonable objection period.
- **Nth-party visibility.** The vendor inventory captures known subcontractors and subprocessors for high-criticality / high-data-sensitivity vendors. Where full Nth-party visibility is not obtainable, the Security Officer documents a risk acceptance and any compensating controls.
- **Breach notification cascade.** Each BAA must require the Business Associate to notify Company of any breach of unsecured PHI without unreasonable delay (and no later than the period specified in the BAA), regardless of whether the breach occurred at the Business Associate or a downstream subcontractor.
- **Audit and termination rights.** Each BAA must preserve Company's right to terminate if the Business Associate (or any of its subcontractors) materially breaches and fails to cure within a reasonable period, and must require the Business Associate to obtain equivalent rights from its subcontractors.

### 4. Cybersecurity Supply Chain Risk Management (C-SCRM)

Company's third-party risk program extends to the cybersecurity supply chain: the software, infrastructure, and services that compose Company's technology stack. The Security Officer owns C-SCRM in coordination with the CTO and the Privacy Officer.

#### 4.1 Third-party software and dependency inventory

Company maintains an inventory of third-party software in production and operational use, including SaaS applications, infrastructure providers, container base images, and notable open-source software (OSS) libraries that are integral to the Millie application. SaaS vendors that process PHI or PII are tracked alongside their declared subprocessors in the vendor inventory (see §1). Production container images are built from a known, supported base image set; image provenance is captured at build time and pinned by digest where practical.

#### 4.2 Vulnerability management for dependencies

Application code repositories use automated dependency scanning (e.g., GitHub Dependabot or equivalent) to surface known vulnerabilities in declared dependencies. Findings are triaged by the engineering team and remediated per the patch SLA defined in `sdlc-and-asset-lifecycle.md`. Production container images are scanned for known vulnerabilities at build time and on a periodic cadence; high-severity findings block deployment or trigger an expedited fix. The Security Officer subscribes to security advisories for critical SaaS vendors (e.g., Aptible, AWS, Cloudflare, GitHub) and reviews them on a continuous basis.

#### 4.3 License compliance and SBOM

Open-source dependencies are reviewed for license compatibility with Company's commercial and clinical use; engineering will not introduce dependencies under incompatible licenses without Security Officer and Legal review. Where a vendor provides a Software Bill of Materials (CycloneDX, SPDX, or equivalent), Company will request and retain a copy for critical software in the vendor inventory. For Company's own application, an SBOM is generated from dependency manifests on a best-effort basis and made available upon assessor request.

#### 4.4 Vendor assurance review cadence

For vendors with access to PHI, PII, or other sensitive Company information, the Security Officer reviews available third-party assurance artifacts on a defined cadence:

| Vendor tier | Assurance evidence reviewed | Cadence |
| --- | --- | --- |
| Critical (PHI processor, infrastructure provider) | SOC 2 Type II, HITRUST, ISO 27001, or equivalent; penetration test summary; subprocessor list | Annually, and upon material change |
| High (PII processor, business-system SaaS) | SOC 2 Type II or equivalent | Annually |
| Moderate (limited data exposure) | Vendor security questionnaire; public trust/security page | Every 24 months |
| Low (no sensitive data) | Vendor questionnaire at onboarding | At onboarding only |

Where an expected assurance artifact (e.g., SOC 2 Type II) is unavailable, the Security Officer documents the gap and any compensating controls in the vendor record.

### 5. Vendor Onboarding Security Assessment

Before access is granted, every vendor that will create, receive, maintain, transmit, access, or otherwise process Company PHI, PII, or other sensitive information completes Company's security assessment intake. The current questionnaire template is maintained in [`../ECH Security Assessment Questions - Questions.csv`](../ECH%20Security%20Assessment%20Questions%20-%20Questions.csv).

Onboarding workflow:

1. **Intake.** The internal business owner submits a vendor intake to the Security Officer identifying business purpose, data types to be shared, integration pattern, and criticality.
2. **Questionnaire & evidence.** The vendor completes the security assessment questionnaire (depth scaled to risk tier per §4.4); the Security Officer reviews responses together with available assurance artifacts (SOC 2, HITRUST, penetration test summary, SBOM where applicable) and documents findings.
3. **Contracting.** Where PHI is in scope, the Privacy Officer executes a BAA (see §2.2) prior to access. Where PII or other sensitive data is in scope but PHI is not, the Privacy Officer and Legal determine whether a Data Use Agreement, Data Processing Addendum, or equivalent is required.
4. **Provisioning.** Access is provisioned only after contracts are executed and the vendor record is added to the vendor inventory with owner, BAA/DPA status, data scope, criticality, and renewal date.

### 6. Vendor Annual Review and Offboarding

**Annual review.** Each vendor in the inventory receives a review at least annually (more frequently if criticality, data sensitivity, or recent incidents warrant). The review confirms: continued business need; current data scope and access; BAA/DPA still in force; current assurance artifacts on file (per §4.4); any material changes in vendor services, ownership, subprocessors, or security posture; and outstanding remediation items. The Privacy Officer monitors BAA renewals for continued HIPAA compliance. Material risks are escalated through Company's risk management process per `governance-and-risk-management.md`.

**Trigger-based reviews.** A vendor review is also performed on: material change in vendor services or data access; a confirmed or suspected security incident or breach affecting the vendor; significant change in vendor ownership or corporate structure; changes in applicable legal or contractual requirements; or other material change in business operations.

**Offboarding.** When a vendor relationship ends: (a) all access granted to the vendor (and vice versa) is revoked promptly and the vendor inventory record is updated to reflect termination; (b) per the executed BAA or DPA, the vendor must return or securely destroy all Company PHI / sensitive data in its possession and, where required, certify destruction in writing; (c) the return-or-destroy obligation flows down to the vendor's subcontractors and subprocessors that held Company data; (d) the signed BAA, the security assessment, the assurance artifacts, and any destruction certification are retained in the `Contracts > BAAs` folder consistent with Company's records retention schedule.

## IV. Training & Awareness

All personnel involved in vendor selection, contracting, or oversight shall receive training on this Policy at the time of role assignment, with annual updates thereafter, in accordance with the [governance-and-risk-management.md](governance-and-risk-management.md) Training Program.

## V. Sanctions

Any personnel member who violates this Policy will be subject to disciplinary action, up to and including termination of employment or engagement, in accordance with Company HR policy. Vendors that violate their contractual obligations under a Business Associate Agreement or Data Use Agreement may be subject to contract termination, financial penalties, and reporting to the Office for Civil Rights as required by HIPAA.

## VI. References

**Regulatory:**

- 45 CFR §164.308(b) — Business associate contracts and other arrangements (administrative safeguards).
- 45 CFR §164.314(a) — Business associate contracts (organizational requirements / security).
- 45 CFR §164.502(e) — Disclosures to business associates.
- 45 CFR §164.504(e) — Business associate contracts (privacy).

**Questionnaire mapping:**

- SIG Lite 2025 — Section B (Nth Party / Supply Chain Management): B.1, B.2.
- SIG Lite 2025 — Section S (Supply Chain Risk Management): S.1, S.32, S.57, S.61, S.80, S.100.

**Linked Millie policies:**

- [governance-and-risk-management.md](governance-and-risk-management.md) — risk management framework, training program, sanctions.
- [hipaa-definitions.md](hipaa-definitions.md) — defined terms (Business Associate, PHI, Subcontractor, etc.).
- [incident-and-breach-response.md](incident-and-breach-response.md) — incident and breach handling, including vendor-originated incidents.
- [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md) — patch SLAs, change management, secure development.
- [`../ECH Security Assessment Questions - Questions.csv`](../ECH%20Security%20Assessment%20Questions%20-%20Questions.csv) — vendor security questionnaire template (lives at repo root, not in this folder).

## VII. Definitions used in this Policy

Defined terms (Business Associate, Subcontractor, PHI, etc.) follow [hipaa-definitions.md](hipaa-definitions.md). Terms specific to this Policy:

- **Nth-Party.** Any party in the supply chain downstream of a direct vendor — subcontractors of a Business Associate ("fourth party"), and their subcontractors in turn ("fifth party," etc.). Shorthand for "any party further down the chain than Company's direct counterparty."
- **C-SCRM (Cybersecurity Supply Chain Risk Management).** The discipline of identifying, assessing, and managing cybersecurity risk introduced by third-party software, infrastructure, services, and the broader supply chain that supports Company's technology stack. Aligned with NIST SP 800-161.
- **Subprocessor.** A third party engaged by a Business Associate or vendor to process Company PHI or PII on the vendor's behalf (e.g., a vendor's cloud-hosting, email-delivery, or analytics provider). A subprocessor is a form of Subcontractor under HIPAA when PHI is involved.
- **SBOM (Software Bill of Materials).** A formal, machine-readable inventory of the components (libraries, packages, dependencies) that comprise a software product, typically in CycloneDX or SPDX format.
- **Vendor inventory.** The authoritative tracker maintained by the Security Officer recording, for each third party with access to Company data: owner, business purpose, data type, access level, criticality / risk tier, BAA or other contractual status, renewal / review date, and known subcontractor or subprocessor considerations.

## VIII. Revision history

| Date | Author | Change |
| --- | --- | --- |
| 2022-05-02 | Privacy Officer | Original Business Associate Agreement Policy (L-001) issued. |
| 2026-05-23 | Security Officer | Information Security & Data Governance Framework §11 (Third-Party & Vendor Management) issued under IT-026. |
| 2026-05-24 | Privacy Officer | Consolidated L-001 and Framework §11 into this Policy; added C-SCRM section; added subcontractor / Nth-party flow-down section; added vendor onboarding, annual review, and offboarding sections; added Sanctions clause. |

## Appendix A — BAA Template Locations

The current BAA templates are maintained alongside the original docx-format policies in the `Policy Docs/` folder. Executed BAAs are stored in the Millie Google Workspace `Contracts > BAAs` folder per §2.2.

- Current BAA template (for Company use as Covered Entity): `Policy Docs/03c HIPAA - Business Associate Agreement Policy.docx`.
- Current BAA template (for Business Associate use with its Subcontractors): `Policy Docs/HIPAA - Millie_BAA (for BA Use with Subcontractor).docx` (legacy `.doc` version also present as `Policy Docs/03l HIPAA - Millie_BAA (for BA Use with Subcontractor).doc`).

Use of any template other than the current Company-approved form, or modification of an approved form, requires Privacy Officer approval per §2.2.
