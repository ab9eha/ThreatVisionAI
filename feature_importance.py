import os

import pandas as pd
import joblib
import matplotlib.pyplot as plt


# ---------------------------------------
# Create results folder
# ---------------------------------------

os.makedirs("results", exist_ok=True)


# ---------------------------------------
# Load trained model
# ---------------------------------------

model = joblib.load(
    "models/multifeature_model.pkl"
)


# ---------------------------------------
# Feature names
# ---------------------------------------

features = [
    "Failed_Logins",
    "Connection_Count",
    "Packet_Size",
    "Login_Hour",
    "Port_Requests"
]


# ---------------------------------------
# Get feature importance
# ---------------------------------------

importance = model.feature_importances_


# ---------------------------------------
# Create results table
# ---------------------------------------

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})


importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)


# ---------------------------------------
# Save CSV
# ---------------------------------------

importance_df.to_csv(
    "results/feature_importance.csv",
    index=False
)


# ---------------------------------------
# Create chart
# ---------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    importance_df["Feature"],
    importance_df["Importance"]
)

plt.title(
    "ThreatVision AI - Feature Importance"
)

plt.xlabel("Network Behavior Feature")

plt.ylabel("Importance")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.savefig(
    "results/feature_importance.png",
    dpi=300
)

plt.close()


# ---------------------------------------
# Display results
# ---------------------------------------

print()
print("=" * 60)
print("THREATVISION AI - EXPLAINABLE AI")
print("=" * 60)

print()

print(importance_df.to_string(index=False))

print()

print("Created:")
print("results/feature_importance.csv")
print("results/feature_importance.png")

print()

print("Feature importance analysis completed.")

print("=" * 60)