import streamlit as st
import google.generativeai as genai

# 1. KONFIGURACE A DESIGN
st.set_page_config(page_title="VŠE BIP Smart Assistant", page_icon="✨", layout="centered")

# INSANE CSS UPGRADE
st.markdown("""
    <style>
    /* Základní barvy - VŠE Pink a Dark Theme */
    :root {
        --vse-pink: #d42273;
        --bg-dark: #0e1117;
        --glass-bg: rgba(255, 255, 255, 0.05);
    }

    /* Vynucení tmavého pozadí pro celou aplikaci */
    .stApp {
        background-color: var(--bg-dark);
        color: white;
    }

    /* Úprava tlačítek - Viditelný text a neonový glow */
    .stButton>button {
        width: 100% !important;
        border-radius: 15px !important;
        border: 2px solid var(--vse-pink) !important;
        background-color: var(--glass-bg) !important;
        color: white !important; /* Fix pro viditelnost textu */
        font-weight: 600 !important;
        font-size: 16px !important;
        padding: 15px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton>button:hover {
        background-color: var(--vse-pink) !important;
        box-shadow: 0 0 20px rgba(212, 34, 115, 0.6) !important;
        transform: scale(1.02) !important;
    }

    /* Styl pro Info boxy - Glassmorphism efekt */
    .stAlert {
        background: rgba(212, 34, 115, 0.1) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 34, 115, 0.3) !important;
        border-radius: 20px !important;
        color: white !important;
    }

    /* Skrytí standardních prvků Streamlitu */
    #MainMenu, footer, header {visibility: hidden;}

    /* Animovaný nadpis s gradientem */
    .main-title {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ffffff, var(--vse-pink));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGO (vycentrované s jemným stínem)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", width=450)
    except:
        st.write("⚠️ Logo missing")

st.markdown('<h1 class="main-title">BIP Smart Guide</h1>', unsafe_allow_html=True)
st.markdown("---")

# 4. HLAVNÍ AKCE
st.link_button(
    "📂 OTEVŘÍT KOMPLETNÍ MANUÁL (CANVA)", 
    "https://vsebip.my.canva.site/", 
    width='stretch'
)

st.write("") # Mezera

# 5. CHECKLIST - Teď s viditelnými popisky
st.subheader("📋 Administrativní Milestone")

dokumenty = {
    "📄 Dopis o přijetí": "Oficiální potvrzení o přijetí zahraniční školou.",
    "✍️ Learning Agreement": "Smlouva o předmětech (nechte pole 'Podmínky uznání' prázdné!).",
    "🚆 Cestovní doklady": "Všechny jízdenky/letenky nahrané v jednom PDF souboru.",
    "🏦 Bankovní účet": "Zadej v InSIS s účelem 'stipendium na výjezdy'.",
    "🚨 Emergency Contact": "Povinný externí formulář (viz e-mail od OZS).",
    "📜 Smlouva o grantu": "Podepsat a doručit originál pro výplatu peněz."
}

col1, col2 = st.columns(2)
items = list(dokumenty.items())

for i in range(len(items)):
    label, info = items[i]
    with (col1 if i % 2 == 0 else col2):
        if st.button(label, width='stretch'):
            st.info(info)

st.write("---")

# 6. INTELEKTUÁLNÍ ASISTENT (Gemini 1.5)
st.subheader("🤖 AI Konzultant")

try:
    # Použití klíče ze Secrets
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    def nacti_znalosti():
        with open("znalosti.txt", "r", encoding="utf-8") as f:
            return f.read()

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash-latest',
        system_instruction=nacti_znalosti()
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat UI
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Zeptej se na cokoliv ohledně BIP..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
except Exception as e:
    st.error(f"Systémová chyba: {e}")





