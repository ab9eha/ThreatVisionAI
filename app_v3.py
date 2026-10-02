import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="ThreatVision AI",
    page_icon="🛡️",
    layout="wide"
)


# ---------------------------------------------------------
# LOAD TRAINING DATA
# ---------------------------------------------------------

@st.cache_resource
def train_model():

    data = pd.read_csv(
        "data/training_data_v2.csv"
    )

    features = [
        "Failed_Logins",
        "Connection_Count",
        "Packet_Size",
        "Login_Hour",
        "Port_Requests"
    ]

    X = data[features]
    y = data["Attack"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    metrics = {
        "Accuracy": accuracy_score(
            y_test,
            predictions
        ),
        "Precision": precision_score(
            y_test,
            predictions,
            zero_division=0
        ),
        "Recall": recall_score(
            y_test,
            predictions,
            zero_division=0
        ),
        "F1 Score": f1_score(
            y_test,
            predictions,
            zero_division=0
        )
    }

    importance_df = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    return model, metrics, importance_df


# Train model
model, metrics, importance_df = train_model()


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🛡️ ThreatVision AI")

st.subheader(
    "AI-Powered Network Threat Detection"
)

st.write(
    "A machine-learning cybersecurity research "
    "dashboard for detecting potentially suspicious "
    "network activity."
)

st.divider()


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("🛡️ ThreatVision AI")

st.sidebar.info(
    "Upload a CSV file containing network "
    "behavioral features for AI analysis."
)

st.sidebar.markdown(
    """
### Required columns

- IP
- Failed_Logins
- Connection_Count
- Packet_Size
- Login_Hour
- Port_Requests
"""
)


# ---------------------------------------------------------
# MODEL PERFORMANCE
# ---------------------------------------------------------

st.header("🤖 Model Performance")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Accuracy",
    f"{metrics['Accuracy']:.2f}"
)

col2.metric(
    "Precision",
    f"{metrics['Precision']:.2f}"
)

col3.metric(
    "Recall",
    f"{metrics['Recall']:.2f}"
)

col4.metric(
    "F1 Score",
    f"{metrics['F1 Score']:.2f}"
)

st.caption(
    "These metrics come from a hold-out test split "
    "of the current synthetic research dataset."
)


# ---------------------------------------------------------
# FEATURE IMPORTANCE
# ---------------------------------------------------------

st.header(
    "🔍 Explainable AI — Feature Importance"
)

st.write(
    "The chart shows which network behavior features "
    "contributed most to the Random Forest model's "
    "classification decisions."
)

importance_chart = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Random Forest Feature Importance"
)

importance_chart.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(
    importance_chart,
    use_container_width=True
)


# ---------------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------------

st.divider()

st.header("📂 Network Activity Analysis")

uploaded_file = st.file_uploader(
    "Upload Network Activity CSV",
    type=["csv"]
)


if uploaded_file is not None:

    df = pd.read_csv(
        uploaded_file
    )

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


    # -----------------------------------------------------
    # AI PREDICTIONS
    # -----------------------------------------------------

    df["AI_Prediction"] = model.predict(
        df[
            [
                "Failed_Logins",
                "Connection_Count",
                "Packet_Size",
                "Login_Hour",
                "Port_Requests"
            ]
        ]
    )

    df["AI_Result"] = df[
        "AI_Prediction"
    ].map({
        0: "Normal",
        1: "Attack"
    })


    # -----------------------------------------------------
    # SUMMARY METRICS
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # RESULTS TABLE
    # -----------------------------------------------------

    st.header(
        "📊 AI Classification Results"
    )

    st.dataframe(
        df,
        use_container_width=True
    )


    # -----------------------------------------------------
    # SECURITY ALERTS
    # -----------------------------------------------------

    st.header(
        "🚨 Security Alerts"
    )

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
                f"{row['Connection_Count']} | "
                f"Port requests: "
                f"{row['Port_Requests']}"
            )


    # -----------------------------------------------------
    # THREAT DISTRIBUTION
    # -----------------------------------------------------

    st.header(
        "📈 Threat Distribution"
    )

    result_counts = (
        df["AI_Result"]
        .value_counts()
    )

    threat_chart = px.pie(
        values=result_counts.values,
        names=result_counts.index,
        title="AI Threat Classification"
    )

    st.plotly_chart(
        threat_chart,
        use_container_width=True
    )


    # -----------------------------------------------------
    # NETWORK BEHAVIOR
    # -----------------------------------------------------

    st.header(
        "📡 Network Behavior Analysis"
    )

    failed_login_chart = px.bar(
        df,
        x="IP",
        y="Failed_Logins",
        title="Failed Login Activity"
    )

    st.plotly_chart(
        failed_login_chart,
        use_container_width=True
    )


    connection_chart = px.bar(
        df,
        x="IP",
        y="Connection_Count",
        title="Connection Activity"
    )

    st.plotly_chart(
        connection_chart,
        use_container_width=True
    )


else:

    st.info(
        "Upload a network activity CSV file "
        "to begin AI analysis."
    )


# ---------------------------------------------------------
# RESEARCH INFORMATION
# ---------------------------------------------------------

st.divider()

st.header(
    "🧪 Research Information"
)

st.write(
    """
ThreatVision AI uses a Random Forest machine-learning
classifier trained using multiple synthetic network
behavior features.
"""
)

st.write(
    """
The current research dataset is synthetic and
intended for educational experimentation.
The reported metrics should not be interpreted
as real-world intrusion-detection performance.
"""
)

st.write(
    """
Future research can evaluate ThreatVision AI using
larger public cybersecurity datasets, additional
network features, cross-validation, hyperparameter
optimization, multiclass attack detection, and
explainable-AI techniques.
"""
)

st.caption(
    "ThreatVision AI — Educational Cybersecurity "
    "Research Project"
)