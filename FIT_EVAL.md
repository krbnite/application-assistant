# Fit Evaluation

Rules for scoring a job description go / medium / no-go before any packet is built.

**Job Hunt Cycle:** 2026  
**Last Rule Refresh:** 2026-09-12

If the current calendar year is later than the Job Hunt Cycle, do not apply these rules mechanically. On the first JD of the new cycle, ask Kevin whether his evidence base or preferences changed in the areas that most affect scoring:

- new role or job history
- new portfolio projects
- LLM or foundation-model training, fine-tuning, evaluation, or deployment
- C++ / edge / embedded deployment
- 3D vision / graphics / geospatial production work
- cloud, distributed systems, or large-scale data platforms
- bioinformatics, genomics, or molecular-data experience
- management and headcount preference
- location, remote, compensation, and relocation constraints

After refreshing the rules, update both fields above. Do not run this refresh on every role; it is a cycle-start maintenance step.

This file is the screening layer that runs **before** `APPLICATION_WORKFLOW_PROTOCOL.md`. Scoring a JD does not require reading the banks end to end; it requires the filters, tests, and process rules below. Only once a role is greenlit does the workflow protocol take over and select a packet-building mode.

When Kevin pastes a new JD without explicitly asking for a resume, start here: run fit evaluation, give the verdict and notes one-liner, then if the role is a go or conditional go, note the logical next action (e.g., ask whether he wants to discuss the decision or proceed to the resume-first workflow). 

If Kevin explicitly asks to build a resume or packet, use `APPLICATION_WORKFLOW_PROTOCOL.md` directly and treat any prior fit evaluation as context rather than re-litigating the role.

These rules reflect accumulated fit-evaluation work, but the file should stand on its own. Keep examples only when they clarify how to apply a rule; avoid citation-style side notes that require another file to be meaningful.

---

## 1. Order of Operations

Run these in order. Steps 1-3 are cheap and frequently decisive; do not skip them to get to the analysis.

1. **Precedent check.** If prior job folders, notes, or tracking files are available, search them for the company and role family. A prior packet or prior score can change the decision, especially for same-company coordination.
2. **Nearest-precedent comparison.** If prior fit evaluations are available, compare against the closest previously scored role. Scores should stay comparable across the cycle, but the process must still work without a tracking file.
3. **Resolve decision-changing unknowns.** Location, comp band, req status, client identity, career level, or actual modeling substrate. Do not build against an unresolved unknown when the answer could change the verdict, priority, or application target.
4. **Best-role-at-company check.** If the req is junior- or mid-scoped, check the company's job board for a senior version before scoring. Also check for adjacent roles that are a better first target by fit, interest, work mode, or narrative strength. This is the upstream version of the multiple-reqs coordination rule in §2.
5. **Generic-JD research.** If the JD names no concrete techniques, read what the product actually does — product pages, launch announcements, engineering blogs — before scoring. An unspecific JD is missing information, not a soft gate.
6. **Apply the gates and strong cautions (§2), then the structural tests (§3), then score.**
7. **End with a one-line verdict Kevin can paste into his notes (§8).** Logging is optional; do it only when Kevin asks, when it is likely to become an application target, or when the evaluation produced a reusable rule.

### Corollaries

- **The JD text outranks indirect evidence.** Do not use an org chart, a job-board pattern, or a company's positioning to soften an explicitly stated required qualification.
- **Cost of applying is not fit.** Commutability, remoteness, and a cheap packet belong in the *ranking*, never in the verdict.
- **Prior notes are helpful but not required.** Kevin scores roles outside any one session or file. An unfamiliar role name is not evidence it was never assessed — ask rather than treating it as suspect.

---

## 2. Gates and Strong Cautions

Check these before detailed analysis. Some are true hard gates; others are coordination risks that should change sequencing, target selection, or recruiter questions rather than automatically killing a role.

### Headcount ownership and management load
"Directly manage," "hire and retain," "lead and grow a team," "build out the team."

Kevin's stated preference is **technical leadership with light management**, but this is a weighted preference rather than a binary filter. Headcount-heavy roles lower fit and should raise the evidence bar, especially when they make the work less technical. They are not automatic no-go roles when salary, scope, brand, mission, or strategic value compensates.

His record: one official direct report at CVB (~2 years, owned performance management, led the hiring process), two unofficial reports, ~2 additional years as informal team lead, plus one report at WWE for ~6 months.

Score management load as a tradeoff:

- **Light IC leadership:** mentoring, design reviews, technical direction, project leadership. Usually positive.
- **Hybrid technical lead / player-coach:** some people leadership or hiring, while still owning technical work. Mixed; score against comp, seniority, and whether the role preserves hands-on technical depth.
- **Headcount-primary management:** direct management, performance reviews, hiring/retention, roadmap ownership through others. Lowers fit substantially unless the package or opportunity is unusually strong.
- **Director-plus org building:** usually a poor fit unless Kevin explicitly wants that tradeoff for the specific role.

- **Refinement — check the stated career level first.** "Lead and mentor a team" at an IC track level is technical leadership, not headcount, and is his preferred shape. The filter should only fire on TLM/Manager/Director reqs.

### Active security clearance
Filter **only** on clearance required at start.

- "Minimum of a Secret Clearance is required," "Minimum Clearance Required to Start: Top Secret" → **hard gate**. Clearances cannot be self-obtained.
- "Ability to obtain," "eligibility for U.S. security clearance" → **not a gate**. That is sponsorship; a US citizen with clean history is processed while working unclassified and the employer absorbs the timeline.
- Drug-testing and QNSP conditions attach to sponsored roles and are Kevin's call, not a scoring input.

### Platform engineering
Cloud-service enumeration, Kubernetes, vector stores, Spark/Flink, developer tooling, "reusable platform capabilities," build systems, engineering workflows.

Fires on **substance**, not just surface signals — a simulation-platform role with no cloud-service list can still trip it. Treat infrastructure terms as a scrutiny trigger, not an automatic rejection: the gate fires when platform building is the main job rather than support for model quality, evaluation, or scientific validation. Watch for JDs that explicitly disavow the research profile ("shipping production-quality engineering systems rather than research prototypes").

### 3D and graphics vision
3D reconstruction, multi-view geometry, point clouds, meshes, SLAM, NeRF, procedural modeling, pose and correspondence, volumetric analysis, lidar-centered autonomy or reconstruction.

Kevin's CV evidence is categorically 2D: POD-05 thermal segmentation and keypoint extraction, POD-08 frame-level localization, MSG-01 self-supervised video, WWE-05 VGG16 fine-tuning.

Lidar by itself is not a hard gate when it appears as one environmental or geospatial data source. It becomes a gate when 3D reconstruction, autonomy perception, or lidar geometry is the role's core.

### Causal-inference-led roles
Roles where formal causal inference is the core method rather than a supporting tool. POD-10 supplies quasi-experimental language, but the Measurement Science cluster's do-not-overstate line on DiD, IV, and propensity-score matching holds.

### Multiple reqs at one company
Multiple applications to one company can be fine when the roles are clearly distinct, the applications are spaced out, or a recruiter is coordinating the process. The risk is **uncoordinated duplication**: same-week submissions to adjacent teams, conflicting narratives, or a weaker req defining Kevin internally before the stronger req is reviewed.

Use this as a sequencing rule, not a blanket veto:

- If one req is clearly strongest, apply to that one first.
- If a second req is genuinely different and strong, wait until the first process has either moved forward, gone quiet, or produced a recruiter contact who can advise.
- If a recruiter conversation opens, mention adjacent roles and ask where Kevin should be routed.
- Do not let a low-fit or lower-level req dilute a high-fit packet at the same company.

### Agency submission without a client name
Contingency submission attaches a placement fee to Kevin's candidacy and can make him more expensive than an identical direct applicant. **Obtain the client name before authorizing any submission**, and never let an agency submit somewhere he might apply directly. Prefer applying direct when the client is identifiable.

---

## 3. The Two Structural Tests

These decide the cases where the domain looks right but the role is wrong. Apply both.

### Overlay or core?

**Is the unfamiliar thing an overlay on a core Kevin owns, or is it the core?**

| Role | Unfamiliar thing | Core | Verdict |
|---|---|---|---|
| Waymo Weather | terrestrial meteorology | measurement rigor + spatiotemporal inference | overlay → **GO** |
| Overstory | Earth-observation craft, fire science | validation methodology, uncertainty quantification | overlay → **soft go** |
| Tubi | recommender systems | recommender systems | core → **NO-GO** |
| PNNL GEOINT | hyperspectral LWIR + SAR physics | hyperspectral LWIR + SAR physics | core → **NO-GO** |
| Samsara Edge AI | edge model optimization | edge model optimization | core → **NO-GO** |

A domain gap sitting on top of a methodological core Kevin owns is learnable and often forgiven. A domain gap that *is* the technical core is not.

### Build or deploy?

The edge/CV space splits in two, and only one half is Kevin's. **Screen on the verb, not the noun.**

- **BUILD** — design, train, validate, adapt from papers, run ablations, error-analyze, select architectures. **His.**
- **DEPLOY** — optimize, quantize, prune, serve, integrate onto constrained hardware. Triton, TensorRT, ONNX Runtime, Jetson, ROS2, driver integration. **Not his**, and roughly a year to acquire.

Both halves say "computer vision" and both say "edge." They are different jobs.

---

## 4. Keyword Meaning Checks

Some terms name genuine strengths for Kevin, but adjacent hiring markets may use the same words to mean different technical work. Use this section to check what the JD means before scoring. These are **weighted evidence and interpretation warnings**, not automatic blockers; they become negative only when the market meaning is central to the role and Kevin's meaning is merely adjacent.

| Term | Kevin's meaning | Alternate meaning to check for |
|---|---|---|
| **validation** | statistical / scientific model validation | hardware and systems QA |
| **computer vision** | 2D medical and scientific imaging | 3D reconstruction, graphics, AR/VR, autonomy |
| **simulation** | physics-informed scientific simulation | physics engines, robotics sim, digital twins |
| **signal processing** | biosignal and geophysical | RF, comms, DSP hardware |
| **remote sensing** | space-facing — solar wind, magnetosphere, ionosphere | earth-facing and adversarial — ground emissivity, radar backscatter, atmospheric correction |
| **multi-modal** | sensor modalities — IMU, PPG, thermal, video | biological modalities — genomic, transcriptomic, proteomic |
| **biomarker** | digital and behavioral | molecular, predicting drug response |
| **cold start** | sensor / patient — new device or patient, no history | user / item — sparse categorical embeddings, huge vocabularies |

**Altitude, not just modality.** "Computer vision" can diverge two ways that compound: wrong *modality* (2D vs 3D) and wrong *altitude* — Kevin is a practitioner who ships production CV inside a broader sensor practice, while some senior CV reqs want a recognized domain authority with conference-venue standing.

**Check which way the sensor points.** "Remote sensing" in a title should not automatically trigger a favorable prior. Kevin's remote-sensing credibility is real, but it is heliophysical. Earth-observation roles can still be good fits when the core is spatiotemporal inference, uncertainty, or validation; they become weaker when the core is satellite-image production craft, SAR/LWIR instrument physics, atmospheric correction, or GIS operations. The honest pitch is never "I have worked with satellite imagery"; it is *"I infer physical state from indirect, distributed, noisy observations across instrument networks, and I build the validation methodology that proves those inferences hold."*

---

## 5. Recurring Blockers

Ranked by observed frequency across the 2026 cycle.

1. **Production LLM / foundation-model experience** (~10 roles). See the three-rung ladder below.
2. **Distributed compute and cloud data platforms** (~7): Spark, Ray, Databricks, Snowflake, Azure ML, Flink.
3. **C++** (~7): CACI, Parallel Domain, Slingshot, Greylock, NBCU, D-Wave, Samsara Edge AI.
4. **3D geometry** (~5). See §2.
5. **Speech / ASR** (~3): Cresta, Cerence, Canals.
6. **Vision transformers, VLMs, and vision foundation models** (~3): Buzz, HavocAI, Tubi-adjacent.

### The three-rung LLM ladder

The single most useful calibration in the cycle. Locate every LLM requirement on one of these rungs before scoring it.

1. **UNDERSTAND** — "practical and theoretical understanding of LLMs or other foundation models." **Kevin clears this.** ProblemForm, the MCP pipeline work, application-assistant, TRAIN-03, and the pretrain-then-adapt lineage in CVB-11 and PUB-13. Do not score this as a miss.
2. **ADAPT** — demonstrated hands-on LoRA/PEFT fine-tuning, knowledge distillation, transformer architecture depth. **Does not clear today.**
3. **TRAIN** — training large models from scratch, owning optimizer and scheduler choices, debugging divergence at scale. **Far beyond**, and no solo project will buy it.

**Generative-system evaluation is the door.** Across Snorkel, Atlassian, Cresta, and Yahoo, the one LLM-adjacent requirement Kevin can genuinely touch is evaluation — rubric design, LLM-as-judge, property-based evaluation. That is consistently his entry point into LLM work.

### C++ — escalation note

Originally priced as an unlock for defense R&D and simulation, two "physics is the qualification" sectors. Two developments complicate that:

- It has now appeared as a **minimum requirement inside the IOT cluster** (Samsara Edge AI, remote, $178.6-319k). The wall is no longer only outside his strongest lane.
- But the two defense-lane roles scored since the clearance filter was corrected (PNNL, HavocAI) died on *other* grounds — instrument physics and embedded deployment craft. **C++ alone would not have unlocked either.** Lowering the clearance wall revealed a second wall behind it.

Net: still cheap (he has C and the numerical-computing instincts; modern C++ is weeks for basic credibility, though longer for production-grade C++ judgment), but worth less as a lane-opener than first estimated.

---

## 6. Low-ROI Sectors and Open Lanes

### Currently low-ROI

- **Consumer-internet personalization.** Recommendations, search ranking, feed ranking, ads optimization at consumer scale. One specialty, effectively closed absent a deliberate multi-year pivot. Screen on JD title plus employer type — "ML Engineer" or "Applied Scientist" at a streaming, social, marketplace, e-commerce, or adtech company. **A small project cannot close this**, unlike the LLM-evaluation gap.
- **Edge / embedded deployment engineering.** See the build-vs-deploy test. This is a current gap, not a permanent identity claim: modern C++ plus a serious edge deployment project could change the evaluation, but it should not be treated as already covered.

### Watch

- **"Machine Learning Engineer" at B2B business-software companies** has often resolved to document AI, LLM agents, or conventional production engineering. Treat the title as uninformative at this company type and go straight to the product.

### Open — and consistently under-targeted

- **ML evaluation and model quality.** Kevin's strongest differentiator and his door into LLM work.
- **Environmental modeling for operational decision-making.** Spatiotemporal inference on sparse noisy environmental data plus the validation rigor to prove the estimates hold. Extends to aviation, energy, insurance, agriculture, logistics.
- **2D operational and industrial computer vision.** Detection, segmentation, tracking, anomaly detection, edge inference, in industrial, inspection, manufacturing, and OT settings. POD-05 is directly on point and the 3D filter does not fire. Search the industrial/inspection shape, not the bare term "computer vision."
- **Thermal sensing specifically.** POD-09 (physics-informed thermal modeling, Newtonian heat transfer, synthetic thermogram generation) plus POD-05 make thermal his single most literal domain match. Standing watch on thermal/LWIR reqs in simulation, inspection, grid, health, and industrial-sensing contexts.

---


## 7. Current-Cycle Prep Signals

Track recurring gaps that affect multiple otherwise-good roles. Treat this as a current-cycle planning aid, not a permanent ranking. See when document was last updated in the header.


1. **Survival / reliability analysis** — ~1 weekend. Closes the single named gap in Fleetio, the highest-probability role.
2. **Promote ProblemForm, application-assistant, and the MCP pipeline project into `RESUME_BULLET_BANK.md`** with proper IDs and cluster scores. ~1 day. They currently exist only as candidate language in `RESUME_TAILORING_AGENT.md`. This closes part of the *perceived* LLM gap with capability Kevin already has, and improves every packet built afterward.
3. **LLM-evaluation credibility** via extending ProblemForm with judge-vs-human agreement, position and verbosity bias, a small benchmark. 2-4 weekends.
4. **nnU-Net / MONAI** — ~2 weekends. Opens the imaging branch of HWD.
5. **Modern C++** — weeks. See the escalation note above; worth less than first priced.
6. **Geometric deep learning** — 3-6 months. What Kevin actually wants; connects to his mathematical-physics roots.
7. **Diffusion / image generation** — months. Most competitive, furthest from existing evidence, lowest ROI.

---

## 8. Output Format

Every fit evaluation produces two things.

**1. Full analysis** — verdict, the gates that fired, honest gaps named specifically, what genuinely clears, ranking against the current queue, and any decision-changing unknown to resolve before building.

**2. A short, pastable verdict for Kevin's notes**, covering: verdict, comp and location when known, the deciding gate(s), the strongest genuine hits, and any required pre-action. Kevin pastes this directly.

When Kevin wants a durable record, log the full entry wherever the current job-search tracker lives. Use a clear `Company - Role - VERDICT` heading, and note what the entry is logged *for* when it produced a reusable rule.

### Scoring vocabulary

| Verdict | Meaning |
|---|---|
| **STRONG GO** | Build-list tier. Clears the required list; gaps are overlays. |
| **GO** | Build list, with a named risk. |
| **MEDIUM / SOFT GO** | Worth a low-cost direct application; not worth a tailored packet ahead of the build list. |
| **MEDIUM / CONDITIONAL** | One or two cheaply resolvable unknowns stand between this and a real verdict. Name the questions. |
| **NO-GO** | A hard gate fires, the domain gap is the core (subject-matter mismatch), or the core craft is outside Kevin's current evidence base (role-practice mismatch). |

When maintaining a tracker, log instructive NO-GOs. Several of the most useful rules in this file came from roles Kevin will never apply to.

---

## 9. Revision Discipline

- Hold a position under pushback unless a specific argument warrants updating, and **name what moved it**. Incredulity alone is not an argument — but re-examine honestly before answering, because the flaw is sometimes real.
- When a verdict is revised and a durable tracker exists, record the revision *and the reasoning error*, not just the new score.
- Cross-model checks (ChatGPT, Codex) are useful and have produced genuine finds — the Tristar AI client identification among them. They are working without repo access, so they cannot see prior packets, prior scores, or same-day corrections. Weight their JD analysis; supply the repo context they lack.
- State confidence and falsification conditions on significant claims.

---

*Derived from accumulated 2026 role evaluations. Keep this file concise and self-contained; use role logs only for deeper audits or disputed decisions.*
