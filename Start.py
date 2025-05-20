import streamlit as st
import pandas as pd
import io
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

data_manager = DataManager(fs_protocol= "webdav", fs_root_folder="Quiz_LN_Informatik")

login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

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
    st.image("https://drive.switch.ch/index.php/f/8599875366", width=120)

name = st.session_state.get('name')
 
st.markdown(f"🦠  Hallo {name}! 🦠 ")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
In dieser Lernapp werden 10 Single-Choice Fragen zum Thema Parasitologie aus dem Modul Medizinische Mikrobiologie 2 in Form eines Quizzes gestellt!

Diese App wurde von folgenden Personen entwickelt:
- Lisa Pianezzi (pianelis@students.zhaw.ch)
- Michelle Weder (wedermic@students.zhaw.ch)
- Leah Cosslett (cossllea@students.zhaw.ch)

"""

st.markdown("**Anleitung:**")

st.markdown('Wähle zuerst einen Quiz Modus aus. Der "Low Brain Power Mode" beinhaltet 10 Fragen, der "A Little More Brain Power Mode" enthält 20 Fragen. Um den ausgewählten Modus zu starten, klicke auf den "Quiz starten" Button.')
st.markdown('Wenn du den Zurück-Button wählst, wird die Seite neu gestartet, du musst deine aktuelle Antwort also nochmals bestätigen.')
st.markdown('Um deine Antworten zur Auswertung zu speichern, klicke auf den "Auswertung anzeigen" Button.')

st.markdown("Jetzt weisst du alles was du wissen musst, um die App zu benutzen. Viel Spass beim Lernen!")

if st.button("Zum Quiz-Modus auswählen"):
    st.switch_page("pages/1_Quiz-Modus.py")