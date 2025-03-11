import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
import xgboost as xgb
from score import score
from sklearn.utils.class_weight import compute_sample_weight



# ...existing code to load your cleaned train dataset...
df = pd.read_parquet('CIBMTR/data/train_cleaned_v2.parquet').astype(float)
race_groups = df.set_index('ID').filter(like='race_group').melt(ignore_index=False).query('value == 1').sort_index()\
    ['variable'].astype('category').cat.codes

# Separate features and target
X = df.drop(columns=['efs', 'efs_time', 'ID'])
y0 = df['efs_time']
y1 = df['efs']

# Clean feature names to remove '[', ']', '<'
X.columns = X.columns.astype(str).str.replace("[", "_", regex=False)\
                                .str.replace("]", "_", regex=False)\
                                .str.replace("<", "_", regex=False)

# Train-test split
X_train, X_test, y0_train, y0_test, y1_train, y1_test = train_test_split(X, y0, y1, test_size=0.2, random_state=42)

# Train an XGBoost classifier
# Calculate sample weights to ensure each race group has equal effect
sample_weights = pd.Series(
    compute_sample_weight(class_weight='balanced', y=race_groups.loc[X_train.index]), 
    index=X_train.index)

# ---- Train survival model for efs_time using xgb.train ----
dtrain = xgb.DMatrix(X_train, label=y0_train, weight=sample_weights)
dtest  = xgb.DMatrix(X_test, label=y0_test)

params_surv = {
    'objective': 'survival:cox',
    'eval_metric': 'cox-nloglik',
    'seed': 42,
    'missing': np.nan
}
num_round = 1000
model0 = xgb.train(params_surv, dtrain, num_round)
# Predict risk scores on training and test sets; note these represent risk levels
efs_time_pred_train = model0.predict(dtrain)
efs_time_pred_test = model0.predict(dtest)

# Append predicted risk score to features for classifier training
X_train['efs_time_pred'] = efs_time_pred_train
X_test['efs_time_pred'] = efs_time_pred_test

print('corr', X_train[['efs_time_pred']].join(y0_train.to_frame()).corr())

# ---- Train the XGBoost classifier using the enhanced features ----
model1 = xgb.XGBClassifier(
    n_estimators=1000,
    learning_rate=0.01,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    objective='binary:logistic',
    eval_metric='logloss',
    random_state=42
)
model1.fit(X_train, y1_train, sample_weight=sample_weights)

# Evaluate the model
y_pred = model1.predict(X_test)
accuracy = accuracy_score(y1_test, y_pred)
auc = roc_auc_score(y1_test, model1.predict_proba(X_test)[:, 1])
print("Accuracy:", accuracy)
print("AUC:", auc)

ids = df.loc[X_test.index, 'ID'].values
proba = model1.predict_proba(X_test)[:, 1]
test_race_groups = race_groups.loc[X_test.index].values

submission = {'prediction':
    {idx: proba for idx, proba in zip(ids, proba)}}
submission = pd.DataFrame(submission)
submission.insert(0, 'ID', range(len(submission)))

solution = {'efs': {idx: efs for idx, efs in zip(ids, df.loc[X_test.index, 'efs'])}, 
            'efs_time': {idx: efs_time for idx, efs_time in zip(ids, df.loc[X_test.index, 'efs_time'] )},
            'race_group': {idx: race_group for idx, race_group in zip(ids, test_race_groups)}}
solution = pd.DataFrame(solution)
solution.insert(0, 'ID', range(len(solution)))
print(score(solution, submission, 'ID'))
