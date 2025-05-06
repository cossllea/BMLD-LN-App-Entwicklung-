import streamlit as st
import pandas as pd
import io
from utils.data_manager import DataManager

#### ACHTUNG: Wir müssen den Dataframe anpassen bevor der Code richtig funktioniert 
    # Spalte #RichtigeAntwort muss die Ausgeschriebene Antwort enthalten nicht nur A, B, C oder D
    # wir brauchen mehr Fragen 
    # Alle Umlaute müssen ausgeschrieben werden

data_manager = DataManager(fs_protocol= "webdav", fs_root_folder="Quiz_LN_Informatik")

data_manager.load_app_data(
    session_state_key= "Fragen_Parasitologie_df",
    file_name = "parasitologie_fragen.csv")

st.title("10 zufällige Fragen")



# Überprüfen, ob der DataFrame existiert
if "Fragen_Parasitologie_df" in st.session_state:
    # DataFrame aus dem Session State abrufen
    df = st.session_state["Fragen_Parasitologie_df"]

     # Zeige die Anzahl der Zeilen im DataFrame
    st.write("Anzahl der Zeilen im DataFrame:", len(df))

    # Quiz Button:
    if st.button("Quiz starten"):
         # Entferne Duplikate aus dem DataFrame
        df = df.drop_duplicates(subset="Frage")

        # Wähle 10 zufällige Fragen ohne Wiederholungen
        num_questions = min(10, len(df))  # Wähle maximal 10 Fragen oder die Anzahl der verfügbaren Fragen
        st.session_state["random_questions"] = df.sample(n=num_questions, replace=False)
        st.session_state["user_answers"] = {}  # Initialisiere die Benutzerantworten


    # Fragen und Antwortmöglichkeiten anzeigen
    if "random_questions" in st.session_state:
        random_questions = st.session_state["random_questions"]
    

        for i, row in enumerate(random_questions.iterrows(), start=1):
            st.subheader(f"Frage {i}: {row[1]['Frage']}")
            user_answer = st.radio(
                "Wähle eine Antwort:",
                options=[row[1]['A'], row[1]['B'], row[1]["C"], row[1]['D']],
                key=f"question_{i}"
            )

            # Speichere die Benutzerantwort
            st.session_state["user_answers"] [i] = {
                "question": row[1]['Frage'],
                "correct_answer": row[1]['RichtigeAntwort'],
                "user_answer": user_answer
            }

        #Auswertun anzeigen
        if st.button("Auswertung anzeigen"):
            if "user_answers" in st.session_state:
                correct_count = 0
                incorrect_count = 0 
                incorrect_questions = []

                # Vergleiche die Antworten
                for i, answer_data in st.session_state["user_answers"].items():
                    if answer_data["user_answer"] == answer_data["correct_answer"]:
                        correct_count += 1
                    else:
                        incorrect_count += 1
                        incorrect_questions.append(answer_data["question"])

                # Ergebnisse anzeigen
                st.write(f"Richtige Antworten: {correct_count}")
                st.write(f"Falsche Antworten: {incorrect_count}")

                if incorrect_questions:
                    st.write("Falsche Fragen:")
                    for question in incorrect_questions:
                        st.write(f"- {question}")

else:
    st.error("Der DataFrame konnte nicht geladen werden. Bitte überprüfe die Datenquelle.")