import streamlit as st
import requests

st.title("Customer Churn Prediction")

tenure = st.slider("Tenure", 1, 72)
monthly_charges = st.number_input("Monthly Charges")

if st.button("Predict"):
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json={
            "tenure": tenure,
            "MonthlyCharges": monthly_charges
        })
        st.write("Prediction:", response.json())
    except:
        st.error("API not running")
