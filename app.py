import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("telecom_churn_model.pkl", "rb"))

st.title("📱 Telecom Customer Churn Prediction Dashboard")

st.write("Enter customer details:")

# Inputs
SeniorCitizen = st.selectbox("Senior Citizen (0 = No, 1 = Yes)", [0, 1])
Tenure = st.number_input("Tenure (Months)")
MonthlyCharges = st.number_input("Monthly Charges")
TotalCharges = st.number_input("Total Charges")

Gender = st.selectbox("Gender", ["Male", "Female"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaymentMethod = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

if st.button("Predict Churn"):
    
    # Convert categorical to numeric (must match training encoding)
    gender_male = 1 if Gender == "Male" else 0

    contract_one_year = 1 if Contract == "One year" else 0
    contract_two_year = 1 if Contract == "Two year" else 0

    pm_electronic = 1 if PaymentMethod == "Electronic check" else 0
    pm_mailed = 1 if PaymentMethod == "Mailed check" else 0
    pm_bank = 1 if PaymentMethod == "Bank transfer (automatic)" else 0
    pm_credit = 1 if PaymentMethod == "Credit card (automatic)" else 0

    # Final input array (must match training feature order!)
    input_data = np.array([[
        SeniorCitizen,
        Tenure,
        MonthlyCharges,
        TotalCharges,
        gender_male,
        contract_one_year,
        contract_two_year,
        pm_electronic,
        pm_mailed,
        pm_bank,
        pm_credit
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer will stay")