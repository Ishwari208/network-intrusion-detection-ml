# 🛡 Network Intrusion Detection using Machine Learning

## 📌 Overview
This project implements a supervised machine learning pipeline to classify network traffic as either **Normal** or **Malicious (Attack)** using the NSL-KDD dataset.

The goal is to develop an intelligent intrusion detection system capable of identifying malicious network activity with high accuracy and minimal false negatives.

---

## 🎯 Problem Statement

Traditional rule-based intrusion detection systems struggle to detect evolving and unknown attacks.  
This project applies machine learning techniques to automatically learn patterns in historical network traffic data and classify new traffic as either normal or malicious.

---

## 📂 Dataset

- **Dataset Used:** NSL-KDD
- **Total Records:** 125,973
- **Features:** 41 network traffic attributes
- **Target:** Attack Type

For simplicity and model stability, the problem was converted into **Binary Classification**:
- `0 → Normal Traffic`
- `1 → Malicious Attack`

---

## 🧠 Machine Learning Approach

### 1️⃣ Data Preprocessing
- Loaded NSL-KDD dataset
- Converted multi-class labels into binary classification
- Removed unnecessary columns
- Applied One-Hot Encoding for categorical features
- Split dataset into 80% training and 20% testing sets

---

### 2️⃣ Models Implemented

#### 🔹 Logistic Regression (Baseline Model)
- Linear classification model
- Used as an interpretable baseline
- Achieved ~95% accuracy

#### 🔹 Random Forest (Ensemble Model)
- Ensemble of multiple decision trees
- Captures complex non-linear patterns
- Achieved ~99.89% accuracy
- Significantly reduced false negatives

---

## 📊 Model Evaluation Metrics

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Feature Importance Analysis

### ⚠ Important Insight
In intrusion detection systems, **minimizing false negatives is critical**, as undetected attacks can compromise system security.

The Random Forest model drastically reduced false negatives compared to Logistic Regression.

---

## 🔍 Confusion Matrix Analysis

The Random Forest model demonstrated:

- Very high true positives
- Very low false positives
- Very low false negatives

This indicates strong classification reliability for detecting malicious traffic.

---

## 📈 Feature Importance Analysis

Random Forest provides feature importance scores, highlighting which network traffic attributes contribute most to attack detection.

This improves interpretability and provides insights into critical intrusion indicators.

---

## 🏆 Final Results

| Model                | Accuracy |
|----------------------|----------|
| Logistic Regression | ~95%     |
| Random Forest        | ~99.89%  |

Random Forest was selected as the final preferred model due to its superior performance and reduced false negatives.

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Seaborn
- Matplotlib
- Google Colab

---

## 🚀 Key Learnings

- Supervised learning for cybersecurity applications
- Binary classification modeling
- Model comparison techniques
- Confusion matrix interpretation
- Importance of recall in intrusion detection
- Ensemble learning advantages

---

## 📌 Future Improvements (Optional Enhancements)

- Cross-validation for robust validation
- Hyperparameter tuning
- ROC curve visualization
- Deployment using Flask (optional)

---

## 👩‍💻 Author

Ishwari Dahale  
Final Year Engineering Project  
Machine Learning & Data Analytics Focus
