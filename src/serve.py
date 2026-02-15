import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Paths for SageMaker vs local
SAGEMAKER_MODEL_PATH = "/opt/ml/model/model.pkl"
LOCAL_MODEL_PATH = "models/model.pkl"

MODEL_PATH = SAGEMAKER_MODEL_PATH if os.path.exists(SAGEMAKER_MODEL_PATH) else LOCAL_MODEL_PATH

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")

print(f"Loading model from: {MODEL_PATH}")
model = joblib.load(MODEL_PATH)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok"})

@app.route("/invocations", methods=["POST"])
def predict():
    try:
        payload = request.get_json(force=True)

        if not payload or "inputs" not in payload:
            return jsonify({"error": "Request JSON must contain 'inputs' key"}), 400

        rows = payload["inputs"]

        # Expecting a list of dicts (raw features)
        if not isinstance(rows, list) or not isinstance(rows[0], dict):
            return jsonify({
                "error": "inputs must be a list of objects with feature names as keys"
            }), 400

        # Convert to DataFrame (ColumnTransformer expects column names)
        df = pd.DataFrame(rows)

        preds = model.predict(df)

        return jsonify({"predictions": preds.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
