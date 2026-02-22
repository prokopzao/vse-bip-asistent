import streamlit as st
import google.generativeai as genai

# 1. NASTAVENÍ VZHLEDU STRÁNKY
st.set_page_config(page_title="VŠE BIP Asistent", page_icon="🎓", layout="centered")
st.image("https://fph.vse.cz/wp-content/uploads/sites/4/2021/03/FPH_logo_CZ_RGB.png", width=350)
# 2. HLAVIČKA A ODKAZ NA MANUÁL
st.title("🎓 VŠE BIP: Asistent pro InSIS")
st.markdown("Bojuješ s byrokracií před výjezdem? Proklikej si náš manuál nebo se zeptej AI.")

st.link_button(
    label="📖 OTEVŘÍT VIZUÁLNÍ MANUÁL (Canva)", 
    url="https://vsebip.my.canva.site/", 
    use_container_width=True
)

# NOVINKA: KOMPLETNÍ CHECKLIST INSIS
st.write("### ⚡ Rychlé instrukce k checklistu v InSIS:")
col1, col2 = st.columns(2)

with col1:
    if st.button("📄 Dopis o přijetí", use_container_width=True):
        st.info("**Acceptance Letter:** Nahraj scan nebo PDF do kolonky 'Dopis o přijetí'. Koordinátorka schvaluje hromadně v pondělí, hned se to neozelená!")
    
    if st.button("✍️ Learning Agreement", use_container_width=True):
        st.info("**LA:** Zvol 'Krátkodobá kombinovaná mobilita'.")
    
    if st.button("🚆 Jízdenky / Letenky", use_container_width=True):
        st.info("**Cesta:** Nahraj cestu TAM i ZPĚT v 1 PDF. Eko doprava (vlak/bus) = 417 EUR, letadlo = 309 EUR.")

with col2:
    if st.button("🏦 Bankovní spojení", use_container_width=True):
        st.info("**Účet:** V Portálu studenta přidej k účtu účel 'k výplatě stipendia na zahraniční výjezdy'.")
        
    if st.button("🚨 Emergency Contact", use_container_width=True):
        st.info("**Nouzový kontakt:** Vyplň externí formulář z e-mailu od OZS. V InSISu se to odškrtne samo.")

    if st.button("📜 Účastnická smlouva", use_container_width=True):
        st.info("**Smlouva:** Připraví ji koordinátorka cca 14 dní před odjezdem. Musíš ji podepsat, nahrát a donést ORIGINÁL do RB 410.")

st.divider()

# 3. CHAT S AI ASISTENTEM
st.subheader("🤖 Zeptej se asistenta")

# Tvůj API klíč
API_KEY = "AIzaSyD6MR1aVgKw6pove4KVUABuDByJURJPGJo" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

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
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})




