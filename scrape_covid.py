import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/country/malaysia/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    counters = soup.find_all("div", class_="maincounter-number")

    if len(counters) >= 3:
        cases = counters[0].text.strip()
        deaths = counters[1].text.strip()
        recovered = counters[2].text.strip()

        print("==========================================")
        print(" COVID-19 Data Scraped for Malaysia")
        print(" Source: Worldometers")
        print("==========================================")
        print(f" Total Cases     : {cases}")
        print(f" Total Deaths    : {deaths}")
        print(f" Total Recovered : {recovered}")
        print("==========================================")
except Exception as e:
    print(f"Error scraping data: {e}")

