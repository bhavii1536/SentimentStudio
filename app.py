import streamlit as st
from PIL import Image

# Set Streamlit page config
st.set_page_config(page_title="Sentiment Studio 💬", layout="wide")

# Title and Subheader
st.title("💬 Sentiment Studio")
st.subheader("Real-Time Social Media Opinion Dashboard Using Machine Learning")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio("Go to", ["Home", "Platform Insights", "Upload Data", "About"])

# Home Section
if section == "Home":
    st.markdown("### 🌟 Welcome to Sentiment Studio!")
    st.success("This tool helps you analyze public sentiment from platforms like Twitter, Reddit, and Instagram.")
    st.info("⚙️ Features coming soon: Real-time scraping, sentiment prediction, beautiful graphs!")

# Platform Insights Section
elif section == "Platform Insights":
    st.markdown("### 📊 Social Media Sentiment Insights")
    st.warning("Feature under development. Stay tuned!")

# Upload Data Section
elif section == "Upload Data":
    st.markdown("### 📁 Upload CSV File for Analysis")
    uploaded_file = st.file_uploader("Upload a CSV file with text data (e.g., tweets or comments):", type="csv")
    if uploaded_file:
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write("📄 Uploaded Data:")
        st.dataframe(df.head())

# About Section
elif section == "About":
    st.markdown("### ℹ️ About This Project")
    st.markdown("""
    **Sentiment Studio** is your real-time dashboard for analyzing public emotions across multiple social media platforms 🌍💡  
    Built using **Python + Streamlit + Machine Learning + NLP** ❤️  
    """)
    st.markdown("Made with ☕ & ❤️ by **Bhavii1536**")

# Footer
st.markdown("---")
st.markdown("💡 *This is an academic project. Live APIs, ML models, and dashboards coming soon!*")

