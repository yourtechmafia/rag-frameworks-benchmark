"""Run each framework's built-in web loader on a client-rendered page and a
server-rendered page; print how many characters of real content come back."""
import warnings; warnings.filterwarnings("ignore")
JS = "https://docsify.js.org/#/quickstart"          # Docsify, rendered in the browser
SSR = "https://pnpm.io/catalogs"                     # Docusaurus, rendered on the server
MARK = {JS: "docsify-cli", SSR: "catalog:"}          # a phrase from the article body

def report(name, url, text):
    text = " ".join((text or "").split())
    print(f"{name:42} {'JS ' if url == JS else 'SSR'} {len(text):6} chars  contains article text: {MARK[url] in text}")

from langchain_community.document_loaders import WebBaseLoader
for u in (JS, SSR):
    report("LangChain WebBaseLoader", u, WebBaseLoader(u).load()[0].page_content)

from llama_index.readers.web import SimpleWebPageReader, TrafilaturaWebReader
for u in (JS, SSR):
    report("LlamaIndex SimpleWebPageReader(html_to_text)", u, SimpleWebPageReader(html_to_text=True).load_data([u])[0].text)
    try:
        report("LlamaIndex TrafilaturaWebReader", u, TrafilaturaWebReader().load_data([u])[0].text or "")
    except Exception as e:
        print(f"{'LlamaIndex TrafilaturaWebReader':42} {u}: {type(e).__name__}: {e}")

from haystack import Pipeline
from haystack.components.fetchers import LinkContentFetcher
from haystack.components.converters import HTMLToDocument
p = Pipeline(); p.add_component("fetch", LinkContentFetcher()); p.add_component("html", HTMLToDocument())
p.connect("fetch.streams", "html.sources")
for u in (JS, SSR):
    docs = p.run({"fetch": {"urls": [u]}})["html"]["documents"]
    report("Haystack LinkContentFetcher + HTMLToDocument", u, docs[0].content if docs else "")
