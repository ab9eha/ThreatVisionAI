# ThreatVision AI: Machine Learning for Network Threat Detection

## Abstract

ThreatVision AI is an educational cybersecurity research project investigating the use of machine learning to classify potentially suspicious network activity. The project implements a complete machine-learning workflow, including data preparation, model training, evaluation, model comparison, feature-importance analysis, and interactive visualization through a Streamlit dashboard.

The prototype evaluates Decision Tree, Random Forest, and Logistic Regression approaches and later extends the system to a multi-feature Random Forest model using network-behavior indicators such as failed login attempts, connection counts, packet size, login hour, and port requests.

The current experiments use a small synthetic dataset. Therefore, the reported results demonstrate the machine-learning workflow rather than real-world intrusion-detection performance.

## 1. Introduction

Cybersecurity systems increasingly use automated analysis to identify potentially suspicious activity. Traditional rule-based approaches can be useful for known patterns, but machine-learning methods provide another approach for identifying relationships among multiple behavioral features.

ThreatVision AI was developed to explore how supervised machine learning can be applied to a simplified network-threat classification problem.

The project focuses on the distinction between two classes:

* Normal activity
* Potentially suspicious activity

## 2. Problem Statement

Manual examination of large quantities of network activity can be difficult and time-consuming.

This project investigates whether machine-learning models can use network-behavior features to classify activity into normal or potentially suspicious categories.

## 3. Research Objectives

The main objectives are:

1. Develop a working machine-learning cybersecurity prototype.
2. Train supervised classification models.
3. Compare multiple machine-learning algorithms.
4. Evaluate models using standard classification metrics.
5. Investigate feature importance in a Random Forest model.
6. Develop an interactive cybersecurity dashboard.
7. Document the limitations of using synthetic training data.

## 4. Methodology

The project follows this workflow:

```text
Dataset
   ↓
Data Preparation
   ↓
Train/Test Split
   ↓
Machine-Learning Models
   ↓
Predictions
   ↓
Performance Evaluation
   ↓
Feature Analysis
   ↓
Interactive Dashboard
```

A 70/30 train-test split was used with a fixed random state to make the experiment reproducible.

## 5. Dataset

The project initially used a small synthetic dataset based on failed-login activity.

A second dataset was developed containing multiple behavioral features:

* Failed_Logins
* Connection_Count
* Packet_Size
* Login_Hour
* Port_Requests

The target variable was:

* 0 = Normal
* 1 = Attack

The dataset is synthetic and was created for educational experimentation.

## 6. Machine-Learning Models

Three classification algorithms were investigated:

### Decision Tree

A Decision Tree was used as an interpretable baseline classifier.

### Random Forest

Random Forest was investigated as an ensemble-learning approach using multiple decision trees.

### Logistic Regression

Logistic Regression was included as a linear classification baseline.

## 7. Evaluation Metrics

The models were evaluated using:

### Accuracy

The proportion of predictions that were correct.

### Precision

The proportion of predicted attack cases that were actually attack cases.

### Recall

The proportion of actual attack cases that were correctly identified.

### F1 Score

The harmonic mean of precision and recall.

These metrics provide different perspectives on classification performance.

## 8. Experimental Results

The project automatically generates model-comparison results in:

```text
results/model_comparison.csv
```

A visualization is generated at:

```text
results/model_comparison.png
```

Confusion matrices are also generated for the investigated models.

Because the dataset is small and synthetic, these results should not be interpreted as evidence of production-level cybersecurity detection performance.

## 9. Explainable AI

The multi-feature Random Forest model provides feature-importance measurements.

The project generates:

```text
results/feature_importance.csv
results/feature_importance.png
```

These outputs help investigate which input features contribute most strongly to the trained model's classification process.

Feature importance should be interpreted as a property of this particular trained model and dataset. It does not establish that a feature is universally predictive of cyber attacks.

## 10. Interactive Dashboard

ThreatVision AI provides a Streamlit dashboard that allows users to upload compatible CSV network-activity data.

The dashboard provides:

* AI-based classification
* Threat counts
* Security alerts
* Threat-distribution visualization
* Network-behavior visualization
* Research information

The application is intended for educational and defensive cybersecurity research.

## 11. Limitations

Several limitations should be considered.

### Synthetic Data

The current dataset is synthetic and substantially smaller than datasets used in real intrusion-detection research.

### Limited Features

The prototype uses only a small number of network-behavior features.

### Binary Classification

The current model distinguishes between normal activity and a general attack category rather than identifying specific attack families.

### Generalization

Performance measured on this dataset cannot be assumed to generalize to real-world network environments.

### Dataset Size

The small sample size limits the strength of statistical conclusions that can be drawn from the experiments.

## 12. Ethical Considerations

ThreatVision AI is intended for defensive cybersecurity education and research.

Users should only analyze network information that they own or are explicitly authorized to examine.

The project should not be used to monitor, attack, or interfere with systems without authorization.

## 13. Future Research

Future versions could investigate:

* Larger public intrusion-detection datasets
* Additional network-traffic features
* Multiclass attack classification
* Cross-validation
* Hyperparameter optimization
* Additional ensemble models
* Explainable-AI methods such as SHAP
* Class imbalance handling
* Robustness testing
* Detection of previously unseen activity
* Testing across multiple datasets

## 14. Conclusion

ThreatVision AI demonstrates a complete introductory machine-learning workflow for a cybersecurity classification problem.

The project combines data preparation, supervised learning, model comparison, evaluation, feature analysis, and interactive visualization.

The current implementation should be considered an educational research prototype rather than a production intrusion-detection system. Its primary value is demonstrating the development and evaluation process while identifying the additional work required for meaningful real-world validation.
