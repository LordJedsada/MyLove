import streamlit as st
import random
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="พลังใจจากเรา", page_icon="❤️")

# ส่วนหัวของ App
st.title("💖 ตู้เติมพลังใจอัตโนมัติ")
st.subheader("ถ้าเหนื่อยหรือท้อ กดปุ่มข้างล่างได้เลยนะ")

# รายการข้อความให้กำลังใจ (คุณแก้ข้อความเองได้เลย!)
messages = [
    "วันนี้เก่งมากแล้วนะ พักผ่อนเยอะๆ นะครับ 💤",
    "เราอยู่ข้างๆ เธอนะ ไม่ว่าจะเจออะไรมา ✌️",
    "รอยยิ้มของเธอคือความสุขของเรานะ 😊",

]

# ปุ่มกดรับข้อความ
if st.button("ขอกำลังใจหน่อย ✨"):
    with st.spinner('กำลังดึงพลังงานดีๆ มาให้...'):
        time.sleep(1) # เพิ่มความตื่นเต้นเล็กน้อย
        selected = random.choice(messages)
        st.balloons() # เอฟเฟกต์ลูกโป่งลอย
        st.success(f"### {selected}")

# ส่วน Chat เล็กๆ (Interactive)
st.divider()
user_input = st.text_input("อยากบอกอะไรเราไหม? (พิมพ์ตรงนี้ได้นะ)")
if user_input:
    st.write(f"เรารับรู้แล้วนะ: '{user_input}' ... เดี๋ยวเราจะตั้งใจอ่านแน่นอน ❤️")

# ปรับแต่ง CSS นิดหน่อยให้ดูหวานขึ้น
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_config=True)
