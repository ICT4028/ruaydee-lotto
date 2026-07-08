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
# 2. ฟังก์ชันโหลดข้อมูลแบบดึงตรงจากหน้าเว็บ (ตัดปัญหาระบบหาไฟล์ไม่เจอ) 🌟
# ==========================================
@st.cache_data
def load_data():
    # แผนที่ 1: ดึงออนไลน์ผ่าน URL ตรงๆ จาก GitHub ของคุณเลย (ชัวร์สุด ไม่กลัวพาสเพี้ยน)
    try:
        github_url = "https://raw.githubusercontent.com/ict4028/ruaydee-lotto/main/to_lotto.csv"
        df = pd.read_csv(github_url)
        df = df.dropna(how='all')
        df.columns = ["date", "number"]
        df = df.dropna()
        df["number"] = df["number"].astype(float).astype(int).astype(str).str.zfill(2)
        return df, "GitHub URL (ดึงสำเร็จแว้ว)"
    except:
        pass

    # แผนที่ 2: ถ้าเน็ตล่ม ให้หาไฟล์ในเครื่องต่อ
    possible_files = ["to_lotto.csv", "to_lotto.xlsx"]
    for filename in possible_files:
        if os.path.exists(filename):
            try:
                if filename.endswith('.xlsx'):
                    df = pd.read_excel(filename, sheet_name=0)
                else:
                    df = pd.read_csv(filename)
                df = df.dropna(how='all')
                df.columns = ["date", "number"]
                df = df.dropna()
                df["number"] = df["number"].astype(float).astype(int).astype(str).str.zfill(2)
                return df, f"ไฟล์ในระบบ ({filename})"
            except:
                continue
        
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
        if st.button("🐻📊 สแกนสถิติสุดเจ๋ง"):
            top_nums = df["number"].value_counts().head(10).index.tolist()
            lucky = random.choice(top_nums)
            st.snow()
            st.markdown(
                f"""
                <div class="fortune-card">
                    <div style="font-size: 40px;">🐻👓</div>
                    <h3 style="color:#b5ead7;">เลขสถิติสุดแม่น</h3>
                    <div class="lucky-number">{lucky}</div>
                    <p style="color:#74c69d; font-size:14px;">น้อนหมีคำนวณมาแล้ว เลขนี้เด็ดสุดๆ!</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
else:
    st.error("😭 แงงง น้อนพยายามหาทุกทางแล้วก็ยังไม่เจอไฟล์ข้อมูลเลย")
    st.info("กรุณาตรวจสอบว่าใน GitHub มีไฟล์ชื่อ to_lotto.csv อยู่หน้าแรกสุดแล้วหรือยังนะน้าาา")