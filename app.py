import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="AI Weather Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# ---------------- COLORFUL UI ----------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #e0f2fe, #fef9c3);
}

h1 {
    text-align: center;
    color: #0f172a;
    font-size: 42px;
    font-weight: 800;
}

.card {
    background: linear-gradient(135deg, #38bdf8, #60a5fa);
    padding: 20px;
    border-radius: 15px;
    color: white;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
    text-align: center;
}

.small-card {
    background: linear-gradient(135deg, #34d399, #10b981);
    padding: 15px;
    border-radius: 12px;
    color: white;
    text-align: center;
    margin-top: 10px;
}

.warn-card {
    background: linear-gradient(135deg, #f97316, #ef4444);
    padding: 15px;
    border-radius: 12px;
    color: white;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🌦️ AI Weather Intelligence Dashboard")
st.write("🔥 Colorful Smart Weather Prediction System")

# ---------------- INPUT ----------------
city = st.text_input("Enter City Name", "Islamabad")

# ---------------- SESSION ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- WEATHER ENGINE ----------------
def weather_engine(city):
    seed = sum(ord(c) for c in city.lower())
    np.random.seed(seed)

    temp = np.random.randint(15, 40)
    humidity = np.random.randint(25, 90)
    wind = np.random.randint(5, 35)

    condition = np.random.choice([
        "Sunny ☀️",
        "Cloudy ☁️",
        "Rainy 🌧️",
        "Windy 🌬️",
        "Pleasant 🌤️"
    ])

    return temp, humidity, wind, condition

# ---------------- BUTTON ----------------
if st.button("🚀 Generate Weather"):

    temp, humidity, wind, condition = weather_engine(city)

    # save history
    st.session_state.history.append({
        "City": city,
        "Temp": temp,
        "Humidity": humidity,
        "Wind": wind,
        "Condition": condition,
        "Time": datetime.now().strftime("%H:%M:%S")
    })

    # ---------------- COLORFUL CARDS ----------------
    col1, col2, col3, col4 = st.columns(4)

    col1.markdown(f"""
    <div class="card">
    🌡️<br><b>Temperature</b><br>{temp}°C
    </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
    <div class="small-card">
    💧<br><b>Humidity</b><br>{humidity}%
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div class="small-card">
    🌬️<br><b>Wind</b><br>{wind} km/h
    </div>
    """, unsafe_allow_html=True)

    col4.markdown(f"""
    <div class="card">
    📍<br><b>Condition</b><br>{condition}
    </div>
    """, unsafe_allow_html=True)

    # ---------------- ALERT SYSTEM ----------------
    st.markdown("### ⚡ Weather Insight")

    if temp >= 35:
        st.markdown('<div class="warn-card">🔥 Extreme Heat Alert!</div>', unsafe_allow_html=True)
    elif temp <= 18:
        st.markdown('<div class="small-card">❄️ Cold Weather Alert!</div>', unsafe_allow_html=True)
    elif "Rain" in condition:
        st.markdown('<div class="warn-card">☔ Rain Expected!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="small-card">😊 Normal Pleasant Weather</div>', unsafe_allow_html=True)

    # ---------------- CHART ----------------
    st.markdown("### 📊 Weather Chart")

    df = pd.DataFrame({
        "Type": ["Temp", "Humidity", "Wind"],
        "Value": [temp, humidity, wind]
    })

    st.bar_chart(df.set_index("Type"))

# ---------------- HISTORY ----------------
if len(st.session_state.history) > 0:

    st.markdown("### 📜 History")

    st.dataframe(pd.DataFrame(st.session_state.history), use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🌦️ AI Weather Dashboard | Colorful UI Version | Streamlit Project")
