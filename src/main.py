import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from src.app import run_app

if __name__ == "__main__":
    load_dotenv(find_dotenv(), override=True)
    run_app()