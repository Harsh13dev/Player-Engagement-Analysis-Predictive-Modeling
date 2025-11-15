import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
import sys

MODEL_FILE = 'player_engagement_prediction_pipeline.joblib'

FEATURE_ORDER = [
    'Age', 'Gender', 'Location', 'GameGenre', 'PlayTimeHours',
    'InGamePurchases', 'GameDifficulty', 'SessionsPerWeek',
    'AvgSessionDurationMinutes', 'PlayerLevel', 'AchievementsUnlocked'
]

# --- Streamlit UI ---
st.set_page_config(page_title="Player Engagement Predictor", layout="wide")
st.title("🎮 Online Player Engagement Level Predictor")
st.markdown("---")

st.markdown("""
<style>
.stApp {
    background-image: url('https://images.pexels.com/photos/1365795/pexels-photo-1365795.jpeg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)

# --- Model Loading ---
@st.cache_resource
def load_model():
    """Loads the saved ML pipeline."""
    if not os.path.exists(MODEL_FILE):
        st.error(f"Error: Model file '{MODEL_FILE}' not found.")
        st.warning("Please ensure you have saved your trained pipeline using joblib.dump() "
                   "in the same directory as this Streamlit script.")
        sys.exit()

    try:
        pipeline = joblib.load(MODEL_FILE)
        return pipeline
    except Exception as e:
        st.error(f"Error loading model pipeline: {e}")
        st.stop()


# Load the model once when the app starts
model_pipeline = load_model()


# --- Prediction Function ---
def predict_engagement(input_data):
    """Takes raw input data (dict) and predicts EngagementLevel."""

    # Convert input data dictionary into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Reorder columns to match the training data order (CRITICAL)
    input_df = input_df[FEATURE_ORDER]

    # Predict using the full pipeline (handles preprocessing and classification)
    prediction = model_pipeline.predict(input_df)[0]

    return prediction




# --- Input Fields ---
with st.container():
    st.subheader("Player Profile & Behavior Metrics")
    col1, col2, col3 = st.columns(3)

    # Column 1: Demographics
    with col1:
        age = st.slider('Age', min_value=16, max_value=50, value=30)
        gender = st.selectbox('Gender', ['Male', 'Female'])
        location = st.selectbox('Location', ['USA', 'Europe', 'Asia' ,'Other'])

    # Column 2: Game Metrics
    with col2:
        game_genre = st.selectbox('Game Genre', ['Strategy', 'Sports', 'Action', 'RPG', 'Simulation'])
        difficulty = st.selectbox('Game Difficulty', ['Easy', 'Medium', 'Hard'])
        purchases = st.radio('In-Game Purchases', ['Yes', 'No'],
                             help="Select 'Yes' if the player makes in-game purchases.")

    # Column 3: Play Stats (Numerical)
    with col3:
        play_time = st.number_input('PlayTimeHours', min_value=0.0, max_value=25.0, value=15.0)
        sessions_week = st.number_input('SessionsPerWeek', min_value=1, max_value=20, value=5)
        avg_session = st.number_input('AvgSessionDurationMinutes', min_value=10, max_value=300, value=90)
        player_level = st.number_input('PlayerLevel', min_value=1, max_value=100, value=50)
        achievements = st.number_input('AchievementsUnlocked', min_value=0, max_value=100, value=25)

st.markdown("---")

# --- Prediction Logic ---
if st.button('Predict Player Engagement Level', use_container_width=True, type="primary"):
    # Create the raw input dictionary from Streamlit widgets
    player_input = {
        'Age': age,
        'Gender': gender,
        'Location': location,
        'GameGenre': game_genre,
        'PlayTimeHours': play_time,
        'InGamePurchases': purchases,
        'GameDifficulty': difficulty,
        'SessionsPerWeek': sessions_week,
        'AvgSessionDurationMinutes': avg_session,
        'PlayerLevel': player_level,
        'AchievementsUnlocked': achievements
    }

    # st.write(player_input)
    # Perform prediction
    prediction = predict_engagement(player_input)

    if prediction == 0:
        prediction_label = "Low"
    elif prediction == 1:
        prediction_label = "Medium"
    elif prediction == 2:
        prediction_label = "High"

    st.success(f"Prediction Complete!")
    st.subheader(f"Predicted Engagement Level: **{prediction_label}**")
