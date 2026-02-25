import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Tuvalu National Weather Center",
    page_icon="🇹🇻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Load API Key from Streamlit Secrets
# (Make sure you added OPENWEATHER_API_KEY in the Streamlit Cloud Advanced Settings!)
try:
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]
except:
    st.error("API Key not found. Please add OPENWEATHER_API_KEY to Streamlit Secrets.")
    st.stop()

# 3. Weather Fetching Function (Using Coordinates)
def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# ... (keep your header/styling sections) ...

# 5. Dashboard Layout
col1, col2, col3 = st.columns(3)

# Exact coordinates for the islands
islands = {
    "Funafuti": {"lat": -8.5208, "lon": 179.1962},
    "Nanumea": {"lat": -5.67, "lon": 176.12},
    "Nui": {"lat": -7.22, "lon": 177.15}
}

for i, (name, coords) in enumerate(islands.items()):
    data = get_weather(coords["lat"], coords["lon"])
    
    if data.get("main"):
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()
        hum = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        
        with [col1, col2, col3][i]:
            st.metric(label=f"📍 {name}", value=f"{temp}°C", delta=desc)
            st.write(f"💨 Wind: {wind} m/s")
            st.write(f"💧 Humidity: {hum}%")
    else:
        with [col1, col2, col3][i]:
            st.error(f"Could not load data for {name}")
# Coordinates for Tuvalu islands
islands = ["Funafuti", "Nanumea", "Nui"]

for i, island in enumerate(islands):
    data = get_weather(island)
    if data.get("main"):
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()
        hum = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        
        with [col1, col2, col3][i]:
            st.metric(label=f"📍 {island}", value=f"{temp}°C", delta=desc)
            st.write(f"💨 Wind: {wind} m/s")
            st.write(f"💧 Humidity: {hum}%")
    else:
        with [col1, col2, col3][i]:
            st.error(f"Could not load data for {island}")

# 6. Interactive Map Section
st.markdown("---")
st.subheader("Regional Satellite View")

# Center of Tuvalu roughly: -7.1095, 177.6493
map_data = pd.DataFrame({
    'lat': [-8.5208, -5.6700, -7.2200],
    'lon': [179.1962, 176.1200, 177.1500]
})

st.map(map_data)

st.info("💡 Pro-Tip: This dashboard updates automatically when you refresh the page. Data provided by OpenWeather API.")
