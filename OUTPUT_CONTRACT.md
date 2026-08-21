# Application Output Contract

This file defines what "done" means when creating a tailored application packet from Kevin's application-assistant system.

## Primary Inputs

- `MASTER_RESUME_TEMPLATE.md`: canonical resume structure and section placeholders.
- `PROFILE_BANK.md`: canonical reusable profile/headline options.
- `JD_CLUSTER_BANK.md`: profile clusters, archetype JDs, and core/add-on matching signals.
- `RESUME_BULLET_BANK.md`: canonical evidence reservoir and cluster-scored bullet selection guide.
- `COVER_LETTER_BANK.md`: canonical reservoir of reusable cover-letter paragraph modules.
- `TAILORED_RESUME_AUDIT_TEMPLATE.md`: required audit format for tailoring decisions.
- `INTERVIEW_QA_TEMPLATE.md`: role-specific HR screener and hiring-manager Q&A prep template.
- `TAILORED_RESUME_PLAN_TEMPLATE.json`: copyable JSON plan for selecting resume profile, themes, bullets, skills, education, and publications.
- `COVER_LETTER_PLAN_TEMPLATE.json`: copyable JSON plan for selecting and lightly editing cover-letter modules.
- `generate_resume_docx.py`: DOCX generator that consumes a role-specific resume plan.
- `generate_cover_letter_docx.py`: DOCX generator that consumes a role-specific cover-letter plan.

## Default Packet

When Kevin provides a job description and asks for a tailored application packet, create these by default unless he says to skip one:

- Tailored resume DOCX.
- Cover-letter DOCX.
- Role-specific audit Markdown.
- Interview Q&A Markdown companion.

Do not create PDFs by default. Kevin will convert final DOCX files to PDF at submission time so he can make final manual tweaks.

Use this filename pattern unless Kevin asks otherwise. Keep submission-facing DOCX files in the associated job folder root; keep support/prep files in a `supporting/` subfolder.

- `YYYY-MM-DD_Kevin-Urban_Resume_{Company}.docx`
- `YYYY-MM-DD_Kevin-Urban_Cover-Letter_{Company}.docx`
- `supporting/YYYY-MM-DD_Kevin-Urban_Resume_{Company}_plan.json`
- `supporting/YYYY-MM-DD_Kevin-Urban_Cover-Letter_{Company}_plan.json`
- `supporting/YYYY-MM-DD_Kevin-Urban_Resume_{Company}_audit.md`
- `supporting/YYYY-MM-DD_Kevin-Urban_{Company}_interview_qa.md`

Store generated resume and cover-letter DOCX files in the associated job folder root so the immediately needed application files are easy to find. Store role-specific plans, audits, and interview Q&A companions in that job folder's `supporting/` subfolder.

Completed role-specific plans, resumes, cover letters, audits, and interview Q&A companions are application artifacts, not canonical process files. Keep them under ignored `job-search/` folders by default.

Track only reusable templates, generators, banks, archetypes, and process rules. If a completed job-specific artifact reveals a reusable lesson, promote that lesson into a tracked bank or process file rather than tracking the completed artifact itself.

## Resume Contract

### Length Target

- Target length: 3 pages.
- A fourth page is allowed only when Kevin or the agent explicitly decides it is necessary or strategically appropriate.
- If the resume reaches 4 pages, the audit must include a short justification.
- Do not preserve bullets merely because they are strong in the abstract. A tailored 3-page resume should feel deliberately selected.

### Cluster Confidence Rule

Use the JD archetype's `Core / necessary matching signals` to choose the primary cluster. Use `Variable / add-on signals` only after the primary cluster is chosen.

Suggested confidence labels:

- `High`: one cluster clearly matches the JD's core problem, data type, responsibilities, and hidden concerns; secondary clusters are only flavor or support.
- `Medium-High`: one cluster is the best match, but a secondary cluster should influence profile language or bullet selection.
- `Mixed`: two clusters both match core JD signals; choose a primary cluster and deliberately borrow from the secondary.
- `Low`: no current cluster fits the core JD signals well; consider the default profile or create a new retained/provisional cluster.

Do not let an add-on signal override a missing core signal. For example, FDA IDE/PMA language strengthens a health/neurotech match when present, but it does not define the health/neurotech archetype by itself.

### Bullet Selection

For each tailored resume:

1. Start from the primary cluster's high-scoring bullets in `RESUME_BULLET_BANK.md`.
2. Add secondary-cluster bullets only when the JD genuinely blends clusters.
3. Drop primary-cluster bullets when they are redundant, too detailed, or less relevant than other available evidence.
4. Prefer light edits and merges over inventing new bullets.
5. Create new bullets only when the JD reveals a real evidence gap and Kevin's known background supports the claim.
6. If a new bullet is created, decide in the audit whether it should be retained in the bullet bank, marked provisional, or treated as one-off tailoring.

### Profile / Headline

For each tailored resume:

1. Start from one profile/headline pair in `PROFILE_BANK.md` unless a new cluster is required.
2. Lightly edit the profile for the JD's core and add-on signals.
3. Surface and defend every meaningful profile/headline change in the audit.
4. Distinguish between:
   - `Light edit`: wording, emphasis, or ordering changed for this JD.
   - `Add-on`: a JD-specific element added to the generic profile.
   - `New reusable profile language`: wording that may strengthen `PROFILE_BANK.md`.
5. Do not update `PROFILE_BANK.md` for one-off wording unless it improves the reusable cluster profile.

### Resume Plan And Generator

Use `TAILORED_RESUME_PLAN_TEMPLATE.json` as the starting shape for a role-specific resume plan.

- Start from `MASTER_RESUME_TEMPLATE.md`.
- Fill the profile slot from `PROFILE_BANK.md`.
- Fill core research themes, experience bullets, skills, education, and publications from `RESUME_BULLET_BANK.md`.
- Plain string IDs pull exact canonical text from `RESUME_BULLET_BANK.md`.
- Object entries with `id`, `label`, and/or `text` represent light edits to canonical bullets and must be defended in the audit.
- Object entries without an `id` are custom bullets and should be rare.
- Blank `headline` and `profile` fields are filled from the selected `profile_cluster`; populated fields indicate role-specific tailoring and must be audited.
- Use `publication_section_title` when the selected publication set includes nonstandard entries such as unpublished manuscripts, conference abstracts/posters, public science writing, or research writing.
- Treat existing DOCX resumes as examples or generated outputs, not canonical sources.
- Generate the DOCX with `generate_resume_docx.py`; do not manually rebuild the DOCX unless the generator cannot express the needed tailoring.
- Validate before generating when possible.

## Cover Letter Contract

### Length And Shape

- Target length: 1 page.
- Usual structure: salutation, 4-6 paragraphs, closing, signature.
- Target word count: roughly 400-650 words.
- Prefer short paragraphs over dense walls of text.
- If a letter exceeds one page, cut before shrinking type.

### Selection And Tone

For each cover letter:

1. Choose an opener from `COVER_LETTER_BANK.md` based on the primary profile/JD cluster.
2. Choose 2-3 evidence paragraphs that support the role's most important hidden concern.
3. Choose one company/role bridge that explains why this specific role makes sense.
4. Choose one closing paragraph.
5. Lightly edit selected modules for the job description's terminology, company mission, product context, and target role.
6. Create new paragraphs only when the JD requires a materially distinct argument that the bank cannot express.
7. If new paragraph language is broadly reusable, add it to `COVER_LETTER_BANK.md`; otherwise keep it in the local plan and audit only.

Use Kevin's established cover-letter voice: substantive, technically literate, thesis-driven, and low-fluff. The letter should explain the through-line behind the resume, not repeat every bullet. Keep enthusiasm concrete: tie interest to the company's actual problem, data, product, or mission.

Use honest adjacent-domain framing when Kevin lacks exact domain experience. Do not fabricate experience or imply direct ownership of unsupported domains, tools, regulatory activities, or clinical expertise.

### Cover-Letter Plan And Generator

Use `COVER_LETTER_PLAN_TEMPLATE.json` as the starting shape for a role-specific cover-letter plan.

- Plain string IDs pull exact canonical text from `COVER_LETTER_BANK.md`.
- Object entries with `id`, `label`, and/or `text` represent light edits to canonical modules and must be defended in the audit.
- Object entries without an `id` are custom paragraphs and should be rare.
- `variables` supplies placeholder values such as `company_problem`, `target_domain`, and `closing_keywords`.
- Generate the DOCX with `generate_cover_letter_docx.py`.
- Validate before generating when possible.

## Interview Q&A Contract

Create a role-specific Markdown Q&A companion by default, using `INTERVIEW_QA_TEMPLATE.md`.

- Include likely HR screener questions and hiring-manager questions.
- Use the tailored resume, cover letter, resume audit, JD cluster, and job description to choose the strongest answer anchor for each question.
- Optimize for answer selection and concise landings, not exhaustive recall.
- For questions where Kevin might over-explain, include a short "stop after" cue.
- Include gaps and do-not-overstate notes so Kevin can answer honestly without volunteering unnecessary weakness.
- Store the completed Q&A file in the ignored associated job folder's `supporting/` subfolder.

## Audit Contract

Create one role-specific audit from `TAILORED_RESUME_AUDIT_TEMPLATE.md` and store it in the associated job folder's `supporting/` subfolder.

The audit should record:

- Primary profile/JD cluster, confidence, and any archetype updates.
- Resume profile/headline choices and edits.
- Resume bullet choices, edits, merges, drops, and any new bullets.
- Cover-letter plan path and DOCX path.
- Cover-letter modules kept as-is, lightly edited, replaced, dropped, or newly created.
- Any resume or cover-letter language that should be promoted to a reusable bank.
- Claims intentionally avoided and gaps not to overstate.
- Render status and page count for generated DOCX files.

## Verification

- Render and visually verify each generated DOCX before delivery.
- Confirm resume and cover-letter page counts.
- Check for awkward page breaks, orphan headings, cramped bullets, cramped paragraphs, inconsistent formatting, missing signature, missing audit details, or unresolved placeholders.
- If visual rendering is unavailable, say so in the final response.

## Final Response Contract

The final response should include:

- Tailored resume path and page count.
- Resume plan path.
- Cover-letter DOCX path and page count.
- Cover-letter plan path.
- Audit path.
- Interview Q&A path.
- Primary cluster and confidence.
- Starting profile used or new cluster created.
- Any profile-bank, JD-archetype, resume-bullet-bank, or cover-letter-bank updates.
- Whether visual verification was completed for each DOCX.
