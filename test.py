import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


prices = soup.find_all("p", class_="price_color")

tab_prices = []
for price in prices:
	tab_prices.append(price.string)


print(tab_prices)



