from langchain_community.document_loaders import WebBaseLoader

url = "https://docsify.js.org/#/quickstart"
doc = WebBaseLoader(url).load()[0]
text = doc.page_content.strip()
print(f"{len(text)} characters: {text[:80]!r}")
