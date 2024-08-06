import os
import streamlit as st
from src.utils import clear_history
from src.document_loader import load_document
from src.chunker import chunk_data
from src.embeddings import create_embeddings, calculate_embedding_cost
from src.qa import ask_and_get_answer
from streamlit_chat import message

def run_app():
    st.image('images/WashU_Buddy_Logo.png')

    if 'file_list' not in st.session_state:
        st.session_state.file_list = []

    with st.sidebar:
        api_key = st.text_input('OpenAI API Key:', type='password')
        if api_key:
            os.environ['OPENAI_API_KEY'] = api_key

        uploaded_file = st.file_uploader('Upload a file:', type=['pdf', 'docx', 'txt', 'csv'])
        chunk_size = st.number_input('Chunk size:', min_value=100, max_value=2048, value=512, on_change=clear_history)
        k = st.number_input('k', min_value=1, max_value=20, value=3, on_change=clear_history)
        add_data = st.button('Add Data', on_click=clear_history)

        if uploaded_file and add_data:
            with st.spinner('Reading, chunking, and embedding file ...'):
                bytes_data = uploaded_file.read()
                file_name = os.path.join('files', uploaded_file.name)
                with open(file_name, 'wb') as f:
                    f.write(bytes_data)

                data = load_document(file_name)
                chunks = chunk_data(data, chunk_size=chunk_size)
                st.write(f'Chunk size: {chunk_size}, Chunks: {len(chunks)}')

                tokens, embedding_cost = calculate_embedding_cost(chunks)
                st.write(f'Embedding cost: ${embedding_cost:.4f}')

                vector_store = create_embeddings(chunks)
                
                st.session_state.vs = vector_store
                st.session_state.file_list.append(uploaded_file.name)
                st.success('File has been successfully uploaded.')

        st.divider()
        st.write("Uploaded Files:")
        for file in st.session_state.file_list:
            st.write(file)

    if 'history' not in st.session_state:
        st.session_state.history = []

    q = st.text_input('WASHU BUDDY ADMIN PANEL', placeholder='Ask me anything about Washington University in St. Louis...')
    if q:
        if 'vs' in st.session_state:
            vector_store = st.session_state.vs
            answer = ask_and_get_answer(vector_store, q, k)
            
            st.session_state.history.append({"text": q, "is_user": True})
            st.session_state.history.append({"text": answer, "is_user": False})

    for chat in st.session_state.history:
        message(chat['text'], is_user=chat['is_user'])
