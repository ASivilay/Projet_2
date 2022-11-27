import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
from PIL import Image
import pathlib


urlMain = "http://books.toscrape.com/"
#url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
urlCategory = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html'
url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
page = requests.get(urlCategory)
soup = BeautifulSoup(page.content, 'html.parser')

productCategory = 'Mystery'

#Ecriture dans le fichier csv
columnsTitles = ['Titre du livre', 'Lien du livre', 'Catégorie', 'Prix HT', 'Prix TTC', 'Disponibilité', 'Code', 'Note']
with open('data.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, delimiter = ',')
	writer.writerow(columnsTitles)

	#Recuperation des livres
	lis = soup.find('ol', class_='row').find_all('li')
	for li in lis:
		tmpProductUrl = li.find('a').get('href').replace('../', "")
		productUrl = urljoin('http://books.toscrape.com/catalogue/', tmpProductUrl)
		productPage = requests.get(productUrl)
		productSoup = BeautifulSoup(productPage.content, 'html.parser')

		#Recuperation des donnees du livre
		productTitle = productSoup.find('div', class_='col-sm-6 product_main').find('h1').string
		tmpProductReview = productSoup.find('div', class_='col-sm-6 product_main').find_all('p')[2]
		productReview = tmpProductReview['class'][1]
		productDescription = productSoup.find('div', id='product_description').findNext('p').string

		tds = productSoup.find('table', class_='table table-striped').find_all('td')
		productUniversalCode = tds[0].string
		productExcTax = tds[2].string
		productIncTax = tds[3].string
		productAvailability = tds[5].string

		#Telechargement de l'image
		imgSrc = productSoup.find('img').get('src')
		imgUrl = urljoin(urlMain, imgSrc)
		img = Image.open(requests.get(imgUrl, stream = True).raw)
		imgPath = '\\images\\' + productTitle + '.jpg'
		img.save(str(pathlib.Path().absolute()) + imgPath)

		writer.writerow([productTitle, url, productCategory, productExcTax, productIncTax, productAvailability, productUniversalCode, productReview])









"""
print(productUniversalCode)
print(productExcTax)
print(productIncTax)
print(productAvailability)
print(productDescription)
print(productReview)
print(imgUrl)
"""

