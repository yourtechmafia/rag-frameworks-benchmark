"""LangChain 1.x RAG: text splitter + HuggingFace embeddings + Qdrant + ChatAnthropic."""
import os

from langchain_anthropic import ChatAnthropic
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

from harness import PROMPT, SETTINGS

COLLECTION = os.environ.get("RAGBENCH_COLLECTION", "langchain")
embeddings = HuggingFaceEmbeddings(
    model_name=SETTINGS["embedding_model"],
    query_encode_kwargs={"prompt": SETTINGS["query_prefix"]},
)
llm = ChatAnthropic(model=SETTINGS["llm"], temperature=SETTINGS["temperature"], max_tokens=SETTINGS["max_tokens"])
prompt = ChatPromptTemplate.from_messages([("human", PROMPT)])
chain = prompt | llm
store = None


def build_index(docs):
    global store
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=SETTINGS["chunk_size_chars"], chunk_overlap=SETTINGS["chunk_overlap_chars"]
    )
    chunks = splitter.split_documents(
        [Document(page_content=d["text"], metadata={"url": d["url"]}) for d in docs]
    )
    store = QdrantVectorStore.from_documents(
        chunks, embeddings, url=SETTINGS["qdrant_url"], collection_name=COLLECTION, force_recreate=True
    )


def answer(question):
    global store
    if store is None:
        store = QdrantVectorStore.from_existing_collection(
            embedding=embeddings, collection_name=COLLECTION, url=SETTINGS["qdrant_url"]
        )
    hits = store.similarity_search(question, k=SETTINGS["top_k"])
    context = "\n\n".join(h.page_content for h in hits)
    reply = chain.invoke({"context": context, "question": question})
    return {"answer": reply.content,
            "contexts": [{"text": h.page_content, "url": h.metadata["url"]} for h in hits]}
