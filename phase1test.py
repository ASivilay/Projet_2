import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
from PIL import Image
import pathlib
import os


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



img = Image.open(requests.get(result, stream = True).raw)


productTitle = soup.find('div', class_='col-sm-6 product_main').find('h1').string
productImageName = '\\images\\' + productTitle + '.jpg'
#img.save(productImageName)
#img.save('/images/' + productImageName)

currentDir = str(pathlib.Path().absolute())
#test = os.path.join(currentDir, productImageName)
test = currentDir + productImageName

img.save(test)

print(currentDir)
print(test)









#test = pathlib.Path().absolute()

#img.save('/images/'{productImageName})

#print(test, productImageName)

#print(productImage)
#print(result)

#print(pathlib.Path().absolute())




#test = currentDir + '/' + productImageName

#print(test)
