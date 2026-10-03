# Third-party content in `corpus/` and `results/`

The corpus is a frozen snapshot (October 3, 2026) of public documentation pages, kept here so the benchmark can be reproduced. Each page belongs to its project and is redistributed under that project's licence:

| Site | Source repository | Licence |
| --- | --- | --- |
| https://docs.astral.sh/uv/ | https://github.com/astral-sh/uv | Apache-2.0 (uv is dual-licensed Apache-2.0 / MIT) |
| https://pnpm.io/ | https://github.com/pnpm/pnpm.io | MIT |
| https://go-echarts.github.io/go-echarts/ | https://github.com/go-echarts/go-echarts | MIT |
| https://docsify.js.org/ | https://github.com/docsifyjs/docsify | MIT |

Retrieved chunks quoted in `results/` come from the same pages. Every file's source URL, fetch time and SHA-256 hash are in `corpus/manifest.csv`.

The benchmark code itself is under the MIT licence in `LICENSE`.
