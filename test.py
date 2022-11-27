import requests
from bs4 import BeautifulSoup
import csv


url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#lis = soup.find('div', class_="side_categories").find_all('li.ul.li')
uls = soup.find('div', class_="side_categories").find_all('ul')

lis = uls[1].find_all('li')

"""
for li in lis:
	categoryUrl = li.find('a').get('href')
	print(categoryUrl)

	categoryName = li.text.replace('[ "/s]', "").strip()
	print(categoryName)

"""

links = []
categories = []

for li in lis:
	link = li.find('a').get('href')
	links.append(url + link)

	categorie = li.find('a').text.replace('[ "/s]', "").strip()
	categories.append(categorie)


print(links)
print(categories)