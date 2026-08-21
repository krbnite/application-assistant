# Cover Letter Output Contract

This file defines what "done" means when creating a tailored cover letter from Kevin's application-assistant system.

## Primary Inputs

- `COVER_LETTER_BANK.md`: canonical reservoir of reusable cover-letter paragraph modules.
- `COVER_LETTER_PLAN_TEMPLATE.json`: copyable JSON plan for selecting and lightly editing cover-letter modules.
- `generate_cover_letter_docx.py`: DOCX generator that consumes a role-specific cover-letter plan.
- `PROFILE_BANK.md`, `JD_CLUSTER_BANK.md`, `RESUME_BULLET_BANK.md`, and the tailored resume audit: supporting context for choosing the right emphasis.

## Output Format

- Create a tailored `.docx` cover letter by default.
- Do not create a PDF by default. Kevin will convert the DOCX to PDF at submission time if needed.
- Use this filename pattern unless Kevin asks otherwise:
  - `YYYY-MM-DD_Kevin-Urban_Cover-Letter_{Company}_plan.json`
  - `YYYY-MM-DD_Kevin-Urban_Cover-Letter_{Company}.docx`
- Store each role-specific cover-letter plan and DOCX in that application's associated job folder.
- Completed role-specific cover-letter plans and DOCXs are application artifacts, not canonical process files. Keep them under ignored `job-search/` folders by default.
- Track only reusable templates, generators, banks, archetypes, and process rules. If a tailored cover letter creates reusable language, promote that language into `COVER_LETTER_BANK.md` rather than tracking the completed job-specific artifact.

## Length And Shape

- Target length: 1 page.
- Usual structure: salutation, 4-6 paragraphs, closing, signature.
- Target word count: roughly 400-650 words.
- Prefer short paragraphs over dense walls of text.
- If a letter exceeds one page, cut before shrinking type.

## Selection Contract

For each cover letter:

1. Choose an opener from `COVER_LETTER_BANK.md` based on the primary profile/JD cluster.
2. Choose 2-3 evidence paragraphs that support the role's most important hidden concern.
3. Choose one company/role bridge that explains why this specific role makes sense.
4. Choose one closing paragraph.
5. Lightly edit selected modules for the job description's terminology, company mission, product context, and target role.
6. Create new paragraphs only when the JD requires a materially distinct argument that the bank cannot express.
7. If new paragraph language is broadly reusable, add it to `COVER_LETTER_BANK.md`; otherwise keep it in the local plan and audit only.

## Tone Contract

- Use Kevin's established cover-letter voice: substantive, technically literate, thesis-driven, and low-fluff.
- The letter should explain the through-line behind the resume, not repeat every bullet.
- Keep enthusiasm concrete: tie interest to the company's actual problem, data, product, or mission.
- Use honest adjacent-domain framing when Kevin lacks exact domain experience.
- Do not fabricate experience or imply direct ownership of unsupported domains, tools, regulatory activities, or clinical expertise.

## Plan Contract

Use `COVER_LETTER_PLAN_TEMPLATE.json` as the starting shape for a role-specific plan.

- Plain string IDs pull exact canonical text from `COVER_LETTER_BANK.md`.
- Object entries with `id`, `label`, and/or `text` represent light edits to canonical modules and must be defended in the audit.
- Object entries without an `id` are custom paragraphs and should be rare.
- `variables` supplies placeholder values such as `company_problem`, `target_domain`, and `closing_keywords`.
- Validate before generating when possible.

## Audit Contract

When a tailored resume audit exists for the same role, add or complete the cover-letter section in that audit.

The audit should record:

- Cover-letter plan path and DOCX path.
- Starting modules selected.
- Which modules were kept as-is, lightly edited, or replaced.
- Any new paragraphs created and whether they should be promoted to `COVER_LETTER_BANK.md`.
- Any claims intentionally avoided.
- Render status and page count.

## Verification

- Render and visually verify the DOCX before delivery.
- Confirm page count.
- Check for awkward page breaks, cramped paragraphs, inconsistent spacing, missing signature, or unresolved placeholders.
- If visual rendering is unavailable, say so in the final response.

## Final Response Contract

When delivering or summarizing a tailored cover letter, include:

- Cover-letter DOCX path.
- Cover-letter plan path.
- Audit path if updated.
- Modules selected and any meaningful edits.
- Any new reusable language or bank updates.
- Page count and whether visual verification was completed.
