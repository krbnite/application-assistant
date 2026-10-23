# Kevin Urban, PhD

Last updated: 2026-10-19

Research Scientist | Applied ML | Statistical Signal Processing | Sensor AI | Scientific Computing

[Email](mailto:kevin.ddu@gmail.com) | [LinkedIn](https://linkedin.com/in/machinesaidgo) | [GitHub](https://github.com/krbnite) | [Technical Writing](https://krbnite.github.io)


## Profile

Across physical, physiological, behavioral, and geophysical systems, my work focuses on turning noisy, indirect measurements into reliable models, estimates, and decisions. I build time-series and spatiotemporal ML models, statistical signal-processing methods, Bayesian estimators, computer-vision pipelines, and physics-informed simulations. My experience spans wearable and medical-device research, production customer analytics, research software, and distributed geophysical observations. I remain hands-on across problem formulation, implementation, experimental design, validation, and research-to-product translation, with particular attention to data quality, uncertainty, and the conditions under which a model can be trusted.


## Core Research Themes

- **Time-series and spatiotemporal ML:** Built sequence models, weakly supervised wearable pipelines, spectral/time-frequency methods, DTW validation frameworks, and spatiotemporal representations across biosignal, thermal, image, and geophysical data.
- **Sensor inference under uncertainty:** Designed Bayesian, streaming, and adaptive estimators for indirect physiological and physical measurements where uncertainty, drift, irregular sampling, and hardware artifacts are central rather than incidental.
- **Simulation and synthetic data:** Built physics-informed thermal models, synthetic thermogram generation, dynamical-system simulations, and visualizations to reason about sparse observations and latent process behavior.
- **Deployment-honest validation:** Repeatedly redesigned evaluation methods to reflect real deployment conditions, including leave-one-subject-out validation, leakage audits, staged/prospective pilot studies, and model stress tests under distribution shift.

## Experience


### Podimetrics

**Principal Data Scientist | Remote | Dec 2024 - Apr 2026**

Adaptive statistical estimation, computer vision, and physics-informed modeling for FDA-cleared remote-monitoring products using thermal arrays and pressure sensors for diabetic foot ulcer detection and fall-risk assessment.

- **On-device fall-risk estimation:** Designed and implemented streaming fall-risk estimators for SmartMat+, a battery-powered patient-facing edge device enabling near-real-time risk updates after a 17-second pressure-sensor session. Prototyped Bayesian and weighted-window approaches in Python, selected the strongest estimator, translated it to C, validated numerical equivalence, and supported firmware integration for prospective testing.
- **Adaptive fall-risk monitoring:** Reduced time to reliable patient-specific estimates from roughly 20-30 days to 3-5 days through adaptive streaming estimation and Bayesian cold-start methods.
- **Robust estimator validation:** Benchmarked candidates on synthetic, staged, and prospective datasets, progressing from 5-participant internal testing to a 10-recruit characterization study and a 3-month, 30-patient pilot while stress-testing drift, regime shifts, outliers, irregular sampling, cold-start behavior, and long-horizon error accumulation.
- **Adaptive alert logic:** Designed baseline-updating and alert-triggering logic for longitudinal fall-risk monitoring from pressure-derived stability metrics, evaluating deviations from individualized baselines and requiring time-bounded persistence before clinical escalation.
- **Production thermal-imaging algorithms and pipeline ownership:** Owned the production thermal-imaging, modeling, and detection pipeline; substantially refactored the Python codebase, integrated consultant-supplied data-quality modules, and extended localization, left/right classification, segmentation, scan-quality handling, and anatomical keypoint temperature extraction for a deployed platform serving roughly 15k active patients and 25k lifetime patients.
- **SmartMat+ thermal algorithm adaptation:** Adapted the production thermal pipeline for SmartMat+ by adding device-specific processing for its different sensor-matrix shape, training new machine-learning and calibration models, and collaborating with hardware engineering on data collection and validation and software engineering on sandbox testing and Git workflows.
- **Physics-informed thermal modeling:** Developed physics-informed thermal models to support algorithm development and evaluation, including a synthetic thermogram generation framework for realistic spatiotemporal simulation and a Newtonian heat-transfer model for extrapolating short-duration thermal scans toward thermal equilibrium.
- **Personalized DFU detection prototype:** Developed and presented an adaptive temperature-asymmetry model for thermal-scan diabetic foot-ulcer detection, using individualized conservatively updated thermal baselines to improve robustness for patients with Charcot foot, peripheral arterial disease, or changing health status.
- **PR-triggered pipeline sandbox validation:** Validated thermal-processing and model-inference changes in isolated clones of the production AWS environment, using PR-triggered Terraform/GitHub Actions provisioning, configuring scan-processing workflows and pipeline revisions, and submitting scans to exercise the integrated system.
- **Next Best Action analytics:** Co-designed an analytical framework combining quasi-experimental methods with baseline-adjusted behavioral response metrics to evaluate intervention effectiveness, support patient segmentation, optimize reengagement channels, and enable future A/B testing and personalized outreach.
- **Cross-functional technical leadership:** Served as the primary scientific partner to software and hardware engineering teams, advising on algorithm integration, sensor behavior, scan-processing pipelines, validation methodology, and implementation decisions to ensure production systems preserved the integrity of physiological data and scientific conclusions.

### Cohen Veterans Bioscience

**Research Scientist - Wearable ML & Signal Processing**

**Official title: Director of Data Science & Digital Health | New York, NY | Jul 2021 - May 2024**

**Official title: Associate Director of Data Science - Sensor Analytics | New York, NY | Jun 2019 - Jul 2021**

**Official title: Senior Data Scientist, Early Signal Team | New York, NY | Jul 2018 - Jun 2019**

Hands-on research across physiological time-series modeling, wearable study design, clinical prediction, reusable ML software, and scientific validation.

- **Wearable gesture recognition:** Built Conv1D-LSTM gesture-recognition models for Rett stereotypy detection across Shimmer IMUs, Apple Watch, and Oura Ring datasets; informed IMU sampling-rate decisions using Nyquist reasoning and 25-400 Hz ablations, showing that higher sampling rates degraded classification performance.
- **Deployment-honest validation:** Identified overlapping-window data leakage, time-ordering bias, and evaluation-target mismatch in a gesture-recognition prototype, then redesigned validation around leave-one-subject-out cross-validation to estimate unseen-patient generalization in a small cohort.
- **Wearable study design and evaluation:** Co-developed in-lab and longitudinal home-use wearable protocols with a partner hospital for personalized Rett syndrome monitoring, then reconstructed and audited multimodal data from smartwatch sensors, video recordings, and behavioral annotations post-collection, identifying missing or inconsistently documented sensor-synchronization procedures, timestamp inconsistencies, annotation ambiguity, limited behavioral coverage, and temporal-alignment limits that made brief behavioral events unreliable targets for patient-specific stereotypy detection.
- **Free-living Parkinson's monitoring:** Used a weakly supervised walk-detection framework to restrict disease inference to gait-relevant, walk-like intervals within unconstrained free-living recordings, then applied an end-to-end deep neural network to discriminate Parkinsonian gait from healthy controls with approximately 90% single-event accuracy and 100% daily majority-vote accuracy.
- **End-to-end biosignal modeling:** Adapted an end-to-end Conv1D-LSTM architecture from wearable gesture recognition to ECG sleep-apnea detection, then validated the approach through ablation studies that progressively replaced a classical signal-processing, handcrafted-feature, and SVM pipeline with learned representations; the TensorFlow/Keras framework was later ported to PyTorch and adapted to Parkinson's disease monitoring.
- **Cross-domain representation learning:** Explored DRCN-style reconstruction/classification networks, variational autoencoder architectures, transfer learning, and unsupervised domain adaptation for wearable physiological time series, using TensorFlow/Keras and PyTorch prototypes with shared representations and pseudolabel concepts to adapt general activity models toward new sensors, subjects, and clinical datasets.
- **Sleep sensor validation:** Reframed conventional PSG/actigraphy validation methodology by developing a DTW-based evaluation framework accounting for systematic physiological timing differences in sleep onset between EEG- and motion-based measurements.
- **SensorNet reusable biosignal modeling package:** Developed SensorNet, an internal, pip-installable package for the Sensor Analytics Team, consolidating recurring Conv1D-LSTM implementations into a configurable model class with training, updating, and inference methods plus DTW-like and time-series augmentation utilities; pinned installations to documented revision hashes for reproducibility as the package evolved.
- **Large-scale wearable data processing:** Converted free-living multimodal wearable recordings into a queryable local database, enabling efficient slicing, temporal alignment, quality auditing, and model development without loading full sensor streams into memory.
- **Clinician-friendly machine learning:** Built Random Forest and XGBoost models to predict patient dropout risk from longitudinal EHRs, using SHAP, LIME, and feature-importance analyses to make model behavior interpretable for skeptical clinical stakeholders.
- **Early-term birth prediction:** Collaborated with Columbia University on maternal-health prediction using clinical and Columbia-provided EEG-derived features, focusing on hyperparameter tuning, model selection, missing-data handling, and leakage detection.
- **Sensor-driven questionnaire estimation:** Proposed a Sensor-Driven Questionnaire Estimation framework for estimating clinic-administered assessments from passive sensor signals, targeting the PHQ-9 depression screener first based on initial supporting evidence and availability. Developed literature-grounded synthetic examples and envisioned an extension to a continuously updated patient-state proxy refined through Kalman-filter-style data assimilation when observed assessment scores became available.
- **Wearables knowledge graph and database evaluation:** Evaluated graph, document, relational, time-series, and key-value databases for a wearable-to-biological-phenomenon knowledge graph; designed schema iterations and demonstrated Neo4j/Cypher query patterns for many-to-many mappings among sensors, algorithms, symptoms, disorders, and physiological signals.
- **AWS research-computing access and workflow tooling:** Configured an EC2/Linux research environment and created login, synchronization, IAM role-assumption, and EC2-selection scripts for personal and team use, reducing workflow friction on a newly introduced cloud research system.
- **Cross-project scientific code and leakage review:** Reviewed other researchers' software packages and modeling pipelines across projects, identifying data-leakage risks and scrutinizing implementation choices that affected the validity of scientific results.
- **Parkinson's digital biomarkers:** Named, built, and led the Sensor Analytics Team; secured a Michael J. Fox Foundation grant and its second-year renewal to develop digital biomarkers for longitudinal Parkinson's disease monitoring using Verily Watch data from PPMI.
- **Reproducible team workflows and tooling:** Created reusable project-organization practices, code-review patterns, and technical tutorials to reduce reproducibility friction and technical debt across data science research projects.

### WWE

**Senior Data Scientist | Stamford, CT | Aug 2017 - Jul 2018**

**Data Scientist | Stamford, CT | Oct 2016 - Aug 2017**

- **Deep learning for churn prediction:** Replaced a logistic-regression-based churn prediction system with a 5-layer neural network, improving total AUC from approximately 0.64 to 0.73; independently developed Gaussian noise injection between hidden layers as a regularization strategy, contributing approximately half of the overall performance gain.
- **Transfer learning and fine-tuning for computer vision:** Built a 20-class WWE Superstar image-recognition prototype by fine-tuning ImageNet-pretrained VGG16 with a custom classification head, two-phase frozen-base/top-block-unfrozen training, heavy data augmentation, VGG16/VGG19/ResNet50 comparison, and confidence-thresholded out-of-roster rejection under roughly 50 images per class.
- **Live-event data products and executive reporting:** Owned collection, transformation, analysis, and table preparation for executive live-event reporting across YouTube, WWE Network, Facebook, and Twitter, implementing most pipelines directly and delegating Twitter collection to a direct report; partnered with the manager responsible for Tableau SQL and visualizations. These API-based data products replaced vendor feeds costing roughly $1M/year.
- **Live-event analytics latency reduction:** Co-developed multi-platform live-event reporting workflows that captured viewership metrics across YouTube, Facebook, Twitter, WWE.com, and WWE Network within minutes of broadcast, replacing manual cross-team reporting processes that previously took 12-24 hours.
- **AWS automated scoring to Redshift:** Developed and maintained AWS-hosted automated web-scraping, API collection, model-scoring, and reporting workflows, using cron to schedule hourly/daily data collection and daily analytical reports; churn-model scores were written to Redshift for marketing and product dashboards.
- **Shared GPU-enabled AWS/Linux research environment:** Administered a GPU-enabled AWS EC2/Linux instance shared by three users, configuring user accounts, private and shared directory permissions, NVIDIA/TensorFlow dependencies, and Jupyter and RStudio servers while troubleshooting colleagues' environment issues.
- **Reusable R ingestion-to-reporting package:** Built an R package spanning SFTP data ingestion, parsing and transformation, analysis, plotting, and HTML/PDF report generation for stakeholder email distribution; handed the package off to consultants to run and maintain.
- **Revenue attribution and behavioral research:** Built revenue-attribution, survey-fusion, sentiment-analysis, seasonal-behavior, and customer-behavior analyses over large-scale WWE Network and social-platform datasets to support segmentation, marketing decisions, churn/winback forecasting, and stakeholder reporting.
- **Streaming-account anomaly and enforcement investigation:** Investigated anomalous WWE Network account usage by rebuilding SQL analyses and mapping device activity, revealing individual accounts with 200+ devices streaming simultaneously across countries and exposing a failure to enforce the platform's two-device concurrency limit.

### Center for Solar-Terrestrial Research

**Research Assistant, New Jersey Institute of Technology | Newark, NJ | Aug 2012 - May 2016**

PhD research inferred polar-cap electrodynamics from distributed magnetometer, satellite, and spacecraft observations using novel spectral methods for noisy geophysical time series.

- **Polar-cap inference and coordinate validation:** Developed median-relative spectral analysis over 63-day Antarctic magnetometer baselines to test how magnetic coordinates mapped ground sensors into the magnetosphere, revealing hidden polar-cap structure and showing how widely used coordinates could misclassify high-latitude sites; motivated observational representations that better separated deep polar-cap behavior from boundary-straddling, cusp-like behavior.
- **Solar-wind forecasting and inverse nowcasting:** Developed dynamic lagged-correlation analyses linking deep polar-cap ground-sensor power to upstream solar-wind magnetic-field fluctuations, supporting an inverse remote-sensing approach for nowcasting near-Earth solar-wind state parameters.
- **Geophysical signal interpretation:** Analyzed ground magnetometer observations by disentangling overlapping effects from coastline geometry, crustal conductivity, ionospheric conductivity, and solar-wind coupling.
- **Multi-instrument space weather reconstruction:** Reconstructed and animated heliospheric event timelines as dynamic global visualizations of space weather propagation across a distributed instrument chain spanning the Sun to the heliosheath, integrating observations from SDO, ACE, approximately 180 INTERMAGNET magnetometers, the Antarctic AGO network, DMSP satellites, the Van Allen Probes, and Voyager 2.
- **Computational mathematics, granular fluids, and nonlinear dynamics:** Translated analytical models of granular fluid dynamics into numerical simulations and visualizations, including parameterized Poincare map analyses of chaotic dynamical systems, contributing to four peer-reviewed publications from 2011-2014.
- **Scientific collaboration:** Contributing member of the NASA RBSPICE instrument team on the Van Allen Probes mission; delivered invited talks at AGU, the Air Force Research Laboratory, and CEDAR.

## Selected Independent Research & Software Projects

- **Self-supervised behavioral video analysis:** MachineSaidGo / independent R&D: Designed and prototyped self-supervised deep learning architectures for mouse behavioral analysis from video, exploring activity classification and anomaly detection from unlabeled video sequences using PyTorch and computer-vision libraries.
- **Granular-dynamics surrogate modeling:** MachineSaidGo / independent research collaboration: Collaborated with mechanical-engineering researchers on RNN forecasting and PyTorch surrogate-modeling approaches for computationally expensive tapped-granular-system simulations, extending a long-running nonlinear-dynamics and scientific-simulation research thread.
- **ProblemForm:** Built a human-AI problem-formulation system with a multi-phase LLM refinement pipeline, CLI, benchmark suite, rubric/property-based evaluation framework, and documented methodology for improving questions, prompts, decisions, plans, and specifications before downstream execution.
- **Application Assistant:** Built an agent-assisted document-generation workflow connecting reusable evidence banks with DOCX and Markdown generation, traceable selection decisions, public-content safeguards, and validation checks.

## Internships

- **Trajectory Optimization and Design - NASA Jet Propulsion Laboratory**, Pasadena, CA (May-Aug 2011). Full spacecraft mission design to Jupiter's Trojan asteroids: science goals, instrument selection, trajectory optimization, concurrent engineering, and formal NASA review board presentation; contributing author on peer-reviewed paper.
- **Observational Cosmology Laboratory - NASA Goddard Space Flight Center**, Greenbelt, MD (Summer 2007). Developed software to model data collection and analysis for the Absolute Spectrum Polarimeter, a proposed spacecraft instrument for detecting B-mode gravitational-wave signatures.
- **Heliophysics Division - NASA Goddard Space Flight Center**, Greenbelt, MD (Summer 2006). Developed web content and gained early experience with Python, HTML, CSS, JavaScript, PHP, and UNIX command-line tools.

## Technical Skills

**Machine learning:** Deep learning; sequence modeling with Conv1D/CNNs, LSTMs, transformers, and TCNs; representation learning; autoencoders/VAEs; transfer learning; fine-tuning; self-supervised learning; tree-based learning; clustering; explainable AI with SHAP and LIME; computer vision; image localization/segmentation; human activity recognition; gesture recognition; synthetic data generation; physics-informed modeling; model selection; validation/verification; ablation studies.

**Statistical signal processing and estimation:** Bayesian inference; inverse problems; state estimation; stochastic filtering; Kalman filtering; recursive Bayesian estimation; adaptive estimators; tracking; uncertainty-aware modeling; drift/regime-shift analysis; robustness testing; Normal-Inverse-Gamma priors; time-series and longitudinal modeling; spatiotemporal modeling; time-frequency methods; STFT; PSD/spectral analysis; wavelets; coherence analysis; time-series similarity and alignment with DTW.

**Sensor analytics and modalities:** IMUs, accelerometers, gyroscopes, ECG, pressure sensing, thermal imaging, magnetometers, cameras, medical devices, satellites/spacecraft, sensor fusion, multimodal sensing, physiological sensing, wearables, longitudinal monitoring, digital biomarkers, field validation, sensor synchronization, embedded deployment.

**Languages and tools:** Python, PyTorch, TensorFlow/Keras, OpenCV, HuggingFace, scikit-learn, SciPy, NumPy, MLflow, C, R, MATLAB, IDL, SQL, Linux, Docker, Git, Jupyter, AWS, GCP, Bash, GitHub Actions, cron; reusable package development and version-pinned dependencies; integration testing in team-provisioned Terraform/AWS sandboxes.


## Education

**PhD, Physics:** New Jersey Institute of Technology / Rutgers University, 2016.

**MS, Applied Physics:** Minor in Applied Math, NJIT / Rutgers University, 2010.

**BS, Applied Physics:** Minor in Applied Math, NJIT / Rutgers University, 2008.


## Selected Training

- Udacity Deep Learning Nanodegree, 2017.
- Intel IoT Edge AI Scholarship.
- Building with the Claude API.

## Publications, Research Writing & Selected Presentations

- Atri, R. and Urban, K. (co-first authors) et al. "Deep Learning for Daily Monitoring of Parkinson's Disease Outside the Clinic Using Wearable Sensors." Sensors, 2022.
- Urban et al. "Rethinking the Polar Cap: Eccentric Dipole Structuring of ULF Power." JGR: Space Physics, 2016.
- Blackmore et al. "Analysis, simulation and visualization of 1D tapping via reduced dynamical models." Physica D: Nonlinear Phenomena, 2014.
- Diniega et al. "Mission to the Trojan Asteroids: Lessons Learned During a JPL Planetary Science Summer School Mission Design Exercise." Planetary and Space Science, 2013.
- Rosato et al. "Dynamical systems model and discrete element simulations of a tapped granular column." Powders and Grains, AIP Conference Proceedings, 2013.
- Urban et al. "Quiet Time Observations of the Open-Closed Boundary Prior to the CIR-Induced Storm." Space Weather, 2011.
- Blackmore et al. "Tapping dynamics for a column of particles and beyond." Journal of Mechanics of Materials and Structures, 2011.
- Blackmore, Urban, and Rosato. "Integrability analysis of regular and fractional Blackmore-Samulyak-Rosato fields." Condensed Matter Physics, 2010.
- Urban, Kevin. "The hydromagnetic structure of the polar cap and its interaction with the solar wind." PhD dissertation, NJIT / Rutgers University, 2016.
- Atri, R. and Urban, K. "Augmented Unsupervised Domain Adaptation for Deep Time Series Models." Working paper / unpublished.
- Urban, K. and Atri, R. "Evaluating the impact of domain expertise and deep learning in the design and performance of sleep apnea detection models." Working paper / unpublished.
- Urban, K. "Bounded Dynamic Time Warping for Epoch-by-Epoch Agreement Between Polysomnography and Sleep-Tracking Devices." Manuscript in preparation.
- Urban, K. "Are Wearables Worth the Hype?" Cohen Veterans Bioscience public science article / Q3 newsletter, 2020.
- Postma, F., Rozenberg, Z., Shokhirev, N., Urban, K., Rubin, U., and Brunner, D. "Technical Performance Verification of Wearable and Home Sensor Devices Monitoring Sleep: Best Practices." Conference abstract/poster, Biological Psychiatry 87(9), S343, 2020. DOI: 10.1016/j.biopsych.2020.02.880.
- Rosato et al. "Tapped Granular Systems: Simulations and Machine Learning Approaches." 75th Annual Meeting of the APS Division of Fluid Dynamics, 2022. Conference abstract / oral presentation.
- "Daily Monitoring of Parkinson's Disease: Signals of Motor Health and Sleep Hygiene." Invited presentation, Michael J. Fox Foundation Digital Health Working Group, December 10, 2021.
- "Machine Learning and Signal Processing Approaches to the Verily Watch Dataset." Invited presentation, Michael J. Fox Foundation Digital Health Working Group, June 30, 2021.
- "Transitioning from Academic Research to Industry Data Scientist." Invited presentation, NASA Goddard Space Flight Center Internship Lecture Series, July 27, 2021.
- "Quantifying Stereotypic Hand Movements in Rare Disorders Using IMU Sensors and Deep Learning Algorithms." Conference presentations, Society of Biological Psychiatry, May 16, 2019, and National Organization for Rare Disorders, October 18, 2019.

## Selected Awards

- Received two 2023 CVB Milestone Achievement Awards for project execution, research leadership, and cross-functional collaboration.
- CVB Award for Best Keynote Speaker, "Movement as a Case Study," 2021.
