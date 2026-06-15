import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Weather Dashboard",
    page_icon="🌤️",
    layout="wide"
)

# ---------------- PREMIUM UI THEME ----------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #dbeafe, #f0f9ff);
}

.main {
    background: transparent;
}

h1 {
    text-align: center;
    color: #0284c7;
    font-size: 42px;
    font-weight: bold;
}

.stMetric {
    background: white;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🌤️ AI Weather Intelligence Dashboard")
st.write("✨ Smart, Clean & Modern Weather Prediction System")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Controls")

city = st.sidebar.text_input("Enter City", "Islamabad")
unit = st.sidebar.selectbox("Unit", ["Celsius", "Fahrenheit"])

# ---------------- HISTORY ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- SMART WEATHER ENGINE ----------------
def weather_engine(city):
    seed = sum(ord(c) for c in city.lower())
    np.random.seed(seed)

    base_temp = np.random.randint(18, 38)
    humidity = np.random.randint(30, 85)
    wind = np.random.randint(5, 30)

    conditions = ["Sunny ☀️", "Cloudy ☁️", "Rainy 🌧️", "Windy 🌬️", "Pleasant 🌤️"]
    condition = np.random.choice(conditions)

    # AI-style adjustment
    if "Rain" in condition:
        base_temp -= 3
    if humidity > 70:
        base_temp -= 1

    return base_temp, humidity, wind, condition

# ---------------- BUTTON ----------------
if st.sidebar.button("🚀 Generate Forecast"):

    temp, humidity, wind, condition = weather_engine(city)

    if unit == "Fahrenheit":
        temp = (temp * 9/5) + 32

    # save history
    st.session_state.history.append({
        "City": city,
        "Temp": round(temp, 1),
        "Humidity": humidity,
        "Wind": wind,
        "Condition": condition,
        "Time": datetime.now().strftime("%H:%M:%S")
    })

    # ---------------- METRICS ROW ----------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🌡️ Temperature", f"{round(temp,1)}°")
    col2.metric("💧 Humidity", f"{humidity}%")
    col3.metric("🌬️ Wind", f"{wind} km/h")
    col4.metric("📍 Condition", condition)

    # ---------------- BEAUTIFUL RESULT CARD ----------------
    st.markdown("### 🌟 AI Weather Insight")

    if temp >= 35:
        st.success("🔥 Hot Weather - Stay Hydrated!")
    elif temp <= 15:
        st.info("❄️ Cold Weather - Wear Warm Clothes")
    elif "Rain" in condition:
        st.warning("☔ Rain Expected - Carry Umbrella")
    else:
        st.success("😊 Perfect Weather Conditions")

    # ---------------- CHART ----------------
    st.markdown("### 📊 Weather Analysis")

    df = pd.DataFrame({
        "Type": ["Temperature", "Humidity", "Wind"],
        "Value": [temp, humidity, wind]
    })

    st.bar_chart(df.set_index("Type"))

# ---------------- HISTORY ----------------
if len(st.session_state.history) > 0:

    st.markdown("### 📜 Recent Weather History")

    hist_df = pd.DataFrame(st.session_state.history)

    st.dataframe(hist_df, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🌤️ AI Weather Dashboard | Modern UI Version | Built with Streamlit")
