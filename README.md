# make.fun — "Sum up 25 November's world news in one image"
# Bounty: news-image-20261125

Self-contained, offline Python 3.13 generator that turns the day's news cycle
into a single 1024×1024 PNG (under 1 MiB) at `/output/entry.png`.

## What this repo contains
- `main.py` — deterministic image generator (entry program).
- `README.md` — this brief + run/test instructions.
- `LICENSE` — MIT License.
- `requirements.txt` — runtime dependencies.
- `tests/test_entry.py` — self-test suite (7 tests).
- `AGENT_TRANSCRIPT.md` — AI-coding-agent session transcript.
- `.gitignore` — excludes caches, venv, dist, etc.

## Entry requirements (from make.fun/bounty/news-image-20261125)
* Program writes one image to `/output/entry.png`.
* Image is a whole PNG or JPEG of at most **1 MiB** and **1024 × 1024 px**.
* **No network**: two runs must produce identical bytes.
* Program lives at `main.py` in the repository root (Python 3.13).

## Run
```
python -m venv .venv
.venv/bin/pip install -r requirements.txt
python main.py            # writes /output/entry.png (env ENTRY_OUTPUT overrides)
```

## Tests
```
.venv/bin/python -m unittest discover -s tests -v
```

## Submit
* Public repo: `<github-username>/news-image-20261125`
* Delivery files (do NOT include API tokens):
  1. Public GitHub repo URL
  2. `main.py` (in repo)
  3. AI-coding-agent transcript(s)
* Follow make.fun's submission flow for your agent.

## License
MIT — see [LICENSE](LICENSE).
