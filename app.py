import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Weather Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
    <style>
    .main {background-color: #0f172a;}
    h1 {color: #38bdf8;}
    .stMetric {background-color: #1e293b; padding: 10px; border-radius: 10px;}
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🌦️ AI Weather Intelligence Dashboard")
st.write("Smart AI-based Weather Simulation System (Streamlit Edition)")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Controls")

city = st.sidebar.text_input("Enter City Name", "Islamabad")
unit = st.sidebar.selectbox("Temperature Unit", ["Celsius", "Fahrenheit"])

show_history = st.sidebar.checkbox("Show Weather History", True)

# ---------------- SESSION HISTORY ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- WEATHER ENGINE ----------------
def weather_engine(city):
    np.random.seed(len(city) + int(datetime.now().second))

    temp = np.random.randint(10, 45)
    humidity = np.random.randint(20, 95)
    wind = np.random.randint(5, 50)

    condition = np.random.choice([
        "Sunny ☀️", 
        "Cloudy ☁️", 
        "Rainy 🌧️", 
        "Stormy ⛈️", 
        "Windy 🌬️"
    ])

    return temp, humidity, wind, condition

# ---------------- MAIN BUTTON ----------------
if st.sidebar.button("🚀 Generate Weather"):

    temp, humidity, wind, condition = weather_engine(city)

    if unit == "Fahrenheit":
        temp = (temp * 9/5) + 32

    # save history
    st.session_state.history.append([city, temp, humidity, wind, condition])

    # ---------------- TOP METRICS ----------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🌡️ Temperature", f"{round(temp,1)}°")
    col2.metric("💧 Humidity", f"{humidity}%")
    col3.metric("🌬️ Wind Speed", f"{wind} km/h")
    col4.metric("📍 Condition", condition)

    # ---------------- ALERT SYSTEM ----------------
    st.subheader("⚡ AI Weather Insight")

    if temp > 35:
        st.error("🔥 Extreme Heat Alert!")
    elif temp < 15:
        st.info("❄️ Cold Weather Alert!")
    elif "Rainy" in condition:
        st.warning("☔ Rain Expected – carry umbrella!")
    else:
        st.success("😊 Normal Weather Conditions")

    # ---------------- CHART ----------------
    st.subheader("📊 Weather Analysis Chart")

    df = pd.DataFrame({
        "Parameters": ["Temperature", "Humidity", "Wind"],
        "Values": [temp, humidity, wind]
    })

    st.bar_chart(df.set_index("Parameters"))

# ---------------- HISTORY SECTION ----------------
if show_history and len(st.session_state.history) > 0:

    st.subheader("📜 Weather History")

    hist_df = pd.DataFrame(
        st.session_state.history,
        columns=["City", "Temp", "Humidity", "Wind", "Condition"]
    )

    st.dataframe(hist_df, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Built with Streamlit | AI Weather Simulation Dashboard")
