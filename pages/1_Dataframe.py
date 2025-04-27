import streamlit as st

st.title("Dataframe")

st.write("Hier sind die ersten 10 Fragen aus der Datei `parasitologie_fragen.csv`:")

# Zeige die Tabelle mit den ersten 10 Zeilen an
if "Fragen_Parasitologie_df" in st.session_state:
    st.dataframe(st.session_state["Fragen_Parasitologie_df"].head(10), use_container_width=True)
else:
    st.write("Der DataFrame wurde noch nicht geladen. Bitte kehre zur Startseite zurück, um die Daten zu laden.")