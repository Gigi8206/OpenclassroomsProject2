import requests
from bs4 import BeautifulSoup
import csv
def scrap_book():
 url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
 reponse = requests.get(url)
 page = reponse.content
 soup = BeautifulSoup(page,"html.parser")
 product_page_url = url
 list_td = soup.findAll('td')
 upc =list_td[0].text
 title = soup.h1.text
 price_including_tax = list_td[3].text
 price_exluding_tax = list_td[2].text
 number_available = list_td[5].text
 list_p= soup.findAll('p')
 product_description = list_p[3].text
 list_a = soup.findAll('a')
 category = list_a[3].text
 review_rating = soup.find("p",{"class": "star-rating"}).get("class")[1]
 image_url = soup.find("img").get("src").strip('../../')
 en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_exluding_tax", "number_available",
            "product_description", "category", "review_rating", "image_url"]
 # Créer un nouveau fichier pour écrire dans le fichier appelé « phase1.csv »
 with open('phase1.csv', 'w') as fichier_csv:
  writer = csv.writer(fichier_csv, delimiter=',')
  writer.writerow(en_tete)
  ligne = [product_page_url, upc, title, price_including_tax, price_exluding_tax, number_available, product_description,
          category, review_rating, image_url]
  writer.writerow(ligne)
 return product_page_url, upc, title, price_including_tax,price_exluding_tax,number_available,product_description,category,review_rating,image_url
print(scrap_book())



