import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import random

# Login
LoginManager().go_to_login('Start.py')

# Data laden
data_manager = DataManager(fs_protocol="webdav", fs_root_folder="Quiz_LN_Informatik")
data_manager.load_app_data(
    session_state_key="Fragen_Parasitologie_df",
    file_name="parasitologie_fragen.csv"
)

st.title("10 zufällige Fragen")

def start_quiz(df):
    if "random_questions" in st.session_state:
        del st.session_state["random_questions"]
    if "user_answers" in st.session_state:
        del st.session_state["user_answers"]
    if "current_question_index" in st.session_state:
        del st.session_state["current_question_index"]

    df = df.sample(frac=1).reset_index(drop=True)
    question_list = df.drop_duplicates(subset="question").sample(
        n=min(10, len(df)), random_state=None
    ).to_dict(orient="records")

    st.session_state["random_questions"] = question_list
    st.session_state["user_answers"] = {}
    st.session_state["current_question_index"] = 0

# Starte Quiz
if "Fragen_Parasitologie_df" in st.session_state:
    df = st.session_state["Fragen_Parasitologie_df"]

    if st.button("Quiz starten"):
        start_quiz(df)

    if "random_questions" in st.session_state:
        questions = st.session_state["random_questions"]
        total_questions = len(questions)
        current_index = st.session_state.get("current_question_index", 0)
        question = questions[current_index]

        st.subheader(f"Frage {current_index + 1} von {total_questions}")
        st.write(question["question"])

        if pd.notna(question.get("images")) and question["images"].strip():
            st.image(question["images"], caption="Bild zur Frage", use_container_width=True)

        # Platzhalter-Option mit Parasit-Emoji
        placeholder_option = "🦠 Parasit auswählen..."

        options = [placeholder_option, question["answer_a"], question["answer_b"], question["answer_c"], question["answer_d"]]
        user_answer = st.radio(
            "Wähle eine Antwort:",
            options=options,
            key=f"question_{current_index}"
        )

        # Antwort speichern, nur wenn nicht Platzhalter
        if user_answer != placeholder_option:
            st.session_state["user_answers"][current_index] = {
                "question": question["question"],
                "correct_answer": question["correct_answer"],
                "user_answer": user_answer
            }

        # Navigationsbuttons
        cols = st.columns(3)
        with cols[0]:
            if current_index > 0:
                if st.button("← Zurück"):
                    st.session_state["current_question_index"] -= 1

        with cols[2]:
            if current_index < total_questions - 1:
                if st.button("Weiter →"):
                    st.session_state["current_question_index"] += 1
            else:
                if st.button("Auswertung anzeigen"):
                    if "user_answers" in st.session_state:
                        correct_count = 0
                        incorrect_count = 0
                        unanswered = []
                        incorrect_questions = []

                        for i in range(total_questions):
                            if i not in st.session_state["user_answers"]:
                                unanswered.append(questions[i]["question"])
                                continue

                            answer_data = st.session_state["user_answers"][i]
                            if answer_data["user_answer"] == answer_data["correct_answer"]:
                                correct_count += 1
                            else:
                                incorrect_count += 1
                                incorrect_questions.append({
                                    "question": answer_data["question"],
                                    "correct_answer": answer_data["correct_answer"],
                                    "user_answer": answer_data["user_answer"]
                                })

                        st.success(f"Richtige Antworten: {correct_count}")
                        st.error(f"Falsche Antworten: {incorrect_count}")
                        if unanswered:
                            st.warning(f"Unbeantwortete Fragen: {len(unanswered)}")

                        if incorrect_questions:
                            st.write("Falsch beantwortete Fragen:")
                            for q in incorrect_questions:
                                st.markdown(f"""
                                - **Frage:** {q['question']}
                                    - **Deine Antwort:** <span style='color:red'>{q['user_answer']}</span>  
                                    - **Richtige Antwort:** <span style='color:green'>{q['correct_answer']}</span>
                                """, unsafe_allow_html=True)

                        # Ergebnisse speichern
                        results = {
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "correct_count": correct_count,
                            "incorrect_count": incorrect_count,
                            "unanswered": len(unanswered),
                            "details": st.session_state["user_answers"]
                        }

                        try:
                            if "user_results" not in st.session_state:
                                st.session_state["user_results"] = []
                            st.session_state["user_results"].append(results)

                            DataManager().append_record(
                                session_state_key="data_df",
                                record_dict=results
                            )
                            st.success("Ergebnisse wurden gespeichert.")
                        except Exception as e:
                            st.error(f"Fehler beim Speichern der Ergebnisse: {e}")

else:
    st.error("Der DataFrame konnte nicht geladen werden. Bitte überprüfe die Datenquelle.")
