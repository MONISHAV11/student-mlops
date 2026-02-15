# app/main.py
import sys
import os
import pandas as pd

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from predict import predict

def main():
    # Example student input data (can modify these values)
    input_data = pd.DataFrame([{
        "G1": 10,
        "G2": 12,
        "studytime": 2,
        "failures": 0,
        # "absences" is missing, it will be automatically filled with 0
    }])

    # Call the predict function
    result = predict(input_data)

    # Print the prediction
    print("Prediction:", result)

if __name__ == "__main__":
    main()
