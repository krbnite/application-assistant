# General Resume Workflow

Use this mode for a broad research/ML resume without a single target JD, including contractor/annotation platforms and a public GitHub readership. It is a curated CV-like output, not a new canonical evidence source.

## When to run

Run when Kevin requests it, at the start of a new job-search cycle, or after substantial new evidence merits a refresh. When new bullets are promoted, suggest a refresh if useful; do not regenerate automatically for every addition or wording edit. Confirm the current search folder from context; do not assume the calendar year always defines a new search.

## Inputs and selection

Read this guide, AGENTS.md, RESUME_TAILORING_AGENT.md, MASTER_RESUME_TEMPLATE.md, PROFILE_BANK.md, RESUME_BULLET_BANK.md, PUBLICATION_PRESENTATION_BANK.md, OUTPUT_CONTRACT.md, and TAILORED_RESUME_PLAN_TEMPLATE.json. JD_CLUSTER_BANK.md is optional for balancing breadth; no JD or cluster-match analysis is required. Start from canonical evidence rather than an earlier generated resume. Use the Default Sensor ML Research Scientist profile as a starting point, then explain any broadening needed for applied ML, research software, or other supported work.

Select distinct contributions across recent sensor/health work, wearable ML, research software, production business ML, physical-science research, projects, publications, and useful training or awards. These are candidate sections, not a mandate to include everything. Keep a coherent hands-on research identity. No fixed page cap applies: include useful breadth while cutting duplicate accomplishments, alternative versions of the same bullet, and low-value detail. Preserve publication status and attribution. Follow the IC/functional-title rules and choose separate or grouped CVB layout deliberately, recording why. Do not manufacture a Staff/Principal rank translation.

## Outputs and build

Keep local deliverables in `job-search/<cycle>/00_General-Resume/`:

- `YYYY-MM-DD_Kevin-Urban_General-Resume.docx` (required editable deliverable).
- PDF only when requested; default is DOCX.

Maintain one public, tracked `GENERAL_RESUME.md` at the repository root, with a Last updated date and a prominent README link once the file exists. The banks remain authoritative. Review the existing Markdown and its Git diff before rebuilding; reconcile useful manual edits by deliberately promoting supported facts/wording into the banks or incorporating justified output edits into the new selection. Do not silently discard edits or treat old resume claims as new evidence.

Use one temporary selection plan, based on TAILORED_RESUME_PLAN_TEMPLATE.json, under `job-search/<cycle>/00_General-Resume/supporting/`. Add:

```json
{
  "workflow_mode": "general-resume",
  "job_search_cycle": "2026",
  "date": "2026-10-19",
  "company": "General",
  "role_title": "General research science and applied ML resume",
  "public_contact_email": "kevin.ddu@gmail.com"
}
```

Supply the normal profile, sections and selected bank entries as well. When GENERAL_RESUME.md exists, add `public_resume_base_sha256` with the SHA-256 of the version reviewed and reconciled. The generator refuses an absent/stale baseline before writing either output. The hash prevents accidental overwrite; it does not substitute for editorial review. Inspect both outputs before committing public changes.

Validate and generate with the canonical generator:

```bash
python generate_resume_docx.py job-search/2026/00_General-Resume/supporting/general_resume_plan.json --validate-only
python generate_resume_docx.py job-search/2026/00_General-Resume/supporting/general_resume_plan.json
```

General mode derives the two output paths from cycle/date; it ignores the template's role-specific output_path and disallows --out. DOCX and Markdown use the same selected text, section order, grouped titles, and variants. Markdown replaces the private contact line with public email, LinkedIn, and GitHub links. Use only the agreed public email; omit phone, street address, private notes, job-search strategy, unsupported claims, and internal evidence/guidance. Review free text as well as bank selections for disclosure suitability. Neither output contains bank IDs or selection rationale.

## Verification and cleanup

Validate the plan, inspect selected evidence for coverage and duplication, verify functional/official headings and dates, and check public content and contact details. Render the final DOCX, inspect every page, and report actual page count; length alone is not a failure. Follow the documents skill for rendering. Review Markdown and its diff, including any manual-edit reconciliation. If rendering or content verification fails, preserve temporary material and explain what remains; never claim unperformed QA.

After successful verification and delivery, remove only temporary plans, one-off build scripts, and rendering intermediates created for this general-resume run. Do not delete pre-existing files, final DOCX, requested PDF, or public Markdown. The generator cleans its own scratch directory but retains the input plan until the agent completes QA. General mode does not require a durable plan, formal audit, cover letter, or interview Q&A. Report selection/positioning decisions, layout, omissions, output locations, page count, verification, and cleanup in final notes.

## Refresh and publication

Commit public Markdown only after reviewing its diff and public content; never commit local search artifacts. Add the README link when first publishing the file. Retain earlier dated local deliverables unless Kevin requests cleanup; same-day replacement should be intentional. Existing misplaced broad-resume files are a separate migration decision, not permission to move/delete them during protocol implementation. A new search or bank update does not itself authorize publishing or pushing changes.
