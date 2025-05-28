import streamlit as st

# Page Setup
st.set_page_config(
    page_title="Instant Duty & Document Checker",
    page_icon="📦",
    layout="centered"
)

# Title & Intro
st.title("📦 Instant Duty & Document Checker")
st.write("""
Welcome to **Instant Duty & Document Checker** — your AI-powered assistant for international trade compliance.

With just an **invoice**, **product name**, or **product image**, LogScale can instantly determine:
- 📊 Applicable **customs duties**
- 📄 Required **import/export documents**

This tool helps importers, exporters, and freight professionals reduce clearance time, avoid missing paperwork, and make confident trade decisions.
""")

# Demo Video
st.subheader("🎥 Watch How It Works")
st.video("https://www.youtube.com/watch?v=6nDmtt1I4TY&ab_channel=LogoMagicians")  # Replace with your demo link

# How it works
st.markdown("---")
st.subheader("⚙️ How It Works")
st.markdown("""
1. Upload an **invoice** or **product photo**  
2. Our AI extracts details and identifies the **HS code**  
3. It returns:
   - 📈 Estimated **duties and taxes**
   - 📋 List of **required clearance documents**
""")

# Benefits
st.markdown("---")
st.subheader("✅ Benefits")
st.markdown("""
- Reduce customs delays  
- Eliminate manual document checks  
- Ensure compliance with local regulations  
- Save time and money  
""")

# Coming Soon
st.markdown("---")
st.subheader("🚀 Coming Soon")
st.markdown("""
- Integration with customs APIs for real-time tariffs  
- Export documentation checker  
- Alerts on required licenses and restrictions  
""")

