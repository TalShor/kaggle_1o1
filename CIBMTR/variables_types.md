# CIBMTR Variables Types

## Treatment-Related Variables

### Transplant Procedure Variables

- **graft_type**: Type of graft (Peripheral blood or Bone marrow)
- **prod_type**: Product type (PB or BM)
- **conditioning_intensity**: Intensity of conditioning regimen (RIC, NMA, MAC, etc.)
- **tbi_status**: Total Body Irradiation status and protocol
- **melphalan_dose**: Melphalan chemotherapy dosage
- **rituximab**: Whether Rituximab was given in conditioning
- **in_vivo_tcd**: In-vivo T-cell depletion status
- **gvhd_proph**: Graft-versus-host disease prophylaxis

### Donor/Recipient Matching Variables

- **donor_related**: Whether donor is related to recipient
- **hla_match_***: Multiple HLA matching parameters at different loci
- **hla_high_res_*** and **hla_low_res_***: High/low resolution HLA matching
- **tce_match** and **tce_div_match**: T-cell epitope matching
- **tce_imm_match**: T-cell epitope immunogenicity match
- **cmv_status**: CMV serostatus matching
- **sex_match**: Sex matching between donor and recipient

## Patient Characteristics Variables

### Demographics

- **age_at_hct**: Age at time of transplant
- **race_group**: Race
- **ethnicity**: Ethnicity

### Disease Characteristics

- **prim_disease_hct**: Primary disease requiring transplant
- **dri_score**: Disease risk index
- **cyto_score** and **cyto_score_detail**: Cytogenetic risk scoring
- **mrd_hct**: Minimal residual disease status

### Comorbidities/Pre-existing Conditions

- **comorbidity_score**: Sorror comorbidity score
- **karnofsky_score**: Performance status
- **obesity**: Obesity status
- **diabetes**: Diabetes status
- **psych_disturb**: Psychiatric disturbance
- **arrhythmia**: Arrhythmia status
- **cardiac**: Cardiac issues
- **pulm_moderate** and **pulm_severe**: Pulmonary complications
- **renal_issue**: Renal issues
- **hepatic_mild** and **hepatic_severe**: Hepatic complications
- **peptic_ulcer**: Peptic ulcer status
- **rheum_issue**: Rheumatologic issues
- **prior_tumor**: History of solid tumor
- **vent_hist**: History of mechanical ventilation

## Other Variables

### Temporal Variables

- **year_hct**: Year of transplant
- **donor_age**: Age of donor

### Outcome Variables

- **efs**: Event-free survival (outcome)
- **efs_time**: Time to event (outcome)

## Key Variables for Treatment Stratification

To stratify the treatments effectively, focus on these key treatment variables:

- **conditioning_intensity**: Fundamental difference in treatment approach
- **graft_type/prod_type**: Type of cells used
- **tbi_status**: Whether and how radiation was used
- **gvhd_proph**: Protocol for preventing graft-versus-host disease
- **in_vivo_tcd**: Whether T-cell depletion was used
- **melphalan_dose**: Chemotherapy dosing

These variables most directly describe the treatment approach and would give you the clearest stratification of different treatment protocols.