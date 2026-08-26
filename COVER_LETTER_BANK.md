# Cover Letter Bank

This file is the canonical reservoir for reusable cover-letter paragraph modules. It is intentionally modular rather than a pile of finished letters: each tailored cover letter should select, lightly edit, or replace a small number of paragraphs based on the job description, selected profile cluster, tailored resume, and audit notes.

Use old cover letters as style references only. Do not treat any prior company-specific cover letter as canonical source text.

## Use Rules

- Target one page and usually 4-6 paragraphs.
- Start with a cluster-specific opener when one clearly fits.
- Use 2-3 evidence paragraphs, not every strong example.
- Include a company/role bridge that explains why this specific role makes sense.
- Avoid repeating the resume mechanically. The cover letter should explain the through-line and relevance.
- Prefer light edits over inventing new claims.
- Do not overstate direct domain experience. Use adjacent-domain framing when the role asks for something Kevin has not owned directly.
- If a paragraph is created for one role and seems reusable, add it here in a future commit. Otherwise keep it in the local plan/audit only.

## Module Table

| ID | Cluster | Module role | Use / cut guidance |
|---|---|---|---|
| OPEN-DEFAULT-01 | Default | Opener | Broad sensor-inference opener for cross-domain applied scientist roles. |
| OPEN-HWD-01 | HWD | Opener | Health, wearables, neurotech, digital biomarkers, and medical-device analytics. |
| OPEN-SAR-01 | SAR | Opener | Sensor AI, robotics, autonomy, edge perception, cameras, and physical-world sensing. |
| OPEN-BSP-01 | BSP | Opener | Bayesian estimation, signal processing, spatiotemporal inference, scientific ML, and physical systems. |
| OPEN-IOT-01 | IOT | Opener | Industrial, operational, time-series, monitoring, and decision-support roles. |
| OPEN-CLP-01 | CLP | Opener | Closed-loop, adaptive, feedback, action-under-uncertainty, and self-learning physical systems. |
| OPEN-QRE-01 | QRE | Opener | Quantitative/applied research-engineering opener: data infrastructure, statistical modeling, and evaluation rigor for a research team, domain-neutral (finance, healthcare, or other). |
| EVID-POD-01 | HWD/SAR/CLP | Evidence | Podimetrics regulated product, embedded estimator, thermal CV, and validation evidence. |
| EVID-POD-02 | IOT/CLP/HWD | Evidence | Podimetrics longitudinal monitoring, adaptive alerting, intervention, and product-decision evidence. |
| EVID-POD-03 | HWD/SAR/IOT | Evidence | Podimetrics production Python scan-pipeline, debugging, PR, consultant-QC integration, and multi-vendor hardware support. |
| EVID-CVB-01 | HWD | Evidence | CVB wearable digital biomarkers, Parkinson's, Rett, sleep, and clinical-study evidence. |
| EVID-CVB-02 | HWD/IOT | Evidence | CVB feasibility judgment, clinician-friendly ML, and responsible clinical modeling evidence. |
| EVID-CVB-03 | HWD/CLP | Evidence | Sensor-driven questionnaire estimation, passive sensing, mental-health risk, and pivot from unsupported wearable-suicide prediction. |
| EVID-CSTR-01 | BSP/SAR/CLP | Evidence | Space-weather / geophysical spatiotemporal inference and distributed sensors. |
| EVID-WWE-01 | IOT | Evidence | WWE production analytics, business ML, A/B testing, and stakeholder decision support. |
| EVID-ADAPT-01 | HWD/SAR | Evidence | Transfer learning, fine-tuning, DRCN/domain adaptation, and general-to-patient adaptation evidence for foundation-model-adjacent roles. |
| EVID-RESEARCH-01 | Default | Evidence | Early-stage research direction, hidden assumptions, validation, and research-to-product judgment. |
| BRIDGE-HWD-01 | HWD | Company bridge | Connects Kevin's health/wearable background to the company's patient/product mission. |
| BRIDGE-SAR-01 | SAR | Company bridge | Connects sensor inference to physical-world perception and deployed systems. |
| BRIDGE-BSP-01 | BSP | Company bridge | Connects physical inference and spatiotemporal modeling to the target scientific domain. |
| BRIDGE-IOT-01 | IOT | Company bridge | Connects operational ML to business/production decision systems. |
| BRIDGE-CLP-01 | CLP | Company bridge | Connects estimation, validation, and deployment to adaptive feedback systems. |
| BRIDGE-GAP-01 | Default | Gap bridge | Honest adjacent-domain bridge when Kevin lacks the exact target domain. |
| BRIDGE-QRE-01 | QRE | Company bridge | Connects research-engineering discipline (pipelines, data-quality judgment, evaluation infrastructure) to the target research team's problem; domain-neutral. |
| CLOSE-DEFAULT-01 | Default | Closing | General concise close. |
| CLOSE-HWD-01 | HWD | Closing | Health/wearable/digital biomarker close. |
| CLOSE-SAR-01 | SAR | Closing | Sensor AI / perception close. |
| CLOSE-BSP-01 | BSP | Closing | Physical systems / scientific ML close. |
| CLOSE-IOT-01 | IOT | Closing | Operational ML close. |
| CLOSE-CLP-01 | CLP | Closing | Closed-loop physical AI close. |
| CLOSE-QRE-01 | QRE | Closing | Quantitative research-engineering close. |

## Canonical Text

### OPEN-DEFAULT-01: Cross-domain sensor inference opener

I am excited to apply for the {role_title} position at {company}. Across physical, physiological, and geophysical systems, my career has focused on one core technical problem: transforming noisy, indirect sensor measurements into reliable estimates and decisions in real-world systems. {company_possessive} work on {company_problem} is a strong match for the kind of applied science I have spent my career building: models and validation methods that hold up under noise, uncertainty, hardware artifacts, heterogeneous users, and changing operating conditions.

### OPEN-HWD-01: Health and wearable sensing opener

I am excited to apply for the {role_title} position at {company}. My recent work has centered on longitudinal physiological sensing, wearable data, digital biomarkers, and medical-device analytics: turning noisy real-world measurements into models and validation frameworks that can support clinical or product decisions. {company_possessive} work on {company_problem} is a compelling extension of that same theme.

### OPEN-SAR-01: Sensor AI and edge perception opener

I am excited to apply for the {role_title} position at {company}. My career has focused on building inference systems from imperfect real-world sensor measurements, where sensor behavior, uncertainty, validation design, and deployment constraints matter as much as the model architecture. {company_possessive} work on {company_problem} closely matches the sensor AI and research-to-engineering problems I have spent my career pursuing.

### OPEN-BSP-01: Physical systems and signal processing opener

I am excited to apply for the {role_title} position at {company}. Across geophysical, physiological, and engineered sensor systems, my career has focused on transforming noisy, indirect observations into reliable estimates of latent physical or physiological state. {company_possessive} work on {company_problem} is a compelling extension of that same problem into {target_domain}.

### OPEN-IOT-01: Operational time-series ML opener

I am excited to apply for the {role_title} position at {company}. My work sits at the intersection of time-series ML, sensor analytics, statistical inference, and production decision support: building models that remain useful when data is noisy, incomplete, delayed, heterogeneous, and tied to real operational decisions. {company_possessive} focus on {company_problem} is a strong match for that background.

### OPEN-CLP-01: Closed-loop physical AI opener

I am excited to apply for the {role_title} position at {company}. I build estimation and ML systems for physical and physiological data where uncertainty, feedback, drift, and changing operating conditions are central rather than incidental. {company_possessive} work on {company_problem} is especially interesting because it requires models that can improve decisions in the loop, not just perform well in a static benchmark.

### OPEN-QRE-01: Quantitative/applied research-engineering opener

I am excited to apply for the {role_title} position at {company}. My work has consistently lived at the boundary of statistical modeling, data infrastructure, and rigorous evaluation: building the pipelines and validation frameworks that turn messy, real-world data into research-ready evidence, then using that evidence honestly. {company_possessive} work on {company_problem} is a strong fit for that combination of data-engineering discipline, mathematical judgment, and evaluation rigor.

### EVID-POD-01: Regulated product and sensor algorithm evidence

Most recently, at Podimetrics, I worked on FDA-cleared remote-monitoring products using thermal arrays and pressure sensors for diabetic foot ulcer detection and fall-risk assessment. I designed streaming estimation algorithms for a battery-powered patient-facing edge device, translated selected methods from Python into embedded C, validated numerical equivalence, supported firmware integration, and extended production thermal computer-vision workflows for foot localization, segmentation, scan-quality handling, and anatomical keypoint temperature extraction.

### EVID-POD-02: Longitudinal monitoring and decisioning evidence

At Podimetrics, the practical challenge was not just model development, but building monitoring and decision systems that remained meaningful under drift, sparse observations, outliers, irregular sampling, hardware artifacts, and heterogeneous patient behavior. That work included adaptive alert logic for longitudinal pressure-sensor data, staged and prospective validation, and analytics tied to patient monitoring and intervention decisions.

### EVID-POD-03: Production scan-pipeline evidence

At Podimetrics, I also worked directly in the production Python scan-processing codebase, helping software engineering debug odd pipeline behavior, fix bugs, review implementation details, and integrate consultant-built quality-control components needed to keep thermal algorithms reliable across chip and hardware vendors over time.

### EVID-CVB-01: Wearable digital biomarker evidence

At Cohen Veterans Bioscience, I led sensor analytics and digital-health research programs using free-living wearable data for Parkinson's disease monitoring, Rett syndrome stereotypy detection, and sleep-sensor validation. That work required building and evaluating models across smartwatch, IMU, ECG, Oura Ring, Apple Watch, Shimmer, video-adjacent behavioral annotations, and clinical-study data while keeping synchronization, weak labels, patient heterogeneity, and real-world generalization visible.

### EVID-CVB-02: Responsible clinical ML judgment evidence

At Cohen Veterans Bioscience, I also worked on clinical ML problems where the most important contribution was often defining what the data could responsibly support. I evaluated a wearable suicide-risk prediction initiative as infeasible without an adequate prospective data foundation, redirected the program toward more tractable clinical risk indicators, and built clinician-friendly dropout-risk models using interpretable ML methods such as SHAP, LIME, and feature-importance analysis.

### EVID-CVB-03: Sensor-driven questionnaire estimation evidence

At Cohen Veterans Bioscience, my first response to a leadership push for a "wearable suicide model" was to make the problem more scientifically tractable. I proposed Sensor-Driven Questionnaire Estimation: targeting the PHQ-9 depression screener first, since it is freely available and already had some supporting evidence, and envisioning a roadmap extension toward a continuously updated wearable-derived proxy index that could be corrected via Kalman-filter-style data assimilation whenever a real PHQ-9 score became available. I generalized the core approach with a broad literature review and synthetic examples to show how wristwatch signals could estimate clinic-administered psychological assessments and broader patient-state risk indicators, framed around what prospective data could responsibly support.

### EVID-CSTR-01: Spatiotemporal physical inference evidence

My doctoral research in space physics focused on inferring geomagnetic and polar-cap electrodynamic structure from distributed magnetometer, satellite, and spacecraft observations. That work required spectral methods for noisy geophysical time series, validation of coordinate representations, and reasoning across spatially distributed observations where the underlying system state could not be measured directly.

### EVID-WWE-01: Production business ML evidence

At WWE, I built and maintained automated data processing, machine learning, and reporting pipelines for customer segmentation, churn prediction, A/B test analysis, and executive reporting. That experience is useful where applied ML has to connect technical modeling, product or business decisions, and stakeholder communication in a production environment.

### EVID-ADAPT-01: Transfer learning and domain-adaptation evidence

I have also done model-adaptation work that maps well to foundation-model-adjacent roles. At WWE, I fine-tuned ImageNet-pretrained VGG16 for a small-data image-recognition prototype using a custom head, two-phase training, augmentation, architecture comparisons, and confidence-thresholded rejection. At Cohen Veterans Bioscience, I explored DRCN-style reconstruction/classification networks, autoencoder-based representations, source/target batch training, and pseudolabeling for wearable time-series domain adaptation and patient-level modeling.

### EVID-RESEARCH-01: Early-stage research direction evidence

Across these projects, I have found that I am most effective in research-intensive environments where the problem itself is still taking shape. I enjoy identifying which questions are worth asking, uncovering hidden assumptions, challenging flawed ones, exploring unconventional solution paths, and establishing evaluation approaches that expose structural risks before significant engineering effort is invested.

### BRIDGE-HWD-01: Health and patient-product bridge

What draws me to {company} is the opportunity to apply that same research-to-product discipline to {company_problem}. I am especially interested in work where physiological data, clinical evidence, product architecture, and responsible validation have to be reasoned about together rather than treated as separate problems.

### BRIDGE-SAR-01: Sensor AI and deployed perception bridge

What draws me to {company} is the opportunity to apply that same research-to-engineering discipline to {company_problem}. My strongest work happens where applied science, statistical signal processing, and engineering pragmatism meet: defining the right problem, building models that are robust to real-world failure modes, and partnering across teams to turn those models into reliable deployed systems.

### BRIDGE-BSP-01: Physical systems transfer bridge

I do not come from a conventional {target_domain} background. What I would bring is a strong foundation in spatiotemporal inference, statistical signal processing, Bayesian estimation, physics-informed modeling, simulation, and research-to-production translation for noisy real-world systems. I would be excited to apply that foundation to {company_possessive} work on {target_contribution}.

### BRIDGE-IOT-01: Operational decision bridge

What draws me to {company} is the opportunity to apply that same production-minded modeling discipline to {company_problem}. I am especially interested in environments where modeling, data quality, instrumentation, and stakeholder decisions have to be reasoned about together.

### BRIDGE-CLP-01: Closed-loop bridge

What draws me to {company} is the opportunity to work on systems where learning, estimation, and action are connected. My strongest contribution would be helping define what the system can know, how uncertainty should be represented, how feedback should be validated, and how model behavior should be translated into reliable operating decisions.

### BRIDGE-GAP-01: Honest adjacent-domain bridge

I should be clear that my background is not in {gap_domain}. What I would bring is adjacent depth in {adjacent_strengths}, along with the habit of learning the signal-generation process, artifacts, labels, validation constraints, and failure modes before turning a promising analysis into a product claim.

### BRIDGE-QRE-01: Quantitative research-engineering bridge

What draws me to {company} is the opportunity to apply that same research-engineering discipline — translating open-ended research questions into reliable pipelines, catching subtle data-quality and measurement problems before they become false conclusions, and building evaluation infrastructure researchers can actually trust — to {company_possessive} work on {company_problem}.

### CLOSE-DEFAULT-01: General concise close

I would welcome the opportunity to bring my background in {closing_keywords} to {company}.

### CLOSE-HWD-01: Health and biomarkers close

I would welcome the opportunity to bring my background in longitudinal health monitoring, wearable sensing, machine learning, statistical signal processing, Bayesian estimation, digital biomarkers, and deployment-oriented validation to {company_possessive} work on {company_problem}.

### CLOSE-SAR-01: Sensor AI close

I would welcome the opportunity to bring my background in sensor AI, computer vision, time-series ML, Bayesian estimation, statistical signal processing, and production-oriented validation to {company}.

### CLOSE-BSP-01: Physical systems close

I would welcome the opportunity to bring my background in statistical signal processing, Bayesian estimation, spatiotemporal inference, physics-informed modeling, simulation, and sensor analytics to {company}.

### CLOSE-IOT-01: Operational ML close

I would welcome the opportunity to bring my background in time-series ML, sensor analytics, production data products, robust validation, and decision-support modeling to {company}.

### CLOSE-CLP-01: Closed-loop physical AI close

I would welcome the opportunity to bring my background in Bayesian estimation, adaptive monitoring, sensor ML, physics-informed modeling, and deployment-honest validation to {company_possessive} work on {company_problem}.

### CLOSE-QRE-01: Quantitative research-engineering close

I would welcome the opportunity to bring my background in {closing_keywords} to {company_possessive} research team.
