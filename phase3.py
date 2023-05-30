from phase2 import get_books_by_category_url, get_categories
from phase2 import upload_books

def phase3(upload_images=False):
    categories = get_categories()
    for category, href in categories[1:]:
        books_data = get_books_by_category_url(href, upload_images=upload_images)
        upload_books(f"{ category }.csv", books_data)


if __name__ == '__main__':
    phase3()