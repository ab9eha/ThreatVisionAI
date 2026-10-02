import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.set_page_config(
    page_title="ThreatVision AI",
    page_icon="🛡️",
    layout="wide"
)

# Load trained model
model = joblib.load("models/threat_model.pkl")

st.title("🛡️ ThreatVision AI")
st.write("AI-Powered Network Threat Detection System")

uploaded_file = st.file_uploader(
    "Upload a CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    if "Failed_Logins" not in df.columns:
        st.error("CSV must contain a Failed_Logins column")
        st.stop()

    # AI Prediction
    df["AI_Prediction"] = model.predict(
        df[["Failed_Logins"]]
    )

    # Convert numbers to labels
    df["AI_Result"] = df["AI_Prediction"].map({
        0: "Normal",
        1: "Attack"
    })

    st.subheader("📊 AI Analysis Results")
    st.dataframe(df, use_container_width=True)

    st.subheader("🚨 Threat Alerts")

    attack_count = 0

    for _, row in df.iterrows():

        if row["AI_Result"] == "Attack":

            attack_count += 1

            st.error(
                f"🚨 Attack Detected from {row['IP']} "
                f"({row['Failed_Logins']} failed logins)"
            )

    col1, col2 = st.columns(2)

    col1.metric(
        "Total Records",
        len(df)
    )

    col2.metric(
        "Detected Attacks",
        attack_count
    )

    result_counts = df["AI_Result"].value_counts()

    fig = px.pie(
        values=result_counts.values,
        names=result_counts.index,
        title="AI Threat Classification"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info(
        "Upload a CSV file to begin analysis."
    )