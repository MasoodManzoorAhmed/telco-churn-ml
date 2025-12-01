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
This project builds a full production-grade Machine Learning system that predicts telecom customer churn.
It showcases real-world ML engineering skills expected by companies in:
🇸🇦 Saudi Arabia • 🇶🇦 Qatar • 🇦🇪 UAE • 🇬🇧 UK
The system includes:
✔ Data preprocessing pipeline
✔ Exploratory Data Analysis
✔ SMOTE for imbalance handling
✔ Model training (LogReg, RF, XGBoost)
✔ Deep Learning ANN using Keras
✔ Evaluation: AUC, F1, Recall, Confusion Matrices
✔ Streamlit web deployment
✔ AWS EC2 cloud hosting
✔ CI/CD pipeline with GitHub Actions + SSH auto-deploy
This mirrors real enterprise telecom churn prediction workflows.
________________________________________
# **2. Business Problem**
Telecom providers lose millions due to customer churn.
This system answers:
“Which customers are likely to leave next month, and why?”
Value to business:
•	Reduce churn rate
•	Improve customer retention
•	Offer personalized promotions
•	Increase revenue and customer satisfaction
•	Focus retention teams on high-risk customers
________________________________________
# **3. Dataset Description**
Dataset: IBM Telco Customer Churn
Rows: 7032
Predictors: 20
Target: Churn (Yes/No)
Includes:
•	Demographics
•	Phone/Internet services
•	Contract type
•	Billing & payment
•	Monthly and total charges
•	Tenure
________________________________________
# **4. Tech Stack**
Category	Tools
Languages	Python
Data Processing	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Modeling	Logistic Regression, Random Forest, XGBoost
Deep Learning	TensorFlow / Keras
Handling Imbalance	SMOTE (imblearn)
Model Saving	Joblib
Web Deployment	Streamlit
Cloud Hosting	AWS EC2 (Ubuntu 22.04)
CI/CD	GitHub Actions + EC2 SSH Deploy
________________________________________
# **5. Data Preprocessing**
✔ Missing & Invalid Values
•	Cleaned TotalCharges
•	Removed corrupted rows
•	Converted to float
✔ Data Cleaning
•	Removed whitespaces
•	Dropped customerID
✔ Encoding & Scaling
•	One-Hot Encoding for categorical variables
•	StandardScaler for numerical features
✔ Class Imbalance Fix (SMOTE)
Before: Churn “Yes” = 1869
After SMOTE: 4130 (balanced)
________________________________________
# **6. Exploratory Data Analysis (Key Insights)**
🔥 High Churn Groups:
•	Tenure < 3 months
•	Month-to-month contracts
•	Fiber optic users
•	High monthly charges
•	Payment: Electronic check
•	No online security/tech support
Gender had no significant effect.
________________________________________
# **7. Model Development**
Trained & compared:
✔ Logistic Regression
✔ Random Forest
✔ XGBoost
✔ ANN (TensorFlow/Keras)
All models used the same preprocessing pipeline for fair comparison.
________________________________________
# **8. Model Evaluation**
📌 AUC Scores
Model	AUC
ANN (Best)	0.826
Logistic Regression	0.822
XGBoost	0.821
Random Forest	0.814
📌 Classification Metrics Summary
Model	Accuracy	Recall (Churn)	F1 (Churn)
Logistic Regression	0.74	0.72	0.60
Random Forest	0.77	0.64	0.60
XGBoost	0.76	0.66	0.59
ANN	0.78	0.62	0.61
All models performed robustly for business use.
________________________________________
# **9. Final Production Model — Random Forest**
Although ANN had the best AUC, the production-ready model is:
✅ Random Forest (with full preprocessing pipeline + SMOTE)
Why Random Forest?
•	Most stable across metrics
•	Best balance of precision + recall
•	Lightweight (easy to deploy)
•	Interpretable for decision-makers
•	Works exceptionally well on tabular business data
•	Fast inference on cloud servers
________________________________________
# **10. Top 10 Churn Drivers (Feature Importances)**
Rank	Feature	Meaning
1	tenure	Shorter stay → higher churn
2	TotalCharges	Low lifetime value → churn
3	MonthlyCharges	High monthly bill → churn
4	Contract_TwoYear	Strong retention
5	PaymentMethod_ElectronicCheck	Highest churn rate
6	InternetService_FiberOptic	High expectations
7	PaperlessBilling_Yes	Price sensitive
8	Contract_OneYear	Mid-level retention
9	gender_Male	Slightly higher churn
10	OnlineSecurity_Yes	Reduces churn
________________________________________
# **🔥 11. Business Recommendations
✔ Focus on first-3-month customers
✔ Push users to 1–2 year contracts
✔ Offer incentives for high-bill users
✔ Convert customers from Electronic Check → Auto-Pay
✔ Add TechSupport / OnlineSecurity bundles
✔ Improve customer complaints handling for Fiber Optic users
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
•	Professional MLOps setup recruiters love
________________________________________
# **15. System Architecture Diagram**
                    ┌───────────────────────────────┐
                    │      Google Colab (Training)   │
                    │  SMOTE + RF + ANN + Evaluation │
                    └───────────────┬───────────────┘
                                    │
                                    ▼
             ┌───────────────────────────────────────────┐
             │ Local Machine (VS Code)                    │
             │ Model Artifacts + Streamlit App            │
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
               │ Telecom Managers / End-Users        │
               │ Web Dashboard for Churn Prediction  │
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

