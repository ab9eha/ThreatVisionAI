import os

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)


# ---------------------------------------
# Create results folder
# ---------------------------------------

os.makedirs("results", exist_ok=True)


# ---------------------------------------
# Load dataset
# ---------------------------------------

data = pd.read_csv("data/training_data.csv")


# ---------------------------------------
# Features and target
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
# Define models
# ---------------------------------------

models = {
    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "Logistic Regression": LogisticRegression(
        random_state=42
    )
}


# ---------------------------------------
# Evaluate models
# ---------------------------------------

results = []

predictions = {}


for name, model in models.items():

    model.fit(X_train, y_train)

    predicted = model.predict(X_test)

    predictions[name] = predicted

    results.append({
        "Model": name,
        "Accuracy": accuracy_score(
            y_test,
            predicted
        ),
        "Precision": precision_score(
            y_test,
            predicted,
            zero_division=0
        ),
        "Recall": recall_score(
            y_test,
            predicted,
            zero_division=0
        ),
        "F1 Score": f1_score(
            y_test,
            predicted,
            zero_division=0
        )
    })


# ---------------------------------------
# Results DataFrame
# ---------------------------------------

results_df = pd.DataFrame(results)


# ---------------------------------------
# Save CSV
# ---------------------------------------

results_df.to_csv(
    "results/model_comparison.csv",
    index=False
)


# ---------------------------------------
# Create model comparison chart
# ---------------------------------------

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score"
]

chart_data = results_df.set_index("Model")[metrics]

ax = chart_data.plot(
    kind="bar",
    figsize=(10, 6)
)

ax.set_title(
    "ThreatVision AI - Model Performance Comparison"
)

ax.set_ylabel("Score")

ax.set_xlabel("Machine Learning Model")

ax.set_ylim(0, 1.05)

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "results/model_comparison.png",
    dpi=300
)

plt.close()


# ---------------------------------------
# Create confusion matrices
# ---------------------------------------

for name, predicted in predictions.items():

    matrix = confusion_matrix(
        y_test,
        predicted
    )

    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=[
            "Normal",
            "Attack"
        ]
    )

    display.plot()

    plt.title(
        f"Confusion Matrix - {name}"
    )

    plt.tight_layout()

    filename = name.lower().replace(
        " ",
        "_"
    )

    plt.savefig(
        f"results/confusion_matrix_{filename}.png",
        dpi=300
    )

    plt.close()


print()
print("=" * 60)
print("RESEARCH RESULTS GENERATED")
print("=" * 60)

print()
print("Created:")

print("results/model_comparison.csv")
print("results/model_comparison.png")

print()
print("Confusion matrices created for:")

for name in models:
    print(f"- {name}")

print()
print("All results saved successfully.")
print("=" * 60)