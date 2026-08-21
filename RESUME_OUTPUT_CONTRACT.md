# Tailored Resume Output Contract

This file defines what "done" means when creating a tailored resume from Kevin's Markdown resume system.

## Primary Inputs

- `MASTER_RESUME_TEMPLATE.md`: canonical resume structure and section placeholders.
- `PROFILE_BANK.md`: canonical reusable profile/headline options.
- `JD_CLUSTER_BANK.md`: profile clusters, archetype JDs, and core/add-on matching signals.
- `RESUME_BULLET_BANK.md`: canonical evidence reservoir and cluster-scored bullet selection guide.
- `TAILORED_RESUME_AUDIT_TEMPLATE.md`: required audit format.
- `TAILORED_RESUME_PLAN_TEMPLATE.json`: copyable JSON plan for selecting profile, themes, bullets, skills, education, and publications.
- `generate_resume_docx.py`: DOCX generator that consumes a role-specific plan.

## Output Format

- Create a tailored `.docx` resume by default.
- Do not create a PDF by default. Kevin will convert the final DOCX to PDF at submission time so he can make final manual tweaks.
- Use this filename pattern unless Kevin asks otherwise:
  - `YYYY-MM-DD_Kevin-Urban_Resume_{Company}_plan.json`
  - `YYYY-MM-DD_Kevin-Urban_Resume_{Company}.docx`
  - `YYYY-MM-DD_Kevin-Urban_Resume_{Company}_audit.md`

## Length Target

- Target length: 3 pages.
- A fourth page is allowed only when Kevin or the agent explicitly decides it is necessary or strategically appropriate.
- If the resume reaches 4 pages, the audit must include a short justification.
- Do not preserve bullets merely because they are strong in the abstract. A tailored 3-page resume should feel deliberately selected.

## Cluster Confidence Rule

Use the JD archetype's `Core / necessary matching signals` to choose the primary cluster. Use `Variable / add-on signals` only after the primary cluster is chosen.

Suggested confidence labels:

- `High`: one cluster clearly matches the JD's core problem, data type, responsibilities, and hidden concerns; secondary clusters are only flavor or support.
- `Medium-High`: one cluster is the best match, but a secondary cluster should influence profile language or bullet selection.
- `Mixed`: two clusters both match core JD signals; choose a primary cluster and deliberately borrow from the secondary.
- `Low`: no current cluster fits the core JD signals well; consider the default profile or create a new retained/provisional cluster.

Do not let an add-on signal override a missing core signal. For example, FDA IDE/PMA language strengthens a health/neurotech match when present, but it does not define the health/neurotech archetype by itself.

## Bullet Selection Contract

For each tailored resume:

1. Start from the primary cluster's high-scoring bullets in `RESUME_BULLET_BANK.md`.
2. Add secondary-cluster bullets only when the JD genuinely blends clusters.
3. Drop primary-cluster bullets when they are redundant, too detailed, or less relevant than other available evidence.
4. Prefer light edits and merges over inventing new bullets.
5. Create new bullets only when the JD reveals a real evidence gap and Kevin's known background supports the claim.
6. If a new bullet is created, decide in the audit whether it should be retained in the bullet bank, marked provisional, or treated as one-off tailoring.

## Profile / Headline Contract

For each tailored resume:

1. Start from one profile/headline pair in `PROFILE_BANK.md` unless a new cluster is required.
2. Lightly edit the profile for the JD's core and add-on signals.
3. Surface and defend every meaningful profile/headline change in the audit.
4. Distinguish between:
   - `Light edit`: wording, emphasis, or ordering changed for this JD.
   - `Add-on`: a JD-specific element added to the generic profile.
   - `New reusable profile language`: wording that may strengthen `PROFILE_BANK.md`.
5. Do not update `PROFILE_BANK.md` for one-off wording unless it improves the reusable cluster profile.

## Template Contract

For each tailored resume:

1. Start from `MASTER_RESUME_TEMPLATE.md`.
2. Fill the profile slot from `PROFILE_BANK.md`.
3. Fill the core research themes, experience bullets, skills, and publications from `RESUME_BULLET_BANK.md`.
4. Keep stable sections such as education unless the JD or page budget creates a clear reason to alter them.
5. Treat existing DOCX resumes as examples or generated outputs, not as canonical sources.
6. Record the selected profile, bullet IDs, edited text, merged bullets, custom bullets, skills, and publications in a role-specific JSON plan.
7. Generate the DOCX with `generate_resume_docx.py`; do not manually rebuild the DOCX unless the generator cannot express the needed tailoring.

## Generator Contract

Use `TAILORED_RESUME_PLAN_TEMPLATE.json` as the starting shape for a role-specific plan.

- Plain string IDs pull exact canonical text from `RESUME_BULLET_BANK.md`.
- Object entries with `id`, `label`, and/or `text` represent light edits to canonical bullets and must be defended in the audit.
- Object entries without an `id` are custom bullets and should be rare; the audit must decide whether to add them to the bullet bank, mark them provisional, or keep them one-off.
- Blank `headline` and `profile` fields are filled from the selected `profile_cluster`; populated fields indicate role-specific profile/headline tailoring and must be audited.
- Validate before generating when possible.

## Verification

- Render and visually verify the DOCX before delivery.
- Confirm page count.
- Check for awkward page breaks, orphan headings, cramped bullets, inconsistent formatting, or missing profile/audit details.
- If visual rendering is unavailable, say so in the final response.

## Final Response Contract

The final response should include:

- Tailored resume path.
- Resume plan path.
- Audit path.
- Primary cluster and confidence.
- Starting profile used or new cluster created.
- Any profile-bank, JD-archetype, or bullet-bank updates.
- Page count and whether the DOCX was visually verified.
