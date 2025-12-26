import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

base_url = "https://books.toscrape.com/"
url = base_url

rating_dict = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

books_data = []

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        stock = book.find("p", class_="instock availability").text.strip()

        rating_class = book.find("p", class_="star-rating")["class"]
        rating_text = rating_class[1]
        rating = rating_dict.get(rating_text, 0)

        img_url = urljoin(url, book.find("img")["src"])
        book_url = urljoin(url, book.a["href"])

        books_data.append([
            title,
            price,
            stock,
            rating,
            img_url,
            book_url
        ])

    next_button = soup.find("li", class_="next")
    if next_button:
        url = urljoin(url, next_button.a["href"])
    else:
        url = None


with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Title",
        "Price",
        "Stock",
        "Rating",
        "Image URL",
        "Book URL"
    ])
    writer.writerows(books_data)
