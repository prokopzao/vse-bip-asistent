import streamlit as st
import google.generativeai as genai

# 1. NASTAVENÍ STRÁNKY A LOGA
st.set_page_config(page_title="VŠE BIP Asistent", page_icon="🎓", layout="centered")
st.image("https://fm.vse.cz/wp-content/uploads/page/44/FM_logo_CZ_RGB.png", width=400)

st.title("🎓 VŠE BIP: Asistent pro InSIS")
st.markdown("Vítej na Fakultě managementu! Proklikej si checklist nebo se zeptej AI na detaily.")

st.link_button(label="📖 OTEVŘÍT VIZUÁLNÍ MANUÁL (Canva)", url="https://vsebip.my.canva.site/", use_container_width=True)

# 2. RYCHLÝ CHECKLIST (Tlačítka)
st.write("### ⚡ Rychlé instrukce k checklistu:")
col1, col2 = st.columns(2)
with col1:
    if st.button("📄 Dopis o přijetí", use_container_width=True): st.info("Nahraj scan/PDF. Schvaluje se hromadně v pondělí!")
    if st.button("✍️ Learning Agreement", use_container_width=True): st.info("Postup je podrobně rozepsán v manuálu.")
    if st.button("🚆 Jízdenky / Letenky", use_container_width=True): st.info("Všechny doklady (tam i zpět) v 1 PDF souboru.")
with col2:
    if st.button("🏦 Bankovní spojení", use_container_width=True): st.info("Přidej účel 'k výplatě stipendia na zahraniční výjezdy'.")
    if st.button("🚨 Emergency Contact", use_container_width=True): st.info("Vyplň externí formulář z e-mailu od OZS.")
    if st.button("📜 Účastnická smlouva", use_container_width=True): st.info("Podepiš, nahraj a ORIGINÁL přines do kanceláře.")

st.divider()

# 3. MOZEK ASISTENTA
st.subheader("🤖 Zeptej se asistenta")

# KLÍČ: Použij ten, co máš na screenshotu
API_KEY = "AIzaSyATI0KCn_Df-rF5l2JxWIgFHaMOF7iMgb4" 
genai.configure(api_key=API_KEY)

def nacti_znalosti():
    try:
        with open("znalosti.txt", "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Chyba při čtení znalosti.txt: {e}"

# TADY JE TEN START - POUŽÍVÁME 'gemini-1.5-flash'
try:
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=nacti_znalosti()
    )
except Exception as e:
    st.error(f"Nepodařilo se nastartovat model: {e}")

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
            # TADY VOLÁME GOOGLE
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("⚠️ Google API má problém. Zkus v AI Studiu vygenerovat nový 'Free' API klíč.")
            st.info(f"Detail chyby: {e}")





