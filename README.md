# 🎮 Player Engagement Analysis & Prediction Predictive Modeling 🚀

## Project Overview

This project develops a comprehensive Machine Learning solution for the gaming industry to analyze and predict a player's future engagement level. By classifying players into **Low, Medium, or High Engagement**, the system provides predictive power for two critical business drivers: **maximizing player retention** and upholding **social responsibility** by moderating potential gaming addiction.

The entire workflow, from initial Exploratory Data Analysis (EDA) and model selection to final deployment assets (Streamlit app and Power BI dashboard), is provided within this repository.

---

## 🎯 Dual Business Objective

The predictive model is designed to drive strategic action by transforming raw player data into two actionable segments:

| Priority | Engagement Level Predicted | Actionable Insight | Business Value |
| :--- | :--- | :--- | :--- |
| **Commercial Growth** | **Low Engagement** | Players at high risk of **churn**. | **Retention & CLV:** Trigger personalized offers and content reminders to reduce player attrition. |
| **Social Responsibility** | **High Engagement** | Players exhibiting potential **excessive play** patterns. | **Moderation & Trust:** Automatically activate responsible gaming features (e.g., break reminders, time limits) to ensure player welfare. |

---

## 💻 Technical Stack & Deliverables

### **Technology Stack**

| Category | Tools & Libraries | Files |
| :--- | :--- | :--- |
| **Analysis & Modeling** | Python, Pandas, NumPy, Scikit-learn, XGBoost, LightGBM | `player-engagement-analysis-prediction.ipynb` |
| **Reporting** | Power BI | `Dashboard.pbix` |
| **Deployment** | Streamlit | `app.py` |
| **Model Pipeline** | `joblib` | `player_engagement_prediction_pipeline.joblib` |

### **Classification Algorithms Compared**

The project is a **Multi-Class Classification** task. The analysis compares several high-performance ensemble models, with **XGBoost** and **LightGBM** typically emerging as top performers.

* Decision Tree Classifier
* Random Forest Classifier
* Gradient Boosting Classifier
* AdaBoost Classifier
* **XGBoost Classifier**
* **LGBM Classifier**

---

## 📂 Repository Structure

| File/Folder | Description |
| :--- | :--- |
| `data.csv` / `online_gaming_behavior_dataset.csv` | The raw player behavior datasets. |
| `player-engagement-analysis-prediction.ipynb` | **Master Jupyter Notebook** detailing all steps: EDA, Feature Engineering, Model Training, Comparative Evaluation, and Hyperparameter Tuning. |
| `player_engagement_prediction_pipeline.joblib` | The **final saved ML pipeline** (preprocessor + best model) used for real-time inference. |
| `app.py` | Python script for the **Streamlit web application**, providing a user interface for live predictions. |
| `Dashboard.pbix` | **Power BI Dashboard source file** for interactive visualization of player segmentation and model metrics. |

---

