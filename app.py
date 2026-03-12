import streamlit as st
import random
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="พลังใจจากเรา", page_icon="❤️")

# ฟังก์ชันสำหรับสร้าง "พายุหัวใจ" คละสี (Red, Pink, White)
def heart_rain():
    # ลิสต์หัวใจที่คุณเลือกมา
    hearts = ["❤️", "💖", "💗", "💓", "🤍"]
    
    # สร้าง HTML/JS สำหรับทำเอฟเฟกต์หัวใจตก
    heart_js = f"""
    <div id="hearts-container"></div>
    <script>
    (function() {{
        const hearts = {hearts};
        function createHeart() {{
            const heart = document.createElement("div");
            heart.innerHTML = hearts[Math.floor(Math.random() * hearts.length)];
            heart.style.position = "fixed";
            heart.style.left = Math.random() * 100 + "vw";
            heart.style.top = "-20px";
            heart.style.fontSize = (Math.random() * 20 + 20) + "px";
            heart.style.animation = "fall " + (Math.random() * 3 + 2) + "s linear";
            heart.style.zIndex = "9999";
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 5000);
        }}
        const style = document.createElement('style');
        style.innerHTML = `@keyframes fall {{ to {{ transform: translateY(105vh); }} }}`;
        document.head.appendChild(style);
        
        // ปล่อยหัวใจออกมา 50 ดวง
        for(let i=0; i<50; i++) {{
            setTimeout(createHeart, i * 100);
        }}
    }})();
    </script>
    """
    st.components.v1.html(heart_js, height=0)

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
        heart_rain()  # เรียกฟังก์ชันหัวใจใหม่ที่แก้แล้ว
        st.success(f"### {selected}")

# ส่วน Chat เล็กๆ
st.divider()
user_input = st.text_input("อยากบอกอะไรเราไหม? (พิมพ์ตรงนี้ได้นะ)")

if user_input:
    st.write(f"ข้อความ ' {user_input} ' ส่งถึงใจเค้าเรียบร้อย! ขอให้เธอหายเหนื่อย กินให้อิ่ม นอนพักผ่อนให้เต็มที่นะคับบ 🚀❤️")

# ปรับแต่ง CSS
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
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)
