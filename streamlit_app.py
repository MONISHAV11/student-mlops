import streamlit as st
import pandas as pd
import joblib

# Load model
MODEL_PATH = "models/model.pkl"
model = joblib.load(MODEL_PATH)

st.set_page_config(page_title="Student Performance Predictor", layout="centered")

st.title("🎓 Student Performance Prediction App")
st.write("Fill in the details below to predict the final score (G3)")

# Input form
with st.form("prediction_form"):
    school = st.selectbox("School", ["GP", "MS"])
    sex = st.selectbox("Sex", ["F", "M"])
    age = st.number_input("Age", min_value=10, max_value=25, value=18)
    address = st.selectbox("Address", ["U", "R"])
    famsize = st.selectbox("Family Size", ["LE3", "GT3"])
    Pstatus = st.selectbox("Parent Status", ["T", "A"])
    Medu = st.slider("Mother Education (0-4)", 0, 4, 2)
    Fedu = st.slider("Father Education (0-4)", 0, 4, 2)
    Mjob = st.selectbox("Mother Job", ["teacher", "health", "services", "at_home", "other"])
    Fjob = st.selectbox("Father Job", ["teacher", "health", "services", "at_home", "other"])
    reason = st.selectbox("Reason for School Choice", ["home", "reputation", "course", "other"])
    guardian = st.selectbox("Guardian", ["mother", "father", "other"])
    traveltime = st.slider("Travel Time (1-4)", 1, 4, 2)
    studytime = st.slider("Study Time (1-4)", 1, 4, 2)
    failures = st.slider("Past Class Failures", 0, 3, 0)
    schoolsup = st.selectbox("School Support", ["yes", "no"])
    famsup = st.selectbox("Family Support", ["yes", "no"])
    paid = st.selectbox("Extra Paid Classes", ["yes", "no"])
    activities = st.selectbox("Extra Activities", ["yes", "no"])
    nursery = st.selectbox("Nursery", ["yes", "no"])
    higher = st.selectbox("Wants Higher Education", ["yes", "no"])
    internet = st.selectbox("Internet Access", ["yes", "no"])
    romantic = st.selectbox("Romantic Relationship", ["yes", "no"])
    famrel = st.slider("Family Relationship (1-5)", 1, 5, 3)
    freetime = st.slider("Free Time (1-5)", 1, 5, 3)
    goout = st.slider("Going Out (1-5)", 1, 5, 3)
    Dalc = st.slider("Workday Alcohol (1-5)", 1, 5, 1)
    Walc = st.slider("Weekend Alcohol (1-5)", 1, 5, 1)
    health = st.slider("Health (1-5)", 1, 5, 3)
    absences = st.slider("Absences", 0, 100, 4)
    G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
    G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

    submitted = st.form_submit_button("Predict Final Grade")

if submitted:
    input_data = pd.DataFrame([{
        "school": school,
        "sex": sex,
        "age": age,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Medu": Medu,
        "Fedu": Fedu,
        "Mjob": Mjob,
        "Fjob": Fjob,
        "reason": reason,
        "guardian": guardian,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences,
        "G1": G1,
        "G2": G2
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"📊 Predicted Final Grade (G3): {prediction:.2f}")