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

# 4. Custom Styling & Header
st.markdown("""
    <style>
    .stMetric {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🇹🇻 Tuvalu National Weather Center</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #aaa;'>Last Updated: {datetime.now().strftime('%d %B %Y, %H:%M')}</p>", unsafe_allow_html=True)

# 5. Dashboard Layout (Island Metrics)
col1, col2, col3 = st.columns(3)

# Exact coordinates for the islands
islands_data = {
    "Funafuti": {"lat": -8.5208, "lon": 179.1962},
    "Nanumea": {"lat": -5.67, "lon": 176.12},
    "Nui": {"lat": -7.22, "lon": 177.15}
}

for i, (name, coords) in enumerate(islands_data.items()):
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

# 6. Interactive Map Section
st.markdown("---")
st.subheader("Regional Satellite View")

map_df = pd.DataFrame([
    {'lat': -8.5208, 'lon': 179.1962, 'name': 'Funafuti'},
    {'lat': -5.6700, 'lon': 176.1200, 'name': 'Nanumea'},
    {'lat': -7.2200, 'lon': 177.1500, 'name': 'Nui'}
])

st.map(map_df)

st.info("💡 Data provided by OpenWeather API. Dashboard refreshes on page reload.")
