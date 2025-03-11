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



x = df.groupby('efs').apply(lambda df: df.assign(efs_rank = lambda x: x['efs_time'].rank()))
# Group by 'efs' and rank within each group
x = df.groupby('efs').apply(lambda df: df.assign(efs_rank=df['efs_time'].rank()))

# Negate the ranks for the events group (efs=1) so lower ranks mean earlier events
# This makes events (1) have negative values and censored (0) have positive values
mask = x.index.get_level_values(0) == 1
x.loc[mask, 'efs_rank'] = x.loc[mask, 'efs_rank'] - x.loc[mask, 'efs_rank'].max()

df = df.join(x[['efs_rank']].reset_index(level=0, drop=True))

# Separate features and target
X = df.drop(columns=['efs', 'efs_time', 'efs_rank', 'ID'])
y = df['efs_rank']

# Clean feature names to remove '[', ']', '<'
X.columns = X.columns.astype(str).str.replace("[", "_", regex=False)\
                                .str.replace("]", "_", regex=False)\
                                .str.replace("<", "_", regex=False)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an XGBoost classifier
# Calculate sample weights to ensure each race group has equal effect
sample_weights = pd.Series(
    compute_sample_weight(class_weight='balanced', y=race_groups.loc[X_train.index]), 
    index=X_train.index)


# ---- Train the XGBoost regressor using the enhanced features ----
model1 = xgb.XGBRegressor(
    n_estimators=1000,
    learning_rate=0.01,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    objective='reg:squarederror',
    eval_metric='rmse',
    random_state=42
)
model1.fit(X_train, y_train, sample_weight=sample_weights)

# Evaluate the model
y_pred = model1.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# auc = roc_auc_score(y_test, model1.predict_proba(X_test)[:, 1])
# print("Accuracy:", accuracy)
# print("AUC:", auc)

ids = df.loc[X_test.index, 'ID'].values
proba = -model1.predict(X_test)
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
