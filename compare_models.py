import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


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
# Train and evaluate models
# ---------------------------------------

results = []


for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

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

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })


# ---------------------------------------
# Create results table
# ---------------------------------------

results_df = pd.DataFrame(results)


# ---------------------------------------
# Display results
# ---------------------------------------

print()
print("=" * 70)
print("THREATVISION AI - MODEL COMPARISON")
print("=" * 70)

print()

print(
    results_df.to_string(
        index=False,
        formatters={
            "Accuracy": "{:.2f}".format,
            "Precision": "{:.2f}".format,
            "Recall": "{:.2f}".format,
            "F1 Score": "{:.2f}".format
        }
    )
)

print()
print("=" * 70)