from langchain.text_splitter import RecursiveCharacterTextSplitter
from ingestion.load_documents import load_medical_documents


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