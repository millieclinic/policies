---
title: "Network & Cloud Security"
sources: []
supersedes: []
last_reviewed: 2026-05-24
owner: "Security Officer + CTO (joint)"
status: "active"
---

# Network & Cloud Security

> **New policy authored 2026-05-24** to close gaps in SIG Lite 2025 §N (Network Security) and the AWS Questionnaire surfaced by the ECH Security Assessment. This policy codifies current Millie cloud posture; items marked TODO are tracked in [TODO.md](../TODO.md).

## I. Scope

This Policy applies to all Company network infrastructure, cloud services (AWS, Aptible, Cloudflare, Snowflake, and any other cloud platform listed in [platform-and-access-matrix.md](platform-and-access-matrix.md)), and to all Company personnel who configure, operate, or access these services.

## II. Policy

Millie, Inc. ("Company") operates a cloud-native production environment and shall maintain documented standards for cloud account management, identity and access, network segmentation, encryption, detection and monitoring, and patch management that are reasonable and appropriate to safeguard the confidentiality, integrity, and availability of Protected Health Information ("PHI") and other sensitive Company data. Inherited controls from managed-service providers (Aptible, AWS, Cloudflare) are recognized as primary safeguards; Company-managed configurations must align with this Policy and with [technical-safeguards.md](technical-safeguards.md). Known deviations are documented in [TODO.md](../TODO.md) and reviewed by the Security Officer at least quarterly.

## III. Procedure

### 1. Network Architecture Overview

Millie is cloud-native; production traffic does not traverse a Company-owned data center. The architecture has three tiers:

- **Aptible** — application containers, managed PostgreSQL/Redis, production VPC, TLS termination, and managed-database backups (runs on AWS underneath).
- **AWS** — single account used for S3 object storage, IAM, GuardDuty, CloudTrail, the Snowflake-to-S3 integration, the long-term S3 log archive, and Terraform state.
- **Cloudflare** — DNS, CDN, WAF, and DDoS protection at the edge.

On-premise networking is limited to office WiFi (see §8); no production traffic, PHI, or scoped data traverses the office network. Staff reach production services over the public Internet through authenticated, encrypted channels.

### 2. IAM & Authentication Standard

*Addresses AWS Questionnaire rows 4–7, 11–17 and SIG H.1.*

- **Root account.** Shared email alias (Q5). MFA enabled, no active access keys (Q6). Used only for break-glass actions — most recent use was enabling GuardDuty (Q7).
- **IAM users.** Console access requires IAM user + 2FA (Q11–12). SAML SSO is **not** in place; migration to SSO is tracked in [TODO.md](../TODO.md) #12 and is the Company's stated direction.
- **Programmatic access keys.** Used for narrow service integrations — primarily Aptible deploy automation and backend S3 writes (Q13). Rotated at least every 90 days (Q15). One unused staging key tied to in-progress SES setup is retained and tracked in [TODO.md](../TODO.md) #17 (Q14).
- **IAM roles.** Preferred over long-lived users for service-to-service access (e.g., Snowflake integration). Roles unused >90 days are reviewed for removal (Q16, TODO #18).
- **Known IAM gaps — acknowledged for assessor transparency.** Console-access IAM users exist (Q11, TODO #12). Wildcard admin policies — including AWS-managed `AdministratorAccess` and full-S3/IAM policies — exist on a limited set of identities (Q17, TODO #14). These deviations from least-privilege are accepted at Company scale pending SSO migration and policy-scoping; the Security Officer reviews the IAM inventory at least quarterly.

### 3. Secrets Management

*Addresses AWS Questionnaire row 19.*

Secrets shall be stored only in approved secret stores:

- **Application runtime secrets** — Aptible environment variables (encrypted at rest, scoped per app).
- **Workforce shared secrets** — 1Password vaults, scoped by team.
- **Prohibited.** Secrets in source code, plaintext config, chat, email, or ticket systems.

AWS Secrets Manager and SSM Parameter Store are **not** currently used (Q19); migration is under consideration. Service credentials and access keys are rotated at least every 90 days, on personnel offboarding, and on any suspected compromise. Workforce passwords follow the [technical-safeguards.md](technical-safeguards.md) Password Standard.

### 4. VPC, Subnet & Network Segmentation

*Addresses AWS Questionnaire rows 20–23 and SIG N.3, N.8.*

- **Inbound.** No security group permits non-HTTP/HTTPS access from the Internet (Q20); public app endpoints sit behind Cloudflare.
- **Database isolation.** All RDS instances are in private subnets and not publicly accessible (Q22); access is mediated through the Aptible integration.
- **Outbound.** Security groups govern outbound access for each VPC; egress flows through security groups, NAT gateways, and centralized monitoring (Q23).
- **Public subnet — known deviation.** All subnets are associated with a private local route table, but a public route table remains in the account (Q21). Remediation tracked in [TODO.md](../TODO.md) #15.
- **DMZ.** No traditional DMZ. The cloud-native equivalent is application-layer isolation: Cloudflare WAF + Aptible's hosted-app boundary terminate untrusted traffic before it reaches containers, and databases sit in private subnets unreachable from the Internet (SIG N.8).

### 5. S3 Storage Posture

*Addresses AWS Questionnaire rows 24–25, 27, 32.*

- **Block public access** is enabled on all S3 buckets (Q25). No bucket permits open access or grants access to "any authenticated AWS user" (Q24).
- **CloudTrail data events / S3 access logging** are enabled (Q27).
- **Backups.** Primary database backups via Aptible managed point-in-time recovery. Long-term application logs and other data archived to S3 with bucket-level encryption and versioning where appropriate.
- **Dedicated backup account — NOT in place** (Q32). On the roadmap; current single-account posture is documented as accepted risk until scheduled.

### 6. Encryption

*Addresses AWS Questionnaire rows 9–10.*

- **At rest.** RDS and managed data stores use Aptible-managed encryption (Q9; see [Aptible docs](https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-encryption/database-encryption)).
- **EC2 volumes.** Volume encryption applied where Company directly operates EC2 (Q10); direct EC2 footprint is small because compute is delivered through Aptible.
- **In transit.** TLS 1.2+ for all external traffic; terminated at Cloudflare and Aptible.

Full encryption standards — FIPS 140-2 modules, NIST SP 800-52/77/113 in transit, NIST SP 800-111 at rest — are stated in [technical-safeguards.md](technical-safeguards.md) §Encryption and apply to all cloud-stored Company data.

### 7. Detection & Monitoring

*Addresses AWS Questionnaire rows 26–28 and SIG N.7.*

- **GuardDuty** is enabled in all active AWS regions and serves as the Company's intrusion detection capability (Q28).
- **CloudTrail** records management events and S3 data events (Q27); logs feed CloudWatch.
- **CloudWatch** is the centralized log destination for AWS services and Aptible application logs.
- **AWS Config — NOT enabled** (Q26). Acknowledged gap tracked in [TODO.md](../TODO.md) #16; accepted risk pending assessor feedback. Will be enabled if requested or if the Security Officer determines it is needed.

Log review cadence, alerting thresholds, and retention are governed by [technical-safeguards.md](technical-safeguards.md) §Logging & Monitoring and [information-security-framework.md](information-security-framework.md) §9.

### 8. Network Device & Wireless

*Addresses SIG N.9, N.11, N.12.*

The office network is for workforce productivity only; no production systems, PHI, or scoped data are hosted on or routed through it.

- **Wireless.** WPA3 (or WPA2-AES where WPA3 is not yet supported). Pre-shared keys rotated on personnel offboarding affecting many users.
- **Guest isolation.** Separate guest SSID isolated from the business network at the AP/router level; guest traffic cannot reach business devices.
- **No default passwords.** Default admin passwords on any office network device — APs, routers, switches — are changed before the device enters service (SIG N.12).
- **Baseline.** Vendor-recommended secure baselines; admin interfaces not exposed to the Internet (SIG N.11).
- **Patching.** Office network equipment patched on the vendor's released cadence and reviewed at least annually.

### 9. Patch Management for Network & Cloud

*Addresses OWASP A06 (CSV row 77, Remediate=Yes, TODO #2) and SIG N.4.*

Patch SLA for systems within Company control:

| Severity | SLA |
|---|---|
| Critical | 7 calendar days |
| High | 30 calendar days |
| Medium | 90 calendar days |
| Low | Next regular maintenance cycle |

- **Managed services** (Aptible, AWS RDS, Cloudflare) inherit the provider's patch cadence; the Company tracks provider status pages and applies any customer-side action (e.g., engine upgrades) within the SLA above.
- **Container base images** rebuilt on dependency-CVE alerts and at least monthly.
- **GitHub plan / version upgrade** in progress, tracked in [TODO.md](../TODO.md) #2.

Application code and developer-dependency patching is governed by [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md) §Operations & Maintenance.

### 10. SSRF & Outbound Network Defenses

*Addresses OWASP A10 (CSV row 81, FOLLOW UP, TODO #8).*

Server-Side Request Forgery (SSRF) is addressed with defense-in-depth:

- **Outbound URL allowlisting** where the application's outbound calls are limited to known destinations (e.g., payment processors, third-party APIs).
- **AWS instance metadata endpoint (`169.254.169.254`)** is explicitly blocked from application subnets, except where required by a specific managed-service integration using IMDSv2 with session-token authentication. IMDSv1 is prohibited on any Company-operated EC2.
- **Egress filtering** — outbound traffic from application subnets transits NAT gateways and is subject to §4 security groups; posture is deny-by-default for non-standard egress.
- **Application-layer mitigations** — input validation on user-supplied URLs, disallowing redirects to internal IP ranges, rejecting non-HTTP(S) schemes — required for any endpoint that fetches a URL on behalf of a user.

### 11. Hardening Baseline

*Addresses OWASP A05 (CSV row 76) and SIG D.1.*

- **Managed services preferred** over self-managed infrastructure to inherit vendor hardening.
- **Hardened base images** — container base images selected from minimal, vendor-supported distributions (e.g., distroless or official-slim). Unused services, packages, and ports removed.
- **CIS Benchmarks** (AWS Foundations, Docker) are the reference standard; the Company does not formally certify against CIS but uses them as input to configuration review.
- **Deviations** — including IAM and subnet deviations called out elsewhere in this Policy — require Security Officer approval and entry in [TODO.md](../TODO.md).

### 12. Infrastructure as Code (IaC)

*Addresses AWS Questionnaire row 29.*

- **Terraform** manages AWS, Aptible, and Cloudflare resources; state stored in S3 with block-public-access, SSE, versioning, and access restricted to a narrow IAM role.
- **Application configuration** managed in Aptible (env vars, app settings).
- **Change review** — IaC changes follow the Change Management subsection of [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md): PR review, peer approval, `terraform plan` reviewed before apply, rollback strategy identified for material changes.

### 13. AWS-Specific Incident Response

*Addresses AWS Questionnaire row 31.*

The AWS/Aptible incident playbook is maintained in [incident-and-breach-response.md](incident-and-breach-response.md) §III(3) and is not duplicated here. Cloud-specific containment actions enumerated there include revoking IAM credentials, isolating affected security groups, snapshotting affected EBS volumes for forensics, and rotating exposed keys.

### 14. DR & Backup Testing in the Cloud

*Addresses SIG K.2, K.5.*

The enterprise DR Testing Program is defined in [operational-safeguards.md](operational-safeguards.md) §Contingency Planning. Cloud-specific cadence layered on top:

- **Monthly** — restore-test of an Aptible-managed RDS snapshot into a non-production environment; success/failure logged.
- **Quarterly** — failover or recovery drill exercising the cloud-IR runbook (e.g., bringing an environment up in a secondary region or from a clean snapshot).
- **Annually** — end-to-end DR exercise per the operational-safeguards DR Testing Program.

Test outcomes and corrective actions are logged and reported to the Security Officer.

### 15. AWS Questionnaire Coverage Statement

The 33 AWS Questionnaire rows in `ECH Security Assessment Questions - Questions.csv` (rows 2–33) document current implementation state. This Policy is the written standard those answers map to; items answered NO with TODO follow-ups are tracked in [TODO.md](../TODO.md).

## IV. Training & Awareness

> Personnel with cloud or infrastructure administrative access shall complete cloud-security training (AWS/Aptible) within 30 days of access provisioning, with annual updates thereafter, in accordance with the [governance-and-risk-management.md](governance-and-risk-management.md) Training Program.

## V. Sanctions

> Any personnel member who violates this Policy will be subject to disciplinary action, up to and including termination of employment or engagement, in accordance with Company HR policy. Misconfiguration of cloud services that results in PHI exposure may trigger a breach assessment under [incident-and-breach-response.md](incident-and-breach-response.md). Sanctions are documented and tracked by the Privacy Officer.

## VI. References

- **SIG Lite 2025 §N — Network Security** (N.1, N.2, N.3, N.4, N.5, N.7, N.8, N.9, N.11, N.12).
- **AWS Well-Architected Framework** — Security Pillar.
- **CIS AWS Foundations Benchmark** (current version).
- **OWASP Top 10 (2021)** — A05 Security Misconfiguration, A06 Vulnerable & Outdated Components, A10 SSRF.
- **45 CFR §164.312** — HIPAA Security Rule Technical Safeguards; **§164.308(a)(1)** — Risk Analysis & Management.
- Linked Millie policies: [information-security-framework.md](information-security-framework.md) · [technical-safeguards.md](technical-safeguards.md) · [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md) · [incident-and-breach-response.md](incident-and-breach-response.md) · [operational-safeguards.md](operational-safeguards.md) · [governance-and-risk-management.md](governance-and-risk-management.md) · [platform-and-access-matrix.md](platform-and-access-matrix.md) · [hipaa-definitions.md](hipaa-definitions.md).
- Evidence: `ECH Security Assessment Questions - Questions.csv` rows 2–33 (AWS), 76/77/81 (OWASP A05/A06/A10), 136–145 (SIG N).
- [TODO.md](../TODO.md) — open remediation items referenced throughout this Policy.

## VII. Definitions used in this Policy

HIPAA-defined terms are listed in [hipaa-definitions.md](hipaa-definitions.md). Additional terms used here:

- **IaC (Infrastructure as Code).** Provisioning and managing infrastructure through machine-readable definition files (e.g., Terraform) under source control and code review, rather than manual console actions.
- **Hardening Baseline.** A documented set of configuration settings — applied at build or deploy time — that reduces attack surface by disabling unused services, removing default credentials, restricting permissions, and applying vendor security settings (e.g., CIS Benchmarks).
- **SSRF (Server-Side Request Forgery).** A vulnerability in which an attacker causes a server to make HTTP requests to attacker-chosen destinations, including internal services or cloud metadata endpoints (e.g., `169.254.169.254`).
- **DMZ (Demilitarized Zone).** Traditionally a perimeter network segment between the Internet and a trusted internal network. In a cloud-native architecture, the equivalent function is provided by edge services (Cloudflare WAF), the managed app boundary (Aptible), and private subnets for backend resources.
- **VPC (Virtual Private Cloud).** A logically isolated section of a cloud provider's network where the Company provisions subnets, route tables, and security groups.
- **Egress filtering.** Controls applied to outbound traffic leaving Company networks or subnets — destination allowlists, deny-by-default rules, NAT-gateway routing — intended to limit data exfiltration and SSRF impact.

## VIII. Revision history

| Date | Version | Author | Summary of changes |
|---|---|---|---|
| 2026-05-24 | 1.0 | Security Officer + CTO | Initial publication. Codifies existing Millie AWS / Aptible / Cloudflare cloud posture into a written policy to back the AWS Questionnaire (CSV rows 2–33) and SIG Lite 2025 §N (CSV rows 136–145). Open remediation items tracked in [TODO.md](../TODO.md). |
