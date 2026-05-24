---
title: "System Development Life Cycle (SDLC) & Asset Lifecycle"
sources: ["System Development Life Cycle (SDLC) & Asset Lifecycle Policy.pdf (Policy # IT-009)"]
supersedes: ["IT-009 SDLC & Asset Lifecycle Policy"]
last_reviewed: 2026-05-24
owner: "CTO (Security Officer co-owner)"
status: "active"
---

# System Development Life Cycle (SDLC) & Asset Lifecycle

> **Source.** Originally `System Development Life Cycle (SDLC) & Asset Lifecycle Policy.pdf`. The source PDF was mis-stamped with the header "Security Incident Management Policy / IT-026"; that header was a copy-paste error in the source Word template and has been corrected here. The corrected Policy # is **IT-009**. The original PDF remains in `Policy Docs/` for audit history; the original Markdown conversion is archived in `New Policy Docs/_archive/`.
>
> Expanded 2026-05-24 with Change Management, Patch Management SLA, Code Integrity, and Secure Coding pointers in response to gaps surfaced by the ECH Security Assessment ([POLICY-VS-QUESTIONNAIRE-MAPPING.md](../POLICY-VS-QUESTIONNAIRE-MAPPING.md) SIG G.2, OWASP A03/A04/A06/A08/A10, SIG N.4).

## I. Scope

This Policy applies to Company information systems, software platforms, cloud services, endpoints, mobile devices, and hardware assets that are used to create, receive, maintain, or transmit Company data or Protected Health Information ("PHI"). It applies to all Company personnel and contractors responsible for implementing, maintaining, or supporting Company systems.

## II. Policy

Millie, Inc. ("Company") maintains a System Development Life Cycle ("SDLC") and asset lifecycle management process to ensure systems and hardware are appropriately planned, deployed, maintained, and retired in a secure manner. Security, privacy, and operational requirements shall be considered throughout the lifecycle of Company systems and assets.

Company systems and assets shall be managed in accordance with applicable Company policies, including:

- [governance-and-risk-management.md](governance-and-risk-management.md) (Risk Management)
- [technical-safeguards.md](technical-safeguards.md) (Encryption, Passwords, Remote Access, Workstation Use, Device & Media Management)
- [operational-safeguards.md](operational-safeguards.md) (Administrative & Physical Safeguards, Contingency)
- [incident-and-breach-response.md](incident-and-breach-response.md)
- [network-and-cloud-security.md](network-and-cloud-security.md)
- [vendor-and-business-associates.md](vendor-and-business-associates.md)

## III. Procedure

### 1. Planning & Acquisition

Prior to implementation of new systems, applications, or hardware, Company will evaluate:

- Business and operational needs;
- Security and privacy requirements;
- Whether the system will access or store PHI;
- Vendor security considerations (see [vendor-and-business-associates.md](vendor-and-business-associates.md) and the ECH security questionnaire at [`../ECH Security Assessment Questions - Questions.csv`](../ECH%20Security%20Assessment%20Questions%20-%20Questions.csv));
- Backup, access, and support requirements; and
- Total cost of ownership including security tooling.

Where applicable, Business Associate Agreements will be executed before vendors are permitted to access PHI.

### 2. Secure Design & Development

Secure design and development practices apply to all software Company builds or materially modifies.

#### 2.1 Secure Coding Standard

Company developers shall follow established secure-coding guidance, including:

- **OWASP ASVS** (Application Security Verification Standard) for web/API applications;
- **OWASP Top 10** awareness training for all engineers;
- Language- and framework-specific best practices (e.g., parameterized queries to prevent SQL injection per OWASP A03; output encoding to prevent XSS).

Code involving authentication, authorization, cryptography, or PHI access requires Security Officer or designee review prior to merge.

#### 2.2 AppSec Role in SDLC

Security review is integrated into the SDLC at: (a) design phase for new features touching PHI or authentication, (b) pre-merge review for security-sensitive code, and (c) pre-deployment review for material releases. The Security Officer is accountable; engineering peers conduct day-to-day review. (Addresses OWASP A04 — Insecure Design.)

#### 2.3 Code Integrity & Signed Artifacts

Source code is version-controlled in GitHub with branch protection and required reviews. Build artifacts (container images, application bundles) shall be:

- Produced through repeatable, automated pipelines (Infrastructure as Code per §6.1 below);
- Stored in trusted registries;
- Signed where feasible (container image signing); and
- Verified at deployment time.

Manual edits to production artifacts outside the pipeline are prohibited without documented emergency-change approval. (Addresses OWASP A08 — Software and Data Integrity Failures.)

### 3. Configuration & Deployment

Systems and devices shall be configured using established security baselines prior to production use, including where appropriate:

- Password protection per [technical-safeguards.md](technical-safeguards.md) §1;
- Access controls (RBAC, least privilege);
- Encryption at rest and in transit per [technical-safeguards.md](technical-safeguards.md) §2;
- Multi-factor authentication; and
- Secure remote access protections.

Access to systems containing PHI shall be limited to authorized personnel.

### 4. Testing & Implementation

Company will perform testing and validation prior to deployment of new systems or material system changes to confirm:

- Systems function as intended;
- Security controls are operating appropriately;
- Access restrictions are properly configured; and
- No regressions in privacy or security posture.

Where feasible, security testing includes automated dependency scanning, static analysis (SAST), and dynamic analysis (DAST) of authenticated paths.

### 5. Change Management

(Addresses SIG G.2.) All material changes to production systems shall be tracked through a documented change management process.

#### 5.1 Change Categories

- **Standard change** — pre-approved, low-risk, repeatable (e.g., dependency patch within established SLA). Documented, no separate approval required.
- **Normal change** — non-routine change requiring review and approval. Requires: change request, security impact review, deployment plan, rollback plan, and approval from CTO or designee (Security Officer for security-sensitive changes).
- **Emergency change** — change required to address a production incident or security vulnerability under active exploit. Expedited approval verbally (CTO or Security Officer); post-implementation review within 5 business days.

#### 5.2 Required Artifacts for Normal Changes

- Description of change and rationale;
- Risk assessment (privacy, security, operational);
- Testing performed;
- Rollback plan;
- Approval signatures;
- Post-deployment verification.

#### 5.3 Audit Trail

All changes deployed to production are traceable via version control, deployment logs, and change request records. Records are retained per [governance-and-risk-management.md](governance-and-risk-management.md) §6 Records Retention Schedule.

### 6. Operations & Maintenance

Company systems and hardware shall be maintained throughout their operational lifecycle through activities including:

#### 6.1 Infrastructure as Code (IaC)

All AWS infrastructure is managed through Terraform; application configuration is managed through Aptible. IaC changes follow the change management process in §5. Manual ("ClickOps") changes to production infrastructure are prohibited except under emergency change.

#### 6.2 Patch Management & SLA

(Addresses OWASP A06, SIG N.4.) Security patches are applied per the following SLA:

| Severity | SLA from vendor advisory / KEV listing |
|---|---|
| Critical (CVSS 9.0+ or actively exploited / KEV) | 7 calendar days |
| High (CVSS 7.0–8.9) | 30 calendar days |
| Medium (CVSS 4.0–6.9) | 90 calendar days |
| Low (CVSS < 4.0) | Next regular maintenance cycle |

Patching of managed services (Aptible, RDS, Cloudflare) is inherited from those vendors; Company monitors vendor advisories and pushes vendor-released patches into application code per the same SLA. Open-source dependency patches are tracked through automated dependency scanning (e.g., Dependabot) with PRs reviewed per §2.1.

#### 6.3 Vulnerability Scanning

- **Application dependencies** — automated scanning on every PR + nightly scan of main branch.
- **Container images** — scanned at build time and weekly thereafter.
- **Cloud infrastructure** — see [network-and-cloud-security.md](network-and-cloud-security.md) §7 Detection & Monitoring.
- **Findings** triaged within 5 business days; remediation per the patch SLA above.

#### 6.4 Other Maintenance Activities

- User access reviews (cadence per [README.md](../README.md) Quarterly section);
- Monitoring for security incidents per [incident-and-breach-response.md](incident-and-breach-response.md);
- Backup and recovery per [operational-safeguards.md](operational-safeguards.md) §4 Contingency Planning;
- Replacement of unsupported systems where feasible;
- Periodic risk assessments per [governance-and-risk-management.md](governance-and-risk-management.md) §4.

### 7. Retirement & Disposal

When systems or hardware are retired, replaced, transferred, or disposed of, Company shall:

- Remove or disable system access;
- Remove Company data and PHI where applicable;
- Sanitize or destroy storage media per [technical-safeguards.md](technical-safeguards.md) §5 Device & Media Management (NIST SP 800-88 sanitization guidelines);
- Update asset inventories in [platform-and-access-matrix.md](platform-and-access-matrix.md).

Electronic media containing PHI shall be disposed of in a secure manner consistent with Company policies and applicable HIPAA requirements.

## IV. Training & Awareness

All engineering personnel shall complete secure-coding and SDLC training at the time of role assignment, with annual updates thereafter, in accordance with the [governance-and-risk-management.md](governance-and-risk-management.md) Training Program. Training includes OWASP Top 10, secure-by-design principles, and Company-specific change management procedures.

## V. Sanctions

Any personnel member who violates this Policy — including bypassing change management, deploying without required review, or failing to apply patches within SLA — will be subject to disciplinary action, up to and including termination of employment or engagement, in accordance with Company HR policy. Severity is assessed based on intent, the nature of the systems involved, and impact on PHI confidentiality, integrity, or availability. Sanctions are documented and tracked by the Privacy Officer.

## VI. References

- HIPAA Security Rule — 45 C.F.R. §§ 164.308(a)(1), 164.308(a)(8), 164.312
- NIST SP 800-218 — Secure Software Development Framework (SSDF)
- NIST SP 800-88 — Guidelines for Media Sanitization
- OWASP ASVS, OWASP Top 10
- SIG Lite 2025 §G (IT Operations Management), §N.4 (Patch Management)
- Linked Millie policies as referenced inline above.

## VII. Definitions used in this Policy

Defined terms (PHI, Workforce, etc.) follow [hipaa-definitions.md](hipaa-definitions.md). Terms specific to this Policy:

- **IaC (Infrastructure as Code)** — declarative configuration of infrastructure managed in version control and deployed through automated pipelines.
- **SBOM (Software Bill of Materials)** — inventory of components, libraries, and dependencies that make up a software artifact.
- **KEV (Known Exploited Vulnerabilities)** — CISA-maintained catalog of vulnerabilities with evidence of active exploitation; treated as Critical regardless of CVSS score.
- **Change** — any modification to a production system, configuration, or piece of code that is deployed to or affects users.

## VIII. Revision history

| Date | Change | By |
|---|---|---|
| 2022 | Original SDLC & Asset Lifecycle Policy adopted (IT-009). | Original policy |
| 2026-05-18 | Source PDF updated. | (per source) |
| 2026-05-24 | Corrected mis-stamped header ("Security Incident Management Policy / IT-026" → "SDLC & Asset Lifecycle / IT-009"). Added §2 Secure Design & Development (OWASP A03, A04, A08), §5 Change Management (SIG G.2), §6.2 Patch Management SLA (OWASP A06, SIG N.4), §6.3 Vulnerability Scanning. Normalized "Chief Security Officer" → "Security Officer". Replaced inline policy name references with relative links to consolidated files. | Consolidation effort |
