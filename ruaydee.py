import os
import random
import pandas as pd
import streamlit as st

# ==========================================
# 1. การตั้งค่าหน้าเว็บ RUAYDEE v2.0 (Cute Edition)
# ==========================================
st.set_page_config(
    page_title="RUAYDEE v2.0 - นำโชคความรวยกับน้อนๆ 💖", 
    page_icon="✨", 
    layout="centered"
)

# ตกแต่ง CSS ให้มีความน่ารัก พาสเทล มีความโค้งมนและเอฟเฟกต์ดุ๊กดิ๊ก
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600&display=swap');
    * { font-family: 'Kanit', sans-serif; }
    
    /* พื้นหลังพาสเทลไล่เฉดสีสุดน่ารัก */
    .stApp {
        background: linear-gradient(135deg, #ffe5ec 0%, #f0e6ff 50%, #e8f0fe 100%);
        color: #4a4a4a;
    }
    
    /* การ์ดหลักและเดสก์ท็อปไอเทม */
    .fortune-card {
        background: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 24px;
        box-shadow: 0 10px 25px rgba(244, 143, 177, 0.2);
        border: 3px solid #ffb7b2;
        text-align: center;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    
    /* สไตล์ตัวเลขนำโชคแบบนุ่มฟู */
    .lucky-number {
        font-size: 90px;
        font-weight: bold;
        color: #ff7096;
        text-shadow: 3px 3px 0px #ffcbd5;
        margin: 15px 0;
        animation: bounce 1s infinite alternate;
    }
    
    /* อนิเมชันเด้งดุ๊กดิ๊กสำหรับตัวเลข */
    @keyframes bounce {
        from { transform: translateY(0); }
        to { transform: translateY(-10px); }
    }
    
    /* ปุ่มกดสไตล์ลูกกวาด */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #ff9aa2 0%, #ffb7b2 100%) !important;
        color: white !important;
        border: 2px solid #ffb7b2 !important;
        border-radius: 15px !important;
        height: 55px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 10px rgba(255, 154, 162, 0.4) !important;
        transition: all 0.2s ease-in-out !important;
    }
    
    /* เอฟเฟกต์ตอนเอาเมาส์ไปชี้ปุ่ม */
    .stButton>button:hover {
        transform: scale(1.03) !important;
        background: linear-gradient(90deg, #ffb7b2 0%, #ff9aa2 100%) !important;
        box-shadow: 0 6px 15px rgba(255, 154, 162, 0.6) !important;
    }
    
    /* สไตล์ตัวการ์ตูนดุ๊กดิ๊ก */
    .character-box {
        font-size: 50px;
        margin-bottom: -10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. คัมภีร์ข้อมูลสถิติหวยตัวเต็มจากไฟล์ของพี่ (ฝังแบบพรีเมียม) 👑
# ==========================================
@st.cache_data
def load_data():
    try:
        # ดึงข้อมูลสถิติเลขท้าย 2 ตัวทั้งหมดจากไฟล์จริงของพี่มาใส่ไว้ตรงนี้เลยค่ะ
        all_numbers = [
            "21", "61", "38", "32", "00", "59", "37", "94", "28", "46", "21", "89", "31", "42", "60", "17", "79", "90", "78", "79", 
            "43", "09", "61", "89", "85", "91", "14", "44", "66", "91", "30", "16", "62", "11", "90", "73", "99", "71", "55", "73", 
            "07", "92", "15", "06", "02", "14", "58", "47", "92", "61", "53", "14", "42", "83", "75", "50", "15", "18", "79", "02", 
            "36", "92", "38", "95", "57", "82", "83", "38", "95", "15", "97", "39", "73", "19", "05", "56", "18", "14", "45", "17", 
            "29", "70", "67", "79", "80", "40", "35", "53", "61", "38", "85", "59", "89", "20", "85", "22", "25", "42", "81", "97", 
            "06", "94", "98", "77", "22", "24", "64", "83", "53", "92", "88", "98", "57", "59", "90", "58", "93", "26", "40", "15", 
            "52", "32", "43", "86", "44", "94", "81", "25", "42", "14", "78", "92", "45", "78", "87", "49", "26", "87", "02", "95", 
            "98", "50", "33", "68", "09", "94", "51", "38", "26", "86", "25", "50", "74", "79", "35", "04", "22", "25", "84", "50", 
            "11", "39", "06", "02", "07", "22", "37", "96", "14", "79", "33", "93", "09", "57", "58", "05", "29", "86", "82", "91", 
            "22", "35", "44", "94", "79", "28", "52", "26", "05", "20", "46", "39", "73", "22", "12", "56", "35", "52", "95", "01", 
            "35", "79", "08", "69", "62", "45", "22", "25", "29", "84", "04", "40", "35", "95", "44", "38", "28", "27", "79", "48", 
            "52", "94", "40", "25", "11", "90", "09", "45", "63", "32", "92", "33", "68", "02", "48", "94", "86", "44", "79", "95", 
            "26", "52", "20", "18", "80", "14", "63", "35", "79", "02", "95", "01", "28", "16", "67", "62", "51", "88", "46", "05", 
            "85", "44", "01", "96", "27", "55", "23", "49", "24", "09", "43", "59", "42", "02", "66", "11", "64", "10", "34", "68", 
            "73", "81", "12", "00"
        ]
        df = pd.DataFrame({"number": all_numbers})
        return df, "คัมภีร์เวทมนตร์ตัวเต็มย้อนหลัง 15 ปี 📜✨"
    except:
        return None, None

df, file_used = load_data()

# ==========================================
# 3. การแสดงผล UI (Cute Theme)
# ==========================================

st.markdown(
    """
    <div class="fortune-card">
        <div class="character-box">🐰✨🐻</div>
        <h1 style="color:#ff7096; margin-top:10px;">RUAYDEE v2.0</h1>
        <p style="color:#7a7a7a; font-size:16px;">ให้น้อนๆ ช่วยสุ่มเลขนำโชคสุดปังให้พี่ๆ น้าาา~ 💕</p>
    </div>
    """, 
    unsafe_allow_html=True
)

if df is not None:
    st.toast(f"🐣 เปิดคัมภีร์สำเร็จ: {file_used}", icon="✅")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # ปุ่มที่ 1: สุ่มพลังดวงดาว
        if st.button("🐱✨ สุ่มพลังดวงดาว"):
            lucky = f"{random.randint(0, 99):02d}"
            st.balloons()
            st.markdown(
                f"""
                <div class="fortune-card">
                    <div style="font-size: 40px;">🐱🚀</div>
                    <h3 style="color:#ff9aa2;">เลขดวงดาวน้อนแมว</h3>
                    <div class="lucky-number">{lucky}</div>
                    <p style="color:#a899e6; font-size:14px;">ขอให้พลังแห่งดวงดาวสถิตอยู่กับเจ้ามนุษย์!</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
    with col2:
        # ปุ่มที่ 2: สแกนสถิติเด่น (ดึงสถิติตัวฮิตจากไฟล์พี่จริงๆ มาสุ่มให้)
        if st.button("🐻📊 สแกนสถิติสุดเจ๋ง"):
            # หาเลขที่ออกบ่อยที่สุด 15 อันดับแรกจากไฟล์ที่พี่ให้มา
            top_nums = df["number"].value_counts().head(15).index.tolist()
            lucky = random.choice(top_nums)
            st.snow()
            st.markdown(
                f"""
                <div class="fortune-card">
                    <div style="font-size: 40px;">🐻👓</div>
                    <h3 style="color:#b5ead7;">เลขสถิติสุดแม่น</h3>
                    <div class="lucky-number">{lucky}</div>
                    <p style="color:#74c69d; font-size:14px;">น้อนหมีคัดเลขเด็ดที่ออกบ่อยสุดมาให้เลยค๊าฟ!</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
else:
    st.error("😭 แงงง ระบบโหลดข้อมูลภายในขัดข้อง")