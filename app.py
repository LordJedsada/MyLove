import streamlit as st
import random
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="พลังใจจากเรา", page_icon="❤️")

# ส่วนหัวของ App
st.title("💖 ตู้เติมพลังใจอัตโนมัติจาก Bec")
st.subheader("ถ้าเหนื่อย เข้ามากดเติมใจได้คับบ")

# รายการข้อความให้กำลังใจที่คุณเขียนไว้
messages = [
    "วันนี้เก่งมากแล้วนะ อย่าลืมพักผ่อนแล้วหาอะไรอร่อยๆกินเติมพลังด้วยนะคับบ ❤️💤",
    "เค้าอยู่ข้างๆเธอนะ ไม่ว่าจะเจออะไรมาสู้ๆๆนะคับบ ✌️",
    "รอยยิ้มของเธอคือความสุขของเค้านะคับ 😊",
]

# ปุ่มกดรับข้อความ
if st.button("ขอกำลังใจหน่อย ✨"):
    with st.spinner('กำลังดึงพลังงานดีๆ มาให้...'):
        time.sleep(0.7) 
        selected = random.choice(messages)
        st.balloons() # กลับมาใช้ลูกโป่งที่ทำงานได้แน่นอน 100%
        st.success(f"### {selected}")

# ส่วน Chat เล็กๆ
st.divider()
user_input = st.text_input("อยากบอกอะไรเราไหม? (พิมพ์ตรงนี้ได้นะ)")

if user_input:
    # ข้อความตอบกลับน่ารักๆ แบบที่คุณเลือกไว้
    st.write(f"ข้อความ ' {user_input} ' ส่งถึงใจเค้าเรียบร้อย! ขอให้เธอหายเหนื่อย กินให้อิ่ม นอนพักผ่อนให้เต็มที่นะคับบ 🚀❤️")

# ปรับแต่งปุ่มให้เป็นสีชมพูแดงสวยๆ
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        background-color: #ff4b4b;
        color: white;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
