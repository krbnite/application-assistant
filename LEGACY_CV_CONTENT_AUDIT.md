# Legacy CV Content Audit

This audit records what was reviewed from the imported legacy CV system and what was promoted into the current application-assistant system.

## Sources Reviewed

- `archive/legacy-cv-system/snippets/work/`
- `archive/legacy-cv-system/snippets/publications/`
- `archive/legacy-cv-system/snippets/misc/scholarships-and-awards.tex`
- `archive/legacy-cv-system/notes/work/easi-cvb/`
- Moved 2024 DOCX resumes now stored under ignored `job-search/2024/`

## Source Boundary

For public resume generation, use the top-level banks and template as the source of truth. Older local archives require deliberate promotion into the banks before use.

MachineSaidGo may be referenced as Kevin's LLC / exploratory side-project umbrella when strategically useful and supported by canonical content.

## Promoted To Active Bullet Bank

| New / updated ID | Source | Reason |
|---|---|---|
| `CVB-17` | Legacy CVB code-contribution and workflow notes | Captures reusable research-ops/team-enablement evidence not explicit in the current bank. |
| `CVB-18` | Legacy EaSiEco/database/knowledge-graph notes | Captures graph/database/schema work that can matter for knowledge representation, sensor ontology, or platform roles. |
| `WWE-06` | Legacy WWE content analytics snippet and 2024 DOCX resumes | Splits vendor/API remediation from the broader production data-products bullet. |
| `WWE-07` | Legacy WWE content analytics snippet and 2024 DOCX resumes | Preserves the strong 12-24 hour to minutes live-event latency story. |
| `WWE-08` | Legacy WWE advanced analytics snippet | Preserves attribution, survey-fusion, sentiment, and customer-behavior evidence for operational/business ML roles. |
| `CSTR-07` | Legacy CSTR research assistant snippet and old summary CV | Preserves the strongest forecasting/inverse-nowcasting version of the space-weather work. |
| `PUB-06` to `PUB-08` | Legacy publication snippets | Restores omitted peer-reviewed granular-dynamics publications. |
| `INT-02`, `INT-03` text updates | 2024 DOCX resumes and legacy snippets | Adds enough detail to make old NASA internships interpretable if ever selected. |

## Added As Separate Inventory

`PUBLICATION_PRESENTATION_BANK.md` was added because the legacy repo contains more publications, invited presentations, internal talks, awards, and CV-like material than belongs in the compact resume bullet bank.

Use that file for:

- research-heavy roles,
- academic/CV-like variants,
- cover letters,
- interview prep,
- audit support when a bullet references a presentation, poster, award, or grant/program milestone.

## Reviewed But Not Promoted

| Material | Decision |
|---|---|
| Unpromoted local-archive project material | Not promoted into the canonical banks; revisit only if Kevin supplies or approves public-facing framing. |
| Full internal CVB presentation lists | Inventory only; too bulky for the active bullet bank. |
| Old profile language from 2024 DOCX resumes | Not promoted; current profile bank is sharper and better aligned with the current target clusters. |
| Full coursework / continuing education lists | Reference inventory unless an academic CV or education-heavy role appears. |
| Hack for the Sea details | Added to awards inventory, not active bullet bank. |
| Legacy LaTeX build mechanics | Preserved in archive; not used in the current DOCX/Markdown workflow. |

## Follow-Up Candidates

- Decide whether the generator should support a `presentation_ids` field later. For now, presentations are tracked in `PUBLICATION_PRESENTATION_BANK.md` but not generated directly.
- Consider adding a lightweight `awards_ids` field only if awards start appearing in tailored resumes.
- If an operational/business analytics role appears, prioritize `WWE-06`, `WWE-07`, and `WWE-08` before creating new WWE bullets.
- If a physical-systems forecasting role appears, prioritize `CSTR-07` and the expanded granular-dynamics publication entries.
