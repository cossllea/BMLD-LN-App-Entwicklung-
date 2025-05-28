import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

data_manager = DataManager(fs_protocol="webdav", fs_root_folder="Quiz_LN_Informatik")

login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

data_manager.load_app_data(
    session_state_key="Fragen_Parasitologie_df",
    file_name="parasitologie_fragen.csv"
)

data_manager.load_user_data(
    session_state_key='data_df',
    file_name='data.csv',
    initial_value=pd.DataFrame()
)

cols = st.columns([3, 1])
with cols[0]:
    st.title("PathoLogic-Quiz")
with cols[1]:
    st.image("https://drive.switch.ch/index.php/s/NQzo46BcGfLbd3Z/download", width=150)


name = st.session_state.get('name')
st.markdown(f"🦠  Hallo {name}! 🦠 ")

# Quiz-Modus Auswahl
quiz_mode_select = st.radio(
    "Wähle deinen Quiz-Modus:",
    ["Low Brain Power", "A Little More Brain Power"],
    key="quiz_mode_select"
)

if st.button("Modus bestätigen"):
    st.session_state["quiz_mode"] = quiz_mode_select
    st.success(f"Modus '{quiz_mode_select}' gewählt! Du wirst zum Quiz weitergeleitet.")
    st.switch_page("pages/2_Quiz.py")  # Passe ggf. den Pfad an!

st.write(f"**Aktueller Modus:** {st.session_state.get('quiz_mode', 'Noch keiner gewählt')}")

