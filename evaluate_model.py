import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# ---------------------------------------
# Load dataset
# ---------------------------------------

data = pd.read_csv("data/training_data.csv")


# ---------------------------------------
# Separate features and target
# ---------------------------------------

X = data[["Failed_Logins"]]
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
# Load trained model
# ---------------------------------------

model = joblib.load("models/threat_model.pkl")


# ---------------------------------------
# Make predictions
# ---------------------------------------

predictions = model.predict(X_test)


# ---------------------------------------
# Calculate metrics
# ---------------------------------------

accuracy = accuracy_score(y_test, predictions)

precision = precision_score(
    y_test,
    predictions,
    zero_division=0
)

recall = recall_score(
    y_test,
    predictions,
    zero_division=0
)

f1 = f1_score(
    y_test,
    predictions,
    zero_division=0
)


# ---------------------------------------
# Display results
# ---------------------------------------

print()
print("=" * 50)
print("THREATVISION AI - MODEL EVALUATION")
print("=" * 50)

print()

print(f"Accuracy :  {accuracy:.2f}")
print(f"Precision:  {precision:.2f}")
print(f"Recall   :  {recall:.2f}")
print(f"F1 Score :  {f1:.2f}")

print()

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print()

print("Classification Report:")
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

print("=" * 50)