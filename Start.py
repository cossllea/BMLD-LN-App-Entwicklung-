import streamlit as st
import pandas as pd
import io
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
st.write("Navigiere über die Sidebar zu den verschiedenen Seiten der App.")

#### ACHTUNG: Wir müssen den Dataframe anpassen bevor der Code richtig funktioniert 
    # Spalte #RichtigeAntwort muss die Ausgeschriebene Antwort enthalten nicht nur A, B, C oder D
    # wir brauchen mehr Fragen 
    # Alle Umlaute müssen ausgeschrieben werden