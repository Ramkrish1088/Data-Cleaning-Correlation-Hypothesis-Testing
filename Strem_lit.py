import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# ------------------- Page Config -------------------
st.set_page_config(
    page_title="❤️ Heart Attack Prediction App",
    page_icon="🫀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ------------------- Load Dataset -------------------
df_heart = pd.read_csv(r'D:\DS\My_work\Heart_attack\Data\heart_attack_prediction_dataset.csv')

# Define binary Yes/No columns
binary_cols = [
    "Diabetes",
    "Family History",
    "Smoking",
    "Obesity",
    "Alcohol Consumption",
    "Previous Heart Problems",
    "Medication Use"
]

# Encode categorical columns (except binary yes/no that we handle manually)
label_encoders = {}
for col in df_heart.columns:
    if df_heart[col].dtype == "object" and col not in binary_cols:   # categorical
        le = LabelEncoder()
        df_heart[col] = le.fit_transform(df_heart[col])
        label_encoders[col] = le

# Split into features and target
X = df_heart.drop(columns=["Heart Attack Risk"])   # 👈 label column
y = df_heart["Heart Attack Risk"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model + encoders
joblib.dump((model, label_encoders), "rf_model.pkl")

# Load model
model, label_encoders = joblib.load("rf_model.pkl")

# ------------------- UI -------------------
st.title("❤️ Heart Attack Prediction App")
st.markdown("<h5 style='text-align:center; color:gray;'>Fill in the details below to check your heart attack risk</h5>", unsafe_allow_html=True)

# 👉 Patient Name / ID (manual input, not dropdown)
patient_name = st.text_input("🆔 Enter Patient Name ")

# Collect inputs dynamically
user_input = {}
st.subheader("🔹 Enter Patient Details")

for col in X.columns:
    if col in binary_cols:  
        val = st.radio(f"{col}?", options=["No", "Yes"])
        user_input[col] = 1 if val == "Yes" else 0
    elif col in label_encoders:  
        val = st.selectbox(f"Select {col}", options=label_encoders[col].classes_)
        user_input[col] = label_encoders[col].transform([val])[0]
    else:  
        val = st.number_input(f"Enter {col}", value=float(df_heart[col].mean()))
        user_input[col] = val

# Convert input to DataFrame
input_df = pd.DataFrame([user_input])

# Custom CSS for Predict button
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #28a745, #218838);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 12px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #218838, #1e7e34);
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Prediction Button
if st.button("🔮 Predict"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    patient_info = f"<b>👤 Patient:</b> {patient_name if patient_name else 'Not Provided'}<br>"

    if prediction == 1:  # High Risk
        st.markdown(
            f"<div style='background-color:#ffccd5; padding:15px; border-radius:10px; text-align:center; color:#c1121f; font-size:18px; font-weight:bold;'>"
            f"{patient_info}"
            f"⚠️ High Risk of Heart Attack <br> Probability: {max(proba)*100:.2f}%"
            f"</div>",
            unsafe_allow_html=True
        )
    else:  # Low Risk
        st.markdown(
            f"<div style='background-color:#d8f3dc; padding:15px; border-radius:10px; text-align:center; color:#1b4332; font-size:18px; font-weight:bold;'>"
            f"{patient_info}"
            f"✅ Low Risk of Heart Attack <br> Probability: {max(proba)*100:.2f}%"
            f"</div>",
            unsafe_allow_html=True
        )