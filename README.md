# Health Insurance Premium Prediction using Machine Learning

An end-to-end machine learning project that predicts an individual's annual health insurance premium based on demographic, financial, lifestyle, and medical information.

This project was developed as part of the **Data Science & Generative AI Bootcamp** by **Codebasics**. It demonstrates the complete machine learning lifecycle, including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and deployment using Streamlit.

---

## Project Overview

Health insurance companies determine premium amounts based on several customer-specific factors such as age, income, smoking habits, BMI, employment status, and medical history.

The objective of this project is to build a regression model capable of accurately estimating annual health insurance premiums using historical customer data.

The project covers:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Selection
- Multicollinearity Analysis (VIF)
- Feature Scaling
- Model Training
- Model Evaluation
- Error Analysis
- Model Export
- Streamlit Deployment

---

## Dataset

The dataset contains customer information including:

- Age
- Gender
- Marital Status
- Region
- Number of Dependants
- BMI Category
- Smoking Status
- Employment Status
- Annual Income
- Medical History
- Genetic Risk
- Insurance Plan
- Health Insurance Premium (Target Variable)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Statsmodels
- Streamlit
- Joblib

---

## Machine Learning Workflow

```
Dataset
    │
    ▼
Data Cleaning
    │
    ▼
Exploratory Data Analysis
    │
    ▼
Feature Engineering
    │
    ▼
Feature Selection
    │
    ▼
Feature Scaling
    │
    ▼
Train-Test Split
    │
    ▼
Model Training
    │
    ├── Linear Regression
    └── XGBoost Regressor
    │
    ▼
Model Evaluation
    │
    ▼
Error Analysis
    │
    ▼
Model Export
    │
    ▼
Streamlit Deployment
```

---

## Data Preprocessing

The dataset underwent several preprocessing steps before model training:

- Handling missing values
- Removing duplicate records
- Outlier detection and treatment
- Feature engineering
- Encoding categorical variables
- Feature scaling using MinMaxScaler
- Variance Inflation Factor (VIF) analysis
- Feature selection

---

## Feature Engineering

Additional features were created to improve model performance, including:

- Lifestyle Risk Score
- Income in Lakhs
- Encoded Medical History
- Encoded Categorical Variables

---

## Model Performance

### Linear Regression

| Metric | Score |
|---------|-------|
| Training R² Score | **0.9586** |
| Testing R² Score | **0.9573** |

The Linear Regression model performed well and demonstrated good generalization, with similar training and testing scores.

---

### XGBoost Regressor

| Metric | Score |
|---------|-------|
| Testing R² Score | **0.9940** |

The XGBoost Regressor significantly outperformed the baseline Linear Regression model by capturing complex, non-linear relationships within the data. Due to its superior predictive performance, it was selected as the final model for deployment.

---

## Error Analysis

To assess prediction quality, percentage errors between actual and predicted premiums were calculated.

Predictions with an absolute percentage error greater than **10%** were classified as extreme errors.

Results showed that only **6.9%** of the test observations fell into this category, indicating that the model provides reliable premium predictions for the majority of customers.

---

## Project Structure

```
ML-Project-health-premium-prediction/
│
├── app/
│   ├── artifacts/
│   │   ├── scaler.pkl
│   │   └── train_model.pkl
│   │
│   ├── main.py
│   └── prediction_helper.py
│
├── health_premium_prediction.ipynb
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ML-Project-health-premium-prediction.git
```

Move to the project directory:

```bash
cd ML-Project-health-premium-prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Navigate to the application folder:

```bash
cd app
```

Run the Streamlit application:

```bash
streamlit run main.py
```

The application will launch automatically in your default web browser.

---

## Application Features

- User-friendly Streamlit interface
- Real-time insurance premium prediction
- Automatic data preprocessing
- XGBoost-based prediction model
- Fast and accurate predictions
- Model persistence using Pickle

---

## Future Improvements

- Hyperparameter tuning using Optuna
- SHAP Explainability
- Docker containerization
- Cloud deployment
- REST API with FastAPI
- Database integration
- User authentication and history tracking

---

## Acknowledgements

This project was completed as part of the **Data Science & Generative AI Bootcamp** conducted by **Codebasics**.

As part of the bootcamp, learners work on industry-oriented case studies based on business scenarios created by **AtliQ**, a fictional company used throughout Codebasics' projects. This project focuses on building an end-to-end machine learning solution for predicting health insurance premiums, providing practical experience in data preprocessing, feature engineering, model development, evaluation, and deployment.

---

## License

This project is licensed under the MIT License.

---


# Connect with Me

<p align="left">
<a href="https://github.com/Adeel-Khan11" target="_blank">
<img src="https://img.shields.io/badge/GitHub-Adeel--Khan11-181717?style=for-the-badge&logo=github" />
</a>

<a href="https://www.linkedin.com/in/adeel-khan-4a6b56308" target="_blank">
<img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
</a>
</p>

If you found this project helpful, consider giving it a ⭐ on GitHub.hare your feedback.
