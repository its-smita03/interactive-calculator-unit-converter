
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select(".quote")

    print("=== Web Scraper: Quotes ===")

    for i, item in enumerate(quotes, start=1):
        quote = item.select_one(".text").get_text(strip=True)
        author = item.select_one(".author").get_text(strip=True)

        print(f"\n{i}. {quote}")
        print("Author:", author)

except requests.RequestException as error:
    print("Website request failed:", error)
