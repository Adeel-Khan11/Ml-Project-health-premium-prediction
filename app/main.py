import streamlit as st
import time
from prediction_helper import predict
# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(
    page_title="Health Insurance Premium Predictor",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ CSS ------------------ #
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

.stApp{
background: linear-gradient(135deg,#0f172a,#111827,#1e3a8a);
background-size:400% 400%;
animation:bg 15s ease infinite;
color:white;
}

@keyframes bg{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.block-container{
padding-top:1rem;
padding-bottom:2rem;
}

section[data-testid="stSidebar"]{
background:#071426;
border-right:1px solid rgba(255,255,255,.08);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p{
color:white;
}

.hero{

padding:40px;

border-radius:25px;

background:linear-gradient(120deg,#2563eb,#7c3aed,#06b6d4);

background-size:300% 300%;

animation:hero 8s ease infinite;

box-shadow:0 20px 40px rgba(0,0,0,.35);

margin-bottom:30px;

}

@keyframes hero{

0%{background-position:0% 50%;}

50%{background-position:100% 50%;}

100%{background-position:0% 50%;}

}

.hero h1{

font-size:48px;

color:white;

font-weight:800;

margin-bottom:10px;

}

.hero p{

font-size:18px;

color:white;

opacity:.95;

}

.card{

background:rgba(255,255,255,.08);

backdrop-filter:blur(18px);

padding:25px;

border-radius:20px;

border:1px solid rgba(255,255,255,.15);

margin-bottom:20px;

box-shadow:0 8px 25px rgba(0,0,0,.25);

transition:.35s;

}

.card:hover{

transform:translateY(-5px);

box-shadow:0 15px 30px rgba(0,0,0,.35);

}

.card-title{

font-size:24px;

font-weight:700;

margin-bottom:15px;

color:#7dd3fc;

}

div[data-baseweb="select"]>div{

background:#13233f;

color:white;

border-radius:12px;

}

input{

border-radius:12px !important;

}

.stNumberInput input{

background:#13233f;

color:white;

}

.stTextInput input{

background:#13233f;

color:white;

}

.stButton>button{

width:100%;

height:65px;

font-size:22px;

font-weight:bold;

border-radius:16px;

border:none;

background:linear-gradient(90deg,#2563eb,#7c3aed);

color:white;

transition:.3s;

}

.stButton>button:hover{

transform:scale(1.03);

box-shadow:0 10px 25px rgba(37,99,235,.45);

}

.metric-card{

background:linear-gradient(135deg,#16a34a,#22c55e);

padding:35px;

border-radius:25px;

text-align:center;

color:white;

box-shadow:0 10px 30px rgba(0,0,0,.3);

}

.footer{

text-align:center;

margin-top:40px;

color:#CBD5E1;

font-size:14px;

}

</style>

""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------ #

with st.sidebar:

    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063822.png", width=120)

    st.title("Health Insurance")

    st.write("### AI Premium Predictor")

    st.info("""
Predict health insurance premiums instantly using Machine Learning.

✔ Personalized Prediction

✔ Fast Results

✔ Accurate Model

✔ Easy Interface
""")

# ------------------ HERO ------------------ #

st.markdown("""

<div class="hero">

<h1>💙 Health Insurance Premium Predictor</h1>

<p>

Estimate your annual health insurance premium using Artificial Intelligence.

Fill in your details below and receive an instant premium prediction.

</p>

</div>

""", unsafe_allow_html=True)

# ------------------ PERSONAL ------------------ #




st.markdown("""
<div class="card">
<div class="card-title">
👤 Personal Information
</div>
""", unsafe_allow_html=True)



col1,col2,col3=st.columns(3)

with col1:

    age=st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1
    )

    gender=st.selectbox(
        "Gender",
        ["Female","Male"]
    )

with col2:

    region=st.selectbox(
        "Region",
        [
            "Southeast",
            "Northeast",
            "Southwest",
            "Northwest"
        ]
    )

    marital_status=st.selectbox(
        "Marital Status",
        [
            "Unmarried",
            "Married"
        ]
    )

with col3:

    bmi=st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=24.5
    )

    bmi_category=st.selectbox(
        "BMI Category",
        [
            "Normal",
            "Overweight",
            "Obesity",
            "Underweight"
        ]
    )

st.markdown("</div>", unsafe_allow_html=True)
# ============================================================
# LIFESTYLE INFORMATION
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<div class="card-title">
🏃 Lifestyle Information
</div>
""", unsafe_allow_html=True)

col1,col2,col3=st.columns(3)

with col1:

    physical_activity=st.selectbox(
        "Physical Activity",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

with col2:

    stress_level=st.selectbox(
        "Stress Level",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

with col3:

    smoking_status=st.selectbox(
        "Smoking Status",
        [
            "No Smoking",
            "Occasional",
            "Regular"
        ]
    )

st.markdown("</div>",unsafe_allow_html=True)


# ============================================================
# EMPLOYMENT INFORMATION
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<div class="card-title">
💼 Employment Information
</div>
""", unsafe_allow_html=True)

col1,col2,col3=st.columns(3)

with col1:

    employment_status=st.selectbox(
        "Employment Status",
        [
            "Salaried",
            "Self-Employed",
            "Freelancer"
        ]
    )

with col2:



    income_lakhs = st.number_input(
        "Annual Income (Lakhs)",
        min_value=1.0,
        max_value=100.0,
        value=15.0,
        step=0.5
    )

with col3:

    dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=10,
        value=2,
        step=1
    )

st.markdown("</div>",unsafe_allow_html=True)


# ============================================================
# MEDICAL INFORMATION
# ============================================================
income_level=0
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<div class="card-title">
❤️ Medical Information
</div>
""", unsafe_allow_html=True)

col1,col2=st.columns(2)

with col1:

    medical_history=st.selectbox(
        "Medical History",
        [
            "No Disease",
            "High blood pressure",
            "Heart disease",
            "Diabetes",
            "Thyroid",
            "Diabetes & High blood pressure",
            "Diabetes & Heart disease",
            "Diabetes & Thyroid",
            "High blood pressure & Heart disease"
        ]
    )

with col2:

    insurance_plan=st.selectbox(
        "Insurance Plan",
        [
            "Bronze",
            "Silver",
            "Gold"
        ]
    )

st.markdown("</div>",unsafe_allow_html=True)


# ============================================================
# SUMMARY CARD
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<div class="card-title">
📋 Review Your Information
</div>
""", unsafe_allow_html=True)

left,right=st.columns(2)

with left:

    st.write(f"**👤 Gender:** {gender}")
    st.write(f"**🎂 Age:** {age}")
    st.write(f"**🌍 Region:** {region}")
    st.write(f"**💍 Marital Status:** {marital_status}")
    st.write(f"**⚖ BMI:** {bmi}")
    st.write(f"**📊 BMI Category:** {bmi_category}")

with right:

    st.write(f"**🏃 Activity:** {physical_activity}")
    st.write(f"**😰 Stress:** {stress_level}")
    st.write(f"**🚭 Smoking:** {smoking_status}")
    st.write(f"**💼 Employment:** {employment_status}")

    st.write(f"**💵 Income (Lakhs):** {income_lakhs}")
    st.write(f"**❤️ Medical:** {medical_history}")
    st.write(f"**❤️ :Plan** {insurance_plan}")

st.markdown("</div>",unsafe_allow_html=True)


# ============================================================
# PREDICT BUTTON
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

predict_btn = st.button("🚀 Predict Insurance Premium")
# ============================================================
# PART 3 : PREDICTION & RESULT
# ============================================================

import time
import random

# ============================================================
# PREDICTION
# ============================================================

if predict_btn:

    progress = st.progress(0)

    status = st.empty()

    for i in range(101):
        time.sleep(0.01)
        progress.progress(i)
        status.info(f"🤖 AI is analyzing your profile... {i}%")

    progress.empty()
    status.empty()

    # ============================================
    # Create input dictionary
    # ============================================

    input_dict = {

        "age": age,

        "number_of_dependants": dependents,

        "income_level": income_level,

        "income_lakhs": income_lakhs,

        "insurance_plan": insurance_plan,

        "gender": gender,

        "region": region,

        "marital_status": marital_status,

        "bmi_category": bmi_category,

        "smoking_status": smoking_status,

        "employment_status": employment_status,

        "physical_activity": physical_activity,

        "stress_level": stress_level,

        "medical_history": medical_history

    }

    try:

        premium = predict(input_dict)

        monthly = premium / 12

        # ----------------------------------------

        if premium < 25000:
            risk = "🟢 LOW RISK"
            color = "#22C55E"

        elif premium < 50000:
            risk = "🟡 MEDIUM RISK"
            color = "#FACC15"

        else:
            risk = "🔴 HIGH RISK"
            color = "#EF4444"

        st.balloons()

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#2563EB,#7C3AED);
            padding:35px;
            border-radius:25px;
            text-align:center;
            box-shadow:0px 12px 35px rgba(0,0,0,.35);
            color:white;
        ">

        <h1>💰 Estimated Annual Premium</h1>

        <h1 style="font-size:60px;">
        ₹ {premium:,.0f}
        </h1>

        <hr>

        <h3>Monthly Premium</h3>

        <h2>
        ₹ {monthly:,.0f}
        </h2>

        </div>

        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "👤 Age",
                age
            )

        with col2:

            st.metric(
                "⚖ BMI",
                bmi_category
            )

        with col3:

            st.metric(
                "👨‍👩‍👧 Dependents",
                dependents
            )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div style="
            background:{color};
            padding:25px;
            border-radius:20px;
            color:white;
            text-align:center;
            font-size:32px;
            font-weight:bold;
        ">
            {risk}
        </div>
        """, unsafe_allow_html=True)

        st.success("✅ Prediction completed successfully!")

      

    except Exception as e:

        st.error("Prediction Failed")

        st.exception(e)

# ============================================================
# SIDEBAR
# ============================================================


st.sidebar.markdown("""
### 🤖 AI Model

🟢 **Status**
> Ready

⚡ **Algorithm**
> XGBoost Regressor

💰 **Prediction**
> Annual Insurance Premium

🎯 **Accuracy**
> High Performance

📊 **Features Used**
> 18 Engineered Features
""")


st.sidebar.header("💡 Health Tips")

st.sidebar.success("🏃 Exercise Daily")

st.sidebar.success("🥗 Healthy Diet")

st.sidebar.success("😴 Sleep 7-8 Hours")

st.sidebar.success("🚭 Avoid Smoking")

st.sidebar.success("🩺 Regular Checkups")

# ============================================================
# FOOTER
# ============================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr style="border:1px solid #334155;">
<div style="text-align:center;color:#CBD5E1;">

<h3>💙 Health Insurance Premium Predictor</h3>

Built with ❤️ using Streamlit & Machine Learning

<p style="font-size:15px;">
AI-powered insurance premium estimation system.
</p>

</div>
""", unsafe_allow_html=True)