# 📘 Customer Churn Prediction — End-to-End Machine Learning System (Production Ready)
**By: Masood Manzoor Ahmed — Machine Learning Engineer (Telecom • AI • Cloud)**

---

## 📑 Table of Contents
1. Project Overview  
2. Business Problem  
3. Dataset Description  
4. Tech Stack  
5. Data Preprocessing  
6. Exploratory Data Analysis  
7. Model Development  
8. Model Evaluation  
9. Final Production Model  
10. Top Churn Drivers  
11. Business Recommendations  
12. How to Run Locally  
13. AWS EC2 Deployment  
14. CI/CD Pipeline (GitHub Actions → EC2)  
15. Architecture Diagram  
16. Future Enhancements  
17. About the Author  
18. Contact  

---

# 1. Project Overview

This project develops a **production-grade Machine Learning system** that predicts telecom customer churn.  
It demonstrates a complete end-to-end ML engineering workflow used by **Saudi, UAE, and Qatar telecom companies**.

### The system includes:
- Full preprocessing pipeline  
- Exploratory Data Analysis (EDA)  
- Imbalance handling with SMOTE  
- Model training (LogReg, Random Forest, XGBoost)  
- ANN (Keras + TensorFlow)  
- Evaluation: AUC, F1, Recall, Confusion Matrices  
- Streamlit Web App  
- AWS EC2 deployment  
- Automated CI/CD using GitHub Actions  

This mirrors real enterprise telecom churn prediction pipelines.

---

# 2. Business Problem

Telecom providers lose millions due to customer churn.  
This system answers:

> **“Which customers are likely to churn next month, and why?”**

### Business value:
- Reduce churn rate  
- Improve customer retention  
- Enable targeted discount/offer strategies  
- Increase annual revenue  
- Support retention teams with risk segmentation  

---

# 3. Dataset Description

**Dataset:** IBM Telco Customer Churn  
**Rows:** 7032  
**Predictors:** 20  
**Target Column:** `Churn` (Yes/No)

### Includes:
- Customer demographics  
- Phone & Internet services  
- Contract type  
- Billing & payment patterns  
- Monthly & total spending  
- Tenure  

---

# 4. Tech Stack

| Category           | Tools |
|-------------------|-------|
| Programming       | Python |
| Data Processing   | Pandas, NumPy |
| Visualization     | Matplotlib, Seaborn |
| ML Models         | Logistic Regression, Random Forest, XGBoost |
| Deep Learning     | TensorFlow / Keras |
| Handling Imbalance| SMOTE (imblearn) |
| Model Saving      | Joblib |
| Web Deployment    | Streamlit |
| Cloud Hosting     | AWS EC2 (Ubuntu 22.04) |
| CI/CD             | GitHub Actions + SSH Deploy |

---

# 5. Data Preprocessing

### ✔ Missing & Invalid Values
- Cleaned `TotalCharges`  
- Converted to float  
- Removed 11 corrupted entries  

### ✔ Data Cleaning
- Trimmed whitespace  
- Dropped `customerID` as non-predictive  

### ✔ Encoding & Scaling
- One-Hot Encoding for categorical columns  
- StandardScaler for numerical columns  

### ✔ Fixing Imbalance: SMOTE
- Before SMOTE: **1869 churn cases**  
- After SMOTE: **4130 balanced cases**  

Improves model fairness and recall.

---

# 6. Exploratory Data Analysis (Key Insights)

### High churn groups:
- Tenure < 3 months  
- Month-to-month contracts  
- Fiber optic users  
- High monthly charges  
- Electronic check payment  
- Customers lacking TechSupport / OnlineSecurity  

Gender had **no significant correlation** with churn.

---

# 7. Model Development

Trained and compared four different models:

- Logistic Regression  
- Random Forest  
- XGBoost  
- ANN (TensorFlow/Keras)  

All models follow the **same preprocessing pipeline** for fairness.

---

# 8. Model Evaluation

## 📌 AUC Scores

| Model               | AUC     |
|--------------------|---------|
| **ANN (Best)**     | **0.826** |
| Logistic Regression | 0.822   |
| XGBoost             | 0.821   |
| Random Forest       | 0.814   |

<br>

## 📌 Classification Metrics Summary

| Model               | Accuracy | Recall (Churn) | F1 (Churn) |
|---------------------|----------|----------------|------------|
| Logistic Regression | 0.74     | **0.72**       | 0.60       |
| Random Forest       | 0.77     | 0.64           | 0.60       |
| XGBoost             | 0.76     | 0.66           | 0.59       |
| **ANN**             | **0.78** | 0.62           | 0.61       |

<br>

All models performed reliably for business production use.

---

# 9. Final Production Model — Random Forest

Although the ANN achieved the **best AUC**, the selected production model is:

## ✅ **Random Forest Classifier (with full preprocessing pipeline + SMOTE)**

### Why Random Forest?
- Most stable across all metrics  
- Best balance between precision & recall  
- Easy to deploy (no TensorFlow overhead)  
- Fast inference on EC2  
- Interpretable for business teams  
- Highly effective on tabular business datasets  

---

# 10. Top 10 Churn Drivers

| Rank | Feature                       | Explanation |
|------|-------------------------------|-------------|
| 1    | tenure                        | Shorter stay → higher churn |
| 2    | TotalCharges                  | Low lifetime value → churn |
| 3    | MonthlyCharges                | High monthly bill → cancellation |
| 4    | Contract_TwoYear              | Strong retention |
| 5    | PaymentMethod_ElectronicCheck | Highest churn method |
| 6    | InternetService_FiberOptic    | Higher expectations → churn |
| 7    | PaperlessBilling_Yes          | Price-sensitive users |
| 8    | Contract_OneYear              | Medium retention |
| 9    | gender_Male                   | Minimal effect — model used it in minor splits |
| 10   | OnlineSecurity_Yes            | Reduces churn |

Note: Gender showed no meaningful correlation with churn in EDA.
ML model assigned small importance due to feature interactions, not because gender truly drives churn.
---

# 11. Business Recommendations

- Target first-3-month customers  
- Move users to **1–2 year contracts**  
- Offer retention offers for high-bill users  
- Convert Electronic Check → Auto-Pay  
- Promote TechSupport & Security add-ons  
- Improve Fiber Optic service quality  

---

# 12. How to Run Locally

```
pip install -r requirements.txt
streamlit run app_streamlit.py

```

---

# 13. AWS EC2 Deployment (Production)

```
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

streamlit run app/app_streamlit.py --server.address 0.0.0.0 --server.port 8501
```

Access:  
`http://<EC2-PUBLIC-IP>:8501`

---

# 14. CI/CD Pipeline (GitHub Actions → EC2)

This project includes a **full CI/CD pipeline**.

### CI (Continuous Integration)
On every push to `main`:
- Python environment is created  
- Dependencies installed  
- Streamlit smoke test runs  
- Ensures app does not crash  

### CD (Continuous Deployment)
If CI passes:  
- GitHub Actions SSHs into EC2  
- Pulls latest code  
- Installs dependencies  
- Automatically updates production app  

### Benefits:
- No manual deployment  
- Zero-downtime updates  
- Production always matches GitHub  
- Follows modern MLOps practices  

---

# 15. System Architecture Diagram

```
                    ┌───────────────────────────────┐
                    │      Google Colab (Training)  │
                    │  SMOTE + RF + ANN + Evaluation│
                    └───────────────┬───────────────┘
                                    │
                                    ▼
             ┌───────────────────────────────────────────┐
             │ Local Machine (VS Code)                   │
             │ Model Artifacts + Streamlit App           │
             └───────────────┬───────────────────────────┘
                             │ Git Push
                             ▼
           ┌───────────────────────────────────────────┐
           │           GitHub Repository               │
           │   CI: Install + Test Streamlit App        │
           │   CD: SSH into EC2 → git pull             │
           └───────────────┬───────────────────────────┘
                            │ Auto Deploy
                            ▼
        ┌──────────────────────────────────────────────────────┐
        │                     AWS EC2 Ubuntu                   │
        │  venv + Streamlit Server + RandomForest Model        │
        └──────────────────────┬───────────────────────────────┘
                               │
                               ▼
               ┌────────────────────────────────────┐
               │ Telecom Managers / End-Users       │
               │ Web Dashboard for Churn Prediction │
               └────────────────────────────────────┘
```

---

# 16. Future Enhancements

### MLOps / Engineering
- Docker containerization  
- Nginx + Gunicorn for production  
- AWS CloudWatch monitoring  
- Log predictions to PostgreSQL / DynamoDB  

### Modeling
- LightGBM & CatBoost  
- Optuna hyperparameter tuning  
- SHAP explainability dashboard  

### UI/UX
- Full business dashboard (Streamlit/Grafana)  
- Downloadable PDF reports  

### CI/CD
- Automated unit tests  
- Rollback strategy  
- AWS Elastic Beanstalk / ECS deployment  

---

# 17. About the Author

**Masood Manzoor Ahmed**  
Machine Learning Engineer | AI | Cloud | Analytics

Expertise includes:
- Predictive Modeling  
- Deep Learning  
- Telecom Analytics  
- End-to-End ML Engineering  
- Cloud Deployment (AWS)  
- MLOps Foundations  

---

# 18. Contact

📌 **LinkedIn:** www.linkedin.com/in/masoodmanzoorahmed  
📌 **GitHub:** https://github.com/MasoodManzoorAhmed/telco-churn-ml  
📌 **Email:** masoodmanzoorahmed@gmail.com  

