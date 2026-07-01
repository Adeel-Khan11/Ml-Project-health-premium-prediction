import pandas as pd
from joblib import load

# ================= Load ================= #


model = load("artifacts/train_model.pkl")
scaler_data = load("artifacts/scaler.pkl")

scaler = scaler_data["scaler"]
cols_to_scale = scaler_data["cols_to_scale"]

# =====================================================
# PREPROCESS
# =====================================================

def preprocess(input_dict):

    columns = [
        'age',
        'number_of_dependants',
        'income_level',
        'income_lakhs',
        'insurance_plan',
        'normalized_risk_score',
        'lifestyle_risk_score',
        'gender_Male',
        'region_Northwest',
        'region_Southeast',
        'region_Southwest',
        'marital_status_Unmarried',
        'bmi_category_Obesity',
        'bmi_category_Overweight',
        'bmi_category_Underweight',
        'smoking_status_Occasional',
        'smoking_status_Regular',
        'employment_status_Salaried',
        'employment_status_Self-Employed'
    ]

    X = pd.DataFrame([[0]*len(columns)], columns=columns)

    # --------------------------------------------------
    # Numerical
    # --------------------------------------------------

    X.loc[0,"age"] = input_dict["age"]

    X.loc[0,"number_of_dependants"] = input_dict["number_of_dependants"]

    X.loc[0,"income_lakhs"] = input_dict["income_lakhs"]

    # --------------------------------------------------
    # Label Encoding
    # --------------------------------------------------

    income_encoder = {
        "<10L":0,
        "10L - 25L":1,
        "25L - 40L":2,
        "> 40L":3
    }

    plan_encoder = {
        "Bronze":0,
        "Silver":1,
        "Gold":2
    }



    X.loc[0,"insurance_plan"] = plan_encoder[input_dict["insurance_plan"]]

    # --------------------------------------------------
    # Medical Risk Score
    # --------------------------------------------------

    disease_score = {
        "diabetes":6,
        "heart disease":8,
        "high blood pressure":6,
        "thyroid":5,
        "no disease":0,
        "none":0
    }

    diseases = input_dict["medical_history"].lower().split(" & ")

    total = 0

    for d in diseases:
        total += disease_score[d]

    # same normalization as training

    X.loc[0,"normalized_risk_score"] = total / 14

    # --------------------------------------------------
    # Lifestyle Risk
    # --------------------------------------------------

    activity = {
        "High":0,
        "Medium":1,
        "Low":4
    }

    stress = {
        "High":4,
        "Medium":1,
        "Low":0
    }

    X.loc[0,"lifestyle_risk_score"] = (
        activity[input_dict["physical_activity"]]
        + stress[input_dict["stress_level"]]
    )

    # --------------------------------------------------
    # One Hot Encoding
    # --------------------------------------------------

    if input_dict["gender"]=="Male":
        X.loc[0,"gender_Male"]=1

    if input_dict["region"]=="Northwest":
        X.loc[0,"region_Northwest"]=1

    elif input_dict["region"]=="Southeast":
        X.loc[0,"region_Southeast"]=1

    elif input_dict["region"]=="Southwest":
        X.loc[0,"region_Southwest"]=1

    # Northeast -> baseline

    if input_dict["marital_status"]=="Unmarried":
        X.loc[0,"marital_status_Unmarried"]=1

    if input_dict["bmi_category"]=="Obesity":
        X.loc[0,"bmi_category_Obesity"]=1

    elif input_dict["bmi_category"]=="Overweight":
        X.loc[0,"bmi_category_Overweight"]=1

    elif input_dict["bmi_category"]=="Underweight":
        X.loc[0,"bmi_category_Underweight"]=1

    if input_dict["smoking_status"]=="Occasional":
        X.loc[0,"smoking_status_Occasional"]=1

    elif input_dict["smoking_status"]=="Regular":
        X.loc[0,"smoking_status_Regular"]=1

    if input_dict["employment_status"]=="Salaried":
        X.loc[0,"employment_status_Salaried"]=1

    elif input_dict["employment_status"]=="Self-Employed":
        X.loc[0,"employment_status_Self-Employed"]=1

    # --------------------------------------------------
    # Scaling
    # --------------------------------------------------

    X[cols_to_scale] = scaler.transform(X[cols_to_scale])

    # Drop because the trained model doesn't expect it
    X.drop(columns=["income_level"], inplace=True)

    return X


# =====================================================
# Prediction
# =====================================================

def predict(input_dict):

    X = preprocess(input_dict)

    prediction = model.predict(X)

    return round(float(prediction[0]),2)