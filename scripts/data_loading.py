"""
Week 1 - Data Loading
Pulls a random sample of listing remarks from rets_property for taxonomy
building and downstream NLP work.
"""
import mysql.connector
import pandas as pd

DB_CONFIG = dict(host='localhost', user='root', password='root', database='real_estate')


def load_sample(n=1000):
    conn = mysql.connector.connect(**DB_CONFIG)
    query = f"""
        SELECT L_ListingID, L_Address, L_Keyword2 as beds,
               LM_Dec_3 as baths, L_SystemPrice as price, L_Remarks as remarks
        FROM rets_property
        WHERE L_Remarks IS NOT NULL AND LENGTH(L_Remarks) > 50
        ORDER BY RAND() LIMIT {n}
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


if __name__ == "__main__":
    df = load_sample(1000)
    df.to_csv("data/processed/listing_sample.csv", index=False)
    print(f"Saved {len(df)} listings to data/processed/listing_sample.csv")
    print(df[["L_ListingID", "beds", "baths", "price"]].head())
