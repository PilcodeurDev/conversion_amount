"""
Requests = Client HTTP : Envoyer des requêtes HTTP et récupère les données
BeautifulSoup4 = Parseur : Analyse le HTML / Naviguer dans le DOM
"""
"""
1) python3 -m venv mon_environnement
2) source mon_environnement/bin/activate <-- préfixe visible confirme que l'environnement est actif
    (désactiver l'env virtuel : deactivate)
3) pip3 install requests
4) python3 -c "import requests; print(requests.__version__)" <-- pour vérifier l'installation

"""
import requests
from bs4 import BeautifulSoup
from pprint import pprint

# url = "https://books.toscrape.com"
# response = requests.get(url)

# with open('index.html', "w") as file:
#     file.write(response.text)

# Une fois scaper, on peux travailler avec le index.html créé en local.
with open("index.html", "r") as file:
    html = file.read()

"""
autre exemple :
# Si la requête a réussi, le code de statut sera 200
print(response.status_code)
# Affiche le contenu json de la réponse
print(response.text)
# Affiche le contenu json de la réponse sous forme de dictionnaire
print(response.json())
# Affiche le contenu json de la réponse sous forme de liste
print(response.json()[0])
"""

""" Parser
n°1) 'lxml-xml' Analyse les fichiers xml
n°2) 'html.parser' Analyse spécifiquement du html, intégré dans python.
n°3) 'html5lib' Analyse du html, plus tolérent sur les erreurs de formatage.
"""
soup = BeautifulSoup(html, 'html.parser')
# # pretiffy() affiche le html plus facile a lire (ajout l'indentation)
# print(soup.prettify())

# ATTETION : deux fois les même méthodes sur "soup" : en snake_case et camelCase
# Privilégier le snake_case
# souvant utilisé :
#   .find("p") pour trouver la premiere balise "p"
#   .find_all("p") liste de toute les balises "p"
#   .find('body') tous le corps du site.
#   class_ <== represente la class d'une balise html. le underscore est ajouter pour ne pas confondre vec le mot clef class pour créer des classe sur python.
# articles = soup.find_all("article", class_="product_pod")
# pprint(articles)

# Exercice N°1:
# Récupérer le nom de toute les catégories sur le site.

# 1) Trouver une balise d'entrée unique pour travailler sur le DOM
aside = soup.find("div", class_="side_categories")
# 2) Descendre pour récupérer la ul qui contient tous les li
categories = aside.find("ul").find('li').find('ul')
for category in categories.children:
    if category.name:
        # Affich le text de chaque enfant
        #.strip() retire tous les espaces avant et après
        print(category.text.strip())

# Exercice n°2:
# Récupérer toute les images du site

images = soup.find('section').find_all('img')
for img in images:
    #pour récupérer l'attribut src = .get("src")
    print(img.get("src"))
