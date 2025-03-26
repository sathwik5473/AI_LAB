import streamlit as st
import joblib

st.title("Loan Approval Process Automation")

# Load the model (Fix: Add quotes around file name)
model = joblib.load("loan_data1.joblib")

# User inputs
Gender = st.number_input("Enter Gender (Male:1, Female:0)", min_value=0, max_value=1)
Married = st.number_input("Enter Marital status (Yes:1, No:0)", min_value=0, max_value=1)
Applicant_income = st.number_input("Enter Applicant Income")
Loan_amount = st.number_input("Enter Loan Amount")

# Predict button
if st.button('Predict Approval'):
    # Fix: Convert inputs to correct type
    prediction = model.predict([[int(Gender), int(Married), float(Applicant_income), float(Loan_amount)]])

    # Fix: Check the first element of the prediction
    if prediction[0] == 'Y':  
        st.success('Loan Approved')
    else:
        st.error('Loan Rejected')
