import pandas as pd

def load_books(filepath):
    books_df = pd.read_csv(filepath)

    books_df["price"] = (
        books_df["price"]
        .astype(str)  # Si c'est un str
        .astype(float)  # Conversion en float
    )

    return books_df

def describe_prices(df):
    price_series = df['price']

    description = {
        'Prix moyen': price_series.mean(),
        'Prix min': price_series.min(),
        'Prix max': price_series.max(),
        'Mediane': price_series.median(),
        'Écart-type': price_series.std(),
        '1er quartile': price_series.quantile(0.25),
        '3eme quartile': price_series.quantile(0.75)
    }

    for key, value in description.items():
        print(f"{key}: {value:.2f}")

def availability_counts(df):
    df2 = df.groupby(['availability', 'rating']).agg({
        'rating': 'count',
        'price': 'mean'
    })

    df2.rename(columns={'rating': 'count'}, inplace=True)
    df2.rename(columns={'price': 'average price'}, inplace=True)

    return df2