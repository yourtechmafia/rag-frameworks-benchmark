"""Score pipeline answers with Ragas 0.4.3 (Haiku 4.5 as judge, temperature 0).

Metrics: faithfulness, context precision (with reference), context recall,
answer correctness. Writes <result_dir>/ragas_run1.csv and prints the means.

Usage (eval venv, through the ledger proxy on :8787):
    python eval/score.py results/clean/langchain [results/clean/llamaindex ...]
Run one process per result directory to score them in parallel.
"""
import json
import sys
from pathlib import Path

from langchain_anthropic import ChatAnthropic
from langchain_huggingface import HuggingFaceEmbeddings
from ragas import EvaluationDataset, evaluate
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import AnswerCorrectness, Faithfulness, LLMContextPrecisionWithReference, LLMContextRecall
from ragas.run_config import RunConfig

REPO = Path(__file__).resolve().parents[1]
GOLD = {q["id"]: q for q in map(json.loads, open(REPO / "questions" / "questions.jsonl"))}

emb = LangchainEmbeddingsWrapper(HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5", model_kwargs={"device": "cpu"}))
METRICS = [Faithfulness(), LLMContextPrecisionWithReference(), LLMContextRecall(), AnswerCorrectness()]


def score(result_dir: Path, run: int = 1) -> None:
    rows = [json.loads(l) for l in open(result_dir / f"run{run}.jsonl")]
    samples = [{
        "user_input": r["question"],
        "response": r["answer"] or "I don't know.",
        "retrieved_contexts": [c["text"] for c in r["contexts"]] or [""],
        "reference": GOLD[r["id"]]["reference"],
    } for r in rows]
    # The proxy logs each call under this phase, so several scorers can run in parallel.
    phase = f"judge-{result_dir.parent.name}-{result_dir.name}"
    llm = LangchainLLMWrapper(ChatAnthropic(model="claude-haiku-4-5", temperature=0, max_tokens=4096,
                                            default_headers={"x-bench-phase": phase}))
    result = evaluate(EvaluationDataset.from_list(samples), metrics=METRICS, llm=llm, embeddings=emb,
                      run_config=RunConfig(max_workers=12, timeout=240), show_progress=False)
    df = result.to_pandas()
    df.insert(0, "id", [r["id"] for r in rows])
    df.drop(columns=["retrieved_contexts", "response", "reference", "user_input"]).to_csv(
        result_dir / f"ragas_run{run}.csv", index=False)
    cols = ["faithfulness", "llm_context_precision_with_reference", "context_recall", "answer_correctness"]
    print(result_dir, {c: round(df[c].mean(), 3) for c in cols if c in df}, "nan:", int(df[cols].isna().sum().sum()))


if __name__ == "__main__":
    for d in sys.argv[1:]:
        score(Path(d))
