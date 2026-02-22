import streamlit as st
import google.generativeai as genai

# 1. NASTAVENÍ STRÁNKY A LOGA
st.set_page_config(page_title="VŠE BIP Asistent", page_icon="🎓", layout="centered")

# Logo Fakulty managementu VŠE
st.image("https://fm.vse.cz/wp-content/uploads/page/44/FM_logo_CZ_RGB.png", width=400)

st.title("🎓 VŠE BIP: Asistent pro InSIS")
st.markdown("Proklikej si checklist nebo se zeptej AI na detaily k výjezdu.")

st.link_button(
    label="📖 OTEVŘÍT VIZUÁLNÍ MANUÁL (Canva)", 
    url="https://vsebip.my.canva.site/", 
    use_container_width=True
)

# 2. INTERAKTIVNÍ CHECKLIST
st.write("### ⚡ Rychlé instrukce k checklistu v InSIS:")
col1, col2 = st.columns(2)

with col1:
    if st.button("📄 Dopis o přijetí", use_container_width=True):
        st.info("**Acceptance Letter:** Nahraj scan/PDF. Schvaluje se hromadně v pondělí!")
    if st.button("✍️ Learning Agreement", use_container_width=True):
        st.info("**LA:** Políčko 'Podmínky k uznání' nechte zcela PRÁZDNÉ!")
    if st.button("🚆 Jízdenky / Letenky", use_container_width=True):
        st.info("**Cesta:** Všechny doklady (tam i zpět) v 1 PDF souboru.")

with col2:
    if st.button("🏦 Bankovní spojení", use_container_width=True):
        st.info("**Účet:** Přidej účel 'k výplatě stipendia na zahraniční výjezdy'.")
    if st.button("🚨 Emergency Contact", use_container_width=True):
        st.info("**Kontakt:** Vyplň externí formulář z e-mailu od OZS.")
    if st.button("📜 Účastnická smlouva", use_container_width=True):
        st.info("**Smlouva:** Podepiš, nahraj a ORIGINÁL přines koordinátorce.")

st.divider()

# 3. MOZEK ASISTENTA (AI CHAT)
st.subheader("🤖 Zeptej se asistenta")

# KONFIGURACE AI - Tvůj nový "čerstvý" klíč
API_KEY = "AIzaSyCvYQlFNA_EUreujD8QLbCKYnSAvScw3Cw"
genai.configure(api_key=API_KEY)

# Funkce pro načtení dokumentů
def nacti_znalosti():
    try:
        with open("znalosti.txt", "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "Jsi asistent pro BIP na VŠE. Odpovídej přátelsky a stručně."

# Inicializace modelu - používáme stabilní 'gemini-1.5-flash'
try:
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash-latest',
        system_instruction=nacti_znalosti()
    )
except Exception as e:
    st.error(f"Nepodařilo se nastartovat model: {e}")

# Paměť chatu
if "messages" not in st.session_state:
    st.session_state.messages = []

# Vykreslení historie
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Vstup od uživatele
if prompt := st.chat_input("Napiš svůj dotaz (např. Jak vyplnit LA?)..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Zde se ptáme Googlu
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("⚠️ Asistent narazil na komunikační problém s Googlem.")
            st.info(f"Detail chyby: {e}")







