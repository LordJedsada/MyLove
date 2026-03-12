import streamlit as st
import random
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="พลังใจจากเรา", page_icon="❤️")

# ส่วนหัวของ App
st.title("💖 ตู้เติมพลังใจอัตโนมัติ")
st.subheader("ถ้าเหนื่อยหรือท้อ กดปุ่มข้างล่างได้เลยนะ")

# รายการข้อความให้กำลังใจ
messages = [
    "วันนี้เก่งมากแล้วนะ อย่าลืมพักผ่อนแล้วหาอะไรอร่อยๆกิน เติมพลังด้วยนะคับบ ❤️💤",
    "เค้าอยู่ข้างๆเธอนะ ไม่ว่าจะเจออะไรมาสู้ๆๆนะคับบ ✌️",
    "รอยยิ้มของเธอคือความสุขของเค้านะคับ 😊",
]

# ปุ่มกดรับข้อความ
if st.button("ขอกำลังใจหน่อย ✨"):
    with st.spinner('กำลังดึงพลังงานดีๆ มาให้...'):
        time.sleep(1) 
        selected = random.choice(messages)
        st.balloons() 
        st.success(f"### {selected}")

# ส่วน Chat เล็กๆ
st.divider()
user_input = st.text_input("อยากบอกอะไรเราไหม? (พิมพ์ตรงนี้ได้นะ)")
if user_input:
    st.write(f"เค้ารับรู้แล้วนะ: '{user_input}' ... เดี๋ยวเค้าจะตั้งใจอ่านแน่นอน ❤️")

# ส่วนที่แก้ไข: ปรับจาก unsafe_allow_config เป็น unsafe_allow_html
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
