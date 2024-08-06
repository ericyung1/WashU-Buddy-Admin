import os
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader, CSVLoader

def load_document(file):
    name, extension = os.path.splitext(file)

    if extension == '.pdf':
        print(f'Loading {file}')
        loader = PyPDFLoader(file)
    elif extension == '.docx':
        print(f'Loading {file}')
        loader = Docx2txtLoader(file)
    elif extension == '.txt':
        loader = TextLoader(file)
    elif extension == '.csv':
        loader = CSVLoader(file)
    else:
        print('Document format is not supported.')
        return None
    data = loader.load()
    return data
