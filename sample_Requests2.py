#外部ライブラリを必ずインストールする
# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

URL = 'https://www.sozosha.ac.jp/'

r = requests.get(URL)
#print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
soup_title = soup.find("title")

print(soup_title)

