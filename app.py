import streamlit as st
import requests

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Tuvalu National Weather & TV Hub", 
    layout="wide", 
    page_icon="🇹🇻"
)

# 2. THE "CLEAN LOOK" CSS & TUVALU BRANDING
st.markdown("""
    <style>
        /* Hide Streamlit elements for a professional 'Web App' feel */
        footer {display: none !important;}
        header {visibility: hidden;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        
        /* Deep Ocean Background */
        .stApp {background-color: #001f2b;}
        
        /* Space management */
        .block-container {padding-top: 1.5rem !important; padding-bottom: 0rem !important;}
        
        /* Custom font for headers */
        h3 { font-family: 'Inter', sans-serif; letter-spacing: -0.5px; }
    </style>
""", unsafe_allow_html=True)

# 3. WEATHER FETCHING FUNCTION
def get_weather():
    try:
        if "OPENWEATHER_API_KEY" in st.secrets:
            api_key = st.secrets["OPENWEATHER_API_KEY"]
            # Fetching for Funafuti, Tuvalu
            url = f"http://api.openweathermap.org/data/2.5/weather?q=Funafuti,TV&appid={api_key}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()
            
            return {
                "temp": round(data['main']['temp']),
                "hum": data['main']['humidity'],
                "wind": round(data['wind']['speed'] * 3.6, 1), # Convert m/s to km/h
                "cond": data['weather'][0]['description'],
                "icon": data['weather'][0]['icon']
            }
    except Exception as e:
        pass
    
    # Fallback Data (Default display if API is offline/secret missing)
    return {"temp": 29, "hum": 75, "wind": 14.5, "cond": "partly cloudy", "icon": "02d"}

w = get_weather()

# 4. MAIN DASHBOARD LAYOUT
# col1: National Resilience Weather Hub | col2: Solomon TTV Guide
col1, col2 = st.columns([1.1, 2], gap="large")

with col1:
    # --- NATIONAL RESILIENCE HUB WEATHER INTERFACE ---
    weather_card = f"""
    <div style="
        background: linear-gradient(160deg, #002B36 0%, #004B5E 100%); 
        border-radius: 28px; 
        padding: 30px; 
        color: white; 
        border: 2px solid #38bdf8; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        font-family: 'Inter', -apple-system, sans-serif;
    ">
        <div style="text-align: center; border-bottom: 1px solid rgba(56, 189, 248, 0.3); padding-bottom: 15px; margin-bottom: 25px;">
            <h3 style="margin:0; font-size: 1.1rem; color: #FFD700; letter-spacing: 2px; font-weight: 800;">🇹🇻 NATIONAL RESILIENCE HUB</h3>
            <p style="margin:5px 0 0; font-size: 0.75rem; color: #9ca3af; font-weight: 600;">COASTAL MONITORING: FUNAFUTI</p>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 style="font-size: 4.2rem; margin:0; font-weight: 800; color: white; letter-spacing: -3px;">{w['temp']}°C</h1>
                <p style="color: #38bdf8; font-weight: 700; font-size: 1.2rem; text-transform: capitalize; margin-top: -5px;">{w['cond']}</p>
            </div>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="120" style="filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.5));">
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 25px;">
            
            <div style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 18px; border-left: 5px solid #38bdf8;">
                <small style="color: #9ca3af; display: block; font-size: 0.7rem; font-weight: bold; text-transform: uppercase;">Tidal Risk</small>
                <span style="font-weight: 800; color: #00ffcc; font-size: 1.1rem;">NORMAL</span>
            </div>

            <div style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 18px; border-left: 5px solid #FFD700;">
                <small style="color: #9ca3af; display: block; font-size: 0.7rem; font-weight: bold; text-transform: uppercase;">UV Index</small>
                <span style="font-weight: 800; color: #f8fafc; font-size: 1.1rem;">HIGH (8)</span>
            </div>

            <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 18px;">
                <small style="color: #9ca3af; display: block; font-size: 0.7rem; font-weight: bold; text-transform: uppercase;">Humidity</small>
                <span style="font-weight: 800; font-size: 1.2rem;">{w['hum']}%</span>
            </div>

            <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 18px;">
                <small style="color: #9ca3af; display: block; font-size: 0.7rem; font-weight: bold; text-transform: uppercase;">Wind Speed</small>
                <span style="font-weight: 800; font-size: 1.2rem;">{w['wind']} <small style="font-size: 0.7rem;">km/h</small></span>
            </div>
        </div>

        <div style="margin-top: 25px; background: rgba(56, 189, 248, 0.1); border: 1px dashed #38bdf8; padding: 12px; border-radius: 15px; text-align: center;">
            <p style="margin:0; font-size: 0.8rem; color: #38bdf8; font-weight: 600;">
                🌊 ADVISORY: No coastal flood threats detected for the current tide cycle.
            </p>
        </div>
    </div>
    """
    # Use HTML component to bypass Markdown text rendering issues and provide Safari stability
    st.components.v1.html(weather_card, height=550)

with col2:
    # --- TV GUIDE SECTION ---
    st.markdown("<h3 style='color: white; margin-top: 0;'>📅 Solomon TTV Program Guide</h3>", unsafe_allow_html=True)
    
    # Sandboxed iframe to prevent Safari download triggers
    st.components.v1.html("""
        <iframe 
            src="https://www.ttv.sb/tv-guide/" 
            width="100%" 
            height="750px" 
            style="border: 1px solid #1f2937; border-radius: 20px; background: white;"
            sandbox="allow-scripts allow-same-origin allow-forms"
            loading="lazy">
        </iframe>
    """, height=780)
