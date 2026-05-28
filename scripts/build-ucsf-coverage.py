#!/usr/bin/env python3
"""build-ucsf-coverage.py — produce the UCSF Security Review coverage matrix.

Sources the 39 UCSF questions (already categorized by a prior AI pass embedded
in the source xlsx's "AI - Categorized Questions" sheet) and re-grades each
against the CURRENT consolidated policy structure in
`Current Policies (… Generated)/3.a Final Markdown/`.

Writes:
  2. Gaps/2.a Gaps Markdown/coverage_matrix_UCSF.csv
  2. Gaps/2.a Gaps Markdown/SUMMARY_UCSF.md
  2. Gaps/2.a Gaps Markdown/GAPS_UCSF.md
"""

from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "2. Gaps" / "2.a Gaps Markdown"

# Mapping: old source filename -> new consolidated location (for human-readable citations)
# (Used in the Proposed Answer column.)
P = {
    "01a": "01a. Information Security Framework",
    "01b": "01b. HIPAA Definitions",
    "01c": "01c. Risk Management Policy",
    "01d": "01d. Safeguards Policy",
    "02a": "02a. Privacy Policy",
    "02b": "02b. Patient Rights — Access, Amendment & Accounting of Disclosures",
    "02c": "02c. PHI Use, Disclosure, Minimum Necessary & De-Identification",
    "03a": "03a. Technical Safeguards — Encryption, Passwords, Remote Access & Workstations",
    "04a": "04a. Contingency Planning Policy",
    "04b": "04b. Paper Document Management Policy",
    "04c": "04c. COVID Policy",
    "04d": "04d. Medical Waste Management Plan",
    "05a": "05a. Incident & Breach Response",
    "06a": "06a. Business Associate Agreement Policy",
    "06b": "06b. SDLC & Asset Lifecycle Policy",
    "06c": "06c. BAA Template (Subcontractor)",
    "07b": "07b. Insurance Authorization Form Template",
    "ss_mat": "Supporting Sources/Millie Matrix of Platforms, Software Subscriptions, and Access (1).xlsx",
    "ss_risk": "Supporting Sources/Copy of Annual Risk Letter _ Mitigations from 03q HIPAA - Risk Management Policy.docx",
    "ss_dr": "Supporting Sources/Disaster Recovery Review - May 2026.xlsx",
}

# ROWS: each is a dict with the column values. Item # is the UCSF row number.
# Coverage: Full / Partial / None / N/A / Evidence-only
# Flag Risk: High / Medium / Low / None
ROWS = [
    # 1. Roles & responsibilities — workforce
    {
        "section": "Roles & Responsibilities",
        "item": "1",
        "question": "Are information security roles and responsibilities for the entire workforce established? Are all workforce members aware of and understand their role in information security? (logging off, securing patient records, etc.)",
        "plain": "Does everyone at Millie know what they personally need to do to keep patient data safe?",
        "coverage": "Full",
        "proposed": f"Yes. Millie's required Privacy & Security training covers workforce responsibilities (minimum-necessary access, breach reporting, device/password security, encryption, screen locking, secure document handling) and the {P['01d']} Policy assigns workforce-level safeguards. Workforce training acknowledgement is collected per {P['01d']} §IV.",
        "flag": "Low",
        "gap": "Confirm training acknowledgement process and refresh evidence (next training cycle).",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Refresh / finalize workforce security roles & responsibilities document and attach training acknowledgement records.",
    },
    # 2. Roles & responsibilities — third parties
    {
        "section": "Roles & Responsibilities",
        "item": "2",
        "question": "Are information security roles and responsibilities for third-party stakeholders established?",
        "plain": "Do our vendors know what they're responsible for protecting?",
        "coverage": "Full",
        "proposed": f"Yes. The {P['06a']} requires a BAA before any vendor creates, receives, maintains, or transmits PHI; the {P['ss_mat']} identifies third-party systems, access setup owners, license model, and admins.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 3. Platforms prioritized
    {
        "section": "Asset Management",
        "item": "3",
        "question": "Are platforms (hardware, devices, applications, software) prioritized based on the information they process, operational criticality, and business value?",
        "plain": "If everything went down at once, do you know which systems to bring back first?",
        "coverage": "Partial",
        "proposed": f"The {P['ss_mat']} is an application/platform inventory (priority column exists), and the {P['04a']} requires an IT inventory, but a documented recovery-priority order (RTO/RPO per system) is not yet formalized. User-stated software priority: backend, mobile app, admin/frontend.",
        "flag": "Medium",
        "gap": "No formal Critical Systems & Recovery Priority Matrix exists.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Create a Critical Systems & Recovery Priority Matrix (systems × sensitivity × criticality × owner × RTO/RPO × restart order).",
    },
    # 4. Security policy implemented
    {
        "section": "Security Program",
        "item": "4",
        "question": "10) Has your organization implemented a security policy? (If so, please attach)",
        "plain": "Do you have a written security policy?",
        "coverage": "Full",
        "proposed": f"Yes. Millie maintains a consolidated policy suite including {P['01a']}, {P['01c']}, {P['01d']}, {P['03a']}, {P['04a']}, {P['05a']}, {P['06a']}, {P['06b']}, {P['02c']}, {P['02b']}, {P['04b']}, plus the {P['04c']} and {P['04d']}.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 5. Roles documented in writing and communicated
    {
        "section": "Roles & Responsibilities",
        "item": "5",
        "question": "11) Are information security roles & responsibilities documented in writing and communicated throughout the organization?",
        "plain": "Is it written down who's responsible for security, and does everyone know who that is?",
        "coverage": "Full",
        "proposed": f"Yes. Workforce training identifies the Chief Privacy Officer and Chief Security Officer; {P['01c']} and {P['05a']} explicitly assign responsibilities to those roles plus the Risk Review Committee. {P['01b']} defines the Risk Management Team membership.",
        "flag": "Low",
        "gap": "Job descriptions weren't reviewed; only assert role responsibilities, not that they live in JDs (unless HR confirms).",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Optional: Security & Privacy Roles / RACI addendum referencing HR job descriptions.",
    },
    # 6. Legal & regulatory requirements
    {
        "section": "Legal & Regulatory",
        "item": "6",
        "question": "12) Are legal and regulatory requirements regarding securing information, including privacy and civil liberties obligations, understood and managed?",
        "plain": "Do you follow HIPAA and other healthcare privacy laws?",
        "coverage": "Full",
        "proposed": f"Yes. The HIPAA policy suite addresses Privacy Rule (use & disclosure, patient rights, marketing, accounting), Breach Notification, Minimum Necessary, De-Identification, Definitions, and Safeguards. Citations: {P['02c']}, {P['02b']}, §II of {P['05a']}, {P['01b']}, {P['01d']}.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 7. Vulnerability scans + ERA
    {
        "section": "Risk Management",
        "item": "7",
        "question": "Are you identifying risks to your IT Infrastructure by conducting vulnerability scans and an Enterprise Risk Assessment?",
        "plain": "Are you regularly scanning for security weaknesses and assessing risks?",
        "coverage": "Full",
        "proposed": f"Yes. Millie is continuously monitored via ConnectSecure (Tenisi-owned tenant) with scans twice monthly — once after Patch Tuesday and once two weeks later to verify remediations. The {P['01c']} requires annual enterprise risk assessment; the latest annual risk letter is in {P['ss_risk']}.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 8. Date of last risk assessment
    {
        "section": "Risk Management",
        "item": "8",
        "question": "What was the date of your last Risk Assessment?",
        "plain": "When was your last security risk review?",
        "coverage": "Full",
        "proposed": f"The most recent vulnerability scan was performed on 4/30/2026 (Tenisi/ConnectSecure). The most recent annual risk letter is filed in {P['ss_risk']}.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 9. Threats internal/external documented
    {
        "section": "Risk Management",
        "item": "9",
        "question": "Are threats, both internal and external, identified and documented in the risk assessment?",
        "plain": "Does your risk review list out specific threats — both people inside the company and outsiders?",
        "coverage": "Partial",
        "proposed": f"The {P['01c']} §III requires threat identification (Human-Intentional, Human-Unintentional, Environment-Natural, Environment-Man Made), vulnerability identification, control analysis, likelihood, impact, and risk determination. Threat-register evidence is in {P['ss_risk']}.",
        "flag": "Medium",
        "gap": "Confirm current risk assessment / threat register attaches all four threat categories with named threats.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Attach current threat register showing internal/external threats by category, vulnerabilities, controls, likelihood, impact, residual risk, owner.",
    },
    # 10. Who performs risk analysis
    {
        "section": "Risk Management",
        "item": "10",
        "question": "Who is responsible for performing the risk analysis?",
        "plain": "Who actually does the risk review?",
        "coverage": "Full",
        "proposed": f"The Risk Review Committee (Chief Privacy Officer, Chief Security Officer, subject-matter experts), per {P['01c']} §III. {P['01b']} also defines the Risk Management Team (compliance, security, privacy, HR/facilities, technology SMEs). Tenisitech owns the ConnectSecure tenant and performs the vulnerability-scan portion.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 11. Risk tolerance / acceptance authority
    {
        "section": "Risk Management",
        "item": "11",
        "question": "Is there a policy defining organizational risk tolerance and risk acceptance authority?",
        "plain": "Do you have a written rule about who decides which risks are acceptable to live with?",
        "coverage": "Partial",
        "proposed": f"The {P['01c']} requires reporting risk-assessment results to the Risk Review Committee and (for material risks) the Board or designated committee, but does not define explicit risk-tolerance thresholds or formal acceptance authority.",
        "flag": "Medium",
        "gap": "No explicit Risk Acceptance / Risk Tolerance policy.",
        "fix_file": P["01c"],
        "fix_text": "Append 1-paragraph clause to Risk Management Policy: Risk acceptance authority is held by the Chief Security Officer for operational risks; material risks must be accepted in writing by the Chief Executive Officer with Board notification. Acceptance is documented in the risk register with rationale, compensating controls, and review cadence.",
    },
    # 12. Facility security plan
    {
        "section": "Physical Security",
        "item": "12",
        "question": "Is there a facility security plan that manages and protects all assets?",
        "plain": "Do you have a written plan for keeping the clinic building physically secure?",
        "coverage": "Full",
        "proposed": f"Yes. {P['01d']} §III covers Facility Access Controls and physical safeguards; {P['04b']} covers paper-PHI handling and secure storage.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 13. Remote access control
    {
        "section": "Access Control",
        "item": "13",
        "question": "How do you control remote access to your network?",
        "plain": "How do you let people log in safely from outside the clinic?",
        "coverage": "Full",
        "proposed": f"There is currently no remote access via VPN services. Tenisitech uses NinjaOne RMM to remotely access devices as needed for troubleshooting. The {P['03a']} §III (Remote Access) defines requirements where remote access is used (authorization, encryption, no-local-PHI, monitoring, termination of privileges).",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 14. Least privilege / separation of duties
    {
        "section": "Access Control",
        "item": "14",
        "question": "Are access permissions managed, incorporating the principles of least privilege and separation of duties?",
        "plain": "Do people only get access to what they need for their job?",
        "coverage": "Full",
        "proposed": f"Yes. Millie's internal admin dashboard enforces RBAC based on role; AWS, Aptible, and GitHub use RBAC and are limited to the technical team. Supported by §II of {P['02c']} (Minimum Necessary Rule) and {P['01d']} (unique user IDs by job responsibility).",
        "flag": "Low",
        "gap": "Could strengthen with screenshots / admin RBAC role matrix.",
        "fix_file": "N/A — supporting doc (optional)",
        "fix_text": "Optional: Admin RBAC role matrix screenshot.",
    },
    # 15. Network segmentation
    {
        "section": "Network Security",
        "item": "15",
        "question": "Do you segment your network into protected/isolated networks?",
        "plain": "Are your patient-data systems on a separate network from general office WiFi?",
        "coverage": "Full",
        "proposed": "There is no physical server infrastructure (cloud-only). LAN is separate from production. Wireless is split into guest and production networks. Tenisi-owned operational control.",
        "flag": "Low",
        "gap": "No standalone Network Segmentation diagram on file.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Optional: Network Segmentation / Architecture Statement (1 page summary + simple diagram).",
    },
    # 16. Training tracking
    {
        "section": "Training",
        "item": "16",
        "question": "Do you track and measure user training completion?",
        "plain": "Do you keep records of who finished the security training?",
        "coverage": "Partial",
        "proposed": "The Privacy & Security Training (March 2025) document requires every employee to complete training and includes an acknowledgment. A formal completion tracker / LMS export / measurement (test) is not currently on file.",
        "flag": "Medium",
        "gap": "Need evidence that completion is tracked and measured.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Create Training Completion Tracking SOP + roster/export (assignment, completion, reminders, acknowledgement retention).",
    },
    # 17. Vendor management program
    {
        "section": "Vendor Management",
        "item": "17",
        "question": "Do you have a formal vendor management program that requires a minimum level of HIPAA compliance based on risk?",
        "plain": "Do you have a real process for checking vendors' security before working with them?",
        "coverage": "Partial",
        "proposed": f"The {P['06a']} requires BAAs before any vendor handles PHI, and the {P['ss_mat']} identifies vendor admins and BAA status. A formal risk-tiered vendor management program (security questionnaire, scoring, periodic reassessment) is not yet documented.",
        "flag": "Medium",
        "gap": "BAA process exists; vendor security questionnaire/risk tiering evidence not formalized.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Create Vendor Risk Management Program SOP (vendor inventory, risk tier, HIPAA/security questionnaire, BAA review, approval workflow, periodic reassessment) + evidence folder.",
    },
    # 18. Technical controls for stored data
    {
        "section": "Data Protection",
        "item": "18",
        "question": "What technical controls are being used to protect data stored on electronic storage media?",
        "plain": "How is patient data protected on hard drives, databases, and storage?",
        "coverage": "Full",
        "proposed": f"Password protection, unique user IDs, 2FA where possible, approved password manager usage, device encryption for any device touching PHI, prohibitions on local PHI storage, and encryption for ePHI over open networks (per §I/§II/§III/§IV of {P['03a']}). Aptible-managed databases are encrypted at rest (https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-encryption/overview).",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 19. Physical security controls
    {
        "section": "Physical Security",
        "item": "19",
        "question": "What physical security controls are in place to protect data?",
        "plain": "What physical things (locks, cabinets, etc.) protect patient data at the clinic?",
        "coverage": "Full",
        "proposed": f"Per {P['01d']} (Safeguards Policy) §III and {P['04b']} (Paper Document Management), Millie uses locked storage for paper PHI, restricted-access work areas, visitor controls, and workstation locking. §IV of {P['03a']} (Workstation Use) requires session locking and prohibits local PHI storage.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 20. Data in transit
    {
        "section": "Data Protection",
        "item": "20",
        "question": "How is data protected when it is in transit to external organizations?",
        "plain": "How is patient data kept safe when emailed or sent to others?",
        "coverage": "Full",
        "proposed": f"ePHI must be encrypted before email or transmission over open networks (§I of {P['03a']} — Encryption, requiring FIPS 140-2 / NIST SP 800-52/77/113 standards). The Remote Access section (§III of {P['03a']}) prohibits transmitting PHI over unencrypted channels.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 21. Asset lifecycle management
    {
        "section": "Asset Management",
        "item": "21",
        "question": "Are assets formally managed throughout the life cycle (acquisition, movement, transfers, disposal)?",
        "plain": "Is there a documented process for buying, moving, and getting rid of computers and equipment?",
        "coverage": "Full",
        "proposed": f"{P['04a']} requires maintaining and updating an IT inventory and prohibits purchasing IT components without Chief Security Officer approval; §III of {P['03a']} (Remote Access) requires tracking removed Company equipment; §IV (Workstation Use) and {P['04b']} address secure storage and disposal. {P['06b']} (SDLC) covers asset-lifecycle handling for software/systems.",
        "flag": "Low",
        "gap": "Hardware lifecycle for Tenisi-managed devices isn't end-to-end documented in Millie's policies.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Optional: Asset Lifecycle SOP / Tenisi hardware inventory export.",
    },
    # 22. Data leak monitoring
    {
        "section": "Network Security",
        "item": "22",
        "question": "How are you monitoring your networks for data leaks?",
        "plain": "How do you watch for someone leaking data out of the company?",
        "coverage": "Full",
        "proposed": "Audit logging across the data stack: Fivetran (connector / sync activity), Databricks (logins, data access, queries), Hex (workspace actions/access), Aptible (workspace actions, database access), AWS (CloudTrail + CloudWatch for app activity). User Notifications in AWS alert on sign-in anomalies and root-user logins. Anomalous-access investigations are documented in incident logs per §I of 05a (Incident & Breach Response).",
        "flag": "Low",
        "gap": "No standalone DLP/log-monitoring statement; reliance on multiple per-platform audit logs.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Optional: Data Leak Monitoring / DLP Statement (1 page) summarizing per-platform audit logging, review cadence, and escalation.",
    },
    # 23. Baseline configuration
    {
        "section": "Configuration Management",
        "item": "23",
        "question": "Is a baseline configuration of IT systems created and maintained?",
        "plain": "Do you have a standard setup that every computer/server starts from?",
        "coverage": "Full",
        "proposed": "Devices enrolled in NinjaOne (Tenisi RMM) receive patch-management schedules along with baseline security tools, vulnerability-scanning agent (ConnectSecure), and policy management. §IV of 03a (Workstation Use) defines baseline expectations.",
        "flag": "Low",
        "gap": "No documented Secure Configuration Baseline Standard outside Tenisi's NinjaOne configuration.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Optional: Secure Configuration Baseline Standard (endpoint / server / cloud / network baseline controls, owner, review cadence, exceptions).",
    },
    # 24. SDLC for assets and hardware
    {
        "section": "Configuration Management",
        "item": "24",
        "question": "Is a System Development Life Cycle (SDLC) implemented for all asset and hardware configurations?",
        "plain": "Is there a documented step-by-step lifecycle (plan, build, test, deploy, retire) for systems?",
        "coverage": "Full",
        "proposed": f"Yes. {P['06b']} (SDLC & Asset Lifecycle Policy) defines the lifecycle for systems and software (planning, requirements, design, testing, implementation, operations/maintenance, retirement). AGENTS.md adds engineering change discipline, testing, approvals.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 25. Configuration change control
    {
        "section": "Configuration Management",
        "item": "25",
        "question": "Are configuration change control processes in place?",
        "plain": "Is there a real process to track, review, and approve changes to systems?",
        "coverage": "Partial",
        "proposed": f"{P['06b']} §III(c) covers pre-deploy validation and approval gates; engineering changes use GitHub PR review + Aptible deploy logs. A discretely-named Change Management policy/log with classification (standard / normal / emergency) is not yet on file.",
        "flag": "Medium",
        "gap": "Need formal Change Management Policy with change-log template.",
        "fix_file": P["06b"],
        "fix_text": "Append 1-paragraph Change Management section to SDLC Policy: Changes to production systems require peer review and approval through GitHub pull-request + Aptible deploy pipeline. Chief Security Officer owns the change-control process; reviewed annually. Production-change records are retained via Git history and Aptible deploy logs.",
    },
    # 26. Backups
    {
        "section": "Business Continuity",
        "item": "26",
        "question": "Are backups of information and server/laptop configurations created, maintained, and tested periodically?",
        "plain": "Do you back up patient data and computer settings, and do you test the backups?",
        "coverage": "Full",
        "proposed": f"Yes for data and software. {P['04a']} requires backup of all data on the IT System every 24 hours, encrypted off-site storage, quarterly review of backup procedures, and DR drills/tests. The May 2026 DR review is in {P['ss_dr']}. No backup software is in place for laptops; no on-prem server infrastructure exists (SaaS only).",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 27. Disposal policy (data + hardware)
    {
        "section": "Asset Management",
        "item": "27",
        "question": "Is there a disposal policy that addresses both data and hardware?",
        "plain": "Is there a written rule for how to safely throw away patient data and old computers?",
        "coverage": "Full",
        "proposed": f"Yes. {P['01d']} requires PHI disposal in a manner that renders it unreadable/unusable, paper shredding, media sanitization before reuse, and ePHI deletion when no longer needed. {P['04b']} requires shredding of protected documents and vendor certificates of destruction.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 28. BCP/DR plans
    {
        "section": "Business Continuity",
        "item": "28",
        "question": "Are Business Continuity plans and Disaster Recovery plans in place and managed?",
        "plain": "Do you have a written plan for keeping the clinic running after a disaster?",
        "coverage": "Full",
        "proposed": f"Yes. {P['04a']} establishes continuity/disaster response, data and software backup, IT inventory, UPS/power protections, DR plan preparation/approval, critical-provider business-continuity clauses, emergency operations, drills/testing, updates, confidentiality, and insurance considerations. The May 2026 DR review (in {P['ss_dr']}) is the latest evidence.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 29. Background checks + exit interviews
    {
        "section": "HR Security",
        "item": "29",
        "question": "Do you conduct background checks on all members of the workforce, and exit interviews to cover HIPAA obligations after employment?",
        "plain": "Do you check new hires' backgrounds and remind them about confidentiality when they leave?",
        "coverage": "Partial",
        "proposed": "Background checks and exit interviews are HR-managed via Gusto. No formal Millie-side policy / HR attestation documenting that HIPAA-confidentiality reminders are part of the exit process.",
        "flag": "Medium",
        "gap": "HR-owned process not formally documented as a security policy.",
        "fix_file": "N/A — supporting doc (HR-owned)",
        "fix_text": "HR to add: background-check scope and timing, exit checklist including HIPAA confidentiality reminder, access handoff to IT. Capture as HR SOP or 1-paragraph attestation.",
    },
    # 30. Provisioning / deprovisioning of accounts + physical access
    {
        "section": "Access Control",
        "item": "30",
        "question": "Is there a formal process for provisioning and removal of all user accounts, and physical access?",
        "plain": "Is there a documented process for creating and removing user accounts and building access?",
        "coverage": "Partial",
        "proposed": f"§II/§III of {P['03a']} (Password / Remote Access) requires deactivation of passwords and remote access on termination or role change. {P['ss_mat']} captures per-platform admins. A formal cross-system access provisioning/deprovisioning SOP covering all user accounts AND physical access is not yet on file.",
        "flag": "Medium",
        "gap": "Need formal user lifecycle / access request workflow.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Create Access Provisioning & Deprovisioning SOP (request, approval, role mapping, least privilege, provisioning, periodic review, termination/offboarding SLAs, physical access).",
    },
    # 31. Removable media restrictions
    {
        "section": "Data Protection",
        "item": "31",
        "question": "Do you restrict the use of removable media (USB drives) and limit access to only authorized users?",
        "plain": "Are USB sticks and external drives controlled and limited to approved people?",
        "coverage": "Full",
        "proposed": f"Yes. §IV of {P['03a']} (Workstation Use) requires work files to be stored on the external hosting platform or app — not on C drive, CD, thumb drive, or directly on mobile devices unless authorized. §III (Remote Access) prohibits storing PHI on hard drives. {P['01d']} requires ePHI removal from media before reuse.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 32. Data flow mapping
    {
        "section": "Data Mapping",
        "item": "32",
        "question": "Have you mapped all internal and external data flows?",
        "plain": "Do you know exactly where patient data lives and who you share it with?",
        "coverage": "Partial",
        "proposed": f"AGENTS.md describes major systems and workflows (Acuity, EMR/Elation, Zendesk, Zentake, Withings, Customer.io, Twilio/SendGrid, AWS/Aptible). The {P['ss_mat']} identifies systems and access. No complete internal/external sensitive-data-flow map with PHI categories, sources, destinations, vendors, and owners.",
        "flag": "Medium",
        "gap": "No explicit data-flow map / data inventory document.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Create Internal/External Data Flow Map and Data Inventory (system inventory, PHI categories, source/destination, transfers, vendors, storage locations, encryption, owner, retention, BAAs).",
    },
    # 33. Incident review for impact
    {
        "section": "Incident Response",
        "item": "33",
        "question": "Are security/privacy incidents reviewed for impact?",
        "plain": "After a security event, do you review what happened and what damage was done?",
        "coverage": "Full",
        "proposed": f"Yes. §I of {P['05a']} (Security Incident Management) requires prompt reporting, CSO investigation within 24 hours, response priorities, incident logs, post-incident analysis, and annual reporting. §II (Breach Notification) requires investigation, PHI compromise assessment, risk assessment, notifications, mitigation, sanctions, and accounting of disclosures.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 34. Incident management policy with criticality/decision authority
    {
        "section": "Incident Response",
        "item": "34",
        "question": "Do you have an incident management policy that defines criticality and decision response authority?",
        "plain": "Do you have a written policy that says how serious each incident is and who decides what to do?",
        "coverage": "Full",
        "proposed": f"Yes. §I of {P['05a']} assigns incident response authority to the Chief Security Officer, Chief Compliance Officer, Chief Privacy Officer, General Counsel/CLO, and CEO depending on incident actions. §II identifies the Chief Privacy Officer as responsible for breach investigation/notification decisions with Security Officer involvement.",
        "flag": "Low",
        "gap": "Severity-tier categories aren't explicit in the policy.",
        "fix_file": "N/A — supporting doc (optional)",
        "fix_text": "Optional: Incident Severity & Escalation Matrix referenced from the Incident & Breach Response Policy.",
    },
    # 35. Network monitoring
    {
        "section": "Network Security",
        "item": "35",
        "question": "Is the network monitored to detect potential cybersecurity events?",
        "plain": "Are you watching your network for hackers and unusual activity?",
        "coverage": "Partial",
        "proposed": f"§III of {P['03a']} (Remote Access) mentions maintaining/reviewing records of inbound remote access. AWS GuardDuty and User Notifications alert on sign-in anomalies. No formal IDS/IPS / SIEM / firewall-alerting documentation outside Tenisi's NinjaOne agent.",
        "flag": "Medium",
        "gap": "No standalone Network Security Monitoring statement; relies on Tenisi-managed agents + per-platform alerts.",
        "fix_file": "N/A — supporting doc",
        "fix_text": "Create Network Security Monitoring / IDS-IPS Statement (coverage, Tenisi alerting, review cadence, escalation, sample alert evidence).",
    },
    # 36. Physical environment monitoring
    {
        "section": "Physical Security",
        "item": "36",
        "question": "Is the physical environment monitored to detect potential security events? (cameras, security guards, badge readers)",
        "plain": "Do you have cameras or badge readers watching the clinic for break-ins?",
        "coverage": "Partial",
        "proposed": f"{P['01d']} includes visitor controls, IDs, and secure storage. Cameras / guards / badge readers / equivalent active physical-environment monitoring per-site is not documented in policy.",
        "flag": "Medium",
        "gap": "Site-by-site physical monitoring details not documented.",
        "fix_file": "N/A — supporting doc (per-site)",
        "fix_text": "Create per-site Physical Security Monitoring Statement (locks, cameras, badge/access controls, visitor logs, restricted areas, responsible owner, exceptions).",
    },
    # 37. Incident response policy w/ root cause analysis
    {
        "section": "Incident Response",
        "item": "37",
        "question": "Do you have a security/privacy incident response policy that identifies key personnel and requires root cause analysis?",
        "plain": "Do you have a written incident response policy that requires figuring out the root cause?",
        "coverage": "Full",
        "proposed": f"Yes. §I of {P['05a']} identifies key personnel, reporting, investigation, response priorities, incident logs, and post-incident analysis (vulnerabilities exploited, how the incident occurred, resolution/containment, policy adequacy, unresolved vulnerabilities, needed updates). §II covers breach determination and risk assessment.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 38. DR testing
    {
        "section": "Business Continuity",
        "item": "38",
        "question": "Do you test your down time procedures and your disaster recovery plans?",
        "plain": "Do you actually practice your disaster recovery plan?",
        "coverage": "Full",
        "proposed": f"Yes. {P['04a']} requires the Chief Security Officer to conduct drills and exercises with personnel to test and evaluate DR plans, and submit written summaries to the CEO. The May 2026 DR review in {P['ss_dr']} is the latest test evidence.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
    # 39. Lessons learned
    {
        "section": "Business Continuity",
        "item": "39",
        "question": "Do you incorporate lessons learned into the disaster recovery planning process?",
        "plain": "After a disaster drill, do you update your plan based on what you learned?",
        "coverage": "Full",
        "proposed": f"Yes. {P['04a']} states that DR plans and emergency protocols must be revised to remedy deficiencies identified during drills, or to reflect material changes in operations, systems, personnel, contractors, and business arrangements.",
        "flag": "Low",
        "gap": "—",
        "fix_file": "N/A",
        "fix_text": "",
    },
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    csv_path = OUT / "coverage_matrix_UCSF.csv"
    header = [
        "Questionnaire",
        "Section",
        "Item #",
        "Question",
        "Plain English",
        "Coverage",
        "Proposed Answer",
        "Flag Risk",
        "Gap Description",
        "Required Fix - File",
        "Required Fix - Text",
        "Required Fix - Words",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        for r in ROWS:
            fix_words = len(r["fix_text"].split()) if r["fix_text"] else 0
            w.writerow([
                "UCSF Security Review",
                r["section"],
                r["item"],
                r["question"],
                r["plain"],
                r["coverage"],
                r["proposed"],
                r["flag"],
                r["gap"],
                r["fix_file"],
                r["fix_text"],
                fix_words,
            ])
    print(f"Wrote {csv_path.relative_to(REPO)} ({len(ROWS)} rows)")

    # --- SUMMARY_UCSF.md ---
    from collections import Counter
    cov = Counter(r["coverage"] for r in ROWS)
    flag = Counter(r["flag"] for r in ROWS)
    sec = Counter(r["section"] for r in ROWS)
    total_fix_words = sum(len(r["fix_text"].split()) for r in ROWS if r["fix_text"])
    files_needing_changes = sorted(
        {r["fix_file"] for r in ROWS if r["fix_file"] and not r["fix_file"].startswith("N/A")}
    )

    summary = OUT / "SUMMARY_UCSF.md"
    lines = [
        "# UCSF Security Review — Coverage Summary",
        "",
        f"Analyzed all **{len(ROWS)} questions** from `UCSF Docs/UCSF Security Review Questions.xlsx` against the current consolidated policy set in `Current Policies (… Generated)/3.a Final Markdown/` and the evidence files in `Supporting Sources/`.",
        "",
        "## Coverage counts",
        "",
        "| Coverage | Count |",
        "|---|---|",
    ]
    for k in ("Full", "Partial", "None", "N/A", "Evidence-only"):
        lines.append(f"| {k} | {cov.get(k, 0)} |")
    lines += [
        "",
        "## Flag Risk counts (if submitted as-is)",
        "",
        "| Flag Risk | Count |",
        "|---|---|",
    ]
    for k in ("High", "Medium", "Low", "None"):
        lines.append(f"| {k} | {flag.get(k, 0)} |")
    lines += [
        "",
        "## Per-section breakdown",
        "",
        "| Section | Questions |",
        "|---|---|",
    ]
    for s, n in sorted(sec.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {s} | {n} |")
    lines += [
        "",
        "## Remediation effort",
        "",
        f"- **Total `Required Fix - Text` word count across all rows:** {total_fix_words}",
        f"- **Policy files needing additions** ({len(files_needing_changes)}):",
    ]
    for f_ in files_needing_changes:
        lines.append(f"  - `{f_}`")
    lines += [
        "",
        "Everything else is either Full (policy answers it) or needs a **supporting doc** (HR / Tenisi / operational SOP), not a policy edit. See `SUPPORTING-DOCS-NEEDED.md` for the consolidated evidence checklist.",
        "",
        "The per-row analysis is in `coverage_matrix_UCSF.csv` (renders to `coverage_matrix_UCSF.xlsx` after the build).",
    ]
    summary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {summary.relative_to(REPO)}")

    # --- GAPS_UCSF.md ---
    gaps = [r for r in ROWS if r["coverage"] in ("Partial", "None") or r["flag"] in ("High", "Medium")]
    gaps_path = OUT / "GAPS_UCSF.md"
    g = [
        "# UCSF Security Review — Actionable Gaps",
        "",
        f"Subset of `coverage_matrix_UCSF.csv` showing the {len(gaps)} rows that are either **Partial / None** coverage or **High / Medium** flag risk. Each is either fixable with a short policy clause OR requires a supporting document to be created (HR / Tenisi / operational SOP).",
        "",
    ]
    # Group by whether fix is a policy edit or a supporting doc
    policy_edits = [r for r in gaps if r["fix_file"] and not r["fix_file"].startswith("N/A")]
    supporting_needed = [r for r in gaps if r["fix_file"].startswith("N/A — supporting doc")]
    other = [r for r in gaps if r not in policy_edits and r not in supporting_needed]

    g.append(f"## Policy edits needed ({len(policy_edits)})")
    g.append("")
    g.append("| # | Section | Question | Fix file | Fix text (excerpt) |")
    g.append("|---|---|---|---|---|")
    for r in policy_edits:
        excerpt = r["fix_text"][:160] + ("…" if len(r["fix_text"]) > 160 else "")
        g.append(f"| {r['item']} | {r['section']} | {r['question'][:80]}… | `{r['fix_file']}` | {excerpt} |")
    g.append("")

    g.append(f"## Supporting docs needed ({len(supporting_needed)})")
    g.append("")
    g.append("| # | Section | Question | Doc to create |")
    g.append("|---|---|---|---|")
    for r in supporting_needed:
        excerpt = r["fix_text"][:160] + ("…" if len(r["fix_text"]) > 160 else "")
        g.append(f"| {r['item']} | {r['section']} | {r['question'][:80]}… | {excerpt} |")
    g.append("")

    if other:
        g.append(f"## Other ({len(other)})")
        g.append("")
        for r in other:
            g.append(f"- **Item {r['item']}** ({r['section']}): {r['gap']}")
        g.append("")

    gaps_path.write_text("\n".join(g) + "\n", encoding="utf-8")
    print(f"Wrote {gaps_path.relative_to(REPO)} ({len(gaps)} actionable rows)")


if __name__ == "__main__":
    main()
