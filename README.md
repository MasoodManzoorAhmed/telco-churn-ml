
# 📘 **Customer Churn Prediction — End-to-End Machine Learning Project (Production Ready)**

**By: Masood Manzoor Ahmed — Machine Learning Engineer (Telecom / AI / Cloud)**

---

## 📑 **Table of Contents**

1. 📘 Project Overview
2. 🎯 Business Problem
3. 📂 Dataset Description
4. 🔧 Tech Stack
5. 🧼 Data Preprocessing
6. 📊 Exploratory Data Analysis
7. 🤖 Model Development
8. 📈 Model Evaluation
9. 🏆 Final Model Selection
10. 🔥 Top Churn Drivers
11. 💡 Business Recommendations
12. 🧪 How to Run Locally
13. ☁️ AWS EC2 Deployment
14. 🏗 Architecture Diagram
15. 🚀 Future Enhancements
16. 👤 About the Author
17. 📬 Contact

---

# 1️⃣ **Project Overview**

This project builds a **complete, real-world Machine Learning system** for **predicting telecom customer churn**.
It demonstrates practical ML engineering skills used in **Saudi Arabia, Qatar, UAE, and global telecom companies**.

The project includes:

* Full preprocessing pipeline
* EDA (numerical + categorical analysis)
* Handling class imbalance
* ML model training (4 models)
* ANN (Deep Learning)
* Model comparison & AUC scores
* Feature importance
* Business recommendations
* Cloud deployment using Streamlit on AWS EC2

---

# 2️⃣ **Business Problem**

Telecom companies lose millions due to customer churn.

This ML system answers:

> **“Which customers are likely to leave next month, and why?”**

Benefits for telecom operators:

* Retain high-risk customers
* Reduce revenue loss
* Offer targeted promotions
* Improve customer satisfaction
* Improve overall ARPU (Average Revenue Per User)

---

# 3️⃣ **Dataset Description**

**Dataset:** IBM Telco Customer Churn
**Rows:** 7032
**Columns:** 21
**Target:** `Churn` (Yes/No)

Features include:

* Demographics
* Subscription details
* Internet/phone services
* Contract types
* Billing/payment behavior
* Monthly and total spend

---

# 4️⃣ **Tech Stack**

| Category           | Tools                                       |
| ------------------ | ------------------------------------------- |
| Languages          | Python                                      |
| Data Processing    | Pandas, NumPy                               |
| Visualization      | Matplotlib, Seaborn                         |
| ML Models          | Logistic Regression, Random Forest, XGBoost |
| Deep Learning      | TensorFlow / Keras ANN                      |
| Imbalance Handling | SMOTE                                       |
| Deployment         | Streamlit, AWS EC2                          |
| Model Persistence  | Joblib                                      |

---

# 5️⃣ **Data Preprocessing**

Key steps:

### ✔ Handling Missing Data

* Cleaned invalid “TotalCharges” entries
* Converted to float
* Removed 11 corrupted rows

### ✔ Data Cleaning

* Stripped whitespace
* Removed `customerID` (non-predictive)

### ✔ Encoding & Scaling

* One-Hot Encoding for categorical variables
* StandardScaler for numerical features

### ✔ Handling Imbalance (SMOTE)

Before SMOTE:

* Churn “Yes”: **1869**

After SMOTE:

* Churn “Yes”: **4130** (balanced)

This improves recall and fairness of ML models.

---

# 6️⃣ **Exploratory Data Analysis — Key Insights**

### 🔥 High-churn patterns:

* Customers with **0–3 months tenure** → highest risk
* **Month-to-month** contracts churn the most
* **Fiber optic** users churn more than DSL
* **High monthly charges** strongly increase churn
* **Electronic check** payment users churn heavily
* Customers with **TechSupport** churn less
* Gender has **no major impact**

---

# 7️⃣ **Model Development**

Trained 4 classical ML models + 1 deep learning model:

### ✔ Logistic Regression

### ✔ Random Forest

### ✔ XGBoost

### ✔ Deep Learning ANN (Keras)

Each model was trained using the **same preprocessing pipeline** and evaluated on the same test data.

---

# 8️⃣ **Model Evaluation**

### 📌 AUC Scores

| Model               | AUC       |
| ------------------- | --------- |
| **ANN**             | **0.826** |
| Logistic Regression | 0.822     |
| XGBoost             | 0.821     |
| Random Forest       | 0.814     |

### 📌 Test Metrics Summary

| Model               | Accuracy | Recall (Churn) | F1 (Churn) |
| ------------------- | -------- | -------------- | ---------- |
| Logistic Regression | 0.74     | **0.72**       | 0.60       |
| Random Forest       | 0.77     | 0.64           | 0.60       |
| XGBoost             | 0.76     | 0.66           | 0.59       |
| ANN                 | **0.78** | 0.62           | 0.61       |

All models perform well, showing reliability of the pipeline.

---

# 9️⃣ **Final Model Selection — Random Forest (Production Model)**

Although the ANN had the **best AUC**, the production model chosen is:

# ✅ **Random Forest Classifier**

### Reasons:

* Most stable and consistent performance
* Best balance between precision/recall
* Easy deployment
* Lightweight (no TensorFlow overhead)
* Interpretable for telecom stakeholders
* Performs extremely well for **tabular business data**


---

# 🔟 **Top 10 Churn Drivers (Feature Importance)**

| Rank | Feature                       | Meaning                          |
| ---- | ----------------------------- | -------------------------------- |
| 1    | tenure                        | Shorter stay → high churn        |
| 2    | TotalCharges                  | Low lifetime value → churn       |
| 3    | MonthlyCharges                | High charges → cancellation      |
| 4    | Contract_TwoYear              | Strong retention                 |
| 5    | PaymentMethod_ElectronicCheck | Highest churn                    |
| 6    | InternetService_FiberOptic    | Expensive → higher cancellations |
| 7    | PaperlessBilling_Yes          | Price sensitive customers        |
| 8    | Contract_OneYear              | Moderate retention               |
| 9    | gender_Male                   | Slightly higher churn            |
| 10   | OnlineSecurity_Yes            | Reduces churn                    |

---

# 🔥 **11. Business Recommendations**

Based on model findings:

### ✔ Focus on first 3 months of customers

### ✔ Push customers to 1-year and 2-year contracts

### ✔ Offer retention offers to high-bill customers

### ✔ Encourage bank transfer / credit card auto-pay

### ✔ Provide TechSupport / OnlineSecurity add-ons

### ✔ Improve Fiber Optic customer experience

These actions would **significantly reduce churn**.

---

# 12️⃣ **How to Run Locally**

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the Streamlit App:

```bash
streamlit run app_streamlit.py
```

---

# 13️⃣ **AWS EC2 Deployment (Production)**

### ✔ Ubuntu Server 22.04 LTS

### ✔ Deployed using Streamlit

### ✔ Model + pipeline loaded from Pickle

### Steps:

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip python3-venv

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

streamlit run app/app_streamlit.py --server.port 8501 --server.address 0.0.0.0
```

### Access from browser:

```
http://<EC2-PUBLIC-IP>:8501
```

---

# 14️⃣ **System Architecture Diagram**

```
                      ┌───────────────────────────────┐
                      │   Google Colab (Training)      │
                      │  Data Prep + SMOTE + Models    │
                      └───────────────┬───────────────┘
                                      │
                                      ▼
                ┌──────────────────────────────────────────┐
                │     Local Machine (VS Code / Windows)    │
                │    Model Artifacts + Streamlit App       │
                └───────────────┬──────────────────────────┘
                                │   (SCP Upload)
                                ▼
          ┌──────────────────────────────────────────────────────────┐
          │                  AWS EC2 Ubuntu Server                    │
          │   ┌─────────────────────────┐  ┌──────────────────────┐  │
          │   │  Virtual Environment    │  │  Streamlit Frontend  │  │
          │   │  (Dependencies)         │  │  Prediction UI        │  │
          │   └──────────────┬──────────┘  └───────────┬──────────┘  │
          │                  │ loads                    │             │
          │   churn_model_artifacts.pkl (Random Forest) │             │
          └──────────────────┴──────────────────────────┴────────────┘
                                │
                                ▼
                  ┌──────────────────────────────────────┐
                  │   Telecom Managers / End Users        │
                  │  View Predictions in Web Dashboard    │
                  └──────────────────────────────────────┘
```

---

# 15️⃣ **Future Enhancements**

* Deploy backend using **FastAPI**
* Add **CI/CD pipeline (GitHub Actions)**
* Add **Database logging (PostgreSQL / DynamoDB)**
* Build a **Full Retention Dashboard**
* Use **LightGBM / CatBoost** for higher AUC
* Add **Explainability (SHAP Values)**

---

# 👤 **About the Author**

**Masood Manzoor Ahmed**
Machine Learning Engineer | AI | Cloud

Specializes in:

* Predictive Modeling
* Deep Learning
* End-to-End ML Engineering
* Cloud Deployment (AWS)
* Feature Engineering



# 📬 **Contact**

📌 **LinkedIn:** *Add your link*
📌 **GitHub:** *Add repo link*
📌 **Email:** *Add your email*

---


