# OpenclassroomsProject2 "Utilisez les bases de Python pour l'analyse de marché"

phase1.py : Est un programme de scraping du site exemple : http://books.toscrape.com/index.html, 
il extrait les données suivante  : 
•	product_page_url
•	universal_ product_code (upc)
•	title
•	price_including_tax
•	price_excluding_tax
•	number_available
•	product_description
•	category
•	review_rating
•	image_url
A partir d'un livre spécifique : 
"http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html", et l'enregistre en format csv:"phase1.csv)
 Exécution : python phase1.py 

phase2.py : Est un programme de scraping , qui appelle le fichier phase1.py , pour extraire les même données , d’une catégorie spécifique de livre , tout en parcourant automatiquement les multiples pages si présentes  et l’enregistre sous format csv « phase2.csv ».
Exécution : python phase2.py

phase3.py : Est un programme de scraping , qui appelle le fichier phase2.py , afin d’extraire les mêmes données de la phase1, pour chaque catégorie présente au niveau du site web et l’enregistre sous format csv , au nom de la catégorie.
Exécution : python phase3.py

phase4.py : Est un programme de scraping , qui appelle les trois phases , afin d’en extraire les images de chaque livre, et les enregistre dans un dossier «Download images » 
Exécution : python phase4.py



Installation :
Python3 dois être installé sur votre système depuis https://www.python.org/
Il est fortement recommandé d'utiliser un environnement virtuel et de l’activer : 
python -m venv env
source env/bin/activate

![image](https://github.com/Gigi8206/OpenclassroomsProject2/assets/113972351/30cec99e-5c3b-449d-9854-f1f96627abde)
