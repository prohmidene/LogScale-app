import streamlit as st

# Page setup
st.set_page_config(
    page_title="LogScale – AI for Import/Export",
    page_icon="🌍",
    layout="wide",
)

# 🎯 Hero Section
st.image("assets/trade-hero.jpg", use_column_width=True)

st.markdown("<h1 style='text-align: center; color: #00c0b1;'>AI-Powered Import & Export Simplified.</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Make smarter trade decisions. Manage logistics with confidence.</h4>", unsafe_allow_html=True)

st.markdown("""
<center>
<a href='#demo'><button style='font-size:16px;padding:10px 20px;'>🚀 Get Started Free</button></a> &nbsp;
<a href='mailto:contact@logscale.tn'><button style='font-size:16px;padding:10px 20px;'>📞 Talk to Our Team</button></a>
</center>
""", unsafe_allow_html=True)

# 🧭 Mission Statement
st.markdown("---")
st.markdown("## 🧭 Tunisia & Africa are changing. Your business should lead the way.")

st.markdown("""
**LogScale** is an AI-powered platform built to simplify trade operations and help African businesses scale globally.  
Our mission: **Make international commerce effortless, data-driven, and profitable.**

> “Maʿa LogScale, el ʿālam bin īdīk.”  
> *(With LogScale, the world is in your hands.)*
""")

# 👥 Who It’s For
st.markdown("---")
st.markdown("## 👥 Who It’s For")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Importers / Business Owners")
    st.markdown("""
✅ Free AI assistant to simplify clearance  
✅ Get your duties & required documents instantly  
✅ Just drag & drop invoice/product image  
✅ Estimate total shipment cost in one click  
✅ Source products globally with verified suppliers  
✅ Securely archive your trade documents  
✅ Track shipments in real time  

🏆 *Coming Soon:* Product trend alerts, export matching tools
""")

with col2:
    st.subheader("🚚 Freight Forwarders / Brokers")
    st.markdown("""
✅ Auto-classification of declarations  
✅ Instant HS Code detection & validation  
✅ Automatic paperwork generation  
✅ Compliance check and document reminders  
✅ AI-powered client management dashboard  
✅ Reduce clearance errors & time  

🏆 *Coming Soon:* Export declaration modules, client sourcing API
""")

# 📊 How It Works
st.markdown("---")
st.markdown("## 📊 How It Works")

st.markdown("""
**All It Takes Is a Photo or Invoice**

1. 📤 Upload invoice or product photo  
2. 🤖 Our AI extracts details, matches HS codes  
3. 📄 You get duties, fees, and required documents  
4. 🔗 Choose optional sourcing, shipping or brokerage support

[💡 Try a Sample] [🛠️ Integrate With Your Store]
""")

# 📈 Why LogScale?
st.markdown("---")
st.markdown("## 📈 Why LogScale?")

st.markdown("""
🌍 Built for African markets  
🔐 Secure & encrypted data handling  
🤝 Backed by freight professionals & legal experts  
📡 Real-time market and customs updates  
💡 Constantly learning AI to reduce mistakes
""")

# ✨ Early Access Benefits
st.markdown("---")
st.markdown("## ✨ Early Access Benefits")

st.markdown("""
Be the First to Shape the Future of Trade in Africa

✅ Get early access to exclusive sourcing tools  
✅ Contribute to building your ideal platform  
✅ Access private newsletter and roadmap updates

[🚀 Join Beta Access] [🤝 Become a Partner]
""")

# 🚀 Demo Section
st.markdown("---")
st.markdown("<a name='demo'></a>", unsafe_allow_html=True)
st.markdown("## 🚀 Try Our Demo")
st.markdown("Upload an invoice and watch AI extract everything you need for clearance and documentation.")

# Only the Duty & Document Checker remains
st.page_link("pages/2_Instant_Duty_and_Document_Checker.py", label="📦 Go to Duty & Document Checker", icon="📦")

# 📬 Footer
st.markdown("---")
st.markdown("## 📬 Start your import journey the smarter way.")

st.markdown("""
Let LogScale power your growth in Tunisia, Africa, and beyond.

[🌍 Get Started Now] [📩 Contact Our Team] [🔐 Privacy Policy]

---

📧 contact@logscale.tn  
🌐 [www.logscale.tn](http://www.logscale.tn)  
💼 [LinkedIn](https://www.linkedin.com/company/logscale-ai/)
""")
