import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# -------------------------------------------------
# Display Settings
# -------------------------------------------------
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

# -------------------------------------------------
# Load HRIS Export
# -------------------------------------------------
df = pd.read_csv("sample_hr_data.csv")

print("\nData Loaded Successfully")
print("Shape:", df.shape)

# -------------------------------------------------
# Feature Engineering
# -------------------------------------------------

def tenure_band(months):
    if months <= 6:
        return "0-6"
    elif months <= 12:
        return "6-12"
    elif months <= 24:
        return "12-24"
    else:
        return "24+"

df["TenureBand"] = df["TenureMonths"].apply(tenure_band)
df["HighOvertimeFlag"] = np.where(df["OvertimeHours"] > 25, 1, 0)
df["LowPerformanceFlag"] = np.where(df["PerformanceScore"] < 3, 1, 0)

# -------------------------------------------------
# Workforce Diagnostics (KPIs)
# -------------------------------------------------

print("\n--- Workforce Diagnostics ---")

print("Overall Turnover Rate:",
      round(df["Exit"].mean() * 100, 2), "%")

print("Early Attrition Rate (<12 months):",
      round(df[df["TenureMonths"] < 12]["Exit"].mean() * 100, 2), "%")

print("\nTurnover by Department:")
print((df.groupby("Department")["Exit"].mean() * 100).round(2))

print("\nTurnover by Tenure Band:")
print((df.groupby("TenureBand")["Exit"].mean() * 100).round(2))

# -------------------------------------------------
# Cost Estimation
# -------------------------------------------------

df["ReplacementCost"] = df["Salary"] * 0.30
total_cost = df[df["Exit"] == 1]["ReplacementCost"].sum()

print("\nEstimated Total Turnover Cost:",
      round(total_cost, 2))

# -------------------------------------------------
# Predictive Model (Scaled + Balanced)
# -------------------------------------------------

features = [
    "Age",
    "TenureMonths",
    "Salary",
    "OvertimeHours",
    "PerformanceScore",
    "SupervisorRating",
    "HighOvertimeFlag",
    "LowPerformanceFlag"
]

X = df[features]
y = df["Exit"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("logreg", LogisticRegression(
        max_iter=2000,
        class_weight="balanced"
    ))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_prob)

print("\n--- Model Performance ---")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("AUC Score:", round(auc, 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -------------------------------------------------
# Feature Impact
# -------------------------------------------------

logreg_model = model.named_steps["logreg"]

importance = pd.DataFrame({
    "Feature": features,
    "Coefficient": logreg_model.coef_[0]
}).sort_values(by="Coefficient", ascending=False)

print("\n--- Feature Impact ---")
print(importance)

# -------------------------------------------------
# Risk Scores
# -------------------------------------------------

df["AttritionRiskScore"] = model.predict_proba(X)[:, 1]

top_risk = df.sort_values(
    by="AttritionRiskScore",
    ascending=False
).head(10)

print("\n--- Top 10 High-Risk Employees ---")
print(top_risk[["EmployeeID", "AttritionRiskScore"]])

print("\nAnalysis Complete.")
df.to_csv("processed_attrition_output.csv", index=False)