# **📘 Customer Churn Prediction — End-to-End Machine Learning System (Production Ready)**
**By: Masood Manzoor Ahmed — Machine Learning Engineer (Telecom / AI / Cloud)**
________________________________________
## **📑 Table of Contents**
1.	Project Overview
2.	Business Problem
3.	Dataset Description
4.	Tech Stack
5.	Data Preprocessing
6.	Exploratory Data Analysis
7.	Model Development
8.	Model Evaluation
9.	Final Production Model
10.	Top Churn Drivers
11.	Business Recommendations
12.	How to Run Locally
13.	AWS EC2 Deployment
14.	CI/CD Pipeline (GitHub Actions → EC2)
15.	Architecture Diagram
16.	Future Enhancements
17.	About the Author
18.	Contact
________________________________________
# **1. Project Overview**
This project builds a full production-grade Machine Learning system that predicts telecom customer churn.<br>

It showcases real-world ML engineering skills expected by companies in:<br>

🇸🇦 Saudi Arabia • 🇶🇦 Qatar • 🇦🇪 UAE • 🇬🇧 UK<br>

The system includes:<br>

✔ Data preprocessing pipeline<br>

✔ Exploratory Data Analysis<br>

✔ SMOTE for imbalance handling<br>

✔ Model training (LogReg, RF, XGBoost)<br>

✔ Deep Learning ANN using Keras<br>

✔ Evaluation: AUC, F1, Recall, Confusion Matrices<br>

✔ Streamlit web deployment<br>

✔ AWS EC2 cloud hosting<br>

✔ CI/CD pipeline with GitHub Actions + SSH auto-deploy<br>

This mirrors real enterprise telecom churn prediction workflows.<br>

________________________________________
# **2. Business Problem**
Telecom providers lose millions due to customer churn.<br>

This system answers:<br>

“Which customers are likely to leave next month, and why?”<br>

Value to business:<br>

•	Reduce churn rate<br>

•	Improve customer retention<br>

•	Offer personalized promotions<br>

•	Increase revenue and customer satisfaction<br>

•	Focus retention teams on high-risk customers<br>

________________________________________
# **3. Dataset Description**
Dataset: IBM Telco Customer Churn<br>

Rows: 7032<br>

Predictors: 20<br>

Target: Churn (Yes/No)<br>

Includes:<br>

•	Demographics<br>

•	Phone/Internet services<br>

•	Contract type<br>

•	Billing & payment<br>

•	Monthly and total charges<br>

•	Tenure<br>

________________________________________
# **4. Tech Stack**
Category	Tools<br>

Languages	Python<br>

Data Processing	Pandas, NumPy<br>

Visualization	Matplotlib, Seaborn<br>

Modeling	Logistic Regression, Random Forest, XGBoost<br>

Deep Learning	TensorFlow / Keras<br>

Handling Imbalance	SMOTE (imblearn)<br>

Model Saving	Joblib<br>

Web Deployment	Streamlit<br>

Cloud Hosting	AWS EC2 (Ubuntu 22.04)<br>

CI/CD	GitHub Actions + EC2 SSH Deploy<br>

________________________________________
# **5. Data Preprocessing**
✔ Missing & Invalid Values<br>

•	Cleaned TotalCharges<br>

•	Removed corrupted rows<br>

•	Converted to float<br>

✔ Data Cleaning<br>

•	Removed whitespaces<br>

•	Dropped customerID<br>

✔ Encoding & Scaling<br>

•	One-Hot Encoding for categorical variables<br>

•	StandardScaler for numerical features<br>

✔ Class Imbalance Fix (SMOTE)<br>

Before: Churn “Yes” = 1869<br>

After SMOTE: 4130 (balanced)<br>

________________________________________
# **6. Exploratory Data Analysis (Key Insights)**
🔥 High Churn Groups:<br>

•	Tenure < 3 months<br>

•	Month-to-month contracts<br>

•	Fiber optic users<br>

•	High monthly charges<br>

•	Payment: Electronic check<br>

•	No online security/tech support<br>

Gender had no significant effect.<br>

________________________________________
# **7. Model Development**
Trained & compared:<br>

✔ Logistic Regression<br>

✔ Random Forest<br>

✔ XGBoost<br>

✔ ANN (TensorFlow/Keras)<br>

All models used the same preprocessing pipeline for fair comparison.<br>

________________________________________
# **8. Model Evaluation**<br>

📌 AUC Scores<br>

Model	AUC<br>

ANN (Best)	0.826<br>

Logistic Regression	0.822<br>

XGBoost	0.821<br>

Random Forest	0.814<br>

📌 Classification Metrics Summary<br>

Model	                        Accuracy	Recall (Churn)	F1 (Churn)<br>

Logistic Regression            	0.74	    0.72	        0.60<br>

Random Forest	                  0.77	    0.64	        0.60<br>

XGBoost	                        0.76	    0.66	        0.59<br>

ANN	                            0.78	    0.62	        0.61<br>

All models performed robustly for business use.<br>

________________________________________
# **9. Final Production Model — Random Forest**
Although ANN had the best AUC, the production-ready model is:<br>

✅ Random Forest (with full preprocessing pipeline + SMOTE)<br>

Why Random Forest?<br>

•	Most stable across metrics<br>

•	Best balance of precision + recall<br>

•	Lightweight (easy to deploy)<br>

•	Interpretable for decision-makers<br>

•	Works exceptionally well on tabular business data<br>

•	Fast inference on cloud servers<br>

________________________________________
# **10. Top 10 Churn Drivers (Feature Importances)**

| Rank | Feature                       | Meaning                                      |
|------|--------------------------------|----------------------------------------------|
| 1    | tenure                         | Shorter stay → high churn                    |
| 2    | TotalCharges                   | Low lifetime value → churn                   |
| 3    | MonthlyCharges                 | High charges → cancellation                  |
| 4    | Contract_Two year              | Strong retention                             |
| 5    | PaymentMethod_Electronic check | Highest churn users                          |
| 6    | InternetService_Fiber optic    | Expensive plans → higher cancellations       |
| 7    | PaperlessBilling_Yes           | Tech-savvy & price-sensitive customers       |
| 8    | Contract_One year              | Medium retention                             |
| 9    | gender_Male                    | Slightly higher churn                        |
| 10   | OnlineSecurity_Yes             | Reduces churn                                |

________________________________________
# **🔥 11. Business Recommendations
✔ Focus on first-3-month customers <br>
✔ Push users to 1–2 year contracts<br>
✔ Offer incentives for high-bill users<br>
✔ Convert customers from Electronic Check → Auto-Pay<br>
✔ Add TechSupport / OnlineSecurity bundles<br>
✔ Improve customer complaints handling for Fiber Optic users<br>
________________________________________
# **12. Run Locally**
pip install -r requirements.txt
streamlit run app_streamlit.py
________________________________________
# **13. AWS EC2 Deployment (Production)**
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

streamlit run app/app_streamlit.py --server.address 0.0.0.0 --server.port 8501
Access:
http://<EC2-PUBLIC-IP>:8501
________________________________________
# **14. CI/CD Pipeline (GitHub Actions → EC2 Auto Deployment)**
This project includes a full CI/CD pipeline:

CI — Continuous Integration

On every push to main:

•	Python environment created

•	Dependencies installed

•	Streamlit “smoke test” runs (ensures app runs)

CD — Continuous Deployment

If CI passes:

•	GitHub Actions connects to EC2 via SSH

•	Pulls latest code

•	Installs dependencies

•	Updates production app automatically

✔ Benefits
•	No manual deployment

•	Zero-downtime updates

•	Production always matches GitHub

•	Professional MLOps setup
________________________________________
# **15. System Architecture Diagram**
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
________________________________________
# **16. Future Enhancements**
🔥 MLOps & Engineering

•	Add Docker container for reproducible deployment

•	Use Nginx + Gunicorn for production-grade serving

•	Add monitoring with AWS CloudWatch

•	Log predictions into RDS/PostgreSQL

🔥 Modeling
•	Try CatBoost / LightGBM

•	Hyperparameter tuning with Optuna

•	Add SHAP explainability dashboard

🔥 User Interface
•	Build a telecom churn dashboard (Streamlit / Grafana)

•	Add downloadable PDF reports

🔁 CI/CD Enhancements
•	Add automated unit tests

•	Add CD rollback strategy

•	Deploy using AWS Elastic Beanstalk or ECS

________________________________________
# **17. About the Author**
Masood Manzoor Ahmed

ML Engineer | AI | Cloud | Analytics

Expertise:

•	Predictive Modeling

•	Deep Learning

•	Telecom Analytics

•	End-to-End ML Pipelines

•	AWS Deployment

•	MLOps Foundations

________________________________________
# **18. Contact**
📌 LinkedIn: www.linkedin.com/in/masoodmanzoorahmed

📌 GitHub: (https://github.com/MasoodManzoorAhmed/telco-churn-ml)

📌 Email: masooodmanzoorahmed@gmail.com

