import streamlit as st

# Page config
st.set_page_config(page_title="Sentiment Studio", layout="wide")

# ---- Login data ----
VALID_EMAIL = "testuser@example.com"
VALID_PASSWORD = "Test@1234"

# ---- CSS styles ----
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');
        body, .stApp {
            background: linear-gradient(135deg, #7b2ff7, #f107a3);
            color: #f0f0f5 !important;
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
            font-size: 4rem;
            font-weight: 700;
            color: #e0c3fc;
            text-shadow: 0 0 15px #e0c3fc;
            margin-bottom: 0.2rem;
        }
        h3 {
            color: #c7d2fe;
            font-weight: 500;
            margin-top: 0;
            margin-bottom: 2.5rem;
            text-shadow: 0 0 10px #c7d2fe;
        }
        .button-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            justify-items: center;
            max-width: 700px;
            margin: 0 auto;
        }
        .btn {
            background: linear-gradient(45deg, #ff6fd8, #3813c2);
            border: none;
            border-radius: 15px;
            padding: 1.5rem 2.5rem;
            font-size: 1.4rem;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(255, 111, 216, 0.6);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.7rem;
            font-weight: 700;
            width: 180px;
            user-select: none;
        }
        .btn:hover {
            background: linear-gradient(45deg, #3813c2, #ff6fd8);
            box-shadow: 0 0 25px #ff6fd8;
            transform: scale(1.08);
        }
        .emoji {
            font-size: 1.7rem;
        }
        .info {
            margin-top: 2.5rem;
            font-size: 1.2rem;
            color: #ffe4f7;
            min-height: 40px;
            font-weight: 600;
        }
        /* Login form styles */
        .login-container {
            background: rgba(255,255,255,0.1);
            padding: 3rem 4rem;
            border-radius: 20px;
            box-shadow: 0 0 30px rgba(255,111,216,0.5);
            width: 400px;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 0.8rem 1rem;
            margin: 0.5rem 0 1.5rem 0;
            border-radius: 10px;
            border: none;
            font-size: 1rem;
            font-weight: 600;
        }
        input[type="submit"] {
            width: 100%;
            padding: 1rem 0;
            border-radius: 15px;
            border: none;
            background: #ff6fd8;
            color: white;
            font-weight: 700;
            font-size: 1.2rem;
            cursor: pointer;
            box-shadow: 0 0 15px #ff6fd8;
            transition: background 0.3s ease;
        }
        input[type="submit"]:hover {
            background: #3813c2;
            box-shadow: 0 0 25px #3813c2;
        }
        label {
            font-weight: 700;
            font-size: 1rem;
            color: #fbe8ff;
            user-select: none;
        }
    </style>
""", unsafe_allow_html=True)

# ----------- SESSION STATE SETUP ------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---- LOGIN PAGE ----
def login_page():
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<h2 style="color:#f8bbd0; margin-bottom: 1.5rem;">Login to Sentiment Studio</h2>', unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submitted = st.button("Login")

    if submitted:
        if email == VALID_EMAIL and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful! Redirecting...")
            st.experimental_rerun()
        else:
            st.error("Invalid email or password. Try again.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- DASHBOARD PAGE ----
def dashboard():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<h1>Sentiment Studio</h1>', unsafe_allow_html=True)
    st.markdown('<h3>Real-Time Social Media Opinion Dashboard</h3>', unsafe_allow_html=True)

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
        st.markdown('<div class="info">Click any platform button to see a preview message.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------- MAIN LOGIC --------
if not st.session_state.logged_in:
    login_page()
else:
    dashboard()
