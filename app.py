import streamlit as st
import google.generativeai as genai

# 1. KONFIGURACE A DESIGN
st.set_page_config(page_title="VŠE BIP | Asistent", page_icon="💖", layout="centered")

# NEJLEPŠÍ MOŽNÉ CSS PRO ROK 2026
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

    /* DARK CHAT - Fix aby nebělal */
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
    
    /* Vstupní text v chatu */
    [data-testid="stChatInput"] textarea {
        color: white !important;
    }

    /* GLASS CARDS - Dokumenty */
    .doc-card {
        background: var(--glass);
        border: 1px solid rgba(212, 34, 115, 0.3);
        border-radius: 20px;
        padding: 22px;
        margin-bottom: 15px;
        height: 160px; /* Sjednocená výška karet */
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
    }

    /* ANIMOVANÝ NADPIS */
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

    /* SKRYTÍ HEADERU */
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
st.markdown("<p style='text-align: center; opacity: 0.7; font-size: 1.2rem; margin-top: -10px;'>Prémiový průvodce pro studenty FM VŠE</p>", unsafe_allow_html=True)
st.write("")

# 3. HLAVNÍ AKCE (Neon Pink)
st.link_button("📂 OTEVŘÍT KOMPLETNÍ MANU




