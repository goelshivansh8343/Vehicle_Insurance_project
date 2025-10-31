

# import streamlit as st
# import numpy as np
# from PIL import Image
# import joblib
# import pandas as pd
# # --------------------------
# # Page Configuration
# # --------------------------
# st.set_page_config(page_title="Vehicle Insurance Prediction", page_icon="🚗", layout="centered")

# # --------------------------
# # Header Section
# # --------------------------
# st.markdown(
#     """
#     <div style='text-align: center;'>
#         <h1 style='color:#2E86C1;'>🚗 Vehicle Insurance Prediction System</h1>
#         <h3>Let's find out if the company will give insurance or not!</h3>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # --------------------------
# # Image Banner
# # --------------------------
# st.image("https://cdn.pixabay.com/photo/2017/01/06/19/15/car-1957037_1280.jpg", use_container_width=True)

# st.markdown("---")

# # --------------------------
# # User Input Section
# # --------------------------
# st.subheader("🔍 Enter Customer Details Below")

# col1, col2 = st.columns(2)

# with col1:
#     gender = st.selectbox("👫 Gender", ["Male", "Female"])
#     age = st.number_input("🎂 Age", min_value=18, max_value=100, step=1)
#     driving_license = st.selectbox("🚘 Driving License (1: Yes, 0: No)", [1, 0])
#     region_code = st.number_input("🌍 Region Code", min_value=0.0, step=0.1)
#     previously_insured = st.selectbox("🛡️ Previously Insured (1: Yes, 0: No)", [1, 0])

# with col2:
#     vehicle_damage = st.selectbox("💥 Vehicle Damage Before?", ["Yes", "No"])
#     annual_premium = st.number_input("💰 Annual Premium", min_value=1000.0, step=100.0)
#     policy_sales_channel = st.number_input("📊 Policy Sales Channel", min_value=1, step=1)
#     vintage = st.number_input("📅 Vintage (Days)", min_value=0, step=1)
#     less_1_year = False
#     more_2_years =False
#     vehicle_age=st.number_input("Vehicle_Age",step=1)
#     if(vehicle_age>2):
#         less_1_year=False
#         more_2_years=True
#     elif(vehicle_age<1):
#         less_1_year=True
#         more_2_years=False
# st.markdown("---")
# if gender is "Male":
#     gender=1
# else:
#     gender=0

# if vehicle_damage is "Yes":
#     vehicle_damage=1
# else:
#     vehicle_damage=0

# # --------------------------
# # Prepare Input Data
# # --------------------------
# input_data = np.array([[gender, age, driving_license, region_code, previously_insured,
#                         vehicle_damage, annual_premium, policy_sales_channel, vintage,
#                         less_1_year, more_2_years]])

# columns = ['Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured',
#            'Vehicle_Damage', 'Annual_Premium', 'Policy_Sales_Channel', 'Vintage',
#            '< 1 Year', '> 2 Years']

# # --------------------------
# # Prediction Button
# # --------------------------
# if st.button("🔮 Predict Insurance Eligibility"):
#     st.markdown(
#         "<h4 style='text-align:center; color:#117A65;'>Model is analyzing your details...</h4>",
#         unsafe_allow_html=True
#     )
#     input_df = pd.DataFrame(input_data, columns=columns)
#     prediction = joblib.load("artifact/artifact_objects/preprocessor.pkl")
#     model = joblib.load("artifact/artifact_objects/model.pkl")
#     op=prediction.fit_transform(input_df)
#     ll=model.predict(op)
    
#     # Placeholder for actual model prediction
#     if(ll==1):
#          st.success("✅ Eligible for Insurance")
#     else:
#         st.error("❌ Not Eligible for Insurance")


#     # prediction = np.random.choice(["✅ Eligible for Insurance", "❌ Not Eligible for Insurance"])
    
#     # st.success(f"Prediction Result: **{prediction}**")

# st.markdown("---")
# st.caption("© 2025 Vehicle Insurance Prediction | Built By Shivansh_Goel")


# # values = [[1, 35, 1, 28.0, 0, 1, 35000.0, 152.0, 120, True, False]]



import streamlit as st
import numpy as np
import pandas as pd
import joblib

# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(page_title="Vehicle Insurance Predictor", page_icon="🚗", layout="wide")

# --------------------------
# Header Section
# --------------------------
# st.markdown(
#     """
#     <div style='text-align:center; background-color:#EAF2F8; padding:20px; border-radius:10px;'>
#         <h1 style='color:#2E86C1; font-size:45px;'>🚗 Vehicle Insurance Prediction System</h1>
#         <p style='font-size:20px; color:#566573;'>Find out if the company will provide you insurance coverage!</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
st.markdown(
    """
    <div style='text-align:center; background-color:#EAF2F8; padding:20px; border-radius:15px; box-shadow:0px 4px 8px rgba(0,0,0,0.1);'>
        <h1 style='color:#2E86C1; font-size:45px;'>
            🏍️ 🚗 🚚 ✈️ <br>
            Vehicle Insurance Prediction System
        </h1>
        <p style='font-size:20px; color:#566573;'>
            Find out if the company will provide you insurance coverage!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------
# Banner Image
# --------------------------
# st.image(
#     "https://cdn.pixabay.com/photo/2016/06/01/08/39/car-1425160_1280.jpg",
#     use_container_width=True,
#     caption="Your Car, Our Responsibility 🛡️"
# )
# st.image(
#     "https://images.unsplash.com/photo-1503376780353-7e6692767b70",
#     # use_container_width=True,
#     caption="Your Vehicle, Our Responsibility 🛡️"
# )


st.markdown("---")

# --------------------------
# Input Section
# --------------------------
st.subheader("🧾 Fill Customer & Vehicle Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.radio("👫 Select Gender", ["Male", "Female"], horizontal=True)
    age = st.slider("🎂 Customer Age", min_value=18, max_value=100, value=30)
    driving_license_text = st.radio(
        "🚘 Do you have a valid driving license?",
        ["Yes, I have one", "No, I don’t"],
        horizontal=True
    )
    region_code = st.slider("🌍 Select Region Code", min_value=10.0, max_value=300.0, step=1.0, value=45.0)
    previously_insured_text = st.radio(
        "🛡️ Have you been previously insured?",
        ["Yes", "No"],
        horizontal=True
    )

with col2:
    vehicle_damage_text = st.radio("💥 Has your vehicle been damaged before?", ["Yes", "No"], horizontal=True)
    annual_premium = st.number_input("💰 Annual Premium (in ₹)", min_value=1000.0, step=500.0, value=15000.0)
    policy_sales_channel = st.slider("📊 Policy Sales Channel", min_value=1, max_value=200, value=50)
    vintage = st.slider("📅 Vintage (Days with company)", min_value=0, max_value=500, value=100)
    vehicle_age = st.slider("🚙 Vehicle Age (Years)", min_value=0, max_value=10, value=2)

# --------------------------
# Preprocess User Input
# --------------------------
less_1_year = vehicle_age < 1
more_2_years = vehicle_age > 2

gender = 1 if gender == "Male" else 0
driving_license = 1 if "Yes" in driving_license_text else 0
previously_insured = 1 if previously_insured_text == "Yes" else 0
vehicle_damage = 1 if vehicle_damage_text == "Yes" else 0

input_data = np.array([[gender, age, driving_license, region_code, previously_insured,
                        vehicle_damage, annual_premium, policy_sales_channel, vintage,
                        less_1_year, more_2_years]])

columns = ['Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured',
           'Vehicle_Damage', 'Annual_Premium', 'Policy_Sales_Channel', 'Vintage',
           '< 1 Year', '> 2 Years']

st.markdown("---")

# --------------------------
# Prediction Button
# --------------------------
if st.button("🔮 Predict Insurance Eligibility", use_container_width=True):
    st.info("⏳ Model is analyzing your details...")

    input_df = pd.DataFrame(input_data, columns=columns)
    preprocessor = joblib.load("artifact/artifact_objects/preprocessor.pkl")
    model = joblib.load("artifact/artifact_objects/model.pkl")

    processed_data = preprocessor.transform(input_df)
    prediction = model.predict(processed_data)

    st.markdown("---")
    if prediction == 1:
        st.success("✅ Congratulations! The company is likely to provide insurance.")
        st.image("https://cdn-icons-png.flaticon.com/512/1077/1077114.png", width=150)
    else:
        st.error("❌ Sorry! The company may not offer insurance based on your profile.")
        st.image("https://cdn-icons-png.flaticon.com/512/564/564619.png", width=150)

st.markdown("---")

# --------------------------
# Footer
# --------------------------
st.markdown(
    """
    <div style='text-align:center; color:gray; font-size:14px;'>
        © 2025 Vehicle Insurance Predictor | Built with ❤️ by <b>Shivansh Goel</b>
    </div>
    """,
    unsafe_allow_html=True
)
