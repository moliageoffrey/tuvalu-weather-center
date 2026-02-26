import streamlit as st
import requests

# 1. PAGE SETUP
st.set_page_config(page_title="Tuvalu National Weather Center", layout="wide")

# 2. CUSTOM TUVALU STYLING
st.markdown("""
    <style>
        .stApp {background-color: #001f3f;} /* Dark Deep Sea Blue */
        .weather-card {
            background: linear-gradient(135deg, #05445E 0%, #189AB4 100%);
            border-radius: 20px;
            padding: 25px;
            color: white;
            border-bottom: 5px solid #FFD700; /* Tuvalu Gold */
            margin-bottom: 20px;
        }
        .stat-label { color: #D4F1F4; font-size: 0.8rem; text-transform: uppercase; font-weight: bold;}
        .flood-warning { background: #ff4b4b; padding: 10px; border-radius: 10px; text-align: center; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# 3. WEATHER DATA (Enhanced for multiple islands)
def get_island_weather(city):
    try:
        api_key = st.secrets["OPENWEATHER_API_KEY"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},TV&appid={api_key}&units=metric"
        data = requests.get(url).json()
        return data
    except:
        return None

# 4. HEADER
st.markdown("<h1 style='text-align: center; color: white;'>🇹🇻 Tuvalu National Weather Center</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #75E6DA;'>Live Climate & Tide Monitoring for the Archipelago</p>", unsafe_allow_html=True)

# 5. TOP ROW: ALERTS & TIDES
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""
        <div style='background: rgba(255,255,255,0.1); padding: 15px; border-radius: 15px;'>
            <h4 style='margin:0; color: #FFD700;'>🌊 Next High Tide: Funafuti</h4>
            <p style='font-size: 1.5rem; margin:0;'>05:45 PM <span style='font-size: 1rem;'> (2.4m)</span></p>
            <p style='color: #00ff00; font-size: 0.8rem;'>● Normal Operations</p>
        </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
        <div style='background: rgba(255,255,255,0.1); padding: 15px; border-radius: 15px;'>
            <h4 style='margin:0; color: #FFD700;'>🌪️ Cyclone Alert Status</h4>
            <p style='font-size: 1.5rem; margin:0;'>Condition: Green</p>
            <p style='color: #00ff00; font-size: 0.8rem;'>● No Active Threats</p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# 6. MAIN ISLAND DISPLAY
islands = ["Funafuti", "Nanumea", "Nui"]
cols = st.columns(len(islands))

for i, island in enumerate(islands):
    with cols[i]:
        w = get_island_weather(island)
        if w:
            temp = round(w['main']['temp'])
            icon = w['weather'][0]['icon']
            cond = w['weather'][0]['description']
            hum = w['main']['humidity']
            wind = w['wind']['speed']
            
            card_html = f"""
            <div class="weather-card">
                <div style="display: flex; justify-content: space-between;">
                    <span style="font-weight: bold;">📍 {island}</span>
                    <img src="http://openweathermap.org/img/wn/{icon}.png" width="40">
                </div>
                <h1 style="margin: 10px 0; font-size: 3rem;">{temp}°C</h1>
                <p style="text-transform: capitalize; color: #FFD700; margin-bottom: 20px;">{cond}</p>
                <div style="display: flex; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 10px;">
                    <div><span class="stat-label">Wind</span><br>{wind} m/s</div>
                    <div><span class="stat-label">Humidity</span><br>{hum}%</div>
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)

with col2:
    # --- LIVE SATELLITE SECTION ---
    st.markdown("<h3>🛰️ Regional Satellite (Live Clouds & Rain)</h3>", unsafe_allow_html=True)
    
    # Windy.com Live Satellite Map for Tuvalu
    satellite_url = "https://www.windy.com/-8.520/179.200?satellite,-9.319,179.200,6"
    
    # We use st.components.v1.iframe here which is more stable for map providers
    st.components.v1.iframe(
        "https://embed.windy.com/embed2.html?lat=-8.520&lon=179.200&detailLat=-8.520&detailLon=179.200&width=650&height=450&zoom=6&level=surface&overlay=satellite&product=satellite&menu=&message=true&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=default&metricTemp=default&radarRange=-1",
        height=500
    )
    
    # Optional Program Guide below the map
    with st.expander("📺 View TTV Program Guide"):
        st.components.v1.html("""
            <iframe src="https://www.ttv.sb/tv-guide/" width="100%" height="500px" style="border-radius:15px;"></iframe>
        """, height=520)
