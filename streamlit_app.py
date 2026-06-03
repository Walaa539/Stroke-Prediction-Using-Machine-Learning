import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Walaa Salah Stroke Prediction App",
    page_icon="🧠",
    layout="wide"
)

# ---------------------------------------------------------
# Load model
# ---------------------------------------------------------
model = joblib.load("best_stroke_model.pkl")

# ---------------------------------------------------------
# Custom CSS styling
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* -----------------------------------------------------
       Main app background
    ----------------------------------------------------- */
    .stApp {
        background-color: #2f3136;
        color: #f9fafb;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }

    /* -----------------------------------------------------
       General text on dark background
    ----------------------------------------------------- */
    h1, h2, h3, h4, h5, h6,
    p, label,
    .stMarkdown,
    .stText,
    .stCaption {
        color: #f9fafb !important;
    }

    /* -----------------------------------------------------
       Title card
    ----------------------------------------------------- */
    .title-card {
        background: linear-gradient(135deg, #111827, #374151);
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.45);
        margin-bottom: 25px;
        text-align: center;
    }

    .title-card h1 {
        color: #ffffff !important;
        font-size: 44px;
        margin-bottom: 10px;
    }

    .title-card p {
        color: #e5e7eb !important;
        font-size: 18px;
    }

    /* -----------------------------------------------------
       Section cards
    ----------------------------------------------------- */
    .section-card {
        background-color: #3b3f46;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.30);
        margin-bottom: 20px;
    }

    .section-card h3,
    .section-card p {
        color: #ffffff !important;
    }

    /* -----------------------------------------------------
       Result cards
    ----------------------------------------------------- */
    .high-risk-card {
        background: linear-gradient(135deg, #7f1d1d, #dc2626);
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.35);
    }

    .low-risk-card {
        background: linear-gradient(135deg, #064e3b, #059669);
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.35);
    }

    .warning-card {
        background-color: #4b5563;
        padding: 18px;
        border-radius: 14px;
        border-left: 5px solid #f59e0b;
        margin-top: 15px;
    }

    .high-risk-card,
    .high-risk-card *,
    .low-risk-card,
    .low-risk-card *,
    .warning-card,
    .warning-card * {
        color: #ffffff !important;
    }

    /* -----------------------------------------------------
       Buttons
    ----------------------------------------------------- */
    div.stButton > button {
        background-color: #ef4444 !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        padding: 0.7rem 1.5rem !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 18px !important;
        width: 100% !important;
    }

    div.stButton > button:hover {
        background-color: #dc2626 !important;
        color: #ffffff !important;
        border: none !important;
    }

    /* -----------------------------------------------------
       Sidebar
    ----------------------------------------------------- */
    section[data-testid="stSidebar"] {
        background-color: #1f2937 !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span {
        color: #f9fafb !important;
    }

    /* -----------------------------------------------------
       Metrics
    ----------------------------------------------------- */
    div[data-testid="stMetric"] {
        background-color: #3b3f46 !important;
        padding: 15px !important;
        border-radius: 14px !important;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.25) !important;
    }

    div[data-testid="stMetric"] label,
    div[data-testid="stMetric"] div,
    div[data-testid="stMetric"] span {
        color: #ffffff !important;
    }

    /* -----------------------------------------------------
       Expander
    ----------------------------------------------------- */
    div[data-testid="stExpander"] {
        background-color: #3b3f46 !important;
        border-radius: 12px !important;
        border: 1px solid #6b7280 !important;
    }

    div[data-testid="stExpander"] summary,
    div[data-testid="stExpander"] p,
    div[data-testid="stExpander"] span {
        color: #ffffff !important;
    }

    /* -----------------------------------------------------
       Radio buttons
    ----------------------------------------------------- */
    div[data-testid="stRadio"] label,
    div[data-testid="stRadio"] span,
    div[data-testid="stRadio"] p {
        color: #ffffff !important;
    }

    /* -----------------------------------------------------
       Select boxes: closed state
    ----------------------------------------------------- */
    div[data-baseweb="select"] {
        background-color: #f3f4f6 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #f3f4f6 !important;
        color: #111827 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] input {
        color: #111827 !important;
    }

    div[data-baseweb="select"] span {
        color: #111827 !important;
    }

    div[data-baseweb="select"] svg {
        color: #111827 !important;
        fill: #111827 !important;
    }

    /* -----------------------------------------------------
       Select dropdown: opened list
    ----------------------------------------------------- */
    div[data-baseweb="popover"] {
        background-color: transparent !important;
    }

    div[data-baseweb="popover"] div {
        color: #111827 !important;
    }

    ul[role="listbox"] {
        background-color: #f3f4f6 !important;
        color: #111827 !important;
        border-radius: 10px !important;
        border: 1px solid #9ca3af !important;
        padding: 4px !important;
    }

    li[role="option"] {
        background-color: #f3f4f6 !important;
        color: #111827 !important;
        font-weight: 500 !important;
    }

    li[role="option"] div,
    li[role="option"] span {
        color: #111827 !important;
    }

    li[role="option"]:hover {
        background-color: #d1d5db !important;
        color: #111827 !important;
    }

    li[role="option"]:hover div,
    li[role="option"]:hover span {
        color: #111827 !important;
    }

    li[aria-selected="true"] {
        background-color: #9ca3af !important;
        color: #111827 !important;
        font-weight: 700 !important;
    }

    li[aria-selected="true"] div,
    li[aria-selected="true"] span {
        color: #111827 !important;
        font-weight: 700 !important;
    }

    /* -----------------------------------------------------
       Number inputs / text inputs
    ----------------------------------------------------- */
    input,
    textarea {
        color: #111827 !important;
        background-color: #f3f4f6 !important;
    }

    div[data-testid="stNumberInput"] input {
        color: #111827 !important;
        background-color: #f3f4f6 !important;
    }

    div[data-testid="stNumberInput"] button {
        color: #111827 !important;
        background-color: #e5e7eb !important;
    }

    /* -----------------------------------------------------
       Slider
    ----------------------------------------------------- */
    div[data-testid="stSlider"] label,
    div[data-testid="stSlider"] span {
        color: #ffffff !important;
    }

    /* -----------------------------------------------------
       Dataframe
    ----------------------------------------------------- */
    .stDataFrame {
        background-color: #ffffff !important;
        color: #111827 !important;
    }

    .stDataFrame * {
        color: #111827 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("## 🧠 About the App")
    st.write(
        "This application predicts stroke risk using demographic, medical, "
        "and lifestyle information."
    )

    st.markdown("## 📌 Model Note")
    st.write(
        "The model is designed as a screening support tool. "
        "It does not replace medical diagnosis."
    )

    st.markdown("## 👩‍💻 Developed by")
    st.write("**Walaa Salah**")

    st.markdown("## 📊 Important Metrics")
    st.write("- Recall is important for detecting stroke-risk cases.")
    st.write("- Precision is low because the dataset is imbalanced.")
    st.write("- ROC AUC shows the model separates classes well.")

# ---------------------------------------------------------
# Title
# ---------------------------------------------------------
st.markdown(
    """
    <div class="title-card">
        <h1>🧠 Walaa Salah Stroke Prediction App</h1>
        <p>Enter patient information to estimate the probability of stroke risk using a trained machine learning model.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Input layout
# ---------------------------------------------------------
st.markdown(
    """
    <div class="section-card">
        <h3>👤 Patient Information</h3>
        <p>Please fill in the following clinical and lifestyle features.</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.slider("Age", 1, 100, 45)
    hypertension = st.radio(
        "Hypertension",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No",
        horizontal=True
    )
    heart_disease = st.radio(
        "Heart Disease",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No",
        horizontal=True
    )
    ever_married = st.selectbox("Ever Married", ["Yes", "No"])

with col2:
    work_type = st.selectbox(
        "Work Type",
        ["Private", "Self-employed", "Govt_job", "children", "Never_worked"]
    )
    residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
    avg_glucose_level = st.number_input(
        "Average Glucose Level",
        min_value=40.0,
        max_value=300.0,
        value=100.0
    )
    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=70.0,
        value=25.0
    )
    smoking_status = st.selectbox(
        "Smoking Status",
        ["formerly smoked", "never smoked", "smokes"]
    )

# ---------------------------------------------------------
# Feature engineering
# ---------------------------------------------------------
age_group = pd.cut(
    [age],
    bins=[0, 18, 35, 50, 65, 100],
    labels=["Child", "Young Adult", "Adult", "Senior", "Elderly"]
)[0]

bmi_category = pd.cut(
    [bmi],
    bins=[0, 18.5, 24.9, 29.9, 100],
    labels=["Underweight", "Normal", "Overweight", "Obese"]
)[0]

glucose_risk = pd.cut(
    [avg_glucose_level],
    bins=[0, 100, 125, 300],
    labels=["Normal", "Prediabetes", "High"]
)[0]

input_data = pd.DataFrame({
    "gender": [gender],
    "age": [age],
    "hypertension": [hypertension],
    "heart_disease": [heart_disease],
    "ever_married": [ever_married],
    "work_type": [work_type],
    "Residence_type": [residence_type],
    "avg_glucose_level": [avg_glucose_level],
    "bmi": [bmi],
    "smoking_status": [smoking_status],
    "age_group": [age_group],
    "bmi_category": [bmi_category],
    "glucose_risk": [glucose_risk]
})

# ---------------------------------------------------------
# Display engineered features
# ---------------------------------------------------------
with st.expander("View automatically generated health categories"):
    st.write("Age Group:", age_group)
    st.write("BMI Category:", bmi_category)
    st.write("Glucose Risk:", glucose_risk)

# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------
st.markdown("### 🔍 Prediction")

if st.button("Predict Stroke Risk"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    risk_percent = probability * 100

    st.markdown("## Prediction Result")

    metric_col1, metric_col2, metric_col3 = st.columns(3)

    with metric_col1:
        st.metric("Stroke Probability", f"{risk_percent:.1f}%")

    with metric_col2:
        st.metric("Predicted Class", "Stroke Risk" if prediction == 1 else "No Stroke Risk")

    with metric_col3:
        if risk_percent >= 70:
            risk_level = "High"
        elif risk_percent >= 40:
            risk_level = "Moderate"
        else:
            risk_level = "Low"
        st.metric("Risk Level", risk_level)

    st.progress(min(int(risk_percent), 100))

    if prediction == 1:
        st.markdown(
            f"""
            <div class="high-risk-card">
                <h2>⚠️ High Stroke Risk Detected</h2>
                <p>The model predicts that this patient may be at higher risk of stroke.</p>
                <p><b>Predicted probability:</b> {risk_percent:.2f}%</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="warning-card">
                <b>Interpretation:</b> This result means the patient has characteristics similar to stroke-risk cases in the training data.
                In this project, recall is prioritized because detecting possible stroke-risk patients is important in healthcare screening.
                However, this prediction should not be considered a medical diagnosis and should be confirmed by healthcare professionals.
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f"""
            <div class="low-risk-card">
                <h2>✅ Low Stroke Risk Predicted</h2>
                <p>The model predicts that this patient is less likely to have stroke risk based on the provided information.</p>
                <p><b>Predicted probability:</b> {risk_percent:.2f}%</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="warning-card">
                <b>Interpretation:</b> This result means the patient is closer to the non-stroke class based on the model.
                The model performed strongly for identifying non-stroke cases, but no machine learning prediction is perfect.
                Medical evaluation is still required if symptoms or risk factors are present.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Patient Input Summary")
    st.dataframe(input_data)