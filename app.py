import streamlit as st
import google.generativeai as genai
import requests
from streamlit_lottie import st_lottie

# 1. FUNKCE PRO NAČÍTÁNÍ ANIMACÍ
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Odkaz na růžového cyberpunk robota (Lottie JSON)
lottie_ai = load_lottieurl("https://lottie.host/8e202534-7a32-475a-9b48-31628d09325c/k0pY2q0RzX.json")

def nacti_znalosti():
    try:
        with open("znalosti.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Znalosti o BIP FM VŠE nenalezeny. Odpovídej obecně."

# 2. KONFIGURACE A STYLY
st.set_page_config(page_title="VŠE BIP | Asistent", page_icon="💖", layout="centered")

if "messages" not in st.session_state:
    st.session_state.messages = []

# NUKLEÁRNÍ CSS (Včetně stylů pro animaci)
st.markdown("""
    <style>
    :root { --vse-pink: #d42273; --bg-dark: #0e1117; }
    .stApp { background-color: var(--bg-dark) !important; }
    .super-title {
        font-size: 3.5rem; font-weight: 900; text-align: center;
        background: linear-gradient(90deg, #fff, var(--vse-pink), #fff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-size: 200% auto; animation: shine 4s linear infinite;
    }
    @keyframes shine { to { background-position: 200% center; } }
    
    /* Schování Streamlit menu */
    #MainMenu, header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. VIZUÁLNÍ HLAVIČKA S ANIMACÍ
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if lottie_ai:
        st_lottie(lottie_ai, height=250, key="main_robot")
    else:
        st.write("⚠️ Animation failed to load")

st.markdown('<h1 class="super-title">BIP ASISTENT</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8; font-size: 1.2rem; margin-top: -10px;'>Vítej v budoucnosti výjezdů FM VŠE</p>", unsafe_allow_html=True)

st.write("---")

# 4. ADMINISTRATIVNÍ KARTY (Stručné definice)
dokumenty = [
    ("📄 Dopis o přijetí", "Lístek na tvůj výjezd – potvrzení od zahraniční školy."),
    ("✍️ Learning Agreement", "Smlouva o předmětech, které ti VŠE v zahraničí uzná."),
    ("🚆 Cestovní doklady", "Letenky a jízdenky nahrané v jednom PDF v InSIS."),
    ("📜 Účastnická smlouva", "Klíč k penězům – podepisuješ přímo na fakultě."),
    ("🏦 Bankovní spojení", "Tvé číslo účtu zadané v InSIS pro stipendium."),
    ("🚨 Emergency Contact", "Kontakt na blízkou osobu pro krizové situace.")
]

c1, c2 = st.columns(2)
for i, (title, desc) in enumerate(dokumenty):
    with (c1 if i % 2 == 0 else c2):
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.05); border: 1px solid var(--vse-pink); 
                        border-radius: 20px; padding: 20px; margin-bottom: 15px;">
                <div style="color: var(--vse-pink); font-weight: 800;">{title}</div>
                <div style="font-size: 0.9rem; opacity: 0.9;">{desc}</div>
            </div>
        """, unsafe_allow_html=True)

# 5. CHAT A AI LOGIKA
st.write("---")
st.subheader("🤖 Smart Konzultant")

try:
    KLIC = st.secrets["GOOGLE_API_KEY"].strip()
    genai.configure(api_key=KLIC)
    # Používáme tvůj ověřený model
    model = genai.GenerativeModel('models/gemini-flash-latest')

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Zeptej se na cokoliv ohledně BIP..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            kontext = nacti_znalosti()
            # Profesionální a lidský prompt
            full_prompt = f"""
            Jsi přátelský BIP asistent FM VŠE. Pomáhej studentům srozumitelně.
            Znalosti: {kontext}
            Otázka: {prompt}
            """
            
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    st.error(f"Chyba systému: {e}")































