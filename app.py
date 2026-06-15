import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# ---------------- UI ----------------
st.set_page_config(page_title="AI Weather Dashboard", layout="centered")

st.title("🌦️ AI Weather Forecast Dashboard")
st.write("Smart Weather Prediction System (ML-based simulation)")

# ---------------- Input ----------------
city = st.text_input("Enter City Name")

# ---------------- Fake Dataset (ML training) ----------------
# Simple synthetic dataset for ML model
X = np.array([
    [1, 20, 10],
    [2, 25, 15],
    [3, 30, 20],
    [4, 35, 25],
    [5, 40, 30]
])

y_temp = np.array([22, 27, 33, 37, 42])

model = LinearRegression()
model.fit(X, y_temp)

# ---------------- Weather Generator ----------------
def generate_weather(city):
    np.random.seed(len(city))

    day = np.random.randint(1, 6)
    humidity = np.random.randint(20, 90)
    wind = np.random.randint(5, 40)

    features = np.array([[day, humidity, wind]])
    temp = model.predict(features)[0]

    condition = np.random.choice(["Sunny ☀️", "Cloudy ☁️", "Rainy 🌧️", "Stormy ⛈️"])

    return round(temp, 2), humidity, wind, condition

# ---------------- App Logic ----------------
if st.button("Predict Weather"):

    if city == "":
        st.warning("Please enter a city name")
    else:
        temp, humidity, wind, condition = generate_weather(city)

        st.subheader(f"📍 Weather Report: {city}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature 🌡️", f"{temp} °C")
        col2.metric("Humidity 💧", f"{humidity}%")
        col3.metric("Wind 🌬️", f"{wind} km/h")

        st.success(f"Condition: {condition}")

        # ---------------- Chart ----------------
        df = pd.DataFrame({
            "Parameter": ["Temp", "Humidity", "Wind"],
            "Value": [temp, humidity, wind]
        })

        st.bar_chart(df.set_index("Parameter"))

        # ---------------- AI Insight ----------------
        if temp > 35:
            st.warning("🔥 Hot Weather Alert")
        elif temp < 20:
            st.info("❄️ Cold Weather")
        else:
            st.success("😊 Normal Weather Conditions")
