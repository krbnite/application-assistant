# Resume Bullet Bank

This file is the canonical evidence reservoir for tailored resumes. It tags Kevin's reusable resume bullets by archetype so tailored resumes can be created quickly and consistently from `MASTER_RESUME_TEMPLATE.md`.

Use this as guidance, not a mechanical scoring system. A high score means "usually lead with this bullet for this cluster." A lower score means "use only when the JD specifically asks for it or when page budget allows."

## Cluster Codes

- `HWD`: Health, Wearables, Neurotech, And Digital Biomarkers.
- `SAR`: Sensor AI, Robotics, Autonomy, And Edge Perception.
- `BSP`: Bayesian Estimation, Signal Processing, And Physical Systems Research.
- `IOT`: Industrial And Operational Time-Series ML.
- `CLP`: Closed-Loop Physical AI And Self-Learning Systems.

## Score Meaning

- `3`: Lead evidence for this cluster.
- `2`: Strong supporting evidence.
- `1`: Optional or context-dependent.
- `0`: Usually omit or compress heavily.

## Use Rules

- Start with the JD archetype's core signals, then use this bank to choose bullets.
- Prefer bullets scored `3` in the primary cluster, but do not keep all of them automatically.
- Borrow `2` or `3` bullets from a secondary cluster when the JD clearly blends clusters.
- Drop even high-scoring bullets when they are redundant, too detailed, or not needed for the three-page target.
- Create new bullets rarely. When a new bullet is created for a role, record it in the audit and decide whether to add it here as `provisional`.
- Do not invent evidence. Rewrite, merge, or split only from known master-resume material unless Kevin supplies new facts.
- Broad and detailed variants serve different audiences. Prefer broad wording for scientific/modeling roles; use implementation detail when software ownership, reproducibility, research computing, or engineering standards are central. Select one version of the same accomplishment and avoid repeating it through overlapping IDs. Evidence notes are tailoring guidance, not resume text.

## Core Research Theme Bullets

| ID | Bullet | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| CORE-01 | Sensor inference under uncertainty | 3 | 3 | 3 | 2 | 3 | Usually keep. It is the broadest bridge across clusters. |
| CORE-02 | Time-series and spatiotemporal ML | 3 | 2 | 3 | 3 | 2 | Usually keep unless the JD is purely product/leadership. |
| CORE-03 | Computer vision and thermal imaging | 3 | 3 | 2 | 2 | 2 | Lead for CV, sensor, edge, and medical imaging roles; compress for non-CV roles. |
| CORE-04 | Simulation and synthetic data | 2 | 2 | 3 | 1 | 3 | Lead for physical systems, closed-loop, simulation, synthetic-data, or sparse-observation roles. |
| CORE-05 | Research-to-product translation | 3 | 2 | 2 | 3 | 3 | Usually keep for startups, productized ML, regulated systems, and senior roles. |
| CORE-06 | Deployment-honest validation | 3 | 3 | 3 | 3 | 3 | Usually keep. Strong cross-cluster differentiator. |

## Podimetrics

| ID | Bullet | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| POD-01 | On-device fall-risk estimation | 3 | 3 | 2 | 2 | 3 | Lead for edge, embedded, estimation, health, and closed-loop-ish roles. |
| POD-02 | Robust estimator validation | 3 | 2 | 3 | 3 | 3 | Lead for validation, uncertainty, deployment, drift, and sparse/noisy data. |
| POD-03 | Adaptive fall-risk monitoring | 3 | 1 | 2 | 3 | 3 | Lead for longitudinal monitoring, personalized baselines, operational alerts, and adaptive systems. |
| POD-04 | Adaptive alert logic | 3 | 1 | 2 | 3 | 3 | Strong for health decisioning, alerting, production monitoring, and action-under-uncertainty. |
| POD-05 | Production thermal CV and signal-processing pipeline | 3 | 3 | 2 | 2 | 2 | Lead for computer vision, medical device algorithms, production CV, and sensor perception. |
| POD-06 | SmartMat+ thermal algorithm adaptation | 3 | 2 | 2 | 3 | 2 | Strong for transfer/tuning, hardware variation, product deployment, and production diagnostics. |
| POD-07 | Personalized DFU detection prototype | 3 | 1 | 2 | 1 | 2 | Use for clinical personalization, biomarkers, baselines, or adaptive detection; often compress. |
| POD-08 | Framewise foot tracking prototype | 2 | 3 | 2 | 1 | 2 | Use for tracking, segmentation, sequence imaging, and perception roles. |
| POD-09 | Physics-informed thermal modeling | 3 | 2 | 3 | 1 | 3 | Lead for physical modeling, synthetic data, simulation, and scientific ML. |
| POD-10 | Next Best Action analytics | 2 | 0 | 0 | 3 | 1 | Lead for digital health decisioning, intervention analytics, operations, or A/B testing; omit for pure sensor research. |
| POD-11 | Cross-functional technical leadership | 3 | 2 | 2 | 3 | 3 | Keep for senior, lead, startup, regulated, or cross-functional roles. |
| POD-12 | Production scan-pipeline ownership and QC integration | 2 | 2 | 1 | 3 | 2 | Prefer over POD-05 for scientific software leadership, production code ownership, refactoring, and external-module integration; avoid repeating the same pipeline accomplishment in both. |
| POD-13 | Event-driven AWS thermal pipeline | 3 | 3 | 1 | 3 | 2 | Use for AWS/event-driven production pipelines, edge-to-cloud systems, model/API outputs, downstream tools, and provider communications. |
| POD-14 | SmartMat+ edge-to-cloud estimator outputs | 3 | 3 | 2 | 2 | 3 | Use for edge inference, telemetry-backed cloud outputs, sensor-product jobs, and embedded-to-cloud ML framing. |
| POD-15 | PR-triggered pipeline sandbox validation | 2 | 2 | 1 | 3 | 2 | Supporting evidence for isolated integration testing, GitHub Actions, and version-controlled pipeline configuration. Do not claim Terraform authoring or infrastructure ownership. |

## Cohen Veterans Bioscience

In separate-role mode, default placement matters because CVB has three title/date buckets. Use the placement below unless a bullet genuinely spans titles, and explain overrides in final notes or the requested audit. In optional grouped mode, put ordered company-wide CVB bullets in `experience.cvb_grouped` instead; the generator retains all three official title/date lines without assigning each bullet to a specific period. See the tailoring guide for layout selection.

- `cvb_director`: `CVB-01` to `CVB-06`, plus `CVB-17` when research-ops/team-enablement work is relevant.
- `cvb_associate_director`: `CVB-07`, `CVB-08`, `CVB-10` to `CVB-12`, `CVB-20`, plus `CVB-18` when knowledge-graph/database work is relevant and the resume benefits from grouping the late Senior Data Scientist / early Associate Director transition platform work with the Associate Director sensor-analytics story. `CVB-09` may be placed here only when the resume benefits from grouping late Senior Data Scientist / early Sensor Analytics transition work with the Associate Director sensor-analytics story.
- `cvb_senior_ds`: `CVB-09`, `CVB-13` to `CVB-16`, `CVB-18`, `CVB-19`. `CVB-09` defaults here because the sampling-rate ablation work occurred in Kevin's final months as Senior Data Scientist. `CVB-18` is a legitimate spanning/transition bullet: the dated EaSiEco/knowledge-graph/database materials are concentrated in the 2018-2019 Senior Data Scientist period, but some work continued into the first several Associate Director months.
- `CVB-21` (SensorNet) belongs with the Sensor Analytics team work; `CVB-22` (cloud tooling) combines an early EC2 setup with later team tooling; `CVB-23` (code/pipeline review) describes work across projects. Exact title boundaries for these newly supplied facts are not established. Use a combined CVB entry when appropriate, or confirm placement before assigning a narrow title/date bucket.

| ID | Bullet | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| CVB-01 | Technical leadership and mentorship | 3 | 1 | 1 | 2 | 1 | Keep for lead/principal roles; compress for individual-contributor research roles. |
| CVB-02 | Program leadership | 3 | 0 | 0 | 1 | 0 | Use for leadership, grants, nonprofit/research orgs, or Motif-like roadmap roles. |
| CVB-03 | Wearable study design and evaluation | 3 | 1 | 2 | 1 | 1 | Lead for clinical study design, validation, sensor synchronization, and free-living data. |
| CVB-04 | Sleep sensor validation | 3 | 1 | 2 | 0 | 0 | Use for wearable validation, sleep, biosignals, DTW, or measurement mismatch. |
| CVB-05 | Parkinson's research leadership | 3 | 1 | 1 | 1 | 0 | Lead for health/neuro roles; compress for non-health roles. |
| CVB-06 | Multimodal wearable data processing | 3 | 1 | 1 | 2 | 1 | Use for data infrastructure, longitudinal data, queryable datasets, and pipeline roles. |
| CVB-07 | Parkinson's digital biomarkers | 3 | 1 | 1 | 1 | 0 | Lead for digital biomarkers, neurotech, Parkinson's, grants, and wearable health. |
| CVB-08 | Free-living Parkinson's monitoring | 3 | 2 | 1 | 1 | 0 | Strong for weak supervision, wearable ML, gait, and real-world sensor classification. |
| CVB-09 | Wearable gesture recognition | 3 | 2 | 2 | 1 | 1 | Strong for IMUs, activity recognition, ablations, signal processing, and wearable algorithms. Default to Senior Data Scientist; optionally place in Associate Director only when grouping late-Sr-DS / early-Sensor-Analytics transition work improves the resume. |
| CVB-10 | End-to-end biosignal modeling | 3 | 1 | 2 | 1 | 0 | Use for biosignal ML, deep sequence models, ablations, and replacing classical pipelines. |
| CVB-11 | Cross-domain representation learning | 3 | 2 | 2 | 0 | 1 | Use when transfer/domain adaptation, shared representations, DRCN/autoencoders, patient-level personalization, or general-to-subject adaptation is called out. |
| CVB-12 | Weakly supervised learning | 2 | 2 | 1 | 1 | 0 | Use for unlabeled data, weak supervision, activity detection, and real-world model framing. |
| CVB-13 | Research strategy | 2 | 0 | 0 | 1 | 0 | Use for senior judgment, feasibility, data strategy, or executive communication; avoid if space is tight. |
| CVB-14 | Clinician-friendly machine learning | 3 | 0 | 1 | 2 | 0 | Use for interpretable ML, clinical stakeholders, EHR risk, and skeptical audiences. |
| CVB-15 | Deployment-honest validation | 3 | 1 | 2 | 2 | 2 | Strong for leakage, time-ordering bias, LOSO validation, and small-cohort rigor. |
| CVB-16 | Early-term birth prediction | 2 | 0 | 1 | 1 | 0 | Usually omit unless maternal health, EEG-derived clinical features, missing data, clinical ML, or leakage detection is relevant. |
| CVB-17 | Reproducible team workflows and tooling | 1 | 0 | 1 | 2 | 1 | Use for lead, platform-minded, research-ops, or team enablement roles; otherwise compress. |
| CVB-18 | Wearables knowledge graph and database evaluation | 2 | 0 | 1 | 2 | 1 | Use for knowledge graphs, databases, schema design, wearable-to-biology mapping, or ontology-ish roles. |
| CVB-19 | Sensor-driven questionnaire estimation | 3 | 1 | 2 | 1 | 2 | Lead for passive sensing, mental health, clinic-assessment proxy modeling, patient-state estimation, and strategic pivot from unsupported wearable-suicide prediction asks. |
| CVB-20 | Biosignal ablation leadership variant | 3 | 1 | 2 | 1 | 1 | Variant of CVB-10 for staff, lead, manager, or principal roles where experiment design, delegation, and team direction matter; usually choose either CVB-10 or CVB-20, not both. |
| CVB-21 | SensorNet reusable biosignal modeling package | 3 | 2 | 2 | 2 | 2 | Lead for scientific software, reusable ML libraries, configurable model APIs, time-series tooling, and reproducibility. Complement CVB-10/20 only if software design and modeling results each earn separate space. |
| CVB-22 | AWS research-computing access and workflow tooling | 2 | 1 | 2 | 2 | 1 | Concrete computing-focused alternative to broad CVB-17; use for Linux/AWS environments, IAM role assumption, synchronization, and team enablement. Usually choose one of CVB-17/22. |
| CVB-23 | Cross-project scientific code and leakage review | 3 | 1 | 2 | 2 | 2 | Use for scientific software quality, peer code review, and validation standards. Distinguish recurring cross-project review from the specific CVB-15 validation redesign; avoid redundant leakage bullets. |

## WWE

| ID | Bullet | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| WWE-01 | Production viewership data products | 0 | 0 | 0 | 3 | 0 | Use for production data products, dashboards, business impact, and pipeline ownership. |
| WWE-02 | Real-time executive analytics | 0 | 0 | 0 | 2 | 0 | Use for operational dashboards, live decisions, and stakeholder-facing analytics. |
| WWE-03 | Production customer behavior analytics | 1 | 0 | 0 | 3 | 0 | Use for segmentation, churn, A/B testing, and automated ML/reporting pipelines. |
| WWE-04 | Deep learning for churn prediction | 0 | 0 | 0 | 2 | 0 | Use for applied ML performance gains; usually compress behind newer sensor work. |
| WWE-05 | Transfer learning and fine-tuning for computer vision | 1 | 3 | 1 | 0 | 0 | Use as optional evidence when the JD asks for transfer learning, fine-tuning, pretrained-model adaptation, computer vision, or small-data model diagnostics. |
| WWE-06 | YouTube and social-platform data remediation | 0 | 0 | 0 | 3 | 0 | Lead for data engineering, API integration, vendor-gap discovery, stakeholder persuasion, and operational analytics. |
| WWE-07 | Live-event analytics latency reduction | 0 | 0 | 0 | 3 | 0 | Use for real-time dashboards, executive analytics, streaming/live operations, or latency-sensitive reporting. |
| WWE-08 | Revenue attribution and behavioral research | 0 | 0 | 0 | 2 | 0 | Use for attribution, survey fusion, sentiment analysis, customer behavior, or business analytics roles. |
| WWE-09 | AWS automated scoring to Redshift | 0 | 0 | 0 | 3 | 0 | Use for automated model scoring, warehouse/dashboard consumption, AWS pipelines, and stakeholder-facing ML outputs. |
| WWE-10 | Streaming-account anomaly and enforcement investigation | 0 | 0 | 0 | 3 | 0 | Lead for investigative analytics, anomaly detection, fraud-adjacent work, SQL validation, visualization, and challenging operational assumptions. Do not imply established user intent or include an unverified settlement amount. |
| WWE-11 | Shared GPU-enabled AWS/Linux research environment | 1 | 1 | 2 | 2 | 1 | Use for scientific computing, shared GPU/Linux administration, researcher support, and scheduled data workloads. Single-instance experience; do not label as cluster/distributed HPC. |
| WWE-12 | Reusable R ingestion-to-reporting package | 1 | 0 | 2 | 3 | 1 | Lead for reusable packages, automated analysis/reporting, maintainability, and consultant handoff. HTML reports are not evidence of web-application ownership. |

## MachineSaidGo / Independent Research Projects

MachineSaidGo is Kevin's LLC / exploratory side-project umbrella. Do not place it in the main chronological Experience section by default because it can complicate the CVB timeline. Use `project_ids` and a compact `Selected Research Projects` section only when the JD specifically rewards self-supervised video, computer vision, behavioral analysis, scientific simulation, surrogate modeling, consulting/startup initiative, or independent R&D.

| ID | Project | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| MSG-01 | Self-supervised behavioral video analysis | 1 | 3 | 1 | 0 | 1 | Optional project signal for computer vision, behavioral analysis, biotech/animal-behavior research, self-supervised learning, anomaly detection, or video-based sensing roles. |
| MSG-02 | Granular-dynamics surrogate modeling | 0 | 1 | 3 | 0 | 2 | Optional project signal for scientific ML, surrogate modeling, simulation acceleration, nonlinear dynamics, physics-informed ML, and physics/modeling roles. |

## Center For Solar-Terrestrial Research

| ID | Bullet | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| CSTR-01 | Polar-cap representation inference | 0 | 1 | 3 | 1 | 1 | Lead for signal processing, geophysics, spectral/time-frequency methods, representation inference, or physical systems. |
| CSTR-02 | Magnetic-coordinate validation | 0 | 1 | 3 | 0 | 0 | Lead for geophysical/spatial inference, hidden-structure inference, and representation validation; omit for most health or industrial roles. |
| CSTR-03 | Geophysical signal interpretation | 0 | 1 | 3 | 1 | 1 | Use for physical inference, disentangling confounds, and noisy indirect observations. |
| CSTR-04 | Multi-instrument space weather reconstruction | 0 | 2 | 3 | 0 | 1 | Lead for sensor networks, fusion, reconstruction, visualization, or space/weather roles. |
| CSTR-05 | Scientific collaboration | 0 | 1 | 2 | 0 | 0 | Use for research teams, NASA/mission credibility, talks, and scientific collaboration. |
| CSTR-06 | Computational mathematics, granular fluids, and nonlinear dynamics | 0 | 0 | 3 | 0 | 2 | Use for mathematical modeling, simulation, dynamics, and physical AI; usually compress. |
| CSTR-07 | Solar-wind forecasting and inverse nowcasting | 0 | 1 | 3 | 1 | 2 | Use for forecasting, inverse problems, remote sensing, physical systems, and sensor-network inference. |

## Internships

| ID | Bullet | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| INT-01 | JPL trajectory optimization and design | 0 | 1 | 2 | 0 | 1 | Use when expanded internship detail helps aerospace, robotics/autonomy, optimization, physical-systems, or mission-oriented roles. |
| INT-02 | NASA Goddard Heliophysics Division | 0 | 0 | 1 | 0 | 0 | Use only when expanded early software/NASA detail is strategically useful. |
| INT-03 | NASA Goddard Observational Cosmology Laboratory | 0 | 0 | 1 | 0 | 0 | Use only when expanded spacecraft-instrument or cosmology software detail is strategically useful. |
| INT-04 | NASA/JPL research internship signal | 1 | 1 | 1 | 0 | 0 | Default compact brand/research signal when page budget allows; omit only under meaningful page pressure or if early-career detail would distract. |

## Skills Lines

| ID | Skill line | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| SKILL-01 | Machine learning | 3 | 3 | 2 | 2 | 2 | Keep but reorder terms to mirror the JD. |
| SKILL-02 | Statistical signal processing and estimation | 3 | 3 | 3 | 3 | 3 | Usually keep. This is a signature differentiator. |
| SKILL-03 | Sensor analytics and modalities | 3 | 3 | 3 | 2 | 2 | Keep for nearly all target roles; trim modalities irrelevant to the JD only if needed. |
| SKILL-04 | Languages and tools | 2 | 2 | 2 | 3 | 2 | Keep concise; do not overclaim depth in tools only lightly represented. Do not present C++ as professional experience; Kevin has C++ coursework and code-reading literacy, not professional C++ development. |

## Training / Certifications

These are optional keyword and storyline signals. Use `training_ids` only when a role or application form specifically benefits from certification/training evidence; do not create a default resume section just to bulk up the document.

| ID | Training | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| TRAIN-01 | Deep Learning Nanodegree | 1 | 1 | 0 | 0 | 0 | Use sparingly for deep-learning timeline, credibility, and gatekeeper-heavy roles where formal DL training helps support older project evidence. |
| TRAIN-02 | Intel IoT Edge AI Scholarship | 1 | 2 | 0 | 1 | 1 | Use for edge AI, IoT, sensor-device, embedded, and on-device inference roles; usually omit from pure research resumes. |
| TRAIN-03 | Building with the Claude API | 1 | 1 | 0 | 1 | 0 | Use for GenAI, agentic workflow, LLM API, AI-product, or application-form screenings when lightweight formal evidence helps; do not overstate as deep LLM research experience. |
| TRAIN-04 | Tableau 9 Essential Training | 0 | 0 | 0 | 1 | 0 | Generally omit; use only when dashboarding, BI, or Tableau is explicitly requested and page budget is loose. |

## Publications

| ID | Publication | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| PUB-01 | Sensors 2022 Parkinson's disease wearable monitoring | 3 | 1 | 1 | 0 | 0 | Lead publication for health, wearables, neurotech, and digital biomarkers. |
| PUB-02 | JGR Space Physics 2016 polar-cap / ULF power | 0 | 1 | 3 | 0 | 1 | Lead publication for geophysics, physical systems, Bayesian/signal-processing roles. |
| PUB-03 | Physica D 2014 nonlinear dynamics / simulations | 0 | 0 | 2 | 0 | 1 | Use for mathematical modeling, simulation, and physical dynamics. |
| PUB-04 | Planetary and Space Science 2013 JPL mission design | 0 | 1 | 1 | 0 | 0 | Use for aerospace, mission, or systems-design relevance. |
| PUB-05 | Space Weather 2011 open-closed boundary | 0 | 0 | 2 | 0 | 0 | Use for space-weather and geophysical roles; otherwise omit. |
| PUB-06 | Powders and Grains 2013 granular column dynamics | 0 | 0 | 2 | 0 | 1 | Use for physical simulation, granular dynamics, and mathematical modeling roles. |
| PUB-07 | JOMMS 2011 tapping dynamics | 0 | 0 | 2 | 0 | 1 | Use for nonlinear dynamics, simulations, and computational mechanics roles. |
| PUB-08 | Condensed Matter Physics 2010 fractional fields | 0 | 0 | 2 | 0 | 1 | Use only for mathematically oriented modeling roles. |
| PUB-09 | CVB 2020 wearable digital-biomarker science article | 3 | 0 | 0 | 0 | 0 | Public science writing, not peer-reviewed. Lead for Oura-style wearable health science communication. |
| PUB-10 | Biological Psychiatry 2020 wearable/home sleep-sensor verification poster | 3 | 0 | 1 | 0 | 0 | Conference abstract/poster, not a full journal article. Lead for sleep, wearable validation, and home-sensor verification roles. |
| PUB-11 | Bounded DTW sleep-device validation methods manuscript | 3 | 0 | 2 | 0 | 0 | Manuscript in preparation / unpublished. Lead for sleep validation, PSG-device comparison, signal alignment, and methods-heavy wearable roles. |
| PUB-12 | Sleep apnea deep learning and domain-expertise working paper | 3 | 0 | 2 | 0 | 0 | Working paper / unpublished. Lead for EEG/sleep, biosignal ML, ablations, and classical-to-deep-model comparison roles. |
| PUB-13 | Augmented unsupervised domain adaptation working paper | 3 | 2 | 2 | 0 | 1 | Working paper / unpublished. Lead for transfer learning, domain adaptation, shared representations, patient-level adaptation, and deep time-series roles. |
| PUB-14 | APS DFD 2022 tapped granular systems ML presentation | 0 | 1 | 3 | 0 | 2 | Conference abstract / oral presentation, not peer-reviewed. Use for recent physics-informed ML, RNN forecasting, surrogate modeling, granular microstructure, and nonlinear physical systems. |

## Awards

Awards are optional credibility signals. Use `award_ids` only when a role benefits from leadership, program-delivery, funding, presentation, or CV-like evidence; do not include them by default when stronger technical evidence needs the space.

| ID | Award | HWD | SAR | BSP | IOT | CLP | Use / cut guidance |
|---|---|---:|---:|---:|---:|---:|---|
| AWARD-01 | CVB 2023 Milestone Achievement Awards | 1 | 0 | 0 | 1 | 0 | Use sparingly for senior leadership, program-delivery, grant/funding, or CV-like profiles; usually omit from ordinary technical resumes. |

## Canonical Text

The generator uses this section for exact bullet, project, skill, internship, training, publication, and award text. Keep IDs synchronized with the tables above. Plain entries remain a single paragraph. Entries needing internal context use `#### Resume text` plus optional `#### Evidence`, `#### Boundaries`, `#### Selection`, or `#### Variant: name` sections. Only Resume text is emitted by default; notes are never resume text. Select a named variant in a plan with `{"id": "POD-06", "variant": "implementation"}` or `{"id": "WWE-02", "variant": "detailed"}`. A variant and a custom `text` override are mutually exclusive. Keep each resume text or variant to one paragraph. Do not add unmarked paragraphs; the generator rejects ambiguous content. Short selection guidance already covered by the scoring table should stay there; entry-specific explanations may remain alongside the entry without duplicating the table.

### CORE-01: Sensor inference under uncertainty

Designed Bayesian, streaming, and adaptive estimators for indirect physiological and physical measurements where uncertainty, drift, irregular sampling, and hardware artifacts are central rather than incidental.

### CORE-02: Time-series and spatiotemporal ML

Built sequence models, weakly supervised wearable pipelines, spectral/time-frequency methods, DTW validation frameworks, and spatiotemporal representations across biosignal, thermal, image, and geophysical data.

### CORE-03: Computer vision and thermal imaging

Developed and stabilized thermal computer-vision workflows for 17-frame thermogram scans, including foot localization, left/right classification, segmentation masks, background removal, scan-quality handling, and anatomical keypoint temperature extraction.

### CORE-04: Simulation and synthetic data

Built physics-informed thermal models, synthetic thermogram generation, dynamical-system simulations, and visualizations to reason about sparse observations and latent process behavior.

### CORE-05: Research-to-product translation

Partnered with engineering, hardware, clinical, and scientific stakeholders to preserve model validity from prototype through embedded firmware and production deployment in regulated, high-noise environments.

### CORE-06: Deployment-honest validation

Repeatedly redesigned evaluation methods to reflect real deployment conditions, including leave-one-subject-out validation, leakage audits, staged/prospective pilot studies, and model stress tests under distribution shift.

### POD-01: On-device fall-risk estimation

Designed and implemented streaming fall-risk estimators for SmartMat+, a battery-powered patient-facing edge device enabling near-real-time risk updates after a 17-second pressure-sensor session. Prototyped Bayesian and weighted-window approaches in Python, selected the strongest estimator, translated it to C, validated numerical equivalence, and supported firmware integration for prospective testing.

### POD-02: Robust estimator validation

Benchmarked candidates on synthetic, staged, and prospective datasets, progressing from 5-participant internal testing to a 10-recruit characterization study and a 3-month, 30-patient pilot while stress-testing drift, regime shifts, outliers, irregular sampling, cold-start behavior, and long-horizon error accumulation.

### POD-03: Adaptive fall-risk monitoring

Reduced time to reliable patient-specific estimates from roughly 20-30 days to 3-5 days through adaptive streaming estimation and Bayesian cold-start methods.

### POD-04: Adaptive alert logic

Designed baseline-updating and alert-triggering logic for longitudinal fall-risk monitoring from pressure-derived stability metrics, evaluating deviations from individualized baselines and requiring time-bounded persistence before clinical escalation.

### POD-05: Production thermal CV and signal-processing pipeline

#### Resume text

Extended, validated, and refactored FDA-cleared SmartMat thermal-processing workflows spanning scan-quality handling, thermal-equilibrium prediction from 17-frame temperature curves, calibration, foot localization and left/right classification, segmentation and background removal, and anatomical keypoint temperature extraction in a deployed platform serving roughly 15k active patients and 25k lifetime patients.

#### Selection

Keep POD-05 for broad CV/health resumes emphasizing scientific scope, modality, and deployed reach. Prefer POD-12 for engineering-focused resumes emphasizing ownership, refactoring, and integration. Merge selectively rather than spending two bullets on the same underlying pipeline.

### POD-06: SmartMat+ thermal algorithm adaptation

#### Resume text

Led technical investigations to transfer, tune, and validate existing SmartMat thermal scan-processing modules for SmartMat+, tracing hardware, statistical, and algorithmic sources of prediction error across data collection, validation design, training/inference consistency, scan quality, and device-specific behavior to support reliable production deployment.

#### Variant: implementation

Adapted the production thermal pipeline for SmartMat+ by adding device-specific processing for its different sensor-matrix shape, training new machine-learning and calibration models, and collaborating with hardware engineering on data collection and validation and software engineering on sandbox testing and Git workflows.

#### Selection

The default emphasizes scientific diagnosis and validation judgment; the variant emphasizes implementation and model delivery. Use the version that matches the JD, not both. Source for added implementation details: Kevin, October 15, 2026.

### POD-07: Personalized DFU detection prototype

Developed and presented an adaptive temperature-asymmetry model for thermal-scan diabetic foot-ulcer detection, using individualized conservatively updated thermal baselines to improve robustness for patients with Charcot foot, peripheral arterial disease, or changing health status.

### POD-08: Framewise foot tracking prototype

Investigated frame-level foot localization and segmentation across 17-frame thermal scan sequences to stabilize regions of interest before thermal-equilibrium extrapolation, with the goal of reducing noisy temporal inputs and improving downstream temperature estimates.

### POD-09: Physics-informed thermal modeling

Developed physics-informed thermal models to support algorithm development and evaluation, including a synthetic thermogram generation framework for realistic spatiotemporal simulation and a Newtonian heat-transfer model for extrapolating short-duration thermal scans toward thermal equilibrium.

### POD-10: Next Best Action analytics

Co-designed an analytical framework combining quasi-experimental methods with baseline-adjusted behavioral response metrics to evaluate intervention effectiveness, support patient segmentation, optimize reengagement channels, and enable future A/B testing and personalized outreach.

### POD-11: Cross-functional technical leadership

Served as the primary scientific partner to software and hardware engineering teams, advising on algorithm integration, sensor behavior, scan-processing pipelines, validation methodology, and implementation decisions to ensure production systems preserved the integrity of physiological data and scientific conclusions.

### POD-12: Production scan-pipeline ownership and QC integration

#### Resume text

Owned the production thermal-imaging, modeling, and detection pipeline; substantially refactored the Python codebase, integrated data-quality modules supplied by external consultants, and implemented device-specific processing paths for SmartMat+ in collaboration with software and hardware engineering.

#### Evidence

Evidence / selection guidance (Kevin, October 15, 2026): Ownership, substantial refactoring, and consultant-module integration strengthen the earlier contribution-only wording and replace it. Debugging, bug fixes, PR participation, and reliability across chip/hardware vendors remain supported by the earlier bank entry and may be substituted when relevant. Prefer POD-05 for broader scientific/modality framing and POD-06 when SmartMat+ model training and validation are the main accomplishment. Do not imply ownership of the entire cloud platform or all engineering infrastructure.

### POD-13: Event-driven AWS thermal pipeline

Worked on production algorithm components in an AWS-hosted, event-driven SmartMat thermal pipeline where cellular telemetry receipt through an internal routing service triggered scan-quality handling, imputation, transformation, equilibrium-field prediction/estimation, and diabetic foot-ulcer detection modules; thermal outputs fed internal product/engineering and clinical tools, API-accessible outputs, and provider-facing summary emails.

### POD-14: SmartMat+ edge-to-cloud estimator outputs

Designed a SmartMat+ on-device fall-risk estimator whose outputs were generated on embedded hardware and transmitted with device telemetry to AWS for downstream monitoring and analysis.

### POD-15: PR-triggered pipeline sandbox validation

#### Resume text

Validated thermal-processing and model-inference changes in isolated clones of the production AWS environment, using PR-triggered Terraform/GitHub Actions provisioning, configuring scan-processing workflows and pipeline revisions, and submitting scans to exercise the integrated system.

#### Evidence

Evidence / boundaries (Kevin, October 15, 2026, clarified): Terraform use is confirmed, not inferred from a repository name. Kevin opened PRs in the team's infrastructure/controller repository to trigger creation of a full clone of the production AWS setup with its own API address. He edited relevant configuration and GitHub Actions YAML files, including test-data selections and pipeline revision hashes, and pushed scans to the environment to test scan-triggered processing. Software engineers taught him the workflow; much of provisioning remained a black box to him. This establishes hands-on use of Terraform-provisioned AWS environments and configuration of integration-testing workflows, not authorship of Terraform infrastructure, design of the provisioning system, or ownership of the entire cloud platform. Terraform may be named in this qualified context; do not present it as independent infrastructure-as-code expertise. Use generic system descriptions on resumes. This evidence does not by itself establish automated test-suite design.

### CVB-01: Technical leadership and mentorship

Led scientific direction, reviewed modeling and validation decisions, mentored data scientists and ML contributors, and translated ambiguous project goals into concrete technical plans, evaluation criteria, and deployment constraints.

### CVB-02: Program leadership

Led the Sensor Analytics Team through organizational change, secured continued Michael J. Fox Foundation funding, and received two 2023 Milestone Achievement Awards.

### CVB-03: Wearable study design and evaluation

Co-developed in-lab and longitudinal home-use wearable protocols with a partner hospital for personalized Rett syndrome monitoring, then reconstructed and audited multimodal data from smartwatch sensors, video recordings, and behavioral annotations post-collection, identifying missing or inconsistently documented sensor-synchronization procedures, timestamp inconsistencies, annotation ambiguity, limited behavioral coverage, and temporal-alignment limits that made brief behavioral events unreliable targets for patient-specific stereotypy detection.

### CVB-04: Sleep sensor validation

Reframed conventional PSG/actigraphy validation methodology by developing a DTW-based evaluation framework accounting for systematic physiological timing differences in sleep onset between EEG- and motion-based measurements.

### CVB-05: Parkinson's research leadership

Led the wearable Parkinson's disease research program, providing scientific direction while co-developing wearable disease-monitoring models that culminated in a peer-reviewed publication and invited presentations.

### CVB-06: Multimodal wearable data processing

Converted free-living multimodal wearable recordings into a queryable local database, enabling efficient slicing, temporal alignment, quality auditing, and model development without loading full sensor streams into memory.

### CVB-07: Parkinson's digital biomarkers

Named, built, and led the Sensor Analytics Team; secured a Michael J. Fox Foundation grant and its second-year renewal to develop digital biomarkers for longitudinal Parkinson's disease monitoring using Verily Watch data from PPMI.

### CVB-08: Free-living Parkinson's monitoring

Used a weakly supervised walk-detection framework to restrict disease inference to gait-relevant, walk-like intervals within unconstrained free-living recordings, then applied an end-to-end deep neural network to discriminate Parkinsonian gait from healthy controls with approximately 90% single-event accuracy and 100% daily majority-vote accuracy in an 11-subject preliminary study using leave-one-subject-out (LOSO) validation; co-first author of the resulting peer-reviewed publication (Sensors, 2022).

### CVB-09: Wearable gesture recognition

Built Conv1D-LSTM models for Rett stereotypy detection in a wearable-device comparison spanning Shimmer IMUs, Apple Watch, Oura Ring, and Fitbit; guided IMU sampling-rate selection using movement bandwidth, Nyquist criteria, and instrument-noise considerations, then confirmed the lower-rate choice through 25-400 Hz ablations.

### CVB-10: End-to-end biosignal modeling

Adapted an end-to-end Conv1D-LSTM architecture from wearable gesture recognition to ECG sleep-apnea detection, then validated the approach through ablation studies that progressively replaced a classical signal-processing, handcrafted-feature, and SVM pipeline with learned representations; the TensorFlow/Keras framework was later ported to PyTorch and adapted to Parkinson's disease monitoring.

### CVB-11: Cross-domain representation learning

Explored DRCN-style reconstruction/classification networks, variational autoencoder architectures, transfer learning, and unsupervised domain adaptation for wearable physiological time series, using TensorFlow/Keras and PyTorch prototypes with shared representations and pseudolabel concepts to adapt general activity models toward new sensors, subjects, and clinical datasets.

### CVB-12: Weakly supervised learning

Leveraged rules-based walk detection to identify walk-like intervals from unlabeled free-living wearable recordings, enabling Parkinson's disease modeling without manually annotated activity labels.

### CVB-13: Research strategy

Evaluated a wearable suicide-risk prediction initiative as infeasible given no available training data and the need for a long-term prospective study; redirected the program toward more tractable clinical risk indicators such as dropout and prepared executive-facing reports for senior stakeholders, including the White House.

### CVB-14: Clinician-friendly machine learning

Built Random Forest and XGBoost models to predict patient dropout risk from longitudinal EHRs, using SHAP, LIME, and feature-importance analyses to make model behavior interpretable for skeptical clinical stakeholders.

### CVB-15: Deployment-honest validation

Identified overlapping-window data leakage, time-ordering bias, and evaluation-target mismatch in a gesture-recognition prototype, then redesigned validation around leave-one-subject-out cross-validation to estimate unseen-patient generalization in a small cohort.

### CVB-16: Early-term birth prediction

Collaborated with Columbia University on maternal-health prediction using clinical and Columbia-provided EEG-derived features, focusing on hyperparameter tuning, model selection, missing-data handling, and leakage detection.

### CVB-17: Reproducible team workflows and tooling

#### Resume text

Created reusable project-organization practices, code-review patterns, technical tutorials, Bash/AWS/Docker/Conda/Git helper tools, and lightweight environment scaffolding to reduce reproducibility friction and technical debt across data science research projects.

#### Selection

Preserve this broad team-enablement bullet for roles that value reproducible research without requiring low-level cloud detail. Prefer CVB-22 when concrete access/environment automation is more relevant; do not repeat the same tooling work in both. SensorNet (CVB-21) is separate reusable-package evidence.

### CVB-18: Wearables knowledge graph and database evaluation

Evaluated graph, document, relational, time-series, and key-value databases for a wearable-to-biological-phenomenon knowledge graph; designed schema iterations and demonstrated Neo4j/Cypher query patterns for many-to-many mappings among sensors, algorithms, symptoms, disorders, and physiological signals.

### CVB-19: Sensor-driven questionnaire estimation

Proposed a Sensor-Driven Questionnaire Estimation framework as a tractable alternative to an unsupported wearable-suicide prediction mandate, targeting the PHQ-9 depression screener first for its free availability and initial supporting evidence and envisioning a roadmap extension toward a continuously updated proxy index refined via Kalman-filter-style data assimilation whenever a real PHQ-9 score became available; generalized the core approach with a broad literature review and synthetic-data examples to broader clinic-administered assessments and patient-state risk indicators.

### CVB-20: Biosignal ablation leadership variant

Conceived and mapped systematic ablation experiments demonstrating that end-to-end deep learning architectures outperformed handcrafted feature-engineering pipelines across biosignal domains, delegated most model implementation to a direct report, and personally contributed the final, best-performing architecture.

### CVB-21: SensorNet reusable biosignal modeling package

#### Resume text

Developed SensorNet, an internal, pip-installable package for the Sensor Analytics Team, consolidating recurring Conv1D-LSTM implementations into a configurable model class with training, updating, and inference methods plus DTW-like and time-series augmentation utilities; pinned installations to documented revision hashes for reproducibility as the package evolved.

#### Evidence

Evidence / boundaries (Kevin, October 15, 2026): Kevin began the package after repeatedly rewriting the network for new projects. This establishes reusable interfaces, package development/refactoring, and version-pinned project dependencies. Do not infer a public release, PyPI publication, automated test coverage, comprehensive dependency locking, or exact title/date placement. Hash pinning supports reproducibility; it does not prove an entire experiment environment was reproducible.

### CVB-22: AWS research-computing access and workflow tooling

#### Resume text

Configured an EC2/Linux research environment and later created login, synchronization, IAM role-assumption, and EC2-selection scripts for himself and a direct report, reducing workflow friction on a newly introduced cloud research system.

#### Evidence

Evidence / selection guidance (Kevin, October 15, 2026): The initial EC2 setup was a single-user environment early in Kevin's CVB tenure; the later team scripts addressed a new cloud system that initially slowed research. IAM roles here were temporarily assumed roles, not simply Linux user accounts. This is the concrete cloud-workflow alternative to CVB-17, not evidence that Kevin architected the underlying cloud platform. Exact title boundaries remain unconfirmed.

### CVB-23: Cross-project scientific code and leakage review

#### Resume text

Reviewed other researchers' software packages and modeling pipelines across projects, identifying data-leakage risks and scrutinizing implementation choices that affected the validity of scientific results.

#### Evidence

Evidence / selection guidance (Kevin, October 15, 2026): This recurring review work extends beyond the specific gesture-validation redesign in CVB-15. Use for scientific code review and quality judgment; do not infer organization-wide mandatory review policies, release authority, or formal test standards.

### WWE-01: Production viewership data products

#### Resume text

Built API-based social-data pipelines and co-developed live-event KPI dashboards across YouTube, Facebook, Twitter, and WWE Network, replacing third-party data and reporting services costing roughly $1M annually while improving data coverage and timeliness.

#### Evidence

Kevin clarified on October 19, 2026 that his manager reported approximately $1M in combined annual spending across third-party data providers and potentially associated consultants. Kevin did not own the contracts; inclusion of consulting costs is uncertain. The amount describes manager-reported service spending, not independently audited savings.

#### Boundaries

Use "third-party data and reporting services" rather than narrowing the combined spend to data feeds alone. Do not state that consultants were definitely included. Do not translate the roughly $1M annual service cost into $1M in realized savings or confirmed contract cancellations without confirmation. Preserve the co-developed dashboard attribution; Kevin's manager owned Tableau SQL and visualizations, as documented under WWE-02. These boundaries also apply when adapting WWE-02, WWE-06, or WWE-07 into cost-impact claims.

### WWE-02: Real-time executive analytics

#### Resume text

Co-created a multi-platform live-event dashboard by owning its data collection, transformation, and analysis pipelines, enabling real-time executive decisions during broadcasts.

#### Variant: detailed

Owned collection, transformation, analysis, and table preparation for executive live-event reporting across YouTube, WWE Network, Facebook, and Twitter, implementing most pipelines directly and delegating Twitter collection to a direct report; partnered with the manager who built the Tableau SQL and visualizations.

#### Evidence

Attribution / selection guidance (Kevin, October 15, 2026): Use the compact version when the outcome matters most and the detailed version when pipeline ownership, delegation, and collaboration matter. Kevin's manager owned the Tableau SQL and visualizations; do not imply Kevin independently built those components. This attribution also applies to WWE-01 and WWE-07.

### WWE-03: Production customer behavior analytics

Developed and maintained automated data processing, machine learning, and reporting pipelines supporting customer segmentation, churn prediction, executive reporting, and A/B test analysis for marketing and customer engagement initiatives.

### WWE-04: Deep learning for churn prediction

Replaced a logistic-regression-based churn prediction system with a 5-layer neural network, improving total AUC from approximately 0.64 to 0.73; independently developed Gaussian noise injection between hidden layers as a regularization strategy, contributing approximately half of the overall performance gain.

### WWE-05: Transfer learning and fine-tuning for computer vision

Built a 20-class WWE Superstar image-recognition prototype by fine-tuning ImageNet-pretrained VGG16 with a custom classification head, two-phase frozen-base/top-block-unfrozen training, heavy data augmentation, VGG16/VGG19/ResNet50 comparison, and confidence-thresholded out-of-roster rejection under roughly 50 images per class.

### WWE-06: YouTube and social-platform data remediation

Researched YouTube, Facebook, Instagram, and platform-specific APIs to identify major gaps in third-party vendor feeds, then built automated collection and warehousing pipelines that substantially expanded available social/video metrics while reducing vendor dependence.

### WWE-07: Live-event analytics latency reduction

Co-developed multi-platform live-event reporting workflows that captured viewership metrics across YouTube, Facebook, Twitter, WWE.com, and WWE Network within minutes of broadcast, replacing manual cross-team reporting processes that previously took 12-24 hours.

### WWE-08: Revenue attribution and behavioral research

Built revenue-attribution, survey-fusion, sentiment-analysis, seasonal-behavior, and customer-behavior analyses over large-scale WWE Network and social-platform datasets to support segmentation, marketing decisions, churn/winback forecasting, and stakeholder reporting.

### WWE-09: AWS automated scoring to Redshift

#### Resume text

Developed and maintained AWS-hosted automated web-scraping, API collection, model-scoring, and reporting workflows, using cron to schedule hourly/daily data collection and daily analytical reports; churn-model scores were written to Redshift for marketing and product dashboards.

#### Evidence

Evidence / selection guidance (Kevin, October 15, 2026): The cron schedules and ongoing code maintenance strengthen the earlier operations-only wording. These are scheduled workloads on EC2, not evidence of cluster scheduling or distributed execution. Use WWE-11 instead when shared GPU/Linux environment administration is the main requirement; avoid repeating the collection/reporting details.

### WWE-10: Streaming-account anomaly and enforcement investigation

#### Resume text

Investigated anomalous WWE Network account usage by rebuilding SQL analyses and mapping device activity, revealing individual accounts with 200+ devices streaming simultaneously across countries and exposing a failure to enforce the platform's two-device concurrency limit.

#### Evidence

Evidence / interview context (Kevin, October 14, 2026): The original assignment concerned device-switching behavior during major live events. Implausibly large device counts initially led Kevin to suspect his own queries; he rebuilt them incrementally before visualizing geographic and simultaneous usage. He encountered internal pushback based on the stated two-device limit. Kevin reports that WWE subsequently established that MLBAM was not enforcing the limit and that a lawsuit/settlement followed, but he does not recall the precise legal details or amount. Omit the legal outcome and dollar figure from resume claims until confirmed. The observations establish unexpected usage and failed enforcement, not the users' motives or a network intrusion.

### WWE-11: Shared GPU-enabled AWS/Linux research environment

#### Resume text

Administered a GPU-enabled AWS EC2/Linux instance shared by three users, configuring user accounts, private and shared directory permissions, NVIDIA/TensorFlow dependencies, and Jupyter and RStudio servers while troubleshooting colleagues' environment issues.

#### Evidence

Evidence / boundaries (Kevin, October 15, 2026): Approximately 2016-2017. The instance also hosted cron-scheduled scrapers, API collectors, and reporting workflows (WWE-09). This is concrete shared GPU research-computing and Linux administration experience; do not claim a multi-node HPC cluster, distributed training, Slurm/PBS, or measured performance/scaling gains.

### WWE-12: Reusable R ingestion-to-reporting package

#### Resume text

Built an R package spanning SFTP data ingestion, parsing and transformation, analysis, plotting, and HTML/PDF report generation for stakeholder email distribution; handed the package off to consultants to run and maintain.

#### Evidence

Evidence / boundaries (Kevin, October 15, 2026): The handoff supports reusable software and lifecycle/knowledge-transfer experience. Do not infer a public package release, a web application, specific documentation or testing practices, or that the package itself implemented email delivery.

### MSG-01: Self-supervised behavioral video analysis

MachineSaidGo / independent R&D: Designed and prototyped self-supervised deep learning architectures for mouse behavioral analysis from video, exploring activity classification and anomaly detection from unlabeled video sequences using PyTorch and computer-vision libraries.

### MSG-02: Granular-dynamics surrogate modeling

MachineSaidGo / independent research collaboration: Collaborated with mechanical-engineering researchers on RNN forecasting and PyTorch surrogate-modeling approaches for computationally expensive tapped-granular-system simulations, extending a long-running nonlinear-dynamics and scientific-simulation research thread.

### CSTR-01: Polar-cap representation inference

Developed median-relative spectral analysis over 63-day Antarctic magnetometer baselines to test whether the standard magnetic coordinate system correctly mapped ground sensors into the magnetosphere, revealing hidden polar-cap structure not visible in short event studies and motivating a more data-driven geometry.

### CSTR-02: Magnetic-coordinate validation

#### Resume text

Demonstrated that widely used magnetic coordinates could misclassify high-latitude sensor sites, motivating alternative observational coordinate representations that better separated deep polar-cap behavior from boundary-straddling, cusp-like behavior.

#### Evidence

Interview context (Kevin, October 14, 2026): This investigation began during exploratory data analysis when observations did not fit the accepted picture of polar geomagnetic geometry. Kevin then investigated the discrepancy extensively. Use CSTR-01 and CSTR-02 as evidence of testing an accepted representation against observations; avoid broadening the claim into having disproved all polar geomagnetic field geometry.

### CSTR-03: Geophysical signal interpretation

Analyzed ground magnetometer observations by disentangling overlapping effects from coastline geometry, crustal conductivity, ionospheric conductivity, and solar-wind coupling.

### CSTR-04: Multi-instrument space weather reconstruction

Reconstructed and animated heliospheric event timelines as dynamic global visualizations of space weather propagation across a distributed instrument chain spanning the Sun to the heliosheath, integrating observations from SDO, ACE, approximately 180 INTERMAGNET magnetometers, the Antarctic AGO network, DMSP satellites, the Van Allen Probes, and Voyager 2.

### CSTR-05: Scientific collaboration

Contributing member of the NASA RBSPICE instrument team on the Van Allen Probes mission; delivered invited talks at AGU, the Air Force Research Laboratory, and CEDAR.

### CSTR-06: Computational mathematics, granular fluids, and nonlinear dynamics

Translated analytical models of granular fluid dynamics into numerical simulations and visualizations, including parameterized Poincare map analyses of chaotic dynamical systems, contributing to four peer-reviewed publications from 2011-2014.

### CSTR-07: Solar-wind forecasting and inverse nowcasting

Developed dynamic lagged-correlation analyses linking deep polar-cap ground-sensor power to upstream solar-wind magnetic-field fluctuations, supporting an inverse remote-sensing approach for nowcasting near-Earth solar-wind state parameters.

### INT-01: JPL trajectory optimization and design

Trajectory Optimization and Design - NASA Jet Propulsion Laboratory, Pasadena, CA (May-Aug 2011). Full spacecraft mission design to Jupiter's Trojan asteroids: science goals, instrument selection, trajectory optimization, concurrent engineering, and formal NASA review board presentation; contributing author on peer-reviewed paper.

### INT-02: NASA Goddard Heliophysics Division

Heliophysics Division - NASA Goddard Space Flight Center, Greenbelt, MD (Summer 2006). Developed web content and gained early experience with Python, HTML, CSS, JavaScript, PHP, and UNIX command-line tools.

### INT-03: NASA Goddard Observational Cosmology Laboratory

Observational Cosmology Laboratory - NASA Goddard Space Flight Center, Greenbelt, MD (Summer 2007). Developed software to model data collection and analysis for the Absolute Spectrum Polarimeter, a proposed spacecraft instrument for detecting B-mode gravitational-wave signatures.

### INT-04: NASA/JPL research internship signal

Research internships at NASA Goddard Space Flight Center and Jet Propulsion Laboratory (2006, 2007, 2011), spanning spacecraft-instrument software, heliophysics tools, and formal mission-design research.

### SKILL-01: Machine learning

Deep learning; sequence modeling with Conv1D/CNNs, LSTMs, transformers, and TCNs; representation learning; autoencoders/VAEs; transfer learning; fine-tuning; self-supervised learning; tree-based learning; clustering; explainable AI with SHAP and LIME; computer vision; image localization/segmentation; human activity recognition; gesture recognition; synthetic data generation; physics-informed modeling; model selection; validation/verification; ablation studies.

### SKILL-02: Statistical signal processing and estimation

Bayesian inference; inverse problems; state estimation; stochastic filtering; Kalman filtering; recursive Bayesian estimation; adaptive estimators; tracking; uncertainty-aware modeling; drift/regime-shift analysis; robustness testing; Normal-Inverse-Gamma priors; time-series and longitudinal modeling; spatiotemporal modeling; time-frequency methods; STFT; PSD/spectral analysis; wavelets; coherence analysis; time-series similarity and alignment with DTW.

### SKILL-03: Sensor analytics and modalities

IMUs, accelerometers, gyroscopes, ECG, pressure sensing, thermal imaging, magnetometers, cameras, medical devices, satellites/spacecraft, sensor fusion, multimodal sensing, physiological sensing, wearables, longitudinal monitoring, digital biomarkers, field validation, sensor synchronization, embedded deployment.

### SKILL-04: Languages and tools

Python, PyTorch, TensorFlow/Keras, OpenCV, HuggingFace, scikit-learn, SciPy, NumPy, MLflow, C, R, MATLAB, IDL, SQL, Linux, Docker, Git, Jupyter, AWS, GCP.

### TRAIN-01: Deep Learning Nanodegree

Udacity Deep Learning Nanodegree, 2017.

### TRAIN-02: Intel IoT Edge AI Scholarship

Intel IoT Edge AI Scholarship.

### TRAIN-03: Building with the Claude API

Building with the Claude API.

### TRAIN-04: Tableau 9 Essential Training

Tableau 9 Essential Training.

### PUB-01: Sensors 2022 Parkinson's disease wearable monitoring

Atri, R. and Urban, K. (co-first authors) et al. "Deep Learning for Daily Monitoring of Parkinson's Disease Outside the Clinic Using Wearable Sensors." Sensors, 2022.

### PUB-02: JGR Space Physics 2016 polar-cap / ULF power

Urban et al. "Rethinking the Polar Cap: Eccentric Dipole Structuring of ULF Power." JGR: Space Physics, 2016.

### PUB-03: Physica D 2014 nonlinear dynamics / simulations

Blackmore et al. "Analysis, simulation and visualization of 1D tapping via reduced dynamical models." Physica D: Nonlinear Phenomena, 2014.

### PUB-04: Planetary and Space Science 2013 JPL mission design

Diniega et al. "Mission to the Trojan Asteroids: Lessons Learned During a JPL Planetary Science Summer School Mission Design Exercise." Planetary and Space Science, 2013.

### PUB-05: Space Weather 2011 open-closed boundary

Urban et al. "Quiet Time Observations of the Open-Closed Boundary Prior to the CIR-Induced Storm." Space Weather, 2011.

### PUB-06: Powders and Grains 2013 granular column dynamics

Rosato et al. "Dynamical systems model and discrete element simulations of a tapped granular column." Powders and Grains, AIP Conference Proceedings, 2013.

### PUB-07: JOMMS 2011 tapping dynamics

Blackmore et al. "Tapping dynamics for a column of particles and beyond." Journal of Mechanics of Materials and Structures, 2011.

### PUB-08: Condensed Matter Physics 2010 fractional fields

Blackmore, Urban, and Rosato. "Integrability analysis of regular and fractional Blackmore-Samulyak-Rosato fields." Condensed Matter Physics, 2010.

### PUB-09: CVB 2020 wearable digital-biomarker science article

Urban, K. "Are Wearables Worth the Hype?" Cohen Veterans Bioscience public science article / Q3 newsletter, 2020.

### PUB-10: Biological Psychiatry 2020 wearable/home sleep-sensor verification poster

Postma, F., Rozenberg, Z., Shokhirev, N., Urban, K., Rubin, U., and Brunner, D. "Technical Performance Verification of Wearable and Home Sensor Devices Monitoring Sleep: Best Practices." Biological Psychiatry 87(9), S343, 2020. DOI: 10.1016/j.biopsych.2020.02.880.

### PUB-11: Bounded DTW sleep-device validation methods manuscript

Urban, K. "Bounded Dynamic Time Warping for Epoch-by-Epoch Agreement Between Polysomnography and Sleep-Tracking Devices." Manuscript in preparation.

### PUB-12: Sleep apnea deep learning and domain-expertise working paper

Urban, K. and Atri, R. "Evaluating the impact of domain expertise and deep learning in the design and performance of sleep apnea detection models." Working paper / unpublished.

### PUB-13: Augmented unsupervised domain adaptation working paper

Atri, R. and Urban, K. "Augmented Unsupervised Domain Adaptation for Deep Time Series Models." Working paper / unpublished.

### PUB-14: APS DFD 2022 tapped granular systems ML presentation

Rosato et al. "Tapped Granular Systems: Simulations and Machine Learning Approaches." 75th Annual Meeting of the APS Division of Fluid Dynamics, 2022. Conference abstract / oral presentation.

### AWARD-01: CVB 2023 Milestone Achievement Awards

Received two 2023 CVB Milestone Achievement Awards for project execution, research leadership, and cross-functional collaboration.
