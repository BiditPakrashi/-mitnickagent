from dotenv import load_dotenv, find_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import AzureOpenAIEmbeddings
import os

load_dotenv(find_dotenv())
print("----------")
print("@@" + os.environ['OPENAI_API_ADA_BASE'])
print("----------")
embeddings = AzureOpenAIEmbeddings(
        azure_endpoint=os.environ['OPENAI_API_ADA_BASE'],
        openai_api_key=os.environ['OPENAI_ADA_KEY'],
        openai_api_version=os.environ['OPENAI_API_VERSION'],
        azure_deployment=os.environ['OPENAI_ADA_IMAGE']
    )

# List of URLs to load documents from
urls = [
    "https://devsecdocs.r3.app.cloud.comcast.net/documentation/checkmarx-jenkins-pipeline-java.html",
    "https://devsecdocs.r3.app.cloud.comcast.net/documentation/teamcity-checkmarx-plugin-implementation.html",
    "https://devsecdocs.r3.app.cloud.comcast.net/documentation/checkmarx-github-actions.html",
    "https://devsecdocs.r3.app.cloud.comcast.net/documentation/checkmarx-azure-pipeline.html",
    "https://devsecdocs.r3.app.cloud.comcast.net/documentation/snyk-self-onboarding-thru-github-cloud-app.html"
]

# Load documents from URLs
docs = [WebBaseLoader(url).load() for url in urls]

# Flatten the list of documents
docs_list = [item for sublist in docs for item in sublist]

# Split documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=2000, chunk_overlap=250
)
doc_splits = text_splitter.split_documents(docs_list)

# Create a Chroma vector store from the document splits
# vectorstore = Chroma.from_documents(
#     documents=doc_splits,
#     collection_name="rag-chroma",
#     embedding=embeddings,
#     persist_directory="./.chroma",
# )

# Create a Chroma retriever
retriever = Chroma(
    collection_name="rag-chroma",
    persist_directory="./.chroma",
    embedding_function=embeddings,
).as_retriever()



