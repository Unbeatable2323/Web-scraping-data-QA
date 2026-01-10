import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

for page in range(1, 6):  # scrape first 5 pages
    url = BASE_URL.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text if book.select_one(".price_color") else None
        availability = book.select_one(".availability").text.strip() if book.select_one(".availability") else None
        rating = book.p["class"][1] if book.p else None
        product_url = book.h3.a["href"]

        data.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "url": product_url
        })

df = pd.DataFrame(data)
df.to_csv("books_data.csv", index=False)

print("Scraping completed. Data saved to books_data.csv")
