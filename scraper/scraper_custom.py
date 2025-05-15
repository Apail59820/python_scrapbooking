# Chaise ergo sur CDiscount
import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

from scraper.product import Product

def extract_data_from_html(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')
    products = soup.find_all('article')

    product_title = None
    product_price = None
    product_source = None

    products_to_return = []

    try:
        for product in products:
            title = product.find('h4')
            product_title = title.text.strip()

            prices = product.select('span.c-price')

            for price_tag in prices:
                price = price_tag.get("content").strip()
                product_price = float(price.replace(",", "."))

            sources = product.select('a.o-card__link')
            for sources_tag in sources:
                product_source = sources_tag.get("href").strip()

            new_product = Product(product_title, product_price, product_source)
            products_to_return.append(new_product)
        return products_to_return

    except AttributeError:
        print('error')
        return products_to_return

def scrap_all_products():
    products = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.cdiscount.com/maison/r-chaise+ergonomique.html")

        while True:
            page.wait_for_timeout(1500)

            html = page.content()
            new_products = extract_data_from_html(html)
            products.extend(new_products)

            try:
                next_button = page.locator('text="Page suivante"')
                if next_button.is_visible() and next_button.is_enabled():
                    next_button.click()
                    print("Page suivante...")
                    time.sleep(2)
                else:
                    print("Fin de la pagination.")
                    break
            except Exception as e:
                print("Pas de bouton 'Suivant' :", e)
                break

        browser.close()
    return products
