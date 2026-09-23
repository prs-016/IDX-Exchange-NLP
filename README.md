# IDX Exchange NLP Internship — Real Estate Listing Intelligence System

## Overview

This repository contains my individual project work for the **IDX Exchange
NLP Internship**, part of the **Fall 2026 cohort (`nlp-fall-2026`)**. It is
submitted as coursework for the internship program and is maintained
individually, in accordance with the program's repository guidelines.

## Project Goal

The goal of this project is to design and build a **Real Estate Listing
Intelligence System**: an end-to-end NLP pipeline that makes unstructured
MLS listing data — primarily free-text agent remarks — searchable,
structured, and safe to serve to end users. Over twelve weeks, the system
grows from raw data exploration into a deployed, tested application, and
touches the following capabilities:

- Domain-specific taxonomy construction from real listing language
- Text cleaning and normalization of MLS remarks
- Named entity extraction (beds, baths, price, square footage, amenities)
- Natural-language query parsing into safe, parameterized SQL
- Semantic search over listings using sentence embeddings
- Structured signal extraction (condition, financing terms, location features)
- Search-intent classification
- Automatic listing summarization
- Fair Housing Act compliance checking
- A production REST API (FastAPI) exposing the above
- A demo web interface and final technical presentation

## What This Repository Is For

This repository holds the **code** for the project as it is built week over
week: data-access scripts, NLP pipeline components, the REST API, tests, and
documentation. It does **not** contain raw or processed data, database
dumps, or generated datasets — those are excluded per program policy (see
`.gitignore`) and are only ever run locally against a MySQL instance seeded
from the program-provided MLS data.

## Setup

1. Install Docker Desktop (allocate at least 4GB RAM) and Python 3.11+.
2. Create and activate a virtual environment, then install dependencies:
   ```
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Start the local database:
   ```
   docker-compose up -d
   ```
   This launches a MySQL 8.0 container and imports the MLS SQL dumps placed
   in `data/raw/` (not committed to version control).
4. Verify the environment:
   ```
   python tests/test_setup.py
   ```
   This confirms the Python version, required packages, and database
   connectivity are all correctly configured.

## Repository Structure

```
data/{raw,processed,models}   # local-only data — gitignored, never committed
scripts/                      # pipeline code (data loading, cleaning, extraction, parsing, etc.)
tests/                        # pytest test suite
notebooks/                    # exploratory analysis notebooks
docker-compose.yml            # local MySQL environment
requirements.txt              # pinned Python dependencies
```

## Roadmap

| Week | Focus |
|------|-------|
| 0 | Environment setup (Docker, Python, Git) |
| 1 | Domain understanding & taxonomy construction |
| 2 | Text cleaning & normalization |
| 3 | Named entity extraction |
| 4 | Natural-language query parser → SQL |
| 5 | Semantic search with sentence embeddings |
| 6 | Structured listing signal extraction |
| 7 | Search query intent classification |
| 8 | Listing summarization |
| 9 | Fair Housing Act compliance checking |
| 10 | REST API (FastAPI) |
| 11 | Product integration demo |
| 12 | Final presentation & technical defense |

## Author

Prakhar Shah — NLP Engineer Intern, IDX Exchange (Fall 2026 cohort)
