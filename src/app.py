# app.py
import streamlit as st
from src.sidebar import sidebar
from src.file_preview import file_preview
from src.chatbot import chatbot

def run_app():
    st.image('images/WashU_Buddy_Logo.png')
    sidebar()
    file_preview()
    # Uncomment the following line to enable the chatbot
    # chatbot()