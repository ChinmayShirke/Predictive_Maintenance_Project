import streamlit as st
import pandas as pd
import pickle
import time

# ---------------------------
# PAGE CONFIGURATION
# ---------------------------
st.set_page_config(page_title="Predictive Maintenance - RUL Prediction", layout="wide")

# ---------------------------
# LOAD TRAINED MODEL
# ---------------------------
@st.cache_resource
def load_model():
    with open("RandomForest (1).pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# ---------------------------
# USER SETTINGS
# ---------------------------
data_file = "D:\Predictive Maintanance\Testing.csv"   # <- Path of your live data file
refresh_rate = 10                # Refresh every 10 seconds (you can change this)
features =  ["run_id", "cycle", "status", "temperature", "vibration", "pressure", "current"]

# ---------------------------
# MAIN APP
# ---------------------------
st.title("⚙️ Predictive Maintenance Dashboard")
st.markdown("### Real-Time Remaining Useful Life (RUL) Prediction using Random Forest")

placeholder = st.empty()

while True:
    with placeholder.container():
        # STEP 1: Read latest data
        try:
            data = pd.read_csv(data_file)
        except FileNotFoundError:
            st.error(f"❌ File '{data_file}' not found. Please check the file path.")
            st.stop()

        if data.empty:
            st.warning("⚠️ No data found in the file.")
            st.stop()

        latest_data = data.iloc[-1:][features]

        # STEP 2: Predict RUL
        predicted_rul = model.predict(latest_data)[0]

        # STEP 3: Display results
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🧾 Latest Machine Data")
            st.dataframe(latest_data)

        with col2:
            st.subheader("📊 Predicted Remaining Useful Life")
            st.metric(label="RUL (in cycles)", value=round(predicted_rul, 2))

            # Optional warning message
            if predicted_rul < 10:
                st.error("⚠️ Warning: Machine nearing end of useful life!")
            elif predicted_rul < 25:
                st.warning("🟠 Maintenance recommended soon.")
            else:
                st.success("✅ Machine condition is healthy.")

        # STEP 4: Auto refresh
        st.markdown(f"⏳ Auto-refreshing every {refresh_rate} seconds...")
        time.sleep(refresh_rate)
        st.rerun()
