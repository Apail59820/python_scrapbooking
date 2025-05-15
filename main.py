from scraper.scraper_books import BookScraper
from scraper.exporter import export_books_to_csv, export_products_to_csv
from scraper.scraper_custom import scrap_all_products

if __name__ == "__main__":
    bookScraper = BookScraper()

    # Ces lignes sont commentées car j'ai la flemme de re scrap et re-exporter à chaque fois
    # L'affichage du nombre de livres totaux récupérés se trouve dans scraper_books.scrape_all()

    # total_books = bookScraper.scrape_all(50)
    # export_books_to_csv(total_books, "data/books.csv")

    # products = scrap_all_products()
    # export_products_to_csv(products, 'data/products.csv')
    # print("{} produits récupérés.".format(len(products)))

    