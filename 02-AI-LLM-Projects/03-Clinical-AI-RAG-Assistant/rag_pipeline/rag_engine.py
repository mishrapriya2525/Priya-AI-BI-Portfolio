from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.load_documents import load_medical_documents
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS



def chunk_documents():

    documents = load_medical_documents()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":
    chunks = chunk_documents()
    print(f"Created {len(chunks)} text chunks")
    


def load_vector_store():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


def retrieve_documents(query):

    vector_store = load_vector_store()

    docs = vector_store.similarity_search(query, k=3)

    return docs