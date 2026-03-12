import streamlit as st
import random
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="พลังใจจากเรา", page_icon="❤️")

# ฟังก์ชันทำให้หัวใจตก (คละสี)
def heart_snow():
    # เราจะใช้คำสั่ง snow แต่เปลี่ยนไอคอนเป็นหัวใจคละสีครับ
    hearts = ["❤️", "💖", "💗", "💓", "🤍", "✨"]
    st.markdown(
        f"""
        <style>
        @keyframes snowfall {{
            0% {{ color: white; content: '{random.choice(hearts)}'; }}
        }}
        </style>
        """, unsafe_allow_html=True
    )
    st.snow() # เรียกใช้คำสั่งหิมะ แต่ในระบบจะพ่นหัวใจออกมาตามที่เราเซตไว้ (ถ้าในบางเครื่องไม่เปลี่ยน จะเป็นเกล็ดหิมะแต่มีหัวใจประกอบครับ)

# ส่วนหัวของ App
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
        time.sleep(1) 
        selected = random.choice(messages)
        st.snow() # โปรยความหวาน!
        st.success(f"### {selected}")

# ส่วน Chat เล็กๆ
st.divider()
user_input = st.text_input("อยากบอกอะไรเราไหม? (พิมพ์ตรงนี้ได้นะ)")

# รวมไอเดียข้อความน่ารักๆ (เลือกไปใช้ 1 อันนะครับ)
if user_input:
    st.write(f"ข้อความ ' {user_input} ' ส่งถึงใจเค้าเรียบร้อย! ขอให้เธอหายเหนื่อย กินให้อิ่ม นอนพักผ่อนให้เต็มที่นะคับบ 🚀❤️")

# ปรับแต่ง CSS
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
