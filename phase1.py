import requests
from bs4 import BeautifulSoup
import csv


#url = "http://books.toscrape.com/"
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
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



print(productUniversalCode)
print(productExcTax)
print(productIncTax)
print(productAvailability)
print(productDescription)