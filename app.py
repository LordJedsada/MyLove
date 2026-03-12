import streamlit as st
import random
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="พลังใจจากเรา", page_icon="❤️")

# --- ท่าไม้ตาย: เปลี่ยนหิมะให้เป็นหัวใจด้วย CSS ---
def heart_snow_css():
    # เราจะสุ่มเลือกหัวใจมาหนึ่งดวงในแต่ละรอบที่กด
    hearts = ["❤️", "💖", "💗", "💓", "🤍"]
    selected_heart = random.choice(hearts)
    
    st.markdown(f"""
        <style>
        /* บังคับให้เกล็ดหิมะกลายเป็นหัวใจที่คุณเลือก */
        .stSnow {{
            display: none !important;
        }}
        [data-testid="stSnow"] span::before {{
            content: "{selected_heart}" !important;
            color: transparent !important;
            text-shadow: 0 0 0 white !important; /* ป้องกันสีเพี้ยนในบางจอ */
            font-size: 25px !important;
        }}
        /* ส่วนนี้ทำให้ไอคอนหิมะมาตรฐานหายไปและแทนที่ด้วยหัวใจ */
        span[data-testid="stSnowIcon"] {{
            visibility: hidden;
        }}
        span[data-testid="stSnowIcon"]::after {{
            content: "{selected_heart}";
            visibility: visible;
            display: block;
            position: absolute;
            top: 0;
            left: 0;
        }}
        </style>
    """, unsafe_allow_html=True)
    st.snow()

# --- หน้าตา App ---
st.title("💖 ตู้เติมพลังใจอัตโนมัติ")
st.subheader("ถ้าเหนื่อยหรือท้อ กดปุ่มข้างล่างได้เลยนะ")

messages = [
    "วันนี้เก่งมากแล้วนะ อย่าลืมพักผ่อนแล้วหาอะไรอร่อยๆกิน เติมพลังด้วยนะคับบ ❤️💤",
    "เค้าอยู่ข้างๆเธอนะ ไม่ว่าจะเจออะไรมาสู้ๆๆนะคับบ ✌️",
    "รอยยิ้มของเธอคือความสุขของเค้านะคับ 😊",
]

# ปุ่มกดรับข้อความ
if st.button("ขอกำลังใจหน่อย ✨"):
    with st.spinner('กำลังดึงพลังงานดีๆ มาให้...'):
        time.sleep(0.5) 
        selected = random.choice(messages)
        heart_snow_css() # ใช้ฟังก์ชัน CSS แก้ทางหิมะ
        st.success(f"### {selected}")

# ส่วน Chat
st.divider()
user_input = st.text_input("อยากบอกอะไรเราไหม? (พิมพ์ตรงนี้ได้นะ)")

if user_input:
    st.write(f"ข้อความ ' {user_input} ' ส่งถึงใจเค้าเรียบร้อย! ขอให้เธอหายเหนื่อย กินให้อิ่ม นอนพักผ่อนให้เต็มที่นะคับบ 🚀❤️")

# ปรับแต่ง CSS ของปุ่มให้ดูแพง
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)
