import streamlit as st
import pandas as pd
import io
from datetime import datetime
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import random

LoginManager().go_to_login('Start.py') 

data_manager = DataManager(fs_protocol= "webdav", fs_root_folder="Quiz_LN_Informatik")

data_manager.load_app_data(
    session_state_key= "Fragen_Parasitologie_df",
    file_name = "parasitologie_fragen.csv")

st.title("10 zufällige Fragen")

def start_quiz(df):
    """
    Funktion zum Starten oder Zurücksetzen des Quiz.
    Generiert 10 zufällige Fragen und initialisiert die Benutzerantworten.
    """
    # Lösche vorherige Fragen aus dem Session State
    if "random_questions" in st.session_state:
        del st.session_state["random_questions"]
        st.write("Session State für Fragen wurde zurückgesetzt.")  # Debugging

    # Lade den DataFrame neu und mische die Reihenfolge
    df = df.sample(frac=1).reset_index(drop=True)

    # Generiere neue 10 zufällige Fragen
    question_list = df.drop_duplicates(subset="question").sample(
        n=min(10, len(df)), random_state=None
    ).to_dict(orient="records")

    # Speichere die neuen Fragen und initialisiere die Benutzerantworten
    st.session_state["random_questions"] = question_list
    st.session_state["user_answers"] = {}  # Initialisiere die Benutzerantworten

# Überprüfen, ob der DataFrame existiert
if "Fragen_Parasitologie_df" in st.session_state:
    # DataFrame aus dem Session State abrufen
    df = st.session_state["Fragen_Parasitologie_df"]

    # Quiz Button:
    if st.button("Quiz starten"):
        start_quiz(df)

    # Fragen und Antwortmöglichkeiten anzeigen
    if "random_questions" in st.session_state:
        random_questions = st.session_state["random_questions"]
    
        for i, question in enumerate(random_questions, start=1):
            st.subheader(f"Frage {i}: {question['question']}")

            # Überprüfe, ob ein Bild vorhanden ist, und zeige es an
            if pd.notna(question.get('images')):  # Prüfe, ob die Spalte 'image' nicht leer ist
                image_url = question['images']  # WebDAV-URL aus der Spalte 'image'
                st.image(image_url, caption=f"Bild für Frage {i}", use_container_width=True)

            user_answer = st.radio(
                "Wähle eine Antwort:",
                options=[question['answer_a'], question['answer_b'], question["answer_c"], question['answer_d']],
                key=f"question_{i}"
            )

            # Speichere die Benutzerantwort
            if user_answer != "Bitte wählen":
                st.session_state["user_answers"][i] = {
                    "question": question['question'],
                    "correct_answer": question['correct_answer'],
                    "user_answer": user_answer
                }

        #Auswertung anzeigen
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
                        incorrect_questions.append({
                            "question": answer_data["question"],
                            "correct_answer": answer_data["correct_answer"],
                            "user_answer": answer_data["user_answer"]
                        })


                # Ergebnisse anzeigen
                st.write(f"Richtige Antworten: {correct_count}")
                st.write(f"Falsche Antworten: {incorrect_count}")

                if incorrect_questions:
                    st.write("Falsche Fragen:")
                    for question in incorrect_questions:
                        st.markdown(f"""
                        - **Frage:** {question['question']}
                            - **Deine Antwort:** `{question['user_answer']}`
                            - **Richtige Antwort:** `{question['correct_answer']}`
                        """)
                 # Ergebnisse speichern
                results = {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "correct_count": correct_count,
                    "incorrect_count": incorrect_count,
                    "details": st.session_state["user_answers"]
                }

                try:
                    # Initialisiere den Session State Key, falls nicht vorhanden
                    if "user_results" not in st.session_state:
                        st.session_state["user_results"] = []

                    # Speichere die Ergebnisse in der Session State Liste
                    st.session_state["user_results"].append(results)


                    # Speichere die Ergebnisse mit DataManager
                    DataManager().append_record(
                        session_state_key="data_df",  # Session State Key für die Ergebnisse
                        record_dict=results  # Die Ergebnisse als Dictionary
                    )
                    st.success("Ergebnisse wurden gespeichert.")
                except Exception as e:
                    st.error(f"Fehler beim Speichern der Ergebnisse: {e}")
                


else:
    st.error("Der DataFrame konnte nicht geladen werden. Bitte überprüfe die Datenquelle.")