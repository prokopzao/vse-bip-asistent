import streamlit as st
import google.generativeai as genai

# 1. KONFIGURACE A DESIGN
st.set_page_config(page_title="VŠE BIP | Asistent", page_icon="💖", layout="centered")

# ULTIMÁTNÍ CSS PRO ROK 2026 (Dark & Pink)
st.markdown("""
    <style>
    :root {
        --vse-pink: #d42273;
        --bg-dark: #0e1117;
        --glass: rgba(255, 255, 255, 0.05);
    }

    /* Základní temné nastavení */
    .stApp {
        background-color: var(--bg-dark);
        color: white;
    }

    /* DARK CHAT FIX - Aby text a pole byly temné a čitelné */
    [data-testid="stChatMessage"] {
        background-color: rgba(20, 22, 28, 0.8) !important;
        border: 1px solid rgba(212, 34, 115, 0.2) !important;
        border-radius: 15px !important;
        color: white !important;
    }
    
    [data-testid="stChatInput"] {
        background-color: #050505 !important;
        border: 1px solid var(--vse-pink) !important;
        border-radius: 15px !important;
    }
    
    [data-testid="stChatInput"] textarea {
        color: white !important;
    }

    /* GLASS CARDS - Styl karet pro dokumenty */
    .doc-card {
        background: var(--glass);
        border: 1px solid rgba(212, 34, 115, 0.3);
        border-radius: 20px;
        padding: 22px;
        margin-bottom: 15px;
        height: 160px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .doc-card:hover {
        transform: translateY(-8px);
        border-color: var(--vse-pink);
        background: rgba(212, 34, 115, 0.05);
        box-shadow: 0 15px 40px rgba(212, 34, 115, 0.3);
    }

    /* EPIC NEONOVÁ TLAČÍTKA */
    .stButton>button, .stLinkButton > a {
        width: 100% !important;
        border-radius: 50px !important;
        border: 2px solid var(--vse-pink) !important;
        background: rgba(212, 34, 115, 0.1) !important;
        color: white !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        padding: 18px !important;
        transition: 0.3s !important;
        text-decoration: none !important;
    }
    .stButton>button:hover, .stLinkButton > a:hover {
        background: var(--vse-pink) !important;
        box-shadow: 0 0 35px rgba(212, 34, 115, 0.6) !important;
        color: white !important;
    }

    /* ANIMOVANÝ NADPIS BIP ASISTENT */
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

    /* SKRYTÍ HEADERU PRO ČISTÝ VZHLED */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. LOGO (Tvoje růžová verze)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", width=450)
    except:
        st.write("⚠️ Soubor logo.png nenalezen.")

st.markdown('<h1 class="super-title">BIP ASISTENT</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.7; font-size: 1.2rem; margin-top: -10px;'>Prémiový průvodce pro studenty FM VŠE</p>", unsafe_allow_html=True)
st.write("")

# 3. OPRAVENÉ TLAČÍTKO MANUÁL (Tady byla ta chyba)
st.link_button("📂 OTEVŘÍT KOMPLETNÍ MANUÁL (CANVA)", "https://vsebip.my.canva.site/")

st.write("---")

# 4. KOMPLETNÍ DOKUMENTACE (Všechny karty)
st.subheader("📋 Administrativní Milestone")
dokumenty = [
    ("📄 Dopis o přijetí", "Tvůj lístek do světa. Nahraj ho v PDF do InSIS k danému výjezdu."),
    ("✍️ Learning Agreement", "Smlouva o předmětech. Políčko 'Podmínky k uznání' nechte PRÁZDNÉ!"),
    ("🚆 Cestovní doklady", "Všechny jízdenky a letenky (tam i zpět) nahrané jako jeden PDF dokument."),
    ("📜 Účastnická smlouva", "Nejdůležitější dokument. Podepiš originál u koordinátorky na fakultě."),
    ("🏦 Bankovní spojení", "V InSIS přidej účet s účelem 'stipendium na zahraniční výjezdy'."),
    ("🚨 Emergency Contact", "Povinný formulář pro krizové situace. Odkaz najdeš v e-mailu od OZS.")
]

col1, col2 = st.columns(2)
for i, (title, desc) in enumerate(dokumenty):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
            <div class="doc-card">
                <div style="color:var(--vse-pink); font-weight:800; font-size:1.15rem; margin-bottom:8px;">{title}</div>
                <div style="font-size: 0.95rem; line-height: 1.5; opacity: 0.9;">{desc}</div>
            </div>
        """, unsafe_allow_html=True)

# 5. CELEBRACE
st.write("")
if st.button("✨ MÁM VŠECHNO HOTOVO!"):
    st.balloons()
    st.snow()
    st.success("Fantastické! Tvůj výjezd je za dveřmi. Užij si BIP! 🌍")

st.write("---")

# 6. AI ASISTENT (Opravený model a dark theme)
st.subheader("🤖 Smart Konzultant")

try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    def nacti_znalosti():
        with open("znalosti.txt", "r", encoding="utf-8") as f:
            return f.read()

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=nacti_znalosti() + " Jsi BIP ASISTENT. Jsi profesionální, hrdý na FM VŠE a studentům pomáháš s administrativou."
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
    st.error("AI se právě nabíjí, zkuste to za vteřinku.")





