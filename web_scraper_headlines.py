
import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(
        url, headers=headers, timeout=15
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("=== News Headlines Scraper ===\n")

    headlines = soup.select("h2")

    count = 0

    for headline in headlines:
        title = headline.get_text(" ", strip=True)

        if title:
            print(f"{count + 1}. {title}")
            count += 1

        if count == 10:
            break

    if count == 0:
        print("No headlines found.")

except requests.RequestException as error:
    print("Could not fetch headlines:", error)
