
import requests
from requests import get
from bs4 import BeautifulSoup

def get_categories():
    response = get("http://books.toscrape.com/index.html")
    soup = BeautifulSoup(response.text, "html.parser")
    aside = soup.find('aside')
    links = aside.find_all('a')
    links_title = [link.text.strip() for link in links]
    links_href = [link["href"] for link in links]
    return links_title, links_href
print(get_categories())
# Choix d'une categorie:
url_categorie ="https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html"
def scrap_categorie(url):
    book_urls =[]
    r= requests.get(url_categorie)
    if r.ok:
        soup = BeautifulSoup(r.content,"html.parser")
    else:print()
    articles = soup.find_all("article", class_ = "product_pod")
    for article in articles:
    # récuperer url d'un livre
        book_url = article.find("a")["href"][8:]
        book_url=f"https://books.toscrape.com/catalogue{book_url}"
        print(book_url)
    #Ajouter url du livre a la liste book_urls
        book_urls.append(book_url)
    # Afficher la premiere page
        page = soup.select_one("li.current").text.strip('../../')
        print(page)
    #integrer le bouton page suivante
        next_page = soup.select_one("li.next>a")["href"]
        # si il ya une page suivante scrap les données sinon stop
    return book_urls
# Créer un nouveau fichier pour écrire dans le fichier appelé « phase2.csv »
    with open(f"{url_categorie}.csv","a") as file: file.write(information)
    en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_exluding_tax", "number_available",
               "product_description", "category", "review_rating", "image_url"]
    # Créer un nouveau fichier pour écrire dans le fichier appelé « phase1.csv »
    with open('phase2.csv', 'w') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(en_tete)
        ligne = [product_page_url, upc, title, price_including_tax, price_exluding_tax, number_available,
                 product_description,
                 category, review_rating, image_url]
        writer.writerow(ligne)
    return product_page_url, upc, title, price_including_tax, price_exluding_tax, number_available, product_description, category

print(scrap_categorie(url_categorie))





