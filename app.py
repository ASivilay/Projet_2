import requests
from bs4 import BeautifulSoup
import csv


url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


def has_href_and_title(tag):
    return tag.has_attr('href') and tag.has_attr('title')

names = soup.find_all(has_href_and_title)
#names = namesh3.find_all("a", attrs={'title'})
#names = soup.find_all("a", attrs={"title"})

tab_names =[]
for name in names:
	tab_names.append(name.get('title'))


prices = soup.find_all("p", class_="price_color")
#prices = soup.find_all("p", class_="price_color")
#prices = soup.find_all("div", class_="product_price")
#prices = pricesdiv.find_all("p", class_="price_color")
#prices = soup.find_all("div", attrs={"class": "product_price"})

tab_prices = []
for price in prices:
	tab_prices.append(price.string)




en_tete = ['Titre du livre', 'Prix']
with open('data.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, delimiter= ',')
	writer.writerow(en_tete)
	for name, price in zip(tab_names, tab_prices):
		writer.writerow([name, price])


