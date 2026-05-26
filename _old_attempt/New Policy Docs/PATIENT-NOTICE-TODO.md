---
title: "TODO — Patient-Facing Notice of Privacy Practices"
last_reviewed: 2026-05-24
owner: "Privacy Officer"
status: "todo"
---

# TODO — Patient-Facing Notice of Privacy Practices

**This is not a policy. It's a placeholder for content Millie is missing.**

## The gap

During the policy migration (2026-05-24), we discovered that the file originally named `Millie Privacy Policy.docx` is **not** what it sounds like. It is a bundled archive of 9 internal HIPAA staff policies (Accounting of Disclosures, Breach Notification, Device & Media Management, Minimum Necessary, Paper Documents, Passwords, Remote Access, Safeguards, Workstation Use) — all of which now live in the consolidated policy files in `New Policy Docs/`.

**Millie does not appear to have a separate patient-facing Notice of Privacy Practices ("NPP") in this repository.**

A Notice of Privacy Practices is required under [45 CFR §164.520](https://www.ecfr.gov/current/title-45/section-164.520) and must:

- Be written in plain language;
- Be provided to every patient at first service delivery;
- Be posted in a clear and prominent location in the clinic;
- Be posted on Millie's public website if Millie has one;
- Be reviewed and re-issued whenever there is a material change.

## What needs to happen

1. **Confirm whether an NPP exists elsewhere.** Possible locations: clinic intake forms, the patient-facing website (milliclinic.com or similar), or a Google Workspace document not in this repo. If one exists, link to it from this file and rename or remove this TODO.
2. **If no NPP exists, draft one.** The required content per 45 CFR §164.520(b):
   - Header: "**THIS NOTICE DESCRIBES HOW MEDICAL INFORMATION ABOUT YOU MAY BE USED AND DISCLOSED AND HOW YOU CAN GET ACCESS TO THIS INFORMATION. PLEASE REVIEW IT CAREFULLY.**" (uppercase as required)
   - Effective date
   - How Millie uses and discloses PHI (Treatment, Payment, Health Care Operations, and other permitted uses — see [phi-use-and-disclosure.md](phi-use-and-disclosure.md))
   - When patient authorization is required (most marketing, sale of PHI, psychotherapy notes)
   - Patient rights (access, amendment, accounting of disclosures, restrictions, confidential communications, paper copy, breach notification) — see [patient-rights.md](patient-rights.md)
   - Millie's duties (maintain privacy, abide by Notice, notify of changes)
   - Complaints (how to file with Millie's Privacy Officer; how to file with HHS Office for Civil Rights — must not retaliate)
   - Contact for Privacy Officer
3. **Get clinical and legal review.** California has additional state-law requirements (CMIA — Confidentiality of Medical Information Act) that may need to be reflected.
4. **Plan distribution.**
   - Intake packet for every new patient
   - Posted at every clinic location (San Jose, Berkeley)
   - Posted on Millie's website
   - Acknowledgement of receipt collected and stored in patient record per 45 CFR §164.520(c)(2)(ii)
5. **Replace this TODO file** with the final NPP (or a redirect link if it lives in another system).

## Suggested filename when drafted

`notice-of-privacy-practices.md` — to clearly distinguish from the bundle that was misnamed `privacy-policy.md`.

## Related TODO

The bundle file `privacy-policy.md` is archived in `New Policy Docs/_archive/` for historical reference. Its substantive content (including the rescued IT-004 Device & Media Management Policy) has been consolidated into [technical-safeguards.md](technical-safeguards.md), [operational-safeguards.md](operational-safeguards.md), and the other thematic files. Once an actual NPP is drafted, the misnamed bundle no longer serves any reference purpose.
