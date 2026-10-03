"""Time each framework's own imports in a fresh process, 7 times, median.

The shared stack (torch, sentence-transformers, numpy) is imported first and
not counted, so the number is the framework's own import overhead.
Usage: python scripts/import_time.py <framework>   (inside that framework's venv)
"""
import json
import statistics
import subprocess
import sys

MODULES = {
    "baseline": ["anthropic", "qdrant_client"],
    "langchain": ["langchain_anthropic", "langchain_core.prompts", "langchain_huggingface",
                  "langchain_qdrant", "langchain_text_splitters"],
    "llamaindex": ["llama_index.core", "llama_index.embeddings.huggingface",
                   "llama_index.llms.anthropic", "llama_index.vector_stores.qdrant"],
    "haystack": ["haystack", "haystack.components.preprocessors",
                 "haystack_integrations.components.embedders.sentence_transformers",
                 "haystack_integrations.components.generators.anthropic",
                 "haystack_integrations.document_stores.qdrant"],
    "dspy": ["dspy", "qdrant_client"],
    "lightrag": ["lightrag", "lightrag.llm.anthropic"],
    "graphrag": ["graphrag.api"],
}
PRELOAD = "import numpy, torch, sentence_transformers" 

fw = sys.argv[1]
mods = MODULES[fw]
pre = PRELOAD if fw != "graphrag" else "import numpy, pandas"
code = (f"{pre}\nimport time\nt = time.perf_counter()\n"
        + "".join(f"import {m}\n" for m in mods)
        + "print(time.perf_counter() - t)")
times = [float(subprocess.run([sys.executable, "-c", code], capture_output=True, text=True,
                               check=True).stdout.strip().splitlines()[-1]) for _ in range(7)]
print(json.dumps({"framework": fw, "import_s_median": round(statistics.median(times), 3),
                  "runs": [round(t, 3) for t in times]}))
