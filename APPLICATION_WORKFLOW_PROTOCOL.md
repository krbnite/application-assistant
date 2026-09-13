# Application Workflow Protocol

This is the entrypoint for running `application-assistant` efficiently.

Use this file first. Do not read every process, bank, template, and historical artifact by default. Choose the workflow mode Kevin requested, read only the files required for that mode, and expand only when the job or Kevin's request makes the extra work useful.

## Fit-Eval First

When Kevin pastes a new job description and asks whether it is a fit, start with `FIT_EVAL.md`, not the packet workflow below. That screening step should produce a verdict, the reasoning behind it, and a one-line note Kevin can paste into his tracker. End by asking whether Kevin wants to discuss the verdict further or proceed to resume-first mode with any requested add-ons.

When Kevin explicitly asks to tailor a resume, apply to a role, build a packet, or run the workflow for an already-greenlit role, use the packet workflow below directly. Treat any prior fit evaluation as context, but do not repeat the full screening pass unless the role, company, or constraints have changed.

## Default Mode: Resume-First

Use resume-first mode when Kevin asks to apply to a job, tailor a resume, or run the workflow without explicitly requesting a full packet.

### Required Inputs

Read these files before creating the first resume draft:

- `APPLICATION_WORKFLOW_PROTOCOL.md`
- `AGENTS.md`
- `OUTPUT_CONTRACT.md`
- `MASTER_RESUME_TEMPLATE.md`
- `TAILORED_RESUME_PLAN_TEMPLATE.json`
- `JD_CLUSTER_BANK.md`
- `PROFILE_BANK.md`
- `RESUME_BULLET_BANK.md`
- the target role's `job-description.md`

Read `PUBLICATION_PRESENTATION_BANK.md` only when the JD is research-heavy, publication-aware, academic/CV-like, conference/science oriented, or when the selected resume strategy needs a publication/research-writing section.

### Resume-First Outputs

Produce:

- role-specific tailored resume plan JSON in the job folder's `supporting/` subfolder
- tailored resume DOCX in the job folder root
- concise final notes describing primary cluster, fit confidence, major profile/bullet choices, and any important caveats

Do not create a cover letter, formal audit, or interview Q&A companion in resume-first mode unless Kevin asks for that add-on.

Kevin performs DOCX visual QA by default. The agent should still run cheap structural checks when practical: validate the plan, confirm expected company/role naming, check for unresolved placeholders, and report whether page count or visual rendering was skipped.

For priority roles, run a lightweight post-draft cultivation check before final delivery:

- Confirm the first experience section leads with work Kevin would want to discuss, not merely the easiest keyword bridge.
- Check that tailored rewrites preserve the bank-supported claim, avoid unsupported additions, and restore any specifics lost without a role-specific purpose.
- Restore useful concrete evidence such as numbers, named systems, named stakeholders, or named data sources when it strengthens the target role.
- Check for duplicate evidence caused by awards, projects, or repeated bullets.
- Ensure the profile explains the bridge into the target company's domain without apologizing for honest gaps.
- Remove skill keywords broader than Kevin's evidence or the selected cluster's guardrails support.

## Full Packet Mode

Use full packet mode only when Kevin explicitly asks for a full packet or lists the full deliverables.

In addition to resume-first files, read:

- `PUBLICATION_PRESENTATION_BANK.md`
- `COVER_LETTER_BANK.md`
- `COVER_LETTER_PLAN_TEMPLATE.json`
- `TAILORED_RESUME_AUDIT_TEMPLATE.md`
- `INTERVIEW_QA_TEMPLATE.md`

Produce:

- tailored resume DOCX
- tailored cover-letter DOCX
- resume plan JSON
- cover-letter plan JSON
- role-specific audit Markdown
- interview Q&A Markdown companion

Run the full QA pass requested by `OUTPUT_CONTRACT.md`, including DOCX render/visual checks, unless Kevin explicitly says he will handle visual QA.

## Optional Add-On Modes

Use these after resume-first mode, or alongside it when Kevin asks.

### Cover Letter Add-On

Use when the application requires or accepts a cover letter, or Kevin says the role is worth one.

Read:

- `APPLICATION_WORKFLOW_PROTOCOL.md`
- `OUTPUT_CONTRACT.md`
- `COVER_LETTER_BANK.md`
- `COVER_LETTER_PLAN_TEMPLATE.json`
- the target role's `job-description.md`
- the existing role-specific resume plan JSON

Read `PROFILE_BANK.md`, `RESUME_BULLET_BANK.md`, or the generated resume DOCX only if the resume plan does not provide enough context.

Produce:

- cover-letter plan JSON in `supporting/`
- cover-letter DOCX in the job folder root

### Audit Add-On

Use when Kevin wants a formal decision record, a final high-confidence packet, or a reusable trail of why the resume was built the way it was.

Read:

- `APPLICATION_WORKFLOW_PROTOCOL.md`
- `OUTPUT_CONTRACT.md`
- `TAILORED_RESUME_AUDIT_TEMPLATE.md`
- the target role's `job-description.md`
- the existing role-specific resume plan JSON

Read generated DOCX files, `PROFILE_BANK.md`, `RESUME_BULLET_BANK.md`, or prior packets only when the requested audit scope requires that extra detail.

Produce:

- role-specific audit Markdown in `supporting/`

In resume-first mode without the audit add-on, summarize the most important profile and bullet decisions in the final response instead of creating the full audit file.

### Interview Q&A Add-On

Use when Kevin has an interview, expects a recruiter screen, or asks for preparation.

Read:

- `APPLICATION_WORKFLOW_PROTOCOL.md`
- `OUTPUT_CONTRACT.md`
- `INTERVIEW_QA_TEMPLATE.md`
- the target role's `job-description.md`
- the existing role-specific resume plan JSON

Read cover-letter artifacts only if they already exist and Kevin wants interview answers aligned with the letter.

Produce:

- interview Q&A Markdown companion in `supporting/`

### Visual QA Add-On

Use when Kevin asks the agent to inspect final DOCX rendering, page counts, and layout details.

Read:

- `APPLICATION_WORKFLOW_PROTOCOL.md`
- the already-generated DOCX files Kevin asks about
- the target role's `job-description.md` only if checking company/role residue requires it

Render and visually inspect generated DOCX files. Check for page count, awkward page breaks, orphan headings, cramped bullets, inconsistent formatting, unresolved placeholders, and wrong-company residue.

## Prior-Packet Reuse

For similar jobs, start by identifying one or two nearby prior packets from the same cluster rather than scanning all historical applications.

Use prior packets as examples of judgment, not as canonical sources. Before adopting any prior-packet idea, verify that it is supported by the canonical banks or deliberately promote it into a tracked bank/process file.

When optimizing for low token/credit usage:

1. Pick the likely cluster from the JD and `JD_CLUSTER_BANK.md`.
2. Scan only relevant sections of `RESUME_BULLET_BANK.md` and `PROFILE_BANK.md`.
3. Optionally inspect one or two closest prior same-cluster packets for missed section-level ideas.
4. Do not deep-scan the full current-year job-search history unless full packet mode or audit add-on requires it.

## Cover Letter Default

Cover letters are optional. Do not generate one merely because the old full-packet workflow did.

Generate a cover letter only when:

- the application requires one
- the application accepts one and Kevin wants to include it
- the role is strategically important enough that a letter is worth the extra work
- Kevin explicitly requests full packet mode

For forms that ask "why this company/role," prefer a short reusable answer over a full cover-letter DOCX.

## Suggested Prompt

Use this prompt for the low-credit default workflow:

```text
Please use the optimized application-assistant workflow for the JD in:
job-search/2026/XX_Company_Role/job-description.md

First read APPLICATION_WORKFLOW_PROTOCOL.md, then read only the files required for resume-first mode. Generate the tailored resume plan and resume DOCX first. Do not create a cover letter, formal audit, interview Q&A, or DOCX visual render check unless I explicitly ask for those add-ons. I will handle visual QA by default.
```

Use add-on prompts later only when needed:

### Cover Letter Add-On Prompt

```text
Please use APPLICATION_WORKFLOW_PROTOCOL.md and run cover-letter add-on mode for:
job-search/2026/XX_Company_Role/

Read only the files required for the cover-letter add-on. Use the existing resume plan/resume DOCX and job description in the role folder as context. Generate only the cover-letter plan and cover-letter DOCX. Do not create an audit, interview Q&A, or DOCX visual render check unless I explicitly ask.
```

### Interview Q&A Add-On Prompt

```text
Please use APPLICATION_WORKFLOW_PROTOCOL.md and run interview-Q&A add-on mode for:
job-search/2026/XX_Company_Role/

Read only the files required for the interview-Q&A add-on. Use the existing resume plan/resume DOCX and job description in the role folder as context. Generate only the interview Q&A Markdown file. Do not create a cover letter, audit, or DOCX visual render check unless I explicitly ask.
```

### Audit Add-On Prompt

```text
Please use APPLICATION_WORKFLOW_PROTOCOL.md and run audit add-on mode for:
job-search/2026/XX_Company_Role/

Read only the files required for the audit add-on. Use the existing resume plan/resume DOCX and job description in the role folder as context. Generate only the audit Markdown file. Do not create a cover letter, interview Q&A, or DOCX visual render check unless I explicitly ask.
```

### Visual QA Add-On Prompt

```text
Please use APPLICATION_WORKFLOW_PROTOCOL.md and run visual-QA add-on mode for:
job-search/2026/XX_Company_Role/

Inspect only the already-generated DOCX files I ask about. Report page counts, obvious formatting/render issues, wrong-company residue, and unresolved placeholders. Do not generate new application artifacts unless I explicitly ask.
```

Use this explicit override only when the extra artifacts are truly wanted:

```text
Please use APPLICATION_WORKFLOW_PROTOCOL.md and run full packet mode for the JD in:
job-search/2026/XX_Company_Role/job-description.md

This intentionally overrides resume-first mode. Generate the resume DOCX, cover-letter DOCX, audit, interview Q&A, and supporting plan files. Perform the final QA pass unless I say I will handle visual QA.
```
