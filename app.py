import streamlit as st
import pickle

# Load the trained model
with open("logistic_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🧠 Unsupervised Credit Risk Grouping")

# === Input fields with readable options ===

age = st.number_input("Age", min_value=18, max_value=75, step=1)

sex = st.selectbox("Sex", ["female", "male"])
sex_encoded = 0 if sex == "female" else 1

job = st.selectbox("Job", [
    "0 - Unskilled and non-resident",
    "1 - Unskilled and resident",
    "2 - Skilled",
    "3 - Highly skilled"
])
job_encoded = int(job.split(" - ")[0])

housing = st.selectbox("Housing", ["own", "rent", "free"])
housing_map = {"own": 0, "rent": 1, "free": 2}
housing_encoded = housing_map[housing]

saving = st.selectbox("Saving Account", ["little", "moderate", "quite rich", "rich"])
saving_map = {"little": 0, "moderate": 1, "quite rich": 2, "rich": 3}
saving_encoded = saving_map[saving]

checking = st.number_input("Checking Account Balance (DM)", min_value=0.0, step=10.0)

credit = st.number_input("Credit Amount (DM)", min_value=0.0, step=100.0)

duration = st.slider("Loan Duration (months)", 6, 72, step=1)

purpose = st.selectbox("Purpose", [
    "car", "furniture/equipment", "radio/TV", "domestic appliances", "repairs",
    "education", "business", "vacation/others"
])
purpose_map = {
    "car": 0,
    "furniture/equipment": 1,
    "radio/TV": 2,
    "domestic appliances": 3,
    "repairs": 4,
    "education": 5,
    "business": 6,
    "vacation/others": 7
}
purpose_encoded = purpose_map[purpose]

# === Feature list in same order as training ===
features = [[
    age, sex_encoded, job_encoded, housing_encoded, saving_encoded,
    checking, credit, duration, purpose_encoded
]]
risk_map = {
    0: "Good Credit Risk ✅",
    1: "Bad Credit Risk ⚠️"
}

if st.button("🔍 Predict Credit Group"):
    prediction = model.predict(features)
    predicted_cluster = prediction[0]

    if predicted_cluster == 0:
        st.success(f"🔎 Predicted Credit Risk: **{risk_map[predicted_cluster]}**")
    else:
        st.error(f"🔎 Predicted Credit Risk: **{risk_map[predicted_cluster]}**")


