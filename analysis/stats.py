import pandas as pd

def load_books(filepath):
    books_df = pd.read_csv(filepath)

    books_df["price"] = (
        books_df["price"]
        .astype(str)  # Si c'est un str
        .astype(float)  # Conversion en float
    )

    return books_df