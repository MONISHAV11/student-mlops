import pandas as pd

REQUIRED_COLUMNS = [
    'school', 'sex', 'age', 'address', 'famsize', 'Pstatus',
    'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian',
    'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup',
    'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic',
    'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health',
    'absences', 'G1', 'G2', 'G3'
]

def validate_data(df: pd.DataFrame):
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        print("❌ Validation failed. Missing columns:", missing)
        print("➡️ Found columns:", df.columns.tolist())
        raise ValueError("Validation failed due to missing columns")
    print("✅ Data validation passed. All required columns present.")

if __name__ == "__main__":
    df = pd.read_csv("data/raw/student.csv")
    validate_data(df)
