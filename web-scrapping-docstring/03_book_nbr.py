# Objectif : Retourner le nom de toute les catégories avec moins de 5 livres.
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/index.html"

#param : threshold: int = 5 donne la valeur 5 par defaut.
#                         2 donne la valeur 2 par defaut.
def main(threshold: int = 5):
    #IMPORTANT: création de session pour eviter de faire une requette à chaque itération.
    #Tous mettre dans la session
    with requests.Session() as session:

        response = session.get(BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        categories = soup.select("ul.nav.nav-list a")
        # categories[1:] permet de commencer a partir de l'index 1, et non zéro.
        categories_url = [category["href"] for category in categories[1:]]


        #naviguer dans chaque URL
        for categorie_url in categories_url:
            #urljoin permet de concaténer les url.
            absolute_url = urljoin(BASE_URL, categorie_url)
            response = session.get(absolute_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            books = soup.select("article.product_pod")
            nbr_books = len(books)
            category_title = soup.select_one("h1").text
            if nbr_books <= threshold:
                print(f"La catégorie '{category_title}' ne comporte pas assez de livre ({nbr_books}).")

if __name__ == '__main__':
    main(threshold=2)
