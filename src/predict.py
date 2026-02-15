# src/predict.py
import joblib
import os
import pandas as pd

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "student_model.pkl")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at {model_path}")

model = joblib.load(model_path)

# Columns that the model expects
REQUIRED_COLUMNS = ["G1", "G2", "studytime", "failures", "absences"]

def predict(input_df):
    """
    input_df: pandas DataFrame with student data
    Returns: single prediction
    """

    # Ensure input is a DataFrame
    if not isinstance(input_df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    # Fill any missing columns with default value 0
    for col in REQUIRED_COLUMNS:
        if col not in input_df.columns:
            input_df[col] = 0

    # Keep only the required columns and correct order
    input_df = input_df[REQUIRED_COLUMNS]

    print("Final input to model:", input_df)
    
    # Make prediction
    prediction = model.predict(input_df)
    
    return prediction[0]  # return first prediction
