from config.settings import settings 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma 

def retrieve_context(query: str):
    vectorstore = Chroma(
        embedding_function = HuggingFaceEmbeddings(model = settings.EMBEDDING_MODEL),
        persist_directory = settings.CHROMA_PATH
    )
    
    res = vectorstore.similarity_search(query, k = 3)
    
    context = "\n\n".join([chunk.page_content for chunk in res])
    
    return context