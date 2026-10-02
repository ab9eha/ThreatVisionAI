import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


# ---------------------------------------
# Load multi-feature dataset
# ---------------------------------------

data = pd.read_csv(
    "data/training_data_v2.csv"
)


# ---------------------------------------
# Select features
# ---------------------------------------

features = [
    "Failed_Logins",
    "Connection_Count",
    "Packet_Size",
    "Login_Hour",
    "Port_Requests"
]

X = data[features]

y = data["Attack"]


# ---------------------------------------
# Split dataset
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)


# ---------------------------------------
# Create Random Forest
# ---------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ---------------------------------------
# Train model
# ---------------------------------------

model.fit(
    X_train,
    y_train
)


# ---------------------------------------
# Evaluate
# ---------------------------------------

predictions = model.predict(
    X_test
)


print()
print("=" * 60)
print("THREATVISION AI - MULTI-FEATURE MODEL")
print("=" * 60)

print()

print(
    classification_report(
        y_test,
        predictions,
        target_names=[
            "Normal",
            "Attack"
        ],
        zero_division=0
    )
)


# ---------------------------------------
# Save model
# ---------------------------------------

joblib.dump(
    model,
    "models/multifeature_model.pkl"
)


print()
print("Multi-feature model trained successfully!")

print()
print("Saved to:")
print("models/multifeature_model.pkl")

print()
print("=" * 60)