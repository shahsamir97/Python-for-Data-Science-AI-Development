import pandas as pd
import requests
from io import StringIO
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_largest_banks"

headers = {
    "User-Agent": "BankDataLearning/1.0 (your-email@example.com)"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

tables = pd.read_html(StringIO(response.text))

df = tables[0]

print(df)