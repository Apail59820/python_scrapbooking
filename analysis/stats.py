import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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

def plot_price_histogram(df):
    plt.hist(df['price'].values.tolist())
    plt.title('Histogramme des prix')
    plt.xlabel("Prix")
    plt.ylabel("Fréquence")
    plt.savefig("data/histogram_price.png")

def plot_price_boxplot(df):
    plt.boxplot(df['price'].values.tolist())
    plt.title('Boxplot des prix')
    plt.ylabel("Prix")
    plt.savefig("data/boxplot_price.png")

def plot_price_clusters(df):
    kmeans = KMeans(n_clusters=3, random_state=0)
    df['cluster'] = kmeans.fit_predict(df[['price']])

    plt.scatter(df.index, df['price'], c=df['cluster'])
    plt.xlabel("Index")
    plt.ylabel("Prix")
    plt.title("Prix des livres (3 clusters)")
    plt.savefig("data/clustering_price.png")

def plot_cluster_distribution(df):
    kmeans = KMeans(n_clusters=3, random_state=0)
    df['cluster'] = kmeans.fit_predict(df[['price']])

    grouped = [df[df['cluster'] == i]['price'] for i in sorted(df['cluster'].unique())]

    clusters = ['Bas', 'Moyen', 'Haut']

    plt.boxplot(grouped, labels=[f'Prix {clusters[i]}' for i in sorted(df['cluster'].unique())])
    plt.ylabel("Prix")
    plt.title("Distribution des prix par cluster")
    plt.savefig("data/cluster_boxplot.png")

plot_cluster_distribution(load_books('data/books.csv'))
