import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

data_manager = DataManager(fs_protocol= "webdav", fs_root_folder="Quiz_LN_Informatik")

data_manager.load_app_data(
    session_state_key= "Fragen_Parasitologie_df",
    file_name = "parasitologie_fragen.csv")



st.title("Lernapp")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
In dieser Lernapp werden 10 Single-Choice Fragen zum Thema Parasitologie aus dem Modul Medizinische Mikrobiologie 2 in Form eines Quizzes gestellt!

Diese App wurde von folgenden Personen entwickelt:
- Lisa Pianezzi (pianelis@students.zhaw.ch)
- Michelle Weder (wedermic@students.zhaw.ch)
- Leah Cosslett (cossllea@students.zhaw.ch)

"""

st.dataframe(st.session_state["Fragen_Parasitologie_df"], use_container_width=True)
st.write("Die Fragen sind in der Datei `parasitologie_fragen.csv` gespeichert.")