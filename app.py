import streamlit as st
import tensorflow as tf
import numpy as np
from transformers import pipeline

# ---------------------------
# AI Model (HuggingFace - FREE)
# Weather text understanding model (no API key required)
# ---------------------------
classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

st.set_page_config(page_title="AI Weather Dashboard", layout="centered")

st.title("🌦️ AI Weather Dashboard (Streamlit + TensorFlow + HuggingFace)")
st.write("Enter a city and get AI-based weather insights (simulated + ML analysis)")

# ---------------------------
# INPUT
# ---------------------------
city = st.text_input("Enter City Name:")

# Fake weather generator (no API used)
def generate_weather_data(city):
    np.random.seed(len(city))
    temp = np.random.randint(10, 45)
    humidity = np.random.randint(20, 90)
    wind = np.random.randint(5, 40)
    condition = np.random.choice(["Sunny", "Cloudy", "Rainy", "Stormy"])
    return temp, humidity, wind, condition

# ---------------------------
# AI ANALYSIS FUNCTION
# ---------------------------
def ai_weather_analysis(condition):
    result = classifier(condition)[0]
    label = result["label"]
    score = result["score"]
    
    if label == "POSITIVE":
        mood = "Pleasant Weather 😊"
    else:
        mood = "Unpleasant Weather ⚠️"
    
    return mood, score

# ---------------------------
# MAIN APP
# ---------------------------
if st.button("Get Weather Forecast"):
    if city == "":
        st.warning("Please enter a city name")
    else:
        temp, humidity, wind, condition = generate_weather_data(city)

        mood, confidence = ai_weather_analysis(condition)

        st.subheader(f"📍 Weather in {city}")

        st.metric("Temperature 🌡️", f"{temp} °C")
        st.metric("Humidity 💧", f"{humidity}%")
        st.metric("Wind Speed 🌬️", f"{wind} km/h")
        st.write(f"Condition: **{condition}**")

        st.subheader("🤖 AI Weather Insight")
        st.write(f"Mood Prediction: **{mood}**")
        st.write(f"Confidence Score: {round(confidence, 2)}")

        # TensorFlow simple model simulation
        data = np.array([temp, humidity, wind], dtype=np.float32)
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(3, activation='relu'),
            tf.keras.layers.Dense(1)
        ])

        model.compile(optimizer='adam', loss='mse')

        prediction = model(tf.expand_dims(data, axis=0)).numpy()[0][0]

        st.subheader("📊 AI Risk Score (TensorFlow)")
        st.write(round(float(prediction), 2))
