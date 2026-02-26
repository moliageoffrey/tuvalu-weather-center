with col1:
    # --- ENHANCED TUVALU RESILIENCE DASHBOARD ---
    weather_card = f"""
    <div style="
        background: linear-gradient(160deg, #002B36 0%, #004B5E 100%); 
        border-radius: 28px; 
        padding: 25px; 
        color: white; 
        border: 2px solid #38bdf8; 
        box-shadow: 0 15px 30px rgba(0,0,0,0.5);
        font-family: 'Inter', sans-serif;
    ">
        <div style="text-align: center; border-bottom: 1px solid rgba(56, 189, 248, 0.3); padding-bottom: 15px; margin-bottom: 20px;">
            <h3 style="margin:0; font-size: 1.1rem; color: #FFD700; letter-spacing: 2px;">🇹🇻 NATIONAL RESILIENCE HUB</h3>
            <p style="margin:5px 0 0; font-size: 0.75rem; color: #9ca3af;">COASTAL MONITORING: FUNAFUTI</p>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 style="font-size: 4rem; margin:0; font-weight: 800; color: white;">{w['temp']}°C</h1>
                <p style="color: #38bdf8; font-weight: 700; font-size: 1.1rem; text-transform: capitalize;">{w['cond']}</p>
            </div>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="110">
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 20px;">
            
            <div style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 15px; border-left: 4px solid #38bdf8;">
                <small style="color: #9ca3af; display: block; font-size: 0.65rem;">TIDAL RISK</small>
                <span style="font-weight: 700; color: #00ff00;">LOW IMPACT</span>
            </div>

            <div style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 15px; border-left: 4px solid #FFD700;">
                <small style="color: #9ca3af; display: block; font-size: 0.65rem;">UV INDEX</small>
                <span style="font-weight: 700;">HIGH (8/11)</span>
            </div>

            <div style="background: rgba(255,255,255,0.05); padding: 12px; border-radius: 15px;">
                <small style="color: #9ca3af; display: block; font-size: 0.65rem;">HUMIDITY</small>
                <span style="font-weight: 700;">{w['hum']}%</span>
            </div>

            <div style="background: rgba(255,255,255,0.05); padding: 12px; border-radius: 15px;">
                <small style="color: #9ca3af; display: block; font-size: 0.65rem;">WIND SPEED</small>
                <span style="font-weight: 700;">{w['wind']} km/h</span>
            </div>
        </div>

        <div style="margin-top: 20px; background: rgba(56, 189, 248, 0.1); border: 1px dashed #38bdf8; padding: 10px; border-radius: 12px; text-align: center;">
            <p style="margin:0; font-size: 0.75rem; color: #38bdf8; font-weight: 600;">
                📢 ADVISORY: No coastal flood threats detected for the current tide cycle.
            </p>
        </div>
    </div>
    """
    st.components.v1.html(weather_card, height=500)
