import streamlit as st
import google.generativeai as genai

# 1. NASTAVENÍ STRÁNKY
st.set_page_config(page_title="VŠE BIP Asistent", page_icon="🎓", layout="centered")

# 2. CUSTOM CSS (Tady se děje to kouzlo s designem)
st.markdown("""
    <style>
    /* Hlavní barva aplikace (růžová z loga) */
    :root {
        --vse-pink: #d42273; 
    }
    
    /* Odstranění horní linky a menu pro čistý vzhled */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Úprava tlačítek */
    .stButton>button {
        border-radius: 12px;
        border: 1px solid var(--vse-pink);
        background-color: transparent;
        color: white;
        transition: all 0.3s ease;
        font-weight: 500;
        padding: 10px 20px;
    }
    
    .stButton>button:hover {
        background-color: var(--vse-pink);
        color: white;
        border-color: var(--vse-pink);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(212, 34, 115, 0.3);
    }

    /* Styl pro informační boxy */
    .stAlert {
        border-radius: 15px;
        border: none;
        background-color: rgba(212, 34, 115, 0.1);
        border-left: 5px solid var(--vse-pink);
    }
    
    /* Úprava nadpisů */
    h1 {
        font-weight: 800;
        background: -webkit-linear-gradient(#fff, #d42273);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGO (vycentrované)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", width=400)
    except:
        st.write("⚠️ Logo nenalezeno.")

st.title("VŠE BIP: Smart Asistent")
st.markdown("Vítejte v interaktivním průvodci pro výjezdy BIP. Vše na jednom místě.")

# Hlavní akční tlačítko
st.link_button(
    "📖 OTEVŘÍT VIZUÁLNÍ MANUÁL (CANVA)", 
    "https://vsebip.my.canva.site/", 
    width='stretch'
)

st.write("---")

# 4. INTERAKTIVNÍ CHECKLIST
st.subheader("⚡ Rychlé instrukce k dokumentům")

dokumenty = {
    "📄 Dopis o přijetí": "Potvrzení od zahraniční školy, že tě oficiálně berou na pobyt.",
    "✍️ Learning Agreement": "Smlouva o tom, co budeš v cizině studovat a jak se ti to uzná na VŠE.",
    "🚆 Jízdenky / Letenky": "Doklady o dopravě tam i zpět nahrané v jednom PDF souboru.",
    "🏦 Bankovní spojení": "V InSIS zadej číslo účtu s účelem 'stipendium na zahr. výjezdy'.",
    "🚨 Emergency Contact": "Kontakt na blízkou osobu, který vyplňuješ do externího formuláře.",
    "📜 Účastnická smlouva": "Klíčový dokument k výplatě grantu – podepsat a odevzdat originál."
}

col1, col2 = st.columns(2)
items = list(dokumenty.items())

for i in range(len(items)):
    label, info = items[i]
    with (col1 if i % 2 == 0 else col2):
        if st.button(label, width='stretch'):
            st.info(f"**INFO:** {info}")

st.write("---")

# 5. CHAT ASISTENT
st.subheader("🤖 Smart Chat")

try:
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
    st.error(f"⚠️ Asistent je dočasně mimo provoz: {e}")







