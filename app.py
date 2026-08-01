import streamlit as st
import pandas as pd
import joblib

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- Custom CSS (Neon Purple & Violet Theme) ----------------
st.markdown("""
    <style>
        .stApp {
            background: radial-gradient(circle at top left, #1a0b2e 0%, #0d0518 60%, #05020c 100%);
        }
        .block-container {
            padding-top: 2rem;
        }
        h1, h2, h3, h4, h5, h6, p, label, span, div {
            color: #e6d9ff;
        }
        .title-box {
            text-align: center;
            padding: 22px 10px;
            background: linear-gradient(90deg, #6a0dad, #9d4edd, #c77dff);
            border-radius: 14px;
            margin-bottom: 25px;
            box-shadow: 0 0 25px rgba(157, 78, 221, 0.7), 0 0 60px rgba(106, 13, 173, 0.4);
        }
        .title-box h1 {
            color: #ffffff !important;
            font-size: 2.3rem;
            margin-bottom: 4px;
            text-shadow: 0 0 12px #e0aaff;
        }
        .title-box p {
            color: #f3e8ff !important;
            font-size: 1rem;
            margin: 0;
        }
        .info-panel {
            background: #14091f;
            border: 1px solid #6a0dad;
            border-left: 5px solid #c77dff;
            border-radius: 14px;
            padding: 25px 22px;
            box-shadow: 0 0 18px rgba(157, 78, 221, 0.35);
        }
        .info-panel h3 {
            color: #e0aaff !important;
            margin-top: 0;
            text-shadow: 0 0 8px rgba(224, 170, 255, 0.5);
        }
        .info-panel p {
            color: #dcd0f0 !important;
        }
        .info-panel ul {
            padding-left: 20px;
        }
        .info-panel li {
            margin-bottom: 8px;
            font-size: 0.95rem;
            color: #c9b8e8 !important;
        }
        .form-panel {
            background: #14091f;
            border: 1px solid #6a0dad;
            border-radius: 14px;
            padding: 25px 28px 8px 28px;
            box-shadow: 0 0 18px rgba(157, 78, 221, 0.35);
        }
        .form-panel h3 {
            color: #e0aaff !important;
        }
        div.stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #6a0dad, #9d4edd, #c77dff);
            color: white;
            font-size: 18px;
            font-weight: 600;
            padding: 10px;
            border-radius: 10px;
            border: none;
            box-shadow: 0 0 15px rgba(157, 78, 221, 0.6);
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background: linear-gradient(90deg, #9d4edd, #c77dff, #e0aaff);
            box-shadow: 0 0 30px rgba(224, 170, 255, 0.9);
            transform: scale(1.02);
        }
        .result-box {
            padding: 18px;
            border-radius: 12px;
            text-align: center;
            font-size: 1.3rem;
            font-weight: 700;
            margin-top: 15px;
        }
        .approved {
            background-color: #1f0a33;
            color: #c77dff !important;
            border: 2px solid #9d4edd;
            box-shadow: 0 0 20px rgba(157, 78, 221, 0.6);
        }
        .rejected {
            background-color: #2a0a1f;
            color: #ff6ec7 !important;
            border: 2px solid #ff2fb2;
            box-shadow: 0 0 20px rgba(255, 47, 178, 0.5);
        }
        .footer {
            text-align: center;
            margin-top: 35px;
            padding: 12px;
            color: #a688cc !important;
            font-size: 0.85rem;
        }
        section[data-testid="stSidebar"] {
            display: none;
        }
        /* Slider accent */
        div[data-baseweb="slider"] div[role="slider"] {
            background-color: #c77dff !important;
            box-shadow: 0 0 10px #c77dff;
        }
        div[data-baseweb="slider"] > div > div {
            background: #6a0dad !important;
        }
        /* Selectbox */
        div[data-baseweb="select"] > div {
            background-color: #1f0a33 !important;
            border-color: #6a0dad !important;
        }
        hr {
            border-color: #6a0dad !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- Load Model ----------------
model = joblib.load("loan_approval_model.pkl")

# ---------------- Header ----------------
st.markdown("""
    <div class="title-box">
        <h1>🏦 Loan Approval Prediction</h1>
        <p>Fill in the applicant details to check loan approval status instantly.</p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- Layout: Explanation + Form ----------------
left_col, right_col = st.columns([1, 1.6], gap="large")

with left_col:
    st.markdown("""
        <div class="info-panel">
            <h3>ℹ️ About This App</h3>
            <p>This tool uses a trained Machine Learning model to predict
            whether a bank loan application is likely to be
            <b>Approved</b> or <b>Rejected</b>, based on applicant
            information.</p>
            <h3>📋 How It Works</h3>
            <ul>
                <li>Enter personal, financial and property details</li>
                <li>Click <b>Predict Loan Status</b></li>
                <li>The model instantly analyzes the data</li>
                <li>Get your result with a clear approval/rejection message</li>
            </ul>
            <h3>🧠 Factors Considered</h3>
            <ul>
                <li>Gender, Marital Status & Dependents</li>
                <li>Education & Employment Type</li>
                <li>Applicant & Co-applicant Income</li>
                <li>Loan Amount & Term</li>
                <li>Credit History & Property Area</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="form-panel">', unsafe_allow_html=True)

    st.subheader("👤 Personal Details")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
    with col2:
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])

    dependents = st.slider("Number of Dependents", min_value=0, max_value=10, value=0, step=1)

    st.divider()
    st.subheader("💰 Financial Details")

    applicant_income = st.slider("Applicant Monthly Income", min_value=0, max_value=100000, value=5000, step=500)
    coapplicant_income = st.slider("Coapplicant Monthly Income", min_value=0, max_value=50000, value=0, step=500)
    loan_amount = st.slider("Loan Amount (in thousands)", min_value=0, max_value=700, value=120, step=5)
    loan_term = st.slider("Loan Amount Term (in days)", min_value=0, max_value=480, value=360, step=12)

    st.divider()
    st.subheader("🏠 Credit & Property")

    col3, col4 = st.columns(2)
    with col3:
        credit_history = st.selectbox("Credit History", ["Good (1.0)", "Bad (0.0)"])
    with col4:
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    st.write("")
    predict_clicked = st.button("🔍 Predict Loan Status")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- Encoding ----------------
gender_enc = 1 if gender == "Male" else 0
married_enc = 1 if married == "Yes" else 0
education_enc = 0 if education == "Graduate" else 1
self_employed_enc = 1 if self_employed == "Yes" else 0
credit_history_enc = 1.0 if credit_history.startswith("Good") else 0.0

if property_area == "Rural":
    property_area_enc = 0
elif property_area == "Semiurban":
    property_area_enc = 1
else:
    property_area_enc = 2

data = pd.DataFrame({
    "Gender": [gender_enc],
    "Married": [married_enc],
    "Dependents": [float(dependents)],
    "Education": [education_enc],
    "Self_Employed": [self_employed_enc],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [float(coapplicant_income)],
    "LoanAmount": [float(loan_amount)],
    "Loan_Amount_Term": [float(loan_term)],
    "Credit_History": [credit_history_enc],
    "Property_Area": [property_area_enc]
})

# ---------------- Predict ----------------
if predict_clicked:
    prediction = model.predict(data)
    if prediction[0] == 1:
        st.markdown('<div class="result-box approved">✅ Congratulations! Loan Approved</div>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown('<div class="result-box rejected">❌ Sorry, Loan Rejected</div>', unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown("""
    <div class="footer">
        Developed by <b>Misbah Bibi</b> — Software Engineering Student & AI / Machine Learning Engineer
    </div>
""", unsafe_allow_html=True)
