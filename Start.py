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


st.title("Lernapp")

name = st.session_state.get('name')
st.markdown(f"✨ Hallo {name}! ✨")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
In dieser Lernapp werden 10 Single-Choice Fragen zum Thema Parasitologie aus dem Modul Medizinische Mikrobiologie 2 in Form eines Quizzes gestellt!

Diese App wurde von folgenden Personen entwickelt:
- Lisa Pianezzi (pianelis@students.zhaw.ch)
- Michelle Weder (wedermic@students.zhaw.ch)
- Leah Cosslett (cossllea@students.zhaw.ch)

"""
st.write("Navigiere über die Sidebar zu den verschiedenen Seiten der App.")

