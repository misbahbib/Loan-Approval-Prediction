# 🏦 Loan Approval Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a loan application will be **Approved** or **Rejected** using a Machine Learning classification model. The model is trained on historical loan application data and deployed as an interactive web application using **Streamlit**.

---

## 🚀 Features

* Data Cleaning & Preprocessing
* Missing Value Handling
* Label Encoding
* Train-Test Split
* Logistic Regression Model
* Model Evaluation
* Interactive Streamlit Web Application

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

---

## 📊 Dataset Features

* Gender
* Married
* Dependents
* Education
* Self Employed
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Amount Term
* Credit History
* Property Area

### 🎯 Target Variable

**Loan_Status**

* 1 → Loan Approved
* 0 → Loan Rejected

---

## 🤖 Machine Learning Model

**Algorithm:** Logistic Regression

The model was trained on the processed dataset and evaluated using standard classification metrics.

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Model Accuracy

**82.67%**

---

## 📂 Project Structure

Loan-Approval-Prediction/

├── app.py

├── loan_approval_model.pkl

├── requirements.txt

├── README.md

├── loan.csv

---

## ▶️ Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 💡 Future Improvements

* Hyperparameter Tuning
* Random Forest Comparison
* XGBoost Implementation
* SMOTE for Imbalanced Data
* Better UI Design

---

## 👩‍💻 Developed By

**Misbah**

Aspiring AI Engineer | Machine Learning Enthusiast | Python Developer

Building real-world AI & Machine Learning projects while learning and sharing the journey.
