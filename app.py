import streamlit as st
import google.generativeai as genai

# 1. NASTAVENÍ STRÁNKY
st.set_page_config(page_title="VŠE BIP Asistent", page_icon="🎓", layout="centered")

# 2. LOGO S BÍLÝM POZADÍM (Pro fixaci dark mode)
with st.container():
    st.markdown(
        """
        <style>
        .logo-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
        }
        </style>
        <div class="logo-container">
        """, unsafe_allow_html=True
    )
    try:
        # Tady používáme pevnou šířku, což je v pořádku
        st.image("logo.png", width=500)
    except:
        st.write("⚠️ Soubor logo.png nebyl nalezen na GitHubu!")
    st.markdown("</div>", unsafe_allow_html=True)

st.title("🎓 VŠE BIP: Asistent pro InSIS")
st.markdown("Proklikej si checklist nebo se zeptej AI na detaily k výjezdu.")

# OPRAVA: use_container_width -> width='stretch'
st.link_button(
    label="📖 OTEVŘÍT VIZUÁLNÍ MANUÁL", 
    url="https://vsebip.my.canva.site/", 
    width='stretch'
    )


# 2. INTERAKTIVNÍ CHECKLIST
# (zbytek tvého kódu zůstává tak, jak je...)

# 2. INTERAKTIVNÍ CHECKLIST
st.write("### ⚡ Rychlé instrukce k checklistu v InSIS:")
col1, col2 = st.columns(2)
with col1:
    if st.button("📄 Dopis o přijetí", use_container_width=True): st.info("**Acceptance Letter:** Dopis o přijetí (Acceptance Letter): Jedná se o oficiální potvrzení od zahraniční instituce, které dokládá, že jste byli vybráni a přijati k účasti na daném programu. Nahraj scan/PDF.")
    if st.button("✍️ Learning Agreement", use_container_width=True): st.info("**LA:** Studijní smlouva uzavíraná mezi vámi, VŠE a hostitelskou školou. Specifikuje, jaké předměty budete v zahraničí studovat a za kolik kreditů vám budou po návratu uznány. Podívejte se do vizuálního návodu, kde je přesný návod!")
    if st.button("🚆 Jízdenky / Letenky", use_container_width=True): st.info("**Cesta:** Dokumentace vaší dopravy na místo konání pobytu a zpět, která slouží jako doklad o realizaci cesty pro účely vyúčtování nebo proplacení nákladů. Všechny doklady (tam i zpět) v 1 PDF souboru.")
with col2:
    if st.button("🏦 Bankovní spojení", use_container_width=True): st.info("**Účet:** Číslo účtu určené specificky pro výplatu stipendia na zahraniční výjezdy. Přidej účel 'k výplatě stipendia na zahraniční výjezdy'.")
    if st.button("🚨 Emergency Contact", use_container_width=True): st.info("**Kontakt:** Poskytnutí kontaktu na blízkou osobu, která může být informována v případě, že byste se během pobytu v zahraničí dostali do nouzové situace. Vyplň externí formulář z e-mailu od OZS.")
    if st.button("📜 Účastnická smlouva", use_container_width=True): st.info("**Smlouva:** Hlavní smlouva mezi vámi a VŠE (zastoupenou OZS),která definuje podmínky vaší mobility, délku pobytu a výši přidělené finanční podpory. Podepiš, nahraj a ORIGINÁL přines koordinátorce.")

st.divider()

# 3. MOZEK ASISTENTA
st.subheader("🤖 Zeptej se asistenta")

API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=API_KEY)
def nacti_znalosti():
    try:
        with open("znalosti.txt", "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "Jsi asistent pro BIP na VŠE."

# AUTOMATICKÝ VÝBĚR MODELU
try:
    dostupne_modely = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    if 'models/gemini-1.5-flash' in dostupne_modely:
        nazev_modelu = 'gemini-1.5-flash'
    elif 'models/gemini-pro' in dostupne_modely:
        nazev_modelu = 'gemini-pro'
    else:
        nazev_modelu = dostupne_modely[0].replace('models/', '') if dostupne_modely else 'gemini-1.5-flash'

    model = genai.GenerativeModel(
        model_name=nazev_modelu,
        system_instruction=nacti_znalosti()
    )
except Exception as e:
    st.error(f"Chyba při načítání modelů: {e}")
    dostupne_modely = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Napiš svůj dotaz..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("⚠️ Komunikační problém s Googlem.")
            st.info(f"Detail chyby: {e}")
            st.info(f"Viditelné modely pro tento klíč: {dostupne_modely}")







