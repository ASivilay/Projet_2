import requests
from bs4 import BeautifulSoup
import csv



#url = "http://books.toscrape.com/"
url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

categories = soup.find('div', class_="side_categories").find_all('li')

print(categories)