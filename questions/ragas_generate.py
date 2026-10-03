"""Generate candidate questions with Ragas 0.4.3 from a stratified sample of the
cleaned corpus. Every candidate is reviewed by hand before it enters
questions.jsonl; this script only writes questions/ragas_candidates.jsonl.

Generator LLM: claude-haiku-4-5 (temperature 0). Embeddings: BAAI/bge-small-en-v1.5.
"""
import csv
import json
import random
from pathlib import Path

from langchain_anthropic import ChatAnthropic
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.run_config import RunConfig
from ragas.testset import TestsetGenerator
from ragas.testset.graph import KnowledgeGraph, Node, NodeType
from ragas.testset.transforms import apply_transforms, default_transforms
from ragas.testset.transforms.splitters import HeadlineSplitter
from ragas.testset.synthesizers import (
    MultiHopSpecificQuerySynthesizer,
    SingleHopSpecificQuerySynthesizer,
)

REPO = Path(__file__).resolve().parents[1]
CORPUS = REPO / "corpus"
SAMPLE = {"uv": 18, "pnpm": 24, "go-echarts": 10, "docsify": 8}
random.seed(42)


def load_sample():
    rows = list(csv.DictReader(open(CORPUS / "manifest.csv")))
    docs = []
    for site, n in SAMPLE.items():
        pool = []
        for r in rows:
            if r["site"] != site:
                continue
            path = CORPUS / "clean" / Path(r["file"]).relative_to("markdown")
            text = path.read_text()
            if 1500 <= len(text) <= 15000:
                pool.append(Document(page_content=text, metadata={"url": r["url"], "site": site}))
        docs += random.sample(pool, min(n, len(pool)))
    return docs


def main():
    docs = load_sample()
    print(f"{len(docs)} documents sampled")
    llm = LangchainLLMWrapper(ChatAnthropic(model="claude-haiku-4-5", temperature=0, max_tokens=4096))
    emb = LangchainEmbeddingsWrapper(HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5", model_kwargs={"device": "cpu"}))
    run_config = RunConfig(max_workers=4, timeout=180)
    kg_path = REPO / "questions" / "ragas_kg.json"
    if kg_path.exists():  # checkpoint: the LLM transforms are the expensive part
        kg = KnowledgeGraph.load(kg_path)
    else:
        # Ragas 0.4.3 bug: HeadlineSplitter runs on every document, but headlines are only
        # extracted for documents over 500 tokens, so short documents crash the run.
        # Restrict the splitter to nodes that actually have headlines.
        transforms = default_transforms(docs, llm, emb)
        for t in transforms:
            if isinstance(t, HeadlineSplitter):
                t.filter_nodes = lambda n: n.type == NodeType.DOCUMENT and bool(n.properties.get("headlines"))
        kg = KnowledgeGraph(nodes=[
            Node(type=NodeType.DOCUMENT, properties={"page_content": d.page_content, "document_metadata": d.metadata})
            for d in docs
        ])
        apply_transforms(kg, transforms, run_config=run_config)
        kg.save(kg_path)
    gen = TestsetGenerator(llm=llm, embedding_model=emb, knowledge_graph=kg)
    dist = [
        (SingleHopSpecificQuerySynthesizer(llm=llm), 0.6),
        (MultiHopSpecificQuerySynthesizer(llm=llm), 0.4),
    ]
    testset = gen.generate(testset_size=60, query_distribution=dist, run_config=run_config, raise_exceptions=False)
    out = REPO / "questions" / "ragas_candidates.jsonl"
    with open(out, "w") as f:
        for s in testset.to_list():
            f.write(json.dumps(s) + "\n")
    print(f"wrote {len(testset.to_list())} candidates to {out}")


if __name__ == "__main__":
    main()
