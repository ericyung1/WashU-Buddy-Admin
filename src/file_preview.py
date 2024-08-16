# file_preview.py
import os
import streamlit as st
import pandas as pd
import pdfplumber
import docx

def file_preview():
    st.divider()
    st.write("Uploaded Files:")
    for file_name in st.session_state.file_list:
        file_path = os.path.join('files', file_name)
        file_extension = file_name.split('.')[-1]

        with st.expander(file_name):
            if file_extension == 'txt':
                with open(file_path, "r") as f:
                    file_content = f.read()
                st.text_area("File Content", file_content)
            elif file_extension == 'csv':
                df = pd.read_csv(file_path)
                st.dataframe(df)
            elif file_extension == 'pdf':
                with pdfplumber.open(file_path) as pdf:
                    for page in pdf.pages:
                        pil_image = page.to_image().original
                        st.image(pil_image)
            elif file_extension == 'docx':
                doc = docx.Document(file_path)
                doc_text = "\n".join([para.text for para in doc.paragraphs])
                st.text_area("DOCX Content", doc_text)
            else:
                st.write("Preview not available for this file type.")
