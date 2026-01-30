# app.py
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("eligibility_model.pkl")

st.title("Citizen Eligibility Prediction System")

# -------- USER INPUTS --------
age = st.slider("Age", 18, 70, 30)

gender = st.selectbox("Gender", ["Female", "Male", "Others"])
gender_map = {"Female": 0, "Male": 1, "Others": 2}
gender = gender_map[gender]

income = st.number_input("Annual Income (INR)", 30000, 1000000)

employment_map = {
    "Unemployed": 0,
    "Self-Employed": 1,
    "Employed": 2
}
emp_status = st.selectbox("Employment Status", employment_map.keys())
employment = employment_map[emp_status]

family = st.slider("Family Size", 1, 8)

education_map = {
    "Primary": 0,
    "Secondary": 1,
    "Graduate": 2,
    "Postgraduate": 3
}
education_level = st.selectbox("Education Level", education_map.keys())
education = education_map[education_level]

caste_map = {
    "SC": 0,
    "ST": 1,
    "OBC": 2,
    "General": 3
}
caste_value = st.selectbox("Caste", caste_map.keys())
caste = caste_map[caste_value]

disability = st.radio("Disability", ["No", "Yes"])
disability = 1 if disability == "Yes" else 0

area = st.radio("Area", ["Rural", "Urban"])
rural_urban = 0 if area == "Rural" else 1


# -------- PREDICTION --------
if st.button("Predict Eligibility"):

    input_data = pd.DataFrame([[
        age,
        gender,
        income,
        employment,
        family,
        education,
        caste,
        disability,
        rural_urban,
    ]], columns=model.feature_names_in_)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Eligible for Government Scheme")
    else:
        st.error("❌ Not Eligible for Government Scheme")