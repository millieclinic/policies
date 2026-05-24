# TODO — Actions before ECH submission

Tracked items surfaced by [ECH Security Assessment Questions - Questions.csv](ECH%20Security%20Assessment%20Questions%20-%20Questions.csv) and cross-referenced in [POLICY-VS-QUESTIONNAIRE-MAPPING.md §4](POLICY-VS-QUESTIONNAIRE-MAPPING.md). Owner: **Security Officer** (Chase) unless noted. Review at the start of each ECH submission cycle.

Severity: 🔴 Critical (Remediate=Yes or NO answer on Critical-severity gap) · 🟠 High (FOLLOW UP) · 🟡 Operational (judgment call, no formal flag yet).

---

## 🔴 Critical — must close before ECH submission

| # | CSV row | Item | What needs to happen | Owner | Status |
|---|---|---|---|---|---|
| 1 | 73 | **OWASP A02 — Password storage** (Remediate=Yes) | Document the password-hash algorithm in use (argon2id or bcrypt), salt strategy, iteration count, and rotation policy. Update [technical-safeguards.md](New%20Policy%20Docs/technical-safeguards.md) §Encryption. | Engineering | ⬜ |
| 2 | 77 | **OWASP A06 — Vulnerability scanning + patching** (Remediate=Yes) | Complete the GitHub plan/version upgrade. Document patch SLA (Critical=7d, High=30d) in [sdlc-and-asset-lifecycle.md](New%20Policy%20Docs/sdlc-and-asset-lifecycle.md). | Engineering | ⬜ |
| 3 | 78 | **OWASP A07 — Session & token handling** (Remediate=Yes) | Document session expiration, token rotation, refresh-token handling, logout-on-password-change. Update [technical-safeguards.md](New%20Policy%20Docs/technical-safeguards.md) §Access Control. | Engineering | ⬜ |
| 4 | 132 | **SIG M.1.3 — MDM program** (NO + FOLLOW UP) | Stand up MDM (or document why N/A and the compensating controls). Backed by new policy [acceptable-use-and-byod.md](New%20Policy%20Docs/acceptable-use-and-byod.md). | Security Officer | ⬜ |
| 5 | 133–134 | **SIG M.1.5/M.1.6 — BYOD on network with scoped data** (YES + FOLLOW UP) | Pair with #4. Publish BYOD enrollment + acceptance form. Stop allowing un-enrolled personal devices to touch PHI. | Security Officer | ⬜ |

## 🟠 High — close before submission if time, otherwise note as in-flight

| # | CSV row | Item | What needs to happen | Owner | Status |
|---|---|---|---|---|---|
| 6 | 75 | OWASP A04 — Secure SDLC with AppSec | Decide whether current SDLC answer is sufficient; expand SDLC doc with AppSec role if not. | Engineering | ⬜ |
| 7 | 80 | OWASP A09 — Logging & monitoring | Document log review cadence, alert thresholds, retention. Update [technical-safeguards.md](New%20Policy%20Docs/technical-safeguards.md) §Logging. | Engineering | ⬜ |
| 8 | 81 | OWASP A10 — SSRF defenses | Document URL allowlisting; block AWS metadata endpoint from app subnets. Update [network-and-cloud-security.md](New%20Policy%20Docs/network-and-cloud-security.md). | Engineering | ⬜ |
| 9 | 117 | SIG K.2 — DR testing program | Define annual DR test cadence; capture last test date. Update [operational-safeguards.md](New%20Policy%20Docs/operational-safeguards.md) §Contingency. | Security Officer | ⬜ |
| 10 | 119 | SIG K.4 — Pandemic plan (NO) | Add pandemic plan section to Contingency Planning (remote-work activation, supply continuity). | Security Officer | ⬜ |
| 11 | 124 | SIG K.30 — Multi-vendor resiliency (NO) | Document accepted single-vendor risk on Aptible / AWS / Cloudflare + any mitigations + exit considerations. | CTO + Security Officer | ⬜ |

## 🟡 Operational — Zoe's AWS judgment calls (review pre-submission)

These have `No` answers on the AWS questionnaire but are not formally flagged FOLLOW UP. Decide whether to remediate, accept the risk in writing, or answer as-is.

| # | CSV row | Item | Notes from Zoe | Owner |
|---|---|---|---|---|
| 12 | 11 | IAM users with console access | Currently exists; common assessor red flag. | zoe.h@millieclinic.com |
| 13 | 12, 13 | Programmatic access keys configured | Used for Aptible deploy + backend S3 writes. | zoe.h@millieclinic.com |
| 14 | 17 | IAM users/groups/roles with wildcard admin/S3/IAM | Currently exists. | zoe.h@millieclinic.com |
| 15 | 21 | Public subnet still present | "Maybe fix, but not confident how to solve if it breaks something." | zoe.h@millieclinic.com |
| 16 | 26 | AWS Config not enabled | "Might be ok to wait to see if they come back asking." | zoe.h@millieclinic.com |
| 17 | 14 | Unused access key in staging | "Will be used once SES is fully set up; verify next week." | zoe.h@millieclinic.com |
| 18 | 16 | Snowflake IAM role unused >90d | "Flush out good comment for Snowflake." | zoe.h@millieclinic.com |

## Other outstanding follow-ups (not strictly ECH-blocking)

- **Patient-facing Notice of Privacy Practices** is missing from this repo entirely. The file named `privacy-policy.md` is actually a bundle of HIPAA staff policies, not a patient notice. Draft a real NPP. Track in [PATIENT-NOTICE-TODO.md](New%20Policy%20Docs/PATIENT-NOTICE-TODO.md) (created during consolidation).
- **COVID-19 staff guidance is incomplete.** The source `Policy Docs/Millie Clinic COVID Policy.docx` has a "GUIDANCE FOR STAFF: To Do…" placeholder that was never filled in. The patient-facing protocol is fully documented and is now [operational-safeguards.md §A.9](New%20Policy%20Docs/operational-safeguards.md), but staff return-to-work clearance, sick-leave coverage, PPE issuance, and in-clinic exposure-reporting workflow need to be drafted. Owner: Practice Manager + Privacy Officer + clinical lead.
- **AWS and Aptible Security Incident Management Policy.docx** (in `Policy Docs/`, dated May 24) was not converted or integrated during the May 2026 consolidation. Review and decide whether it should be folded into [incident-and-breach-response.md](New%20Policy%20Docs/incident-and-breach-response.md) §III(3) (the AWS-specific incident playbook pointer) or [network-and-cloud-security.md](New%20Policy%20Docs/network-and-cloud-security.md) §13 (AWS-specific incident response section).
- **Out-of-scope SIG sections** to answer as "Not formally documented" or "N/A" rather than author policies for: PCI DSS (rows 82–91), ESG/DEI/modern slavery (146–159), IoMT (64), antitrust (127).
