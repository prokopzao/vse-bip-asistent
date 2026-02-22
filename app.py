import streamlit as st
import google.generativeai as genai

# 1. NASTAVENÍ STRÁNKY A LOGA
st.set_page_config(page_title="VŠE BIP Asistent", page_icon="🎓", layout="centered")
st.image("https://fph.vse.cz/wp-content/uploads/logo/FBA/horizontal/FBA_logo_horizontal_white.png", width=400)

st.title("🎓 VŠE BIP: Asistent pro InSIS")
st.markdown("Proklikej si checklist nebo se zeptej AI na detaily k výjezdu.")

# 2. INTERAKTIVNÍ CHECKLIST
st.write("### ⚡ Rychlé instrukce k checklistu v InSIS:")
col1, col2 = st.columns(2)
with col1:
    if st.button("📄 Dopis o přijetí", use_container_width=True): st.info("**Acceptance Letter:** Nahraj scan/PDF. Schvaluje se hromadně v pondělí!")
    if st.button("✍️ Learning Agreement", use_container_width=True): st.info("**LA:** Podívejte se do vizuálního návodu, kde je přesný návod!")
    if st.button("🚆 Jízdenky / Letenky", use_container_width=True): st.info("**Cesta:** Všechny doklady (tam i zpět) v 1 PDF souboru.")
with col2:
    if st.button("🏦 Bankovní spojení", use_container_width=True): st.info("**Účet:** Přidej účel 'k výplatě stipendia na zahraniční výjezdy'.")
    if st.button("🚨 Emergency Contact", use_container_width=True): st.info("**Kontakt:** Vyplň externí formulář z e-mailu od OZS.")
    if st.button("📜 Účastnická smlouva", use_container_width=True): st.info("**Smlouva:** Podepiš, nahraj a ORIGINÁL přines koordinátorce.")

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


