import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
from PIL import Image
import pathlib


urlMain = "http://books.toscrape.com/"
#url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

productTitle = soup.find('div', class_='col-sm-6 product_main').find('h1').string
tmpProductReview = soup.find('div', class_='col-sm-6 product_main').find_all('p')[2]
productReview = tmpProductReview['class'][1]

productDescription = soup.find('div', id='product_description').findNext('p').string

tds = soup.find('table', class_='table table-striped').find_all('td')
productUniversalCode = tds[0].string
productExcTax = tds[2].string
productIncTax = tds[3].string
productAvailability = tds[5].string



#Telechargement de l'image
imgSrc = soup.find('img').get('src')
imgUrl = urljoin(urlMain, imgSrc)
img = Image.open(requests.get(imgUrl, stream = True).raw)
productImageName = '\\images\\' + productTitle + '.jpg'
img.save(str(pathlib.Path().absolute()) + productImageName)













"""
print(productUniversalCode)
print(productExcTax)
print(productIncTax)
print(productAvailability)
print(productDescription)
"""
print(productReview)
print(imgUrl)
