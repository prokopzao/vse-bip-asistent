 import streamlit as st
import google.generativeai as genai

# 1. NASTAVENÍ VZHLEDU STRÁNKY
st.set_page_config(page_title="VŠE BIP Asistent", page_icon="🎓", layout="centered")

# 2. HLAVIČKA A ODKAZ NA MANUÁL
st.title("🎓 VŠE BIP: Asistent pro InSIS")
st.markdown("Bojuješ s byrokracií před výjezdem? Proklikej si náš manuál nebo se zeptej AI.")

st.link_button(
    label="📖 OTEVŘÍT VIZUÁLNÍ MANUÁL (Canva)", 
    url="https://vsebip.my.canva.site/", 
    use_container_width=True
)

# NOVINKA: KLIKACÍ DLAŽDICE
st.write("### ⚡ Rychlé instrukce k dokumentům:")
col1, col2 = st.columns(2)

with col1:
    if st.button("📄 Acceptance Letter", use_container_width=True):
        st.info("**Acceptance Letter:** Nahraj ho do InSISu do sekce 'Moje studium' hned, jak ti přijde.")
    if st.button("✍️ Learning Agreement", use_container_width=True):
        st.info("**Learning Agreement:** Musí ho podepsat tvoje fakulta i zahraniční škola.")

with col2:
    if st.button("🏥 Pojištění", use_container_width=True):
        st.info("**Pojištění:** Stačí kartička pojištěnce (EHIC) nebo komerční pojištění na celou dobu.")
    if st.button("💳 Grant", use_container_width=True):
        st.info("**Grant:** Účastnickou smlouvu podepisuješ až jako úplně poslední krok.")

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
