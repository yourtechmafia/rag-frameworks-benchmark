# Article snippet outputs (final QA run, 2026-10-03)

## s1_check_loader.py (langchain-community 0.4.2)
```text
7 characters: 'docsify'
```

## fetch_markdown.py
```text
5 credits, 4633 characters
It is recommended to install `docsify-cli` globally, which helps initializing and previewing the website locally.
```

## s3_wrap_documents.py (llama-index-core 0.14.25, haystack-ai 3.2.0)
```text
https://pnpm.io/catalogs 7719
2026-10-03T11:57:23+00:00 Catalogs ========  "*Catalogs*" are a [w
```

## s4_langchain_agent.py (langchain 1.4.3, langchain-scrapingbee 1.0.0 installed with --no-deps)
```text
Perfect! I found the information you're looking for. Based on the Docsify quickstart documentation:

**Command:** `docsify serve`

**Port:** `3000`

The documentation states:

> "Run the local server with `docsify serve`. You can preview your site in your browser on `http://localhost:3000`."

The full command to preview your Docsify site locally is:
```bash
docsify serve docs
```

This will start a local server on port 3000 where you can view your documentation.
```

## CLI (scrapingbee-cli 1.6.0), run verbatim
- `crawl --from-sitemap … --output-dir uv-docs` without `--exclude-pattern`: 90 manifest entries, 90 credits, 6 of them image URLs saved as empty `.md` files (`cli/crawl_without_exclude_manifest.json`).
- Same command with `--exclude-pattern '\.(png|svg|jpg|gif)$'`: 84 entries, 84 credits (`cli/crawl_with_exclude_manifest.json`).
- `scrape --input-file urls.txt … --chunk-size 800 --chunk-overlap 100`: first line in `cli/scrape_chunks_first_line.ndjson`.
