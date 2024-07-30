


## MJFF
* Role: Project manager, R&D
* Presentations 
  - CVB/MJFF Working Group
    * 2021-03: CVB Digital Health: 24/7 Sensor-Driven Support for Parkinson's Disease  (2021 MJFF/CVB Annual Sync)
    * 2021-01: PPMI-Verily Project Update: Deep Reconstruction-Classification Network (DRCN)
    * 2021-06: CVB Sensor Analytics: ML and DSP Applications to the PPMI-Verily Dataset (Invited talk; Co-Presenter with Roozbeh)
* Project Management
  - Funding Acquisition
    * 2021-01: 2021 CVB-MJFF Digital Health Proposal: High-Level Overview (Internal)
    * 2021-01: 2021 CVB-MJFF Digital Health Proposal (Internal Review)
    * 2021-02: CVB-MJFF Digital Phase2 Proposal (Official Release to MJFF) 
  - Planning/Strategy 
    * 2021 OKRs, 6-month goals, project charter
    * 2021 MJFF "Quick Win" Check List: Priorities, Plans, and Timelines (Internal) |
* Research Papers
  - Augmented Unsupervised Domain Adaptation for Deep Time Series Models (DRCN paper, Unpublished)
  - Daily Monitoring of PD Outside the Clinic


## Rett/Gestures
* Lit Reviews, Write-Ups
  - 2021-01-21: Idiosyncratic Stereotypies: Overview of Stereotypy Types and Prevalance in Rett 
    * Lit review and Reference Materials
  - 2021-04-08: Revisiting the Rett Study's Literature Review: An Updated Overview
    * Internal write-up (tons of notes, thoughts, etc)
  - 2021-04-09: Section 1.1 of Rett Grant Proposal: "Relevant Literature and Data" (Protocl/Grant Contribution) | 
    * Official, external-facing write-up


## EaSi Platform - Sleep Data Visualization
| 2021-07-01 | Write-Up | EaSi Platform | Python Package Best Practices (Hint: Use Type Hints) |
| 2021-07-01 | Write-Up | EaSiPlatform | How to use the SleepViz Jupyter Notebook (Documentation, v1) |


## EEG Working Group
| Date | Type | Relevance | Thing |
|---|----|---|---|
| 2021-03-17 | Write-Up | EEG, Project/Team MGMT | EEG-WG Project Organization and Suggested Git/GitLab Practices |
| 2021-04-06 | Write-Up | EEG, Documentation | Notes on Setting and Using Open-BCI EEG Headset |


## Misc
### Data Science Blog
| Date | Type | Relevance | Thing |
|---|----|---|---|
| 2021-02-xx | Presentation | DS Blog, Misc | Beamer Styles: Version-Controllable, LaTeX Style Presentations |
| 2021-03-12 | Write-Up | DS Blog - Misc | Convert your Markdown to Beautiful Presentations with "Markdown-Slides" Tool |
| 2021-03-18 | Write-Up | DS Blog - Machine Learning | On Splitting Time Seres for Model Training (Cliff Notes) |


### Computing Environments
| Project | Env Type | Comments |
|---------|----------|----------|
| EEG-WG | Conda | Attempts platform-independent build; starts w/ a suggestive yml file (constrained only to python version and channels to retrieve pkgs) and creates a temporary conda env; it then identifies Conda's solution to each requested pkg and creates a new yml file by updating the original w/ the sol'n's pkg versions (not for all pkgs in evn, but for the few specified in original temp yml file); uses the documented temp env to build a non-conda-listed eeg pkg (autoreject) using `conda skeleton`; it first builds on my macbook, then converts the build to many other OS architectures; finally, the platform-ind env can be built by anyone now...same basic env but now can specify the os-arch for the eeg autoreject pkg; the env is uploaded to anaconda acct (though havne't used that feature) |
| SleepViz | Conda | Simple like INT003 (but w/ different specs); comes w/ some helper-tool bash scripts |


### Management
| Date | Type | Relevance | Thing |
|---|----|---|---|
| 2020-02-10 | Write-Up | MGMT, Executive Decision Support | DS-Adjacent Needs for EaSi Platform |
| 2020-12-09 | Presentation | Mgmt      | 2021 Sensor Analytics OKRs (Project Management) |
| 2021-02-23 | Write-Up | MGMT, B2B Interview Script | Introducing EaSi-CVB to BizNameHere |


### Awards
* 2021-07 (CVB CWM): MJFF Wearable Project Delivery and Renewal
* 2021-07 (CVB CWM): Best Keynote
