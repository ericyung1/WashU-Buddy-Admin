# chatbot.py
import streamlit as st
from src.qa import ask_and_get_answer

def chatbot():
    if 'history' not in st.session_state:
        st.session_state.history = []

    q = st.text_input('WASHU BUDDY ADMIN PANEL', placeholder='Ask me anything about Washington University in St. Louis...')
    if q:
        if 'vs' in st.session_state:
            vector_store = st.session_state.vs
            answer = ask_and_get_answer(vector_store, q)
            
            st.session_state.history.append({"text": q, "is_user": True})
            st.session_state.history.append({"text": answer, "is_user": False})

    for chat in st.session_state.history:
        message(chat['text'], is_user=chat['is_user'])
