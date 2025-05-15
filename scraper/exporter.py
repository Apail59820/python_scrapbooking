import csv
from book import Book

def export_books_to_csv(books: Book, filepath):
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        header = books[0].to_dict().keys()
        writer.writerow(header)

        for book in books:
            book_dict = book.to_dict()
            book_values = book_dict.values()
            writer.writerow(book_values)