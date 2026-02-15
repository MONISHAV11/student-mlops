# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Example training data
data = pd.DataFrame({
    "G1": [10, 12, 8, 15],
    "G2": [12, 14, 7, 16],
    "studytime": [2, 3, 1, 4],
    "failures": [0, 1, 0, 0],
    "absences": [3, 4, 2, 1],
    "passed": [1, 1, 0, 1]  # target
})

X = data.drop("passed", axis=1)
y = data["passed"]

# Create a pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=10, random_state=42))
])

# Train the model
pipeline.fit(X, y)

# Save the model to src/
model_path = os.path.join("src", "student_model.pkl")
joblib.dump(pipeline, model_path)
print(f"Model saved to {model_path}")
