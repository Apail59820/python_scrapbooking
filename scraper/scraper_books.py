import requests
from bs4 import BeautifulSoup
from book import *

class BookScraper:
    def __init__(self):
        self.soup = None
        self.books = []

    def soup_from_url(self, url):
        req = requests.get(url)
        if req.status_code == 200:
            self.soup = BeautifulSoup(requests.get(url).content, "lxml")
            return True
        else:
            print("Url : '{}', returned {}.".format(url, req.status_code))
            return False

    def scrape_page(self, url):
        if not self.soup_from_url(url):
            print("Skipping the scrapping for this page...")
            return []

        articles = self.soup.find_all("article")
        books = []
        for article in articles:
            book_title = ""
            for h3 in article.find_all("h3"):
                book_title = h3.find("a").text.strip()

            star_rating = article.find("p", class_="star-rating").get("class")
            book_rating = star_rating[1]

            product_price = article.find("p", class_="price_color").text.strip()
            book_price = float(product_price.replace("£", ""))

            product_availability = article.find("p", class_="availability").text.strip()

            books.append(Book(book_title, book_price, product_availability, book_rating))

        return books

    def scrape_all(self, pages = 50):
        base_url = "https://books.toscrape.com/catalogue/"
        total_books = []
        for i in range(0, pages):
            print("Scraping page {}".format(i + 1))
            books = self.scrape_page(base_url + "page-{}.html".format(str(i + 1)))
            if len(books) != 0:
                total_books.extend(books)
        print("Total books: {}".format(len(total_books)))
        return total_books