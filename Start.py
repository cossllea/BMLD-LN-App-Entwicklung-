import streamlit as st
import pandas as pd
import io
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

data_manager = DataManager(fs_protocol= "webdav", fs_root_folder="Quiz_LN_Informatik")

login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://drive.switch.ch/index.php/s/ZbkH4TCqVX6LLOZ/download");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    /* Overlay für bessere Lesbarkeit */
    .block-container {
        background: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 32px rgba(0,0,0,0.07);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

data_manager.load_app_data(
    session_state_key= "Fragen_Parasitologie_df",
    file_name = "parasitologie_fragen.csv")

data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )


cols = st.columns([3, 1])
with cols[0]:
    st.title("PathoLogic-Quiz")
with cols[1]:
    st.image("https://drive.switch.ch/index.php/s/NQzo46BcGfLbd3Z/download", width=150)

name = st.session_state.get('name')
 
st.markdown(f"🦠  Hallo {name}! 🦠 ")

st.markdown("**Anleitung:**")

st.markdown('Wähle zuerst einen Quiz Modus aus. Der "Low Brain Power Mode" beinhaltet 10 Fragen, der "A Little More Brain Power Mode" enthält 20 Fragen. Um den ausgewählten Modus zu starten, klicke auf den "Quiz starten" Button.')
st.markdown('Wenn du den Zurück-Button wählst, wird die Seite neu gestartet, du musst deine aktuelle Antwort also nochmals bestätigen. Du kannst eine Antwort mit einem Doppelklick auf "Weiter" bestätigen.')
st.markdown('Um deine Antworten zur Auswertung zu speichern, klicke auf den "Auswertung anzeigen" Button.')

st.markdown("Jetzt weisst du alles was du wissen musst, um die App zu benutzen. Viel Spass beim Lernen!")

st.markdown("**Kurzanleitung als Video:**")
st.video("https://drive.switch.ch/index.php/s/sh5XGbfkocwWBcf/download")

if st.button("Zum Quiz-Modus auswählen"):
    st.switch_page("pages/1_Quiz-Modus.py")

st.markdown(
    """
    <div style='font-size:16px; color:#888; margin-top:40px; text-align:center;'>
        Diese App wurde von folgenden Personen entwickelt:<br>
        Lisa Pianezzi (<a href="mailto:pianelis@students.zhaw.ch">pianelis@students.zhaw.ch</a>)<br>
        Michelle Weder (<a href="mailto:wedermic@students.zhaw.ch">wedermic@students.zhaw.ch</a>)<br>
        Leah Cosslett (<a href="mailto:cossllea@students.zhaw.ch">cossllea@students.zhaw.ch</a>)
    </div>
    """,
    unsafe_allow_html=True
)