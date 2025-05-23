"""  Objectif :
Le libraire souhaite retirer de la page d'accueil, les livres avec une note de une étoile.
Ce script doit etre utiliser tous les jours pour retirer les moins bien noté de facon automatisé meme si il en rajoute.
Annonce au libraire qu'il y a une erreur si l'id du book (présent dans l'url) est manquant
besoin : recuperer le nom et l'id du ligne
"""
#import de python
import re

#import de librairie supplémentaire (avec pip3 install)
import requests
from bs4 import BeautifulSoup
from pprint import pprint

BASE_URL = "https://books.toscrape.com/index.html"
# Annotation de type pour préciser le retour d'une liste de nombre entier par la fonction main "-> list[int]"
def main() -> list[int]:

    book_ids = []

    #Lève les erreurs
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        #appel API ou envoi de mail pour prévenir le libraire. La on fait juste un print
        print(f"il y a eu un probleme lors de l'acès au site : {e}.")
        raise requests.exceptions.RequestException from e

    soup = BeautifulSoup(response.text, "html.parser")
    one_star_books = soup.select("p.star-rating.One")
    for book in one_star_books:
        try:
            book_link = book.find_next("h3").select_one("a")["href"]
        except AttributeError as e:
            print("impossible de trouver la balise 'h3'.")
            raise AttributeError from e
        except TypeError as e:
            print("imossible de trouver la balise 'a'.")
            raise TypeError from e
        except KeyError as e:
            print("impossible de trouver l'attribut 'href'.")

        #regex:
        # "\d" : cible un nombre
        # "_" : underscore
        # "{1,4}" : nbr de récurence de 1 à 4
        # résultat = r"_\d{1,4}"
        try:
            book_id = re.findall(r"_\d{1,4}", book_link)[0][1:]
        except IndexError as e:
            print("impossible de trouver l'ID du livre.")
            raise IndexError from e
        else:
            book_ids.append(int(book_id))
    return book_ids

if __name__ == "__main__" :
    print(main())
