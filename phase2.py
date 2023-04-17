import requests
from requests import get
from bs4 import BeautifulSoup
url = "http://books.toscrape.com/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
aside = soup.find('aside')
links = aside.find_all('a')
links_title = [link.text.strip() for link in links]
links_href = [link["href"] for link in links]
classics_category = links_title[5]
print(links_title)
print(classics_category)
url_categorie ="http://books.toscrape.com/catalogue/category/books/classics_6/index.html"
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
    # récuperer le titre d'un livre
        titre_livre = article.find("h3").text
        print(titre_livre)
    #Ajouter url du livre a la liste book_urls
        book_urls.append(book_url)
    #Ajouter le titre du livre :
        book_urls.append(titre_livre)
    return book_urls
# Créer un nouveau fichier pour écrire dans le fichier appelé « phase2.csv »
    en_tete = ["book_urls"]
    # Créer un nouveau fichier pour écrire dans le fichier appelé « phase1.csv »
    with open('phase2.csv', 'w') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(en_tete)
        ligne = [links_title]
        writer.writerow(ligne)
    return books_urls, links_title

print(scrap_categorie(url_categorie))