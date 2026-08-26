# JD Cluster Bank

This file is a lightweight index for mapping future job descriptions to Kevin's resume profile clusters.

It is not meant to become a full archive of every pasted job description. The preferred steady state is one synthesized "archetype JD" per profile cluster, built from multiple real JDs. Individual recovered JDs should be used as source examples, then distilled into the cluster archetype so the file does not become bloated.

## Source Files

- `MASTER_RESUME_TEMPLATE.md` - canonical resume structure and section placeholders.
- `PROFILE_BANK.md` - canonical source of profile/headline clusters.
- `RESUME_TAILORING_AGENT.md` - process instructions for tailoring.
- `RESUME_BULLET_BANK.md` - canonical evidence reservoir and cluster-scored resume bullet guide.
- `OUTPUT_CONTRACT.md` - output requirements for tailored application packets.
- `TAILORED_RESUME_AUDIT_TEMPLATE.md` - audit template for tailoring decisions.

## Cluster Mapping From 2026 Company-Specific Resumes And Recovered JDs

These mappings began as inferences from the tailored resumes in the 2026 search folder and were updated after Kevin added the recovered job descriptions on 2026-08-21.

| Company / Folder | Primary Cluster | Secondary Cluster | Confidence | Notes |
|---|---|---|---|---|
| Kobold | Bayesian Estimation, Signal Processing, And Physical Systems Research | Sensor AI / Edge Perception | High | Earlier resume foregrounded Bayesian estimation, sensor fusion, spatiotemporal perception, and physical-system inference. |
| Oura | Health, Wearables, Neurotech, And Digital Biomarkers | Default Sensor ML Research Scientist | High | Wearables, physiological sensing, sleep, digital biomarkers. |
| Omada | Health, Wearables, Neurotech, And Digital Biomarkers | Industrial And Operational Time-Series ML | High | Digital health plus intervention/decision-support analytics. |
| Beacon Biosignals | Health, Wearables, Neurotech, And Digital Biomarkers | Bayesian / Signal Processing | High | Clinical biosignals, neurological sensing, validation-heavy health ML. |
| General Motors | Sensor AI, Robotics, Autonomy, And Edge Perception | Industrial And Operational Time-Series ML | High | Autonomy / sensing / robust model validation likely dominate. |
| Oden Technologies | Industrial And Operational Time-Series ML | Sensor AI / Edge Perception | High | Industrial analytics, operational monitoring, production systems. |
| Trackman | Sensor AI, Robotics, Autonomy, And Edge Perception | Bayesian / Physical Systems Research | High | Sensor/perception/trajectory-style applied physical inference. |
| Compound Eye | Sensor AI, Robotics, Autonomy, And Edge Perception | Bayesian / Physical Systems Research | High | Perception, cameras/sensors, autonomy-adjacent framing. |
| Ionosphere | Bayesian Estimation, Signal Processing, And Physical Systems Research | Default Sensor ML Research Scientist | High | Geophysical/spatiotemporal inference and space-weather background are central. |
| 4MP | Closed-Loop Physical AI And Self-Learning Systems | Industrial / Operational Time-Series ML | High | JD is specifically about learning from correction outcomes, physical feedback loops, uncertainty guardrails, inverse problems, and staged rollout. Keep as a provisional retained cluster. |
| Lumicity | Health, Wearables, Neurotech, And Digital Biomarkers | Industrial And Operational Time-Series ML | Medium-High | Regulated medical algorithm work on complex sensor data; broader than wearables/neurotech but fits the health/clinical algorithm profile best. |
| Cutsforth | Industrial And Operational Time-Series ML | Bayesian / Physical Systems Research | High | Industrial monitoring and physical-system reliability likely dominate. |
| Cargill | Industrial And Operational Time-Series ML | Sensor AI / Edge Perception | High | Industrial/operational analytics with production decision-support framing. |
| Samsara | Sensor AI, Robotics, Autonomy, And Edge Perception | Industrial And Operational Time-Series ML | High | Edge devices, perception, deployed sensor systems, robust validation. |
| Oxman | Bayesian Estimation, Signal Processing, And Physical Systems Research | Default Sensor ML Research Scientist | High | Research themes, physics-informed modeling, spatiotemporal inference, synthetic data. |
| Motif Neurotech | Health, Wearables, Neurotech, And Digital Biomarkers | Bayesian / Signal Processing | High | Neurotech, biosignal/wearable sensing, clinical/device validation. |
| Dexcom - Emerging Sensing Technologies | Health, Wearables, Neurotech, And Digital Biomarkers | Bayesian / Physical Systems Research | Medium-High | CGM/biosensing algorithm role with strong mechanistic modeling, simulation, feasibility, and performance-limit analysis signals. |
| Dexcom - Advanced Sensing Technologies | Health, Wearables, Neurotech, And Digital Biomarkers | Bayesian / Physical Systems Research | High | CGM/biosensing algorithm role emphasizing signal processing, estimation, calibration, detection, sensor-behavior modeling, algorithm maturation, verification strategy, and hardware/firmware/product integration. |
| Senseonics | Health, Wearables, Neurotech, And Digital Biomarkers | Bayesian / Physical Systems Research | High | Implantable CGM algorithm-development role emphasizing mathematical modeling, signal processing, Python/MATLAB/C/C++ scientific computing, data-processing pipelines, unit tests, and sensor performance/accuracy investigations. |
| Atria Health | Health, Wearables, Neurotech, And Digital Biomarkers | Default Sensor ML Research Scientist | Medium-High | Clinical AI scientist role emphasizing foundation-model-adjacent medical models, multimodal health data, fine-tuning/post-training literacy, rigorous evaluation, and patient-level adaptation. |
| Voleon | Quantitative Research ML Engineering | Bayesian / Signal Processing; Industrial / Operational Time-Series ML | High | Research-team ML engineering role emphasizing mathematical maturity, production-quality research code, data pipelines, feature engineering, validation, model evaluation infrastructure, reproducibility, and imperfect heterogeneous data. |

## Preferred Workflow: Source JDs To Archetype JD

For each profile cluster:

1. Collect several real JDs that clearly belong to the cluster.
2. Extract compact fingerprints from each JD: responsibilities, requirements, keywords, hidden concerns, and tone/culture signals.
3. Merge those fingerprints into one generic archetype JD for that cluster.
4. Use the archetype JD as the comparison target when a new JD arrives.
5. Update the archetype only when a new JD adds a genuinely new recurring signal.

This avoids two failure modes:

- Overfitting the profile to one company's wording.
- Building a giant archive that future agents have to reread from scratch.

## JD Archetype Update Rules

Use these rules when a new JD is added after an archetype already exists.

### When A New Profile Cluster Is Needed

Create a new retained cluster when the JD exposes a materially different positioning problem that cannot be handled by lightly editing an existing profile. Do not discard the cluster merely because it is based on one JD.

For the initial archetype:

1. Add the company to the cluster mapping table.
2. Add a new row to `Current Archetype JD Status`.
3. Create a full archetype JD entry using the template below.
4. Mark the archetype as `Provisional` if it is based on one primary JD.
5. Use generic, reusable role language rather than the company's exact wording.
6. Save the source company in `Source JDs used`.
7. Put company-specific requirements that should not be generalized under `Gaps / do-not-overstate items`.
8. Update `PROFILE_BANK.md` only if the new cluster needs a distinct reusable intro/profile. Render and visually verify a DOCX only when producing a DOCX deliverable.

A provisional cluster can later be:

- Strengthened when more JDs reinforce it.
- Merged into a neighboring cluster if future evidence shows it was too narrow.
- Retired from active use only after Kevin explicitly decides it is no longer useful.

### When A New JD Strongly Matches An Existing Archetype

Compare the JD against the existing archetype and update only the reusable parts. Add the new JD to `Source JDs used` and update `Last updated` when any meaningful change is made.

When assigning a JD to a cluster, use `Core / necessary matching signals` to decide whether the archetype is a real match. Use `Variable / add-on signals` only after the cluster is selected, to decide what to emphasize in the tailored profile and bullet selection. Add-on signals should not outweigh missing core signals.

Example: FDA IDE/PMA language in the Motif JD is a strong health/neurotech tailoring signal, but it is not mandatory for the Health, Wearables, Neurotech, And Digital Biomarkers archetype. It belongs in `Variable / add-on signals`, while the core match is health/neurotech data, ML or biomarker work, and validation/product translation.

Add to the archetype when the new JD contributes one of these:

- A recurring or likely-recurring responsibility not already captured.
- A new role title or company context that improves future matching.
- A keyword family future searches should recognize.
- A hidden evaluation concern that changes how Kevin should frame evidence.
- A bullet-selection pattern that would affect future tailoring.
- A gap or do-not-overstate warning that protects against accidental overclaiming.

Do not update the archetype when the new JD merely restates existing signals, uses idiosyncratic company language, or adds a requirement too narrow to help future matching. If a single-source element is important but not yet clearly recurring, include it as an emerging signal or a do-not-overstate note instead of treating it as universal.

### Change Log

- 2026-08-21: Added Motif Neurotech JD to the Health, Wearables, Neurotech, And Digital Biomarkers archetype. Decision: no new cluster; Motif strongly matches the health/neurotech cluster while adding reusable signal around implantable neuromodulation, mental-health biomarkers, data/ML roadmap ownership, improvement-native products, fielded-product research, and FDA IDE/PMA data-feature constraints.
- 2026-08-22: Added Dexcom JD to the Health, Wearables, Neurotech, And Digital Biomarkers archetype. Decision: no new cluster; Dexcom strongly matches health/biosensing while adding reusable signal around continuous glucose monitoring, emerging biosensing technologies, first-principles/mechanistic modeling, simulation environments, technical feasibility, technology readiness, performance limits, and roadmap-facing advanced development.
- 2026-08-22: Added Dexcom Advanced Sensing Technologies JD to the Health, Wearables, Neurotech, And Digital Biomarkers archetype. Decision: no new cluster; the role reinforces Dexcom/biosensing while adding reusable signal around algorithm maturation, calibration/filtering and measurement-system algorithms, design tradeoffs, verification/validation strategy, hardware/firmware resource constraints, design controls, and transition from early concepts to scalable product integration.
- 2026-08-24: Added Senseonics Sr. Algorithm Development Engineer JD to the Health, Wearables, Neurotech, And Digital Biomarkers archetype. Decision: no new cluster; the role reinforces CGM/biosensing while adding reusable signal around Python/MATLAB/C/C++ algorithm-development tooling, reproducible data-processing pipelines, controlled unit tests, and data-driven sensor performance / accuracy investigations.
- 2026-08-25: Added Atria Health Senior AI Scientist JD to the Health, Wearables, Neurotech, And Digital Biomarkers archetype. Decision: no new cluster; Atria adds reusable signal around clinical foundation-model-adjacent model adaptation, open-source model evaluation, fine-tuning/post-training literacy, multimodal medical data, PHI-safe data hygiene, train/test contamination prevention, calibration/subgroup/error analysis, and general-to-patient model adaptation.

## Cluster Archetype JD Template

Use one entry per profile cluster.

```markdown
### Cluster Name - Archetype JD

- Source JDs used:
- Archetype role title(s):
- Typical company / product context:
- Core / necessary matching signals:
- Variable / add-on signals:
- Typical responsibilities:
- Typical requirements:
- Common keywords and phrases:
- Hidden evaluation concerns:
- Tone and culture signals:
- Best starting profile:
- Resume bullets usually retained:
- Resume bullets usually compressed or discarded:
- Gaps / do-not-overstate items:
- Last updated:
```

## Source JD Fingerprint Template

Use these only as inputs to the archetype JD. Keep them compact.

```markdown
### Company - Role Title

- JD source/date:
- Primary profile cluster:
- Secondary cluster, if any:
- Confidence:
- Why this cluster:
- Key JD signal words:
- Hidden evaluation concerns:
- Starting profile used:
- Profile/headline edits made:
- Master resume bullets to lead with:
- Master resume bullets to discard or compress:
- Gaps / do-not-overstate items:
- Notes for future similar roles:
```

## Current Archetype JD Status

| Profile Cluster | Archetype JD Status | Source JDs Used / Notes |
|---|---|---|
| Quantitative Research ML Engineering | Provisional synthesis 2026-08-24 | Voleon Senior Machine Learning Engineer. |
| Health, Wearables, Neurotech, And Digital Biomarkers | Updated 2026-08-25 | Oura, Omada, Beacon Biosignals, Lumicity, Motif Neurotech, Dexcom Emerging, Dexcom Advanced, Senseonics, Atria Health. |
| Sensor AI, Robotics, Autonomy, And Edge Perception | Synthesized 2026-08-21 | General Motors, Trackman, Compound Eye, Samsara. |
| Bayesian Estimation, Signal Processing, And Physical Systems Research | Synthesized 2026-08-21 | Kobold Data Scientist, Kobold Scientific Computing, Ionosphere, Oxman. |
| Industrial And Operational Time-Series ML | Synthesized 2026-08-21 | Oden Technologies, Cutsforth, Cargill, with Lumicity as a health/regulated-product bridge. |
| Closed-Loop Physical AI And Self-Learning Systems | Provisional synthesis 2026-08-21 | 4MP primary, with reinforcing signals from Oden, Cutsforth, Trackman, and GM. |
| Default Sensor ML Research Scientist | Fallback profile, not a separate JD archetype | Use when a new JD is broad or cross-domain enough that no specialized cluster dominates. |

## Synthesized Archetype JDs

### Quantitative Research ML Engineering - Provisional Archetype JD

- Source JDs used: Voleon Senior Machine Learning Engineer.
- Archetype role title(s): Senior Machine Learning Engineer, Research ML Engineer, Quantitative Research Engineer, ML Infrastructure Engineer for Research Teams, Applied ML Engineer.
- Typical company / product context: quantitative investment management, research-intensive AI/ML organizations, scientific or statistical modeling teams, productized research environments, and teams where PhD researchers need maintainable model, data, and experimentation systems.
- Core / necessary matching signals: the JD centers on translating research ideas or prototypes into production-quality code; it asks for strong mathematical maturity in statistics, probability, optimization, linear algebra, or ML; it emphasizes data ingestion, feature engineering, validation, quality monitoring, model evaluation, experiment tooling, reproducibility, and imperfect or heterogeneous data; it expects close collaboration with researchers or domain experts.
- Variable / add-on signals: quantitative trading, financial time series, alpha research, model-development frameworks, experiment management, ML workflow orchestration, distributed computing, model serving, feature stores, performance profiling, numerical-code optimization, R, C/C++, Linux, and production ownership for research systems.
- Typical responsibilities: partner with researchers to design, implement, and productize ML/statistical models; build and maintain data pipelines; develop feature engineering, validation, quality-monitoring, and model-evaluation infrastructure; translate prototypes into performant, well-tested, maintainable code; debug subtle data-quality issues; lead projects from requirements through delivery; set engineering standards inside research teams.
- Typical requirements: Python, NumPy, Pandas, SciPy, scikit-learn, PyTorch/TensorFlow or similar; Linux; software-engineering fundamentals; data structures, algorithms, systems design; statistics, probability, optimization, linear algebra; data-quality discipline; reproducibility; clear communication with researchers; often R, C/C++, distributed computing, model serving, feature stores, experiment management, or performance profiling.
- Common keywords and phrases: quantitative research, research engineering, production-quality code, production-ready models, data ingestion, feature engineering, validation, quality monitoring, model evaluation, experimentation lifecycle, ML workflow orchestration, model-development frameworks, numerical computing, statistical modeling, mathematical maturity, imperfect data, heterogeneous data, reproducibility, correctness, maintainability, performance profiling, financial time series.
- Hidden evaluation concerns: whether Kevin can transfer from sensor/health/geophysical ML to finance or other quantitative research domains; whether he has enough software-engineering depth for a senior MLE bar; whether distributed-computing and performance-optimization gaps are handled honestly; whether his broad research background lands as mathematical/productive rather than diffuse; whether he can collaborate with PhD researchers without over-indexing on domain narrative.
- Tone and culture signals: high technical bar, research-intensive, low tolerance for sloppy data or code, mathematically serious, collaboration with expert researchers, production quality, maintainability, autonomous ownership, detail orientation.
- Best starting profile: Quantitative Research ML Engineering.
- Resume bullets usually retained: Podimetrics robust estimator validation and Python-to-C estimator translation; CVB deployment-honest validation, large-scale data processing, reproducible workflows, and deep time-series/ablation work; WWE production customer/viewership data products; CSTR spectral/time-frequency methods, mathematical modeling, and geophysical signal interpretation; selected publications that signal mathematical and research credibility.
- Resume bullets usually compressed or discarded: health-specific clinical outcome language, FDA/regulatory language, detailed wearable study-design material, therapeutic/patient-specific framing, and medical-device modality lists unless they support validation, noisy data, or research-to-production judgment.
- Gaps / do-not-overstate items: do not claim direct quant-trading strategy ownership, financial-market modeling experience, hedge-fund infrastructure experience, large-scale distributed ML platform ownership, deep C++ systems/performance engineering, or formal finance domain expertise unless Kevin confirms it.
- Last updated: 2026-08-24.

### Health, Wearables, Neurotech, And Digital Biomarkers - Archetype JD

- Source JDs used: Oura, Omada, Beacon Biosignals, Lumicity, Motif Neurotech, Dexcom Emerging Sensing Technologies, Dexcom Advanced Sensing Technologies, Senseonics Sr. Algorithm Development Engineer, Atria Health Senior AI Scientist.
- Archetype role title(s): Senior ML Data Scientist, Principal Applied ML Scientist, Senior AI Scientist, Senior Algorithm/ML Engineer, Staff Algorithm Engineer, Algorithm Engineer, Data and Machine Learning Lead.
- Typical company / product context: wearable health, at-home clinical sensing, continuous glucose monitoring, regulated medical technology, neurotechnology, implantable or wearable therapeutic platforms, emerging biosensing technologies, digital health programs, clinical AI / medical model platforms, neuro/biosignal products, longitudinal member or patient data, and algorithms that turn sensor, clinical, or multimodal health data into actionable health insight.
- Core / necessary matching signals: the JD is centered on health, clinical, medical-device, digital-health, neurotechnology, biological sensing, or patient/member outcomes; it involves physiological, behavioral, wearable, biosignal, clinical, experimental, or longitudinal health data; it asks for ML, statistics, signal processing, biomarker discovery, risk/trajectory modeling, health decision support, or physiological/sensing model development; it values validation, evidence generation, product translation, technology feasibility, or clinical/scientific rigor.
- Variable / add-on signals: implantable devices, neuromodulation, neurostimulation, mental-health biomarkers, women's health, EEG, CGM, glucose sensing, biophysics, physiology, electrochemistry, analytical chemistry, first-principles models, mechanistic models, digital twins, physics-informed ML, simulation environments, technology readiness, performance-limit analysis, calibration, filtering, measurement-system algorithms, clinical foundation models, domain-specific medical models, open-source model survey/evaluation, transfer learning, fine-tuning, post-training, SFT, LoRA/QLoRA, PEFT, DPO/preference tuning, continued pretraining, distillation, DRCN/domain adaptation, patient-level adaptation, multimodal medical data, whole-genome sequencing, advanced imaging, longitudinal labs, family-linked records, PHI-safe data handling, train/test contamination prevention, algorithm architecture, design tradeoffs, verification/validation strategy, controlled unit tests, reproducible data-processing pipelines, algorithm-development tooling, design controls, product development lifecycle, hardware/firmware resource constraints, FDA 510(k), IDE/PMA, regulated documentation, causal inference, recommender systems, reinforcement learning, safe/compliant A/B testing, data/ML roadmap ownership, investor/physician communication, AWS/SageMaker, or commercialization leadership.
- Typical responsibilities: build and validate ML, statistical, signal-processing, estimation, calibration, detection, predictive, mechanistic, first-principles, or deep-learning algorithms for longitudinal sensor, experimental, and clinical data; adapt pretrained/shared representations to domain-specific, patient-specific, or clinically specialized tasks; own model lifecycle from requirements and data curation through production monitoring; develop Python/MATLAB-style data-processing pipelines, scripts, tools, unit tests, and analysis workflows for algorithm development; define data/ML and technology roadmaps; evaluate novel sensing concepts, technical feasibility, readiness, and performance limits; investigate sensor performance and accuracy issues; create simulation environments and predictive models to guide investment or development strategy; develop health trajectory, risk, next-best-action, dosing, therapeutic-effect, adherence, relapse-prediction, or biosignal biomarker models; design experiments, data-collection strategies, analytical approaches, and metadata standards; prevent train/test contamination and manage PHI-sensitive data hygiene; document validation and failure analysis; support regulated product translation, verification strategy, and product lifecycle decisions; provide technical leadership on algorithm architecture and design tradeoffs; collaborate across science, product, software, hardware, firmware, design, regulatory, clinical, investor/customer, and external-research teams to optimize system performance and resource utilization.
- Typical requirements: Python, SQL, MATLAB or similar technical-computing environments, C/C++ or equivalent implementation literacy when the role is product-algorithm-heavy, PyTorch or similar ML stack, HuggingFace/open-source model ecosystem fluency when the role is clinical AI/model-adaptation heavy; time-series analysis, statistical estimation, signal processing, optimization, calibration/filtering methods, deep learning, longitudinal modeling, first-principles or mechanistic modeling, simulation, transfer learning, fine-tuning/post-training literacy, robust validation, calibration/subgroup/error analysis, design-control or V&V awareness, health data fluency, study design awareness, data infrastructure, production monitoring, regulated-industry awareness for data-driven medical features, and clear communication of model value, limits, opportunities, and risks.
- Common keywords and phrases: wearable health data, biosignals, digital biomarkers, longitudinal, at-home, CGM, glucose monitoring, biosensing, novel sensing, biophysics, physiology, electrochemistry, analytical chemistry, clinical AI, medical foundation models, domain-specific models, open-source model evaluation, multimodal health data, whole-genome sequencing, advanced imaging, longitudinal labs, family-linked records, SFT, LoRA, QLoRA, PEFT, DPO, RLHF/RLAIF, continued pretraining, distillation, transfer learning, fine-tuning, DRCN, domain adaptation, patient-level modeling, train/test contamination, PHI, calibration, subgroup analysis, error analysis, mechanistic modeling, first-principles modeling, digital twins, simulation frameworks, technology feasibility, technology readiness, performance limits, calibration, estimation, filtering, measurement systems, algorithm maturation, algorithm architecture, algorithm-development tooling, Python data pipelines, MATLAB, C/C++, unit tests, reproducible analysis workflows, design tradeoffs, verification, validation, design controls, product development lifecycle, resource utilization, FDA, 510(k), IDE/PMA, medical device, neurotechnology, neuromodulation, neurostimulation, implantable device, neural electrophysiology, mental health, clinical validation, patient heterogeneity, signal quality, biomarker discovery, dosing, therapeutic effect, adherence, relapse prediction, improvement-native systems, safe/compliant A/B testing, causal inference, recommender systems, reinforcement learning, actionable insights.
- Hidden evaluation concerns: clinical rigor; avoiding overclaims; whether validation survives noisy free-living or experimental data and patient variability; whether Kevin can handle regulated or productized algorithm work; whether he can lead data strategy as well as model development; whether he can connect research models to hardware, firmware, resource constraints, verification strategy, and commercial product integration; whether causal/intervention or closed-loop therapy language is supported rather than decorative; whether foundation-model, LLM, open-source-model, PHI, genomics, radiology/imaging, and clinical-data governance claims are grounded in confirmed experience; whether neurostimulation, psychiatric, implantable-device, CGM, electrochemistry, analytical-chemistry, formal calibration-algorithm ownership, or design-control ownership gaps are acknowledged honestly; whether his adjacent physiological-sensing, model-adaptation, and physical-modeling background transfers to new biosensing and clinical-AI mechanisms.
- Tone and culture signals: mission-driven health product teams; evidence-conscious; cross-functional; commercialization and release-oriented; often expects senior scientific judgment, data-roadmap ownership, and concise executive/scientific communication without academic over-elaboration.
- Best starting profile: Health, Wearables, Neurotech, And Digital Biomarkers.
- Resume bullets usually retained: Podimetrics FDA-cleared remote monitoring, pressure-sensor modeling, embedded estimator implementation, thermal CV, adaptive alerting, physics-informed thermal modeling, synthetic thermograms, validation under drift/outliers, SmartMat+ hardware-transfer investigations, cross-functional hardware/software/clinical leadership; CVB wearable studies, Parkinsonian gait, Rett stereotypy, sleep validation, patient-level modeling, DRCN/domain adaptation, shared representations, scientific/team leadership, grants and external collaborators; WWE transfer-learning/fine-tuning project when pretrained-model adaptation, small-data diagnostics, or foundation-model-adjacent language is useful; CSTR/PhD physical-systems, simulation, and noisy-sensor inference bullets when the JD emphasizes first-principles, mechanistic, simulation, or feasibility work; Omada/Motif-style roles may also retain Next Best Action, quasi-experimental analytics, A/B testing, data-roadmap, and decision-support language; PUB-13 when the role rewards domain adaptation, deep time-series representation learning, or general-to-subject/patient adaptation.
- Resume bullets usually compressed or discarded: space-weather/geophysics unless framed as statistical signal-processing evidence; WWE/business analytics beyond one compact brand-value line unless experimentation, decisioning, or product analytics is directly relevant; generic image-recognition work unless the role values algorithm breadth.
- Gaps / do-not-overstate items: do not imply direct women's-health domain expertise, EEG/neural electrophysiology diagnostic ownership, active implantable medical-device experience, neuromodulation/neurostimulation therapy ownership, psychiatry/depression clinical expertise, CGM/glucose-sensing ownership, electrochemistry or analytical-chemistry expertise, direct CGM calibration-algorithm ownership, formal design-control ownership, formal FDA IDE/PMA regulatory-authoring ownership, production RL, production digital-twin ownership, production-scale clinical foundation-model ownership, expert LLM post-training infrastructure ownership, direct genomics/radiology model ownership, expert PHI platform/data-governance ownership, expert embedded C++ ownership, or deep AWS/SageMaker experience unless Kevin confirms it.
- Last updated: 2026-08-25.

### Sensor AI, Robotics, Autonomy, And Edge Perception - Archetype JD

- Source JDs used: General Motors, Trackman, Compound Eye, Samsara.
- Archetype role title(s): Future Sensing Engineer, Applied Scientist, ML/CV Applied Scientist, Signal Processing Software Developer, Research Engineer.
- Typical company / product context: autonomous driving, robotic perception, sports or industrial tracking, connected IoT fleets, passive cameras/IMUs, radar/video fusion, edge devices, and real-world sensor systems operating outside curated lab conditions.
- Core / necessary matching signals: the JD is centered on real-world sensor perception, tracking, localization, autonomy, robotics, edge AI, or deployed camera/radar/IMU/IoT systems; it asks for computer vision, signal processing, sensor fusion, or ML on physical sensor streams; it emphasizes robustness, evaluation, deployment constraints, or performance in changing operating environments.
- Variable / add-on signals: autonomous driving, lidar/radar, multimodal fusion, foundation models, imitation learning, reinforcement learning, simulation/synthetic data, geometric computer vision, 3D representation, large fleet-scale datasets, edge optimization, backend/full-stack production ownership, safety-critical systems, ITAR, venue travel, or sports tracking.
- Typical responsibilities: build perception, tracking, localization, segmentation, detection, or multimodal sensor-fusion models; evaluate robustness across weather, lighting, occlusion, noise, range, venues, and deployment environments; translate research papers into deployable models; optimize backend or edge inference; create offline evaluation datasets and metrics; collaborate with firmware, robotics, product, and full-stack teams.
- Typical requirements: Python plus PyTorch/TensorFlow; often C++/Golang/Java for production; computer vision, signal processing, sensor fusion, geometric perception, tracking, large datasets, edge optimization, simulation or synthetic data, experimental discipline, and production ML validation.
- Common keywords and phrases: perception, autonomy, edge AI, sensor fusion, cameras, radar, lidar, IMU, object detection, tracking, segmentation, localization, foundation models, imitation learning, model scaling, synthetic data, edge deployment, real-time robustness.
- Hidden evaluation concerns: whether Kevin's health/geophysics sensor background transfers credibly into autonomy or robotics; whether his models reached deployed hardware; whether validation reflects real operating conditions; whether he can discuss perception without overstating direct autonomous-vehicle experience.
- Tone and culture signals: technically ambitious, deployment-minded, high data volume, product impact, research-to-production, sometimes safety-critical or ITAR-sensitive.
- Best starting profile: Sensor AI, Robotics, Autonomy, And Edge Perception.
- Resume bullets usually retained: thermal-image localization/segmentation, scan-quality handling, edge recursive estimator, sensor validation, weakly supervised activity/gait recognition, transfer learning/image recognition, synthetic data, geophysical multi-instrument reconstruction, and production validation bullets.
- Resume bullets usually compressed or discarded: clinical outcome language when the target is not healthcare; executive dashboards or churn analytics unless the role emphasizes product analytics; detailed regulatory wording unless safety/quality is central.
- Gaps / do-not-overstate items: do not claim direct autonomous-driving stack ownership, lidar/radar production experience, large-scale fleet model ownership, or embedded C++ unless confirmed.
- Last updated: 2026-08-21.

### Bayesian Estimation, Signal Processing, And Physical Systems Research - Archetype JD

- Source JDs used: Kobold Data Scientist, Kobold Scientific Computing, Ionosphere, Oxman.
- Archetype role title(s): Data Scientist, Scientific Computing Engineer, Principal Ionospheric Physicist, Geospatial AI / ML Research Scientist.
- Typical company / product context: scientific ML for physical or environmental systems, mineral exploration, geophysical or ionospheric data assimilation, ecological/geospatial modeling, remote sensing, simulation, and operational scientific software.
- Core / necessary matching signals: the JD is centered on inference, modeling, or scientific computing for physical, geophysical, environmental, spatial, or instrumented systems; it involves sparse, noisy, indirect, heterogeneous, or spatiotemporal observations; it asks for applied statistics, Bayesian inference, signal processing, uncertainty quantification, physics-informed modeling, simulation, inverse problems, data assimilation, or scientific ML; it expects collaboration with domain experts or research-to-product translation.
- Variable / add-on signals: geology/mineral exploration, ionospheric physics, RF/GNSS/SATCOM, ecology, GIS, remote sensing, tomography, Kalman/ensemble methods, 2D/3D or volumetric reconstruction, generative design, reinforcement learning, field work, national security, clearance, scientific visualization, cloud-scale scientific pipelines, or customer whitepapers.
- Typical responsibilities: build predictive, statistical, Bayesian, physics-based, or ML models for sparse and noisy physical measurements; quantify uncertainty; integrate heterogeneous sensor/geospatial datasets; create 2D/3D or volumetric reconstructions; design validation strategies and benchmarks; build scientific computing tools and pipelines; translate domain science into operational or customer-facing capability.
- Typical requirements: advanced degree; Python scientific stack; applied statistics, Bayesian inference, signal processing, data assimilation, Kalman or ensemble methods, geospatial analysis, scientific visualization, physical-system data, research-to-production engineering, and ability to collaborate with domain experts.
- Common keywords and phrases: Bayesian inference, uncertainty quantification, physics-informed modeling, geospatial AI, inverse problems, remote sensing, tomography, sequential estimation, data assimilation, simulation, synthetic data, scientific computing, 2D/3D modeling, operational deployment.
- Hidden evaluation concerns: mathematical seriousness; domain ramp into geology/ecology/space-weather products; ability to reason from sparse indirect measurements; whether Kevin can convert research into maintainable software; whether his cross-domain breadth lands as coherent physical inference rather than scatter.
- Tone and culture signals: research-heavy but commercially or mission oriented; early-stage or founding-level ownership; close collaboration with scientists/domain experts; values intellectual curiosity plus business/product judgment.
- Best starting profile: Bayesian Estimation, Signal Processing, And Physical Systems Research.
- Resume bullets usually retained: NASA/space-weather publications, Bayesian coordinate-system validation, geomagnetic spectral methods, distributed geophysical sensor networks, Podimetrics recursive Bayesian estimators, physics-informed thermal modeling, synthetic thermogram generation, MedPSD or other uncertainty-heavy sensor work.
- Resume bullets usually compressed or discarded: health-specific clinical impact unless framed as noisy physical sensing; business analytics and dashboards unless they show stakeholder translation; generic CV bullets unless geospatial or sensor-imaging relevance is clear.
- Gaps / do-not-overstate items: do not imply mineral exploration, geology, ecology, GIS, RF propagation, security-clearance, or production ionospheric platform experience unless supported by the target resume or Kevin confirms.
- Last updated: 2026-08-21.

### Industrial And Operational Time-Series ML - Archetype JD

- Source JDs used: Oden Technologies, Cutsforth, Cargill, with Lumicity as a regulated-product bridge.
- Archetype role title(s): ML Data Engineer, Senior Data Scientist, Data Scientist / Signal Processing Engineer, Algorithm Engineer.
- Typical company / product context: manufacturing AI, industrial process optimization, predictive maintenance, quality/yield/cost prediction, machine failure monitoring, regulated product algorithms, computer vision for production facilities, and operational ML systems that support real decisions.
- Core / necessary matching signals: the JD is centered on operational, industrial, manufacturing, facility, supply-chain, reliability, or production-product data; it asks for ML/statistical modeling on time-series, sensor, image, process, equipment, or contextual data; it emphasizes deployment, monitoring, anomaly/risk detection, prediction, diagnostics, optimization, scaling, or decision support in real operating environments.
- Variable / add-on signals: rotating machinery, electrical/vibration/acoustic diagnostics, computer vision for manufacturing, predictive maintenance, real-time alerting, quality/yield/cost optimization, multi-site rollout, MLOps tooling, Spark/Beam/MLflow/Docker/Airflow, customer-success collaboration, factory-floor/Gemba culture, regulated product lifecycle, or medical-device algorithm validation.
- Typical responsibilities: build data and ML pipelines for high-dimensional heterogeneous time-series and sensor datasets; develop predictive, anomaly, diagnostic, recommendation, or optimization models; process electrical, vibration, acoustic, thermal, image, and contextual data; deploy and monitor production models; validate in real customer/facility environments; scale POCs to multiple sites; communicate model value and limits to domain experts.
- Typical requirements: Python scientific and ML stack; distributed processing or MLOps tools such as Spark, Beam, MLflow, Docker, Airflow, Vertex, SageMaker, or AWS/GCP; signal processing, feature extraction, computer vision, production deployment, stakeholder communication, and comfort with ambiguous, noisy, sparse, or drifting operational data.
- Common keywords and phrases: manufacturing, industrial analytics, process optimization, predictive maintenance, anomaly detection, real-time alerting, quality, yield, cost, machine failure, sensor data, signal processing, MLOps, deployment, monitoring, drift, multi-site scale.
- Hidden evaluation concerns: direct manufacturing/domain experience; whether Kevin can turn ambiguous operational data into business value; whether he has production and monitoring judgment; whether validation is practical under drift and limited ground truth; whether he can work with non-ML domain experts.
- Tone and culture signals: customer-obsessed, pragmatic, fast-moving, product and deployment oriented, often values factory-floor or field curiosity as much as modeling elegance.
- Best starting profile: Industrial And Operational Time-Series ML.
- Resume bullets usually retained: Podimetrics longitudinal pressure and thermal monitoring, alerting logic, drift/outlier handling, production pipelines, Next Best Action, A/B testing, quasi-experimental intervention analytics, dashboards/KPIs, customer segmentation/churn where business decision support is relevant, and sensor validation.
- Resume bullets usually compressed or discarded: detailed health-study outcomes unless the role is regulated or medical; geophysical publications unless signal-processing depth is needed; pure research language without operational tie-in.
- Gaps / do-not-overstate items: do not imply deep manufacturing operations, rotating-machinery fault physics, electrical machine diagnostics, cloud-platform depth, or multi-facility rollout ownership unless Kevin confirms.
- Last updated: 2026-08-21.

### Closed-Loop Physical AI And Self-Learning Systems - Provisional Archetype JD

- Source JDs used: 4MP primary; reinforcing signals from Oden Technologies, Cutsforth, Trackman, and General Motors.
- Archetype role title(s): Principal AI Engineer, Applied Scientist, ML Scientist for Closed-Loop Learning, Self-Learning Physical Systems, or Physical AI.
- Typical company / product context: hardware, robotics, autonomy, manufacturing, precision machinery, or fielded physical systems where models learn from correction outcomes and decide when to recommend, withhold, or update actions.
- Core / necessary matching signals: the JD is centered on physical-system feedback loops where model outputs influence future measurements or actions; it asks for learning from outcomes, corrections, interventions, or real-world feedback; it requires uncertainty-aware decisioning, guardrails, staged rollout, validation before action, or deciding when not to act; it involves noisy, delayed, sparse, costly, drifting, or partially observed physical data.
- Variable / add-on signals: CNC/manufacturing, robotics control, inverse problems, reinforcement learning, imitation learning, continual learning, transfer across machines/materials/sites, system identification, dynamics/control literacy, conformal or Bayesian risk methods, differentiable simulation, perception/geometry, small expensive datasets, hardware deployment, or self-correcting/autonomous operations.
- Typical responsibilities: model machine or physical-process behavior; learn from sparse, delayed, noisy, unevenly sampled correction outcomes; build uncertainty-aware guardrails; decide when a model is confident enough to act; transfer across machines, materials, users, or sites; design offline evaluation, backtesting, staged rollout, and monitoring; integrate perception, geometry, simulation, and production ML software.
- Typical requirements: inverse problems, optimization, real-world feedback, reinforcement learning or imitation learning literacy, continual learning, retraining loops, calibrated uncertainty, Bayesian/conformal/risk-aware methods, partial observability, latency, missing labels, Python/PyTorch, system identification, dynamics/control literacy, physics-informed learning, and strong production judgment.
- Common keywords and phrases: closed-loop learning, self-correcting systems, correction outcomes, feedback optimization, inverse problems, uncertainty guardrails, withhold correction, staged rollout, transfer learning, continual learning, partial observability, small expensive datasets, physical AI.
- Hidden evaluation concerns: whether Kevin can reason about action consequences rather than only prediction; whether he has enough control/optimization literacy; whether he can be honest about not having direct CNC/manufacturing closed-loop ownership; whether safety and uncertainty framing are concrete.
- Tone and culture signals: deep technical bar, senior ownership, strong preference for physical-system feedback over generic BI/NLP/ad-tech, values careful deployment over benchmark performance.
- Best starting profile: Closed-Loop Physical AI And Self-Learning Systems. Borrow from Industrial And Operational Time-Series ML and Bayesian Estimation when needed.
- Resume bullets usually retained: recursive Bayesian estimators, adaptive alerting, drift/outlier handling, on-device pressure monitoring, thermal CV, physics-informed thermal modeling, synthetic data/simulation, validation under sparse/noisy observations, and space-weather physical inference if mathematical depth helps.
- Resume bullets usually compressed or discarded: healthcare-specific language unless reframed as deployed physical-sensor feedback; dashboards/segmentation/churn unless the JD also asks for operational decision support; generic CV if it distracts from feedback and uncertainty.
- Gaps / do-not-overstate items: do not claim direct CNC, robotics control, servo/PID, reinforcement-learning-on-hardware, or closed-loop manufacturing deployment experience unless Kevin provides it.
- Last updated: 2026-08-21.

## Cluster Matching Signals

### Quantitative Research ML Engineering

Common signals: quantitative research, research engineering, senior ML engineering on research teams, production-quality code for research prototypes, data ingestion, feature engineering, validation, quality monitoring, model evaluation, experimentation lifecycle, reproducibility, correctness, maintainability, mathematical maturity, statistics, probability, optimization, linear algebra, numerical computing, imperfect or heterogeneous data, Python, Linux, R, C/C++, distributed computing, model serving, feature stores, experiment management, and financial time series.

Likely hidden concerns: whether Kevin can transfer from sensor/health/geophysical ML into finance or another quantitative research domain; whether his software-engineering depth is sufficient for a senior MLE role; whether gaps around distributed computing, model serving, feature stores, performance profiling, finance, or production trading systems are acknowledged without underselling his research-to-production strengths.

### Health, Wearables, Neurotech, And Digital Biomarkers

Common signals: wearable sensors, biosignals, physiological monitoring, digital biomarkers, CGM, glucose monitoring, biosensing, novel sensing, first-principles or mechanistic modeling, digital twins, simulation frameworks, technology feasibility, technology readiness, performance-limit analysis, calibration, estimation, filtering, measurement-system algorithms, algorithm maturation, algorithm architecture, verification/validation, design controls, product development lifecycle, neurotech, neuromodulation, neurostimulation, implantable devices, neural electrophysiology, mental-health biomarkers, clinical validation, remote patient monitoring, sleep, Parkinson's, gait, IMU, ECG, smartwatch, FDA, IDE/PMA, medical device, patient heterogeneity, free-living data, data/ML roadmap, biomarker discovery, dosing, adherence, relapse prediction.

Likely hidden concerns: clinical rigor, deployment-honest validation, noisy longitudinal data, patient variability, study design, sensor synchronization, model trustworthiness, senior data-strategy ownership, regulatory awareness, technology feasibility judgment, research-to-product algorithm maturation, hardware/firmware implementation constraints, and avoiding overclaims around implantable devices, neural electrophysiology, neurostimulation, psychiatric clinical expertise, CGM/glucose sensing, electrochemistry, analytical chemistry, formal calibration ownership, formal design-control ownership, or digital-twin ownership.

### Sensor AI, Robotics, Autonomy, And Edge Perception

Common signals: robotics, autonomy, perception, edge AI, cameras, sensor fusion, real-world deployment, embedded systems, CV, localization, segmentation, tracking, production hardware, data quality, model robustness.

Likely hidden concerns: whether Kevin can translate from health/geophysics into autonomy/perception, whether the work was deployed, and whether validation reflects real operating conditions.

### Bayesian Estimation, Signal Processing, And Physical Systems Research

Common signals: Bayesian estimation, statistical signal processing, physics-informed modeling, spatiotemporal inference, geophysics, inverse problems, sensor networks, uncertainty, simulation, synthetic data, coordinate systems, spectral analysis.

Likely hidden concerns: mathematical depth, research originality, ability to reason from sparse/noisy observations, and whether Kevin can communicate cross-domain physical inference coherently.

### Industrial And Operational Time-Series ML

Common signals: industrial analytics, monitoring, anomaly/risk detection, operational decisions, intervention effectiveness, production systems, time-series data, sensor data, A/B testing, dashboards, reliability, manufacturing, energy, logistics, field data.

Likely hidden concerns: business usefulness, stakeholder-facing decision support, production data quality, validation under drift, and ability to convert ambiguous operational data into action.

### Closed-Loop Physical AI And Self-Learning Systems

Common signals: closed-loop learning, self-correcting systems, correction outcomes, feedback optimization, inverse problems, control literacy, partial observability, small expensive datasets, calibrated uncertainty, guardrails, transfer across machines/materials/sites, staged rollout, continual learning, and physical AI.

Likely hidden concerns: whether Kevin can move from prediction to action-aware modeling, whether the control/RL language is honestly supported, whether uncertainty is operational rather than cosmetic, and whether he can frame health-device and geophysical work as credible evidence for physical feedback systems without overstating direct manufacturing or robotics control experience.

### Default Sensor ML Research Scientist

Common signals: broad applied scientist / research scientist / ML scientist roles where the JD combines sensor data, time-series ML, modeling, validation, and production translation without a narrow domain.

Likely hidden concerns: whether Kevin's breadth is a strength or a distraction. Use this cluster when the JD rewards cross-domain sensor ML but still needs a concise through-line.
