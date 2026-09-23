# IDX-Exchange-NLP

12-week NLP internship project — Real Estate Listing Intelligence System, built over
MLS data (`rets_property`, `rets_openhouse`, `california_sold`).

## Setup (Week 0)

1. Install Docker Desktop (allocate 4GB+ RAM) and Python 3.11+.
2. `pip install -r requirements.txt`
3. `docker-compose up -d` — starts a MySQL 8.0 container and auto-imports the SQL
   dumps in `data/raw/` (not committed to git — see `.gitignore`).
4. `python tests/test_setup.py` — verifies Python version, packages, and DB connection.

## Structure

```
data/{raw,processed,models}   # raw/processed data — gitignored, never pushed
scripts/                      # pipeline code (cleaning, extraction, parsing, etc.)
tests/                        # pytest suite
notebooks/                    # exploration notebooks
```

## Roadmap

See internal project docs for the full Week 1–12 plan (taxonomy → text cleaning →
entity extraction → query parsing → semantic search → signal extraction → intent
classification → summarization → fair housing compliance → REST API → demo → defense).
