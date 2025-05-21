from bs4 import BeautifulSoup
from pprint import pprint

with open("index.html", 'r') as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')

articles = soup.find_all("article", class_="product_pod")
for article in articles:
    title = article.find("h3").find("a").get('title')
    print(title)
"""
2eme façon de faire, plus concis : Les Compréhension de liste

# Récupère tous les images avec un attribut alt.
image_tags = soup.find_all('img', alt=True)
# Je veux stocker dans un tableau chaque alt d'images POUR CHAQUE image DANS LE TABLEAU image_tags
alts = [img['alt'] for img in image_tags]
pprint(alts)

title_tags = soup.find_all('a', title=True)
titles = [a['title'] for a in title_tags]
pprint(titles)

En une seule ligne en retirant la premiere variable.
titles = [a['title'] for a in soup.find_all('a', title=True)]
"""
