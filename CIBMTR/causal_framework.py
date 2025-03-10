import numpy as np
import pandas as pd
from econml.dml import LinearDML, SparseLinearDML
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

# Select multiple treatment variables
treatment_vars = ['graft_type', 'tbi_status', 'conditioning_intensity']

# Select covariates (control variables)
covariates = [
    'age_at_hct', 'dri_score', 'prim_disease_hct', 'cyto_score',
    'comorbidity_score', 'karnofsky_score', 'diabetes', 'psych_disturb'
]

# Create dummy variables for treatments
treatment_dummies = pd.get_dummies(train[treatment_vars], drop_first=True)

# Create dummy variables for categorical covariates
X = pd.get_dummies(train[covariates], drop_first=True)

# Outcome variable
Y = train['efs_time']  # Or your preferred outcome

# Use SparseLinearDML for high-dimensional treatments
model_multi = SparseLinearDML(
    model_y=RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42),
    model_t=RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42),
    featurizer=None,  # No need for additional featurization
    alpha=0.05,  # L1 regularization parameter
    max_iter=1000,
    random_state=42
)

# Fit the model with multiple treatments
T = treatment_dummies.values
model_multi.fit(Y, T, X=X)

# Get treatment effect coefficients
treatment_effects = pd.Series(model_multi.coef_, index=treatment_dummies.columns)
treatment_stderr = pd.Series(model_multi.stderr_, index=treatment_dummies.columns)

# Display the results
effects_df = pd.DataFrame({
    'Effect': treatment_effects,
    'Std Error': treatment_stderr,
    'P-value': model_multi.pval_,
    'Lower CI': treatment_effects - 1.96 * treatment_stderr,
    'Upper CI': treatment_effects + 1.96 * treatment_stderr
})
print(effects_df)

# Plot the treatment effects with confidence intervals
plt.figure(figsize=(12, 8))
effects_df = effects_df.sort_values('Effect')
plt.errorbar(
    effects_df['Effect'], 
    range(len(effects_df)),
    xerr=1.96 * effects_df['Std Error'],
    fmt='o',
    capsize=5
)
plt.yticks(range(len(effects_df)), effects_df.index)
plt.axvline(x=0, color='r', linestyle='-', alpha=0.3)
plt.xlabel('Treatment Effect')
plt.title('Treatment Effects with 95% Confidence Intervals')
plt.tight_layout()
plt.show()