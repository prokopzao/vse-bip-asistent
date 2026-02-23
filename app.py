import streamlit as st
import google.generativeai as genai

# 1. KONFIGURACE
st.set_page_config(page_title="VŠE BIP | Asistent", page_icon="💖", layout="centered")

# NEON OVERDRIVE CSS
st.markdown("""
    <style>
    :root {
        --vse-pink: #d42273;
        --bg-dark: #0e1117;
    }

    /* Celé pozadí */
    .stApp {
        background-color: var(--bg-dark);
        color: white;
    }

    /* TOTÁLNÍ ZABIJÁK BÍLÉHO PRUHU */
    div[data-testid="stBottom"] {
        background-color: transparent !important;
        background: transparent !important;
    }
    
    /* NEONOVÝ CHAT BOX */
    div[data-testid="stChatInput"] {
        background-color: rgba(20, 22, 28, 0.9) !important;
        border: 2px solid var(--vse-pink) !important;
        border-radius: 25px !important;
        padding: 8px !important;
        box-shadow: 0 0 20px rgba(212, 34, 115, 0.4) !important;
    }

    /* Fix textu v chatu */
    div[data-testid="stChatInput"] textarea {
        color: white !important;
        caret-color: var(--vse-pink) !important;
    }

    /* Přebarvení placeholderu (Zeptej se...) */
    div[data-testid="stChatInput"] textarea::placeholder {
        color: rgba(212, 34, 115, 0.6) !important;
    }

    /* STYL ZPRÁV */
    [data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(212, 34, 115, 0.1) !important;
        border-radius: 20px !important;
    }

    /* GLASS CARDS DOKUMENTY */
    .doc-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(212, 34, 115, 0.2);
        border-radius: 22px;
        padding: 22px;
        margin-bottom: 15px;
        height: 175px;
        transition: 0.4s ease-in-out;
    }
    .doc-card:hover {
        transform: translateY(-10px);
        border-color: var(--vse-pink);
        background: rgba(212, 34, 115, 0.06);
        box-shadow: 0 15px 45px rgba(212, 34, 115, 0.3);
    }

    /* TLAČÍTKA */
    .stButton>button, .stLinkButton > a {
        width: 100% !important;
        border-radius: 50px !important;
        border: 2px solid var(--vse-pink) !important;
        background: rgba(212, 34, 115, 0.15) !important;
        color: white !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        padding: 18px !important;
        letter-spacing: 1.5px;
        transition: 0.3s !important;
    }
    .stButton>button:hover, .stLinkButton > a:hover {
        background: var(--vse-pink) !important;
        box-shadow: 0 0 40px rgba(212, 34, 115, 0.7) !important;
    }

    /* NADPIS */
    .super-title {
        font-size: 3.8rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #fff, var(--vse-pink), #fff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200% auto;
        animation: shine 4s linear infinite;
    }
    @keyframes shine { to { background-position: 200% center; } }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. LOGO
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", width=450)
    except:
        st.write("⚠️ Logo missing")

st.markdown('<h1 class="super-title">BIP ASISTENT</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.7; font-size: 1.2rem; margin-top: -15px;'>Smart Hub pro studenty FM VŠE</p>", unsafe_allow_html=True)
st.write("")

# 3. MANUÁL
st.link_button("📂 OTEVŘÍT KOMPLETNÍ MANUÁL (CANVA)", "https://vsebip.my.canva.site/")

st.write("---")

# 4. ADMINISTRATIVNÍ KARTY (Všech 6)
st.subheader("📋 Administrativní Milestone")
dokumenty = [
    ("📄 Dopis o přijetí", "Nahraj v PDF do InSIS k danému výjezdu."),
    ("✍️ Learning Agreement", "Smlouva o předmětech. Pole 'Podmínky k uznání' nechte PRÁZDNÉ!"),
    ("🚆 Cestovní doklady", "Všechny jízdenky a letenky (tam i zpět) v jednom PDF."),
    ("📜 Účastnická smlouva", "Podepiš originál u koordinátorky přímo na fakultě."),
    ("🏦 Bankovní spojení", "V InSIS přidej účet s účelem 'stipendium na zahr. výjezdy'."),
    ("🚨 Emergency Contact", "Povinný formulář pro krizové situace. Link máš v e-mailu.")
]

col1, col2 = st.columns(2)
for i, (title, desc) in enumerate(dokumenty):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
            <div class="doc-card">
                <div style="color:var(--vse-pink); font-weight:800; font-size:1.15rem; margin-bottom:10px;">{title}</div>
                <div style="font-size: 0.95rem; line-height: 1.5; opacity: 0.9;">{desc}</div>
            </div>
        """, unsafe_allow_html=True)

# 5. CELEBRACE
st.write("")
if st.button("✨ MÁM VŠECHNO HOTOVO!"):
    st.balloons()
    st.snow()
    st.success("Geniální práce! Užij si svůj BIP výjezd! 🌍")

st.write("---")

# 6. AI ASISTENT (Neon Fix)
st.subheader("🤖 Smart Konzultant")

try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    def nacti_znalosti():
        with open("znalosti.txt", "r", encoding="utf-8") as f:
            return f.read()

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=nacti_znalosti() + " Jsi BIP ASISTENT. Pomáhej studentům FM VŠE profesionálně a v dark-cyber stylu."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Zeptej se na cokoliv ohledně tvého výjezdu..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
except Exception as e:
    st.error("AI se právě restartuje.")







