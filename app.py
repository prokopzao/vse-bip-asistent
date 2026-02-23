import streamlit as st
import google.generativeai as genai

# 1. KONFIGURACE
st.set_page_config(page_title="VŠE BIP | Asistent", page_icon="💖", layout="centered")

# NUKLEÁRNÍ CSS - TOTÁLNÍ TMA A NEONOVÁ ZÁŘ
st.markdown("""
    <style>
    :root {
        --vse-pink: #d42273;
        --bg-dark: #0e1117;
    }

    /* Celkové pozadí aplikace */
    .stApp {
        background-color: var(--bg-dark) !important;
    }

    /* !!! TERMINÁLNÍ FIX BÍLÉHO PRUHU !!! */
    /* Totální zčernání všech spodních vrstev, které už nám funguje */
    [data-testid="stBottom"], 
    [data-testid="stBottomBlockContainer"],
    .st-emotion-cache-1835tfv, 
    .st-emotion-cache-1v09fsh,
    .st-emotion-cache-1c7n2ri,
    footer {
        background-color: var(--bg-dark) !important;
        background: var(--bg-dark) !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* NEONOVÝ CHAT INPUT - Box s růžovou září */
    div[data-testid="stChatInput"] {
        background-color: #050505 !important;
        border: 2px solid var(--vse-pink) !important;
        border-radius: 20px !important;
        box-shadow: 0 0 30px rgba(212, 34, 115, 0.6) !important;
        padding: 8px !important;
    }

    /* TEXT V CHATU - Růžový placeholder a bílý psaný text */
    div[data-testid="stChatInput"] textarea {
        color: white !important;
        -webkit-text-fill-color: white !important;
    }

    div[data-testid="stChatInput"] textarea::placeholder {
        color: var(--vse-pink) !important;
        -webkit-text-fill-color: var(--vse-pink) !important;
        opacity: 1 !important;
    }

    /* STYL ZPRÁV */
    [data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(212, 34, 115, 0.1) !important;
        border-radius: 20px !important;
    }

    /* DOKUMENTAČNÍ KARTY */
    .doc-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(212, 34, 115, 0.2);
        border-radius: 22px;
        padding: 22px;
        margin-bottom: 15px;
        height: 180px;
        transition: 0.4s ease-in-out;
    }
    .doc-card:hover {
        transform: translateY(-8px);
        border-color: var(--vse-pink);
        box-shadow: 0 15px 45px rgba(212, 34, 115, 0.4);
    }

    /* TLAČÍTKA */
    .stButton>button, .stLinkButton > a {
        width: 100% !important;
        border-radius: 50px !important;
        border: 2px solid var(--vse-pink) !important;
        background: rgba(212, 34, 115, 0.1) !important;
        color: white !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        padding: 18px !important;
        letter-spacing: 2px;
        transition: 0.3s !important;
        text-decoration: none !important;
    }
    .stButton>button:hover, .stLinkButton > a:hover {
        background: var(--vse-pink) !important;
        box-shadow: 0 0 40px rgba(212, 34, 115, 0.8) !important;
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
        margin-bottom: 0px;
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
        st.write("⚠️ Nahraj logo.png")

st.markdown('<h1 class="super-title">BIP ASISTENT</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8; font-size: 1.2rem; margin-top: -15px;'>Smart Hub pro studenty FM VŠE</p>", unsafe_allow_html=True)
st.write("")

# 3. MANUÁL
st.link_button("📂 OTEVŘÍT KOMPLETNÍ MANUÁL (CANVA)", "https://vsebip.my.canva.site/")

st.write("---")

# 4. KARTY (Všech 6 kroků)
st.subheader("📋 Administrativní Milestone")
dokumenty = [
    ("📄 Dopis o přijetí", "Tvůj lístek do světa. Nahraj ho v PDF do InSIS k danému výjezdu."),
    ("✍️ Learning Agreement", "Smlouva o předmětech. Políčko 'Podmínky k uznání' nechte PRÁZDNÉ!"),
    ("🚆 Cestovní doklady", "Všechny jízdenky a letenky (tam i zpět) nahrané v jednom PDF."),
    ("📜 Účastnická smlouva", "Podepiš originál u koordinátorky přímo na fakultě."),
    ("🏦 Bankovní spojení", "V InSIS přidej účet s účelem 'stipendium na zahraniční výjezdy'."),
    ("🚨 Emergency Contact", "Povinný formulář pro krizové situace. Link máš v e-mailu od OZS.")
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

# 6. AI ASISTENT (Opravený model a API klíč)
st.subheader("🤖 Smart Konzultant")

try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY) # FIX: Velká písmena musí sedět!
    
    def nacti_znalosti():
        with open("znalosti.txt", "r", encoding="utf-8") as f:
            return f.read()

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=nacti_znalosti() + " Jsi BIP ASISTENT. Pomáhej studentům FM VŠE v dark-cyber stylu."
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
    # Pokud se stane chyba, vypíše se sem (pomůže nám to s laděním)
    st.error(f"AI se právě restartuje. (Chyba: {e})")







