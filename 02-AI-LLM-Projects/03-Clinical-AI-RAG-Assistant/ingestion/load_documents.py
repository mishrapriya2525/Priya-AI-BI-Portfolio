import os
from langchain.document_loaders import PyPDFLoader


def load_medical_documents(data_path="data/medical_papers"):
    documents = []

    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(data_path, file)

            loader = PyPDFLoader(file_path)
            docs = loader.load()

            documents.extend(docs)

    return documents


if __name__ == "__main__":
    docs = load_medical_documents()
    print(f"Loaded {len(docs)} document pages")