from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from rag_pipeline.rag_engine import chunk_documents


def create_vector_store():

    chunks = chunk_documents()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(chunks, embeddings)

    vector_store.save_local("vector_db")

    return vector_store


if __name__ == "__main__":
    create_vector_store()
    print("Vector database created successfully")