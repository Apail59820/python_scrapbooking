import csv
from scraper.book import Book
from typing import List

from scraper.product import Product


def export_books_to_csv(books: List[Book], filepath):
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        header = books[0].to_dict().keys()
        writer.writerow(header)

        for book in books:
            book_dict = book.to_dict()
            book_values = book_dict.values()
            writer.writerow(book_values)

def export_products_to_csv(products: List[Product], filepath):
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        header = products[0].to_dict().keys()
        writer.writerow(header)

        for product in products:
            product_dict = product.to_dict()
            product_values = product_dict.values()
            writer.writerow(product_values)