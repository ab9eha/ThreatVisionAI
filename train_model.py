import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv("data/training_data.csv")

X = data[["Failed_Logins"]]
y = data["Attack"]

model = DecisionTreeClassifier()

model.fit(X, y)

joblib.dump(
    model,
    "models/threat_model.pkl"
)

print("Model trained successfully!")