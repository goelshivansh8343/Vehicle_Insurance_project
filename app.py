import streamlit as st
import pickle
import numpy as np
import pandas as pd
import joblib

# Load your preprocessor and model

st.title("🚗 Vehicle Insurance Prediction System")
st.write("Predict whether a customer will buy a vehicle insurance policy.")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100)
driving_license = st.selectbox("Driving License", [0, 1])
region_code = st.number_input("Region Code", min_value=0.0)
previously_insured = st.selectbox("Previously Insured", [0, 1])
vehicle_damage = st.selectbox("Vehicle Damage", ["Yes", "No"])
annual_premium = st.number_input("Annual Premium", min_value=1000.0)
policy_sales_channel = st.number_input("Policy Sales Channel", min_value=1)
vintage = st.number_input("Vintage (days)", min_value=0)
less_1_year = st.selectbox("< 1 Year", [0, 1])
more_2_years = st.selectbox("> 2 Years", [0, 1])

# Prepare input
input_data = np.array([[gender, age, driving_license, region_code, previously_insured,
                        vehicle_damage, annual_premium, policy_sales_channel, vintage,
                        less_1_year, more_2_years]])

# Transform input
columns = ['Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured',
            'Vehicle_Damage', 'Annual_Premium', 'Policy_Sales_Channel', 'Vintage',
            '< 1 Year', '> 2 Years']




values = [[1, 35, 1, 28.0, 0, 1, 35000.0, 152.0, 120, True, False]]

input_df = pd.DataFrame(values, columns=columns)


# Predict
if st.button("Predict"):
    prediction = joblib.load("artifact/artifact_objects/preprocessor.pkl")
    model = joblib.load("artifact/artifact_objects/model.pkl")
    op=prediction.fit_transform(input_df)
    ll=model.predict(op)


    if ll == 1:
        st.success("✅ The customer is **likely to buy** insurance.")
    else:
        st.error("❌ The customer is **not likely** to buy insurance.")
