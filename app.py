import streamlit as st

# Page config
st.set_page_config(page_title="Sentiment Studio", layout="wide")

# CSS styles for dark, edgy, aesthetic look
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');
        body, .stApp {
            background-color: #121212;
            color: #e0e0e0 !important;
            font-family: 'Poppins', sans-serif;
            height: 100vh;
            margin: 0;
            display: flex !important;
            justify-content: center;
            align-items: center;
        }
        .container {
            text-align: center;
            max-width: 900px;
            width: 90%;
        }
        h1 {
            font-size: 3.5rem;
            font-weight: 700;
            color: #9c27b0;
            text-shadow: 0 0 10px #9c27b0;
            margin-bottom: 0.2rem;
        }
        h3 {
            color: #00bcd4;
            font-weight: 500;
            margin-top: 0;
            margin-bottom: 2rem;
            text-shadow: 0 0 8px #00bcd4;
        }
        .button-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 1.8rem;
        }
        .btn {
            background: transparent;
            border: 2px solid #9c27b0;
            border-radius: 12px;
            padding: 1.2rem 1.8rem;
            font-size: 1.3rem;
            color: #e0e0e0;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 0 5px #9c27b0;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.6rem;
            font-weight: 600;
        }
        .btn:hover {
            background: #9c27b0;
            box-shadow: 0 0 15px #9c27b0;
            transform: scale(1.05);
            color: white;
        }
        .emoji {
            font-size: 1.5rem;
        }
        .info {
            margin-top: 2rem;
            font-size: 1.1rem;
            color: #bbb;
            min-height: 40px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<h1>Sentiment Studio</h1>', unsafe_allow_html=True)
st.markdown('<h3>Real-Time Social Media Opinion Dashboard</h3>', unsafe_allow_html=True)

# Buttons in grid
st.markdown('<div class="button-grid">', unsafe_allow_html=True)

clicked = None
if st.button("🐦 Twitter", key="twitter"):
    clicked = "Twitter data fetching coming soon! 🚀"

if st.button("👽 Reddit", key="reddit"):
    clicked = "Reddit data fetching coming soon! 🚀"

if st.button("📸 Instagram", key="instagram"):
    clicked = "Instagram data fetching coming soon! 🚀"

if st.button("🎥 YouTube", key="youtube"):
    clicked = "YouTube data fetching coming soon! 🚀"

if st.button("🎵 TikTok", key="tiktok"):
    clicked = "TikTok data fetching coming soon! 🚀"

if st.button("💼 LinkedIn", key="linkedin"):
    clicked = "LinkedIn data fetching coming soon! 🚀"

st.markdown('</div>', unsafe_allow_html=True)

if clicked:
    st.markdown(f'<div class="info">{clicked}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="info">Click any platform to see a preview message.</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
