from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
from langchain.docstore.document import Document

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader("./"+q1_pdf)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size = 2000, chunk_overlap = 0)
    texts = text_splitter.split_documents(documents)
    # print(texts[-1])
    # print(len(texts))
    return texts[-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader("./"+q2_pdf)
    documents = loader.load()
    full_text = "\n".join([doc.page_content for doc in documents])
    full_document = Document(page_content=full_text.replace(" ", ""))
    separators=[
        "\n第"
    ]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 60, chunk_overlap = 0, separators = separators)
    texts = text_splitter.split_documents([full_document])
    return len(texts)

# hw02_2(q2_pdf)