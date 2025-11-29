import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(page_title="Telco Customer Churn Predictor", layout="centered")

st.title("📞 Telco Customer Churn Prediction")
st.write("Enter customer details to predict whether they are likely to churn.")

# ---- 1) Load artifacts safely ----
ARTIFACT_PATH = "churn_model_artifacts.pkl"

if not os.path.exists(ARTIFACT_PATH):
    st.error(f"❌ Could not find {ARTIFACT_PATH} in the current folder.")
    st.stop()

try:
    artifacts = joblib.load(ARTIFACT_PATH)
except Exception as e:
    st.error(f"❌ Error loading model artifacts: {e}")
    st.stop()

# Extract objects
model = artifacts.get("model", None)
scaler = artifacts.get("scaler", None)
feature_columns = artifacts.get("feature_columns", None)
num_cols = artifacts.get("num_cols", None)
categorical_cols = artifacts.get("categorical_cols", None)

if model is None or scaler is None or feature_columns is None:
    st.error("❌ Model, scaler, or feature_columns missing in artifacts file.")
    st.stop()

st.success("✅ Model loaded successfully and ready to predict.")

# ---- 2) Form for user input ----
with st.form("churn_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Has Partner?", ["Yes", "No"])
    dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)

    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])

    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox(
        "Payment Method",
        ["Electronic check",
         "Mailed check",
         "Bank transfer (automatic)",
         "Credit card (automatic)"]
    )

    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=1000.0, value=70.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, max_value=100000.0, value=1500.0)

    submitted = st.form_submit_button("Predict Churn")

# ---- 3) Helper: build feature vector exactly like training ----
def prepare_features(form_data: dict) -> pd.DataFrame:
    df_input = pd.DataFrame([form_data])

    df_encoded = pd.get_dummies(df_input, columns=categorical_cols, drop_first=True)

    for col in feature_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    df_encoded = df_encoded[feature_columns]

    df_encoded[num_cols] = scaler.transform(df_encoded[num_cols])

    return df_encoded

# ---- 4) On submit: prepare features + predict ----
if submitted:
    form_data = {
        "gender": gender,
        "SeniorCitizen": int(senior),
        "Partner": partner,
        "Dependents": dependents,
        "tenure": int(tenure),
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": float(monthly_charges),
        "TotalCharges": float(total_charges),
    }

    try:
        X_input = prepare_features(form_data)
        prob = model.predict_proba(X_input)[0, 1]
        pred = int(model.predict(X_input)[0])
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
    else:
        if pred == 1:
            st.error(f"⚠️ High Risk of Churn (Probability: {prob:.2%})")
        else:
            st.success(f"✅ Low Risk of Churn (Probability of Churn: {prob:.2%})")

        st.caption("Model: Random Forest trained with SMOTE and full preprocessing pipeline.")
