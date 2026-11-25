# make.fun — "Sum up 25 November's world news in one image"
# Bounty: news-image-20261125

Self-contained, offline Python 3.13 generator that turns the day's news cycle
into a single 1024×1024 PNG (under 1 MiB) at `/output/entry.png`.

## Entry requirements (from make.fun/bounty/news-image-20261125)

* Program writes one image to `/output/entry.png`.
* Image is a whole PNG or JPEG of at most **1 MiB** and **1024 × 1024 px**.
* **No network**: two runs must produce identical bytes.
* Program lives at `main.py` in the repository root (Python 3.13).

## Requirements

```
Pillow>=10.0
numpy>=1.26
```

## How to run

```
python -m venv .venv
.venv/bin/pip install -r requirements.txt
python main.py            # writes /output/entry.png (or env ENTRY_OUTPUT)
```

Output constraints are self-checked on every run.

## Tests

```
.venv/bin/python -m unittest discover -s tests -v
```

## License

MIT — see [LICENSE](LICENSE).
