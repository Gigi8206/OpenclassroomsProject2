from os.path import join
from os import mkdir
import requests
from bs4 import BeautifulSoup
from csv import writer



def upload_books(filename, books_data):
    en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_exluding_tax", "number_available",
        "product_description", "category", "review_rating", "image_url"]
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        book_writer = writer(csvfile)
        book_writer.writerow(en_tete)
        book_writer.writerows(books_data)

def get_book_data(url, upload_images=False):
    main_page = "http://books.toscrape.com/"
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page,"html.parser")
    soup = soup
    product_page_url = url
    list_td = soup.findAll('td')
    upc = list_td[0].text
    title = soup.h1.text
    price_including_tax = list_td[3].text
    price_exluding_tax = list_td[2].text
    number_available = list_td[5].text
    list_p = soup.findAll('p')
    product_description = list_p[3].text
    list_a = soup.findAll('a')
    category = list_a[3].text
    review_rating = soup.find("p",{"class": "star-rating"}).get("class")[1]
    image_url = main_page+soup.find("img").get("src").strip('../../')

    if upload_images:
        # . is the current dir
        folder = "Download images"
        path = join(".", folder)
        try:
            mkdir(path)
        except FileExistsError:
            pass
    
        image_path = join(".", folder, image_url[image_url.rfind("/") + 1:])
        with open(image_path, 'wb') as file:
            image = requests.get(image_url).content
            file.write(image)

    return product_page_url, upc, title, price_including_tax,price_exluding_tax,number_available,product_description,category,review_rating,image_url

def phase1(upload_images=False):
    url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    book_data = get_book_data(url, upload_images=upload_images)
    print(book_data)
    upload_books("phase1.csv", [book_data])

if __name__ == '__main__':
    phase1()
