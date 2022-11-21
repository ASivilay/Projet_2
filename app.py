import requests
from bs4 import BeautifulSoup
import csv


#url = "http://books.toscrape.com/"
url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


def has_href_and_title(tag):
    return tag.has_attr('href') and tag.has_attr('title')


names = soup.find_all(has_href_and_title)
tab_names =[]
for name in names:
	tab_names.append(name.get('title'))


prices = soup.find_all("p", class_="price_color")
tab_prices = []
for price in prices:
	tab_prices.append(price.string)




columns_titles = ['Titre du livre', 'Prix']
with open('data.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, delimiter= ',')
	writer.writerow(columns_titles)
	for name, price in zip(tab_names, tab_prices):
		writer.writerow([name, price])


