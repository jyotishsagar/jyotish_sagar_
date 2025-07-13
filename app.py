import streamlit as st
from PIL import Image
import os

# Page settings
st.set_page_config(page_title="Jyotish Sagar", layout="wide")

# 🌄 Hanuman ji background
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://w0.peakpx.com/wallpaper/249/186/HD-wallpaper-lord-hanuman-ji-hanuman-ji.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

# 📸 Sidebar: image + menu
image_path = os.path.join(os.getcwd(), "dinesh_narayan.jpg.jpg")
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.sidebar.image(image, caption="पं. दिनेश नारायण मिश्रा", width=180)
else:
    st.sidebar.error("Image file नहीं मिली!")

st.sidebar.markdown("### 📋 Menu")
selected = st.sidebar.radio("चुनें:", ["🏠 Home", "📅 Book Kundali", "🔱 Book Pooja", "📞 Contact"])

# 💻 Main content
st.title("🔮 Jyotish Sagar")
st.markdown("### 🌟 Rashifal • Mahadasha • Astro Remedies")

# 🏠 Home
if selected == "🏠 Home":
    st.subheader("📺 Latest YouTube Video")
    video_url = "https://www.youtube.com/embed/vxKep2NiD9Y"
    st.components.v1.html(f"""
        <iframe width="100%" height="315"
        src="{video_url}"
        frameborder="0" allowfullscreen></iframe>
    """, height=330)

# 📅 Book Kundali
elif selected == "📅 Book Kundali":
    st.subheader("📝 Kundali Booking Form")
    name = st.text_input("आपका नाम")
    birth_date = st.date_input("जन्म तिथि")
    time = st.text_input("जन्म समय")
    place = st.text_input("जन्म स्थान")
    phone = st.text_input("मोबाइल नंबर")
    st.button("सबमिट करें")

# 🔱 Book Pooja
elif selected == "🔱 Book Pooja":
    st.subheader("🕉️ Pooja Booking Form")
    name = st.text_input("नाम")
    pooja_type = st.selectbox("Pooja Type", ["शांति पूजा", "गृह प्रवेश", "मंगल दोष", "रुद्राभिषेक"])
    date = st.date_input("पूजा की तिथि")
    address = st.text_area("स्थान")
    st.button("बुक करें")

# 📞 Contact
elif selected == "📞 Contact":
    st.subheader("📞 संपर्क करें")
    st.markdown("""
    - **नाम:** पं. दिनेश नारायण मिश्रा  
    - **मोबाइल:** +91-8858930846  
    - **ईमेल:** rudranshtiwari0100@gmail.com  
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 Jyotish Sagar | सभी अधिकार सुरक्षित")
