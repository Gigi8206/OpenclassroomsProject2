from phase1 import scrap_book
from requests import get
from bs4 import BeautifulSoup
from csv import writer

root_url = "http://books.toscrape.com/"

def upload_books(book_titles, books_data):
    with open("phase2.csv", "w", newline="") as csvfile:
        book_writer = writer(csvfile)
        book_writer.writerow( book_titles)
        book_writer.writerows(books_data)
def get_categories():
    response = get("http://books.toscrape.com/index.html")
    soup = BeautifulSoup(response.text, "html.parser")
    nav = soup.find('ul', {"class": "nav nav-list"})
    links = nav.find_all('a')
    categories = [(link.text.strip(), root_url + link["href"]) for link in links]
    return categories

def get_user_category(titles):
    print(f"Choisissez entre { ', '.join(titles) }")
    user_response = input("Selectionnez votre categorie : ")
    return user_response
def get_books_by_category():
    categories = get_categories()
    print(f"{ len(categories) - 1} categories trouvées")
    titles = [category[0] for category in categories[1:]]
    user_response = get_user_category(titles)
    while user_response not in titles:
        print("Mauvaise catégorie")
        user_response = get_user_category(titles)

    books_data = []
    for title, href in categories:
        if user_response == title:
            response = get(href)
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all('article')
            page = (soup.find("li", {"class": "current"}))
            # verifier si,il n'ya pas une autre page :
            if page is None:
                all_h3 = soup.find_all('h3').text
            links = [article.find('a') for article in articles]
            for link in links:
                book_titles, book_data = scrap_book( "http://books.toscrape.com/catalogue/" + link["href"].strip('../../../'))
                books_data.append(book_data)
    return book_titles, books_data

if __name__ == '__main__':
        book_titles, books_data = get_books_by_category()
        breakpoint()
        upload_books(book_titles, books_data)
