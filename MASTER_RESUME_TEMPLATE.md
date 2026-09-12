# Master Resume Template

This file is the canonical structure for tailored resumes.

It is intentionally template-like. Do not treat it as the evidence reservoir. Resume evidence lives in `RESUME_BULLET_BANK.md`; reusable profile/headline language lives in `PROFILE_BANK.md`; cluster matching lives in `JD_CLUSTER_BANK.md`.

Generated tailored resumes should usually be 3 pages and should be delivered as DOCX by default according to `OUTPUT_CONTRACT.md`.

## Header

```text
Kevin Urban, PhD
{TAILORED_HEADLINE_FROM_PROFILE_BANK}
kevin.ddu@gmail.com | Nutley, NJ | (973) 464-6833 | linkedin.com/in/machinesaidgo | github.com/krbnite
```

## Profile / Headline Slot

Use one selected headline/profile pair from `PROFILE_BANK.md`.

Rules:

- Do not keep a standalone "general fallback profile" in this template.
- Use `Default Sensor ML Research Scientist` from `PROFILE_BANK.md` when no specialized profile dominates.
- If creating a new profile cluster, start from the default profile only when useful, then narrow it toward the new cluster's core signals.
- Record all profile/headline edits, add-ons, and retention decisions in the audit.

```text
{TAILORED_PROFILE_PARAGRAPH}
```

## Core Research Themes Slot

Generate this section from the `CORE-*` rows in `RESUME_BULLET_BANK.md`.

Default target: 3-5 themes.

Selection rules:

- Prefer high-scoring core themes for the primary cluster.
- Keep `Deployment-honest validation` unless there is a strong reason to drop it.
- Keep `Sensor inference under uncertainty` for most roles because it is Kevin's broadest through-line.
- Add `Computer vision and thermal imaging`, `Simulation and synthetic data`, or `Research-to-product translation` when the JD clearly calls for them.
- Do not include every core theme automatically.

```text
CORE RESEARCH THEMES
- {CORE_BULLET_ID}: {possibly edited bullet}
- {CORE_BULLET_ID}: {possibly edited bullet}
- {CORE_BULLET_ID}: {possibly edited bullet}
```

## Experience

Use the role order below unless the JD requires a highly unusual format. Select bullets from `RESUME_BULLET_BANK.md`; do not paste the whole bank into the resume.

### Podimetrics

```text
Principal Data Scientist | Remote | Dec 2024 - Apr 2026
Adaptive statistical estimation, computer vision, and physics-informed modeling for FDA-cleared remote-monitoring products using thermal arrays and pressure sensors for diabetic foot ulcer detection and fall-risk assessment.

- {POD-* selected bullet}
- {POD-* selected bullet}
- {POD-* selected bullet}
```

Guidance:

- Usually the most important recent evidence block.
- Lead with this section for health, sensor AI, industrial, and closed-loop physical AI roles.
- Select heavily; do not keep all Podimetrics bullets in a tailored 3-page resume.

### Cohen Veterans Bioscience

```text
Director of Data Science & Digital Health | New York, NY | Jul 2021 - May 2024
- {CVB-* selected bullet}
- {CVB-* selected bullet}
- {CVB-* selected bullet}

Associate Director of Data Science - Sensor Analytics | New York, NY | Jun 2019 - Jul 2021
- {CVB-* selected bullet}
- {CVB-* selected bullet}

Senior Data Scientist, Early Signal Team | New York, NY | Jun 2018 - Jun 2019
- {CVB-* selected bullet, if relevant}
```

Guidance:

- Keep strongest health/wearable/neurotech evidence for HWD roles.
- Compress leadership or older role blocks when the JD is more technical than managerial.
- Use Early Signal bullets mainly for clinical ML, interpretability, feasibility judgment, or leakage/validation relevance.

### WWE

```text
Senior Data Scientist | Stamford, CT | Aug 2017 - Jul 2018
- {WWE-* selected bullet, if relevant}

Data Scientist | Stamford, CT | Oct 2016 - Aug 2017
- {WWE-* selected bullet, if relevant}
```

Guidance:

- Usually compress for research-heavy health, sensor AI, and physical systems roles, but retain one compact WWE line when page budget allows because the brand and business-ML range are useful conversation starters.
- Omit entirely only when page budget is unusually tight or the role would be distracted by business/entertainment analytics.
- Retain for industrial/operational ML, production data products, dashboards, A/B testing, stakeholder decision support, or business-impact evidence.

### Center For Solar-Terrestrial Research

```text
Research Assistant, New Jersey Institute of Technology | Newark, NJ | Aug 2012 - May 2016
PhD research inferred polar-cap electrodynamics from distributed magnetometer, satellite, and spacecraft observations using novel spectral methods for noisy geophysical time series.

- {CSTR-* selected bullet}
- {CSTR-* selected bullet}
```

Guidance:

- Lead or preserve more detail for BSP roles.
- Borrow selectively for SAR and CLP roles when sensor networks, physical inference, reconstruction, or simulation matter.
- Compress heavily for HWD or IOT roles unless signal-processing depth is strategically useful.

## Internships

This section is relatively stable but optional under page pressure.

```text
INTERNSHIPS
- Trajectory Optimization and Design - NASA Jet Propulsion Laboratory, Pasadena, CA (May-Aug 2011). Full spacecraft mission design to Jupiter's Trojan asteroids: science goals, instrument selection, trajectory optimization, concurrent engineering, and formal NASA review board presentation; contributing author on peer-reviewed paper.
- Heliophysics Division - NASA Goddard Space Flight Center, Greenbelt, MD (Summer 2006).
- Observational Cosmology Laboratory - NASA Goddard Space Flight Center, Greenbelt, MD (Summer 2007).
```

Rules:

- Default to the compact NASA/JPL signal when page budget allows; the brand/research credibility is often useful even outside aerospace roles.
- Expand the individual internship bullets only when aerospace, robotics/autonomy, optimization, physical systems, spacecraft instruments, or mission-oriented research are directly relevant.
- Omit the internship signal only under meaningful page pressure or when early-career space/physics detail would distract from the target role; record the omission in the audit.

## Selected Research Projects Slot

Use optional `MSG-*` and other project-style rows from `RESUME_BULLET_BANK.md` only when the role benefits from evidence that should not be forced into the main chronology.

```text
SELECTED RESEARCH PROJECTS
- {PROJECT_ID}: {possibly edited project bullet}
```

Rules:

- MachineSaidGo should not appear as a default chronological Experience role. It can complicate the CVB timeline because Kevin maintained CVB contracts while exploring independent consulting / side-venture work.
- Use MachineSaidGo material only when the JD specifically rewards self-supervised video, computer vision, behavioral analysis, surrogate modeling, scientific simulation, consulting/startup initiative, or independent R&D.
- Keep the section compact. If selected projects displace stronger recent work, omit them and preserve the Podimetrics/CVB spine.

## Technical Skills Slot

Use `SKILL-*` rows in `RESUME_BULLET_BANK.md` as the source.

Default rule: keep a robust skills section, but reorder and lightly trim terms to mirror the JD.

```text
TECHNICAL SKILLS
Machine learning: {ordered terms}
Statistical signal processing and estimation: {ordered terms}
Sensor analytics and modalities: {ordered terms}
Languages and tools: {ordered terms}
```

Rules:

- Do not overclaim depth in tools that are lightly represented.
- Put the JD's most important supported terms early.
- Trim low-relevance tools only if page budget is tight.

## Education

This section is stable.

```text
EDUCATION
PhD, Physics: New Jersey Institute of Technology / Rutgers University, 2016.
MS, Applied Physics: Minor in Applied Math, NJIT / Rutgers University, 2010.
BS, Applied Physics: Minor in Applied Math, NJIT / Rutgers University, 2008.
```

## Selected Training Slot

Use `TRAIN-*` rows in `RESUME_BULLET_BANK.md`.

Default target: omit.

Rules:

- Add a compact training section only when the JD, recruiter screen, or application form benefits from explicit course/certification evidence.
- Consider `Deep Learning Nanodegree` when deep-learning timeline or credibility needs reinforcement.
- Consider `Intel IoT Edge AI Scholarship` for edge AI, IoT, sensor-device, embedded, and on-device inference roles.
- Consider `Building with the Claude API` for GenAI, agentic workflow, LLM API, or AI-product roles where lightweight formal evidence helps keyword screening.
- Avoid Tableau unless dashboarding, BI, or Tableau is explicitly requested.

```text
SELECTED TRAINING
- {TRAIN-* selected training}
```

## Selected Publications Slot

Use `PUB-*` rows in `RESUME_BULLET_BANK.md`.

Default target: 2-5 publications, depending on role type and page budget.

Rules:

- Always consider `PUB-01` for health/wearables/neurotech roles.
- Always consider `PUB-02` for physical systems, geophysics, and signal-processing roles.
- Use the section title `Selected Publications & Research Writing` when selected entries include unpublished manuscripts, conference abstracts/posters, or public science writing.
- Include older space/physics publications only when they strengthen the target role.
- Omit publications entirely only if space is tight and the JD is strongly product/industry oriented.

```text
SELECTED PUBLICATIONS
- {PUB-* selected publication}
- {PUB-* selected publication}
```

## Selected Awards Slot

Use `AWARD-*` rows in `RESUME_BULLET_BANK.md`.

Default target: omit.

Rules:

- Add awards only when they strengthen a senior leadership, program-delivery, grant/funding, presentation, or CV-like research narrative.
- Do not use awards to bulk up an ordinary technical resume when stronger technical evidence needs the space.
- Prefer compact award wording; if awards create page pressure, cut them before cutting recent Podimetrics/CVB evidence.

```text
SELECTED AWARDS
- {AWARD-* selected award}
```
