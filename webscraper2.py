import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls024149810/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

soup.find('a', href=True).get_text()

movie_title = []
for title in soup.findAll('h3', {'class':'lister-item-header'}):
    titles = title.find('a', href = True).get_text()
    movie_title.append(titles)

    genre_list = []
for genre in soup.findAll('span', attrs= {'class':'genre'}):
    genre = genre.get_text()
    genre_list.append(genre.strip())

print(movie_title)


print(genre_list)
