# Question set review

`questions.jsonl` holds 100 questions: 57 handwritten (`handwritten.py`) and 43 kept from 60 Ragas 0.4.3 candidates (`ragas_candidates.jsonl` → `ragas_reviewed.jsonl`). Every question carries `gold_urls` (pages that contain the answer), `hop` (single/multi, by number of gold pages) and `js_only` (all gold pages are client-rendered, so a default loader can never retrieve them).

## How Ragas candidates were generated
- 54 cleaned pages sampled per site (`ragas_generate.py`, seed 42), Haiku 4.5 at temperature 0, bge-small embeddings.
- Single-hop specific (60%) and multi-hop specific (40%) synthesizers. Typos in Ragas questions are deliberate persona noise and were kept.

## Rejected candidates (17)
| # | Reason |
| --- | --- |
| 10 | Vague (tqdm in a workspace) and answer restates the example only |
| 12 | Trivial (where README.md sits) |
| 14 | Mixed two unrelated topics; reference answer was wrong about `uv run --with` |
| 20 | Duplicate of handwritten h027 (uvx vs uv tool install) |
| 24 | Garbled question ("installing packages on Linux without creating a kernel") |
| 33 | Duplicate of handwritten h026 (cache keys) |
| 35 | Duplicate of handwritten h025 (`uv cache prune --ci`) |
| 36 | Persona padding; answer is generic |
| 37 | Duplicate of #45 |
| 41 | Nonsense multi-hop (go-echarts imports + Python virtual environments) |
| 46 | Duplicate of #32 |
| 47 | Duplicate of #23 |
| 49 | Duplicate of handwritten h034 (workspace lockfile) |
| 52 | Duplicate of handwritten h026 |
| 55 | Nonsense multi-hop (uv cache + ruff "reproducibility") |
| 57 | Nonsense multi-hop (pnpm config + docsify embeds) |
| 59 | Near-duplicate of #60 (yAxis) |

## Edits
- #7: question rewritten for clarity ("Where foo module supposed to be located…" → explicit uv build backend wording).
- #34: reference corrected (cache-physical-space works on macOS **and** Linux).
- Gold URLs for 12 candidates were mapped by text overlap with the frozen pages, then checked by hand; spurious second URLs on #38 and #40 were removed.
