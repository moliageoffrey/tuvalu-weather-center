import streamlit as st
import requests

# 1. PAGE SETUP (Dedicated Full Width)
st.set_page_config(page_title="Tuvalu National Weather Center", layout="wide")

# 2. FULL-PAGE CSS
st.html("""
    <style>
        /* Hide Streamlit UI */
        footer {display: none !important;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        
        /* Dark Theme & Spacing */
        .stApp {background-color: #0f172a;}
        .block-container {padding-top: 1rem !important; padding-bottom: 2rem !important;}
        
        /* Card Styling */
        .weather-hero {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border-radius: 28px;
            padding: 40px;
            border: 1px solid #334155;
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""")

# 3. WEATHER DATA FETCH
def get_weather():
    try:
        api_key = st.secrets["OPENWEATHER_API_KEY"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q=Funafuti,TV&appid={api_key}&units=metric"
        data = requests.get(url).json()
        return {
            "temp": round(data['main']['temp']),
            "hum": data['main']['humidity'],
            "wind": round(data['wind']['speed'] * 3.6, 1),
            "cond": data['weather'][0]['main'],
            "icon": data['weather'][0]['icon'],
            "desc": data['weather'][0]['description']
        }
    except:
        return {"temp": 30, "hum": 82, "wind": 15, "cond": "Cloudy", "icon": "03d", "desc": "overcast clouds"}

w = get_weather()

# 4. PAGE HEADER & QUICK STATS
st.markdown("<h1 style='text-align: center; color: white;'>🇹🇻 Tuvalu National Weather Center</h1>", unsafe_html=True)

# Metrics Row
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Current Temp", f"{w['temp']}°C")
with m2: st.metric("Humidity", f"{w['hum']}%")
with m3: st.metric("Wind Speed", f"{w['wind']} km/h")
with m4: st.metric("Condition", w['cond'])

st.divider()

# 5. MAIN CONTENT AREA
col_left, col_right = st.columns([1, 1.5], gap="large")

with col_left:
    # Large Weather Hero Card
    st.html(f"""
    <div class="weather-hero">
        <h2 style="color: #9ca3af; font-size: 1rem; margin-bottom: 10px;">FUNAFUTI ATOL</h2>
        <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="150">
        <h1 style="font-size: 5rem; color: white; margin: 0;">{w['temp']}°C</h1>
        <p style="color: #38bdf8; font-size: 1.5rem; text-transform: uppercase; font-weight: bold;">{w['desc']}</p>
        <div style="margin-top: 30px; border-top: 1px solid #334155; padding-top: 20px;">
            <p style="color: #64748b;">Local Time: Funafuti (UTC+12)</p>
        </div>
    </div>
    """)
    
    # Simple Local Tip
    st.info("**Island Advisory:** High humidity levels expected today. Ensure proper hydration and sun protection.")

with col_right:
    # LIVE WINDY MAP EMBED (Focused on Tuvalu)
    st.subheader("🛰️ Live Pacific Wind & Wave Radar")
    
    # This URL is specifically centered on Tuvalu coordinates (-8.52, 179.19)
    windy_url = "https://embed.windy.com/embed2.html?lat=-8.525&lon=179.196&zoom=6&level=surface&overlay=wind&product=ecmwf&menu=&message=true&marker=&calendar=now&pressure=true&type=map&location=coordinates&detail=&metricWind=km/h&metricTemp=%C2%B0C&radarRange=-1"
    
    st.components.v1.iframe(windy_url, height=550)

# 6. FOOTER DATA
st.caption("Data provided by OpenWeatherMap API and Windy.com Satellite Imagery.")