"""
Week 1 - Taxonomy Builder
Extracts the most frequent bigrams from listing remarks to seed a 200+ term
real estate taxonomy.
"""
import json
import nltk
from collections import Counter
from nltk.util import ngrams
import pandas as pd

for pkg in ("punkt", "punkt_tab"):
    nltk.download(pkg, quiet=True)


def build_taxonomy(csv_path="data/processed/listing_sample.csv", top_n=200):
    df = pd.read_csv(csv_path)
    all_text = " ".join(df["remarks"].dropna().str.lower())
    tokens = nltk.word_tokenize(all_text)
    bigrams = list(ngrams(tokens, 2))
    freq = Counter(bigrams)

    terms = [
        {"id": i, "term": " ".join(bigram), "count": count}
        for i, (bigram, count) in enumerate(freq.most_common(top_n))
    ]
    return {"terms": terms}


if __name__ == "__main__":
    taxonomy = build_taxonomy()
    with open("data/processed/taxonomy.json", "w") as f:
        json.dump(taxonomy, f, indent=2)
    print(f"Saved {len(taxonomy['terms'])} taxonomy terms to data/processed/taxonomy.json")
    for t in taxonomy["terms"][:15]:
        print(f"  {t['term']}: {t['count']}")
