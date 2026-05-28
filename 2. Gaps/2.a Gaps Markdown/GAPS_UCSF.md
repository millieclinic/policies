# UCSF Security Review — Actionable Gaps

Subset of `coverage_matrix_UCSF.csv` showing the 11 rows that are either **Partial / None** coverage or **High / Medium** flag risk. Each is either fixable with a short policy clause OR requires a supporting document to be created (HR / Tenisi / operational SOP).

## Policy edits needed (2)

| # | Section | Question | Fix file | Fix text (excerpt) |
|---|---|---|---|---|
| 11 | Risk Management | Is there a policy defining organizational risk tolerance and risk acceptance aut… | `01c. Risk Management Policy` | Append 1-paragraph clause to Risk Management Policy: Risk acceptance authority is held by the Chief Security Officer for operational risks; material risks must … |
| 25 | Configuration Management | Are configuration change control processes in place?… | `06b. SDLC & Asset Lifecycle Policy` | Append 1-paragraph Change Management section to SDLC Policy: Changes to production systems require peer review and approval through GitHub pull-request + Aptibl… |

## Supporting docs needed (9)

| # | Section | Question | Doc to create |
|---|---|---|---|
| 3 | Asset Management | Are platforms (hardware, devices, applications, software) prioritized based on t… | Create a Critical Systems & Recovery Priority Matrix (systems × sensitivity × criticality × owner × RTO/RPO × restart order). |
| 9 | Risk Management | Are threats, both internal and external, identified and documented in the risk a… | Attach current threat register showing internal/external threats by category, vulnerabilities, controls, likelihood, impact, residual risk, owner. |
| 16 | Training | Do you track and measure user training completion?… | Create Training Completion Tracking SOP + roster/export (assignment, completion, reminders, acknowledgement retention). |
| 17 | Vendor Management | Do you have a formal vendor management program that requires a minimum level of … | Create Vendor Risk Management Program SOP (vendor inventory, risk tier, HIPAA/security questionnaire, BAA review, approval workflow, periodic reassessment) + ev… |
| 29 | HR Security | Do you conduct background checks on all members of the workforce, and exit inter… | HR to add: background-check scope and timing, exit checklist including HIPAA confidentiality reminder, access handoff to IT. Capture as HR SOP or 1-paragraph at… |
| 30 | Access Control | Is there a formal process for provisioning and removal of all user accounts, and… | Create Access Provisioning & Deprovisioning SOP (request, approval, role mapping, least privilege, provisioning, periodic review, termination/offboarding SLAs, … |
| 32 | Data Mapping | Have you mapped all internal and external data flows?… | Create Internal/External Data Flow Map and Data Inventory (system inventory, PHI categories, source/destination, transfers, vendors, storage locations, encrypti… |
| 35 | Network Security | Is the network monitored to detect potential cybersecurity events?… | Create Network Security Monitoring / IDS-IPS Statement (coverage, Tenisi alerting, review cadence, escalation, sample alert evidence). |
| 36 | Physical Security | Is the physical environment monitored to detect potential security events? (came… | Create per-site Physical Security Monitoring Statement (locks, cameras, badge/access controls, visitor logs, restricted areas, responsible owner, exceptions). |

