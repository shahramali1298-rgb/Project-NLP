import streamlit as st
import numpy as np
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

st.set_page_config(page_title="AI Weather Dashboard", layout="centered")

st.title("🌦️ AI Weather Dashboard (Streamlit + HuggingFace)")
st.write("AI-based weather simulation system (No API)")

city = st.text_input("Enter City Name:")

def generate_weather_data(city):
    np.random.seed(len(city))
    temp = np.random.randint(10, 45)
    humidity = np.random.randint(20, 90)
    wind = np.random.randint(5, 40)
    condition = np.random.choice(["Sunny", "Cloudy", "Rainy", "Stormy"])
    return temp, humidity, wind, condition

def ai_weather_analysis(condition):
    result = classifier(condition)[0]
    label = result["label"]
    score = result["score"]

    mood = "Pleasant Weather 😊" if label == "POSITIVE" else "Unpleasant Weather ⚠️"
    return mood, score

if st.button("Get Weather Forecast"):
    if not city:
        st.warning("Enter city name")
    else:
        temp, humidity, wind, condition = generate_weather_data(city)

        st.subheader(f"📍 Weather in {city}")
        st.metric("Temperature", f"{temp} °C")
        st.metric("Humidity", f"{humidity}%")
        st.metric("Wind Speed", f"{wind} km/h")
        st.write("Condition:", condition)

        mood, confidence = ai_weather_analysis(condition)

        st.subheader("🤖 AI Insight")
        st.write(mood)
        st.write("Confidence:", round(confidence, 2))
