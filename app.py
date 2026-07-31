import streamlit as st
import pandas as pd
import joblib

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- Custom CSS ----------------
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .title-box {
            text-align: center;
            padding: 20px 10px 10px 10px;
        }
        .title-box h1 {
            color: #1f3c88;
            font-size: 2.4rem;
            margin-bottom: 0px;
        }
        .title-box p {
            color: #555;
            font-size: 1rem;
        }
        div.stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #1f3c88, #2a5298);
            color: white;
            font-size: 18px;
            font-weight: 600;
            padding: 10px;
            border-radius: 10px;
            border: none;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background: linear-gradient(90deg, #2a5298, #1f3c88);
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
            background-color: #d4edda;
            color: #155724;
            border: 2px solid #28a745;
        }
        .rejected {
            background-color: #f8d7da;
            color: #721c24;
            border: 2px solid #dc3545;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 12px;
            color: #888;
            font-size: 0.85rem;
        }
        section[data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- Load Model ----------------
model = joblib.load("loan_approval_model.pkl")

# ---------------- Header ----------------
st.markdown("""
    <div class="title-box">
        <h1>🏦 Loan Approval Prediction</h1>
        <p>Fill in the applicant details below to check loan approval status instantly.</p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- Form ----------------
with st.container(border=True):
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
st.write("")
if st.button("🔍 Predict Loan Status"):
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
