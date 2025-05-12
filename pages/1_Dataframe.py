import streamlit as st
import pandas as pd
import io
from utils.data_manager import DataManager


data_manager = DataManager(fs_protocol= "webdav", fs_root_folder="Quiz_LN_Informatik")

data_manager.load_app_data(
    session_state_key= "Fragen_Parasitologie_df",
    file_name = "parasitologie_fragen.csv")

st.title("Dataframe")
st.write("Hier sind die ersten 10 Fragen aus der Datei `parasitologie_fragen.csv`:")

# Zeige die Tabelle mit den ersten 10 Zeilen an
if "Fragen_Parasitologie_df" in st.session_state:
    st.dataframe(st.session_state["Fragen_Parasitologie_df"].head(55), use_container_width=True)
else:
    st.write("Der DataFrame wurde noch nicht geladen. Bitte kehre zur Startseite zurück, um die Daten zu laden.")