import streamlit as st
from PIL import Image

# ---------------- CONFIGURATION ----------------
st.set_page_config(
    page_title="SafeStreet App",
    page_icon="🚧",
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# ---------------- ASSETS & STYLING ----------------
st.markdown("""
<style>
    /* 1. IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    /* 2. GLOBAL RESET & BACKGROUND */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        background-attachment: fixed;
    }

    /* 3. REMOVE STREAMLIT CHROME */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    .block-container {
        padding-top: 1rem;
        padding-bottom: 5rem;
    }

    /* 5. TYPOGRAPHY */
    h1 { font-weight: 800; color: #fff; font-size: 2.2rem; margin-bottom: 0.2rem; letter-spacing: -1px; }
    h3 { font-weight: 600; color: #e0e0e0; font-size: 1.1rem; margin-top: 0; }
    p { color: #b0b0b0; font-size: 0.9rem; line-height: 1.5; }

    /* 6. BUTTON STYLING */
    .stButton > button {
        width: 100%;
        background: linear-gradient(92.88deg, #455EB5 9.16%, #5643CC 43.89%, #673FD7 64.72%);
        color: white;
        border: none;
        padding: 16px 20px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 16px;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 10px 20px -10px rgba(69, 94, 181, 0.5);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 14px 24px -10px rgba(69, 94, 181, 0.6);
        color: white;
    }

    /* 7. UPLOADER STYLING */
    [data-testid='stFileUploader'] { width: 100%; }
    section[data-testid="stFileUploader"] > section {
        background-color: rgba(255,255,255,0.03);
        border: 2px dashed rgba(255,255,255,0.2);
        border-radius: 20px;
    }

    /* 8. BOTTOM NAV */
    .bottom-nav {
        position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);
        width: 90%; max-width: 400px; height: 65px;
        background: rgba(20, 20, 40, 0.85);
        backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        border-radius: 35px; border: 1px solid rgba(255, 255, 255, 0.1);
        display: flex; justify-content: space-around; align-items: center;
        z-index: 999; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .nav-item { color: rgba(255,255,255,0.4); font-size: 24px; cursor: pointer; }
    .nav-item.active { color: #673FD7; background: rgba(103, 63, 215, 0.15); padding: 10px; border-radius: 50%; }

    /* 9. METRICS */
    .metric-container { display: flex; justify-content: space-between; gap: 10px; margin-top: 20px; margin-bottom: 20px; }
    .metric-box { background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px; text-align: center; flex: 1; }
    .metric-label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; color: rgba(255,255,255,0.5); margin-bottom: 4px; }
    .metric-value { font-size: 1rem; font-weight: 700; color: #fff; }

</style>
""", unsafe_allow_html=True)

# ---------------- APP LOGIC ----------------

def main():
    # Initialize Session State
    if "analysis_complete" not in st.session_state:
        st.session_state.analysis_complete = False

    # Header
    st.markdown("""
        <div style="padding-top: 20px; padding-bottom: 20px;">
            <h1>SafeStreet</h1>
            <p>Automated road damage assessment system.</p>
        </div>
    """, unsafe_allow_html=True)

    # Upload Section
    st.markdown("<h3>📸 Capture / Upload</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    # If file changes, reset analysis
    if uploaded_file:
        # Check if it's a new file (simple check)
        if "last_uploaded" not in st.session_state or st.session_state.last_uploaded != uploaded_file.name:
            st.session_state.analysis_complete = False
            st.session_state.last_uploaded = uploaded_file.name

        image = Image.open(uploaded_file).convert("RGB")
        with st.container():
            st.image(image, caption="Field Capture", use_container_width=True)
            st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)

        analyze_btn = st.button("RUN DIAGNOSTICS")

        # Logic: Run if button clicked OR if analysis was already done for this file
        if analyze_btn:
            st.session_state.analysis_complete = True
            
        if st.session_state.analysis_complete:
            # Mock Logic
            label = "pothole"
            score = 0.89
            
            if "hole" in label:
                damage = "Pothole"
                severity = "High"
                priority = "Immediate"
                color_code = "#FF4B4B" # Red
            elif "crack" in label:
                damage = "Crack"
                severity = "Medium"
                priority = "Scheduled"
                color_code = "#FFA500" # Orange
            else:
                damage = "Wear"
                severity = "Low"
                priority = "Monitor"
                color_code = "#00CC96" # Green

            # SINGLE UNIFIED CARD
            st.markdown(f"""
            <div class="glass-card" style="border-left: 5px solid {color_code};">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                    <h3>Diagnostic Report</h3>
                    <span style="background: {color_code}; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 800; color: white;">
                        {int(score*100)}% MATCH
                    </span>
                </div>
                
                <p style="font-size: 0.95rem; opacity: 0.9;">
                    Detailed analysis identified <strong>{damage}</strong> with <strong>{severity}</strong> severity.
                </p>

                <div class="metric-container">
                    <div class="metric-box">
                        <div class="metric-label">Priority</div>
                        <div class="metric-value" style="color: {color_code}">{priority}</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">Repair Type</div>
                        <div class="metric-value">Patch</div>
                    </div>
                </div>

                <div style="border-top: 1px solid rgba(255,255,255,0.1); margin: 20px 0;"></div>

                <h3>🛠️ Recommended Action</h3>
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 15px;">
                    <div style="background: rgba(255,255,255,0.05); padding: 12px; border-radius: 12px; display: flex; align-items: center;">
                        <span style="font-size: 1.2rem; margin-right: 15px;">🧱</span>
                        <div>
                            <div style="font-size: 0.7rem; text-transform: uppercase; opacity: 0.6;">Material Required</div>
                            <div style="font-weight: 600;">Cold Mix Asphalt (Type-B)</div>
                        </div>
                    </div>
                    
                    <div style="background: rgba(255,255,255,0.05); padding: 12px; border-radius: 12px; display: flex; align-items: center;">
                        <span style="font-size: 1.2rem; margin-right: 15px;">⏱️</span>
                        <div>
                            <div style="font-size: 0.7rem; text-transform: uppercase; opacity: 0.6;">Est. Labor Time</div>
                            <div style="font-weight: 600;">45 Minutes / 2 Workers</div>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Bottom Nav
    st.markdown("""
        <div class="bottom-nav">
            <div class="nav-item">🏠</div>
            <div class="nav-item active">📸</div>
            <div class="nav-item">⚙️</div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()