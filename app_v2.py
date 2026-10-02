import streamlit as st
import pandas as pd
import plotly.express as px
import joblib


# ---------------------------------------
# Page configuration
# ---------------------------------------

st.set_page_config(
    page_title="ThreatVision AI",
    page_icon="🛡️",
    layout="wide"
)


# ---------------------------------------
# Load multi-feature model
# ---------------------------------------

model = joblib.load(
    "models/multifeature_model.pkl"
)


# ---------------------------------------
# Feature list
# ---------------------------------------

features = [
    "Failed_Logins",
    "Connection_Count",
    "Packet_Size",
    "Login_Hour",
    "Port_Requests"
]


# ---------------------------------------
# Header
# ---------------------------------------

st.title("🛡️ ThreatVision AI")

st.subheader(
    "AI-Powered Network Threat Detection"
)

st.write(
    "Multi-feature machine learning dashboard "
    "for educational cybersecurity research."
)


st.divider()


# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.header("ThreatVision AI")

st.sidebar.info(
    "Upload network activity data containing "
    "the required behavioral features."
)


# ---------------------------------------
# File upload
# ---------------------------------------

uploaded_file = st.file_uploader(
    "Upload Network Activity CSV",
    type=["csv"]
)


# ---------------------------------------
# Process uploaded file
# ---------------------------------------

if uploaded_file is not None:

    df = pd.read_csv(
        uploaded_file
    )


    # -----------------------------------
    # Check required columns
    # -----------------------------------

    required_columns = [
        "IP",
        "Failed_Logins",
        "Connection_Count",
        "Packet_Size",
        "Login_Hour",
        "Port_Requests"
    ]


    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]


    if missing_columns:

        st.error(
            "Missing required columns: "
            + ", ".join(missing_columns)
        )

        st.stop()


    # -----------------------------------
    # AI prediction
    # -----------------------------------

    df["AI_Prediction"] = model.predict(
        df[features]
    )


    df["AI_Result"] = df[
        "AI_Prediction"
    ].map({
        0: "Normal",
        1: "Attack"
    })


    # -----------------------------------
    # Main results
    # -----------------------------------

    st.header("📊 AI Analysis")


    st.dataframe(
        df,
        use_container_width=True
    )


    # -----------------------------------
    # Metrics
    # -----------------------------------

    total_records = len(df)

    attack_count = (
        df["AI_Result"] == "Attack"
    ).sum()

    normal_count = (
        df["AI_Result"] == "Normal"
    ).sum()


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Total Records",
        total_records
    )


    col2.metric(
        "Potential Attacks",
        attack_count
    )


    col3.metric(
        "Normal Activity",
        normal_count
    )


    st.divider()


    # -----------------------------------
    # Threat alerts
    # -----------------------------------

    st.header("🚨 Security Alerts")


    attack_rows = df[
        df["AI_Result"] == "Attack"
    ]


    if len(attack_rows) == 0:

        st.success(
            "No potentially suspicious activity "
            "was identified by the model."
        )

    else:

        for _, row in attack_rows.iterrows():

            st.error(
                f"Potential attack detected from "
                f"{row['IP']} | "
                f"Failed logins: "
                f"{row['Failed_Logins']} | "
                f"Connections: "
                f"{row['Connection_Count']}"
            )


    # -----------------------------------
    # Threat distribution
    # -----------------------------------

    st.header("📈 Threat Distribution")


    result_counts = (
        df["AI_Result"]
        .value_counts()
    )


    fig = px.pie(
        values=result_counts.values,
        names=result_counts.index,
        title="AI Threat Classification"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # -----------------------------------
    # Feature overview
    # -----------------------------------

    st.header(
        "🔍 Network Behavior Analysis"
    )


    feature_chart = px.bar(
        df,
        x="IP",
        y="Failed_Logins",
        title="Failed Login Activity"
    )


    st.plotly_chart(
        feature_chart,
        use_container_width=True
    )


else:

    st.info(
        "Upload a network activity CSV file "
        "to begin AI analysis."
    )


# ---------------------------------------
# Research information
# ---------------------------------------

st.divider()

st.header(
    "🧪 Research Information"
)

st.write(
    "ThreatVision AI uses a Random Forest "
    "classifier trained on multiple synthetic "
    "network-behavior features."
)

st.write(
    "The current dataset is synthetic and "
    "intended for educational experimentation. "
    "Results should not be interpreted as "
    "real-world intrusion-detection performance."
)

st.write(
    "Future research should evaluate the "
    "system using larger, representative "
    "cybersecurity datasets."
)