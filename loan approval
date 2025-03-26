
import streamlit as st
import joblib

st.title("Loan Aprroval Process Automation")
model=joblib.load()


Gender=st.number_input("Enter Gender Male:1 Female:0")
Married=st.number_input("Enter Married status Yes:1 No:0")
Applicant_income=st.number_input("Enter Applicant_Income")
Loan_amount=st.number_input("Enter Loan_Amount")



if st.button('Predict Approval'):
    prediction=model.predict([[Gender,Married,Applicant_income,Loan_amount]])

    if prediction=='Y':
        st.text('Loan Aprroved')
    else:
        st.text('Loan Rejected')
