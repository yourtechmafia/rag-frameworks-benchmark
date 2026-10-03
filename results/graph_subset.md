| Pipeline | Indexing cost | Index LLM calls | Query p50 / p95 | Input tokens per query | Answer correctness | Faithfulness | Context recall | Context precision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline | $0.00 | 0 | 1.97 s / 2.52 s | 994 | 0.709 | 0.940 | 0.716 | 0.624 |
| lightrag | $5.98 | 834 | 6.48 s / 10.46 s | 28,150 | 0.672 | 0.862 | 0.973 | n/a (4 of 40 scored) |
| graphrag | $10.53 | 1715 | 5.80 s / 10.59 s | 10,547 | 0.657 | 0.843 | 0.939 | 0.757 |

lightrag answer_correctness vs plain Python: -0.037 (95% CI -0.088 to +0.015)
lightrag faithfulness vs plain Python: -0.077 (95% CI -0.137 to -0.020)
lightrag context_recall vs plain Python: +0.257 (95% CI +0.149 to +0.374)
graphrag answer_correctness vs plain Python: -0.052 (95% CI -0.099 to -0.003)
graphrag faithfulness vs plain Python: -0.097 (95% CI -0.180 to -0.023)
graphrag context_recall vs plain Python: +0.223 (95% CI +0.111 to +0.336)
