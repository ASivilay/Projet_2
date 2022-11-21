import requests
from bs4 import BeautifulSoup
import csv


#url = "http://books.toscrape.com/"
url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

categories = soup.find('div', class_="side_categories").find_all('a')


tab_links = []
tab_categories = []

for categorie in categories:
	tab_links.append(categorie.get('href'))
	tab_categories.append(categorie.string)

columns_titles = ['Lien catégorie', 'Catégorie']
with open('menudata.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, delimiter= ',')
	writer.writerow(columns_titles)
	for link, categorie in zip(tab_links, tab_categories):
		writer.writerow([link, categorie])


