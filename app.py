import streamlit as st
import google.generativeai as genai

def nacti_znalosti():
    try:
        with open("znalosti.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Znalosti o BIP FM VŠE nenalezeny. Odpovídej obecně."

# 1. KONFIGURACE
st.set_page_config(page_title="VŠE BIP | Asistent", page_icon="💖", layout="centered")

# INICIALIZACE HISTORIE (Tohle tam chybělo a způsobovalo chybu!)
if "messages" not in st.session_state:
    st.session_state.messages = []

# NUKLEÁRNÍ CSS - TOTÁLNÍ ELIMINACE BÍLÉ A NEON CHAT
st.markdown("""
    <style>
    :root {
        --vse-pink: #d42273;
        --bg-dark: #0e1117;
    }

    .stApp, [data-testid="stAppViewContainer"] {
        background-color: var(--bg-dark) !important;
    }

    [data-testid="stBottom"], 
    [data-testid="stBottomBlockContainer"],
    .st-emotion-cache-1835tfv, 
    .st-emotion-cache-1v09fsh,
    .st-emotion-cache-1c7n2ri,
    .stChatInputContainer,
    footer {
        background-color: var(--bg-dark) !important;
        background: var(--bg-dark) !important;
        border: none !important;
        box-shadow: none !important;
    }

    div[data-testid="stChatInput"] {
        background-color: #050505 !important;
        border: 2px solid var(--vse-pink) !important;
        border-radius: 20px !important;
        box-shadow: 0 0 30px rgba(212, 34, 115, 0.6) !important;
        padding: 8px !important;
    }

    div[data-testid="stChatInput"] textarea {
        color: white !important;
        -webkit-text-fill-color: white !important;
    }

    div[data-testid="stChatInput"] textarea::placeholder {
        color: var(--vse-pink) !important;
        -webkit-text-fill-color: var(--vse-pink) !important;
        opacity: 1 !important;
    }

    [data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(212, 34, 115, 0.1) !important;
        border-radius: 20px !important;
    }

    .doc-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(212, 34, 115, 0.2);
        border-radius: 22px;
        padding: 22px;
        margin-bottom: 15px;
        height: 160px;
        transition: 0.4s ease-in-out;
    }
    .doc-card:hover {
        transform: translateY(-8px);
        border-color: var(--vse-pink);
        box-shadow: 0 15px 45px rgba(212, 34, 115, 0.4);
    }

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
        display: flex !important;
        justify-content: center !important;
    }
    .stButton>button:hover, .stLinkButton > a:hover {
        background: var(--vse-pink) !important;
        box-shadow: 0 0 40px rgba(212, 34, 115, 0.8) !important;
        color: white !important;
    }

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

    #MainMenu, header {visibility: hidden;}
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
st.markdown("<p style='text-align: center; opacity: 0.8; font-size: 1.2rem; margin-top: -15px;'>Chytrý pomocník pro studenty FM VŠE </p>", unsafe_allow_html=True)
st.write("")

# 3. MANUÁL
st.link_button("📂 OTEVŘÍT KOMPLETNÍ MANUÁL", "https://vsebip.my.canva.site/")

st.write("---")

# 4. ADMINISTRATIVNÍ KARTY (Základní definice)
st.subheader("📋 Administrativní kroky")
dokumenty = [
    ("📄 Dopis o přijetí", "Oficiální potvrzení od zahraniční univerzity, že tě přijali ke krátkodobému studiu."),
    ("✍️ Learning Agreement", "Smlouva o předmětech, které budeš studovat v zahraničí a které ti budou uznány."),
    ("🚆 Cestovní doklady", "Prokázání cesty na místo pobytu a zpět (letenky, jízdenky) nahrané v jednom PDF."),
    ("📜 Účastnická smlouva", "Hlavní dokument o tvém výjezdu, který podepisuješ s fakultou kvůli stipendiu."),
    ("🏦 Bankovní spojení", "Zadání tvého bankovního účtu do systému InSIS pro vyplacení finanční podpory."),
    ("🚨 Emergency Contact", "Kontaktní údaje na osobu blízkou pro případ nouze během tvého pobytu v zahraničí.")
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
st.subheader("🤖 Smart Konzultant")

# 6. SAMOTNÝ CHAT A AI
try:
    KLIC = st.secrets["GOOGLE_API_KEY"].strip()
    genai.configure(api_key=KLIC)
    
    # Model 2.5 Flash, který ti už prokazatelně fungoval
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Zobrazení historie zpráv
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Vstup od uživatele
    if prompt := st.chat_input("Zeptej se na cokoliv ohledně tvého výjezdu..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            kontext = nacti_znalosti()
            full_prompt = f"Jsi BIP asistent FM VŠE. Odpovídej stručně a v dark-cyber stylu. Znalosti: {kontext}\n\nOtázka: {prompt}"
            
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    st.error(f"AI se právě restartuje. (Chyba: {e})")




























