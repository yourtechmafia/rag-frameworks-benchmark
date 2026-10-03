# RAG frameworks benchmark (October 2026)

The same retrieve-and-answer pipeline built in LangChain, LlamaIndex, Haystack, DSPy and plain Python, run on one frozen corpus of 310 scraped documentation pages with identical settings. LightRAG and Microsoft GraphRAG ran a separate graph test on a 100-page subset. Everything in the accompanying article comes from the files in this repo.

Run date: **October 3, 2026**. Python 3.12.15, Apple Silicon Mac.

## Headline results

| Pipeline | Lines of code | p50 / p95 latency | Cost per 100 questions | Answer correctness | Context precision |
| --- | --- | --- | --- | --- | --- |
| Plain Python | 47 | 1.88 s / 2.67 s | $0.167 | 0.637 | 0.515 |
| LangChain 1.4.3 | 34 | 1.78 s / 2.73 s | $0.164 | 0.641 | 0.556 |
| LlamaIndex 0.14.25 | 37 | 1.84 s / 2.52 s | $0.163 | 0.631 | 0.518 |
| Haystack 3.2.0 | 48 | 1.81 s / 2.96 s | $0.173 | 0.641 | **0.605** |
| DSPy 3.4.0 | 53 | 2.00 s / 2.75 s | $0.200 | 0.641 | 0.528 |

- Answer correctness is a statistical tie (paired bootstrap, `results/significance.md`). The only real difference is Haystack's context precision.
- Ingestion mattered more than the framework. Indexing ScrapingBee markdown instead of default-loader text raised answer correctness from 0.498 to 0.637, and from 0.217 to 0.610 on JavaScript-only questions (`results/ingestion_quality.md`).
- Graph test (`results/graph_subset.md`): LightRAG indexed 100 pages for $5.98 and GraphRAG for $10.53. Both had higher context recall but no better answers on these specific questions.

## Layout

| Path | What's in it |
| --- | --- |
| `corpus/urls.csv`, `corpus/manifest.csv` | The 310 URLs, with fetch time, credits and SHA-256 for every page |
| `corpus/raw/`, `corpus/default/`, `corpus/markdown/`, `corpus/clean/` | Plain-GET HTML; the text `WebBaseLoader` extracts from it; ScrapingBee markdown; cleaned markdown |
| `corpus/crawl.py`, `corpus/default_loader.py`, `corpus/clean.py` | How each version was produced |
| `questions/questions.jsonl` | 100 questions with reference answers, gold URLs and tags (57 handwritten, 43 from Ragas) |
| `questions/REVIEW.md` | Which Ragas candidates were rejected and why |
| `pipelines/<framework>/rag.py` | One pipeline per framework; each folder has its own `pyproject.toml` and `uv.lock` |
| `pipelines/harness.py` | Shared settings, prompt, timing and output (not counted in lines of code) |
| `results/<variant>/<pipeline>/run{1,2,3}.jsonl` | Every answer with its retrieved chunks and latency |
| `results/<variant>/<pipeline>/ragas_run1.csv` | Ragas scores per question |
| `results/*.md`, `results/*.csv` | Summary tables, significance tests, overhead, footprint, import time |
| `eval/` | Scoring (Ragas), retrieval metrics, summaries, charts |
| `ledger/spend.csv` | Every Anthropic API call: phase, tokens, cost, latency |
| `proxy/ledger_proxy.py` | The logging proxy that produced the ledger |
| `article_snippets/` | The code blocks from the article, exactly as published, and their output |

## Settings shared by every pipeline

- LLM: Claude Haiku 4.5 (`claude-haiku-4-5`), temperature 0, max 512 output tokens
- Embeddings: `BAAI/bge-small-en-v1.5` (local), with BGE's query prefix
- Vector store: Qdrant 1.19.1 (Docker), cosine
- Chunks: 800 characters, 100 overlap (bge-small truncates at 512 tokens, so token-sized 800 chunks would be cut)
- Top-k 5, one prompt (`pipelines/harness.py`), 3 runs per question, round-robin across frameworks

## Reproduce

```bash
# 1. Qdrant
docker run -d --name ragbench-qdrant -p 127.0.0.1:6333:6333 qdrant/qdrant:v1.19.1

# 2. Logging proxy (records every API call to ledger/spend.csv)
export ANTHROPIC_API_KEY=...
python proxy/ledger_proxy.py 8788 &

# 3. One pipeline (uses pipelines/<framework>/uv.lock)
cd pipelines/langchain && UV_PROJECT_ENVIRONMENT=~/ragbench/envs/langchain uv sync --frozen && cd ../..
scripts/run.sh langchain --reindex --runs 3

# 4. Score it
python eval/score.py results/clean/langchain      # in the env locked in eval/env (ragas 0.4.3)
python eval/summarize.py
```

`corpus/crawl.py` needs a ScrapingBee key (`SCRAPINGBEE_API_KEY`) only if you want to re-crawl. The frozen corpus is already here.

## Known issues we hit (and worked around)

- **Anthropic Python SDK 1.x** removed `temperature` from `messages.create()`. `llama-index-llms-anthropic` 0.12.2, `anthropic-haystack` 6.2.0/6.3.0 and LightRAG 1.5.7 still pass it, so those environments pin `anthropic<1`. LlamaIndex returned "Empty Response" instead of raising.
- **DSPy 3.4.0** installs a lazy numpy proxy; `import qdrant_client` after `import dspy` crashes. `pipelines/dspy/rag.py` imports numpy first.
- **Ragas 0.4.3** needs `langchain-community<0.4`, and its `HeadlineSplitter` crashes on short documents (patched in `questions/ragas_generate.py`).
- **GraphRAG 3.2** defaults to a 3,072-dimension vector store and needed a larger output cap for community reports (`pipelines/graphrag/rag.py`).
- **LightRAG 1.5.7** de-duplicates documents by the last segment of their path, so two URLs ending in `/python` collided and one page was dropped from the graph subset.

## Cost

About $55 of Anthropic API calls in total (answers, Ragas test-set generation, judging, both graph pipelines), itemized by phase in `ledger/spend.csv` (`python scripts/spend.py`). The 310 kept pages cost 554 ScrapingBee credits (557 including 3 redirect URLs that were dropped).
