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
    full_text = "".join([doc.page_content for doc in documents])
    # full_document = Document(page_content=full_text.replace(" ", ""))
    separators=[
        r"(?:\n|^|\s*)第\s+[一二三四五六七八九十百千萬零]+\s+章.*\n",
        r"(?:\n|^|\s*)第\s+\d+\s+條.*\n",
        r"(?:\n|^|\s*)第\s+\d+-+\d+\s+條.*\n",
    ]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 5, chunk_overlap = 0, separators = separators, is_separator_regex = True)
    texts = text_splitter.split_text(full_text)
    return len(texts)

print(hw02_2(q2_pdf))