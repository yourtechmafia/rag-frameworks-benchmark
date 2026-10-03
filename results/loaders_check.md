# Built-in web loaders vs a client-rendered page (2026-10-03)

Script: `eval/loaders_check.py`. Versions: langchain-community 0.4.2, llama-index-readers-web 0.7.0, haystack-ai 3.2.0, trafilatura 2.2.0.

- JS page: https://docsify.js.org/#/quickstart (Docsify renders it in the browser)
- SSR page: https://pnpm.io/catalogs (Docusaurus, server-rendered)

## Run 1

| Loader | JS page | SSR page |
| --- | --- | --- |
| LangChain `WebBaseLoader` | 7 chars ("docsify", the `<title>`) | 6,483 chars, article present |
| LlamaIndex `SimpleWebPageReader(html_to_text=True)` | 0 chars | 6,958 chars, article present |
| LlamaIndex `TrafilaturaWebReader` | 0 chars | 6,180 chars, article present |
| Haystack `LinkContentFetcher` + `HTMLToDocument` | (crashed: the converter returned `None` content) | not reached |

## Run 2, minutes later, after about 170 plain requests to pnpm.io from this IP that hour

| Loader | JS page | SSR page |
| --- | --- | --- |
| LangChain `WebBaseLoader` | 7 chars | 267 chars: **"Vercel Security Checkpoint … Enable JavaScript to continue"**, HTTP 200 |
| LlamaIndex `SimpleWebPageReader(html_to_text=True)` | 0 chars | 292 chars: the same checkpoint page |
| LlamaIndex `TrafilaturaWebReader` | 0 chars | 0 chars |
| Haystack `LinkContentFetcher` + `HTMLToDocument` | 0 chars (`content=None`) | 6,180 chars, article present |

The same URL through the ScrapingBee HTML API right after run 2 (`render_js=false`, `return_page_markdown=true`, 1 credit) returned the full 7,719-character article.

**Takeaways:**
1. None of the built-in loaders runs JavaScript, so the Docsify page comes back empty or as its `<title>`.
2. A bot checkpoint can come back as HTTP 200 and gets indexed as if it were documentation. Nothing errors.

## LangChain `RecursiveUrlLoader("https://docsify.js.org/", max_depth=2)`

Returned 2 documents, both raw HTML (no extractor by default):
1. `https://docsify.js.org/`: the app shell (`<!doctype html>…`), no documentation text.
2. `https://docsify.js.org/${url}`: a 404 page. The loader followed a "link" it found inside a JavaScript template string.

`SitemapLoader` subclasses `WebBaseLoader`, so it fetches the same way (plain HTTP, no JavaScript).
