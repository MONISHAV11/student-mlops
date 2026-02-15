# inference.py
import joblib
import os
import pandas as pd
import json

# Load the model
def model_fn(model_dir):
    model_path = os.path.join(model_dir, "student_model.pkl")
    model = joblib.load(model_path)
    return model

# Parse incoming request
def input_fn(request_body, content_type):
    if content_type == "application/json":
        data = json.loads(request_body)
        return pd.DataFrame([data])
    raise ValueError("Unsupported content type")

# Run prediction
def predict_fn(input_data, model):
    required_cols = ["G1", "G2", "studytime", "failures", "absences"]
    for col in required_cols:
        if col not in input_data.columns:
            input_data[col] = 0
    input_data = input_data[required_cols]
    return model.predict(input_data)[0]

# Format response
def output_fn(prediction, content_type):
    if content_type == "application/json":
        return json.dumps({"prediction": prediction})
    raise ValueError("Unsupported content type")
