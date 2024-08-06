from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import tiktoken

def create_embeddings(chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(chunks, embeddings)
    return vector_store

def calculate_embedding_cost(texts):
    enc = tiktoken.encoding_for_model('text-embedding-ada-002')
    total_tokens = sum([len(enc.encode(page.page_content)) for page in texts])
    return (total_tokens, total_tokens / 1000 * 0.0004)
