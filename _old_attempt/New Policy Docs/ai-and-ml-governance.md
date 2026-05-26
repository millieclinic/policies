---
title: "AI and Machine Learning Governance"
sources: []
supersedes: []
last_reviewed: 2026-05-24
owner: "Security Officer (CTO co-owner for engineering AI; Privacy Officer co-owner for clinical AI)"
status: "active"
---

# AI and Machine Learning Governance

> **New policy authored 2026-05-24** to close gaps in SIG Lite 2025 §R (Artificial Intelligence) surfaced by the ECH Security Assessment. This is a minimum-viable AI policy — expect expansion as Millie's AI use matures and regulatory guidance (e.g., HHS AI rules, state AI transparency laws) evolves.

## I. Scope

This Policy applies to all Company personnel using or evaluating any artificial intelligence, machine learning, or large language model service or model in connection with Company work — whether the AI is built by Millie, embedded in a third-party product, or accessed directly as a consumer or enterprise tool.

## II. Policy

Millie permits AI use that is approved, inventoried, and reviewed. AI tools are treated the same as any other vendor for BAA, security review, and procurement purposes — there is no exemption simply because a tool is "AI." Personnel may not submit PHI, PII, or confidential Company information to any AI tool that has not been approved for that data class. Clinical AI never replaces clinician judgment; it provides decision support that a licensed clinician must review and accept or reject. The Company maintains an inventory of every AI tool in use and reviews that inventory on a defined cadence. Personnel who violate this Policy are subject to sanctions, and any incident involving AI exposure of PHI triggers a breach assessment. Practical guardrails take priority over exhaustive framework compliance at Millie's current scale.

## III. Procedure

### a. AI Tool Approval and Inventory

- The authoritative list of approved AI tools lives in [platform-and-access-matrix.md](platform-and-access-matrix.md). Current approved tools include Heidi (ambient charting), OpenEvidence (clinical decision support), and the enterprise AI platforms listed under "AI Platforms" (OpenAI, Anthropic, Google Vertex, Agno). The matrix is the single source of truth — this Policy does not duplicate it.
- New AI tools — including free tools, browser extensions, mobile apps, and AI features embedded in existing platforms — require Security Officer approval **plus** a clinical or operational stakeholder approval before any use with Company data. Approval criteria:
  - **Data handling:** Does the vendor train on customer data? Where is it stored? What is the retention period? Can data be deleted on request?
  - **BAA availability** if PHI may be touched. A BAA must be executed before any PHI is submitted.
  - **Security posture:** SOC 2 Type II, HITRUST, or equivalent; encryption in transit and at rest.
  - **Clinical validation** if used in any clinical workflow (see §III(c)).
- "Trial," "pilot," and "proof of concept" use are not exempt.

### b. Use of Public AI and LLM Services

**Prohibited.** Personnel shall not submit PHI, PII, or confidential Company information to public consumer LLM services (e.g., ChatGPT consumer, Claude.ai consumer tier, Gemini consumer, Microsoft Copilot consumer) unless the specific service is listed on the approved tool list in [platform-and-access-matrix.md](platform-and-access-matrix.md) with appropriate contractual protections — at minimum, an enterprise tier with a no-training agreement, and a BAA where PHI is involved.

**Permitted.** The following uses do not require pre-approval, regardless of which LLM is used:

- De-identified data per [phi-use-and-disclosure.md](phi-use-and-disclosure.md) (Safe Harbor or Expert Determination) or fully synthetic data.
- General business research, brainstorming, drafting of non-confidential text.
- Code assistance on repositories that do not contain PHI, secrets, or confidential business logic, with output subject to standard code review per [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md).
- Summarization of public documents (papers, regulations, vendor documentation).

**Approved enterprise variants.** Where the Company has procured an enterprise tier of a public LLM (e.g., ChatGPT Enterprise or Claude for Work with a no-training agreement and, where applicable, a BAA), the tool must:

- Be listed in [platform-and-access-matrix.md](platform-and-access-matrix.md).
- Be accessed through Company SSO using a Company identity — not a personal account.
- Be used only for the data classes permitted by its contract.

### c. Clinical and Medical AI

- Any AI tool used in patient care must undergo a documented clinical-validation review by a licensed clinician (or clinical leadership delegate) before deployment. The review covers intended use, known limitations, training-data provenance where available, and any clinically meaningful failure modes.
- AI output is **decision support, not autonomous decision-making.** A licensed clinician must review every AI-generated recommendation, draft note, or summary and explicitly accept, edit, or reject it before it becomes part of the medical record or affects a care decision.
- Patient consent for ambient AI scribes (e.g., Heidi) is obtained per applicable state law. Consent language and intake handling are covered in [phi-use-and-disclosure.md](phi-use-and-disclosure.md) §Marketing & Patient Communications and at patient intake.
- Errors, hallucinations, or anomalous outputs from clinical AI that affect or could affect patient care must be reported to the Privacy Officer and logged. Patterns of error trigger a re-validation review.

### d. AI in Engineering and Software Development

- Code-completion and code-generation AI (e.g., GitHub Copilot, Cursor, Claude Code) is permitted with all of the following: a business-tier license, an IP-indemnification clause from the vendor, a contractual no-training agreement covering Company code, and default scoping to repositories that do not contain PHI.
- All AI-generated code must pass standard code review per [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md). The reviewing engineer — not the AI — is accountable for what merges.
- AI-generated test data and fixtures must not contain real PHI. Use synthetic data or properly de-identified samples per [phi-use-and-disclosure.md](phi-use-and-disclosure.md).
- AI agents that take autonomous actions in Company systems (e.g., merging code, sending email, modifying production data) require Security Officer + CTO approval and must operate under a scoped, auditable service identity — never a human user's credentials.

### e. AI Inventory and Periodic Review

- **Inventory.** Every AI tool, model, or service used with Company data must be listed in [platform-and-access-matrix.md](platform-and-access-matrix.md) with, at minimum: name, vendor, purpose, data sensitivity (None / PII / PHI / Confidential), BAA status, and last review date.
- **Review cadence.**
  - **Quarterly:** Security Officer and CTO review the AI inventory — confirm each tool is still in use, owner is current, BAA is still in force, and no new sub-processors have been added without notice.
  - **Annually:** deeper review including, for clinical AI, a bias and fairness assessment appropriate to the tool's clinical context and patient population. Tools no longer in use are retired and access is removed.
- **Reporting.** Material findings from quarterly and annual reviews are reported to the Risk Review Committee described in [governance-and-risk-management.md](governance-and-risk-management.md) and incorporated into the Company's risk register.

### f. Prohibited AI Uses

- Autonomous medical diagnosis or treatment decisions without clinician review and acceptance.
- Submitting raw PHI to unapproved or consumer-tier AI services.
- Using AI to generate patient communications (clinical or marketing) without human review and explicit approval, per [phi-use-and-disclosure.md](phi-use-and-disclosure.md) §Marketing & Patient Communications.
- Using AI to evaluate, rank, or take adverse action against employees in a manner that constitutes automated decision-making under applicable employment law, without HR and Legal review.
- Generating fake, misleading, or impersonating content — including deepfake audio/video of patients, clinicians, or staff; fabricated clinical documentation; or forged signatures or credentials.

### g. Patient Transparency

- When AI materially affects patient care — for example, an AI-generated note that, after clinician review, becomes part of the medical record — patients have the right to know AI was involved, consistent with applicable state AI transparency requirements.
- Specific patient-facing transparency language (including Notice of Privacy Practices disclosures and consent prompts) is maintained in [patient-rights.md](patient-rights.md) so that patient-facing wording lives in one place.

### h. Incident Response for AI

- AI-related security or privacy incidents — e.g., PHI inadvertently submitted to a public LLM, exposure through an AI vendor breach, prompt-injection compromising a Company AI agent, or clinical AI output contributing to patient harm — follow [incident-and-breach-response.md](incident-and-breach-response.md).
- Specific AI incident triage criteria (severity thresholds, containment for agentic systems, vendor-side breach handling) will be developed as Millie's AI use matures. Until then, the general incident response process governs.

## IV. Training & Awareness

> All personnel shall complete AI usage training at the time of employment or engagement and before being granted access to any AI tool that handles Company data, with annual updates thereafter, in accordance with the [governance-and-risk-management.md](governance-and-risk-management.md) Training Program. Engineering and clinical personnel receive role-specific AI training.

## V. Sanctions

> Any personnel member who violates this Policy — including submitting PHI to unapproved AI services, deploying clinical AI without validation, or using AI in a manner that materially misleads patients — will be subject to disciplinary action, up to and including termination of employment or engagement, in accordance with Company HR policy. AI-related exposure of PHI triggers a breach assessment under [incident-and-breach-response.md](incident-and-breach-response.md). Sanctions are documented and tracked by the Privacy Officer.

## VI. References

- Shared Assessments SIG Lite 2025, §R (Artificial Intelligence) — R.1, R.2, R.4, R.5.
- NIST AI Risk Management Framework (AI RMF 1.0), January 2023.
- 45 CFR §164.502(b) — Minimum Necessary standard; applies to data submitted as input to AI tools.
- 45 CFR §164.514 — De-identification and Limited Data Sets.
- HHS Office for Civil Rights guidance on AI and HIPAA (as published).
- [platform-and-access-matrix.md](platform-and-access-matrix.md) — authoritative AI tool inventory.
- [phi-use-and-disclosure.md](phi-use-and-disclosure.md) — de-identification, marketing & patient communications.
- [sdlc-and-asset-lifecycle.md](sdlc-and-asset-lifecycle.md) — code review for AI-assisted development.
- [incident-and-breach-response.md](incident-and-breach-response.md) — incident handling, including AI incidents.
- [governance-and-risk-management.md](governance-and-risk-management.md) — training program and Risk Review Committee.
- [patient-rights.md](patient-rights.md) — patient-facing transparency language.
- [hipaa-definitions.md](hipaa-definitions.md) — shared definitions.

## VII. Definitions used in this Policy

General HIPAA and security terms used here (PHI, PII, Breach, Workforce, Business Associate, etc.) are defined in [hipaa-definitions.md](hipaa-definitions.md). The following terms are specific to this Policy:

- **Large Language Model (LLM).** A machine-learning model trained on large text corpora to produce natural-language output in response to a prompt (e.g., GPT-class, Claude-class, Gemini-class models).
- **Public AI Service.** An AI tool accessible to the general public on consumer terms — typically without an enterprise contract, no-training agreement, or BAA — regardless of whether a paid subscription is available (e.g., ChatGPT consumer, Claude.ai consumer, Gemini consumer).
- **Enterprise AI Service.** An AI tool offered under an enterprise contract that, at minimum, contains a no-training-on-customer-data commitment and, where applicable, a Business Associate Agreement.
- **Clinical AI.** Any AI tool used in connection with patient care — including but not limited to ambient scribes, clinical decision support, triage assistants, and AI features embedded in the EMR.
- **Ambient AI Scribe.** A clinical AI that listens to a patient encounter (in person or via telehealth) and generates a draft clinical note for clinician review (e.g., Heidi).
- **Generative AI.** AI that produces new content — text, code, images, audio, video — in response to a prompt, as opposed to AI that only classifies or scores existing inputs.
- **Decision Support AI.** AI that surfaces recommendations, summaries, or risk scores to a human decision-maker, who retains responsibility for the final decision.

## VIII. Revision history

| Date | Change | Author |
|---|---|---|
| 2026-05-24 | Initial draft addressing SIG R.1, R.2, R.4, R.5 | Consolidation effort |
