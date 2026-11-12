# Check mathematics in the actual GitHub renderer

The [workflow](../../.github/workflows/hosted-math.yml) checks the exact proposed commit on same-repository pull requests. It has read-only repository permissions, uses no secrets and does not retain checkout credentials. It runs the finite scientific checks, probes the README and compares every mathematical expression on all tracked Markdown pages at widths 1440 and 760.

The collector compares actual accessible MathML from commit-pinned GitHub pages with locally compiled source MathML, including expression counts, symbols, structure and display geometry. The explicit [text contract](math-contract.json) adds checks for headline formulas. This is a hosted rendering test; it does not prove mathematical correctness, novelty or every aspect of visual readability. Screenshots still require inspection.

For a local run, use Node 18 or later, Python 3.10 or later, Git, Playwright and MathJax. The workflow pins Playwright 1.56.1 and MathJax 3.2.1. Install dependencies outside the source tree, then run:

```bash
node verification/hosted_math/probe_hosted_math.cjs \
  --root /absolute/checkout --repository GoGoKo699/Heralded-Entanglement-Borrowing \
  --revision FULL_COMMIT_SHA --page README.md --output /absolute/new-probe

node verification/hosted_math/capture_hosted_math.cjs \
  --root /absolute/checkout --repository GoGoKo699/Heralded-Entanglement-Borrowing \
  --revision FULL_COMMIT_SHA --contract verification/hosted_math/math-contract.json \
  --output /absolute/new-captures
```

Use an actual 40-character commit and a new output directory. The collector reads Git objects; dirty working files do not replace the pinned source. `NODE_PATH` must resolve the chosen runtime packages. An unavailable browser, connection failure or renderer defect remains a failed check until diagnosed and resolved.

These collector/checker files are retained unchanged as one compatible version set:

| File | Git blob identity |
|---|---|
| `capture_hosted_math.cjs` | `6f36ee03223a82d0075da2fe903f21bc5a45a75b` |
| `check_rendered_math.py` | `1d3bf9810d0dfadb844a48b354af80f9b66924bc` |
| `probe_hosted_math.cjs` | `f83ea9da799bee0b53bd5c57315ae2b4b2d9de43` |

The workflow's artifact retention is temporary. A green job does not replace source-bound review of the actual report and screenshots. [Scientific verification](../README.md) documents the distinct analytical and finite-numerical evidence.
