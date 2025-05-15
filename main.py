from scraper.scraper_books import BookScraper
from scraper.exporter import export_books_to_csv

if __name__ == "__main__":
    bookScraper = BookScraper()

    # Ces lignes sont commentées car j'ai la flemme de re scrap et re-exporter à chaque fois
    # L'affichage du nombre de livres totaux récupérés se trouve dans scraper_books.scrape_all()

    # total_books = bookScraper.scrape_all(50)
    # export_books_to_csv(total_books, "data/books.csv")