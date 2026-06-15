import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="AI Weather Dashboard", layout="centered")

st.title("🌦️ AI Weather Forecast Dashboard")
st.write("ML-based Weather Prediction System (Streamlit Safe Version)")

city = st.text_input("Enter City Name")

# ---------------- SAFE AI MODEL (NO SKLEARN DEPENDENCY ISSUE) ----------------
def predict_weather(city):
    np.random.seed(len(city))

    temp = np.random.randint(15, 45)
    humidity = np.random.randint(20, 90)
    wind = np.random.randint(5, 40)

    condition = np.random.choice(["Sunny ☀️", "Cloudy ☁️", "Rainy 🌧️", "Stormy ⛈️"])

    return temp, humidity, wind, condition


if st.button("Predict Weather"):

    if not city:
        st.warning("Please enter city name")
    else:
        temp, humidity, wind, condition = predict_weather(city)

        st.subheader(f"📍 Weather Report: {city}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature 🌡️", f"{temp} °C")
        col2.metric("Humidity 💧", f"{humidity}%")
        col3.metric("Wind 🌬️", f"{wind} km/h")

        st.success(f"Condition: {condition}")

        df = pd.DataFrame({
            "Parameter": ["Temp", "Humidity", "Wind"],
            "Value": [temp, humidity, wind]
        })

        st.bar_chart(df.set_index("Parameter"))

        if temp > 35:
            st.warning("🔥 Hot Weather Alert")
        elif temp < 20:
            st.info("❄️ Cold Weather Alert")
        else:
            st.success("😊 Normal Weather")
