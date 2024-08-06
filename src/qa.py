from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

def ask_and_get_answer(vector_store, q, k=3):
    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)
    retriever = vector_store.as_retriever(search_type='similarity', search_kwarg={'k': k})
    memory = ConversationBufferMemory(memory_key='chat_history', return_message=True)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        chain_type='stuff',
        verbose=True
    )
    response = chain.invoke(q)
    print(response)  # Debug print statement
    answer = response['answer']  # This line might need to be updated based on the actual response structure
    return answer
