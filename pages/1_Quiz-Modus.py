import streamlit as st
import pandas as pd
import io


st.markdown("### **Wähle deinen Quiz-Modus:**")
quiz_mode = st.radio(
    "",
    ("🧠 Low Brain Power (10 Fragen)", "🧠🧠 A Little More Brain Power (20 Fragen)")
)

if st.button("Modus bestätigen"):
    st.session_state["quiz_mode"] = quiz_mode
    st.success(f"Modus '{quiz_mode}' wurde gespeichert. Wechsle jetzt zum Tab 'Quiz'.")