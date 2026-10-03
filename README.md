# ThreatVision AI 🛡️

## AI-Powered Network Threat Detection

ThreatVision AI is a machine-learning-based cybersecurity research project that explores how network behavior can be analyzed to identify potentially suspicious activity.

The project combines **Python, machine learning, cybersecurity, data analysis, explainable AI, and an interactive Streamlit dashboard**.

> **Research note:** The current system uses a synthetic dataset for educational experimentation. Its results should not be interpreted as real-world intrusion-detection performance.

---

## 🚀 Live Demo

**Streamlit App:**
https://threatvisionai-tbjsuzvrwlktwy2pcknsfj.streamlit.app/

**GitHub Repository:**
https://github.com/ab9eha/ThreatVisionAI.git

---

## 🎯 Research Problem

Traditional security monitoring can generate large amounts of network activity that is difficult to analyze manually.

ThreatVision AI explores whether machine-learning techniques can use behavioral network features to classify activity as potentially **Normal** or **Attack**.

The project focuses on developing a reproducible experimental workflow rather than claiming production-ready intrusion detection.

---

## 🔬 Research Objectives

The main objectives of ThreatVision AI are to:

* Develop a machine-learning model for network threat classification.
* Analyze multiple network behavior features.
* Compare different machine-learning algorithms.
* Evaluate models using standard classification metrics.
* Investigate which features contribute most to model predictions.
* Build an interactive cybersecurity dashboard.
* Deploy the experimental system as a web application.
* Identify limitations and directions for future research.

---

## 🤖 Machine Learning Approach

The current multi-feature system uses a **Random Forest Classifier**.

The model analyzes the following network behavior features:

| Feature            | Description                         |
| ------------------ | ----------------------------------- |
| `Failed_Logins`    | Number of failed login attempts     |
| `Connection_Count` | Number of network connections       |
| `Packet_Size`      | Observed packet-size value          |
| `Login_Hour`       | Hour associated with login activity |
| `Port_Requests`    | Number of requested ports           |

The target variable is:

```text
0 = Normal
1 = Attack
```

---

## 🧪 Dataset

The current experimental dataset is **synthetically generated** for educational and research purposes.

It contains examples of normal and potentially suspicious network behavior.

The project deliberately identifies this limitation because a model trained on a small synthetic dataset cannot be assumed to generalize to real-world network environments.

Future versions should be evaluated using larger and representative cybersecurity datasets.

---

## 📊 Model Comparison

ThreatVision AI experiments with multiple machine-learning algorithms:

* Decision Tree
* Random Forest
* Logistic Regression

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

The project also generates:

* Model comparison results
* Confusion matrices
* Feature-importance analysis

These experiments provide a reproducible framework for comparing classification approaches.

---

## 🔍 Explainable AI

ThreatVision AI includes feature-importance analysis for the Random Forest model.

This helps investigate which network behavior features contribute most strongly to the model's classification process.

The feature-importance results are generated using:

```text
feature_importance.py
```

Output files are stored in:

```text
results/
```

This component is included to make the machine-learning workflow more interpretable rather than treating the model as a complete black box.

---

## 🖥️ Interactive Dashboard

The Streamlit dashboard allows users to upload network activity in CSV format and receive AI-generated classifications.

The dashboard provides:

* 📂 CSV file upload
* 🤖 AI-based threat classification
* 📊 Classification results
* 🚨 Security alerts
* 📈 Threat distribution
* 📡 Network behavior visualization
* 🔍 Feature-importance visualization
* 📏 Model evaluation metrics
* 🧪 Research information and limitations

---

## 🔄 System Workflow

```text
Network Activity
       ↓
CSV Dataset
       ↓
Feature Validation
       ↓
Feature Processing
       ↓
Random Forest Model
       ↓
Threat Classification
       ↓
Normal / Potential Attack
       ↓
Security Alerts
       ↓
Interactive Dashboard
```

---

## 📁 Project Structure

```text
ThreatVisionAI/
│
├── data/
│   ├── training_data.csv
│   └── training_data_v2.csv
│
├── models/
│   └── Local trained model files
│
├── results/
│   ├── model_comparison.csv
│   ├── model_comparison.png
│   ├── feature_importance.csv
│   ├── feature_importance.png
│   └── confusion matrices
│
├── app.py
├── app_v2.py
├── app_v3.py
│
├── train_model.py
├── train_multifeature_model.py
├── evaluate_model.py
├── compare_models.py
├── generate_results.py
├── feature_importance.py
│
├── sample_logs.csv
├── sample_logs_v2.csv
│
├── research_report.md
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ab9eha/ThreatVisionAI.git
```

Move into the project directory:

```bash
cd ThreatVisionAI
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

The deployment-ready
