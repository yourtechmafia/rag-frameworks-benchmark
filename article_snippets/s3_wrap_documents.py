from datetime import datetime, timezone

from haystack import Document as HaystackDocument
from llama_index.core import Document as LlamaDocument

from fetch_markdown import fetch_markdown

url = "https://pnpm.io/catalogs"
markdown, credits = fetch_markdown(url)  # server-rendered page: no JS rendering needed
meta = {"url": url, "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}

llama_doc = LlamaDocument(text=markdown, metadata=meta)
haystack_doc = HaystackDocument(content=markdown, meta=meta)

print(llama_doc.metadata["url"], len(llama_doc.text))
print(haystack_doc.meta["fetched_at"], haystack_doc.content[:40].replace("\n", " "))
