import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import posixpath



urlMain = "http://books.toscrape.com/"
url = "http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

lis = soup.find('ol', class_='row').find_all('li')
li = lis[0].find('a').get('href').replace('../', "")
#liTest = li.replace('../', "")


liPath = urljoin('http://books.toscrape.com/catalogue/', li)
#test = urljoin(liPath, li)

#test = posixpath.join(urlMain, 'catalogue/', li)


#print(len(lis))
#print(liTest)
print(liPath)