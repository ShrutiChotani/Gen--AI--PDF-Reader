from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(
        base_url='http://localhost:11434',  # Update this if your base URL is different
        model='nomic-embed-text'
    )
    return embeddings

