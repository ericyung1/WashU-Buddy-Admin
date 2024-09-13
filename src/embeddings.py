from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import tiktoken
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

def create_embeddings(chunks, index):
    embeddings = OpenAIEmbeddings()
    vectors = []
    for i, chunk in enumerate(chunks):
        #embedding = embeddings.embed(chunk.page_content)
        embedding = embeddings.embed_documents([chunk.page_content])[0]
        vectors.append((f'vector_{i}', embedding))
    index.upsert(vectors)
    return index

def calculate_embedding_cost(texts):
    enc = tiktoken.encoding_for_model('text-embedding-ada-002')
    total_tokens = sum([len(enc.encode(page.page_content)) for page in texts])
    return (total_tokens, total_tokens / 1000 * 0.0004)
