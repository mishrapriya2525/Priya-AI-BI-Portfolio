from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.load_documents import load_medical_documents
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

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


def answer_query(query):

    docs = retrieve_documents(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    generator = pipeline(
        "text-generation",
        model="google/flan-t5-base"
    )

    prompt = f"""
    Answer the medical question using the context below.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    result = generator(prompt, max_length=200)

    return result[0]["generated_text"]