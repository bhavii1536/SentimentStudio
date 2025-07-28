import streamlit as st

# Page config
st.set_page_config(page_title="Sentiment Studio 💬", layout="wide")

# CSS styles for neon buttons and background
st.markdown("""
    <style>
        /* Background gradient dark neon */
        body, .stApp {
            background: radial-gradient(circle at center, #0f2027, #203a43, #2c5364);
            color: #eee;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        /* Center all content */
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            gap: 2rem;
        }
        /* Neon glowing title */
        .main-title {
            font-size: 3.8rem;
            font-weight: 900;
            color: #00fff7;
            text-shadow:
                0 0 5px #00fff7,
                0 0 10px #00fff7,
                0 0 20px #00fff7,
                0 0 40px #0ff,
                0 0 80px #0ff;
            text-align: center;
        }
        /* Subheading */
        .sub-title {
            font-size: 1.6rem;
            color: #a0f0f8;
            text-align: center;
            margin-bottom: 3rem;
            font-weight: 600;
            letter-spacing: 1.5px;
        }
        /* Neon popup buttons */
        .neon-button {
            background: transparent;
            border: 2px solid #00fff7;
            border-radius: 15px;
            padding: 1.2rem 2.5rem;
            font-size: 1.5rem;
            font-weight: 700;
            color: #00fff7;
            cursor: pointer;
            transition: 0.3s ease-in-out;
            box-shadow:
                0 0 5px #00fff7,
                0 0 10px #00fff7,
                0 0 20px #00fff7;
        }
        .neon-button:hover {
            background: #00fff7;
            color: #023737;
            box-shadow:
                0 0 15px #00fff7,
                0 0 30px #00fff7,
                0 0 40px #00fff7,
                0 0 80px #00fff7;
            transform: scale(1.05);
        }
        /* Container for buttons */
        .button-container {
            display: flex;
            gap: 2rem;
            flex-wrap: wrap;
            justify-content: center;
            max-width: 900px;
        }
    </style>
""", unsafe_allow_html=True)

# Main container div start
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title and subtitle
st.markdown('<h1 class="main-title">💬 Sentiment Studio</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Real-Time Social Media Opinion Dashboard<br>Powered by Machine Learning</p>', unsafe_allow_html=True)

# Buttons container start
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Platform buttons
if st.button("🐦 Twitter"):
    st.info("Twitter data fetching coming soon! 🚀")

if st.button("👽 Reddit"):
    st.info("Reddit data fetching coming soon! 🚀")

if st.button("📸 Instagram"):
    st.info("Instagram data fetching coming soon! 🚀")

if st.button("🎥 YouTube"):
    st.info("YouTube data fetching coming soon! 🚀")

if st.button("🎵 TikTok"):
    st.info("TikTok data fetching coming soon! 🚀")

if st.button("💼 LinkedIn"):
    st.info("LinkedIn data fetching coming soon! 🚀")

# Buttons container end
st.markdown('</div>', unsafe_allow_html=True)

# Main container div end
st.markdown('</div>', unsafe_allow_html=True)
