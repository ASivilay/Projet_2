import requests
from bs4 import BeautifulSoup
import csv



urlmain = "http://books.toscrape.com/"
url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

lis = soup.find('div', class_="side_categories").find_all('li')


links = []
categories = []


for li in lis:
	a = li.find('a')
	link = a['href']
	links.append(urlmain + link)
	categorie = a.text.replace('[ "/s]', "").strip()
	print(categorie)

	categories.append(categorie)


columns_titles = ['Lien catégorie', 'Catégorie']
with open('menudata2.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, delimiter= ',')
	writer.writerow(columns_titles)
	for link, categorie in zip(links, categories):
		writer.writerow([link,categorie])










