Code to generate:
```bash
ls my-presentations/ |\
    rev | cut -d. -f2- | rev |\
    sed -e "s/^/| /;s/__/_/g;s/_/ | /g;s/$/ |/"\
    > cvb-easi-presentations.md
```

--------------

Might not be everything, but a decent list none-the-less.

TODO: try to gather everything. 

--------------


# Senior Data Scientist, Early Signal Team (June 2018 - July 2019)

| Date | Project | Name | Where |
|------|---------|------|-------|
| 2018-08-01 | Misc             | Device Testing Strategies for EaSi App Development | CVB |
| 2018-08-08 | CVN - Suicide    | Wearables Roadmap: Brainstorm & Lit Review | CVB/CVN |
| 2018-09-05 | MJFF             | Empatica: Data Review & Exploration | CVB/MJFF |
| 2018-08-30 | CVN - Suicide    | Falcon Project: Which Scales for Wearables-based Scale Estimation? | CVB/CVN ("Sensor-Driven Questionnaire Estimation") |
| 2018-09-14 | CVN - Suicide    | Falcon Project: Roadmap for Wearables-based Scale Estimation | CVB/CVN Working Group - "Risk Scrum" |
| 2018-09-21 | CVN - Suicide    | \* No Slides: Co-hosted EaSi-lead SME/KOL workshop | Virtual meeting; various invited attendees |
| 2018-09-26 | MJFF             | Empatica HR/HRV Data Analysis (demo slide) | CVB/MJFF - Funding pitch w/ Udi, Dani et al at MJFF office |
| 2018-09-26 | 
| 2018-10-05 | EaSiEco (Graph)  | Several Wearable Table Schemas Already In-Use | Internal, Kevin+Zhanna |
| 2018-10-12 | EaSiEco (Graph)  | Database Landscape and Data Modeling | CVB, Manager (Dani) update |
| 2018-10-23 | EaSiEco (Graph)  | Neo4j-Pricing | CVB |
| 2018-10-25 | CVN - Suicide    | Review of Naive Bayes | Personal use. |
| 2018-10-29 | CVN - Suicide    | EHR-Driven Suicide Prediction: Lit Review | CVN |
| 2018-10-30   | EaSiEco          | Neo4j-Cypher Translations of Natural Language Queries | internal team; slides within related presentations |
| 2018-11-01   | CVN - Suicide    | Piecing together the CVN Patient-Care Flow Chart | Slides documenting putting this together (now in CVN003 folder) |
| 2018-11-21   | CVN - Suicide    | Self-Harm Overview (Self-Harm Risk Landscaping Efforts ) | CVB, Internal |
| 2018-12-03   | CNN - Suicide    | Suicide/Risk: Recommendations and Review (Wearables -> EHR?) | CVB/CVN Sync, DC area |
| 2018-12-10   | EaSiEco (Graph)  | Review of the EaSiEco Project | CVB STM 2018-Q4 (Kevin + Zhanna) | 
| 2018-12-11   | Rett/Gestures    | X-Shot-Learning | CVB STM 2018-Q4) |
| 2018-12-12   | CVN - Suicide    | Risky Business: EHR + Wearables-Driven Risk-Scale Estimation | CVB CWM 2018-Q4  |
| 2019-01-11   | CVN - Suicide/Dropout | How to understand a model that triggers interventions on its own predictions? (Predictive Modeling and Causal Inference) | CVB-CVN Sync | Few slides outlining the issue and how we might handle it using a multi-pronged/parallel modeling approach (marks the beginning of the suicide-to-dropout transition and work w/ Rajeev) |
| 2019-01-24   | CVN - Dropout    | Using Data to Improve Treatment | CVB/CVN Q1 Meeting (Note: Official transition to "Dropout" project) |
| 2019-02-06   | Rett/Gestures    | Kevin's GestureNet Results | Internal meeting |
| 2019-02-08   | EaSiEco (Graph)  | EaSi Ecosystem Info Deck | 1-on-1s w/ Zhanna; later on at CVB-WWG w/ Deepti |
| 2019-04-24   | CVN - Dropout    | \* In-Person Review Meeting | Dani attended and presented; CVN Annual Meeting - Focus Group |
| 2019-05-01   | Rett         | Poster: Quantifying Stereotypic Hand Movements in Rett Syndrome | Society of Biological Psychiatry (SOBP, 74th Annual Meeting) |
| % 2019-05-01 | CVN - Dropout    | TEDS Dropout Exercise: Hindsight or Prediction (Paper Critique and Original Analysis) | Internal |
| % 2019-05-01 | CVN - Dropout    | TEDS Dropout Exercise: On Ordinal Variables and Random Forests| Internal |
| % 2019-05-01 | CVN - Dropout    | TEDS Dropout Exercise: On Nominal Variables and Random Forests| Internal |
| x 2019-05-20 | Rett/Gestures    | Gesture Recognition - Project Updates | Internal meeting |



# Associate Director of Digital Health, Early Signal Team (July 2019 - January 2020)

| Date | Project | Name | Where |
|------|---------|------|-------|
| 2019-07-10 | CVN - Dropout    | Forecasting Patient Dropout         | CVB CWM 2019-Q2 |
| 2019-07-11 | CVN - Dropout    | Clinically Viable Prediction Models | CVB CWM 2019-Q2 |
| 2019-07-11 | CVN - Dropout    | TEDS Dropout Exercise: Data Leakage and Illegitimacy | CVB CWM 2019-Q2 (impromptu session during lunch) |
| 2019-08-26 | CVN - Dropout    | Dropout Exercise: The TEDS Dataset (Info Deck) | CVN, CVB |
| 2019-08    | Misc      | Hyperparameter Exploration (Modeling Impacts) | CVB |
| x 2019-09 .. | ..        | .. | CVB CWM Q3 -- FIND PREZ !! |
| 2019-10-11 | Misc/John | Frequency Analysis (Tutorial Support) | John |
| 2019-10-18 | Rett      | Poster: Quantifying Stereotypic Hand Movements in Rare Disorders Using IMU Sensors and Deep Learning Algorithms | National Organization for Rare Disorders (NORD, 2019 Meeting) |
| x 2019-09 .. | CWM  | ... | CVB CWM Q4 -- FIND PREZ !!! |


# Associate Director of Data Science (Digital Health), Data Science Team (January 2020 - July 2021)

| Date | Project | Name | Where |
|------|---------|------|-------|
| 2020-01-02 | MJFF, Rett    | Exploring Public Datasets (w/ an eye to Transfer Learning) | MJFF Update |
| 2020-03-23 | MJFF          | PPMI-Verily Wearables: Phase 1 Research Plan | MJFF, SoW slides for MJFF-CVB Digital Health |
| 2020-04-24 | WWG (EaSiEco) | EaSi Ecosystem Info Deck | CVB-WWG w/ Deepti; w/ only minor updates since its use in 1-on-1s w/ Zhanna |
| 2020-06-04 | WWG           | CVB-MJFF Partnership: the PPMI-Verily Dataset | CVB Wearables Working Group w/ Deepti, Zhanna, etc |
| 2020-07-02 | MJFF, Rett    | Gestures and HAR: "In the Lab" & "Out in the Wild" | Sensor Analytics Meeting |
| 2020-07-08 | MJFF, Rett    | Gestures and HAR: "In the Lab" & "Out in the Wild" | CVB-CWM 2020-Q2 |
| 2020-08-25 | EaSi Platform | Shimmer Data Processing Updates | CVB: Enabling Tech Team |
| 2020-09-24 | Rett          | Rett Trial Feasibility | CVB: Enabling Tech and Clinical Teams |
| 2020-09-25 | Rett | Rett Analytics Plan (INCOMPLETE) | CVB: DS and Clinical Teams |
| 2020-10-16 | EaSi Platform PoC | TimeScaleDB Installation on MacOS | CVB: Enabling Tech Team |
| 2020-10-19 | MJFF      | PPMI-Verily Project Updates: Transfer Learning, Data Augmentation, Unsupervised Domain Adaptation | Presentation to MJFF w/ Roozbeh |
| 2020-10-20 | EaSi Platform PoC | TimeScaleDB Setup and Ingestion   | CVB: Enabling Tech Team |
| 2020-10-27 | Mgmt      | 1-on-1s w/ Lee & Kevin | CVB |
| 2020-11-20 | MJFF      | PPMI-Verily Project Update: Deep Reconstruction-Classification Network (DRCN) | Updates and questions about paper submission |
| 2020-12-07 | Mgmt      | Overleaf/LaTex/Git: Potential Research Team Workflows |
| 2020-12-09 | Mgmt      | 2021 Sensor Analytics OKRs | Project managements slides for Lee |
| 2021-02    | Misc/Mgmt | Beamer Styles: Version-Controllable, LaTeX Style Presentations |
| 2021-03-11 | MJFF      | CVB Digital Health: 24/7 Sensor-Driven Support for Parkinson's Disease  | MJFF/CVB Annual Sync (2020-2021 Project Reviews) |
| 2021-06-30 | MJFF      | CVB Sensor Analytics: ML and DSP Applications to the PPMI-Verily Dataset | Roozbeh, Kevin - Invited Presentation at the PPMI Digital Health Working Group Q2 Meeting |


# Associate Director of Data Science (Digital Health), Data Science Team (July 2021 - January 2021)

| Date | Project | Name | Where |
|------|---------|------|-------|
| 2021-07-01 | Mgmt      | 1/2-Year Proj Mgmt Updates | CVB DS team mtg |
| 2021-07-13 | MJFF, CVB | Sensor Analytics Team: Wearables 101 | Roozbeh (prez), Kevin (mgr); CVB CWM Q2 |
| 2021-07-14 | MJFF      | Movement as a Case Study | Winner of the "invited keynote speakers"; CVB CWM Q2 |
| 2021-07-22 | MJFF      | PPMI-Verily Raw Sensor and Derive Data Projects & Analyses | Roozbeh, Kevin; proj update w/ MJFF |
| 2021-10-26 | MJFF      | 2021 PPMI-Verily Derived Data Project Review | MJFF Update |
| 2021-10-27 | Mgmt      | OKR-Driven TeamWork Practices: Mapping the OKR "Data Structure" to the TeamWork Workflow |  CVB CWM Q3 |
| 2021-12-   | MJFF      | Daily Monitoring of Parkinson's Disease: Signals of Motor Health and Sleep Hygiene | Roozbeh, Kevin - Invited Presentation at the PPMI Digital Health Working Group Q4 Meeting |
| 2021-12-17 | Mgmt      | Kevin's 2021 Lookback (Data Science End-of-Year Review Meeting) |

