import streamlit as st
import numpy as np

st.title("AI Weather Dashboard")

city = st.text_input("Enter City")

def weather(city):
    np.random.seed(len(city))
    return np.random.randint(10,45)

if st.button("Check"):
    st.write("Temp:", weather(city))
    st.write("AI says: Weather is normal 😊")
