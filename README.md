# Application Assistant

`application-assistant` is a small, agent-assisted system for creating tailored job-application packets from reusable resume, cover-letter, job-description, and interview-prep materials.

The repo tracks the reusable process, not the details of any particular job search. Job-specific resumes, cover letters, plans, audits, and interview notes live under ignored `job-search/` folders.

## What This Does

Given a job description, the intended workflow is:

1. Match the job description to a reusable profile/JD cluster.
2. Choose and lightly tailor the appropriate resume profile.
3. Select relevant resume bullets from the canonical bullet bank.
4. Generate a tailored resume DOCX.
5. Optionally generate a tailored cover-letter DOCX when useful or required.
6. Optionally produce an audit explaining profile, bullet, and cover-letter decisions.
7. Optionally produce an interview Q&A companion for HR screener and hiring-manager prep.

The goal is not full autopilot. Kevin still reviews the packet before submission. The system is meant to remove repetitive re-optimization and make tailoring decisions auditable.

## Usage

To help ensure the agent follows the intended workflow:

- **Job Search Folder:** First, if not already established, create a new `job-search/<name-of-job-search>` folder for your current job search.
  - Example: I have `job-search/2024/` and `job-search/2026/`, each of which contains subfolders for each role being pursued.
- **Role Subfolders:** Within that folder, create subfolders for each role being pursued.
  - Example: My current `2026` syntax has subfolders like `job-search/2026/<JobNumber>_<Company>_<Role>`, which I like because it organizes the job search chronologically and by company/role, but you can use whatever naming convention you prefer, such as `job-search/2026/<Company1>/<Role1>`, `job-search/2026/<Company1>/<Role2>`, or `job-search/2026/<Company2>/<Role1>`.
- **Job Description:** Each subfolder should contain the job description and any supporting materials for that role.
  - Example: `job-search/2026/17_Dexcom/job-description.md` contains the job description for the Dexcom Staff Algorithm Engineer role.
- **Prompt:** Using ChatGPT/Codex or Claude with permission to access the repo, use the following prompt to ensure the agent follows the intended workflow:

  ```
  Please use the optimized application-assistant workflow for the JD in:
  job-search/2026/XX_Company_Role/job-description.md

  First read APPLICATION_WORKFLOW_PROTOCOL.md, then read only the files required for resume-first mode. Generate the tailored resume plan and resume DOCX first. Do not create a cover letter, formal audit, interview Q&A, or DOCX visual render check unless I explicitly ask for those add-ons. I will handle visual QA by default.
  ```

  If a full packet is needed, use this prompt instead:

  ```
  Please use APPLICATION_WORKFLOW_PROTOCOL.md and run full packet mode for the JD in:
  job-search/2026/XX_Company_Role/job-description.md

  Generate the resume DOCX, cover-letter DOCX, audit, interview Q&A, and supporting plan files. Perform the final QA pass unless I say I will handle visual QA.
  ```

## Current Layout

The core files are intentionally plain Markdown, JSON, and Python so they can be reviewed, diffed, and updated cleanly.

### Workflow And Contracts

- `APPLICATION_WORKFLOW_PROTOCOL.md` - entrypoint for choosing resume-first, full-packet, or add-on workflows.
- `AGENTS.md` - high-level instructions for future agents working in this repo.
- `RESUME_TAILORING_AGENT.md` - main tailoring workflow and decision rules.
- `OUTPUT_CONTRACT.md` - what a completed application packet should include.
- `TAILORED_RESUME_AUDIT_TEMPLATE.md` - audit template for resume decisions.
- `INTERVIEW_QA_TEMPLATE.md` - role-specific interview prep template.

### Matching And Reusable Content

- `PROFILE_BANK.md` - reusable profile/headline clusters.
- `JD_CLUSTER_BANK.md` - job-description archetypes and cluster matching rules.
- `RESUME_BULLET_BANK.md` - canonical resume evidence reservoir and cluster-scored bullet guide.
- `PUBLICATION_PRESENTATION_BANK.md` - fuller CV-style inventory for research-heavy tailoring.
- `COVER_LETTER_BANK.md` - reusable cover-letter paragraph modules.

### Plans And Generators

- `TAILORED_RESUME_PLAN_TEMPLATE.json` - copyable plan shape for a tailored resume.
- `COVER_LETTER_PLAN_TEMPLATE.json` - copyable plan shape for a tailored cover letter.
- `generate_resume_docx.py` - generates a resume DOCX from a resume plan.
- `generate_cover_letter_docx.py` - generates a cover-letter DOCX from a cover-letter plan.
- `requirements.txt` - Python package requirements.

### Archives And Local Output

- `archive/legacy-cv-system/` - preserved legacy CV system and content archive.
- `LEGACY_CV_CONTENT_AUDIT.md` - notes on what was promoted from the legacy CV system.
- `job-search/` - ignored job-specific working folders.
- `.local/` - ignored local sanity-check and hygiene files.

## Quick Start

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Validate a resume plan:

```bash
python3 generate_resume_docx.py job-search/2026/example/supporting/example_resume_plan.json --validate-only
```

Generate a resume DOCX:

```bash
python3 generate_resume_docx.py job-search/2026/example/supporting/example_resume_plan.json
```

Validate a cover-letter plan:

```bash
python3 generate_cover_letter_docx.py job-search/2026/example/supporting/example_cover_letter_plan.json --validate-only
```

Generate a cover-letter DOCX:

```bash
python3 generate_cover_letter_docx.py job-search/2026/example/supporting/example_cover_letter_plan.json
```

For final DOCX work, render and visually inspect the output before submission. Layout matters.

## Content Promotion Rule

The top-level banks are the source of truth for generated application materials. Older resumes, old cover letters, `archive/`, `job-search/`, and external repositories can be mined for content, but useful material should be deliberately promoted into the relevant bank before it becomes part of the standard process.

Kevin's separate public `kitchensink` repository, `https://github.com/krbnite/kitchensink`, is a broad archive of older writing and cross-domain material. It should not be searched automatically for every application, but it is worth asking about when a role might benefit from public writing, older technical essays, talks, side projects, or other material not yet represented here.

## Public Repo Hygiene

This repo is intended to be public. Do not commit job-specific application materials by default. Before committing, check for:

- private job-search artifacts outside `job-search/`
- accidental Office lock files
- sensitive notes that belong in ignored local folders
- unsupported biographical or project claims
- generated DOCX/PDF outputs that should remain local

## Possible Future Structure

The current flat top-level layout keeps every canonical file easy to see while the system is still evolving. If the repo grows, a light structure would probably be cleaner:

```text
resume/
  MASTER_RESUME_TEMPLATE.md
  PROFILE_BANK.md
  RESUME_BULLET_BANK.md
  PUBLICATION_PRESENTATION_BANK.md
  TAILORED_RESUME_PLAN_TEMPLATE.json
  TAILORED_RESUME_AUDIT_TEMPLATE.md
  generate_resume_docx.py

cover-letter/
  COVER_LETTER_BANK.md
  COVER_LETTER_PLAN_TEMPLATE.json
  generate_cover_letter_docx.py

workflow/
  AGENTS.md
  RESUME_TAILORING_AGENT.md
  OUTPUT_CONTRACT.md
  JD_CLUSTER_BANK.md
  INTERVIEW_QA_TEMPLATE.md
```

If this restructuring happens, do it as a separate commit and update generator default paths, documentation references, and any agent instructions at the same time.
