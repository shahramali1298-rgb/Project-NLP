import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# ---------------- UI ----------------
st.set_page_config(page_title="AI Weather Dashboard", layout="centered")

st.title("🌦️ AI Weather Forecast Dashboard")
st.write("ML-based Smart Weather Prediction System")

# ---------------- Input ----------------
city = st.text_input("Enter City Name")

# ---------------- Safe ML Model ----------------
@st.cache_resource
def train_model():
    X = np.array([
        [1, 20, 10],
        [2, 25, 15],
        [3, 30, 20],
        [4, 35, 25],
        [5, 40, 30]
    ])

    y = np.array([22, 27, 33, 37, 42])

    model = LinearRegression()
    model.fit(X, y)
    return model

model = train_model()

# ---------------- Weather Function ----------------
def predict_weather(city):
    np.random.seed(len(city))

    day = np.random.randint(1, 6)
    humidity = np.random.randint(20, 90)
    wind = np.random.randint(5, 40)

    temp = model.predict([[day, humidity, wind]])[0]
    condition = np.random.choice(["Sunny ☀️", "Cloudy ☁️", "Rainy 🌧️", "Stormy ⛈️"])

    return round(temp, 2), humidity, wind, condition

# ---------------- App ----------------
if st.button("Predict Weather"):

    if not city:
        st.warning("Please enter a city name")
    else:
        temp, humidity, wind, condition = predict_weather(city)

        st.subheader(f"📍 Weather Report: {city}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature 🌡️", f"{temp} °C")
        col2.metric("Humidity 💧", f"{humidity}%")
        col3.metric("Wind 🌬️", f"{wind} km/h")

        st.success(f"Condition: {condition}")

        # Chart
        df = pd.DataFrame({
            "Parameters": ["Temp", "Humidity", "Wind"],
            "Values": [temp, humidity, wind]
        })

        st.bar_chart(df.set_index("Parameters"))

        # AI Insight
        if temp > 35:
            st.warning("🔥 Hot Weather Alert")
        elif temp < 20:
            st.info("❄️ Cold Weather Alert")
        else:
            st.success("😊 Normal Weather Conditions")
