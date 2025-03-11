# CIBMTR Variables Types

## Treatment-Related Variables

### Transplant Procedure Variables

- **graft_type**: Type of graft (Peripheral blood or Bone marrow)
  Options: Peripheral blood, Bone marrow
- **prod_type**: Product type (PB or BM)
  Options: PB, BM
- **conditioning_intensity**: Intensity of conditioning regimen (RIC, NMA, MAC, etc.)
  Options: RIC, NMA, MAC, TBD, No drugs reported, N/A, F(pre-TED) not submitted
- **tbi_status**: Total Body Irradiation status and protocol
  Options: No TBI; TBI + Cy +- Other; TBI +- Other, <=cGy; TBI +- Other, >cGy; TBI +- Other, -cGy, single; TBI +- Other, unknown dose; TBI +- Other, -cGy, unknown dose; TBI +- Other, -cGy, fractionated
- **melphalan_dose**: Melphalan chemotherapy dosage
  Options: N/A, Mel not given, MEL
- **rituximab**: Whether Rituximab was given in conditioning
  Options: No, Yes
- **in_vivo_tcd**: In-vivo T-cell depletion status
  Options: Yes, No
- **gvhd_proph**: Graft-versus-host disease prophylaxis
  Options: FK+ MMF +- others; Parent Q = yes, but no agent; FK+ MTX +- others(not MMF); FKalone; Cyclophosphamide alone; CSA + MMF +- others(not FK); TDEPLETION +- other; Cyclophosphamide +- others; No GvHD Prophylaxis; Other GVHD Prophylaxis; CSA alone; TDEPLETION alone; CDselect alone; CSA + MTX +- others(not MMF,FK); FK+- others(not MMF,MTX); CDselect +- other; CSA +- others(not FK,MMF,MTX)

### Donor/Recipient Matching Variables

- **donor_related**: Whether donor is related to recipient
  Options: Unrelated, Related, Multiple donor (non-UCB)
- **hla_match_***: Multiple HLA matching parameters at different loci
- **hla_high_res_*** and **hla_low_res_***: High/low resolution HLA matching
- **tce_match**: T-cell epitope matching
  Options: Permissive, Fully matched, GvH non-permissive, HvG non-permissive
- **tce_div_match**: T-cell epitope matching
  Options: Permissive mismatched, Bi-directional non-permissive, GvH non-permissive, HvG non-permissive
- **tce_imm_match**: T-cell epitope immunogenicity match
  Options: P/P, G/G, H/H, G/B, H/B, P/H, P/G, P/B
- **cmv_status**: CMV serostatus matching
  Options: +/-, +/+, -/-, -/+
- **sex_match**: Sex matching between donor and recipient
  Options: M-M, F-F, F-M, M-F

## Patient Characteristics Variables

### Demographics

- **age_at_hct**: Age at time of transplant
- **race_group**: Race
  Options: White, Black or African-American, Native Hawaiian or other Pacific Islander, Asian, American Indian or Alaska Native, More than one race
- **ethnicity**: Ethnicity
  Options: Not Hispanic or Latino, Hispanic or Latino, Non-resident of the U.S.

### Disease Characteristics

- **prim_disease_hct**: Primary disease requiring transplant
  Options: ALL, MPN, IPA, AML, MDS, Other acute leukemia, AI, SAA, IEA, NHL, PCD, IIS, HIS, Other leukemia, Solid tumor, IMD, HD, CML
- **dri_score**: Disease risk index
  Options: Intermediate, High, N/A - non-malignant indication, N/A - pediatric, High - TED AML case <missing cytogenetics, TBD cytogenetics, Low, Intermediate - TED AML case <missing cytogenetics, N/A - disease not classifiable, Very high, Missing disease status
- **cyto_score**: Cytogenetic risk scoring
  Options: Intermediate, Favorable, Poor, TBD, Normal, Other, Not tested
- **cyto_score_detail**: Cytogenetics for DRI (AML/MDS)
  Options: Intermediate, TBD, Favorable, Poor, Not tested
- **mrd_hct**: Minimal residual disease status
  Options: Negative, Positive

### Comorbidities/Pre-existing Conditions

- **comorbidity_score**: Sorror comorbidity score
- **karnofsky_score**: Performance status
- **obesity**: Obesity status
  Options: No, Yes, Not done
- **diabetes**: Diabetes status
  Options: No, Yes, Not done
- **psych_disturb**: Psychiatric disturbance
  Options: Yes, No, Not done
- **arrhythmia**: Arrhythmia status
  Options: No, Yes, Not done
- **cardiac**: Cardiac issues
  Options: No, Yes, Not done
- **pulm_moderate**: Pulmonary complications
  Options: Yes, Not done, No
- **pulm_severe**: Pulmonary complications
  Options: No, Yes, Not done
- **renal_issue**: Renal issues
  Options: No, Yes, Not done
- **hepatic_mild**: Hepatic complications
  Options: No, Yes, Not done
- **hepatic_severe**: Hepatic complications
  Options: No, Yes, Not done
- **peptic_ulcer**: Peptic ulcer status
  Options: No, Yes, Not done
- **rheum_issue**: Rheumatologic issues
  Options: No, Yes, Not done
- **prior_tumor**: History of solid tumor
  Options: Yes, No, Not done
- **vent_hist**: History of mechanical ventilation
  Options: No, Yes

## Other Variables

### Temporal Variables

- **year_hct**: Year of transplant
- **donor_age**: Age of donor

### Outcome Variables

- **efs**: Event-free survival (outcome)
  Options: Event, Censoring
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
