import streamlit as st
import google.generativeai as genai
from datetime import datetime

# 1. KONFIGURACE A DESIGN (Cyber-VŠE Pink Edition)
st.set_page_config(page_title="VŠE BIP | Smart Assistant", page_icon="💖", layout="centered")

# TOTÁLNÍ DESIGN UPGRADE
st.markdown("""
    <style>
    :root {
        --vse-pink: #d42273;
        --bg-dark: #0e1117;
    }

    /* Vynucení Dark Mode a barev */
    .stApp {
        background-color: var(--bg-dark);
        color: white;
    }

    /* PULZUJÍCÍ AI MOZEK (Aura kolem chatu) */
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(212, 34, 115, 0.4); }
        70% { box-shadow: 0 0 0 15px rgba(212, 34, 115, 0); }
        100% { box-shadow: 0 0 0 0 rgba(212, 34, 115, 0); }
    }

    /* GLASS CARDS 2.0 (Karty s hloubkou) */
    .doc-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(212, 34, 115, 0.2);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 15px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .doc-card:hover {
        transform: translateY(-8px) scale(1.02);
        background: rgba(212, 34, 115, 0.08);
        border-color: var(--vse-pink);
        box-shadow: 0 15px 35px rgba(212, 34, 115, 0.3);
    }

    /* EPIC NEONOVÁ TLAČÍTKA */
    .stButton>button, .stLinkButton > a {
        width: 100% !important;
        border-radius: 50px !important;
        border: 2px solid var(--vse-pink) !important;
        background: rgba(212, 34, 115, 0.1) !important;
        color: white !important;
        font-weight: 800 !important;
        letter-spacing: 1px !important;
        padding: 15px !important;
        text-transform: uppercase;
        transition: 0.3s;
        text-decoration: none !important;
        display: flex !important;
        justify-content: center !important;
    }
    .stButton>button:hover, .stLinkButton > a:hover {
        background: var(--vse-pink) !important;
        box-shadow: 0 0 40px rgba(212, 34, 115, 0.8) !important;
        color: white !important;
    }

    /* ODSTRANĚNÍ STREAMLIT LIŠTY */
    #MainMenu, footer, header {visibility: hidden;}

    /* ANIMOVANÝ NADPIS */
    .super-title {
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(to right, #fff, var(--vse-pink), #fff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200% auto;
        animation: shine 3s linear infinite;
    }
    @keyframes shine { to { background-position: 200% center; } }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGO
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", width=450) # Tady už víme, že logo.png je správně
    except:
        st.write("⚠️ Logo missing")

st.markdown('<h1 class="super-title">BIP GURU 2.0</h1>', unsafe_allow_html=True)

# 3. LIVE ODPOČET (COUNTDOWN)
# Deadline pro rok 2026: 25. února v 15:00
deadline = datetime(2026, 2, 25, 15, 0, 0)
now = datetime.now()
diff = deadline - now

if diff.total_seconds() > 0:
    st.markdown(f"""
        <div style="text-align:center; padding:15px; border:2px solid var(--vse-pink); border-radius:20px; margin: 25px 0; background: rgba(0,0,0,0.3);">
            <p style="margin:0; font-size: 0.8rem; opacity: 0.6; letter-spacing: 3px;">DEADLINE ODEVZDÁNÍ V INSIS:</p>
            <p style="margin:0; font-size: 2.2rem; font-weight: 900; color: white;">
                {diff.days}d : {diff.seconds//3600}h : {(diff.seconds//60)%60}m
            </p>
        </div>
    """, unsafe_allow_html=True)

# 4. ROADMAP (Vizuální cesta studenta)
st.write("### 📍 Tvoje cesta k výjezdu")
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; padding: 0 20px;">
        <div style="text-align:center; flex:1;"><span style="font-size:20px;">🔵</span><br><small style="opacity:0.7;">Nominace</small></div>
        <div style="height:2px; background:var(--vse-pink); flex:1; margin-bottom:15px;"></div>
        <div style="text-align:center; flex:1;"><span style="font-size:25px; filter: drop-shadow(0 0 10px var(--vse-pink));">💗</span><br><b style="color:var(--vse-pink);">Checklist</b></div>
        <div style="height:2px; background:rgba(255,255,255,0.2); flex:1; margin-bottom:15px;"></div>
        <div style="text-align:center; flex:1; opacity:0.3;"><span style="font-size:20px;">⚪</span><br><small>Výjezd</small></div>
    </div>
""", unsafe_allow_html=True)

# 5. DOKUMENTY (Elegantní Glass Cards)
st.write("### 📂 Co musíš mít v pořádku")
dokumenty = [
    ("📄 Dopis o přijetí", "Tvůj lístek do světa. Nahraj ho hned, jak ho dostaneš."),
    ("✍️ Learning Agreement", "Smlouva o předmětech. Políčko 'Podmínky' nechte PRÁZDNÉ."),
    ("🚆 Doklady o dopravě", "Jízdenky/letenky (tam i zpět) v jednom PDF souboru."),
    ("📜 Účastnická smlouva", "Bez podepsaného originálu nedojde stipendium. Nečekej!")
]

col1, col2 = st.columns(2)
for i, (title, desc) in enumerate(dokumenty):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
            <div class="doc-card">
                <div style="color:var(--vse-pink); font-weight:800; font-size:1.1rem; margin-bottom:5px;">{title}</div>
                <div style="font-size: 0.9rem; opacity: 0.8; color: white;">{desc}</div>
            </div>
        """, unsafe_allow_html=True)

# 6. CANVA LINK & CELEBRATION
st.write("")
st.link_button("📂 OTEVŘÍT KOMPLETNÍ MANUÁL (CANVA)", "https://vsebip.my.canva.site/")

if st.button("✨ MÁM VŠECHNO HOTOVO!"):
    st.balloons()
    st.snow()
    st.success("Geniální! Teď už se jen těš na letiště. 🌍✈️")

# 7. AI SMART CHAT (S pulzující aurou)
st.write("---")
st.subheader("🤖 Smart BIP Konzultant")
st.markdown('<div style="animation: pulse 2s infinite; border-radius:15px; padding:2px;">', unsafe_allow_html=True)

try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    def nacti_znalosti():
        with open("znalosti.txt", "r", encoding="utf-8") as f:
            return f.read()

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=nacti_znalosti() + " Jsi BIP GURU. Jsi vtipný, profesionální a mírně sarkastický, ale vždy nápomocný."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Zeptej se svého GURU na cokoliv..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
except Exception as e:
    st.error("GURU právě medituje, zkuste to za vteřinku.")
st.markdown('</div>', unsafe_allow_html=True)





