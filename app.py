import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Sentiment Studio 💬", layout="wide")

# Custom styling
st.markdown("""
    <style>
        .main-title {
            font-size: 3.2rem;
            font-weight: 800;
            color: #6C63FF;
            text-align: center;
        }
        .sub-title {
            font-size: 1.5rem;
            color: #444;
            text-align: center;
        }
        .card {
            padding: 1.5rem;
            background-color: #ffffffdd;
            border-radius: 1rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .card h3 {
            color: #6C63FF;
        }
        .emoji {
            font-size: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Main Titles
st.markdown('<div class="main-title">💬 Sentiment Studio</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">A Real-Time Social Media Opinion Dashboard using Machine Learning</div>', unsafe_allow_html=True)
st.markdown("")

# Columns for platforms
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><div class="emoji">🐦</div><h3>Twitter</h3><p>Analyze trending tweets and hashtags in real time.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><div class="emoji">👽</div><h3>Reddit</h3><p>See what Reddit communities are buzzing about.</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><div class="emoji">📸</div><h3>Instagram</h3><p>Capture sentiment from captions, likes & comments.</p></div>', unsafe_allow_html=True)

st.markdown("---")

# Coming Soon Section
st.markdown("### 🚀 What's Coming Next?")
st.markdown("- ✅ Live API-based data fetching from Twitter, Reddit, Instagram")
st.markdown("- ✅ Real-time sentiment classification using ML")
st.markdown("- ✅ Visual charts, word clouds & alerts for brands")
st.markdown("- ✅ Multi-platform analytics in a single view")
st.markdown("---")

st.markdown("💡 *This is an early version. The engine behind the magic is coming soon!*")

