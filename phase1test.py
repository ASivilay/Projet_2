import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
from PIL import Image


urlMain = "http://books.toscrape.com/"
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#images = []

#for img in soup.find_all('img'):
#	images.append(img.get('src'))


#productImage = soup.find('img').get('src')
imgPath = soup.find('img').get('src')

result = urljoin(urlMain, imgPath)

result.save('test','jpg')

#print(productImage)
print(result)