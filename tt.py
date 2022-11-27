import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
from PIL import Image
import pathlib


urlMain = "http://books.toscrape.com/"
#url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
urlCategory = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html'
#url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
page = requests.get(urlCategory)
soup = BeautifulSoup(page.content, 'html.parser')

productCategory = 'Mystery'



#Bouclage selon pagination
while True:
	page = requests.get(urlCategory)
	pageSoup = BeautifulSoup(page.content, 'html.parser')

	print(urlCategory)

	#Verification bouton Next + chgt url de la page
	nextButton = pageSoup.find('li', class_='next')
	print(nextButton)
	if nextButton:
		urlCategory = urljoin(urlCategory, nextButton.find('a').get('href'))
		print(urlCategory)
	else:
		break

	










"""
print(productUniversalCode)
print(productExcTax)
print(productIncTax)
print(productAvailability)
print(productDescription)
print(productReview)
print(imgUrl)
"""

