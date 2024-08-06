import streamlit as st

def clear_history():
    if 'history' in st.session_state:
        del st.session_state['history']
