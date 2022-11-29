import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
from PIL import Image
import pathlib
import re


urlMain = "http://books.toscrape.com/"
pageMain = requests.get(urlMain)
soupMain = BeautifulSoup(pageMain.content, 'html.parser')


#Recuperation liens + noms categories
ulsSideMenu = soupMain.find('div', class_ = "side_categories").find_all('ul')
lisSideMenu = ulsSideMenu[1].find_all('li')

#Ouverture fichier csv
columnsTitles = ['Titre du livre', 'Lien du livre', 'Catégorie', 'Prix HT', 'Prix TTC', 'Disponibilité', 'Code', 'Note']
with open('data.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, delimiter = ',')
	writer.writerow(columnsTitles)

	#Bouclage sur les categories
	for li in lisSideMenu:
		tmpCategoryLink = li.find('a').get('href')
		categoryLink = urlMain + tmpCategoryLink
		categoryName = li.find('a').text.replace('[ "/s"]',"").strip()


		#Bouclage selon pagination
		while True:
			categoryPage = requests.get(categoryLink)
			pageSoup = BeautifulSoup(categoryPage.content, 'html.parser')

			#Recuperation des livres
			lisBooks = pageSoup.find('ol', class_='row').find_all('li')
			for li in lisBooks:
				tmpProductUrl = li.find('a').get('href').replace('../', "")
				productUrl = urljoin('http://books.toscrape.com/catalogue/', tmpProductUrl)
				productPage = requests.get(productUrl)
				productSoup = BeautifulSoup(productPage.content, 'html.parser')

				#Recuperation des donnees du livre
				productTitle = productSoup.find('div', class_='col-sm-6 product_main').find('h1').string
				tmpProductReview = productSoup.find('div', class_='col-sm-6 product_main').find_all('p')[2]
				productReview = tmpProductReview['class'][1]


				if productSoup.find('div', id='product_description') is None:		#Vérification description du livre n'est pas vide
					productDescription = ""
				else:
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
				tmpProductTitle = re.sub(r'[\\/:"*?<>|]+', "_", productTitle)
				imgPath = '\\images\\' + tmpProductTitle + '.jpg'
				img.save(str(pathlib.Path().absolute()) + imgPath)

				#Ecriture dans le fichier csv
				writer.writerow([productTitle, productUrl, categoryName, productExcTax, productIncTax, productAvailability, productUniversalCode, productReview])

			#Verification bouton Next + chgt url de la page
			nextButton = pageSoup.find('li', class_='next')
			if nextButton:
				categoryLink = urljoin(categoryLink, nextButton.find('a').get('href'))
			else:
				break