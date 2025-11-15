# 🎮 Player Engagement Analysis & Prediction 🚀

## Project Overview

This project develops a robust Machine Learning solution to analyze and predict a player's engagement level in online gaming. By classifying players into **Low, Medium, or High Engagement**, the model provides a dual benefit: driving commercial growth through targeted retention and fulfilling social responsibility by moderating excessive play.

---

## 🎯 The Core Problem

**The gaming industry lacks a predictive mechanism to effectively manage the player lifecycle.** We aim to close this gap by creating an ML system that can:

1.  **Reduce Churn:** Proactively identify players predicted to be at **Low Engagement** before they leave the game.
2.  **Ensure Player Well-being:** Automatically flag players predicted to be at excessive **High Engagement** to trigger responsible gaming interventions.

## 🛠️ Project Components & Deliverables

This project includes development across the entire data science lifecycle:

| Component | Description | Output/Usage |
| :--- | :--- | :--- |
| **Data Source** | Kaggle Dataset: Predict Online Gaming Behavior | `data.csv` |
| **Analysis & Modeling** | Data cleaning, EDA, Feature Engineering, and Model Training/Evaluation. | `player-engagement-analysis-prediction.ipynb` |
| **Model Stack** | Comprehensive comparison of powerful ensemble models. | XGBoost, LGBM, Random Forest, Gradient Boosting, AdaBoost, Decision Tree |
| **Reporting** | Interactive visualization of key metrics, engagement trends, and model performance. | Power BI Dashboard (External) |
| **Deployment Interface** | A simple web application for real-time prediction using the final model. | Streamlit App (External) |

## 🧪 Modeling & Algorithm Details

The solution focuses on **Multi-Class Classification**, predicting one of three categories (`Low`, `Medium`, `High`).

| Model | Status | Key Advantage |
| :--- | :--- | :--- |
| **XGBoost Classifier** | Implemented & Tuned | Highly optimized, often the best performance for tabular data. |
| **LGBM Classifier** | Implemented & Tuned | Fast training speed, excellent performance on large datasets. |
| **Random Forest** | Implemented | Strong baseline, excellent for handling non-linear data and feature importance. |
| **Gradient Boosting** | Implemented | Robust sequential ensemble learner. |
| **AdaBoost** | Implemented | Simple boosting method, good for feature selection. |
| **Decision Tree** | Implemented | Simplest model, provides a quick performance benchmark. |


