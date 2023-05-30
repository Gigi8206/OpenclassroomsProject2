from phase1 import get_book_data, upload_books
from requests import get
from bs4 import BeautifulSoup
from get_number_pages import get_number_of_pages
import constants
from Parse_html import parse_html

root_url = "http://books.toscrape.com/"

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

def get_pages_urls(category_url:str) -> list:
    number_of_pages= get_number_of_pages(category_url)
    if number_of_pages == 1:
        return (category_url,)
    pages_urls = []
    for i in range(number_of_pages):
        pages_urls.append(category_url.replace("index.", f"page-{i+1}."))
    return pages_urls

def get_books_urls(pages_urls: list) ->list:
    books_url = []
    for page_url in pages_urls:
        content = parse_html(page_url)
        titles = content.find_all("h3")
        for title in titles:
            href = title.find('a')["href"]
            if (relative_pattern :="../../../") in href:
                link = href.replace(relative_pattern, f"{constants.url}catalogue/")
            elif (relative_pattern :="../../") in href:
                link = href.replace(relative_pattern, f"{constants.url}catalogue/")
            else:
                raise ValueError("Unknown pattern")
            books_url.append(link)
    return books_url

def get_books_by_category_url(category_url, upload_images=False):
    pages = get_pages_urls(category_url)
    books_url = get_books_urls(pages)

    books_data = []
    for link in books_url:
        book_data = get_book_data(link, upload_images=upload_images)
        books_data.append(book_data)

    return books_data

def get_books_by_category(upload_images=False):
    # We get user input to choose category
    categories = get_categories()
    print(f"{ len(categories) - 1} categories trouvées")
    titles = [category[0] for category in categories[1:]]
    user_response = get_user_category(titles)
    while user_response not in titles:
        print("Mauvaise catégorie")
        user_response = get_user_category(titles)

    # We get all link for the category
    for title, href in categories:
        if user_response == title:
            return get_books_by_category_url(href, upload_images=upload_images)

def phase2(upload_images=False):
    books_data = get_books_by_category(upload_images=upload_images)
    upload_books("phase2.csv", books_data)


if __name__ == '__main__':
    phase2()