import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Sentiment Studio 💬", layout="wide")

# Background Gradient & Styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right top, #a18cd1, #fbc2eb);
        }
        .main-title {
            font-size: 3.2rem;
            font-weight: 800;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            text-align: center;
        }
        .sub-title {
            font-size: 1.5rem;
            color: #f1f1f1;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
            text-align: center;
        }
        .card {
            padding: 1.5rem;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
            border-radius: 1.5rem;
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
            text-align: center;
            color: #fff;
        }
        .card h3 {
            color: #ffffff;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
        }
        .emoji {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        .stApp {
            background: linear-gradient(to right top, #a18cd1, #fbc2eb);
        }
    </style>
""", unsafe_allow_html=True)

# Main Titles
st.markdown('<div class="main-title">💬 Sentiment Studio</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Real-Time Social Media Opinion Dashboard using Machine Learning</div>', unsafe_allow_html=True)
st.markdown("")

# First Row
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><div class="emoji">🐦</div><h3>Twitter</h3><p>Analyze trending tweets and hashtags in real time.</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><div class="emoji">👽</div><h3>Reddit</h3><p>See what Reddit communities are buzzing about.</p></div>', unsafe_allow_html=True)

# Second Row
col3, col4 = st.columns(2)
with col3:
    st.markdown('<div class="card"><div class="emoji">📸</div><h3>Instagram</h3><p>Capture sentiment from captions, likes & comments.</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="card"><div class="emoji">🎥</div><h3>YouTube</h3><p>Analyze video titles, descriptions & comments to get public opinion.</p></div>', unsafe_allow_html=True)

# Divider
st.markdown("---")

# Coming Soon
st.markdown("### 🚀 What's Coming Next?", unsafe_allow_html=True)
st.markdown("- ✅ Live API-based data fetching from **Twitter, Reddit, Instagram, YouTube**")
st.markdown("- ✅ Real-time sentiment prediction using Machine Learning")
st.markdown("- ✅ Visual analytics, word clouds, trend tracking")
st.markdown("- ✅ Unified dashboard with platform filtering")

# Footer
st.markdown("---")
st.markdown("💡 <i>Made with 💖, ☕ & emojis by Bhavii</i>", unsafe_allow_html=True)
